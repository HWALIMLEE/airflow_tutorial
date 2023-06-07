import tempfile
import pandas as pd
from pathlib import Path
from urllib.request import urlretrieve
import logging
import zipfile


def download_data_to_bigquery():
    """Fetches ratings from the given URL."""

    url = "http://files.grouplens.org/datasets/movielens/ml-25m.zip"

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir, "download.zip")
        logging.info(f"Downloading zip file from {url}")
        urlretrieve(url, tmp_path)

        with zipfile.ZipFile(tmp_path) as zip_:
            logging.info(f"Downloaded zip file with contents: {zip_.namelist()}")

            logging.info("Reading ml-25m/ratings.csv from zip file")
            with zip_.open("ml-25m/ratings.csv") as file_:
                ratings = pd.read_csv(file_)



def get_rating_average():
    # userId 에 따른 rating 평균
    ...


def send_mail():
    ...