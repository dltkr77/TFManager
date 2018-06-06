PRAGMA auto_vacuum = 1;
PRAGMA foreign_keys = ON;


DROP TABLE IF EXISTS tbl_model;
CREATE TABLE IF NOT EXISTS tbl_model (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  model_name TEXT NOT NULL,
  model_class TEXT NOT NULL,
  model_config_json TEXT NOT NULL,
  model_path TEXT NOT NULL
);

DROP TABLE IF EXISTS tbl_train;
CREATE TABLE IF NOT EXISTS tbl_train (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  model_id INTEGER REFERENCES  tbl_model(id) ON DELETE CASCADE,
  learning_rate REAL NOT NULL,
  iteration_or_epoch INTEGER NOT NULL,
  performance REAL NOT NULL,
  performance_desc TEXT NOT NULL,
  loss REAL,
  time_elapsed REAL
);