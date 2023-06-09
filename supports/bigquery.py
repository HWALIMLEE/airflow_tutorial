from google.cloud import bigquery


class BigQuery:
    def __init__(self):
        self._client = bigquery.Client()

    @property
    def client(self):
        return self._client

    def insert_data_to_bigquery(self, dataframe, table_id):
        table = self._client.get_table(table_id)
        self._client.load_table_from_dataframe(
            dataframe, table
        )

    def load_data_to_dataframe(self, query):
        return self._client.query(query).to_dataframe()
