
--@block
-- create database

-- user table
CREATE TABLE IF NOT EXISTS users (

    id int NOT NULL AUTO_INCREMENT,
    username varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    PRIMARY KEY (id)
);

-- program table

CREATE TABLE IF NOT EXISTS programs (

    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    description varchar(255) NOT NULL,
    completed boolean NOT NULL,
    PRIMARY KEY (id)
);

-- week table

CREATE TABLE IF NOT EXISTS weeks (

    id int NOT NULL AUTO_INCREMENT,
    week int NOT NULL,
    completed boolean NOT NULL,
    PRIMARY KEY (id)
)

-- workout table

CREATE TABLE IF NOT EXISTS workouts (

    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    completed boolean NOT NULL,
    PRIMARY KEY (id)
);

-- exercise table

CREATE TABLE IF NOT EXISTS exercises (

    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    reps int NOT NULL,
    completed boolean NOT NULL,
    PRIMARY KEY (id)
)