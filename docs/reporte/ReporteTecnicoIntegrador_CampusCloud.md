# UNIVERSIDAD TECNOLÓGICA DE TULA-TEPEJI
## CARRERA: TECNOLOGÍAS DE LA INFORMACIÓN
### ASIGNATURA: BASES DE DATOS EN LA NUBE
**UNIDAD I:** Bases de datos relacionales en la nube  
**ACTIVIDAD DE EVALUACIÓN 3:** Reporte técnico integrador - De CampusCloud local a la nube administrada  
**ESTUDIANTE:** Mariano Silva  
**GRUPO:** TI - Bases de Datos en la Nube  
**DOCENTE:** Mtro. Asignatura  
**FECHA:** Octubre 2026  

---

# ÍNDICE GENERAL
1. Introducción
2. Arquitectura Implementada (Local y Remota)
3. Configuración del Servicio (Docker y SQL Server)
4. Modelo de Datos CampusCloud (Entidades, Relaciones y Diccionario)
5. Creación y Manipulación de Datos (Operaciones CRUD y Consultas Complejas)
6. Persistencia de Datos
7. Usuarios, Roles y Privilegios (Principio de Mínimo Privilegio)
8. Conectividad Remota Colaborativa
9. Problemas Encontrados y Soluciones Aplicadas (Casos Reales)
10. De Nuestra Nube Local a la Nube Real (Comparativa Multi-Cloud)
11. Matriz de Responsabilidad Compartida (¿Qué administra cada uno?)
12. Conclusiones Técnicas
13. Fuentes de Información y Referencias Oficiales

---

# 1. Introducción

El presente reporte técnico documenta de manera integral el diseño, despliegue, gestión y análisis arquitectónico de **CampusCloud**, una solución universitaria de servicios digitales basada en una base de datos relacional desplegada en una **Nube Académica Local**. Durante el desarrollo de la Unidad I de la asignatura *Bases de Datos en la Nube*, se configuró y administró un motor de base de datos **Microsoft SQL Server 2025** sobre contenedores **Docker**, respaldado por almacenamiento persistente mediante volúmenes independientes y segmentación de red.

El objetivo central de este documento es transferir la experiencia práctica obtenida en un entorno local de contenedores hacia los paradigmas de infraestructura y servicios de bases de datos administradas (*Database as a Service* - DBaaS) en los principales proveedores de nube pública: **Amazon Web Services (AWS)**, **Microsoft Azure** y **Google Cloud Platform (GCP)**. 

A través de esta documentación, se asume la perspectiva de un ingeniero del área de Tecnologías de la Información (TI) que evalúa la viabilidad técnica, operativa y de seguridad para migrar un sistema institucional desde servidores físicos y contenedores locales hacia plataformas escalables y de alta disponibilidad en la nube, delimitando claramente qué responsabilidades operativas permanecen en la organización y cuáles son delegadas al proveedor cloud.

---

# 2. Arquitectura Implementada

La solución de CampusCloud fue diseñada bajo una arquitectura modular desacoplada mediante contenedores Docker, permitiendo dos modalidades de consumo: **Conexión Local** (desarrollo y pruebas internas) y **Conexión Remota Cruzada** (consumo colaborativo cliente-servidor en red de área local).

```
[ ARQUITECTURA LOCAL ]
+-----------------------------------------------------------------------------+
| HOST LOCAL (PC Windows - IP: 10.50.149.121)                                 |
|                                                                             |
|   +-----------------------+            +--------------------------------+   |
|   | Cliente SQL Local     |            | Docker Engine 29.x             |   |
|   | (SSMS / DBeaver /     |            |                                |   |
|   |  Azure Data Studio)   |            |  +--------------------------+  |   |
|   +-----------+-----------+            |  | Contenedor SQL Server    |  |   |
|               |                        |  | campuscloud-sqlserver    |  |   |
|               | localhost:1434         |  |                          |  |   |
|               +----------------------->|  | Puerto Interno: 1433     |  |   |
|                                        |  | Base de Datos:           |  |   |
|                                        |  |   CampusCloud            |  |   |
|                                        |  +-------------+------------+  |   |
|                                        |                |               |   |
|                                        |  +-------------v------------+  |   |
|                                        |  | Volumen Docker           |  |   |
|                                        |  | campuscloud-sqlserver-   |  |   |
|                                        |  | data (/var/opt/mssql)    |  |   |
|                                        |  +--------------------------+  |   |
|                                        +--------------------------------+   |
+-----------------------------------------------------------------------------+

[ ARQUITECTURA REMOTA COLABORATIVA ]
+----------------------------+                     +--------------------------+
| CLIENTE REMOTO             |   Red Wi-Fi / LAN   | SERVIDOR CAMPUSCLOUD     |
| (Laptop Compañero - PC B)  |====================>| (PC Estudiante A)        |
| DBeaver / SSMS             |  TCP 10.50.149.121  | Docker SQL Server :1434  |
| Usuario: user_consulta     |     Puerto 1434     | DB: CampusCloud          |
+----------------------------+                     +--------------------------+
```

