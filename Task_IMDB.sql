create database IMDB;
use IMDB;

create table Movie(
movie_id int Primary key auto_increment,
movie_name varchar(30),
movie_released_year int,
movie_songs int,
movie_Language varchar(25)
);

create table media(
media_id int primary key auto_increment,
movie_id int,
media_type varchar(30),
media_file varchar(30),
foreign key (movie_id)
references Movie(movie_id));

create table genres(
genre_id int Primary key Auto_increment,
genre_name varchar(25)
);

create table movie_genres(
movie_id int ,
genre_id int ,
primary key(movie_id,genre_id),
foreign key (movie_id)
references Movie(movie_id),
foreign key (genre_id)
references genres(genre_id)
);

create table users(
user_id int primary key,
user_name varchar(25)
);

create table reviews(
review_id int primary key,
review_text varchar(100),
user_id int,
movie_id int,
foreign key (user_id)
references users(user_id),
foreign key (movie_id)
references Movie(movie_id)
);

create table artist(
artist_id int primary key,
artist_name varchar(25)
);

Create table skills(
skill_id int primary key,
skill_name varchar(25)
);

create table artist_skill(
skill_id int,
artist_id int,
primary key(artist_id,skill_id),
foreign key (skill_id)
references skills(skill_id),
foreign key (artist_id)
references artist(artist_id)
);

create table roles(
role_id int primary key,
role_name varchar(50)
);

create table movie_artist_role(
movie_id int,
artist_id int,
role_id int,
primary key(movie_id,artist_id,role_id),
foreign key (artist_id)
references artist(artist_id),
foreign key (role_id)
references roles(role_id),
foreign key (movie_id)
references Movie(movie_id)
);

Insert into Movie (
movie_name,movie_released_year,movie_songs,movie_language) values     
('ABC',2015,6,'Tamil'),
('DEF',2020,5,'Tamil'),
('XYZ',2019,4,'Hindi'),
('GHI',2000,6,'Telugu'),
('JKL',2003,6,'Malayalam');

Insert into media(
movie_id,media_type,media_file)values
(1,'Image','abc_poster.jpg'),
(1,'Video','abc_trailer.mp4'),
(2,'Image','def_poster.jpg'),
(3,'Video','xyz_trailer.mp4'),
(5,'Image','JKL_poster.jpg');

Insert into genres(genre_name)values
('Action'),
('Comedy'),
('Thriller'),
('Drama');

Insert into movie_genres(movie_id,genre_id)values
(1,1),
(1,2),
(2,3),
(3,4),
(4,1);

Insert into users values
(1,'Lahi'),
(2,'Thanshi'),
(3,'Roshan');

Insert into reviews values
(1,'Good concept',1,1),
(2,'Excellent story',2,1),
(3,'Direction super',3,2);

Insert into artist values
(1,'Kamal'),
(2,'Vijay'),
(3,'Surya');

Insert into skills values
(1,'Acting'),
(2,'Dancing'),
(3,'Singing');

Insert into artist_skill values
(1,1),
(2,1),
(1,2),
(3,2);

Insert into roles values
(1,'Hero'),
(2,'Villain'),
(3,'Guest role');


Insert into movie_artist_role values
(1,1,1),
(2,2,1),
(2,2,2),
(3,3,1);

SELECT * FROM movie_artist_role;
