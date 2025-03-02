import requests
import json
import argparse

# Function to get refresh token and access token using the authorization code
def get_tokens(client_id, client_secret, authorization_code, redirect_uri):
    url = "https://oauth2.googleapis.com/token"
    data = {
        "code": authorization_code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }
    
    response = requests.post(url, data=data)
    
    # Print the full response for debugging
    print("Token response:", response.text)
    
    # Extract and print the refresh token and access token
    tokens = response.json()
    refresh_token = tokens.get("refresh_token")
    access_token = tokens.get("access_token")
    print("Refresh token:", refresh_token)
    print("Access token:", access_token)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get refresh token and access token using the authorization code.")
    parser.add_argument("--client_id", required=True, help="OAuth 2.0 Client ID")
    parser.add_argument("--client_secret", required=True, help="OAuth 2.0 Client Secret")
    parser.add_argument("--authorization_code", required=True, help="Authorization Code")
    parser.add_argument("--redirect_uri", required=True, help="Redirect URI")

    args = parser.parse_args()

    get_tokens(args.client_id, args.client_secret, args.authorization_code, args.redirect_uri)