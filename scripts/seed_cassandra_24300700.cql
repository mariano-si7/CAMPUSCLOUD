USE campuscloud_logs;

DELETE FROM eventos_estudiante WHERE matricula = '2026001';

INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '24300700', '2026-11-01 08:30:15', a1a1a1a1-1111-1111-1111-111111111111,
  'LOGIN_AUTENTICACION', null, 'Autenticacion', '10.50.149.121', 'Chrome/Win11', 'EXITOSO', 45, 'Inicio de sesion institucional correcto'
);

INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '24300700', '2026-11-01 08:45:22', a1a1a1a1-2222-2222-2222-222222222222,
  'SOLICITUD_SERVICIO', 3, 'Servicios Escolares', '10.50.149.121', 'Chrome/Win11', 'EXITOSO', 120, 'Inscripcion a Taller de Cloud Computing'
);

INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '24300700', '2026-11-03 10:15:00', a1a1a1a1-3333-3333-3333-333333333333,
  'SOLICITUD_SERVICIO', 1, 'Servicios Escolares', '10.50.149.121', 'Chrome/Win11', 'EXITOSO', 98, 'Solicitud de Certificado de Estudios Oficial'
);

INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '24300700', '2026-11-06 14:20:45', a1a1a1a1-4444-4444-4444-444444444444,
  'DESCARGA_DOCUMENTO', 1, 'Portal Estudiantil', '10.50.149.121', 'Edge/Win11', 'EXITOSO', 350, 'Descarga de Certificado oficial en formato PDF'
);

INSERT INTO eventos_estudiante (
  matricula, fecha_hora, id_evento, tipo_evento, id_servicio_sql, modulo, ip_origen, dispositivo, estado, latencia_ms, detalles
) VALUES (
  '24300700', '2026-11-10 16:00:10', a1a1a1a1-5555-5555-5555-555555555555,
  'CONSULTA_CATALOGO', null, 'API Gateway', '10.50.149.121', 'CampusCloud-App/Android', 'EXITOSO', 28, 'Consulta de ofertas de empleo y practicas'
);
