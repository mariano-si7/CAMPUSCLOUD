// ===============================================================
// 01-crear-nodos-relaciones.cypher
// Misión 3: Neo4j - Red de Grafos Vengadora
// 
// Construye el grafo de CampusCloud conectando los Estudiantes y 
// Servicios existentes de SQL Server con relaciones y afinidades.
// ===============================================================

// 1. Limpieza de entorno previo (opcional para pruebas reproducibles)
MATCH (n) DETACH DELETE n;

// 2. Creación de Restricciones e Índices para Integridad y Rendimiento
CREATE CONSTRAINT c_estudiante_matricula IF NOT EXISTS
FOR (e:Estudiante) REQUIRE e.matricula IS UNIQUE;

CREATE CONSTRAINT c_servicio_id IF NOT EXISTS
FOR (s:Servicio) REQUIRE s.id_servicio IS UNIQUE;

// 3. Creación de Nodos Estudiante (Basados exactamente en SQL Server dbo.Estudiantes)
CREATE (e1:Estudiante {
  id_estudiante: 1,
  matricula: '24300700',
  nombre: 'Mariano Calzadilla Alvarez',
  correo: 'mariano.calzadilla@campuscloud.edu',
  carrera: 'Tecnologías de la Información',
  cuatrimestre: 7,
  promedio: 9.4
})
CREATE (e2:Estudiante {
  id_estudiante: 2,
  matricula: '2026002',
  nombre: 'Ana Martinez',
  correo: 'ana.martinez@campuscloud.edu',
  carrera: 'Tecnologías de la Información',
  cuatrimestre: 7,
  promedio: 9.8
})
CREATE (e3:Estudiante {
  id_estudiante: 3,
  matricula: '2026003',
  nombre: 'Carlos Gomez',
  correo: 'carlos.gomez@campuscloud.edu',
  carrera: 'Mecatrónica',
  cuatrimestre: 5,
  promedio: 8.7
})
CREATE (e4:Estudiante {
  id_estudiante: 4,
  matricula: '2026004',
  nombre: 'Diana Lopez',
  correo: 'diana.lopez@campuscloud.edu',
  carrera: 'Tecnologías de la Información',
  cuatrimestre: 7,
  promedio: 9.1
})
CREATE (e5:Estudiante {
  id_estudiante: 5,
  matricula: '2026005',
  nombre: 'Eduardo Hernandez',
  correo: 'eduardo.hernandez@campuscloud.edu',
  carrera: 'Desarrollo de Software',
  cuatrimestre: 4,
  promedio: 8.9
})
CREATE (e6:Estudiante {
  id_estudiante: 6,
  matricula: '2026006',
  nombre: 'Fernanda Torres',
  correo: 'fernanda.torres@campuscloud.edu',
  carrera: 'Redes y Ciberseguridad',
  cuatrimestre: 6,
  promedio: 9.2
});

// 4. Creación de Nodos Servicio (Basados exactamente en SQL Server dbo.Servicios)
CREATE (s1:Servicio {
  id_servicio: 1,
  codigo: 'SRV-ACAD-01',
  nombre: 'Certificado de Estudios',
  categoria: 'Academico',
  modalidad: 'Digital',
  arancel: 150.00
})
CREATE (s2:Servicio {
  id_servicio: 2,
  codigo: 'SRV-ADM-02',
  nombre: 'Reexpedición de Credencial',
  categoria: 'Administrativo',
  modalidad: 'Presencial',
  arancel: 120.00
})
CREATE (s3:Servicio {
  id_servicio: 3,
  codigo: 'SRV-EXT-03',
  nombre: 'Inscripción a Taller',
  categoria: 'Extracurricular',
  modalidad: 'Mixta',
  arancel: 0.00
})
CREATE (s4:Servicio {
  id_servicio: 4,
  codigo: 'SRV-ADM-04',
  nombre: 'Baja Temporal',
  categoria: 'Administrativo',
  modalidad: 'Ventanilla',
  arancel: 0.00
})
CREATE (s5:Servicio {
  id_servicio: 5,
  codigo: 'SRV-ACAD-05',
  nombre: 'Asesoría Académica',
  categoria: 'Academico',
  modalidad: 'Virtual',
  arancel: 0.00
});

// 5. Creación de Relaciones con Propiedades

// 5.1 Relaciones :SOLICITA (Derivadas de las Solicitudes reales en SQL Server)
MATCH (e:Estudiante {matricula: '24300700'}), (s:Servicio {id_servicio: 1})
CREATE (e)-[:SOLICITA {id_solicitud: 1, fecha: '2026-11-03', estado: 'Aprobada', calificacion: 5}]->(s);

MATCH (e:Estudiante {matricula: '24300700'}), (s:Servicio {id_servicio: 3})
CREATE (e)-[:SOLICITA {id_solicitud: 11, fecha: '2026-11-01', estado: 'Aprobada', calificacion: 4}]->(s);

