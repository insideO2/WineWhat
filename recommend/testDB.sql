use reviewtestdb;

create table reviewtest(
	id varchar(50) primary key,
    review json
);

insert into reviewtest(id, review) values('userA', json_object(
1, 5,
 2, 4,
 3 , 4,
 4 , 3,
 5 , 0));
insert into reviewtest(id, review) values('userB', json_object(
1, 1,
 2, 0,
 3 , 1,
 4 , 0,
 5 , 4));
insert into reviewtest(id, review) values('userC', json_object(
1, 4,
 2, 0,
 3 , 4,
 4 , 4,
 5 , 2));
insert into reviewtest(id, review) values('userD', json_object(
1, 4,
 2, 2,
 3 , 3,
 4 , 0,
 5 , 1));
insert into reviewtest(id, review) values('userE', json_object(
1, 0,
 2, 0,
 3 , 0,
 4 , 0,
 5 , 0)); 
