SELECT 
    DB_NAME() AS BaseActual;
go

-- Consuulta completa del con4texto

SELECT
    SUSER_NAME() AS LoginActual,
    USER_NAME() AS UsuarioActual,
    DB_NAME() AS BaseActual,
    IS_SRVROLEMEMBER('sysadmin') AS EsSysAdmin,

## Creacion y prueba de un admin alternativo

-- Para hacer un login siempre debemos estar en master
USE master;
GO
-- Crear el login admin_sql
CREATE LOGIN admin_sql 
WITH PASSWORD = 'StrongPassword123!';
CHECK_POLICY = ON;

`CREATE LOGIN admin_sql  : crea una identidad que puede autenticarse ante la instancia
WITH PASSWORD = 'StrongPassword123!' : define la contraseña para el login
CHECK_POLICY = ON : habilita la política de contraseñas de Windows para este login, lo que significa que la contraseña debe cumplir con los requisitos de complejidad y expiración establecidos por el sistema operativo.






-- PRACTICA DE CREACION DE USUARIO Y ASIGNACION DE ROLES

	USE master 
	go

	-- CREATE LOGIN admin_sql

	CREATE LOGIN admin_sql
	WITH PASSWORD = 'Admiin@cloud#12',
	CHECK_POLICY = ON;

	-- Verifiar si existe y esta habilitado

	SELECT 
		name
		type_desc
		is disabled
	FROM sys_server_principals
	WHERE name = 'admin_sql'
	GO 

	-- Demostrar que crear un login no lo hace el adminstrador
	SELECT IS_SRVROLEMEMBER ('sysadmin', 'admin_sql') AS EsSysadmin

	
	
	CREATE DATABASE prueba;
	go

	use prueba;
	CREATE TABLE alumnos (
		id int primary key identity(1,1),
		nombre varchar (50) not null
	);

	INSERT INTO alumnos
	VALUES ('Eustaquio'),
			('Toribio'),
			('Floriupondio'),
			('Maria');
	GO

	USE master
	go

-- Agregar admin_sql el rol de servidofr sysadmin 
	ALTER SERVER ROLE sysadmin
	ADD MEMBER admin_sql;
	GO

	-- Validar la nueva membresia
	SELECT IS_SRVROLEMEMBER ('sysadmin', 'admin_sql') AS EsSysadmin


	-- Deshabilitacion controlada de sa
	ALTER LOGIN sa DISABLE;



-- Seleccionar a master y crear la base de datos

USE master;
go

CREATE DATABASE empresaVentas;
GO


	
