'''
=================================================
Milestone 3

Nama  : Nindia Ekasuci Larasati
Batch : FTDS-030-HCK

Program ini dibuat untuk melakukan automatisasi transform dan load data dari PostgreSQL ke ElasticSearch. 
Adapun dataset yang dipakai adalah dataset mengenai Penjualan Baju Snitch periode tahun 2023 - 2025.
=================================================
'''

import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.models import Variable
from elasticsearch import Elasticsearch

default_args= {
    'owner': 'Nindia Ekasuci Larasati',
    'start_date': datetime(2024, 11, 1)
}

with DAG(
    'etl_csv_files',
    description='from local to postgres',
    schedule_interval='10-30 9 * 11 6',
    default_args=default_args, 
    catchup=False) as dag:

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    @task()
    def extract():
        """
        Extract task:
        Mengambil data mentah dari PostgreSQL (table_m3),
        kemudian menyimpannya ke dalam file CSV
        'P2M3_Nindia_Ekasuci_data_raw.csv'.
        Tahap ini merupakan proses Extract dalam ETL.
        """
        database = "airflow"
        username = "airflow"
        password = "airflow"
        host = "postgres"

        postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"
        engine = create_engine(postgres_url)
        conn = engine.connect()

        df = pd.read_sql('select * from table_m3', conn)
        df.to_csv('/opt/airflow/dags/P2M3_Nindia_Ekasuci_data_raw.csv', index=False)
        print("Success INSERT")


    @task()
    def preprocess_data():
        """
        Preprocess task:
        Membersihkan data mentah dengan beberapa langkah:
        - Normalisasi nama kolom (lowercase).
        - Menyamakan nama kolom diskon.
        - Menghapus data duplikat.
        - Konversi kolom order_date ke datetime.
        - Menangani nilai negatif pada units_sold dan sales_amount.
        - Menangani missing value (mean/mode/drop).
        - Mengatur batas diskon maksimum (0–0.7).
        Hasil preprocessing disimpan ke 'data_clean.csv'.
        """
        df = pd.read_csv('/opt/airflow/dags/P2M3_Nindia_Ekasuci_data_raw.csv')
        df.columns = df.columns.str.lower()

        if 'Discount_%' in df.columns:
            df.rename(columns={'Discount_%': 'discount'}, inplace=True)
        elif 'discount_%' in df.columns:
            df.rename(columns={'discount_%': 'discount'}, inplace=True)
        elif 'discount_' in df.columns:
            df.rename(columns={'discount_': 'discount'}, inplace=True)

        df.drop_duplicates(inplace=True)
        df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce',
                                        infer_datetime_format=True, dayfirst=True)
        df["units_sold"] = df["units_sold"].abs()
        df["sales_amount"] = df["sales_amount"].abs()
        df['units_sold'].fillna(df['units_sold'].mean(), inplace=True)
        df['unit_price'].fillna(df['unit_price'].mean(), inplace=True)
        df['discount'].fillna(df['discount'].mean(), inplace=True)
        df.dropna(subset=['order_date'], inplace=True)
        df['segment'].fillna(df['segment'].mode()[0], inplace=True)
        df['discount'] = df['discount'].clip(lower=0, upper=0.7)

        print("Preprocessed data is Success")
        df.to_csv('/opt/airflow/dags/P2M3_nindia_ekasuci_data_clean.csv', index=False)


    @task()
    def transform():
        """
        Transform task:
        Membuat kolom baru 'unique_id' sebagai gabungan dari order_id dan customer_name,
        untuk dijadikan identifier unik tiap baris.
        Data hasil transformasi disimpan ke 'data_transformed.csv'.
        """
        df = pd.read_csv('/opt/airflow/dags/P2M3_nindia_ekasuci_data_clean.csv')
        df['unique_id'] = df['order_id'].astype(str) + "_" + df['customer_name'].astype(str)

        print("Transform data Success")
        df.to_csv('/opt/airflow/dags/P2M3_nindia_ekasuci_data_transformed.csv', index=False)


    @task()
    def load():
        """
        Load task:
        Membaca data hasil transformasi dan mengirimkannya ke Elasticsearch
        dengan index 'clothing_sale'. Data kemudian dapat divisualisasikan di Kibana.
        """
        es = Elasticsearch("http://elasticsearch:9200")
        print(es.ping())

        df = pd.read_csv("/opt/airflow/dags/P2M3_nindia_ekasuci_data_transformed.csv")

        for i, row in df.iterrows():
            res = es.index(index="clothing_sale", id=i+1, body=row.to_json())

    # pipeline ETL
    start >> extract() >> preprocess_data() >> transform()>> load() >> end