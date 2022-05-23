# Lab 5 STOT - ST0263
## Unit 3: Big Data
## AWS EMR

### Bucket
Public URL: https://sflorezs1datalake.s3.amazonaws.com/raw/datasets/  
Create a bucket with the default configuration.  
![](./images/bucket.png)

Upload datasets to `sflorezs1datalake`.  
![](./images/s3-datasets.png)

### Cluster setup
- **Software configuration:**
![](./images/emr-17-57-46.png)
- **Glue:**
![](./images/emr-17-57-57.png)
- **Edit software settings:**
![](./images/emr-17-58-26.png)
- **Cluster composition:**
![](./images/emr-18-00-34.png)
- **Cluster Nodes and Instances:**
![](./images/emr-18-00-46.png)
- **Cluster scaling:**
![](./images/emr-18-01-09.png)
- **Auto-termination:**
![](./images/emr-18-01-23.png)
- **EBS Root Volume:**
![](./images/emr-18-01-39.png)
- **Security Options:**
![](./images/emr-18-05-18.png)
- **Security Group for master:**
![](./images/emr-18-13-40.png)

### HDFS
`ls`  
![](./images/ls.png)
`ls /user`  
![](./images/ls-user.png)
`upload dataset from s3`  
![](./images/s3-to-hdfs.png)
`ls /tmp/datasets`  
![](./images/ls-tmp-datasets.png)

### HUE
Create datasets dir.  
![](./images/datasets-create-dir.png)
Upload onu dataset.  
![](./images/upload-onu.png)
Data uploaded.  
![](./images/onu-uploaded.png)
Data open.
![](./images/onu-open.png)

### MapReduce

Code can be found in the `./mrjob` directory.

- **Empleados:**
    - El salario promedio por Sector Económico (SE)  
    ![](./images/empleados-18-33.png)
    - El salario promedio por Empleado  
    ![](./images/empleados-18-52.png)
    - Número de SE por Empleado que ha tenido a lo largo de la estadística
    ![](./images/empleados-19-06.png)
- **Empresas:**
    - Por acción, dia-menor-valor, día-mayor-valor  
    ![](./images/empresas-19-21.png)
    - Listado de acciones que siempre han subido o se mantienen estables.  
    ![](./images/empresas-19-35.png)
    - DIA NEGRO: Saque el día en el que la mayor cantidad de acciones tienen el menor valor de acción (DESPLOME), suponga una inflación independiente del tiempo.  
    ![](./images/empresas-19-47.png)
- **Peliculas:**
    - Número de películas vista por un usuario, valor promedio de calificación  
    ![](./images/peliculas-20-16.png)
    - Día en que más películas se han visto  
    ![](./images/peliculas-20-31.png)
    - Día en que menos películas se han visto  
    ![](./images/peliculas-20-39.png)
    - Número de usuarios que ven una misma película y el rating promedio  
    ![](./images/peliculas-20-56.png)
    - Día en que peor evaluación en promedio han dado los usuarios  
    ![](./images/peliculas-21-08.png)
    - Día en que mejor evaluación han dado los usuarios  
    ![](./images/peliculas-21-16.png)
    - La mejor y peor película evaluada por genero  
    ![](./images/peliculas-21-27.png)
