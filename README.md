# Executar os seguintes comandos no Oracle DB

```sql
create user django identified by SUASENHA 
default tablespace users QUOTA unlimited on users;

grant create session,
create table,
create sequence,
create procedure,
create trigger to django;
```
