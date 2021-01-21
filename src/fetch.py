#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os, pickle
import json

from pprint import pprint

import google_auth_oauthlib.flow
import google.auth.transport.requests
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

# TODO: Parameterise this for multiple playlists or channel IDs

CHANNEL_ID = "UCcX7pakiWyBvFq15Vtb87wg"
PLAYLIST_ID = "PLiHBUcQP9Nl4zO7cekAzFS-FU0fi3A3Gr"


def youtube_auth():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = ".client_secret.json"

    # Get credentials and create an API client
    credentials = None
    if os.path.exists(".token.pickle"):
        with open(".token.pickle", "rb") as token:
            credentials = pickle.load(token)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            request = google.auth.transport.requests.Request()
            credentials.refresh(request)
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, scopes
            )
            credentials = flow.run_console()
        with open(".token.pickle", "wb") as token:
            pickle.dump(credentials, token)
    return googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials
    )


def main():
    youtube = youtube_auth()
    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=PLAYLIST_ID,
        maxResults=250,
    )
    response = request.execute()
    items = response.pop("items")
    pprint(response)
    while "nextPageToken" in response:
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=PLAYLIST_ID,
            maxResults=250,
            # type="video",
            # channelId=CHANNEL_ID,
            # publishedAfter="2020-12-01T00:00:00Z",
            pageToken=response["nextPageToken"],
        )
        response = request.execute()
        print(len(response["items"]))
        items += response.pop("items")
        print(len(items))
        pprint(response)
    print("=" * 80)
    print(f"Total items: {len(items)}")
    items.reverse()
    with open("results.json", "w") as results_file:
        json.dump(items, results_file, indent=2)


if __name__ == "__main__":
    main()
