```bash
sudo -i
yum install python3-pip -y
mkdir -p my_layer/python
pip3 install pymysql -t my_layer/python
cd my_layer
zip -r ../pymysql_layer.zip python
cd
aws s3 cp pymysql_layer.zip s3://lambda-packages-pymysql-s3
```


