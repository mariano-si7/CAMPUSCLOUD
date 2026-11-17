# Matriz de Pruebas y Evidencias de Operación - CampusCloud Unidad II

Este documento registra la batería de pruebas funcionales, resultados obtenidos y validación de persistencia para los tres motores NoSQL de CampusCloud.

---

## 1. Misión 2: MongoDB (Sector Documental)

### Matriz de Ejecución de Pruebas

| Identificador | Operación | Comando / Script | Resultado Esperado | Validación Técnica |
| :--- | :--- | :--- | :--- | :--- |
| **TEST-MDB-01** | Creación de Colección | `mongodb/01-crear-coleccion.js` | Colección `detalles_servicios` con validador JSON Schema y 4 índices. | `ok: 1`, índices creados para `codigo`, `id_servicio_sql`, etc. |
| **TEST-MDB-02** | Carga de Documentos | `mongodb/02-insertar-documentos.js` | Inserción de 8 documentos extendidos vinculados a los servicios relacionales. | `insertedCount: 8`. |
| **TEST-MDB-03** | Consulta Filtro Array | `mongodb/03-consultas-filtros.js` (Q1) | Retorna servicios con modalidad `"En Línea"` (Certificado, Asesoría, Bolsa, etc.). | 5 servicios recuperados. |
| **TEST-MDB-04** | Consulta Filtro Subdoc | `mongodb/03-consultas-filtros.js` (Q2) | Retorna servicios con `tiempo_estimado_dias <= 2`. | 3 servicios ágiles ordenados ascendentemente. |
| **TEST-MDB-05** | Consulta Filtro Lógico | `mongodb/03-consultas-filtros.js` (Q3) | Retorna servicios gratuitos de categorías `Academico` o `Extracurricular`. | 3 servicios coincidentes. |
| **TEST-MDB-06** | Actualización Controlada | `mongodb/04-actualizar.js` | Modifica `SRV-ACAD-01` reduciendo días a 2 y agregando requisito con `$addToSet`. | `matchedCount: 1`, `modifiedCount: 1`. |
| **TEST-MDB-07** | Eliminación Controlada | `mongodb/05-eliminar.js` | Elimina servicio `SRV-ACAD-08`. Conteo pasa de 8 a 7. | `deletedCount: 1`, búsqueda posterior retorna `null`. |
| **TEST-MDB-08** | Pipeline Agregación | `mongodb/06-agregacion.js` | Conteo, tiempo promedio y costo promedio por categoría. | Métricas agrupadas para `Academico`, `Administrativo`, etc. |

### Prueba de Persistencia MongoDB
1. Contar documentos: `db.detalles_servicios.countDocuments()` $\rightarrow$ Retorna `7`.
2. Reiniciar contenedor:
   ```powershell
   docker restart campuscloud-mongo
   ```
3. Re-conectar y verificar: Los 7 documentos y sus índices persisten intactos en el volumen `campuscloud-mongo-data`.

---

## 2. Misión 3: Neo4j (Red de Grafos Vengadora)

### Matriz de Ejecución de Pruebas

| Identificador | Operación | Comando / Script | Resultado Esperado | Validación Técnica |
| :--- | :--- | :--- | :--- | :--- |
| **TEST-NEO-01** | Creación del Grafo | `neo4j/01-crear-nodos-relaciones.cypher` | 6 Nodos `:Estudiante`, 5 Nodos `:Servicio`, 17 Relaciones (`:SOLICITA`, `:COLABORA_CON`, etc.). | `Added 11 nodes, 17 relationships`. |
| **TEST-NEO-02** | Consulta Servicios Alumno | `neo4j/02-consultas.cypher` (Q1) | Historial de solicitudes de Mariano Silva (`24300700`). | 2 servicios: Certificado (5 estrellas) y Taller (4 estrellas). |
| **TEST-NEO-03** | Detección de Comunidades | `neo4j/02-consultas.cypher` (Q2) | Estudiantes que comparten `Inscripción a Taller`. | Mariano Silva, Carlos Gomez y Fernanda Torres identificados como compañeros de servicio. |
| **TEST-NEO-04** | Recomendación Colaborativa | `neo4j/02-consultas.cypher` (Q3) | Servicios de colaboradores afines sugeridos a Mariano. | Sugiere `Asesoría Académica` (solicitada con éxito por su colaboradora Ana Martinez). |
| **TEST-NEO-05** | Actualización de Grafo | `neo4j/03-actualizacion.cypher` | Transiciona estado de solicitud a `Aprobada` y agrega nueva alianza. | `Set 4 properties, Added 1 relationship`. |

### Prueba de Persistencia Neo4j
1. Verificar conteo de nodos y aristas con `MATCH (n) RETURN count(n)`.
2. Reiniciar contenedor:
   ```powershell
   docker restart campuscloud-neo4j
   ```
3. Re-conectar a Neo4j Browser (`http://localhost:7474`): Los nodos, aristas y propiedades persisten en el volumen `campuscloud-neo4j-data`.

---

## 3. Misión 4: Apache Cassandra (Sector Columnas Anchas)

### Matriz de Ejecución de Pruebas

| Identificador | Operación | Comando / Script | Resultado Esperado | Validación Técnica |
| :--- | :--- | :--- | :--- | :--- |
| **TEST-CAS-01** | Creación de Keyspace y Tabla | `cassandra/01-crear-keyspace-tabla.cql` | Keyspace `campuscloud_logs` y tabla `eventos_estudiante` con PK `((matricula), fecha_hora, id_evento)`. | Tabla creada con `CLUSTERING ORDER BY (fecha_hora DESC)`. |
| **TEST-CAS-02** | Carga de Eventos Masivos | `cassandra/02-insertar-eventos.cql` | 15 eventos registrados para 3 estudiantes (`24300700`, `2026002`, `2026003`). | `count(*) = 15`. |
| **TEST-CAS-03** | Consulta Partición Completa | `cassandra/03-consultas.cql` (Q1) | Todos los eventos de Mariano Silva ordenados del más reciente al más antiguo. | 5 eventos ordenados desc por `fecha_hora`. |
| **TEST-CAS-04** | Consulta Rango de Fechas | `cassandra/03-consultas.cql` (Q2) | Eventos de Mariano Silva entre `2026-11-01` y `2026-11-05`. | 3 eventos recuperados de forma secuencial. |
| **TEST-CAS-05** | UPDATE con PK Completa | `cassandra/04-actualizar.cql` | Actualiza estado a `APROBADA` y latencia a `85 ms` para evento de Ana Martinez. | Registro actualizado atómicamente por clave compuesta. |
| **TEST-CAS-06** | DELETE con PK Completa | `cassandra/05-eliminar.cql` | Elimina evento fallido de Carlos Gomez. | Registro ocultado mediante Tombstone; total restante para ese alumno: 4. |

---

## 4. Diagnóstico de Incidencia Resuelta

- **Incidencia Detectada:** Error `External filter 'git-lfs filter-process' failed / Smudge error 404` al integrar el repositorio de trabajo colaborativo debido a punteros Git LFS de imágenes locales (`docker_images/neo.tar`).
- **Causa Raíz:** El objeto binario pesado de 592 MB no se encontraba sincronizado en el almacenamiento remoto de Git LFS.
- **Solución Implementada:** Se configuró el filtro local de Git LFS con omisión de smudge (`git-lfs smudge --skip`) y variable de entorno `$env:GIT_LFS_SKIP_SMUDGE="1"`, permitiendo una descarga e integración fluida y limpia del código fuente sin romper el entorno de desarrollo.
