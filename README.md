# Mini Data Warehouse with PySpark, Spark SQL, and SQL Server

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Project Structure](#project-structure)
5. [Getting Started](#getting-started)
6. [ETL Process](#etl-process)
   - [Step 1: Data Ingestion (Bronze Layer)](#step-1-data-ingestion-bronze-layer)
   - [Step 2: Data Cleaning and Transformation (Silver Layer)](#step-2-data-cleaning-and-transformation-silver-layer)
   - [Step 3: Creating Enriched Tables (Gold Layer)](#step-3-creating-enriched-tables-gold-layer)
7. [Using Spark SQL](#using-spark-sql)
8. [Exporting Data to SQL Server](#exporting-data-to-sql-server)
9. [Additional Tips](#additional-tips)
10. [License](#license)

## Introduction
This project demonstrates how to build a mini data warehouse using PySpark, Spark SQL, and SQL Server. It provides an ETL (Extract, Transform, Load) pipeline that ingests raw data, cleans and transforms it, and exports enriched data to a SQL Server database.

## Prerequisites
Before getting started, ensure you have the following installed:
- Python 3.8 or later
- Java Development Kit (JDK) 8 or 11
- Apache Spark
- SQL Server
- Visual Studio Code

## Installation
1. **Python & PySpark**
   - Download and install Python from [Python's official site](https://www.python.org/downloads/).
   - Install PySpark:
     ```bash
     pip install pyspark
     ```

2. **Java Development Kit (JDK)**
   - Download and install JDK 8 or 11 from [Oracle's official site](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html).
   - Set the `JAVA_HOME` environment variable to your JDK installation path.

3. **Apache Spark**
   - Download Apache Spark from [Spark's official site](https://spark.apache.org/downloads.html).
   - Extract the downloaded file and set up the environment variables:
     ```bash
     export SPARK_HOME=/path/to/spark
     export PATH=$SPARK_HOME/bin:$PATH
     ```

4. **SQL Server**
   - Download and install SQL Server from [Microsoft's official site](https://www.microsoft.com/en-us/sql-server/sql-server-downloads).

5. **Visual Studio Code**
   - Download and install Visual Studio Code from [VS Code's official site](https://code.visualstudio.com/).
   - Install the following extensions:
     - Python
     - Jupyter
     - SQL Server (mssql)

## Project Structure
Your project directory should look like this:
