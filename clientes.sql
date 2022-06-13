Drop table if exists clientes;

Create table clientes(
    id_cliente integer primary key autoincrement,
    nombre varchar(50) not null,
    email varchar(50) not null
);


insert into clientes(nombre,email) values ("Luis","luis@email.com");
insert into clientes(nombre,email) values ("Gustabo","gustabo@email.com");
insert into clientes(nombre,email) values ("Kevin","kevin@email.com");


Select * From clientes;