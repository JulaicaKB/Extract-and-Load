Pipeline from excel to mysql

Overview:--
A basic ETL(Extract, Transform, Load) pipeline built using Python and MySQL. 
The pipeline:
1. Extracts data from an Excel dataset
2. Loads it into a MySQL database
3. And Verifies the successful data transfer.

Objectives--
- Extract structured data from an Excel file using Python.
- Load records into MySQL database.
- Prevent duplicate records during recurring executions.
- Verify the data load.

Technologies Used--
- Python
- Pandas
- MySQL
- MySQL Connector/Python
- OpenPyXL
- python-dotenv

Pipeline Workflow--
1. Read data from an Excel file.
2. Inspect and prepare the dataset.
3. Establish a connection to MySQL.
4. If the database and table do not exist then Create them.
5. Load the records into MySQL table.
6. Verify the number of loaded records.
7. Close the database connection.

Dataset--
- Excel dataset that contains 10,000 records and 14 columns related to sales orders, including region, country, item type, sales channel, sales, costs and profits(This is the dataset we use in my classes, and I used it here).
- Dataset name: InternshipData.xlsx

Database--
- Database name: internship_db
- Table name: ExampleData

Data Loading Strategy--
The pipeline uses a full-refresh approach. Any previous records in the target table are deleted before the dataset is reloaded to allow the script to prevent duplication of records during each execution.

Verification--
The pipeline verifies the successful load by comparing the number of records in the MySQL table against the number of records extracted from the Excel file.
