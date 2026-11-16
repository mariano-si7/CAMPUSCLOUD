/**
 * 04-actualizar.js
 * Misión 2: MongoDB - Sector Documental
 * 
 * Ejecuta una actualización controlada sobre un servicio:
 * - Modifica propiedades del subdocumento 'especificaciones' ($set)
 * - Añade un nuevo requisito sin duplicar mediante ($addToSet)
 * - Muestra el estado del documento ANTES y DESPUÉS de la operación.
 */

const dbName = 'CampusCloud';
const collectionName = 'detalles_servicios';
const dbInstance = db.getSiblingDB(dbName);

const codigoObjetivo = "SRV-ACAD-01";

print(`=======================================================`);
print(`[MongoDB] Actualización Controlada de Servicio: ${codigoObjetivo}`);
print(`=======================================================`);

// 1. ESTADO ANTES DE LA ACTUALIZACIÓN
print(`\n>>> ESTADO PREVIO DEL DOCUMENTO:`);
const docAntes = dbInstance[collectionName].findOne({ codigo: codigoObjetivo });
printjson(docAntes);

// 2. EJECUCIÓN DE LA ACTUALIZACIÓN
const resultadoUpdate = dbInstance[collectionName].updateOne(
  { codigo: codigoObjetivo },
  {
    $set: {
      "especificaciones.tiempo_estimado_dias": NumberInt(2),
      "especificaciones.formato_entrega": "Digital PDF con firma electrónica avanzada, código QR y validación blockchain",
      "ultima_actualizacion": new Date()
    },
    $addToSet: {
      requisitos: "Identificación oficial escaneada en formato PDF",
      etiquetas: "blockchain"
    }
  }
);

print(`\nResultado de la operación de actualización:`);
print(`- Coincidentes (matchedCount): ${resultadoUpdate.matchedCount}`);
print(`- Modificados (modifiedCount): ${resultadoUpdate.modifiedCount}`);

// 3. ESTADO DESPUÉS DE LA ACTUALIZACIÓN
print(`\n>>> ESTADO POSTERIOR DEL DOCUMENTO ACTUALIZADO:`);
const docDespues = dbInstance[collectionName].findOne({ codigo: codigoObjetivo });
printjson(docDespues);