### Componentes de la Arquitectura:
- **Host Servidor:** Equipo físico con Windows 11 ejecutando Docker Engine 29.2.
- **Dirección IP de Red Local (Wi-Fi):** `10.50.149.121`
- **Puerto Publicado en Host:** `1434` (mapeado bidireccionalmente hacia el puerto estándar de SQL Server `1433/tcp`).
- **Contenedor:** `campuscloud-sqlserver` basado en la imagen oficial `mcr.microsoft.com/mssql/server:2025-CU8-ubuntu-24.04`.
- **Almacenamiento Persistente:** Volumen Docker con nombre `campuscloud-sqlserver-data` montado en `/var/opt/mssql`.
- **Red Aislada de Docker:** `campuscloud-db-net` (control de tráfico bridge).
- **Clientes SQL Utilizados:** SQL Server Management Studio (SSMS), Azure Data Studio, DBeaver y la utilidad de consola `/opt/mssql-tools18/bin/sqlcmd`.
- **Base de Datos:** `CampusCloud`.

---

# 3. Configuración del Servicio

El servicio de base de datos relacional se orquestó de forma declarativa mediante **Docker Compose**, lo que garantiza que la infraestructura sea reproducible, versionable e independiente de configuraciones manuales propensas a errores.

### Fragmento de Configuración (`compose/docker-compose.yml`):
```yaml
services:
  sqlserver-cloud:
    image: mcr.microsoft.com/mssql/server:2025-CU8-ubuntu-24.04
    container_name: campuscloud-sqlserver
    restart: always
    environment:
      ACCEPT_EULA: "Y"
      MSSQL_SA_PASSWORD: ${MSSQL_SA_PASSWORD}
    ports:
      - "${SQLSERVER_PORT}:1433"
    volumes:
      - sqlserver_data:/var/opt/mssql
    networks:
      - campuscloud_net
    healthcheck:
      test: [
        "CMD-SHELL",
        "/opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P '${MSSQL_SA_PASSWORD}' -C -Q 'SELECT 1' || exit 1"
      ]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 15s

volumes:
  sqlserver_data:
    external: true
    name: ${SQLSERVER_VOLUME}

networks:
  campuscloud_net:
    external: true
    name: ${DOCKER_NETWORK}
```

### Resumen Técnico de Parámetros:

| Aspecto | Configuración Implementada | Justificación Técnica |
|---|---|---|
| **Imagen Base** | `mcr.microsoft.com/mssql/server:2025-CU8-ubuntu-24.04` | Imagen oficial empresarial optimizada sobre Linux Ubuntu LTS. |
| **Nombre Contenedor** | `campuscloud-sqlserver` | Identificador estandarizado dentro del namespace local de Docker. |
| **Puertos (Host:Contenedor)** | `1434:1433` | Permite evitar conflictos de enlace en caso de existir instancias nativas previas en el puerto 1433. |
| **Variables de Entorno** | `ACCEPT_EULA=Y`<br>`MSSQL_SA_PASSWORD=sqlserver2026!` | Cumplimiento de licenciamiento y fijación de contraseña que supera las políticas de complejidad de Microsoft (mínimo 8 caracteres, mayúsculas, minúsculas, números y símbolos). |
| **Almacenamiento** | `campuscloud-sqlserver-data` | Volumen administrado para persistir los archivos maestros y de datos (`.mdf`, `.ldf`). |
| **Healthcheck** | `sqlcmd -Q 'SELECT 1'` | Verificación activa para asegurar que el motor de base de datos ha concluido la inicialización antes de recibir conexiones. |
| **Comandos Operativos** | `docker compose up -d`<br>`docker compose down`<br>`docker restart campuscloud-sqlserver` | Ciclo de vida estandarizado en consola. |

