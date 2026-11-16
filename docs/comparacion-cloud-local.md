# Comparativa Estratégica: Despliegue Local vs Servicios Administrados en la Nube

## 1. Fundamentos: ¿Por qué Docker Local no es un Servicio Administrado?

El despliegue de contenedores en una estación de trabajo mediante Docker Compose representa un entorno de **Infraestructura como Servicio (IaaS) simulada o autocontenida**. En este modelo, el desarrollador o administrador asume el 100% de la carga operativa:

- Provisión y asignación de memoria/CPU física.
- Gestión manual del ciclo de vida del contenedor y reinicios.
- Definición de volúmenes persistentes locales en el sistema de archivos del host.
- Ausencia de alta disponibilidad (si el host se apaga o falla el disco, la base de datos se interrumpe).
- Mantenimiento manual de copias de seguridad (*backups*).

Por el contrario, un **Servicio Administrado en la Nube (Database as a Service - DBaaS)** traslada la gestión de la infraestructura física, el sistema operativo, la replicación multi-zona y la recuperación ante desastres al proveedor de nube, permitiendo al equipo enfocarse en el modelo de datos y las consultas.

---

## 2. Mapa de Tecnologías NoSQL: Local vs Nube Pública

| Paradigma NoSQL | Implementación Local CampusCloud | Alternativa en Amazon Web Services (AWS) | Alternativa en Microsoft Azure | Alternativa en Google Cloud Platform (GCP) |
| :--- | :--- | :--- | :--- | :--- |
| **Documental** | **MongoDB 8.0** *(Contenedor Community)* | **Amazon DocumentDB** *(Compatible con MongoDB, cluster multi-AZ, almacenamiento distribuido de 6 copias)* | **Azure Cosmos DB** *(API for MongoDB, distribución global llave en mano con SLA de 99.999%)* | **Google Cloud Firestore** *(Base de datos documental serverless con sincronización en tiempo real)* |
| **Grafos** | **Neo4j 5** *(Contenedor Community)* | **Amazon Neptune** *(Motor de grafos administrado de alto rendimiento para Apache TinkerPop y SPARQL)* | **Azure Cosmos DB** *(API for Gremlin, grafos a escala masiva)* | **Google Cloud Spanner Graph** *(Grafos integrados a escala planetaria con consistencia fuerte)* |
| **Columnas Anchas** | **Apache Cassandra 4.1** *(Contenedor)* | **Amazon Keyspaces** *(Serverless, compatible con CQL, escalado automático de capacidad y pago por solicitud)* | **Azure Managed Instance for Apache Cassandra** *(Instancias dedicadas con control nativo de nodos)* | **Google Cloud Bigtable** *(Motor columnar de ultra baja latencia para analítica masiva y telemetría)* |

---

## 3. Matriz de Responsabilidad Compartida (Local vs Nube Administrada)

```
NIVEL DE ARQUITECTURA                 DESPLIEGUE LOCAL DOCKER         SERVICIO NUBE DBaaS (AWS/Azure/GCP)
──────────────────────────────────────────────────────────────────────────────────────────────────────────
Diseño de Esquemas y Consultas        [ Cliente / Alumno ]            [ Cliente / Alumno ]
Optimización de Índices               [ Cliente / Alumno ]            [ Cliente / Alumno ]
Control de Acceso y Roles (RBAC)      [ Cliente / Alumno ]            [ Cliente / Alumno ]
Gestión de Secretos / Credenciales    [ Cliente / Alumno ]            [ Cliente / Alumno (KMS / Vault) ]
──────────────────────────────────────────────────────────────────────────────────────────────────────────
Copias de Seguridad (Backups)         [ MANUAL / Cliente ]            [ AUTOMATIZADO por Proveedor ]
Replicación y Alta Disponibilidad     [ MANUAL / Sin soporte ]        [ AUTOMATIZADO Multi-AZ / Multi-Región ]
Parches de Seguridad del Motor        [ MANUAL / Cliente ]            [ AUTOMATIZADO por Proveedor ]
Mantenimiento del Sistema Operativo   [ MANUAL / Host Windows ]       [ GESTIONADO por Proveedor ]
Reemplazo de Hardware y Discos        [ MANUAL / Host Windows ]       [ 100% TRANSPARENTE por Proveedor ]
```

---

## 4. Conclusiones del Contraste Técnico

1. **Para Fase de Desarrollo y Aprendizaje (CampusCloud Local):**
   Docker Compose es insustituible por su costo cero, portabilidad inmediata, aislamiento y reproducibilidad exacta entre entornos de compañeros de equipo.
2. **Para Entorno de Producción Universitario:**
   Migrar a **Amazon Keyspaces** para los eventos masivos, **Azure Cosmos DB** para el catálogo documental y **Amazon Neptune** para la red de alianzas eliminaría la complejidad del mantenimiento de clusters de Cassandra, garantizaría escalabilidad automática ante picos de inscripciones y cumpliría con normativas de protección de datos personales mediante cifrado en reposo y tránsito automático.
