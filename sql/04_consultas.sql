-- 04_consultas.sql: Operaciones CRUD y Consultas Relacionadas
USE CampusCloud;
GO

-- 1. Operación SELECT
SELECT * FROM Estudiantes;
SELECT * FROM Servicios WHERE Activo = 1;
SELECT * FROM Solicitudes WHERE Estado = 'Pendiente';
GO

-- 2. Operación INSERT
INSERT INTO Estudiantes (Matricula, Nombre, Correo) VALUES ('2026011', 'Kevin Duran', 'kevin.duran@campuscloud.edu');
GO

-- 3. Operación UPDATE
UPDATE Solicitudes SET Estado = 'Aprobada' WHERE IdSolicitud = 4;
GO

-- 4. Operación DELETE
DELETE FROM Estudiantes WHERE Matricula = '2026011';
GO

-- 5. Consulta Relacionada 1: Estudiante, servicio solicitado y estado
SELECT 
    e.Matricula,
    e.Nombre AS Estudiante,
    s.NombreServicio AS Servicio,
    sol.FechaSolicitud,
    sol.Estado
FROM Solicitudes sol
INNER JOIN Estudiantes e ON sol.IdEstudiante = e.IdEstudiante
INNER JOIN Servicios s ON sol.IdServicio = s.IdServicio;
GO

-- 6. Consulta Relacionada 2: Total de solicitudes por servicio
SELECT 
    s.NombreServicio,
    COUNT(sol.IdSolicitud) AS TotalSolicitudes
FROM Servicios s
LEFT JOIN Solicitudes sol ON s.IdServicio = sol.IdServicio
GROUP BY s.NombreServicio;
GO

-- 7. Consulta Relacionada 3: Solicitudes pendientes con detalle del estudiante
SELECT 
    e.Nombre,
    e.Correo,
    s.NombreServicio,
    sol.Estado
FROM Solicitudes sol
JOIN Estudiantes e ON sol.IdEstudiante = e.IdEstudiante
JOIN Servicios s ON sol.IdServicio = s.IdServicio
WHERE sol.Estado = 'Pendiente';
GO
