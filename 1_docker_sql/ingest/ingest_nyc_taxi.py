import pandas as pd
from sqlalchemy import create_engine
import pyarrow.parquet as pq
import time
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    args = parser.parse_args()

    print("Reading parquet...")
    table = pq.read_table(args.file)
    df = table.to_pandas()

    print(f"Loaded {len(df)} rows")

    engine = create_engine('postgresql://postgres:postgres@localhost:5432/ny_taxi')

    print("Creating table...")
    df.head(0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')

    print("Inserting data...")
    df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append', chunksize=100_000)
    print("Done!")
