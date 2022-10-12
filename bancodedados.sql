use sistemaponto;

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


insert into usuario 
values
(id_usuario, 'Guilherme', '12345678910'),
(id_usuario, 'Enzo', '12345678911'),
(id_usuario, 'Isaac', '12345678912'),
(id_usuario, 'Antonio', '12345678913'),
(id_usuario, 'Richard', '12345678914'),
(id_usuario, 'Erik', '12345678915'),
(id_usuario, 'Icaro', '12345678916'),
(id_usuario, 'Jorge', '12345678917'),
(id_usuario, 'Joao', '12345678918'),
(id_usuario, 'Ives', '12345678919');

insert into registro (id_registro, id_usuario, entrada, saida)  values
(id_registro, '10000', '2022-10-11 13:10:00', '2022-10-11 13:10:00'),
(id_registro, '10001', '2022-10-11 13:10:00', '2022-10-11 13:10:00'),
(id_registro, '10001', '2022-10-11 13:10:00', '2022-10-11 13:10:00'),
(id_registro, '10002', '2022-10-11 13:10:00', '2022-10-11 13:10:00'),
(id_registro, '10001', '2022-10-11 13:10:00', '2022-10-11 13:10:00'),
(id_registro, '10000', '2022-10-11 13:10:00', '2022-10-11 13:10:00'),
(id_registro, '10000', '2022-10-11 13:10:00', '2022-10-11 13:10:00'),
(id_registro, '10002', '2022-10-11 13:10:00', '2022-10-11 13:10:00'),
(id_registro, '10003', '2022-10-11 13:10:00', '2022-10-11 13:10:00'),
(id_registro, '10000', '2022-10-11 13:10:00', '2022-10-11 13:10:00'),
(id_registro, '10007', '2022-10-11 13:10:00', '2022-10-11 13:10:00');


select registro.id_registro, usuario.nome, registro.entrada, registro.saida 
from usuario
inner join registro
on usuario.id_usuario = registro.id_usuario
where registro.saida is null;

insert into registro values
(id_registro, '10000', '2022-10-11 13:10:00', null),
(id_registro, '10001', '2022-10-11 13:10:00', null),
(id_registro, '10002', '2022-10-11 13:10:00', null),
(id_registro, '10003', '2022-10-11 13:10:00', null),
(id_registro, '10004', '2022-10-11 13:10:00', null),
(id_registro, '10005', '2022-10-11 13:10:00', null),
(id_registro, '10006', '2022-10-11 13:10:00', null);