---

# 4. Modelo de Datos CampusCloud

La base de datos **CampusCloud** fue estructurada para gestionar solicitudes de servicios universitarios realizadas por la comunidad estudiantil, garantizando integridad referencial, unicidad y reglas de negocio sólidas.

```
+--------------------+            +--------------------+
|    Estudiantes     |            |     Servicios      |
+--------------------+            +--------------------+
| PK  IdEstudiante   |            | PK  IdServicio     |
|     Matricula      |            |     NombreServicio |
|     Nombre         |            |     Descripcion    |
|     Correo         |            |     Activo         |
+---------+----------+            +---------+----------+
          |                                 |
          | 1                               | 1
          |                                 |
          | N                               | N
+---------v---------------------------------v----------+
|                    Solicitudes                       |
+------------------------------------------------------+
| PK  IdSolicitud                                      |
| FK  IdEstudiante  -------------------> Estudiantes   |
| FK  IdServicio    -------------------> Servicios     |
|     FechaSolicitud                                   |
|     Estado                                           |
+------------------------------------------------------+
```

### Diccionario de Datos:

1. **Tabla: `Estudiantes`**
   - `IdEstudiante` (`INT`, `IDENTITY(1,1)`, `PRIMARY KEY`): Identificador correlativo interno.
   - `Matricula` (`VARCHAR(20)`, `NOT NULL`, `UNIQUE`): Código único institucional del alumno.
   - `Nombre` (`VARCHAR(100)`, `NOT NULL`): Nombre completo del estudiante.
   - `Correo` (`VARCHAR(100)`, `NOT NULL`, `UNIQUE`): Correo electrónico institucional.

2. **Tabla: `Servicios`**
   - `IdServicio` (`INT`, `IDENTITY(1,1)`, `PRIMARY KEY`): Identificador del trámite académico.
   - `NombreServicio` (`VARCHAR(100)`, `NOT NULL`): Denominación oficial del servicio.
   - `Descripcion` (`VARCHAR(255)`, `NOT NULL`): Detalle del alcance del servicio.
   - `Activo` (`BIT`, `NOT NULL`, `DEFAULT 1`): Bandera lógica (1=Disponible, 0=Inactivo).

3. **Tabla: `Solicitudes`**
   - `IdSolicitud` (`INT`, `IDENTITY(1,1)`, `PRIMARY KEY`): Número de folio de la solicitud.
   - `IdEstudiante` (`INT`, `NOT NULL`, `FOREIGN KEY`): Referencia a `Estudiantes(IdEstudiante)`.
   - `IdServicio` (`INT`, `NOT NULL`, `FOREIGN KEY`): Referencia a `Servicios(IdServicio)`.
   - `FechaSolicitud` (`DATETIME`, `NOT NULL`, `DEFAULT GETDATE()`): Estampa de tiempo del registro.
   - `Estado` (`VARCHAR(30)`, `NOT NULL`, `DEFAULT 'Pendiente'`): Estado operativo (`Pendiente`, `En Proceso`, `Aprobada`, `Rechazada`).

---

# 5. Creación y Manipulación de Datos

Se implementaron y ejecutaron de manera controlada las operaciones básicas de manipulación de datos (CRUD) y consultas analíticas multicapa.

### 5.1 Datos Iniciales Registrados
- **10 Estudiantes:** Registros del alumno `2026001` (Mariano Silva) al `2026010` (Jessica Vargas).
- **5 Servicios:** Certificado de Estudios, Reexpedición de Credencial, Inscripción a Taller, Baja Temporal y Asesoría Académica.
- **15 Solicitudes:** Mapeo de solicitudes distribuidas con diferentes estados administrativos.

