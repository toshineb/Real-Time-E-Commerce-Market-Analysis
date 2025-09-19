# Real-Time E-Commerce Market Analysis

**Azure | Databricks | Power BI | Event Hub | Delta Lake**

---

## 📌 Project Overview
**Dashboard** 
   ![Dashboard](Screenshot%202025-09-19%20124649.png)

This project simulates a **real-world data engineering and analytics solution** where raw e-commerce transactions are streamed, cleaned, enriched, aggregated, and then visualized for **market and customer analysis**.

It showcases mastery across:

* **Cloud-scale streaming (Azure Event Hubs + Databricks)**
* **Data Lakehouse architecture (Bronze → Silver → Gold layers)**
* **Data storytelling with Power BI dashboards**

👉 The purpose is to help decision-makers **improve conversions, optimize marketing spend, and track regional performance in real time**.

---

## ⚙️ Architecture

```
Orders Generator → Azure Event Hub → Databricks (Bronze → Silver → Gold) → Power BI
```

* **Synthetic Orders Streaming**: Python `generate_orders.py` pushes realistic U.S. e-commerce transactions into **Azure Event Hub**.&#x20;
* **Bronze Layer**: `Stream_orders_to_bronze.py` ingests raw JSON into Delta Lake (raw, unmodified).&#x20;
* **Silver Layer**: `Cleaned_values_silver.py` applies cleaning, deduplication, enrichment (calculates `total_amount`, handles nulls, filters for USA orders).&#x20;
* **Gold Layer**: `Aggregated_to_gold.py` produces state-level, time-windowed KPIs (sales + items sold per minute).&#x20;
* **Power BI**: Connects to curated Gold tables for dashboards that tell the business story.

---

## 🗂️ Data Pipeline Details

### 🟤 Bronze Layer – Raw Ingestion

* Ingest JSON from Event Hub via Kafka connector.
* Schema applied for structured ingestion.
* Stores in **Delta Lake** for durability.

### ⚪ Silver Layer – Clean & Enrich

* Convert `timestamp` to proper datetime.
* Handle missing values (`price`, `quantity`).
* Compute `total_amount` = `price × quantity`.
* Deduplicate on `order_id`.
* Filter for valid U.S. state-level data.

### 🟡 Gold Layer – Aggregated Metrics

* Aggregates **real-time KPIs per state per minute**:

  * `total_sales`
  * `total_items`
* Supports Power BI visuals for **regional sales comparisons**.

---

## 📊 Power BI Analysis (Screenshots Provided)

The dashboards are structured into **four perspectives**, each answering a leadership-level business question:

1. **Executive Overview**

   * KPIs: Revenue, Orders, Conversion %, Avg Rating.
   * Provides instant visibility into company health.

2. **Conversion Analysis**

   * Funnel chart (View → Click → Purchase).
   * Conversion % trendlines across time.
   * Spotlights drop-off points and winning products.

3. **Social Engagement**

   * Views vs Clicks vs Likes trendline.
   * Content type comparisons (Social Media, Blog, Video).
   * Heatmap of engagement per product × month.

4. **Customer Sentiment & Reviews**

   * Average rating trend vs. time.
   * Sentiment buckets (Positive, Neutral, Negative).
   * Bubble chart mapping review volume × sentiment × product → exposes at-risk categories.

---

## 🎯 Business Value

* **Conversion Optimization** – Pinpoint where customers exit the funnel.
* **Marketing ROI** – Distinguish between engagement “vanity metrics” vs. conversion-driving content.
* **Product Insights** – Identify high-price, low-review products for targeted campaigns.
* **Customer Satisfaction** – Sentiment analysis reveals hidden dissatisfaction before ratings collapse.
* **Regional Strategy** – State-level aggregation enables targeted promotions & inventory allocation.

---

## 🛠️ How to Run

### Prerequisites

* Azure Subscription (Event Hub, Data Lake Storage, Databricks)
* Power BI Desktop / Service
* Python packages: `faker`, `kafka-python`, `pyspark`

### Steps

1. **Generate Orders**: Run `generate_orders.py` to push events to Event Hub.
2. **Ingest to Bronze**: Deploy `Stream_orders_to_bronze.py` on Databricks.
3. **Clean to Silver**: Run `Cleaned_values_silver.py` to enforce data quality.
4. **Aggregate to Gold**: Run `Aggregated_to_gold.py` for state-level KPIs.
5. **Visualize in Power BI**: Connect Power BI to Gold tables and build dashboards (screenshots included).

---

## 📂 Repository Structure

```
├── Streaming_Pipeline/
│   ├── generate_orders.py
│   ├── Stream_orders_to_bronze.py
│   ├── Cleaned_values_silver.py
│   ├── Aggregated_to_gold.py
│
├── Visuals/
│   └── PowerBI_Dashboard_Screenshots/
│
└── README.md
```

---

## 🔮 Future Enhancements

* Deploy enriched reviews with **NLP sentiment analysis** (e.g., VADER or transformer models).
* Add **real-time dashboards** in Power BI using push datasets.
* Integrate **Azure Synapse** for ad-hoc SQL queries.
* Introduce **data quality checks** with Great Expectations.

---

## ✅ Key Takeaway

This project demonstrates the **full lifecycle of modern analytics**:

* **Engineering discipline** with a Bronze–Silver–Gold architecture.
* **Real-time business KPIs** through Databricks Delta streaming.
* **Storytelling dashboards** that highlight opportunities, risks, and actions.

It’s a showcase of how to bridge **data engineering, analytics, and business decision-making**—skills that employers look for in top-tier data analysts.

---
