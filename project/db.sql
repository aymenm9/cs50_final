-- create database

-- user table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
);

-- program table
CREATE TABLE IF NOT EXISTS programs (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    duration INTEGER NOT NULL,
    completed INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- workout table
CREATE TABLE IF NOT EXISTS workouts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    completed INTEGER NOT NULL,
    program_id INTEGER NOT NULL,
    FOREIGN KEY (program_id) REFERENCES programs(id)
);

-- exercise table
CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    reps INTEGER NOT NULL,
    completed INTEGER NOT NULL,
    workout_id INTEGER NOT NULL,
    FOREIGN KEY (workout_id) REFERENCES workouts(id)
);