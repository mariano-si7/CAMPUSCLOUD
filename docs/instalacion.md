# Guía de Instalación y Despliegue - CampusCloud Unidad II

## 1. Requisitos Previos

- **Sistema Operativo:** Windows 10/11 (con WSL2 habilitado si aplica)
- **Docker Desktop:** Versión 4.25+ en ejecución.
- **Memoria RAM Mínima Recomendada:** 8 GB (se recomienda levantar los servicios de forma modular para optimizar recursos).
- **Herramientas de Cliente Opcionales:** MongoDB Compass, DBeaver, Neo4j Desktop o clientes web incorporados.

---

## 2. Preparación del Entorno

1. Abrir una terminal de PowerShell en la raíz del repositorio:
   ```powershell
   cd C:\REPOSITORIOS\CampusCloud
   ```

2. Generar el archivo de variables locales a partir de la plantilla:
   ```powershell
   Copy-Item docker\.env.example docker\.env
   ```
   *(El archivo `.env` está protegido en `.gitignore` y nunca se subirá al repositorio).*

---

## 3. Despliegue Modular de Servicios

No es necesario iniciar todos los contenedores al mismo tiempo. Puedes levantar únicamente el motor que desees probar:

### A. Levantar MongoDB (Sector Documental)
```powershell
docker compose -f docker/compose.yaml up -d mongodb
```
- Verificar estado: `docker compose -f docker/compose.yaml ps mongodb`
- Ver logs: `docker compose -f docker/compose.yaml logs mongodb`

### B. Levantar Neo4j (Red de Grafos)
```powershell
docker compose -f docker/compose.yaml up -d neo4j
```
- Acceso Web (Neo4j Browser): `http://localhost:7474`
- Usuario inicial: `neo4j` | Contraseña: la configurada en `.env` (ej. `CampusCloudNeo4j2026!`)

### C. Levantar Apache Cassandra (Sector Columnas Anchas)
```powershell
docker compose -f docker/compose.yaml up -d cassandra
```
- *Nota:* Cassandra tarda aproximadamente 60 segundos en inicializar el nodo en memoria. Verificar con:
  ```powershell
  docker exec -it campuscloud-cassandra nodetool status
  ```

---

## 4. Ejecución de Scripts por Motor

### MongoDB
```powershell
# Ejecutar script de creación de colección:
docker exec -i campuscloud-mongo mongosh -u admin -p CampusCloudMongo2026! --authenticationDatabase admin CampusCloud < mongodb/01-crear-coleccion.js

# Insertar documentos:
docker exec -i campuscloud-mongo mongosh -u admin -p CampusCloudMongo2026! --authenticationDatabase admin CampusCloud < mongodb/02-insertar-documentos.js

# Consultas con filtros:
docker exec -i campuscloud-mongo mongosh -u admin -p CampusCloudMongo2026! --authenticationDatabase admin CampusCloud < mongodb/03-consultas-filtros.js

# Actualización:
docker exec -i campuscloud-mongo mongosh -u admin -p CampusCloudMongo2026! --authenticationDatabase admin CampusCloud < mongodb/04-actualizar.js

# Eliminación:
docker exec -i campuscloud-mongo mongosh -u admin -p CampusCloudMongo2026! --authenticationDatabase admin CampusCloud < mongodb/05-eliminar.js

# Agregación:
docker exec -i campuscloud-mongo mongosh -u admin -p CampusCloudMongo2026! --authenticationDatabase admin CampusCloud < mongodb/06-agregacion.js
```

### Neo4j
```powershell
# Crear nodos y relaciones:
docker exec -i campuscloud-neo4j cypher-shell -u neo4j -p CampusCloudNeo4j2026! < neo4j/01-crear-nodos-relaciones.cypher

# Consultas Cypher:
docker exec -i campuscloud-neo4j cypher-shell -u neo4j -p CampusCloudNeo4j2026! < neo4j/02-consultas.cypher

# Actualización controlada:
docker exec -i campuscloud-neo4j cypher-shell -u neo4j -p CampusCloudNeo4j2026! < neo4j/03-actualizacion.cypher
```

### Apache Cassandra
```powershell
# Crear keyspace y tabla:
docker exec -i campuscloud-cassandra cqlsh < cassandra/01-crear-keyspace-tabla.cql

# Insertar eventos:
docker exec -i campuscloud-cassandra cqlsh < cassandra/02-insertar-eventos.cql

# Consultas:
docker exec -i campuscloud-cassandra cqlsh < cassandra/03-consultas.cql

# Actualización:
docker exec -i campuscloud-cassandra cqlsh < cassandra/04-actualizar.cql

# Eliminación:
docker exec -i campuscloud-cassandra cqlsh < cassandra/05-eliminar.cql
```

---

## 5. Detención de Servicios
```powershell
# Detener un servicio específico sin perder datos:
docker compose -f docker/compose.yaml stop mongodb
docker compose -f docker/compose.yaml stop neo4j
docker compose -f docker/compose.yaml stop cassandra

# Detener todos los contenedores activos:
docker compose -f docker/compose.yaml stop
```
