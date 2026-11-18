db = db.getSiblingDB('CampusCloud');
db.detalles_servicios.deleteMany({});

db.detalles_servicios.insertMany([
  {
    id_servicio_sql: 1,
    codigo: "SRV-ACAD-01",
    nombre_servicio: "Certificado de Estudios Oficial",
    categoria: "Academico",
    activo: true,
    modalidades: ["En Línea", "Ventanilla"],
    requisitos: [
      "Comprobante de no adeudo en biblioteca",
      "Historial académico completo validado",
      "Comprobante de pago arancelario",
      "Fotografía tamaño infantil digitalizada",
      "Identificación oficial escaneada en formato PDF"
    ],
    especificaciones: {
      departamento_responsable: "Servicios Escolares",
      tiempo_estimado_dias: 2,
      costo_arancel: 150.0,
      formato_entrega: "Digital PDF con firma electrónica avanzada, código QR y validación blockchain",
      vigencia_meses: 12
    },
    etiquetas: ["titulacion", "oficial", "calificaciones", "documento", "blockchain"],
    ultima_actualizacion: new Date("2026-11-18T10:00:00Z")
  },
  {
    id_servicio_sql: 2,
    codigo: "SRV-ADM-02",
    nombre_servicio: "Reexpedición de Credencial Institucional",
    categoria: "Administrativo",
    activo: true,
    modalidades: ["Presencial", "Ventanilla"],
    requisitos: [
      "Reporte de extravío o credencial deteriorada",
      "Comprobante de pago arancelario",
      "Identificación oficial vigente"
    ],
    especificaciones: {
      departamento_responsable: "Control Escolar y Credencialización",
      tiempo_estimado_dias: 1,
      costo_arancel: 120.0,
      formato_entrega: "Física PVC con chip RFID y banda magnética",
      vigencia_meses: 12
    },
    etiquetas: ["credencial", "rfid", "acceso", "identificacion"],
    ultima_actualizacion: new Date("2026-11-18T10:00:00Z")
  },
  {
    id_servicio_sql: 3,
    codigo: "SRV-EXT-03",
    nombre_servicio: "Inscripción a Taller Extracurricular",
    categoria: "Extracurricular",
    activo: true,
    modalidades: ["En Línea", "Presencial", "Híbrida"],
    requisitos: [
      "Estar inscrito en el cuatrimestre activo",
      "Cumplir prerrequisitos técnicos del taller",
      "Carta compromiso de asistencia mínima 80%"
    ],
    especificaciones: {
      departamento_responsable: "Extensión Universitaria y Cultura",
      tiempo_estimado_dias: 0,
      costo_arancel: 0.0,
      formato_entrega: "Acceso a plataforma LMS Moodle y constancia curricular",
      vigencia_meses: 4
    },
    etiquetas: ["taller", "cultura", "deportes", "habilidades", "lms"],
    ultima_actualizacion: new Date("2026-11-18T10:00:00Z")
  },
  {
    id_servicio_sql: 4,
    codigo: "SRV-ADM-04",
    nombre_servicio: "Baja Temporal Voluntaria",
    categoria: "Administrativo",
    activo: true,
    modalidades: ["Ventanilla"],
    requisitos: [
      "Solicitud por escrito justificada",
      "Constancia de no adeudo general",
      "Entrevista con tutor y dirección de carrera"
    ],
    especificaciones: {
      departamento_responsable: "Dirección de Carrera y Servicios Escolares",
      tiempo_estimado_dias: 5,
      costo_arancel: 0.0,
      formato_entrega: "Dictamen oficial de baja temporal sellado",
      vigencia_meses: 6
    },
    etiquetas: ["baja", "tramite", "escolar", "dictamen"],
    ultima_actualizacion: new Date("2026-11-18T10:00:00Z")
  },
  {
    id_servicio_sql: 5,
    codigo: "SRV-ACAD-05",
    nombre_servicio: "Asesoría Académica Especializada",
    categoria: "Academico",
    activo: true,
    modalidades: ["En Línea", "Presencial"],
    requisitos: [
      "Solicitud vía portal estudiantil con 24h de anticipación",
      "Identificación de temas o materias requeridas"
    ],
    especificaciones: {
      departamento_responsable: "Coordinación de Tutorías y Asesorías",
      tiempo_estimado_dias: 1,
      costo_arancel: 0.0,
      formato_entrega: "Sesión 1 a 1 de 60 min con registro de bitácora",
      vigencia_meses: 1
    },
    etiquetas: ["tutoria", "regularizacion", "academico", "docencia"],
    ultima_actualizacion: new Date("2026-11-18T10:00:00Z")
  },
  {
    id_servicio_sql: 6,
    codigo: "SRV-EXT-06",
    nombre_servicio: "Bolsa de Trabajo y Prácticas Profesionales",
    categoria: "Extracurricular",
    activo: true,
    modalidades: ["En Línea"],
    requisitos: [
      "Avance curricular mínimo del 70%",
      "Curriculum vitae en formato institucional estandarizado",
      "Seguro facultativo IMSS vigente"
    ],
    especificaciones: {
      departamento_responsable: "Vinculación Empresarial y Bolsa de Empleo",
      tiempo_estimado_dias: 3,
      costo_arancel: 0.0,
      formato_entrega: "Carta de presentación institucional y enlace a vacantes",
      vigencia_meses: 6
    },
    etiquetas: ["empleo", "estadía", "practicas", "empresas", "cv"],
    ultima_actualizacion: new Date("2026-11-18T10:00:00Z")
  },
  {
    id_servicio_sql: 7,
    codigo: "SRV-SAL-07",
    nombre_servicio: "Servicio Médico y Orientación Psicológica",
    categoria: "Salud_Estudiantil",
    activo: true,
    modalidades: ["Presencial", "En Línea"],
    requisitos: [
      "Credencial escolar vigente o número de matrícula oficial",
      "Cita previa para atención psicológica salvo urgencias"
    ],
    especificaciones: {
      departamento_responsable: "Unidad Médica y Salud Integral CampusCloud",
      tiempo_estimado_dias: 0,
      costo_arancel: 0.0,
      formato_entrega: "Ficha de valoración clínica y receta médica digital",
      vigencia_meses: 12
    },
    etiquetas: ["medico", "psicologia", "salud", "bienestar", "urgencias"],
    ultima_actualizacion: new Date("2026-11-18T10:00:00Z")
  }
]);

// Crear indices para acelerar consultas de Compass
db.detalles_servicios.createIndex({ codigo: 1 }, { unique: true });
db.detalles_servicios.createIndex({ categoria: 1 });
db.detalles_servicios.createIndex({ modalidades: 1 });
db.detalles_servicios.createIndex({ "especificaciones.departamento_responsable": 1 });

print("SEEDING COMPLETADO: " + db.detalles_servicios.countDocuments() + " documentos insertados correctamente.");
