# End-to-End Data Engineering Portfolio – Summer 2026 Internships  
**Abiral Pokhrel** | Freshman Data Engineer | abiralpokhrel@edu (or your email) | [LinkedIn](https://linkedin.com/in/abiralpokhrel)  

🔥 **Built live during Nov 2025 – Jan 2026** using Data Engineering Zoomcamp 2026 cohort.  
🚀 **Target: Remote DE Intern @ Databricks, Snowflake, Rippling, Meta, Google, etc.**  
💼 **Skills in progress:** Python (ETL), SQL (advanced), Airflow, PySpark, dbt, Docker, GCP/BigQuery, Kafka streaming.  

## Mega Project: Personal + Public Data Warehouse (Evolving Weekly)
**Core Pipeline:** NYC Taxi + Personal Data (Spotify/Strava) → Batch/Streaming ETL → Analytics Dashboard  
- **Ingestion:** APIs/Parquet → Dockerized PostgreSQL  
- **Orchestration:** Airflow DAGs (scheduled daily)  
- **Transformation:** PySpark + dbt (star schema, SCD2)  
- **Storage:** BigQuery (partitioned/clustered)  
- **Serving:** Looker Studio dashboard (live metrics)  
- **Deployment:** Docker + GCP free tier  
- **Live Demo:** [Coming Week 3 – Streamlit app]  

**Architecture (Week 1):**  
![Week 1 Diagram](architecture_diagrams/week1-docker-sql.png) *(Adding draw.io diagrams weekly)*  

### Progress Log
| Week | Focus | Status | Key Commit |
|------|--------|--------|------------|
| 1 (Nov 18–24) | Docker + SQL + NYC Taxi Ingest | ✅ In Progress | [Commit Link](https://github.com/abiralpokhrel-learns/de-internship-2026/commit/abc123) |
| 2 | Airflow + GCP | ⏳ | - |
| ... | ... | ... | ... |

**Run Locally:**  
1. `docker compose up -d` (in `1_docker_sql/`)  
2. Download [NYC Taxi Parquet](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet)  
3. `python ingest/ingest_nyc_taxi.py --file yellow_tripdata_2023-01.parquet`  
→ Loads ~2.8M rows into pgAdmin (localhost:8080).  

**Weekly Updates:** Follow my 8-week plan – new commits every day. Questions? DM on LinkedIn or check #de-zoomcamp Slack.  

*Last updated: Nov 19, 2025*
