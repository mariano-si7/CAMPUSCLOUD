// ===============================================================
// 02-consultas.cypher
// Misión 3: Neo4j - Red de Grafos Vengadora
// 
// 3 Consultas Estratégicas en Lenguaje Cypher:
// 1. Servicios solicitados por un estudiante específico
// 2. Estudiantes que comparten un mismo servicio (Comunidades)
// 3. Recomendación colaborativa basada en la red de alianzas
// ===============================================================

// ---------------------------------------------------------------
// CONSULTA 1: Servicios usados / solicitados por un estudiante
// Contexto: Conocer el historial académico de 'Mariano Silva' (24300700)
// ---------------------------------------------------------------
MATCH (e:Estudiante {matricula: '24300700'})-[r:SOLICITA]->(s:Servicio)
RETURN 
  e.nombre AS Estudiante,
  e.carrera AS Carrera,
  s.nombre AS Servicio,
  s.categoria AS Categoria,
  r.fecha AS FechaSolicitud,
  r.estado AS Estado,
  r.calificacion AS CalificacionServicio
ORDER BY r.fecha DESC;

// ---------------------------------------------------------------
// CONSULTA 2: Estudiantes que comparten un mismo servicio
// Contexto: Detectar grupos de trabajo o compañeros inscritos a 'Inscripción a Taller'
// ---------------------------------------------------------------
MATCH (e1:Estudiante)-[r1:SOLICITA]->(s:Servicio)<-[r2:SOLICITA]-(e2:Estudiante)
WHERE id(e1) < id(e2) AND s.nombre = 'Inscripción a Taller'
RETURN 
  s.nombre AS ServicioCompartido,
  e1.nombre AS Estudiante_1,
  e1.carrera AS Carrera_1,
  e2.nombre AS Estudiante_2,
  e2.carrera AS Carrera_2,
  r1.estado AS Estado_Estudiante1,
  r2.estado AS Estado_Estudiante2;

// ---------------------------------------------------------------
// CONSULTA 3: Algoritmo de Recomendación Basado en Alianzas de Grafos
// Contexto: Recomendar a 'Mariano Silva' (24300700) servicios que sus colaboradores
// directos han utilizado con éxito (calificación >= 4) y que Mariano aún no solicita.
// ---------------------------------------------------------------
MATCH (target:Estudiante {matricula: '24300700'})-[:COLABORA_CON]-(colaborador:Estudiante)
MATCH (colaborador)-[r:SOLICITA]->(recomendado:Servicio)
WHERE NOT (target)-[:SOLICITA]->(recomendado) 
  AND (r.calificacion >= 4 OR r.estado = 'Aprobada')
RETURN 
  target.nombre AS EstudianteObjetivo,
  colaborador.nombre AS RecomendadoPor,
  recomendado.nombre AS ServicioSugerido,
  recomendado.categoria AS Categoria,
  r.calificacion AS CalificacionOtorgada,
  "Servicio aprobado por colaborador de confianza" AS MotivoRecomendacion;
