-- ===============================================================
-- 02-insertar-eventos.cql
-- Misión 4: Apache Cassandra - Sector Columnas Anchas
-- 
-- Inserción de 15 eventos masivos de telemetría correspondientes a 
-- 3 estudiantes de CampusCloud (2026001, 2026002, 2026003).
-- ===============================================================

USE campuscloud_logs;

-- ===============================================================
-- 1. EVENTOS ESTUDIANTE: Mariano Silva (2026001)
-- ===============================================================
INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '2026001', '2026-11-01 08:30:15', a1a1a1a1-1111-1111-1111-111111111111,
  'LOGIN_AUTENTICACION', null, 'Autenticacion', '10.50.149.121', 'Chrome/Win11', 'EXITOSO', 45, 'Inicio de sesion institucional correcto'
);

INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '2026001', '2026-11-01 08:45:22', a1a1a1a1-2222-2222-2222-222222222222,
  'SOLICITUD_SERVICIO', 3, 'Servicios Escolares', '10.50.149.121', 'Chrome/Win11', 'EXITOSO', 120, 'Inscripcion a Taller de Cloud Computing'
);

INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '2026001', '2026-11-03 10:15:00', a1a1a1a1-3333-3333-3333-333333333333,
  'SOLICITUD_SERVICIO', 1, 'Servicios Escolares', '10.50.149.121', 'Chrome/Win11', 'EXITOSO', 98, 'Solicitud de Certificado de Estudios'
);

INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '2026001', '2026-11-06 14:20:45', a1a1a1a1-4444-4444-4444-444444444444,
  'DESCARGA_DOCUMENTO', 1, 'Portal Estudiantil', '10.50.149.121', 'Edge/Win11', 'EXITOSO', 350, 'Descarga de Certificado oficial en formato PDF'
);

INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '2026001', '2026-11-10 16:00:10', a1a1a1a1-5555-5555-5555-555555555555,
  'CONSULTA_CATALOGO', null, 'API Gateway', '10.50.149.121', 'CampusCloud-App/Android', 'EXITOSO', 28, 'Consulta de ofertas de empleo y practicas'
);

-- ===============================================================
-- 2. EVENTOS ESTUDIANTE: Ana Martinez (2026002)
-- ===============================================================
INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '2026002', '2026-11-02 09:00:12', b2b2b2b2-1111-1111-1111-111111111111,
  'LOGIN_AUTENTICACION', null, 'Autenticacion', '10.50.149.145', 'Firefox/macOS', 'EXITOSO', 50, 'Login desde red wifi universitaria'
);

INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '2026002', '2026-11-02 09:20:30', b2b2b2b2-2222-2222-2222-222222222222,
  'SOLICITUD_SERVICIO', 5, 'Tutorias', '10.50.149.145', 'Firefox/macOS', 'EXITOSO', 110, 'Agendamiento de Asesoria Academica en Bases de Datos'
);

INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '2026002', '2026-11-04 11:45:00', b2b2b2b2-3333-3333-3333-333333333333,
  'SOLICITUD_SERVICIO', 2, 'Control Escolar', '10.50.149.145', 'Firefox/macOS', 'EN_PROCESO', 140, 'Tramite de Reexpedicion de Credencial extraviada'
);

INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '2026002', '2026-11-08 17:30:15', b2b2b2b2-4444-4444-4444-444444444444,
  'ACTUALIZACION_PERFIL', null, 'Configuracion', '10.50.149.145', 'Safari/iOS', 'EXITOSO', 65, 'Actualizacion de numero telefonico de contacto'
);

INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '2026002', '2026-11-12 12:10:05', b2b2b2b2-5555-5555-5555-555555555555,
  'CONSULTA_HISTORIAL', null, 'Portal Estudiantil', '10.50.149.145', 'Firefox/macOS', 'EXITOSO', 38, 'Revision de boleta parcial de calificaciones'
);

-- ===============================================================
-- 3. EVENTOS ESTUDIANTE: Carlos Gomez (2026003)
-- ===============================================================
INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '2026003', '2026-11-03 07:50:00', c3c3c3c3-1111-1111-1111-111111111111,
  'LOGIN_AUTENTICACION', null, 'Autenticacion', '10.50.149.201', 'Edge/Win10', 'FALLIDO', 120, 'Intento fallido: clave caducada'
);

INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '2026003', '2026-11-03 07:52:10', c3c3c3c3-2222-2222-2222-222222222222,
  'LOGIN_AUTENTICACION', null, 'Autenticacion', '10.50.149.201', 'Edge/Win10', 'EXITOSO', 48, 'Inicio de sesion exitoso tras renovar credencial'
);

INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '2026003', '2026-11-03 08:15:30', c3c3c3c3-3333-3333-3333-333333333333,
  'SOLICITUD_SERVICIO', 2, 'Control Escolar', '10.50.149.201', 'Edge/Win10', 'RECHAZADA', 210, 'Reexpedicion rechazada por falta de comprobante de pago'
);

INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '2026003', '2026-11-05 11:00:00', c3c3c3c3-4444-4444-4444-444444444444,
  'SOLICITUD_SERVICIO', 3, 'Deportes', '10.50.149.201', 'Edge/Win10', 'EXITOSO', 95, 'Inscripcion a Taller de Acondicionamiento Fisico'
);

INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '2026003', '2026-11-09 15:40:20', c3c3c3c3-5555-5555-5555-555555555555,
  'LOGOUT', null, 'Portal Estudiantil', '10.50.149.201', 'Edge/Win10', 'EXITOSO', 15, 'Cierre de sesion voluntario'
);

-- Confirmación de cantidad total de eventos insertados
SELECT count(*) AS total_eventos_cargados FROM eventos_estudiante;
