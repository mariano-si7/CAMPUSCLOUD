-- 03_datos.sql: Inserción de datos mínimos requeridos
USE CampusCloud;
GO

-- 1. Insertar 10 Estudiantes
INSERT INTO Estudiantes (Matricula, Nombre, Correo) VALUES
('2026001', 'Mariano Silva', 'mariano.silva@campuscloud.edu'),
('2026002', 'Ana Martinez', 'ana.martinez@campuscloud.edu'),
('2026003', 'Carlos Gomez', 'carlos.gomez@campuscloud.edu'),
('2026004', 'Diana Lopez', 'diana.lopez@campuscloud.edu'),
('2026005', 'Eduardo Hernandez', 'eduardo.hernandez@campuscloud.edu'),
('2026006', 'Fernanda Torres', 'fernanda.torres@campuscloud.edu'),
('2026007', 'Gabriel Ruiz', 'gabriel.ruiz@campuscloud.edu'),
('2026008', 'Hilda Morales', 'hilda.morales@campuscloud.edu'),
('2026009', 'Ignacio Castro', 'ignacio.castro@campuscloud.edu'),
('2026010', 'Jessica Vargas', 'jessica.vargas@campuscloud.edu');
GO

-- 2. Insertar 5 Servicios
INSERT INTO Servicios (NombreServicio, Descripcion, Activo) VALUES
('Certificado de Estudios', 'Emisión de certificado oficial de calificaciones', 1),
('Reexpedición de Credencial', 'Reposición de credencial universitaria', 1),
('Inscripción a Taller', 'Registro a talleres extracurriculares', 1),
('Baja Temporal', 'Tramite de suspensión temporal de estudios', 1),
('Asesoría Académica', 'Solicitud de tutoría individual con docente', 1);
GO

-- 3. Insertar 15 Solicitudes
INSERT INTO Solicitudes (IdEstudiante, IdServicio, FechaSolicitud, Estado) VALUES
(1, 1, GETDATE()-10, 'Aprobada'),
(2, 2, GETDATE()-9, 'En Proceso'),
(3, 3, GETDATE()-8, 'Aprobada'),
(4, 1, GETDATE()-7, 'Pendiente'),
(5, 5, GETDATE()-6, 'Aprobada'),
(6, 4, GETDATE()-5, 'Rechazada'),
(7, 2, GETDATE()-4, 'Aprobada'),
(8, 3, GETDATE()-3, 'Pendiente'),
(9, 5, GETDATE()-2, 'En Proceso'),
(10, 1, GETDATE()-1, 'Pendiente'),
(1, 3, GETDATE()-12, 'Aprobada'),
(2, 5, GETDATE()-11, 'Aprobada'),
(3, 2, GETDATE()-10, 'Rechazada'),
(4, 4, GETDATE()-9, 'Pendiente'),
(5, 1, GETDATE()-8, 'En Proceso');
GO
