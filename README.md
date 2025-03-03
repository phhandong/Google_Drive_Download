<h2 align="center"> Google Drive Download Tool
</h2>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
![Stars](https://img.shields.io/github/stars/phhandong/Google_Drive_Download?style=flat)
[![GitHub Issues](https://img.shields.io/github/issues/phhandong/Google_Drive_Download)](https://github.com/phhandong/Google_Drive_Download/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/phhandong/Google_Drive_Download)](https://github.com/phhandong/Google_Drive_Download/pulls)
[![License](https://img.shields.io/github/license/phhandong/Google_Drive_Download)](/LICENSE)

</div>

---

- 😡🤬🥵 Are you anxious about downloading the big files from the google drive?
- 😫😖😨 Do you want a cross platform (Linux/Windows) download tool for downloading tool for fetch files in a stable way?
- 🙀😿😾 Have you experienced the anxiety when downloading a lot of data but be noticed "Too many users have viewed or downloaded"?

Then this Tool is **ALL YOU WANT**

# 🔧 Usage

## Preparing

1. Visit the Google Cloud Console https://console.cloud.google.com/
2. Create a new project ![image](https://github.com/user-attachments/assets/7505b31e-957a-4560-9bcb-15d435d576d7)
3. Enable the "Google Drive API" ![image](https://github.com/user-attachments/assets/84ed6bcc-4328-4add-8ec6-8f251be15da1)
4. Create a OAuth2.0 Credentails

- Visit the APIs&Service -> Credentials, press CREATE CREDENTIALS and choose OAuth client ID ![w_20250302195421](https://github.com/user-attachments/assets/c106e795-3819-42d2-9e19-faf8558c4fca)
  and select a type you want (typecally 'Desktop app')
- Now you can get your Client ID and Client Secret ![image](https://github.com/user-attachments/assets/4b650cbe-ffeb-4567-87b0-4aa736f0f1ee)
- If you haven't agreed the OAuth consent screen, you have to config your settings first ![image](https://github.com/user-attachments/assets/51d65e87-78c1-4d80-b6be-b76167283eb1)
- Enable the Google Driver in the API Library ![image](https://github.com/user-attachments/assets/e9c9bedb-b49f-4ad2-b734-3ae468e3b5c7)
- Add your account into the test users ![image](https://github.com/user-attachments/assets/d50f9916-4246-4c1d-b184-6fb324ae808b)
- Authorize your account to this Client, Replace the CLIENT ID with yours in this URL and get the AUTHORIZATION_CODE https://accounts.google.com/o/oauth2/v2/auth?scope=https://www.googleapis.com/auth/drive&access_type=offline&include_granted_scopes=true&response_type=code&client_id=YOUR_CLIENT_ID&redirect_uri=urn:ietf:wg:oauth:2.0:oob
- **Do not close the page** and paste the AUTHORIZATION_CODE into **get_fresh.sh**, then you will get you **Refresh Token** and **Access Token**. Please note that, the **Access Token** will be expired in 1 hour but **Refresh Token** can last long, so that's why we need update the **Access Token** while downloading.

5. For now, you've got every token you need before download from your google driver

## 🚀 Run the download tool

1. Replace your API Tokens in download.sh
2. Replace `FOLDER_ID` with the folder/file ID, take 'https://drive.google.com/file/d/1Nca0w_sNB5lAMY1Oh9iXvdc1K2H_AC8r/view?usp=drive_link' for example, the file ID is '1Nca0w_sNB5lAMY1Oh9iXvdc1K2H_AC8r'

## 👯‍♂️ Contribution

**Any** issue and PR are welcomed!.

## 📃 License

`MIT`

## ❤️ Acknowledgement

- [google-ads-python](https://github.com/googleads/google-ads-python)
- [gdown](https://github.com/wkentaro/gdown)
