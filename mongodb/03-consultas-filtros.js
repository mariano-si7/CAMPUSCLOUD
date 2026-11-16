/**
 * 03-consultas-filtros.js
 * Misión 2: MongoDB - Sector Documental
 * 
 * Ejecuta al menos 3 consultas con filtros avanzados diferentes:
 * 1. Filtro por elemento dentro de un array ($in / coincidencia exacta)
 * 2. Filtro sobre propiedades de subdocumentos con operadores de comparación ($lte, $gt)
 * 3. Filtro compuesto con operadores lógicos ($and, $or) y proyección selectiva
 */

const dbName = 'CampusCloud';
const collectionName = 'detalles_servicios';
const dbInstance = db.getSiblingDB(dbName);

print(`=======================================================`);
print(`[MongoDB] Ejecución de Consultas con Filtros Avanzados`);
print(`=======================================================`);

// Consulta 1: Filtro por elemento dentro de un array
print(`\n--- CONSULTA 1: Servicios disponibles en modalidad 'En Línea' ---`);
const consulta1 = dbInstance[collectionName].find(
  { modalidades: "En Línea", activo: true },
  { codigo: 1, nombre_servicio: 1, categoria: 1, modalidades: 1, "especificaciones.tiempo_estimado_dias": 1, _id: 0 }
).toArray();
printjson(consulta1);
print(`Total encontrados: ${consulta1.length}`);

// Consulta 2: Filtro por campo dentro del subdocumento 'especificaciones'
print(`\n--- CONSULTA 2: Servicios ágiles (tiempo estimado <= 2 días) ---`);
const consulta2 = dbInstance[collectionName].find(
  { "especificaciones.tiempo_estimado_dias": { $lte: 2 } },
  { codigo: 1, nombre_servicio: 1, "especificaciones.departamento_responsable": 1, "especificaciones.tiempo_estimado_dias": 1, _id: 0 }
).sort({ "especificaciones.tiempo_estimado_dias": 1 }).toArray();
printjson(consulta2);
print(`Total encontrados: ${consulta2.length}`);

// Consulta 3: Filtro lógico compuesto ($and, $or) con aranceles y categorías
print(`\n--- CONSULTA 3: Servicios gratuitos de categoría 'Academico' o 'Extracurricular' ---`);
const consulta3 = dbInstance[collectionName].find(
  {
    $and: [
      { "especificaciones.costo_arancel": 0.00 },
      { $or: [{ categoria: "Academico" }, { categoria: "Extracurricular" }] }
    ]
  },
  { codigo: 1, nombre_servicio: 1, categoria: 1, "especificaciones.costo_arancel": 1, etiquetas: 1, _id: 0 }
).toArray();
printjson(consulta3);
print(`Total encontrados: ${consulta3.length}`);
