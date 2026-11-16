-- ===============================================================
-- 03-consultas.cql
-- Misión 4: Apache Cassandra - Sector Columnas Anchas
-- 
-- Consultas eficientes orientadas a la Partition Key y Clustering Key:
-- 1. Toda la actividad de un estudiante en orden cronológico descendente
-- 2. Actividad de un estudiante dentro de un intervalo temporal específico
-- 3. Consulta puntual por clave primaria compuesta exacta
-- 4. Demostración y justificación de las limitaciones de CQL
-- ===============================================================

USE campuscloud_logs;

-- ---------------------------------------------------------------
-- CONSULTA 1: Historial cronológico completo de Mariano Silva (2026001)
-- Eficiencia: O(1) en búsqueda de partición + lectura secuencial en disco
-- ---------------------------------------------------------------
SELECT 
  matricula, 
  fecha_hora, 
  tipo_evento, 
  modulo, 
  estado, 
  ip_origen, 
  latencia_ms, 
  detalles 
FROM eventos_estudiante 
WHERE matricula = '2026001';

-- ---------------------------------------------------------------
-- CONSULTA 2: Actividad en un intervalo o periodo de fechas (01 al 05 de Nov)
-- Eficiencia: Búsqueda binaria dentro del índice de la SSTable sobre el clustering
-- ---------------------------------------------------------------
SELECT 
  matricula, 
  fecha_hora, 
  tipo_evento, 
  modulo, 
  estado, 
  latencia_ms, 
  detalles 
FROM eventos_estudiante 
WHERE matricula = '2026001' 
  AND fecha_hora >= '2026-11-01 00:00:00' 
  AND fecha_hora <= '2026-11-05 23:59:59';

-- ---------------------------------------------------------------
-- CONSULTA 3: Consulta exacta por Clave Primaria Completa
-- ---------------------------------------------------------------
SELECT 
  matricula, 
  fecha_hora, 
  id_evento, 
  tipo_evento, 
  detalles 
FROM eventos_estudiante 
WHERE matricula = '2026001' 
  AND fecha_hora = '2026-11-01 08:45:22' 
  AND id_evento = a1a1a1a1-2222-2222-2222-222222222222;

-- ---------------------------------------------------------------
-- EXPLICACIÓN TÉCNICA DE LIMITACIONES DE CONSULTA EN CQL:
--
-- 1. ¿Por qué NO se puede ejecutar: "SELECT * FROM eventos_estudiante WHERE tipo_evento = 'SOLICITUD_SERVICIO'"?
--    Respuesta: En Cassandra no existe un índice global por defecto. Si no se provee la
--    Partition Key ('matricula'), Cassandra tendría que escanear TODAS las particiones en
--    TODOS los nodos del cluster (Full Cluster Scan), destruyendo el rendimiento distribuido.
--
-- 2. El peligro de 'ALLOW FILTERING':
--    CQL rechaza consultas sin partition key a menos que se fuerce con 'ALLOW FILTERING'.
--    En producción, 'ALLOW FILTERING' es un antipatrón crítico que causa latencias inaceptables
--    y caídas de nodos por sobrecarga de CPU y memoria.
--
-- 3. Restricciones de Rango:
--    Los operadores de rango (<, >, <=, >=) ÚNICAMENTE se permiten sobre columnas de clustering
--    y siempre que la Partition Key esté explícitamente fijada con igualdad (=).
-- ---------------------------------------------------------------
