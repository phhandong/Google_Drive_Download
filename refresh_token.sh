#!/bin/bash

CLIENT_ID="YOUR_CLIENT_ID"
CLIENT_SECRET="YOUR_CLIENT_SECRET"
AUTHORIZATION_CODE="YOUR_AUTHORIZATION_CODE"
REDIRECT_URI="urn:ietf:wg:oauth:2.0:oob"

python /c:/Users/HanDong/Desktop/get_fresh.py --client_id "$CLIENT_ID" --client_secret "$CLIENT_SECRET" --authorization_code "$AUTHORIZATION_CODE" --redirect_uri "$REDIRECT_URI"