MATCH (e:Estudiante {matricula: '2026002'}), (s:Servicio {id_servicio: 2})
CREATE (e)-[:SOLICITA {id_solicitud: 2, fecha: '2026-11-04', estado: 'En Proceso', calificacion: null}]->(s);

MATCH (e:Estudiante {matricula: '2026002'}), (s:Servicio {id_servicio: 5})
CREATE (e)-[:SOLICITA {id_solicitud: 12, fecha: '2026-11-02', estado: 'Aprobada', calificacion: 5}]->(s);

MATCH (e:Estudiante {matricula: '2026003'}), (s:Servicio {id_servicio: 3})
CREATE (e)-[:SOLICITA {id_solicitud: 3, fecha: '2026-11-05', estado: 'Aprobada', calificacion: 5}]->(s);

MATCH (e:Estudiante {matricula: '2026003'}), (s:Servicio {id_servicio: 2})
CREATE (e)-[:SOLICITA {id_solicitud: 13, fecha: '2026-11-03', estado: 'Rechazada', calificacion: 1}]->(s);

MATCH (e:Estudiante {matricula: '2026004'}), (s:Servicio {id_servicio: 1})
CREATE (e)-[:SOLICITA {id_solicitud: 4, fecha: '2026-11-06', estado: 'Pendiente', calificacion: null}]->(s);

MATCH (e:Estudiante {matricula: '2026004'}), (s:Servicio {id_servicio: 4})
CREATE (e)-[:SOLICITA {id_solicitud: 14, fecha: '2026-11-04', estado: 'Pendiente', calificacion: null}]->(s);

MATCH (e:Estudiante {matricula: '2026005'}), (s:Servicio {id_servicio: 5})
CREATE (e)-[:SOLICITA {id_solicitud: 5, fecha: '2026-11-07', estado: 'Aprobada', calificacion: 5}]->(s);

MATCH (e:Estudiante {matricula: '2026005'}), (s:Servicio {id_servicio: 1})
CREATE (e)-[:SOLICITA {id_solicitud: 15, fecha: '2026-11-05', estado: 'En Proceso', calificacion: null}]->(s);

MATCH (e:Estudiante {matricula: '2026006'}), (s:Servicio {id_servicio: 3})
CREATE (e)-[:SOLICITA {id_solicitud: 16, fecha: '2026-11-08', estado: 'Aprobada', calificacion: 4}]->(s);

// 5.2 Relaciones de Alianzas y Colaboración entre Estudiantes (:COLABORA_CON)
MATCH (e1:Estudiante {matricula: '24300700'}), (e2:Estudiante {matricula: '2026002'})
CREATE (e1)-[:COLABORA_CON {proyecto: 'Arquitectura CampusCloud', afinidad: 'Alta', rol_lider: 'Mariano'}]->(e2);

MATCH (e2:Estudiante {matricula: '2026002'}), (e4:Estudiante {matricula: '2026004'})
CREATE (e2)-[:COLABORA_CON {proyecto: 'Proyecto Integrador NoSQL', afinidad: 'Muy Alta', rol_lider: 'Ana'}]->(e4);

MATCH (e1:Estudiante {matricula: '24300700'}), (e5:Estudiante {matricula: '2026005'})
CREATE (e1)-[:COLABORA_CON {proyecto: 'Tutorías de Programación', afinidad: 'Media', rol_lider: 'Mariano'}]->(e5);

// 5.3 Relaciones de Interés Académico (:TIENE_INTERES_EN)
MATCH (e1:Estudiante {matricula: '24300700'}), (s:Servicio {id_servicio: 5})
CREATE (e1)-[:TIENE_INTERES_EN {motivo: 'Reforzar arquitectura cloud', prioridad: 'Alta'}]->(s);

MATCH (e3:Estudiante {matricula: '2026003'}), (s:Servicio {id_servicio: 1})
CREATE (e3)-[:TIENE_INTERES_EN {motivo: 'Trámite de prácticas profesionales', prioridad: 'Media'}]->(s);

// 5.4 Relación de Dependencia entre Servicios (:PRERREQUISITO_DE)
MATCH (s_asesoria:Servicio {id_servicio: 5}), (s_cert:Servicio {id_servicio: 1})
CREATE (s_asesoria)-[:PRERREQUISITO_DE {motivo: 'Aprobación de asesorías para liberar constancia oficial'}]->(s_cert);

// Resumen del grafo creado
MATCH (e:Estudiante) WITH count(e) AS TotalEstudiantes
MATCH (s:Servicio) WITH TotalEstudiantes, count(s) AS TotalServicios
MATCH ()-[r]->() WITH TotalEstudiantes, TotalServicios, count(r) AS TotalRelaciones
RETURN TotalEstudiantes, TotalServicios, TotalRelaciones;
