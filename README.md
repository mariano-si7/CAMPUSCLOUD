# CampusCloud: Nube Académica Local

Proyecto integrador de la asignatura **Bases de Datos en la Nube**  
**Universidad Tecnológica de Tula-Tepeji (UTTT)**  
**Alumno:** Mariano Calzadilla Alvarez (Matrícula: 24300700)

---

## 1. Visión General del Proyecto

**CampusCloud** es una arquitectura de datos progresiva orientada al sector educativo superior, diseñada para ilustrar el paradigma de **Persistencia Políglota** (*Polyglot Persistence*):
- **Unidad I (Relacional):** Núcleo transaccional ACID implementado en **Microsoft SQL Server 2022** (con réplica en PostgreSQL), gestionando las tablas centrales `Estudiantes`, `Servicios` y `Solicitudes`.
- **Unidad II (NoSQL - Evaluación 2 / 55 %):** Extensión modular con tres tecnologías NoSQL complementarias que defienden y enriquecen la plataforma sin sustituir la base relacional:
  1. **MongoDB 8.0 (Sector Documental):** Catálogo dinámico con especificaciones flexibles, subdocumentos y arrays.
  2. **Neo4j 5 (Red de Grafos):** Red de conexiones, comunidades, alianzas de estudio y recomendaciones colaborativas.
  3. **Apache Cassandra 4.1 (Sector Columnas Anchas):** Bitácora masiva de telemetría de eventos y auditoría de accesos.

---

## 2. Estructura del Repositorio

Alineado rigurosamente con la *Guía de organización del repositorio CampusCloud* (UTTT):

```
CampusCloud/
├── docker/
│   ├── compose.yaml                     # Compose integrado (SQL Server, Postgres, Mongo, Neo4j, Cassandra)
│   └── .env.example                     # Plantilla de variables de entorno sin secretos
├── docs/
│   ├── arquitectura-campuscloud.md      # Arquitectura políglota y justificación técnica
│   ├── instalacion.md                   # Guía de despliegue modular paso a paso
│   ├── pruebas.md                       # Matriz de pruebas y validación de persistencia
│   ├── comparacion-cloud-local.md       # Comparativa Local vs AWS, Azure y GCP
│   └── reporte/                         # Entregables técnicos de la Unidad I
├── evidencias/
│   └── unidad-ii/                       # Capturas organizadas por tecnología
│       ├── mongodb/
│       ├── neo4j/
│       ├── cassandra/
│       └── generales/
├── mongodb/                             # Scripts ejecutables MongoDB (.js)
│   ├── 01-crear-coleccion.js
│   ├── 02-insertar-documentos.js
│   ├── 03-consultas-filtros.js
│   ├── 04-actualizar.js
│   ├── 05-eliminar.js
│   └── 06-agregacion.js
├── neo4j/                               # Scripts Cypher (.cypher)
│   ├── 01-crear-nodos-relaciones.cypher
│   ├── 02-consultas.cypher
│   └── 03-actualizacion.cypher
├── cassandra/                           # Scripts CQL (.cql)
│   ├── 01-crear-keyspace-tabla.cql
│   ├── 02-insertar-eventos.cql
│   ├── 03-consultas.cql
│   ├── 04-actualizar.cql
│   └── 05-eliminar.cql
├── reportes/
│   └── unidad-ii/                       # Reporte Técnico Oficial (Word y PDF)
│       ├── generate_report_u2.py
│       ├── Calzadilla_Mariano_ReportePracticas_NoSQL.docx
│       └── Calzadilla_Mariano_ReportePracticas_NoSQL.pdf
├── scripts/
│   └── package_submission.py            # Generador del ZIP para Classroom
├── .gitignore                           # Exclusión de archivos sensibles y temporales
├── notasgenerales.md                    # Comandos de apoyo y atajos rápidos
└── README.md
```

---

## 3. Despliegue Rápido con Docker Compose

1. **Configurar variables:**
   ```powershell
   Copy-Item docker\.env.example docker\.env
   ```

2. **Levantar servicios de forma modular:**
   ```powershell
   # Levantar MongoDB:
   docker compose -f docker/compose.yaml up -d mongodb

   # Levantar Neo4j:
   docker compose -f docker/compose.yaml up -d neo4j

   # Levantar Apache Cassandra:
   docker compose -f docker/compose.yaml up -d cassandra
   ```

3. **Verificar estado:**
   ```powershell
   docker compose -f docker/compose.yaml ps
   ```

---

## 4. Ejecución de Prácticas

### Práctica 1: MongoDB
```powershell
docker exec -i campuscloud-mongo mongosh -u admin -p CampusCloudMongo2026! --authenticationDatabase admin CampusCloud < mongodb/01-crear-coleccion.js
docker exec -i campuscloud-mongo mongosh -u admin -p CampusCloudMongo2026! --authenticationDatabase admin CampusCloud < mongodb/02-insertar-documentos.js
docker exec -i campuscloud-mongo mongosh -u admin -p CampusCloudMongo2026! --authenticationDatabase admin CampusCloud < mongodb/03-consultas-filtros.js
docker exec -i campuscloud-mongo mongosh -u admin -p CampusCloudMongo2026! --authenticationDatabase admin CampusCloud < mongodb/04-actualizar.js
docker exec -i campuscloud-mongo mongosh -u admin -p CampusCloudMongo2026! --authenticationDatabase admin CampusCloud < mongodb/05-eliminar.js
docker exec -i campuscloud-mongo mongosh -u admin -p CampusCloudMongo2026! --authenticationDatabase admin CampusCloud < mongodb/06-agregacion.js
```

### Práctica 2: Neo4j
- Acceso Web: [http://localhost:7474](http://localhost:7474) (Usuario: `neo4j` | Clave: `CampusCloudNeo4j2026!`)
- Vía CLI:
```powershell
docker exec -i campuscloud-neo4j cypher-shell -u neo4j -p CampusCloudNeo4j2026! < neo4j/01-crear-nodos-relaciones.cypher
docker exec -i campuscloud-neo4j cypher-shell -u neo4j -p CampusCloudNeo4j2026! < neo4j/02-consultas.cypher
docker exec -i campuscloud-neo4j cypher-shell -u neo4j -p CampusCloudNeo4j2026! < neo4j/03-actualizacion.cypher
```

### Práctica 3: Apache Cassandra
```powershell
docker exec -i campuscloud-cassandra cqlsh < cassandra/01-crear-keyspace-tabla.cql
docker exec -i campuscloud-cassandra cqlsh < cassandra/02-insertar-eventos.cql
docker exec -i campuscloud-cassandra cqlsh < cassandra/03-consultas.cql
docker exec -i campuscloud-cassandra cqlsh < cassandra/04-actualizar.cql
docker exec -i campuscloud-cassandra cqlsh < cassandra/05-eliminar.cql
```
