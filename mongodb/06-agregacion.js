/**
 * 06-agregacion.js
 * Misión 2: MongoDB - Sector Documental
 * 
 * Pipeline de agregación analítica sobre los servicios de CampusCloud:
 * - Agrupa por categoría
 * - Calcula total de servicios, promedio de tiempo de respuesta y costo acumulado
 * - Ordena por volumen de servicios
 */

const dbName = 'CampusCloud';
const collectionName = 'detalles_servicios';
const dbInstance = db.getSiblingDB(dbName);

print(`=======================================================`);
print(`[MongoDB] Pipeline de Agregación: Métricas por Categoría`);
print(`=======================================================`);

const pipeline = [
  // 1. Filtrar únicamente servicios activos
  {
    $match: {
      activo: true
    }
  },
  // 2. Agrupar por categoría y calcular métricas acumuladas
  {
    $group: {
      _id: "$categoria",
      total_servicios: { $sum: 1 },
      tiempo_promedio_dias: { $avg: "$especificaciones.tiempo_estimado_dias" },
      costo_promedio_arancel: { $avg: "$especificaciones.costo_arancel" },
      modalidades_disponibles: { $addToSet: "$modalidades" },
      lista_servicios: { $push: "$nombre_servicio" }
    }
  },
  // 3. Proyectar y dar formato a los campos calculados
  {
    $project: {
      categoria: "$_id",
      _id: 0,
      total_servicios: 1,
      tiempo_promedio_dias: { $round: ["$tiempo_promedio_dias", 1] },
      costo_promedio_arancel: { $round: ["$costo_promedio_arancel", 2] },
      lista_servicios: 1
    }
  },
  // 4. Ordenar descendentemente por total de servicios
  {
    $sort: {
      total_servicios: -1
    }
  }
];

const metricas = dbInstance[collectionName].aggregate(pipeline).toArray();
printjson(metricas);
