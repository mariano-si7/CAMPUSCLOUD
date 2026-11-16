/**
 * 01-crear-coleccion.js
 * Misión 2: MongoDB - Sector Documental
 * 
 * Crea la colección 'detalles_servicios' con esquema de validación JSON Schema
 * e índices optimizados para la integración con SQL Server.
 */

const dbName = 'CampusCloud';
const collectionName = 'detalles_servicios';

const dbInstance = db.getSiblingDB(dbName);

print(`=======================================================`);
print(`[MongoDB] Inicializando colección: ${collectionName} en DB: ${dbName}`);
print(`=======================================================`);

// Si la colección existe, se recrea para garantizar entorno limpio
try {
  dbInstance[collectionName].drop();
  print(`Colección previa eliminada correctamente.`);
} catch (e) {
  print(`Colección limpia lista para crearse.`);
}

// Creación de colección con validación JSON Schema
dbInstance.createCollection(collectionName, {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["id_servicio_sql", "codigo", "nombre_servicio", "categoria", "activo", "modalidades", "requisitos", "especificaciones"],
      properties: {
        id_servicio_sql: {
          bsonType: "int",
          description: "ID de referencia exacta a la tabla Servicios de SQL Server (clave externa lógica)"
        },
        codigo: {
          bsonType: "string",
          description: "Código alfanumérico institucional único del servicio (ej. SRV-ACAD-01)"
        },
        nombre_servicio: {
          bsonType: "string",
          description: "Nombre oficial del servicio universitario"
        },
        categoria: {
          enum: ["Academico", "Administrativo", "Extracurricular", "Salud_Estudiantil"],
          description: "Categoría del servicio dentro del catálogo dinámico"
        },
        activo: {
          bsonType: "bool",
          description: "Estado operativo del servicio"
        },
        modalidades: {
          bsonType: "array",
          minItems: 1,
          items: {
            bsonType: "string"
          },
          description: "Modalidades de atención (Presencial, En Línea, Ventanilla, Mixta)"
        },
        requisitos: {
          bsonType: "array",
          items: {
            bsonType: "string"
          },
          description: "Lista de documentos o condiciones obligatorias"
        },
        especificaciones: {
          bsonType: "object",
          required: ["departamento_responsable", "tiempo_estimado_dias", "costo_arancel", "formato_entrega"],
          properties: {
            departamento_responsable: { bsonType: "string" },
            tiempo_estimado_dias: { bsonType: "int" },
            costo_arancel: { bsonType: ["double", "int"] },
            formato_entrega: { bsonType: "string" },
            vigencia_meses: { bsonType: "int" }
          },
          description: "Subdocumento con metadatos técnicos y administrativos"
        },
        etiquetas: {
          bsonType: "array",
          items: { bsonType: "string" },
          description: "Palabras clave para indexación y búsqueda"
        }
      }
    }
  }
});

print(`Colección '${collectionName}' creada con esquema JSON Schema.`);

// Creación de índices
dbInstance[collectionName].createIndex({ codigo: 1 }, { unique: true });
dbInstance[collectionName].createIndex({ id_servicio_sql: 1 });
dbInstance[collectionName].createIndex({ categoria: 1, activo: 1 });
dbInstance[collectionName].createIndex({ "especificaciones.tiempo_estimado_dias": 1 });

print(`Índices creados exitosamente:`);
printjson(dbInstance[collectionName].getIndexes());
