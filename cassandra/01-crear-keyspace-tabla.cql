-- ===============================================================
-- 01-crear-keyspace-tabla.cql
-- Misión 4: Apache Cassandra - Sector Columnas Anchas
-- 
-- Diseño orientado a consultas (Query-Driven Design) para telemetría
-- masiva de eventos de estudiantes de CampusCloud.
-- ===============================================================

-- 1. Creación del Keyspace institucional
CREATE KEYSPACE IF NOT EXISTS campuscloud_logs
WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': 1
};

USE campuscloud_logs;

-- 2. Creación de Tabla de Eventos de Telemetría
-- JUSTIFICACIÓN DE CLAVES:
-- - Partition Key ((matricula)): Concentra todos los eventos de un estudiante
--   en la misma partición física mediante el Murmur3Partitioner.
-- - Clustering Keys (fecha_hora, id_evento): Ordena los datos físicamente en disco
--   en orden cronológico descendente (los más recientes primero).
CREATE TABLE IF NOT EXISTS eventos_estudiante (
  matricula text,
  fecha_hora timestamp,
  id_evento uuid,
  tipo_evento text,
  id_servicio_sql int,
  modulo text,
  ip_origen text,
  dispositivo text,
  estado text,
  latencia_ms int,
  detalles text,
  PRIMARY KEY ((matricula), fecha_hora, id_evento)
) WITH CLUSTERING ORDER BY (fecha_hora DESC)
  AND comment = 'Bitacora de auditoria y eventos masivos por estudiante en CampusCloud';

-- 3. Verificación de metadata de la tabla creada
DESCRIBE TABLE eventos_estudiante;
