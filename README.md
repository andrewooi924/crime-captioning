
# End User Guide

This comprehensive end user guide covers everything needed to eectively utilise the machine learning assisted video
annotation tool, including detailed instructions and step-by-step guidance on how to import your own videos, perform
video captioning and evaluate the outputted caption.

## Running with Docker (Recommended)

### 1. Setting up Label Studio

In this section, we will first be setting up Label Studio and creating two projects, each required for video captioning and caption evaluating respectively.

#### 1.1 Starting up and Closing the Label Studio Instance

##### With Command Prompt
1. To start up Label Studio, open up **Docker Desktop** and your **Command Prompt**
2. Run the command
```bash
docker run -it -p 8080:8080 -v %cd%/mydata:/label-studio/data heartexlabs/label-studio:latest label-studio --log-level DEBUG
```
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfDZj2jrprL4_3xbKwbFHU_KVqvVMu6w0l7CqKC8qwcMzMXS--mXFmvaFJQVvaPuEJX4cB-QsUf7sDLh8lsKYTT_o-lNvAJlFvrp4vtPswgnw9lpCOhWTppZsSjGX40S1PTyDIBs1je5JzpXbw0B012LFw?key=aJAMiN2pWmOeIr7IPgSyVA)**
3. To close Label Studio, you can press the **CTRL** and **C** keys on your keyboard together in the console to close it. The browser window can be closed at any time.


##### With Windows Powershell
1. To start up Label Studio, open up your **Windows Powershell**
2. Run the command
```bash
docker run -it -p 8080:8080 -v ${PWD}/mydata:/label-studio/data heartexlabs/label-studio:latest label-studio --log-level DEBUG
```
3. To close Label Studio, you can press the **CTRL** and **C** keys on your keyboard together in the console to close it. The browser window can be closed at any time.

##### With Docker Desktop
1. To start up Label Studio, open up your **Docker Desktop**, navigate to the **Containers** tab and start the Label Studio container.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXceJ6-qpFm8oeY73_vaDJ87UDMFLsD6gXx3RE8lUcTT5RoZGFZ3WSvKuIy6UIe0iicg-UDRnxCTjWfc7QpoD206ru_PNcVmhip-6eGb1fxQ3AiWNs78mC66NS-KxdhIgnf8vQjdNJSAVCYLig2TQRxSpWM?key=aJAMiN2pWmOeIr7IPgSyVA)**
2. Once the container is running properly, it should look like this
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdKRw_oj5xngwTkyQDyE-5nc3_JKUF1ISeqmGxuKKmuGjNV7sPqaE7gHo5qk1cZxRfivedv5fYnaEhzcymemmgIlT8V16NJ5t6JaatjjMShBYfAWI7cr-vxitPuAcsGRoAgfNMPGsJWzhchINHyxS3HIHjl?key=aJAMiN2pWmOeIr7IPgSyVA)**
3. To close Label Studio, you can press on the **Stop** button to close it.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfvEXJvZcjJN-_uF11L7hkPL7WXPV7thzDyBd0dFkz5mNFgovzviwUwr7_uiJJdjalaCqPhLyF1NSitn5ErtQFlBGxgC7TxhCzHQ8I8ybpZoZGHEv3Ep9xS-Gj_3otWYjQ4CFZiTuCLKDQ2Tp3yVmIo8PI?key=aJAMiN2pWmOeIr7IPgSyVA)**
> [!WARNING]
> If the error below is encountered, it means that your docker instance is not running as it should. Please ensure that you have **Docker Desktop** running.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeHgkBW0H40hf9Gf-k1W_XD4bs24KstpveOsHG24rUXcUEstMXq30FYiHvf7O33k4Br0WleRgzFV6EQpA7Ozb6pYJundcLoVPST4F74bQGw82c5meTG3LhD8qpD24kXeWOoXcfAlJzxyvc5V0rhp6JtWTd-?key=aJAMiN2pWmOeIr7IPgSyVA)**
#### 1.2 Accessing the Label Studio Instance
1. In the browser of your choice, you can access the Label Studio Instance through the url [http://localhost:8080](http://localhost:8080)
2. In the **SIGN UP** tab, enter your email and password to create an account
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfTDDKomrF0c929BNdj5HShL5ymDxnETRdtDpIcdV_nt70w1dXqSVDJ--uv9c8S1_RwOy5_OK1pcc83z2qNbDOM05h0ouws-fQ5bOsDK3u7es4S6BsE2jtTnZp8tQUVm5WamYiWUMmIFaFkKCVl-viFlONf?key=aJAMiN2pWmOeIr7IPgSyVA)**
3. Once signed in, the window should look like this:
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdS4lyFJQvZBQBdOgyxnNEvPgZR7U2BABjdCbsr0GHZpwM-OvqRhH-KKgfAnNnB5yBMi_cuizqj-q4lhq_PFt_cCy_Je7ZI7i_PlBOsmQjHliK2-XfOfluZ0c1-DP0FXaR3BGsgh96FRjoin379xnEbVEBa?key=aJAMiN2pWmOeIr7IPgSyVA)**

