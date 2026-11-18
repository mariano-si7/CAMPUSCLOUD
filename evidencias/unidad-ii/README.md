# Índice y Nomenclatura de Evidencias - CampusCloud Unidad II

Alineado con la Sección 4 de la *Guía de organización del repositorio CampusCloud (UTTT)*:

## 1. MongoDB (`evidencias/unidad-ii/mongodb/`)
- `01-conexion.png`: Conexión exitosa a MongoDB mediante mongosh / Compass.
- `02-documentos-insertados.png`: Salida de ejecución de `02-insertar-documentos.js` con los 8 documentos cargados.
- `03-consultas-filtros.png`: Salida de las 3 consultas con filtros (arrays, subdocumentos y lógica compuesta).
- `04-actualizacion-antes-despues.png`: Evidencia visual del documento `SRV-ACAD-01` antes y después de ejecutar `04-actualizar.js`.
- `05-eliminacion.png`: Evidencia del conteo previo (8) y posterior (7) al eliminar `SRV-ACAD-08`.
- `06-agregacion.png`: Salida del pipeline de agregación con promedios y conteos por categoría.
- `07-persistencia.png`: Comprobación de conteo de documentos antes y después del reinicio del contenedor.
- `08-autenticacion.png`: Acceso mediante usuario administrativo autenticado en admin.

## 2. Neo4j (`evidencias/unidad-ii/neo4j/`)
- `01-conexion-browser.png`: Acceso a la interfaz web Neo4j Browser (`localhost:7474`).
- `02-nodos-relaciones-grafo.png`: Visualización gráfica de la red completa (nodos Estudiante, Servicio y relaciones).
- `03-consulta-servicios-estudiante.png`: Tabla de resultados de servicios solicitados por Mariano Calzadilla Alvarez (`2026001`).
- `04-consulta-estudiantes-compartidos.png`: Identificación de alumnos que comparten el taller extracurricular.
- `05-consulta-recomendacion.png`: Salida de la recomendación de servicios basada en colaboradores afines.
- `06-actualizacion-antes-despues.png`: Modificación del estado de solicitud y nueva alianza creada.
- `07-persistencia.png`: Verificación del grafo tras reiniciar el contenedor `campuscloud-neo4j`.

## 3. Apache Cassandra (`evidencias/unidad-ii/cassandra/`)
- `01-conexion-cqlsh.png`: Conexión al cluster `CampusCloudCluster` mediante `cqlsh`.
- `02-creacion-keyspace-tabla.png`: Ejecución de `01-crear-keyspace-tabla.cql` y salida del `DESCRIBE TABLE`.
- `03-insercion-eventos.png`: Inserción de los 15 eventos masivos de telemetría.
- `04-consulta-particion.png`: Consulta de eventos del alumno `2026001` ordenados por fecha descendente.
- `05-consulta-rango-fechas.png`: Filtrado por intervalo de fechas (`01 al 05 de Nov`).
- `06-actualizacion-cql.png`: Ejecución de UPDATE con Primary Key completa antes y después.
- `07-eliminacion-cql.png`: Ejecución de DELETE y comprobación de supresión.

## 4. Generales (`evidencias/unidad-ii/generales/`)
- `01-docker-compose-ps.png`: Estado de los contenedores (`Up` y puertos publicados).
- `02-docker-volumes.png`: Listado de volúmenes persistentes con `docker volume ls`.
- `03-docker-network.png`: Inspección de la red `campuscloud-db-net` conectando los contenedores.