### 5.2 Operaciones CRUD Representativas
```sql
-- INSERT: Registro controlado de un nuevo aspirante/estudiante
INSERT INTO Estudiantes (Matricula, Nombre, Correo) 
VALUES ('2026011', 'Kevin Duran', 'kevin.duran@campuscloud.edu');

-- SELECT: Consulta de filtrado operativo
SELECT IdSolicitud, IdEstudiante, Estado 
FROM Solicitudes 
WHERE Estado = 'Pendiente';

-- UPDATE: Actualización de estatus de trámite universitario
UPDATE Solicitudes 
SET Estado = 'Aprobada' 
WHERE IdSolicitud = 4;

-- DELETE: Remoción controlada de registro temporal
DELETE FROM Estudiantes 
WHERE Matricula = '2026011';
```

### 5.3 Consultas Relacionales (JOINs)
Para satisfacer el análisis inter-entidad exigido, se formularon consultas con uniones de tablas:

```sql
-- Consulta 1: Estudiante, servicio solicitado y estado del trámite
SELECT 
    e.Matricula,
    e.Nombre AS Estudiante,
    s.NombreServicio AS Servicio,
    sol.FechaSolicitud,
    sol.Estado
FROM Solicitudes sol
INNER JOIN Estudiantes e ON sol.IdEstudiante = e.IdEstudiante
INNER JOIN Servicios s ON sol.IdServicio = s.IdServicio;

-- Consulta 2: Métrica de demanda por servicio universitario
SELECT 
    s.NombreServicio,
    COUNT(sol.IdSolicitud) AS TotalSolicitudes
FROM Servicios s
LEFT JOIN Solicitudes sol ON s.IdServicio = sol.IdServicio
GROUP BY s.NombreServicio;

-- Consulta 3: Auditoría de solicitudes pendientes con datos de contacto
SELECT 
    e.Nombre,
    e.Correo,
    s.NombreServicio,
    sol.Estado
FROM Solicitudes sol
JOIN Estudiantes e ON sol.IdEstudiante = e.IdEstudiante
JOIN Servicios s ON sol.IdServicio = s.IdServicio
WHERE sol.Estado = 'Pendiente';
```

---

# 6. Persistencia de Datos

En la arquitectura de contenedores, la capa de lectura y escritura es por definición **efímera (volátil)**. Si un contenedor se detiene o se destruye sin un volumen enlazado, todas las bases de datos generadas durante su ciclo de ejecución se destruyen irrecuperablemente.

Para mitigar este riesgo estructural, se enlazó el directorio `/var/opt/mssql` del contenedor al volumen persistente de Docker `campuscloud-sqlserver-data`.

### Protocolo de Comprobación de Persistencia Realizado:
1. **Paso 1 (Registro de datos de control):** Se insertó un estudiante de prueba (`Matricula: 2026999`, `Nombre: Prueba Persistencia`). Total de registros = 11.
2. **Paso 2 (Detención y reinicio del contenedor):** Se ejecutó el comando `docker restart campuscloud-sqlserver`, provocando la finalización del proceso de SQL Server y el reinicio total del contenedor en Linux.
3. **Paso 3 (Reconexión y auditoría):** Tras reiniciar el servicio, se ejecutó la consulta:
   ```sql
   SELECT Nombre FROM Estudiantes WHERE Matricula = '2026999';
   ```
4. **Resultado Verificado:** El registro fue recuperado íntegramente (`Prueba Persistencia`), comprobando que los archivos de base de datos residen físicamente en el volumen administrado por el host y no en la capa descartable del contenedor.

---

# 7. Usuarios, Roles y Privilegios (Seguridad)

Aplicando el estándar de la industria del **Principio de Mínimo Privilegio (PoLP)**, se segmentó la seguridad en SQL Server creando inicios de sesión (*Logins*) y usuarios de base de datos (*Users*) asignados a roles específicos.

### Matriz de Control de Acceso:

| Operación | Rol Administrador (`user_admin`) | Rol Operador (`user_operador`) | Rol Consulta (`user_consulta`) |
|:---|:---:|:---:|:---:|
| **SELECT** | Sí | Sí | Sí |
| **INSERT** | Sí | Sí | **No (Denegado)** |
| **UPDATE** | Sí | Sí | **No (Denegado)** |
| **DELETE** | Sí | Sí | **No (Denegado)** |
| **CREATE TABLE** | Sí | **No** | **No** |
| **Administrar Roles/Usuarios** | Sí | **No** | **No** |

### Evidencia Técnica de Permisos Concedidos vs. Rechazados:

