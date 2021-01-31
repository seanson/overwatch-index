import os

import google_auth_oauthlib.flow
import google.auth.transport.requests
import googleapiclient.discovery
import googleapiclient.errors

# TODO: Given YouTube requires a stateful client init this probably merits a helper class
def youtube_auth_apikey():
    api_service_name = "youtube"
    api_version = "v3"
    developerKey = os.environ.get("GOOGLE_API_KEY")
    return googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=developerKey
    )

def fetch_playlist_items(youtube, playlist_id, max_results=250):
    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=250,
    )
    response = request.execute()
    items = response.pop("items")
    while "nextPageToken" in response:
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=max_results,
            pageToken=response["nextPageToken"],
        )
        response = request.execute()
        items += response.pop("items")
    return items


""" Leaving this code here as an option for when the site is transitioned to a backend, use developer key for now """
# SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
# def youtube_auth_oauth():

#     # Disable OAuthlib's HTTPS verification when running locally.
#     # *DO NOT* leave this option enabled in production.
#     os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

#     api_service_name = "youtube"
#     api_version = "v3"
#     client_secrets_file = ".client_secret.json"

#     # # Get credentials and create an API client
#     credentials = None
#     if os.path.exists(".token.pickle"):
#         with open(".token.pickle", "rb") as token:
#             credentials = pickle.load(token)
#     if not credentials or not credentials.valid:
#         if credentials and credentials.expired and credentials.refresh_token:
#             request = google.auth.transport.requests.Request()
#             credentials.refresh(request)
#         else:
#             flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
#                 client_secrets_file, SCOPES
#             )
#             credentials = flow.run_console()
#         with open(".token.pickle", "wb") as token:
#             pickle.dump(credentials, token)

#     return googleapiclient.discovery.build(
#         api_service_name, api_version, credentials=credentials
#     )
