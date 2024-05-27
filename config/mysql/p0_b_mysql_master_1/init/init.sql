# compose/mysql/init/init.sql
GRANT ALL PRIVILEGES ON *.* TO 'mydb'@'%';
FLUSH PRIVILEGES;