1. **Operación Autorizada para `user_consulta`:**
   ```sql
   -- Ejecutado con credenciales de user_consulta
   SELECT TOP 1 Nombre FROM Estudiantes;
   -- Resultado: Ejecución exitosa (Retorna 'Mariano Silva').
   ```

2. **Operación Rechazada por Falta de Privilegios para `user_consulta`:**
   ```sql
   -- Intento de inserción con user_consulta
   INSERT INTO Estudiantes (Matricula, Nombre, Correo) 
   VALUES ('2026999', 'Prueba Denegada', 'denegado@campuscloud.edu');
   ```
   **Respuesta del Motor SQL Server:**
   ```text
   Msg 229, Level 14, State 5, Line 1
   The INSERT permission was denied on the object 'Estudiantes', database 'CampusCloud', schema 'dbo'.
   ```
   Esta prueba valida formalmente el aislamiento de privilegios a nivel de esquema.

---

# 8. Conectividad Remota Colaborativa

Para la práctica cruzada colaborativa (Estudiante A $\leftrightarrow$ Estudiante B), se validó la comunicación entre dos estaciones de trabajo en la misma red de área local inalámbrica.

- **Servidor (Estudiante A):** IP `10.50.149.121`, Puerto `1434`.
- **Cliente Remoto (Estudiante B):** Conexión vía cliente SQL (SSMS / DBeaver) hacia `10.50.149.121,1434`.
- **Autenticación Utilizada:** Usuario de solo lectura `user_consulta`.

### Fundamentos Técnicos Clave:
- **¿Por qué no se utiliza `localhost` en una conexión remota?**  
  `localhost` (o `127.0.0.1`) es una dirección de bucle invertido (*loopback*) que resuelve exclusivamente al adaptador virtual del equipo local emisor. Cuando el Estudiante B escribe `localhost`, su máquina intenta buscar un SQL Server en su propia computadora, no en la del Estudiante A. Para viajar a través de los conmutadores y puntos de acceso de la red, es mandatorio utilizar la dirección IP asignada en la interfaz de red compartida.
- **Diferencia entre Conexión Local y Remota:**  
  La conexión local viaja mediante la pila de red interna o sockets locales sin salir del sistema operativo. La conexión remota requiere enrutamiento de paquetes TCP/IP, resolución ARP, atravesar interfaces físicas/inalámbricas y someterse a políticas de filtrado del Firewall.
- **Riesgos y Barreras de Seguridad Identificados:**  
  1. Bloqueo de puertos TCP entrantes por el Firewall de Windows en el equipo servidor.  
  2. Aislamiento de clientes (*AP Client Isolation*) en redes Wi-Fi públicas o institucionales que impide que los dispositivos conectados se comuniquen entre sí.  
  3. Cambios dinámicos de dirección IP derivados del servidor DHCP local.

---

# 9. Problemas Encontrados y Soluciones Aplicadas

Durante el proceso de despliegue y validación se presentaron situaciones técnicas reales que demandaron diagnósticos estructurados:

| # | Problema Detectado | Causa Raíz Identificada | Solución Técnica Aplicada | Resultado Obtenido |
|---|---|---|---|---|
| **1** | **Conflicto de enlace en puerto 1433** | Existía en el host un contenedor previo en ejecución (`redsocial-sql`) que ocupaba el socket `0.0.0.0:1433`. | Se reconfiguró el mapeo en `docker-compose.yml` para publicar el puerto del host en `1434:1433`. | SQL Server arrancó sin colisiones y accesible en `localhost,1434`. |
| **2** | **Error "Página no encontrada" en navegador** | Se intentó acceder a `http://127.0.0.1:5432` vía navegador web asumiendo interfaz gráfica web. | Se diferenció el protocolo binario de bases de datos del protocolo HTTP. Se utilizó el gestor web pgAdmin (`puerto 8082`) y clientes nativos (SSMS/DBeaver) para SQL Server. | Conexión y administración visual exitosa desde las herramientas correspondientes. |
| **3** | **Error de sintaxis en ruta de Docker Compose** | Al ejecutar comandos con `-f compose/docker-compose.yml` estando ya dentro del directorio `compose/`, el sistema buscaba la ruta errónea `compose/compose/...`. | Se normalizó la ejecución directa con `docker compose up -d` dentro del directorio o saliendo a la raíz del repositorio con `cd ..`. | Orquestación limpia y reproducible de los contenedores. |
| **4** | **Bloqueo de cambios en interfaz de VS Code** | VS Code mantenía un búfer en memoria no guardado en la pestaña del editor, impidiendo visualizar las modificaciones externas realizadas en disco. | Se ejecutó la instrucción `File: Revert File` para descartar el borrador en memoria y recargar el contenido actualizado desde el sistema de archivos. | Visualización inmediata de la configuración unificada. |

