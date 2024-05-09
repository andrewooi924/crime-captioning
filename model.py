import shutil, os, uuid, json, csv, re, random
from typing import List, Dict, Optional
from pathlib import Path
import subprocess, requests
from label_studio_ml.model import LabelStudioMLBase
from label_studio_ml.response import ModelResponse
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

prediction = ""

class CrimeCaptioning(LabelStudioMLBase):
    """Custom ML Backend model
    """
    
    def setup(self):
        """Configure any parameters of your model here
        """
        self.set("model_version", "0.0.1")

    def predict(self, tasks: List[Dict], context: Optional[Dict] = None, **kwargs) -> ModelResponse:
        """ Write your inference logic here
            :param tasks: [Label Studio tasks in JSON format](https://labelstud.io/guide/task_format.html)
            :param context: [Label Studio context in JSON format](https://labelstud.io/guide/ml_create#Implement-prediction-logic)
            :return model_response
                ModelResponse(predictions=predictions) with
                predictions: [Predictions array in JSON format](https://labelstud.io/guide/export.html#Label-Studio-JSON-format-of-annotated-tasks)
        """
        # print(f'''\
        # Run prediction on {tasks}
        # Received context: {context}
        # Project ID: {self.project_id}
        # Label config: {self.label_config}
        # Parsed JSON Label config: {self.parsed_label_config}
        # Extra params: {self.extra_params}''')

        video_url = tasks[0]['data']['video_url'].split("/")[-1]
        print(video_url)
        prediction = self.caption(video_url)
        print("Prediction: " + prediction)

        # add caption to JSON file
        file_path = "caption.json"

        with open(file_path, "r") as json_file:
            data = json.load(json_file)

        data["data"]["video_url"] = tasks[0]['data']['video_url']
        data["data"]["caption"] = prediction

        with open(file_path, "w") as json_file:
            json.dump(data, json_file)

        json_prediction = {
            "model_version": self.get("model_version"),
            "score": 0.12,
            "result": [{
                "value": prediction
            }]
        }
        return ModelResponse(predictions=[json_prediction])

        # example for resource downloading from Label Studio instance,
        # you need to set env vars LABEL_STUDIO_URL and LABEL_STUDIO_API_KEY
        # path = self.get_local_path(tasks[0]['data']['image_url'], task_id=tasks[0]['id'])

        # example for simple classification
        return [{
            "model_version": self.get("model_version"),
            "score": 0.12,
            "result": [{
                "id": "vgzE336-a8",
                "from_name": "sentiment",
                "to_name": "text",
                "type": "choices",
                "value": {
                    "choices": [ "Negative" ]
                }
            }]
        }]
        
        return ModelResponse(predictions=[])
    
    # def fit(self, event, data, **kwargs):
    #     """
    #     This method is called each time an annotation is created or updated
    #     You can run your logic here to update the model and persist it to the cache
    #     It is not recommended to perform long-running operations here, as it will block the main thread
    #     Instead, consider running a separate process or a thread (like RQ worker) to perform the training
    #     :param event: event type can be ('ANNOTATION_CREATED', 'ANNOTATION_UPDATED')
    #     :param data: the payload received from the event (check [Webhook event reference](https://labelstud.io/guide/webhook_reference.html))
    #     """

        # use cache to retrieve the data from the previous fit() runs
        # old_data = self.get('my_data')
        # old_model_version = self.get('model_version')
        # print(f'Old data: {old_data}')
        # print(f'Old model version: {old_model_version}')

        # # store new data to the cache
        # self.set('my_data', 'my_new_data_value')
        # self.set('model_version', 'my_new_model_version')
        # print(f'New data: {self.get("my_data")}')
        # print(f'New model version: {self.get("model_version")}')

        # print('fit() completed successfully.')

    def caption(self, video_name):
        result = []
        DIR_PREFIX = str(uuid.uuid4())
        
        try:
            # Initialising connection to microsoft azure blob storage
            account_url = "https://andrewmonashfyp.blob.core.windows.net"
            default_credential = DefaultAzureCredential()
            blob_service_client = BlobServiceClient(account_url, credential=default_credential)
            container_name = "ml-vat-dataset"
            container_client = blob_service_client.get_container_client(container_name)

            # Downloading video from microsoft azure blob storage
            download_file_path = Path(f"vid_cap/input/{video_name}")
            with open(file=download_file_path, mode="wb") as download_file:
                download_file.write(container_client.download_blob(video_name).readall())

            subprocess.run("python vid_cap/demo.py", check=True)
            subprocess.run("python vid_cap/Test_Anomaly_Detector_public.py", check=True)
            subprocess.run("python vid_cap/Save_Anomaly_Clips.py", check=True)
            subprocess.run("python vid_cap/Prepare_frames.py", check=True)
            subprocess.run("python vid_cap/generate_res_feature.py", check=True)
            subprocess.run("python vid_cap/TestTagging.py", check=True)
            subprocess.run("python vid_cap/train_model.py --corpus vid_cap/Files/ucfc-vd_Corpus.pkl --ecores vid_cap/Files/Scaled_ResNeXt.npy --tag vid_cap/ucfcvd_e1000_tag_feats.npy --ref vid_cap/Files/ucfc-vd_ref.pkl --demo True --test vid_cap/saves/UCF-CAP-best.ckpt", check=True)

            # cleaning up
            frame_dir = os.listdir("vid_cap/AnomalyFrames/")
            frame_path = os.path.join("vid_cap/AnomalyFrames/", frame_dir[0])
            for file in os.listdir(frame_path):
                file_path = os.path.join(frame_path, file)
                os.remove(file_path)

        except Exception as e:
            print("Video captioning failed: " + e)
        
        finally:
            with open("vid_cap/demo_test.log", "r") as file:
                result = file.readline()
                
            return result


    def azure_auth():
        try:
            account_url = "https://andrewmonashfyp.blob.core.windows.net"
            default_credential = DefaultAzureCredential()

            print("Creating BlobServiceClient object")
            # Create the BlobServiceClient object
            blob_service_client = BlobServiceClient(account_url, credential=default_credential)

            # Create a unique name for the container
            container_name = str(uuid.uuid4())  
                    
            # Create the container
            container_client = blob_service_client.create_container(container_name)

            print("Creating local directory")
            # Create a local directory to hold blob data
            local_path = "./test"
            os.mkdir(local_path)

            print("Creating file")
            # Create a file in the local data directory to upload and download
            local_file_name = str(uuid.uuid4()) + ".txt"
            upload_file_path = os.path.join(local_path, local_file_name)

            print("Writing text to file")
            # Write text to the file
            file = open(file=upload_file_path, mode='w')
            file.write("Hello, World!")
            file.close()

            print("Creating blob client")
            # Create a blob client using the local file name as the name for the blob
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

            print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

            # Upload the created file
            with open(file=upload_file_path, mode="rb") as data:
                blob_client.upload_blob(data)

            print("\nListing blobs...")

            # List the blobs in the container
            blob_list = container_client.list_blobs()
            for blob in blob_list:
                print("\t" + blob.name)

            # Download the blob to a local file
            # Add 'DOWNLOAD' before the .txt extension so you can see both files in the data directory
            download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
            container_client = blob_service_client.get_container_client(container= container_name) 
            print("\nDownloading blob to \n\t" + download_file_path)

            with open(file=download_file_path, mode="wb") as download_file:
                download_file.write(container_client.download_blob(blob.name).readall())

            # Clean up
            print("\nPress the Enter key to begin clean up")
            input()

            print("Deleting blob container...")
            container_client.delete_container()

            print("Deleting the local source and downloaded files...")
            os.remove(upload_file_path)
            os.remove(download_file_path)
            os.rmdir(local_path)

            print("Done")
        except Exception as e:
            print("Failed")