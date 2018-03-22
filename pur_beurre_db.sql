#After the connection to the MySQL database, do the following queries

CREATE DATABASE pur_beurre_db;

CREATE USER script@localhost IDENTIFIED BY "SUPERmotdepasse3000";

GRANT ALL ON pur_beurre_db.* TO script IDENTIFIED BY "SUPERmotdepasse3000";