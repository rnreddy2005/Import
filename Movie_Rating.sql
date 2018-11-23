
create table user_table(user_id integer,user_name varchar(30),country varchar(10),start_dt  date, end_dt date)primary index(user_id);
create table movie_table( movie_id integer,movie_title_name varchar(100),movie_type varchar(10)) primary index(movie_id);
create table rating_table(user_id integer,movie_id integer,score smallint ,business_day  date)primary index(user_id,movie_id);
   
  /* insert sample records for user table */
insert into user_table(1,'ram','SG','2018-11-20','2018-11-20');
insert into user_table(1,'ram','USA','2018-11-21','9999-12-31');
insert into user_table(2,'krish','USA','2018-11-23','9999-12-31');
insert into user_table(3,'naresh','USA','2018-11-23','9999-12-31');
insert into user_table(4,'john','IND','2018-11-23','9999-12-31');
insert into user_table(5,'michel','UK','2018-11-23','9999-12-31');

  /* insert sample records for movie  table */
insert into movie_table(1,'spiderman','action');
insert into movie_table(2,'batman','action');
insert into movie_table(3,'titanic','romatic');
insert into movie_table(4,'avengers','action');
insert into movie_table(5,'Nemo','cartoon');

  /* insert sample records for rating  table */
insert into rating_table(2,4,5,'2018-11-23');
insert into rating_table(1,4,4,'2018-11-23');
insert into rating_table(3,4,2,'2018-11-23');
insert into rating_table(4,3,1,'2018-11-23');
insert into rating_table(5,4,5,'2018-11-23');
insert into rating_table(2,2,5,'2018-11-23');

select movie_title_name ,avg(score)
from movie_table mv 
inner join rating_table rt
on mv.movie_id = rt.movie_id
inner join user_table ut
on ut.user_id = rt.user_id
where ut.country='USA' and mv.movie_type='action'
group by movie_title_name