### 2. Importing videos into Label Studio
In this section, we will be understanding how to import videos into Label Studio through Microsoft Azure Blob Storage. **Please note that the model only supports .mp4 video files.**

#### 2.1 Accessing Microsoft Azure Blob Storage Containers
1. Navigate to [https://portal.azure.com/#home](https://portal.azure.com/#home), then select your storage account.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcDEjBkpkKknqqH3-lONwhsf6QDEK91pKFqPKnqY_T6rsP5U0K8kucLXL4nSDNAbJo5NxOEwghALkscbxrXaR7lNgAABYvY9G1MLImuffXXoCikYYvWva9MFumliCjzetk0hYSRJRWUrftI7XJsnQzVtm0k?key=aJAMiN2pWmOeIr7IPgSyVA)**
2. Click on the **Containers** tab in the sidebar on the left side of the page.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe_2zRh0JWWPbfRhi7OaZQvxHpBllYe-1UjYs3SeAHJ3hf9PHS5c7riNNdyzTU1l1KTyIA7zZwikvn9j-Qx-hXuoRYjpls2mrn2mFrdDmMcquJZ8UbXLdVPO0JIQ5nFEWGMS15QxUJmNEha0V4ARFr2v5Q?key=aJAMiN2pWmOeIr7IPgSyVA)**
3. Click on the blob container that you are using to store your videos.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdQ7sULRYVkdo59UKNqSqJTRjF-GXwZu3qRHOyyhwwHAOAYBzYk5M_2F_hygmuXUgWndSzHM-qx0IKMgWXTcMFVdATug_6_Q5_DhSISBpbJ9jxfYYiGPHtQZFcE2as3JxnlQX8lrUKH66Y0fyWKyLZC5EDR?key=aJAMiN2pWmOeIr7IPgSyVA)**

#### 2.2 Uploading videos to Microsoft Azure Blob Storage
1. Press the **Upload** button
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcMnC3bACY89arWUn1_tSELY3NMTmgMj9wNYxBm1y0wMHuDg6OvMWf_dIZ0mLA0H7zxp8mHbOGmtq9e-fdem6I-VPUKAF3pmp13pApYHFx-rD6JzHmTs5g5lmT6hbtKd5rgIdsgr9wY02KF3024tGHplp4?key=aJAMiN2pWmOeIr7IPgSyVA)**
2. Upload your desired videos and press the **Upload** button below.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd4V1nmamY2EXi9yxHNsCnY1DZJDG8KA_sbb3KdL973Hp7snBJRJ5uifPUV67d4KrazLjnFmVvKzCtIwY971wo1JCMkbkOWMURdNhxtuz2CZ5OgwuN2O2gnvT8v8fp6zn2iNmQ9qUeALShLetG89he1lPDP?key=aJAMiN2pWmOeIr7IPgSyVA)**

