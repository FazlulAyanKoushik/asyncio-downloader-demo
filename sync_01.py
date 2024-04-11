"""
Demo for sequential way of downloading images from pexels.com
"""

import time
import requests
import os
from pathlib import Path
from typing import List, Optional


def download_file(photo_id: str, dirname:str) -> None:
    """
    Download a file from pexels.com
    :param photo_id: id of the photo to download
    :param dirname: directory where photo will be saved
    :return:
    """
    try:
        url = f"https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=640&h=480"
        print(f"Downloading {photo_id} from {url}")

        # download the file
        file_path = Path(f"{dirname}/{photo_id}.jpeg")

        # to avoid 403 forbidden error,
        # sometimes the server blocks the request if it is not from a browser or a bot is detected.
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        response = requests.get(url, headers=headers, timeout=10)

        # write the content to the file
        with open(file_path, "wb") as f:
            f.write(response.content)

        print(f"Downloaded {photo_id} to {file_path}")

    except Exception as e:
        print(f"Error downloading {photo_id}: {e}")


def download_files(photo_ids: List[str], dirname: Optional[str] = "images_01") -> None:
    """
    Download files from pexels.com
    :param photo_ids: list of photo ids to download
    :param dirname: directory where photos will be saved. Default is "images_01"
    :return:
    """

    # create the directory if it does not exist
    os.makedirs(dirname, exist_ok=True)
    for photo_id in photo_ids:
        download_file(photo_id, dirname)
        print(f"----> Downloaded {photo_id}")

    pass


if __name__ == "__main__":
    # get the list of photo ids
    with open("list_photo_ids.txt", "r") as f:
        # photo_ids = [line.rstrip() for line in f.readlines()]
        # photo_ids = f.read().splitlines()  # read the file and split the lines

        photo_ids = f.read().splitlines()

    start = time.time()

    # call download_files
    download_files(photo_ids)

    end = time.time()

    elapsed_time = end - start

    print(f"Time taken: {elapsed_time:.4f} seconds")
