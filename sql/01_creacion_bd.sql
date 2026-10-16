-- 01_creacion_bd.sql: Creación de la base de datos CampusCloud para SQL Server
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'CampusCloud')
BEGIN
    CREATE DATABASE CampusCloud;
END
GO

USE CampusCloud;
GO