#### 2.3 Accessing Label Studio's cloud storage interface
1. In Label Studio, navigate to the project for **Captioning**.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfDDBDB1DqbohqZtpMcXGqYx9GRTDWF0lgN5WV-ukfzdq4e_NVT7553vk2f4UabW-0Qexc8oXUA6SMgHZYqxkktxruDD0HrC2guug-Q6pM0T3tAk-2aiUSBqu6kf31x_G0QcPJ2nh8oy6FtYg1O0Ntnc6eG?key=aJAMiN2pWmOeIr7IPgSyVA)**
2. Click on the **Settings** button in the top right of the page.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXetdqDc4pwEFt8R0JCnsy_pqxMoH14yv1pLCdhvOtlTUDeIlYhZESefOpQu4sBAlb7wAmaqfcc2lP-l3wmSStiBXPgV6BiR1ErBAZkpLx358C3kD7xbWo5nfP0ndlwycC8ApLiXmXdZksYJ5yaEEX2LmKIz?key=aJAMiN2pWmOeIr7IPgSyVA)**
3. Press the **Cloud Storage** button in the right sidebar.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcg9005lcrvtrPrDbiRsQkkxq-lSirJyOUVddgbh-TpVZrLVv42f59PyjFVsVg4C0utOuLxbaaFl_DeAA8gYsGWXaXZ-0Onr5OtFGMe7O7C_UtO6Aa8kDgNV7Dj_RBheWiexPHDbVVxY6gf0Ne0A01scc8C?key=aJAMiN2pWmOeIr7IPgSyVA)**

#### 2.4 Syncing Microsoft Azure Blob Storage to Label Studio
1. In the **Source Cloud Storage** section, press the **Sync Storage** button.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcvyIB_s1RbWFBeYZGUQtlCSE6SD1QiRFrL0lP-axvn_wL55VAvRCLTtqYQAAwVypf7p6M8S55oLN9tSLOJB-9PN2NDFeiaWAyx49fyrZhRkvxWNlsN864ZY5ZsrtL_lIgi_Wrs_RbzPrwXcJ0bDfrZ1Bii?key=aJAMiN2pWmOeIr7IPgSyVA)**
2. Repeat the same steps for accessing and syncing for the **Evaluating** project.

### 3. Setting up the video captioning model
#### 3.1 Starting up the conda environment
1. First, open up **Anaconda Prompt**
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcjOQNt4fnB2axP0Hgp_JA-ZV3eJ580fgxfiEC3evp5mm5suSo_qggA4GURA_8MFjy8BHpxWaJJE2NV4izhZzn-XDbdodUIH_bNdJldff6DIl-2Ot9BMHr1GY9YSfgf_ZWpgtn_QxhClwnwCeqVievNQHOS?key=aJAMiN2pWmOeIr7IPgSyVA)**
2. Access your conda environment using the command ```conda activate ENV_NAME``` where ENV_NAME is the name of your conda environment.

#### 3.2 Hosting the video captioning model
1. Navigate to the cloned GitHub repository containing the **_wsgi.py** file in your terminal.
2. To begin hosting the video captioning model, run the command python _wsgi.py -p 9090, where -p 9090 specifies the port of the model.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdbodV1LVMWGpBk---UXcyodW17IGbR2bKi0t7WZ9GSX23kLuRziQUqCb7R_avv-aqxWcBantkPhRDKiBwPKBldoVj_MLSIsnYVjKXDry1Y-QbhsyLVwLN5tyaP4xAAa-skShqN7z0PcuDrJ-UvmByamhSV?key=aJAMiN2pWmOeIr7IPgSyVA)**
3. To close the model without closing the console, press the **CTRL** and **C** keys together on your keyboard. Otherwise, you can just close the console window.
> [!NOTE]
> You can set the port number to your preferred one, as long as that port is not already being used by any other software application.

### 4. Performing video captioning
In this section, we will be performing video captioning on our desired video.

#### 4.1 Selecting a video task
In the **Captioning** project, select any video you desire. In this case, we selected the project with ID 782.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd3ckvDSsNIXzrY2GKaR_2H-RtaJSxLgwbzeftBzekxv-Cj1t5CCDCulmZc13K8XiUmSkSV2nO9e7a7rJPLBO66LAAVWx64YjfZr0a9DDQeFCIJku7bt1vRPWtMEsqft5NB2LcyWOpn4PLIs9SQ5g2W-_Ml?key=aJAMiN2pWmOeIr7IPgSyVA)**

