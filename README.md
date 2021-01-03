# DWH ETL project

## Installation and execution
In order to run this project it is necessary to have installed python locally and to have a properly set AWS account. 

Execute the file create_tables.py to create the staging tables and analytical tables into the previously created Redshift cluster. 

After table creation, execute etl.py to extract transform and load data into the Redshift cluster. 

## Motivation
This project implements an ETL between an S3 data storage and a Redshift Datawarehouse. 

The tables created into the Redshift cluster follow the star schema 
data model with 4 dimensions tables and 1 fact table to let an hypotetic analytics team perform data analysis. 

## Details

Data Warehouse Configurations:
- Create AWS account
- Create IAM role and add "AmazonS3ReadOnlyAccess" policy to the new role to allow reading S3 data
- Create security group to allow correct access to Redshift cluster
- Create Redshift Cluster, link it to correct security group and IAM role
- Take note of necessary configuration information to use into dwh.cfg file

The source datasets are public datasets available at "s3a://udacity-dend/". Data are copied from S3 to staging tables in Redshift cluster and then manipulated
to remove duplicate rows and correctly insert them in the analytical tables. Additional quality checks can be implemented (checks on null values on some columns,
remove rows presenting duplicates on PRIMARY KEYS)

## File Description 
```create_tables.py```: it contains the functions necessary to create the empty tables and load the data from the S3 source buckets into the Redshift clusters

```sql_queries.py```: it is used by create_tables to drop and create the tables on the DWH and to copy data from S3 into Redshift's staging tables

```etl.py```: it contains the functions necessary to tranform and load the data from the staging tables to the 5 final analytical tables onto the Redshift cluster

## Acknowledgements
Udacity provided the course material necessary to implement the project
