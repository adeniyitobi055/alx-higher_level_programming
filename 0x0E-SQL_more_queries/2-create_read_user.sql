-- creates the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create a user user_0d_2
CREATE USER IF NOT EXISTS user_0d_2 IDENTIFIED BY 'user_0d_2_pwd';
-- grant privileges
GRANT SELECT PRIVILEGE ON hbtn_0d_2 . * TO user_0d_2@localhost;
