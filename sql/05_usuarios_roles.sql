-- 05_usuarios_roles.sql: Gestión de Usuarios, Roles y Privilegios en SQL Server
USE CampusCloud;
GO

-- 1. Crear Roles de Base de Datos
IF DATABASE_PRINCIPAL_ID('rol_administrador') IS NULL CREATE ROLE rol_administrador;
IF DATABASE_PRINCIPAL_ID('rol_operador') IS NULL CREATE ROLE rol_operador;
IF DATABASE_PRINCIPAL_ID('rol_consulta') IS NULL CREATE ROLE rol_consulta;
GO

-- 2. Asignar Permisos a los Roles
-- Administrador: Control Total (SELECT, INSERT, UPDATE, DELETE, CREATE TABLE, DDL)
GRANT SELECT, INSERT, UPDATE, DELETE, ALTER, CONTROL TO rol_administrador;

-- Operador: SELECT, INSERT, UPDATE, DELETE (sin DDL ni administración)
GRANT SELECT, INSERT, UPDATE, DELETE TO rol_operador;

-- Consulta: Solo SELECT
GRANT SELECT TO rol_consulta;
GO

-- 3. Crear Logins y Usuarios de Prueba
-- Usuario Consulta
IF NOT EXISTS (SELECT * FROM sys.server_principals WHERE name = 'user_consulta')
    CREATE LOGIN user_consulta WITH PASSWORD = 'UserConsulta123!', CHECK_POLICY = OFF;
IF NOT EXISTS (SELECT * FROM sys.database_principals WHERE name = 'user_consulta')
    CREATE USER user_consulta FOR LOGIN user_consulta;
ALTER ROLE rol_consulta ADD MEMBER user_consulta;

-- Usuario Operador
IF NOT EXISTS (SELECT * FROM sys.server_principals WHERE name = 'user_operador')
    CREATE LOGIN user_operador WITH PASSWORD = 'UserOperador123!', CHECK_POLICY = OFF;
IF NOT EXISTS (SELECT * FROM sys.database_principals WHERE name = 'user_operador')
    CREATE USER user_operador FOR LOGIN user_operador;
ALTER ROLE rol_operador ADD MEMBER user_operador;

-- Usuario Administrador
IF NOT EXISTS (SELECT * FROM sys.server_principals WHERE name = 'user_admin')
    CREATE LOGIN user_admin WITH PASSWORD = 'UserAdmin123!', CHECK_POLICY = OFF;
IF NOT EXISTS (SELECT * FROM sys.database_principals WHERE name = 'user_admin')
    CREATE USER user_admin FOR LOGIN user_admin;
ALTER ROLE rol_administrador ADD MEMBER user_admin;
GO
