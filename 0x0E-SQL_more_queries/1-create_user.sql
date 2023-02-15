-- creates the MySQL server user user_0d_1
-- user_0d_1 would have all privileges on your MySQL server
-- The user_0d_1 password would be set to user_0d_1_pwd
-- If the user user_0d_1 already exists, it would not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL TO 'user_0d_1'@'localhost';
