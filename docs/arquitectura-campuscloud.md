# Arquitectura Técnica Políglota - CampusCloud (Unidad II)

## 1. Visión General y Filosofía de Persistencia Políglota

CampusCloud ha evolucionado de un modelo puramente relacional (Unidad I) hacia una **arquitectura de persistencia políglota** (*Polyglot Persistence*). Bajo este enfoque, no se sustituye el motor relacional principal (Microsoft SQL Server), sino que se complementa con tres motores NoSQL especializados, asignando a cada tecnología la carga de trabajo para la que fue diseñada:

```
                                  [ CLIENTE / ALUMNOS / DOCENTES ]
                                                │
                                                ▼
                             ┌─────────────────────────────────────┐
                             │       RED: campuscloud-db-net       │
                             └──────────────────┬──────────────────┘
                                                │
         ┌─────────────────────────┬────────────┴────────────┬─────────────────────────┐
         │                         │                         │                         │
         ▼                         ▼                         ▼                         ▼
┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│    SQL SERVER    │      │     MONGODB      │      │      NEO4J       │      │ CASSANDRA / CQL  │
│  (Relacional)    │      │  (Documental)    │      │     (Grafos)     │      │ (Columnas Anchas)│
├──────────────────┤      ├──────────────────┤      ├──────────────────┤      ├──────────────────┤
│• Estudiantes     │      │• Detalles        │      │• Nodos Alumno    │      │• Telemetría      │
│• Servicios       │◄────►│  Extendidos      │◄────►│• Nodos Servicio  │◄────►│• Auditoría de    │
│• Solicitudes     │      │• Requisitos      │      │• Red de Alianzas │      │  Eventos Masivos │
│• Transacciones   │      │• Especificaciones│      │• Recomendaciones │      │• Latencias e IPs │
│  ACID Críticas   │      │• Costos / Arrays │      │• Comunidades     │      │• Consultas por PK│
└──────────────────┘      └──────────────────┘      └──────────────────┘      └──────────────────┘
   Puerto: 1434               Puerto: 27017            Puertos: 7474/7687          Puerto: 9042
```

---

## 2. Matriz de Roles y Responsabilidades de Almacenamiento

| Motor | Modelo de Datos | Caso de Uso en CampusCloud | Entidades Principales | Justificación Técnica |
| :--- | :--- | :--- | :--- | :--- |
| **SQL Server 2022** | Relacional (RDBMS) | Integridad transaccional y catálogo base | `Estudiantes`, `Servicios`, `Solicitudes` | Garantía estricta de propiedades ACID, claves foráneas e integridad referencial institucional. |
| **MongoDB 8.0** | Documental (BSON / JSON) | Catálogo dinámico con especificaciones variables | `detalles_servicios` | Esquema flexible; soporte nativo para arrays de requisitos y subdocumentos de especificaciones. |
| **Neo4j 5** | Grafo de Propiedades (LPG) | Red social académica y recomendación | `(:Estudiante)`, `(:Servicio)`, `[:SOLICITA]`, `[:COLABORA_CON]` | Consultas Cypher eficientes en recorridos de relaciones sin costosos JOINs cruzados recursivos. |
| **Apache Cassandra 4.1** | Columnas Anchas (Wide-Column) | Bitácora de telemetría de eventos y auditoría | `eventos_estudiante` | Alta velocidad de escritura masiva en append-only (SSTables), escalabilidad horizontal y consultas de series de tiempo agrupadas por partición de estudiante. |

---

## 3. Red y Almacenamiento Persistente en Docker

- **Red Compartida:** `campuscloud-db-net` (aislamiento seguro para comunicación entre contenedores por nombre DNS).
- **Volúmenes Persistentes Independientes:**
  - `campuscloud-sqlserver-data` $\rightarrow$ `/var/opt/mssql`
  - `campuscloud-postgres-data` $\rightarrow$ `/var/lib/postgresql/data`
  - `campuscloud-pgadmin-data` $\rightarrow$ `/var/lib/pgadmin`
  - `campuscloud-mongo-data` $\rightarrow$ `/data/db`
  - `campuscloud-neo4j-data` $\rightarrow$ `/data`
  - `campuscloud-cassandra-data` $\rightarrow$ `/var/lib/cassandra`
