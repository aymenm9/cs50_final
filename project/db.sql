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
    completed INTEGER NOT NULL
);

-- workout table
CREATE TABLE IF NOT EXISTS workouts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    completed INTEGER NOT NULL
);

-- exercise table
CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    reps INTEGER NOT NULL,
    completed INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS user_programs (
    user_id INTEGER NOT NULL,
    program_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (program_id) REFERENCES programs(id),
    PRIMARY KEY (user_id, program_id)
);

CREATE TABLE IF NOT EXISTS program_workouts (
    program_id INTEGER NOT NULL,
    workout_id INTEGER NOT NULL,
    FOREIGN KEY (program_id) REFERENCES programs(id),
    FOREIGN KEY (workout_id) REFERENCES workouts(id),
    PRIMARY KEY (program_id, workout_id)
);

CREATE TABLE IF NOT EXISTS workout_exercises (
    workout_id INTEGER NOT NULL,
    exercise_id INTEGER NOT NULL,
    FOREIGN KEY (workout_id) REFERENCES workouts(id),
    FOREIGN KEY (exercise_id) REFERENCES exercises(id),
    PRIMARY KEY (workout_id, exercise_id)
);