---

# 10. De Nuestra Nube Local a la Nube Real

A continuación, se compara la arquitectura implementada en la **Nube Académica Local** con los servicios de bases de datos relacionales administradas ofrecidos por los proveedores cloud líderes: **Amazon Web Services (AWS)**, **Microsoft Azure** y **Google Cloud Platform (GCP)**.

| Elemento Técnico | Nube Académica Local (Docker) | AWS (Amazon RDS for SQL Server) | Microsoft Azure (Azure SQL Database / Managed Instance) | Google Cloud (Cloud SQL for SQL Server) |
|---|---|---|---|---|
| **Base de Datos** | SQL Server 2025 en contenedor Linux | Motor SQL Server administrado (Ediciones Express, Web, Standard, Enterprise) | Motor SQL Server como servicio PaaS nativo | Motor SQL Server totalmente administrado |
| **Servidor / Compute** | Computadora física del alumno | Instancias Amazon EC2 dedicadas administradas internamente | Servidores lógicos compartidos o instancias administradas dedicadas | Máquinas virtuales de Compute Engine gestionadas por Google |
| **Almacenamiento** | Volumen Docker en disco duro local | Volúmenes EBS (SSD de uso general gp3 o IOPS aprovisionados io2) | Almacenamiento Azure Premium SSD escalable automáticamente | Almacenamiento persistente SSD con auto-redimensionamiento |
| **Endpoint de Acceso** | `localhost:1434` o `10.50.149.121:1434` | Endpoint DNS: `campuscloud.c123.us-east-1.rds.amazonaws.com:1433` | Nombre de servidor calificado: `campuscloud.database.windows.net:1433` | IP pública/privada administrada en Google Cloud VPC: `34.x.x.x:1433` |
| **Administración del SO** | Responsabilidad 100% del estudiante | Asumida 100% por AWS (parches de seguridad transparentes) | Asumida 100% por Microsoft | Asumida 100% por Google |
| **Actualizaciones y Parches** | Manual (descargar nueva imagen Docker y recrear) | Ventanas automáticas de mantenimiento configurables | Actualizaciones continuas sin tiempo de inactividad (Zero Downtime) | Mantenimiento programado y automatizado por Google |
| **Respaldos (Backups)** | Manuales vía scripts SQL o copia de volumen | Snapshots automatizados diarios y recuperación puntual (PITR) hasta 35 días | Copias de seguridad automáticas con retención a largo plazo (LTR) | Backups automáticos diarios y retención configurable |
| **Seguridad de Red** | Firewall de Windows local | Grupos de Seguridad de VPC (Security Groups) y subredes privadas | Reglas de Firewall de Azure SQL, Private Endpoints y Virtual Networks | Cloud SQL Auth Proxy y redes autorizadas en VPC |
| **Alta Disponibilidad** | Ninguna (si se apaga la PC, el servicio cae) | Multi-AZ mediante réplicas sincrónicas Always On | Alta disponibilidad integrada con SLAs del 99.99% | Failover automático multi-zona |
| **Escalamiento** | Limitado al hardware de la PC | Vertical (cambio de tipo de instancia) y almacenamiento elástico | Escalamiento dinámico de vCores y cómputo Serverless | Escalamiento de CPU/RAM con reinicio mínimo |

---

# 11. ¿Qué Administra Cada Uno? (Modelo de Responsabilidad Compartida)

Al pasar de una solución local en contenedores a un servicio administrado (DBaaS), la organización transfiere la carga pesada de la infraestructura al proveedor cloud, liberando tiempo para enfocarse en el valor del negocio y los datos.

| Nivel Arquitectónico | Tarea o Responsabilidad | Nube Académica Local (Implementación Actual) | Servicio Administrado en la Nube (AWS / Azure / GCP) |
|---|---|---|---|
| **Infraestructura** | Mantenimiento de hardware físico, energía y refrigeración | Administrado localmente por el estudiante | **Proveedor Cloud** |
| **Infraestructura** | Red física, cables y enrutadores | Administrado localmente | **Proveedor Cloud** |
| **Infraestructura** | Virtualización y aprovisionamiento de recursos | Docker Engine local | **Proveedor Cloud** |
| **Plataforma** | Instalación del sistema operativo y parches de seguridad del host | Estudiante | **Proveedor Cloud** |
| **Plataforma** | Instalación, configuración y licenciamiento del motor SQL Server | Estudiante (Docker Compose) | **Proveedor Cloud** |
| **Plataforma** | Respaldos automáticos y recuperación ante desastres | Estudiante (Manual) | **Proveedor Cloud** (con configuración del cliente) |
| **Plataforma** | Alta disponibilidad y conmutación por error (Failover) | No implementado / Manual | **Proveedor Cloud** |
| **Seguridad y Red** | Configuración de firewall y aislamiento de red | Firewall de Windows / Estudiante | **Responsabilidad Compartida** (Proveedor ofrece VPC/Firewalls; Cliente define reglas) |
| **Datos y Aplicación** | Diseño del esquema, tablas, índices y relaciones | Estudiante / Organización | **Cliente / Organización** |
| **Datos y Aplicación** | Creación de usuarios, roles y asignación de permisos | Estudiante / Organización | **Cliente / Organización** |
| **Datos y Aplicación** | Optimización de consultas SQL y lógica de negocio | Estudiante / Organización | **Cliente / Organización** |

---

# 12. Conclusiones Técnicas

La implementación de **CampusCloud** en la Nube Académica Local proporcionó una comprensión profunda y práctica sobre el funcionamiento interno de los sistemas gestores de bases de datos relacionales en entornos contenerizados. La utilización de **Docker y Docker Compose** demostró ser una estrategia sumamente eficiente para encapsular dependencias, definir puertos y garantizar la reproducibilidad de servicios sin requerir instalaciones pesadas directamente sobre el sistema operativo anfitrión.

Durante esta práctica se asumieron responsabilidades operativas complejas que en entornos tradicionales consumen considerables recursos de TI: el aprovisionamiento manual del motor de base de datos, la gestión de volúmenes para evitar la pérdida de información por la naturaleza efímera de los contenedores, la resolución de conflictos de red y la administración rigurosa de privilegios bajo el principio de mínimo privilegio.

Comprender estos mecanismos en el ámbito local facilita enormemente la transición hacia servicios administrados en la nube como **AWS RDS, Azure SQL Database o Google Cloud SQL**. En dichas plataformas, el proveedor asume la administración del hardware, el sistema operativo, los parches de seguridad y la alta disponibilidad, permitiendo a los desarrolladores y DBAs centrarse exclusivamente en el diseño del modelo relacional, la integridad de los datos y el rendimiento de las consultas. 

En conclusión, la Nube Académica Local sirvió como un puente formativo insustituible: haber gestionado los volúmenes, puertos y roles desde la raíz técnica permite ahora interactuar con los servicios cloud no como "cajas negras", sino con el pleno entendimiento de las capas de infraestructura, red y almacenamiento que operan detrás de cada consola en la nube.

---

# 13. Fuentes de Información y Referencias Oficiales

1. **Microsoft Corporation.** (2025). *Documentación técnica de Microsoft SQL Server en contenedores de Docker*. Microsoft Learn. https://learn.microsoft.com/es-es/sql/linux/sql-server-linux-docker-container-deploy
2. **Docker Inc.** (2026). *Docker Compose file specification and networking reference*. Docker Documentation. https://docs.docker.com/compose/
3. **Amazon Web Services.** (2026). *Guía del usuario de Amazon Relational Database Service (RDS) para Microsoft SQL Server*. AWS Documentation. https://docs.aws.amazon.com/es_es/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html
4. **Microsoft Azure.** (2026). *Información general sobre Azure SQL Database y modelos de implementación*. Microsoft Learn. https://learn.microsoft.com/es-es/azure/azure-sql/database/sql-database-paas-overview
5. **Google Cloud.** (2026). *Cloud SQL para SQL Server: Descripción general del producto y arquitectura*. Google Cloud Documentation. https://cloud.google.com/sql/docs/sqlserver