#### 4.2 Running the video captioning model
1. The video captioning model will begin to run automatically in the console hosting the video captioning model.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfIJWNGjD0QnTaWwYFxns-1OsIHZpzFWgG6LTxfbIeXkDiKr2WVb2q08gewxm2yl0wMPAme_zWHmWp2iaCIJkXfdnMgyKIuSTczwJw5UeeKDauVSS7szJAjIGhJFlC9hf3XTgBDHRhrVDHPH3cGImZHq0Eb?key=aJAMiN2pWmOeIr7IPgSyVA)**
2. Once the video captioning model has finished running, the output should look like this:
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdLOz4CfF-NciJcgxT2vNTQvHxRJUTqBumFgLqjEVWzdPGswFsFzgYBMWiB9wEFrrccrhg9Q8K0ANkOGvvwzHtOkwPr0uz-UeJU17jX11etprfsU6Pc5Ap_c41EFdPjYifZstAXi8I2hRr2G1jOawxJR-fT?key=aJAMiN2pWmOeIr7IPgSyVA)**

#### 4.3 Accessing the outputted caption JSON file
The outputted caption JSON file can be accessed in the **crime-captioning** folder we cloned from GitHub to host the video captioning model under the filename **caption.json**.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd4lnA_CSYrSaLw4IjKopKRbajUuny0nQFVOvp9yGo019dEZGEsoe8WK1J7WWR7RJhF5BAva1N8MRlAjaE__iKK-vBB-Jd2jk2RqkYfRLJCI0JxkmsDhKuHCdjNRNtIjpkwbxgJXXf3CYJAgVg9QCQBDdY?key=aJAMiN2pWmOeIr7IPgSyVA)**

### 5. Evaluating the outputted video caption
In this section, we will be evaluating the outputted caption from the video captioning model.

#### 5.1 Importing the caption into Label Studio
1. In Label Studio, navigate to the **Evaluating** project.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc6-hId-SvoD2odKEs3hBeHQV8dzIJvXE-tRU3vaRhsjD1zWwr61xSmdTeweHmzYLQDcSmR_VWTYwwnOazFgDT09aEYGWPAzU8wQhVNwC9qUKM7j2WhLMZLhJDnAdTRMM2pYylj1jKpMnh1izmZCo9z1Tk?key=aJAMiN2pWmOeIr7IPgSyVA)**
2. Click on the **Import** button in the top right of the page.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfrvfeb2E2wrxQrz6hx77kBH_n_gfMPFuguAyKswNvUpYwYHdaB-CFvjmRzAD4en8hb_vQI1kNyQisRb4EITBsUUstHarZSD7AY_bcKUTlt3C0bz0aKgHAhLXVrDC5-YvZXT-O-bPY-2nniGaNwSBS-xu1m?key=aJAMiN2pWmOeIr7IPgSyVA)**
3. Upload the caption file **caption.json**.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeJcs8I_tNQREtiLVs5rCGHaOPUzQZ8BpQ4tL5Dy0cdHjNltTRdDVmBtEmU9SZIQUvRFq31rwR8q1WM4qwD1fQ8oE8RYOoWJsyzqDG828fIotKGb8lK6HEmMjZOQHVf4OEbQeqQCYI2G6uV5kcYHALtTbE?key=aJAMiN2pWmOeIr7IPgSyVA)**
4. Press the **Import** button in the top right to import the caption as a new task.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd74ddkMcE2qY7KUmSzPW0HDco2F3_kD6KlzGAeJZYQlBK3RXgesYh6dhkPfR3_BL0x4KfV0_2N5h1dPqqAQDHXlz0eBcJ0JXGoiCGw0XLLoKlL83hboVpPTi6a09qZZUhu7tVWThRyY9DfGoNHNAEHzPuz?key=aJAMiN2pWmOeIr7IPgSyVA)**

