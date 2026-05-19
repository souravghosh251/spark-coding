# Spark Coding Concepts

## What is Apache Spark?

Apache Spark is a unified compute engine and a set of libraries for parallel data processing on large-scale datasets.

---

## What is Unified in Spark?

“Unified” means Spark provides a single platform where different types of data processing tasks can be performed together using one engine.

It allows:

- Data Engineers to build ETL pipelines
- Data Analysts to perform SQL queries and analytics
- Data Scientists to build Machine Learning models

—all within the same ecosystem.

---

## Features of Apache Spark

- Fast in-memory processing
- Distributed computing
- Fault tolerant
- Scalable
- Supports multiple programming languages:
  - Python (PySpark)
  - Scala
  - Java
  - SQL

---

## Spark Components

| Component | Purpose |
|-----------|----------|
| Spark Core | Basic execution engine |
| Spark SQL | SQL and structured data processing |
| Spark Streaming | Real-time stream processing |
| MLlib | Machine Learning |
| GraphX | Graph processing |

---

## Why Use Spark?

- Handles Big Data efficiently
- Faster than traditional Hadoop MapReduce
- Supports real-time and batch processing
- Easy integration with cloud and data platforms

---

## Example Use Cases

- ETL Pipelines
- Real-Time Log Processing
- Recommendation Systems
- Fraud Detection
- Data Analytics Dashboards

---

## Simple Definition

> Apache Spark is a unified analytics engine used for fast and parallel processing of large-scale data.

---

# Theory Continued

# Database Concepts

## What is a Database?

A Database is an organized collection of data that can be stored, managed, and retrieved efficiently.

It is used to store application data such as:

- Employee records
- Customer details
- Orders and transactions
- Banking data
- Product information

---

## Types of Databases

| Database Type | Example |
|---------------|----------|
| Relational Database (RDBMS) | Oracle, MySQL, PostgreSQL |
| NoSQL Database | MongoDB, Cassandra |
| Cloud Database | BigQuery, Snowflake |

---

## Popular Databases

### Oracle
- Enterprise-level relational database
- Highly secure and scalable
- Mostly used in banking and large organizations

### MySQL
- Open-source relational database
- Lightweight and easy to use
- Commonly used in web applications

### PostgreSQL
- Advanced open-source relational database
- Supports complex queries and analytics
- Widely used in Data Engineering

---

## What is Tabular Format?

Data stored in rows and columns is called tabular format.

Example:

| emp_id | name  | salary |
|--------|-------|--------|
| 101 | Sourav | 50000 |
| 102 | Rahul | 60000 |

Here:
- Rows represent records
- Columns represent attributes

---

## File Formats in Data Engineering

| Format | Description |
|--------|-------------|
| CSV | Comma-separated text file |
| JSON | Semi-structured data format |
| Parquet | Columnar storage format used in Big Data |
| Avro | Row-based compact storage |
| ORC | Optimized format for Hadoop workloads |

---

## Difference Between File and Database

| File | Database |
|------|-----------|
| Stores raw data | Stores structured data |
| Limited scalability | Highly scalable |
| No query optimization | Supports indexing and optimization |
| Example: CSV file | Example: MySQL |

---

## Simple Definition

> A Database is a system used to store, manage, and retrieve structured data efficiently.


## 3 V's of Big Data

Big Data is commonly characterized by the **3 V’s**:

| V | Meaning | Explanation |
|---|----------|-------------|
| Volume | Huge Amount of Data | Massive quantities of data generated from social media, applications, sensors, transactions, etc. |
| Velocity | Speed of Data Generation | Data is generated and processed very fast, sometimes in real-time. |
| Variety | Different Types of Data | Data comes in multiple formats such as structured, semi-structured, and unstructured data. |

---


