create database sistemaponto;

create table if not exists usuario (
id_usuario smallint auto_increment primary key, 
nome varchar(40) not null,
cpf char(11) not null unique
) auto_increment = 10000;


create table if not exists registro(
id_registro smallint auto_increment primary key,
id_usuario smallint,
entrada datetime,
saida datetime,
constraint fk_id_usuario foreign key (id_usuario) references usuario(id_usuario)
);