#### 5.2 Evaluating the caption
1. Click on the newly imported task.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcZ5BYohe7WDcqdMBivxjzs70h9FXvYFV3DvM7IHnrD6gw6_cB4YrGJScbJoDMqHwIAfoodRSR76j2TatDArC6gbPzMerO4QA9hN9quRmKcInK7nXcMMmGLrMbsPqXAvq_9hsAoxa53qKqDuoZSGXP11fJV?key=aJAMiN2pWmOeIr7IPgSyVA)**
2. You will see the imported video, the caption predicting the crime occurring in the video, along with timestamps depicting the predicted start and end time of the anomaly or crime.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfEKT4BxaBzzIHgur4_jgCr-Kx91e-PF4Eqm5BVRq4H0JEx9aldFRq5hD9_578oS4OsN0iiVBKDWKhZR9c-0yuALglSK02yQXoxS3HcAFM6jr8_QyI4bxOYOH05ApbpUWnIpbu6WxJ37EUig5eFMyg96wcR?key=aJAMiN2pWmOeIr7IPgSyVA)**
3. Below that, you can evaluate whether the caption is accurate or not.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeiVLU3am56xdkCrcEh36aMcxTaXUJW4SKZVtqHMxdOBbvXvhxaDHr99vprYyf8YCyG1-Y3qpyfruFDgA7_rIoFgiAjIRrdLdVU3Om35jYg3-Myt5hm1meLVn-N1BZuUl3bRvYEkl1tPdjDGo7-vG5pcZzc?key=aJAMiN2pWmOeIr7IPgSyVA)**
4. If it is inaccurate, a text box will pop up where you can input your own caption predicting the crime occurring in the video.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdUZvsxppaZwQWTEpsZ8jK3beawxdwYKf5oWalVwHXoYBOnbYplUzKmddJb2rEYGlG4BeNqQxVJof8UhpbYvPT_-8GC0ypC184tZA7XHZjHj12x6mv0avhFLDaWuxIMQ6UIu7w1ZtVWhI3dYJZVzUiSwC1U?key=aJAMiN2pWmOeIr7IPgSyVA)**
5. If it is accurate or you have already finished inputting your own caption for an inaccurate caption by the video captioning model, press the Submit button in the bottom right to generate the Label Studio JSON file which is the final output.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcflifKfTSMcrAS7HOSOFpRU17fMhTYX8YLl5ecAU0Y6825NyqbxfOA4hvAfWuUv8cWgqjTgTSVh_iUP8XcWcdYx4lhJO3SSUfd-5OnolEJWPz8uESLtLb0XMO5e7z4YfCCx1qr5-0cCFbfrMnA7n8waI4?key=aJAMiN2pWmOeIr7IPgSyVA)**

#### 5.3 Accessing the outputted Label Studio JSON file
1. Navigate to the **Containers** tab in Microsoft Azure Blob Storage.
2.  Click on the container which stores the output for Label Studio.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXflBEufLQBhURp8-tOygCjk8DIwacOKPsT_zYMLMbBliA8-FipWC0dtlNX-ZapvXt2TBu2v1GZ-ke40WfVypXLBD9rKPiEpMwBFsKOCOY3hpHKYOBGXbBqniMcCE_x068618jCHP0Bhj1S5FQirRaI3k4M?key=aJAMiN2pWmOeIr7IPgSyVA)**
3. Click on the latest file which should be the output for the caption you have just evaluated.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfbAi1OnkFSc4kdchFAdWrw9Y3YrQu2h-kZDDbAfG5OHUdoczfXYnZhmG_1VSzLuu08gsa7IdY9Ar_msgIrkHojFBxT1AFmKJTE1Eg-JznP__KGeFDLJmj1Yl4F3aCqbeNQrmMT1EPmq-HgQ3Ia8YyEhVW3?key=aJAMiN2pWmOeIr7IPgSyVA)**
4. Press the **Download** button to download the file.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdsCCRrJnz581tTOw1OyZwCLrVelnL52xwEBgwDdLYrDHSlVXXjlwmhs3_yh1nBcwfwgpKk9EItXBai840jRmOINfvkb8_RPR5cOOO10Q8VGnJzgFUfFdV1QAKlY5kFVC0xdzGzGnZbERx1-Hs8Y9iZJXhU?key=aJAMiN2pWmOeIr7IPgSyVA)**
5. Open up the file in a text editor of your choice, here is what the contents of the output should look like.
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcqjDK-K2qrvZroOuatwaqwUDh8n9kuilBkWVi8BcinK4HSibM2p5DFuSZa2szhOINOj43hyEY1BrYZjSG3veWAgunWfOCfUiPD4n3LOfAN6fFqOFFRd51z2rLmFkZ2fzXVK9DbpCekzKbJmNo4okf6ARw?key=aJAMiN2pWmOeIr7IPgSyVA)**
