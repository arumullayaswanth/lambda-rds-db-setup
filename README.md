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

### 🔹 A. Using MySQL Workbench

1. Open **MySQL Workbench** → Add new connection
2. Set:

   * Connection Name: `rds-test-db`
   * Hostname: `mydbinstance.c0n8k0a0swtz.us-east-1.rds.amazonaws.com`
   * Port: `3306`
   * Username: `admin`
   * Password: enter and store
3. Click **Test Connection**

✅ Ensure RDS security group allows TCP 3306 from your IP

```sql
SHOW DATABASES;
```

and you see:

```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test               |
+--------------------+
```

### What each database means

| Database             | Purpose                                     |
| -------------------- | ------------------------------------------- |
| `information_schema` | Metadata about tables, columns, permissions |
| `mysql`              | MySQL system database (users, privileges)   |
| `performance_schema` | Performance monitoring                      |
| `sys`                | Performance views and helpers               |
| `test`               | ✅ The database your **Lambda created**      |

---

### Next Step: Check the table created by Lambda

Run:

```sql
USE test;
SHOW TABLES;
```

Expected output:

```
+----------------+
| Tables_in_test |
+----------------+
| mytable        |
+----------------+
```

---

### Check table structure

```sql
DESCRIBE mytable;
```

Example output:

```
+------------+--------------+------+-----+-------------------+-------------------+
| Field      | Type         | Null | Key | Default           | Extra             |
+------------+--------------+------+-----+-------------------+-------------------+
| id         | int          | NO   | PRI | NULL              | auto_increment    |
| name       | varchar(255) | NO   |     | NULL              |                   |
| created_at | timestamp    | YES  |     | CURRENT_TIMESTAMP |                   |
+------------+--------------+------+-----+-------------------+-------------------+
```

---

### Test inserting data manually

```sql
INSERT INTO mytable (name) VALUES ('AWS Lambda Test');
```

Check data:

```sql
SELECT * FROM mytable;
```

Example result:

```
+----+------------------+---------------------+
| id | name             | created_at          |
+----+------------------+---------------------+
| 1  | AWS Lambda Test  | 2026-03-11 15:40:10 |
+----+------------------+---------------------+
```

---

✅ This confirms:

* Lambda → RDS connection works
* Database creation works
* Table creation works
