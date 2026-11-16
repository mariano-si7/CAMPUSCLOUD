/**
 * 02-insertar-documentos.js
 * Misión 2: MongoDB - Sector Documental
 * 
 * Inserta 8 documentos representativos que extienden los 5 servicios
 * relacionales de SQL Server más 3 servicios complementarios.
 */

const dbName = 'CampusCloud';
const collectionName = 'detalles_servicios';
const dbInstance = db.getSiblingDB(dbName);

print(`=======================================================`);
print(`[MongoDB] Insertando catálogo extendido en: ${collectionName}`);
print(`=======================================================`);

const servicios = [
  {
    id_servicio_sql: NumberInt(1),
    codigo: "SRV-ACAD-01",
    nombre_servicio: "Certificado de Estudios",
    categoria: "Academico",
    activo: true,
    modalidades: ["En Línea", "Ventanilla"],
    requisitos: [
      "Comprobante de no adeudo en biblioteca",
      "Historial académico completo validado",
      "Comprobante de pago arancelario",
      "Fotografía tamaño infantil digitalizada"
    ],
    especificaciones: {
      departamento_responsable: "Servicios Escolares",
      tiempo_estimado_dias: NumberInt(3),
      costo_arancel: 150.00,
      formato_entrega: "Digital PDF con firma electrónica avanzada y código QR",
      vigencia_meses: NumberInt(12)
    },
    etiquetas: ["titulacion", "oficial", "calificaciones", "documento"]
  },
  {
    id_servicio_sql: NumberInt(2),
    codigo: "SRV-ADM-02",
    nombre_servicio: "Reexpedición de Credencial",
    categoria: "Administrativo",
    activo: true,
    modalidades: ["Presencial"],
    requisitos: [
      "Acta de extravío o credencial física deteriorada",
      "Identificación oficial vigente (INE o pasaporte)",
      "Recibo de pago en caja universitaria"
    ],
    especificaciones: {
      departamento_responsable: "Control Escolar y Credencialización",
      tiempo_estimado_dias: NumberInt(5),
      costo_arancel: 120.00,
      formato_entrega: "Tarjeta plástica PVC con chip RFID y banda magnética",
      vigencia_meses: NumberInt(24)
    },
    etiquetas: ["identidad", "credencial", "acceso", "reposicion"]
  },
  {
    id_servicio_sql: NumberInt(3),
    codigo: "SRV-EXT-03",
    nombre_servicio: "Inscripción a Taller",
    categoria: "Extracurricular",
    activo: true,
    modalidades: ["Presencial", "Mixta"],
    requisitos: [
      "Estar inscrito en el cuatrimestre vigente",
      "Seguro facultativo activo (IMSS)",
      "Carta compromiso de asistencia al 80%"
    ],
    especificaciones: {
      departamento_responsable: "Dirección de Actividades Culturales y Deportivas",
      tiempo_estimado_dias: NumberInt(1),
      costo_arancel: 0.00,
      formato_entrega: "Confirmación de registro por correo institucional y lista de asistencia",
      vigencia_meses: NumberInt(4)
    },
    etiquetas: ["taller", "deportes", "cultura", "credito_complementario"]
  },
  {
    id_servicio_sql: NumberInt(4),
    codigo: "SRV-ADM-04",
    nombre_servicio: "Baja Temporal",
    categoria: "Administrativo",
    activo: true,
    modalidades: ["Ventanilla", "En Línea"],
    requisitos: [
      "Carta de exposición de motivos firmada por el estudiante",
      "Constancia de no adeudo institucional completa",
      "Entrevista con el tutor académico"
    ],
    especificaciones: {
      departamento_responsable: "Dirección de División Académica",
      tiempo_estimado_dias: NumberInt(10),
      costo_arancel: 0.00,
      formato_entrega: "Oficio oficial de dictamen de baja temporal",
      vigencia_meses: NumberInt(6)
    },
    etiquetas: ["tramite", "baja", "escolar", "suspension"]
  },
  {
    id_servicio_sql: NumberInt(5),
    codigo: "SRV-ACAD-05",
    nombre_servicio: "Asesoría Académica",
    categoria: "Academico",
    activo: true,
    modalidades: ["Presencial", "En Línea"],
    requisitos: [
      "Solicitud de asesoría indicando materia y temas específicos",
      "Boleta de calificaciones parciales previa"
    ],
    especificaciones: {
      departamento_responsable: "Coordinación de Tutorías y Asesorías",
      tiempo_estimado_dias: NumberInt(2),
      costo_arancel: 0.00,
      formato_entrega: "Agendamiento en plataforma y enlace de sesión virtual / cubículo",
      vigencia_meses: NumberInt(1)
    },
    etiquetas: ["tutoria", "refuerzo", "materias", "docente"]
  },
  {
    id_servicio_sql: NumberInt(6),
    codigo: "SRV-EXT-06",
    nombre_servicio: "Bolsa de Trabajo y Estadías",
    categoria: "Extracurricular",
    activo: true,
    modalidades: ["En Línea"],
    requisitos: [
      "Currículum Vitae en formato institucional UTTT",
      "Constancia de cumplimiento de créditos para estadía",
      "Seguro médico activo"
    ],
    especificaciones: {
      departamento_responsable: "Departamento de Vinculación y Empleabilidad",
      tiempo_estimado_dias: NumberInt(3),
      costo_arancel: 0.00,
      formato_entrega: "Acceso al portal de postulaciones y vinculación empresarial",
      vigencia_meses: NumberInt(12)
    },
    etiquetas: ["empleo", "estadia", "practicas", "vinculacion"]
  },
  {
    id_servicio_sql: NumberInt(7),
    codigo: "SRV-SAL-07",
    nombre_servicio: "Servicio Médico y Psicológico",
    categoria: "Salud_Estudiantil",
    activo: true,
    modalidades: ["Presencial", "En Línea"],
    requisitos: [
      "Credencial de estudiante vigente",
      "Cuestionario de tamizaje de salud inicial"
    ],
    especificaciones: {
      departamento_responsable: "Unidad de Servicios Médicos y Apoyo Psicológico",
      tiempo_estimado_dias: NumberInt(1),
      costo_arancel: 0.00,
      formato_entrega: "Diagnóstico médico / cita de seguimiento clínico",
      vigencia_meses: NumberInt(6)
    },
    etiquetas: ["salud", "medico", "psicologia", "bienestar"]
  },
  {
    id_servicio_sql: NumberInt(8),
    codigo: "SRV-ACAD-08",
    nombre_servicio: "Préstamo Interbibliotecario Digital",
    categoria: "Academico",
    activo: true,
    modalidades: ["En Línea"],
    requisitos: [
      "Cuenta activa en el repositorio digital",
      "Sin multas vigentes por préstamos físicos"
    ],
    especificaciones: {
      departamento_responsable: "Biblioteca Universitaria",
      tiempo_estimado_dias: NumberInt(1),
      costo_arancel: 0.00,
      formato_entrega: "Token de acceso temporal a libros y bases de datos IEEE/Springer",
      vigencia_meses: NumberInt(1)
    },
    etiquetas: ["biblioteca", "libros", "investigacion", "recursos"]
  }
];

const resultado = dbInstance[collectionName].insertMany(servicios);
print(`Total de documentos insertados: ${resultado.insertedCount}`);
print(`IDs generados:`);
printjson(resultado.insertedIds);
