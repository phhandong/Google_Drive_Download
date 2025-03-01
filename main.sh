#!/bin/bash

FOLDER_ID="FOLDER ID"
GOOGLE_API="GOOGLE API"

download_file() {
    FILE_ID=$1
    FILE_NAME=$2
    curl -H "Authorization: Bearer ${GOOGLE_API}" -C - "https://www.googleapis.com/drive/v3/files/${FILE_ID}?alt=media" -o "${FILE_NAME}"
}

download_folder() {
    PARENT_ID=$1
    PARENT_PATH=$2

    # Fetch the list of files and folders in the specified Google Drive folder
    response=$(curl -H "Authorization: Bearer ${GOOGLE_API}" "https://www.googleapis.com/drive/v3/files?q='${PARENT_ID}'+in+parents&fields=files(id,name,mimeType)")

    # Parse the response and download each file
    echo "$response" | jq -c '.files[]' | while read -r file; do
        FILE_ID=$(echo "$file" | jq -r '.id')
        FILE_NAME=$(echo "$file" | jq -r '.name')
        FILE_PATH="${PARENT_PATH}/${FILE_NAME}"

        # Check if the file is a folder or a file
        if [[ $(echo "$file" | jq -r '.mimeType') == "application/vnd.google-apps.folder" ]]; then
            mkdir -p "$FILE_PATH"
            echo "Created directory: $FILE_PATH"
            download_folder "$FILE_ID" "$FILE_PATH"
        else
            download_file "$FILE_ID" "$FILE_PATH"
            echo "Downloaded: $FILE_PATH"
        fi
    done
}

download_folder "$FOLDER_ID" "."
