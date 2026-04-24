# Olist E-commerce RFM Analysis 

## Overview
This project provides a professional **RFM (Recency, Frequency, Monetary) Analysis** of the Olist e-commerce dataset. It helps in customer segmentation, allowing businesses to identify high-value customers, churn risks, and loyalty patterns.

## Features
- **Data Preprocessing**: Cleaned and aggregated Olist order data.
- **RFM Scoring**: Applied `qcut` to categorize customers into segments (Champions, Hibernating, etc.).
- **Interactive Dashboard**: Built using **Streamlit** with real-time filtering, treemaps, and revenue analysis.

## Project Structure
- `dataset/`: Contains the raw e-commerce data.
- `notebook/`: Contains the Jupyter analysis code and `app.py`.
- `outputs/`: Stores generated visualizations.

## How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Launch dashboard: `streamlit run notebook/app.py`
