import requests
import logging
import re


FILES_EXTENSIONS = [
    ".mp3", ".mp4"
]


def download(name: str, ext: str, url: str):
    file_path = f"downloads/{'videos' if ext == '.mp4' else 'audios'}/tmp/{name}{ext}"

    with open(file_path, "wb") as file:
        logging.info(f"Downloading {ext}...")
        response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
        if response.status_code == 200:
            file.write(response.content)
            logging.info(f"{ext} Downloaded - {file_path}")
        
    return file_path


def remove_special_chars(value: str):
    final_string = ''
    for i in value.split('\n'):
        final_string = re.sub(r"[^a-zA-Z0-9]+", ' ', i)
    return final_string