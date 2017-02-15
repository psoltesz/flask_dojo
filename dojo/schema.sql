drop table if exists flaskdojo;
create table flaskdojo (
  id serial primary key,
  title text not null,
  status text
);
