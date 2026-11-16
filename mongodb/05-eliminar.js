/**
 * 05-eliminar.js
 * Misión 2: MongoDB - Sector Documental
 * 
 * Ejecuta una eliminación controlada por identificador único (código de servicio):
 * - Verifica existencia previa
 * - Ejecuta deleteOne
 * - Demuestra estado antes y después de la operación.
 */

const dbName = 'CampusCloud';
const collectionName = 'detalles_servicios';
const dbInstance = db.getSiblingDB(dbName);

const codigoAEliminar = "SRV-ACAD-08";

print(`=======================================================`);
print(`[MongoDB] Eliminación Controlada de Servicio: ${codigoAEliminar}`);
print(`=======================================================`);

// 1. ESTADO ANTES DE ELIMINAR
print(`\n>>> CONTEO TOTAL ANTES DE ELIMINAR: ${dbInstance[collectionName].countDocuments()}`);
const docAEliminar = dbInstance[collectionName].findOne({ codigo: codigoAEliminar });
print(`Documento a eliminar encontrado:`);
printjson(docAEliminar);

// 2. EJECUCIÓN DE LA ELIMINACIÓN
const resultadoDelete = dbInstance[collectionName].deleteOne({ codigo: codigoAEliminar });
print(`\nResultado del borrado (deletedCount): ${resultadoDelete.deletedCount}`);

// 3. ESTADO DESPUÉS DE ELIMINAR
print(`\n>>> CONTEO TOTAL DESPUÉS DE ELIMINAR: ${dbInstance[collectionName].countDocuments()}`);
const docVerificacion = dbInstance[collectionName].findOne({ codigo: codigoAEliminar });
print(`Búsqueda posterior del código '${codigoAEliminar}': ${docVerificacion ? "Aún existe (ERROR)" : "null (ELIMINADO EXITOSAMENTE)"}`);
