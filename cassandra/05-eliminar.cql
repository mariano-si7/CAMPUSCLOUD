-- ===============================================================
-- 05-eliminar.cql
-- Misión 4: Apache Cassandra - Sector Columnas Anchas
-- 
-- Operación DELETE controlada en Cassandra (CQL):
-- Demostración de eliminación puntual y justificación del concepto de Tombstones.
-- ===============================================================

USE campuscloud_logs;

-- 1. CONSULTA PREVIA DEL EVENTO QUE SERÁ ELIMINADO
SELECT 
  matricula, 
  fecha_hora, 
  id_evento, 
  tipo_evento, 
  estado, 
  detalles 
FROM eventos_estudiante 
WHERE matricula = '2026003' 
  AND fecha_hora = '2026-11-03 07:50:00' 
  AND id_evento = c3c3c3c3-1111-1111-1111-111111111111;

-- 2. EJECUCIÓN DEL DELETE CONTROLADO
-- Se especifica la clave primaria exacta para no afectar otros eventos de la partición.
DELETE FROM eventos_estudiante 
WHERE matricula = '2026003' 
  AND fecha_hora = '2026-11-03 07:50:00' 
  AND id_evento = c3c3c3c3-1111-1111-1111-111111111111;

-- 3. VERIFICACIÓN POSTERIOR: COMPROBAR QUE YA NO EXISTE
SELECT 
  matricula, 
  fecha_hora, 
  id_evento, 
  tipo_evento, 
  estado, 
  detalles 
FROM eventos_estudiante 
WHERE matricula = '2026003' 
  AND fecha_hora = '2026-11-03 07:50:00' 
  AND id_evento = c3c3c3c3-1111-1111-1111-111111111111;

-- Verificación de los eventos restantes del estudiante Carlos Gomez (deben quedar 4 eventos)
SELECT 
  matricula, 
  fecha_hora, 
  tipo_evento, 
  estado 
FROM eventos_estudiante 
WHERE matricula = '2026003';

-- ---------------------------------------------------------------
-- NOTA TÉCNICA: EL MECANISMO DE TOMBSTONES EN CASSANDRA:
-- En arquitectura de columnas anchas (LSM-Tree), los datos escritos en disco (SSTables)
-- son inmutables. Por lo tanto, un comando 'DELETE' no borra físicamente los bytes del disco
-- al instante; en su lugar, escribe un marcador especial llamado 'Tombstone' con una marca
-- de tiempo.
-- 
-- El Tombstone oculta el dato en las consultas posteriores. El espacio en disco sólo se
-- libera físicamente cuando se ejecuta el proceso en segundo plano de 'Compaction' y una
-- vez superado el umbral 'gc_grace_seconds' (normalmente 10 días), evitando que réplicas
-- atrasadas revivan datos antiguos ("zombie data").
-- ---------------------------------------------------------------
