# Lab 6 STOT - ST0263
## Unit 3: Big Data
## AWS EMR
I will be using the same EMR config as in [Lab5](../Lab5/).

### PySpark CLI
Word count in PySpark CLI in master node:  
![](./images/PySpark%20CLI.jpg)

As you can see the two directories were created in `/tmp`:  
![](./images/CLI%20ls.jpg)

Submit a [file](./wc-pyspart.py) to PySpark  

![](./images/Submit%20file.jpg)

### Zeppelin

Word count in Zeppelin:  
![](./images/wc%20zeppelin.jpg)

### JupyterHub

Upload [wordcount-spark.ipynb](./wordcount-spark.ipynb).  

Change kernel to `PySpark`:  
![](./images/kernel-change.jpg)

Run:  
![](./images/wc%20jupyter%20hub.jpg)

### Hive

Create database, create table, store HDI data in table in hive directly.  
![](./images/hue%20store%20data.jpg)

Show tables.  
![](./images/hue%20hive%20show%20tables.jpg)

Describe HDI table.  
![](./images/describe%20hdi%20table.jpg)

Select data from said table.  
![](./images/hue%20hive%20show.jpg)

Select all countries that have a gni greater than 2000 and show their gni.  

![](./images/gni%20gt%202000.jpg)

Create new table for JOIN in external s3 storage.  

![](./images/table%20expo%20createed.jpg)

Join expo and hdi tables.  

![](./images/join.jpg)

### Word count in Hive

Using alternative 1.  

![](./images/create%20docs%20tabke.jpg)

Sort by word.  

![](./images/sort%20by%20word.jpg)

Sort by word descending.  

![](./images/descending.jpg)

Insert the last result into another table.  

![](./images/insert%20into%20other%20table.jpg)