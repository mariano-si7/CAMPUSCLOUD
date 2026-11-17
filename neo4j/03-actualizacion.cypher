// ===============================================================
// 03-actualizacion.cypher
// Misión 3: Neo4j - Red de Grafos Vengadora
// 
// Actualización Controlada de Nodos y Relaciones:
// 1. Verificación del estado previo
// 2. Transición de estado de solicitud y calificación
// 3. Creación de una nueva alianza estratégica
// 4. Verificación del estado posterior
// ===============================================================

// 1. ESTADO PREVIO DE LA SOLICITUD DE ANA MARTINEZ
MATCH (e:Estudiante {matricula: '2026002'})-[r:SOLICITA]->(s:Servicio {nombre: 'Reexpedición de Credencial'})
RETURN 
  e.nombre AS Estudiante,
  s.nombre AS Servicio,
  r.id_solicitud AS ID_Solicitud,
  r.estado AS Estado_Previo,
  r.calificacion AS Calificacion_Previa;

// 2. ACTUALIZACIÓN CONTROLADA (SET)
MATCH (e:Estudiante {matricula: '2026002'})-[r:SOLICITA]->(s:Servicio {nombre: 'Reexpedición de Credencial'})
SET 
  r.estado = 'Aprobada',
  r.fecha_conclusion = '2026-11-16',
  r.calificacion = 5,
  r.folio_digital = 'CRE-2026-002-OK';

// 3. EXPANSIÓN DE LA RED: NUEVA ALIANZA DE CIBERSEGURIDAD
MATCH (e_fer:Estudiante {matricula: '2026006'}), (e_mar:Estudiante {matricula: '24300700'})
MERGE (e_fer)-[c:COLABORA_CON {proyecto: 'Defensa de Infraestructura NoSQL'}]->(e_mar)
ON CREATE SET c.afinidad = 'Muy Alta', c.fecha_inicio = '2026-11-16';

// 4. VERIFICACIÓN DEL ESTADO POSTERIOR
MATCH (e:Estudiante {matricula: '2026002'})-[r:SOLICITA]->(s:Servicio {nombre: 'Reexpedición de Credencial'})
RETURN 
  e.nombre AS Estudiante,
  s.nombre AS Servicio,
  r.id_solicitud AS ID_Solicitud,
  r.estado AS Estado_Actualizado,
  r.fecha_conclusion AS FechaConclusion,
  r.calificacion AS Calificacion_Final,
  r.folio_digital AS Folio;
