# AWS Lambda
## Things to know about Lambda

AWS Lambda is a purely compute resource that allows users to deploy code directly and not worry about infrastructure maintenance. Think of it as pushing just the python script as opposed to instantiating the EC2 and updating the OS, maintaining security patches, installing the language with dependant libraries and then running your code. Lambda does away with all of that. Just Fire and Forget.

You can find the Lambda service in the Compute section of the list of services in AWS console.

Now, where can lambda be used. One example of using Lambda is in ETL. A common and often necessary activity in entreprises is to be able to load data from databases to datawarehouses on a daily basis. This is done through the Extract Transform and Load routine. The code written to do this connects to the source database, takes all the records entered for that day , transforms the schema to match the target database and loads into the respective tables. AWS Redshift is a datawarehouse commonly used in cloud architectures to store data. Data is extracted from source databases like MongoDB and is stored in S3 as a flat file also called a text file which triggers a EC2 containing the ETL code to load the data into redshift. 

The new way of doing the routine would be to set a trigger for the moment new data is stored in S3 , the trigger launches the code deployed in a Lambda function that connects to S3 and redshift and transforms and loads data into the target tables. The advantage: Cost. With Lambda one does not have to deal with EC2 instance costs and maintenances. 

Lambda is pretty inexpensive, while you will get billed for a minimum of 100ms regardless of the actual runtime. The cost for running a Lambda function is low enough to make economic sense for the industry to explore and exploit the serverless option.

<a href="https://openwhisk.apache.org/" target="_blank">Apache openwhisk</a>  is an open source example of the serverless application of which AWS lambda is an example.


- [Awesome Big Data](#awesome-bigdata)
    - [RDBMS](#rdbms)
    - [Frameworks](#frameworks)
    - [Distributed Programming](#distributed-programming)
    - [Distributed Filesystem](#distributed-filesystem)
    - [Key-Map Data Model](#key-map-data-model)
    - [Document Data Model](#document-data-model)
    - [Key-value Data Model](#key-value-data-model)

## RDBMS
* [MySQL](https://www.mysql.com/) The world's most popular open source database.
* [PostgreSQL](https://www.postgresql.org/) The world's most advanced open source database.
* [Oracle Database](http://www.oracle.com/us/corporate/features/database-12c/index.html) - object-relational database management system.
* [Teradata](http://www.teradata.com/products-and-services/teradata-database/) - high-performance MPP data warehouse platform.

## Frameworks

* [IBM Streams](https://www.ibm.com/analytics/us/en/technology/stream-computing/) - platform for distributed processing and real-time analytics.  Integrates with many of the popular technologies in the Big Data ecosystem (Kafka, HDFS, Spark, etc.)
* [Apache Hadoop](http://hadoop.apache.org/) - framework for distributed processing. Integrates MapReduce (parallel processing), YARN (job scheduling) and HDFS (distributed file system).
* [Tigon](https://github.com/caskdata/tigon) - High Throughput Real-time Stream Processing Framework.
* [Pachyderm](http://pachyderm.io/) - Pachyderm is a data storage platform built on Docker and Kubernetes to provide reproducible data processing and analysis.
