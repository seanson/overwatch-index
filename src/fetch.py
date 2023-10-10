#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import youtube

from dotenv import load_dotenv

load_dotenv()


def main():
    client = youtube.youtube_auth_apikey()
    playlist_id = os.environ.get("PLAYLIST_ID")
    print(f"Fetching playlist ID: {playlist_id}")
    items = youtube.fetch_playlist_items(client, playlist_id)
    print(f"Found {len(items)} items from playlist")
    items.reverse()
    print("Writing output results.json")
    with open("results.json", "w") as results_file:
        json.dump(items, results_file, indent=2)


if __name__ == "__main__":
    main()
