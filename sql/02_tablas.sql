-- 02_tablas.sql: Creación de tablas e integridad de datos en SQL Server
USE CampusCloud;
GO

-- Limpieza de tablas si ya existen
IF OBJECT_ID('dbo.Solicitudes', 'U') IS NOT NULL DROP TABLE dbo.Solicitudes;
IF OBJECT_ID('dbo.Servicios', 'U') IS NOT NULL DROP TABLE dbo.Servicios;
IF OBJECT_ID('dbo.Estudiantes', 'U') IS NOT NULL DROP TABLE dbo.Estudiantes;
GO

-- Tabla 1: Estudiantes
CREATE TABLE Estudiantes (
    IdEstudiante INT IDENTITY(1,1) PRIMARY KEY,
    Matricula VARCHAR(20) NOT NULL UNIQUE,
    Nombre VARCHAR(100) NOT NULL,
    Correo VARCHAR(100) NOT NULL UNIQUE
);
GO

-- Tabla 2: Servicios
CREATE TABLE Servicios (
    IdServicio INT IDENTITY(1,1) PRIMARY KEY,
    NombreServicio VARCHAR(100) NOT NULL,
    Descripcion VARCHAR(255) NOT NULL,
    Activo BIT NOT NULL DEFAULT 1
);
GO

-- Tabla 3: Solicitudes
CREATE TABLE Solicitudes (
    IdSolicitud INT IDENTITY(1,1) PRIMARY KEY,
    IdEstudiante INT NOT NULL,
    IdServicio INT NOT NULL,
    FechaSolicitud DATETIME NOT NULL DEFAULT GETDATE(),
    Estado VARCHAR(30) NOT NULL DEFAULT 'Pendiente',
    CONSTRAINT FK_Solicitudes_Estudiantes FOREIGN KEY (IdEstudiante) REFERENCES Estudiantes(IdEstudiante),
    CONSTRAINT FK_Solicitudes_Servicios FOREIGN KEY (IdServicio) REFERENCES Servicios(IdServicio)
);
GO
