import os
import requests
import json
import subprocess
import time
import argparse

# Function to get a new access token using the refresh token
def get_access_token():
    url = "https://oauth2.googleapis.com/token"
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": REFRESH_TOKEN,
        "grant_type": "refresh_token"
    }
    response = requests.post(url, data=data, verify=False, proxies={})
    response_data = response.json()
    
    # Debugging: Print the response
    print("Access token response:", response_data)
    
    return response_data.get("access_token")



# Function to download files from Google Drive using curl
def download_file(file_id, file_name, retries=3):
    global  ACCESS_TOKEN
    url = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    local_retries = retries
    
    for attempt in range(local_retries):
        try:
            # Use curl to download the file
            curl_command = ["curl", "-H", f"Authorization: Bearer {ACCESS_TOKEN}", "-C", "-", url, "-o", file_name]
            process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            
            # Real-time output of curl command
            for line in process.stdout:
                print(line, end="")
            
            process.wait()
            if process.returncode == 0:
                local_retries = retries
                return
            else:
                raise subprocess.CalledProcessError(process.returncode, curl_command)
        except subprocess.CalledProcessError as e:
            print(f"Error downloading {file_name}: {e}")
            if attempt < retries - 1:
                print(f"Retrying... ({attempt + 1}/{retries})")
                time.sleep(2)
                ACCESS_TOKEN = get_access_token()
            else:
                print(f"Failed to download {file_name} after {retries} attempts")

# Function to recursively download files and folders
def download_folder(parent_id, parent_path, retries=3):
    global ACCESS_TOKEN
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    url = f"https://www.googleapis.com/drive/v3/files?q='{parent_id}'+in+parents&fields=files(id,name,mimeType)"
    local_retries = retries
    for attempt in range(local_retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            response_data = response.json()
            
            # Debugging: Print the response
            print("Response:", response_data)
            
            for file in response_data.get("files", []):
                file_id = file["id"]
                file_name = file["name"]
                file_path = os.path.join(parent_path, file_name)
                
                # Check if the file is a folder or a file
                if file["mimeType"] == "application/vnd.google-apps.folder":
                    os.makedirs(file_path, exist_ok=True)
                    print("Created directory:", file_path)
                    download_folder(file_id, file_path)
                else:
                    download_file(file_id, file_path)
                    print("Downloaded:", file_path)
            local_retries =  retries
            return
        except requests.RequestException as e:
            print(f"Error fetching folder {parent_id}: {e}")
            if attempt < retries - 1:
                print(f"Retrying... ({attempt + 1}/{retries})")
                time.sleep(2)
                ACCESS_TOKEN = get_access_token()
            else:
                print(f"Failed to fetch folder {parent_id} after {retries} attempts")


if __name__ == '__main__':
  args = argparse.ArgumentParser()
  args.add_argument("--FOLDER_ID", help="Google Drive folder ID")
  args.add_argument("--CLIENT_ID", help="Google Client ID")
  args.add_argument("--CLIENT_SECRET", help="Google Client Secret")
  args.add_argument("--REFRESH_TOKEN", help="Google Refresh Token")
  args.add_argument("--OUTPUT_DIR", default='./', help="Directory to Download Files")
  args = args.parse_args()
  
  FOLDER_ID = args.FOLDER_ID
  CLIENT_ID = args.CLIENT_ID
  CLIENT_SECRET = args.CLIENT_SECRET
  REFRESH_TOKEN = args.REFRESH_TOKEN
  OUTPUT_DIR = args.OUTPUT_DIR
  ACCESS_TOKEN = get_access_token()
  download_folder(FOLDER_ID, OUTPUT_DIR)