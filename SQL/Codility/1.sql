show databases;
use Codility

insert into elements values(2);
insert into elements values(10);
insert into elements values(20);
insert into elements values(10);

SELECT SUM(v) 
FROM elements

CREATE USER "vscode"@"%" IDENTIFIED WITH mysql_native_password BY "mysqlPW1!!";