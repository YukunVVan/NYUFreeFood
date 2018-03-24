CREATE SEQUENCE user_id START 1000 increment 1; 

CREATE TABLE user_info(
id INT,
username VARCHAR (100) NOT NULL UNIQUE,
first_name VARCHAR (100) NOT NULL,
last_name VARCHAR (100) NOT NULL,
password VARCHAR (100) NOT NULL);
COMMIT ;

##INSERT INTO user_info (id, username, first_name, last_name, password) VALUES (nextval('user_id').......);

##=====================================================================##
CREATE SEQUENCE playlist START 100 increment 1;

CREATE TABLE playlist_spotify(
playlist_id INT PRIMARY KEY,
playlist_name VARCHAR (200) );
COMMIT ;
## nextval('playlist')

##=====================================================================##

CREATE SEQUENCE playlist_track START 100 increment 1;

CREATE TABLE track_list (
Track_Id SERIAL PRIMARY KEY, 
Track_Name VARCHAR (200),
Playlist_Id INT UNIQUE);

COMMIT ;

##INSERT INTO track_list (Track_Name, Playlist_Id) VALUES ('Demons', nextval('playlist_track'));

##=====================================================================##


CREATE TABLE track_mood (
mood_id SERIAL PRIMARY KEY,
track_id SERIAL NOT NULL ,
score_track INT NOT NULL);
COMMIT ;

## INSERT INTO track_list (score_track) VALUES (6);

##=====================================================================##

CREATE TABLE mood_name_id (
mood_id SERIAL PRIMARY KEY,
mood VARCHAR (50),
track_id SERIAL NOT NULL);
COMMIT ;

##INSERT INTO mood_name_id (mood) VALUES ('happy');

##=====================================================================##

CREATE SEQUENCE user_id_1 START 1000 increment 1; 


CREATE TABLE master_data (
userid INT NOT NULL ,
mood_id SERIAL NOT NULL ,
self_mood_score INT NOT NULL ,
score_track INT NOT NULL );
COMMIT ;

##=====================================================================##