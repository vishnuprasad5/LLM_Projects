# Virtual Database Assistant & Database Management System

## Overview

This project comprises two main components: a Virtual Database Assistant and a Database Management System. The Virtual Database Assistant leverages language models to interpret natural language questions and translate them into SQL queries to retrieve data from the database. Conversely, the Database Management System facilitates functionalities such as updating stock, sales, discounts, and adding new products to the database.

## Virtual Database Assistant

### Methods and Libraries Used
- Language Model: Google Generative AI (LLM)
- LangChain Community SQLDatabase
- SQL Query Execution: LangChain Experimental SQLDatabaseChain
- Embeddings: HuggingFace Embeddings
- Vector Stores: FAISS
- Few-shot Learning
- User Interface: Streamlit

### Functionality
Users can pose questions in natural language, which are then converted into SQL queries by the assistant. These queries are executed to retrieve answers from the database.

https://github.com/vishnuprasad5/LLM_Projects/assets/132830156/95a96f77-478c-4353-b71b-1a0c2a826ad9

### Sample Questions
- Determine the percentage of revenue contributed by the laptop category to the total revenue.
- Which accessory has the highest total sales revenue?
- Can you list laptops that haven't been sold yet?
- Which brand's item achieved the highest sales volume?
- How much percentage of revenue contributed by 8GB RAM phones to total sales revenue?

## Database Management System

### Methods and Libraries Used
- Web Framework: Flask
- Database Connection: MySQL Connector
- Frontend: HTML, CSS, JavaScript

### Functionality
The Database Management System offers the following features:
- Update Stock: Modify the stock quantity of existing products.
- Update Sales: Update sales records for products.
- Update Discount: Adjust discount rates for products.
- Add New Product: Incorporate new products into the database.
