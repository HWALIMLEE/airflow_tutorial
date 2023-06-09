import tempfile
import pandas as pd
from pathlib import Path
from urllib.request import urlretrieve
import logging
import zipfile

from supports.bigquery import BigQuery


def is_exists():
    bq = BigQuery()
    next_task = 'download_data_to_bigquery'
    query = f"""
            SELECT COUNT(*) AS cnt FROM `pseudolab-de4e-tutorial.de4e.movie_data` 
            """
    result = bq.client.query(query).result()
    if next(result).cnt > 0:
        next_task = 'get_movie_data'
    return next_task


def download_data_to_bigquery():
    """Fetches ratings from the given URL."""

    bq = BigQuery()
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
    bq.insert_data_to_bigquery(ratings, table_id='pseudolab-de4e-tutorial.de4e.movie_data')


def load_data_from_bigquery():
    bq = BigQuery()
    query = f"""
            SELECT * FROM `pseudolab-de4e-tutorial.de4e.movie_data` LIMIT 100
            """
    result = bq.load_data_to_dataframe(query)
    return result


def get_count_over_4() -> int:
    bq = BigQuery()
    query = f"""
            SELECT
              COUNT(*) AS cnt
            FROM (
              SELECT
                userId,
                AVG(rating) AS avg_rating
              FROM
                `pseudolab-de4e-tutorial.de4e.movie_data`
              GROUP BY
                userId
              HAVING
                avg_rating > 4)
            """
    count_result = bq.client.query(query).result()
    return next(count_result).cnt


def delete_movie_data():
    bq = BigQuery()
    query = f"""
            DELETE FROM `pseudolab-de4e-tutorial.de4e.movie_data`
            WHERE TRUE
            """
    bq.client.query(query).result()