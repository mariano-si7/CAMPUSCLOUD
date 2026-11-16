-- ===============================================================
-- 04-actualizar.cql
-- Misión 4: Apache Cassandra - Sector Columnas Anchas
-- 
-- Operación UPDATE controlada en Cassandra (CQL):
-- Demostración de requisitos de Primary Key completa y semántica de Upsert.
-- ===============================================================

USE campuscloud_logs;

-- 1. CONSULTA PREVIA DEL ESTADO DEL REGISTRO
SELECT 
  matricula, 
  fecha_hora, 
  id_evento, 
  tipo_evento, 
  estado, 
  latencia_ms, 
  detalles 
FROM eventos_estudiante 
WHERE matricula = '2026002' 
  AND fecha_hora = '2026-11-04 11:45:00' 
  AND id_evento = b2b2b2b2-3333-3333-3333-333333333333;

-- 2. EJECUCIÓN DE UPDATE CONTROLADO
-- Nota Técnica: En CQL, todo UPDATE requiere OBLIGATORIAMENTE la clave primaria completa
-- (Partition Key + todas las Clustering Keys). No se permite UPDATE con filtros parciales.
UPDATE eventos_estudiante 
SET 
  estado = 'APROBADA', 
  latencia_ms = 85, 
  detalles = 'Tramite de credencial aprobado; pago confirmado por finanzas' 
WHERE matricula = '2026002' 
  AND fecha_hora = '2026-11-04 11:45:00' 
  AND id_evento = b2b2b2b2-3333-3333-3333-333333333333;

-- 3. CONSULTA POSTERIOR PARA VERIFICAR EL CAMBIO
SELECT 
  matricula, 
  fecha_hora, 
  id_evento, 
  tipo_evento, 
  estado, 
  latencia_ms, 
  detalles 
FROM eventos_estudiante 
WHERE matricula = '2026002' 
  AND fecha_hora = '2026-11-04 11:45:00' 
  AND id_evento = b2b2b2b2-3333-3333-3333-333333333333;

-- ---------------------------------------------------------------
-- NOTA TÉCNICA: SEMÁNTICA DE UPSERT EN CASSANDRA:
-- En el motor de Cassandra, 'UPDATE' e 'INSERT' operan bajo el mismo mecanismo interno.
-- Si la clave primaria no existe en disco, 'UPDATE' creará automáticamente el registro.
-- La actualización no lee antes de escribir (Read-before-write), sino que escribe una
-- nueva celda en la Memtable con una marca de tiempo (timestamp) más reciente.
-- ---------------------------------------------------------------
