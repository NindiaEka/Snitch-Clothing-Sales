# Sales and Inventory Analytics Dashboard for Fashion Supply Chain: Snitch Clothing Sales Case Study

## Repository Outline
Adapun file - file yang ada pada project kali ini adalah :

1. README.md - Penjelasan gambaran umum project
2. ddl.txt - perintah query yang akan di exsekusi pada postgres
3. airflow_ES.yaml - Berisi file untuk menyimpan konfigurasi pipeline / ETL dalam bentuk struktur data yang mudah dibaca.
4. .env - Berisi file data penting dan rahasia (seperti username, password, atau API key) supaya tidak ditulis langsung di dalam kode program.
5. P2M3_Nindia_Ekasuci_DAG.py - Program yang berisi proses ETL dengan python
6. P2M3_Nindia_Ekasuci_gx.ipynb - Notebook yang berisi validasi otomatis terhadap data menggunakan great expetations
7. P2M3_Nindia_Ekasuci_Conceptual_Problem.txt - Berisi penjelasan mengenai pemahaman dasar mengenai proses yang telah dilakukan
8. P2M3_Nindia_Ekasuci_data_raw.csv - Berisi raw data format csv 
9. P2M3_nindia_ekasuci_data_clean.csv - Berisi file data format csv yang telah dilakukan data cleaning
10. P2M3_nindia_ekasuci_data_transformed.csv - Berisi file data format csv yang telah dilakukan transformasi (penambahan unique value/primary key)
11. P2M3_Nindia_Ekasuci_DAG_graph.jpg - Berisi gambar pipeline hasil dari ETL
12. folder images - Berisi gambar hasil visualisasi di kibana 

## Problem Background
Industri fashion menghadapi tantangan seperti fluktuasi permintaan musiman, tren cepat berubah, dan gangguan rantai pasok global. Dalam konteks ini, tim inventaris dan supply chain perlu beralih dari pendekatan reaktif ke strategi proaktif berbasis data demi menjaga keseimbangan antara ketersediaan produk dan efisiensi stok. Dengan memanfaatkan data penjualan (seperti dataset Snitch Clothing Sales), perusahaan dapat meningkatkan visibilitas permintaan, merespons dinamika pasar, dan meningkatkan ketahanan rantai pasok melalui praktik modern seperti real-time tracking, predictive analytics, dan localized distribution.

## Objective (Tujuan)
- Meningkatkan akurasi forecasting permintaan, khususnya untuk kategori produk utama.
- Menurunkan frekuensi stockouts dan overstock, sehingga biaya operasional menurun.
- Meningkatkan efisiensi operasional, melalui data-driven planning dan real-time inventory monitoring.
- Meningkatkan ketahanan rantai pasok dalam menghadapi volatilitas pasar melalui proaktif planning.

## Manfaat
Bagi tim Supply Chain / Logistik, laporan ini akan sangat membantu dalam meningkatkan efisiensi distribusi, menekan biaya, mengantisipasi fluktuasi permintaan, dan menjaga ketersediaan produk sehingga rantai pasok lebih gesit dan responsif terhadap pasar.


## Project Output
Output dari project ini adalah visualisasi dari kibana yang disimpan dalam bentuk format gambar

## Data
Data yang diambil pada project kali ini adalah dataset mengenai penjualan clothes (Snitch) pada kurun waktu 2023 - 2025. Data tersebut memiliki 2500 baris dan 12 kolom. Data masih terbilang 'kotor' karena banyak memiliki missing value, banyak format data yang tidak sesuai dan penamaan pada kolom yang tidak standar.

## Method
Pada project kali ini dilakukan proses ETL menggunakan airflow dan elastic search untuk melakukan tahapan visualisasi menggunakan kibana.

## Stacks
Bahasa pemrograman dan tools :
- Python
- VS Code
- Docker
- Postgres
- Great Expetations
- Kibana

Library python yang digunakan :
- pandas
- airflow
- sqlalchemy
- elasticsearch
- great_expetations

## Reference
- [Snitch Clothing Sales](https://www.kaggle.com/datasets/nayakganesh007/snitch-clothing-sales)

- [What is Supply Chain Forecasting? Best Methods, Benefits, and Challenges](https://www.inboundlogistics.com/articles/supply-chain-forecasting/)

- [How to Improve Retail Demand Forecasting for Higher Profits](https://www.tredence.com/blog/retail-demand-forecasting)

- [Designing for disruption: How fashion brands are future-proofing fulfilment](https://www.voguebusiness.com/story/consumers/designing-for-disruption-how-fashion-brands-are-future-proofing-fulfilment)

- [5 Key Benefits of Integrating Inventory Forecasting Into Your Retail Strategy](https://hypersonix.ai/blogs/5-key-benefits-of-integrating-inventory-forecasting-into-your-retail-strategy)

- [Agrawal, S., Kumar, P., & Gupta, R. (2023). Data-driven decision making in supply chain management. International Journal of Research Publication and Reviews, 9(5), 307–314.](https://www.researchgate.net/publication/386188295_Data-driven_decision_support_system_enabling_the_circularity_of_products)

- [Christopher, M. (2016). Logistics & supply chain management (5th ed.). Harlow: Pearson Education Limited.](https://nibmehub.com/opac-service/pdf/read/Logistics%20and%20Supply%20Chain%20Management-%205th%20edition.pdf)

- [Porter, M. E. (1985). Competitive advantage: Creating and sustaining superior performance. New York: Free Press.](https://www.hbs.edu/faculty/Pages/item.aspx?num=193)




