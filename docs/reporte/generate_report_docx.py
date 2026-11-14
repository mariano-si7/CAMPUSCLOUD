import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from build_docx_helpers import (
    set_cell_background, set_cell_margins, set_cell_borders,
    add_code_block, add_callout, format_table
)

def create_report():
    doc = docx.Document()

    # Configure Margins: 1 inch (2.54 cm) on all sides
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Styles
    navy = RGBColor(0x1B, 0x36, 0x5D)
    dark_gray = RGBColor(0x33, 0x41, 0x55)
    charcoal = RGBColor(0x1E, 0x29, 0x3B)

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(15)
        run.font.bold = True
        run.font.color.rgb = navy
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(12.5)
        run.font.bold = True
        run.font.color.rgb = dark_gray
        return p

    def add_p(text, bold_prefix=None):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.name = "Arial"
            r_pre.font.size = Pt(10)
            r_pre.font.bold = True
            r_pre.font.color.rgb = charcoal
        run = p.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(10)
        run.font.color.rgb = charcoal
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.name = "Arial"
            r_pre.font.size = Pt(10)
            r_pre.font.bold = True
            r_pre.font.color.rgb = charcoal
        run = p.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(10)
        run.font.color.rgb = charcoal
        return p

    # ==========================================================
    # 4.1 PORTADA
    # ==========================================================
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(36)
    p_inst.paragraph_format.space_after = Pt(4)
    r = p_inst.add_run("UNIVERSIDAD TECNOLÓGICA DE TULA-TEPEJI")
    r.font.name = "Arial"
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = navy

    p_carrera = doc.add_paragraph()
    p_carrera.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_carrera.paragraph_format.space_after = Pt(28)
    r = p_carrera.add_run("Área de Tecnologías de la Información • Bases de Datos en la Nube")
    r.font.name = "Arial"
    r.font.size = Pt(11)
    r.font.color.rgb = dark_gray

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(24)
    p_title.paragraph_format.space_after = Pt(6)
    r = p_title.add_run("ACTIVIDAD DE EVALUACIÓN 3\nREPORTE TÉCNICO INTEGRADOR")
    r.font.name = "Arial"
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.color.rgb = navy

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(36)
    r = p_sub.add_run("De CampusCloud Local a la Nube Administrada\nImplementación de SQL Server en Docker, Persistencia, Seguridad y Comparativa Cloud")
    r.font.name = "Arial"
    r.font.size = Pt(12)
    r.font.italic = True
    r.font.color.rgb = dark_gray

    # Metadata table in cover
    meta_table = doc.add_table(rows=6, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Asignatura:", "Bases de Datos en la Nube"),
        ("Unidad:", "Unidad I: Bases de datos relacionales en la nube"),
        ("Proyecto:", "CampusCloud (Nube Académica Local)"),
        ("Estudiante:", "Mariano Silva"),
        ("Docente:", "Profesor Titular de la Asignatura"),
        ("Fecha de Entrega:", "Octubre de 2026")
    ]
    for row_idx, (k, v) in enumerate(meta_data):
        row = meta_table.rows[row_idx]
        cell_k, cell_v = row.cells[0], row.cells[1]
        cell_k.width = Inches(2.2)
        cell_v.width = Inches(4.3)
        set_cell_background(cell_k, "F8FAFC")
        set_cell_background(cell_v, "FFFFFF")
        set_cell_margins(cell_k, top=60, bottom=60, left=100, right=100)
        set_cell_margins(cell_v, top=60, bottom=60, left=100, right=100)
        set_cell_borders(cell_k, color="E2E8F0", sz="4", val="single")
        set_cell_borders(cell_v, color="E2E8F0", sz="4", val="single")
        
        pk = cell_k.paragraphs[0]
        pk.paragraph_format.space_after = Pt(0)
        rk = pk.add_run(k)
        rk.font.name = "Arial"
        rk.font.size = Pt(9.5)
        rk.font.bold = True
        rk.font.color.rgb = navy
        
        pv = cell_v.paragraphs[0]
        pv.paragraph_format.space_after = Pt(0)
        rv = pv.add_run(v)
        rv.font.name = "Arial"
        rv.font.size = Pt(9.5)
        rv.font.color.rgb = charcoal

    doc.add_page_break()

    # ==========================================================
    # 4.2 INTRODUCCIÓN
    # ==========================================================
    add_h1("1. Introducción")
    add_p(
        "El presente reporte técnico integra y documenta de manera detallada la implementación de CampusCloud: "
        "Sistema Universitario de Servicios Digitales, desarrollado como parte de la Unidad I de la asignatura "
        "Bases de Datos en la Nube. Durante esta etapa práctica, se configuró una Nube Académica Local mediante "
        "contenedores Docker que hospeda el motor de base de datos relacional Microsoft SQL Server 2025 sobre Linux, "
        "incorporando almacenamiento persistente desacoplado, segmentación de red y un modelo relacional de datos normalizado."
    )
    add_p(
        "El objetivo primordial de este documento es transferir las lecciones aprendidas en el entorno local hacia "
        "los paradigmas modernos de servicios administrados en la nube pública (Database as a Service - DBaaS), "
        "tales como Amazon Web Services (AWS RDS), Microsoft Azure SQL Database y Google Cloud SQL. "
        "A través de este análisis técnico, se detallan los mecanismos de persistencia física, la administración "
        "del ciclo de vida del contenedor, el control de acceso bajo el principio de mínimo privilegio, las pruebas "
        "de conectividad remota colaborativa cruzada y la matriz de responsabilidad compartida entre la organización y los proveedores cloud."
    )

    # ==========================================================
    # 4.3 ARQUITECTURA IMPLEMENTADA
    # ==========================================================
    add_h1("2. Arquitectura Implementada")
    add_p(
        "La arquitectura de CampusCloud se diseñó para operar bajo un esquema cliente-servidor desacoplado, "
        "permitiendo el aprovisionamiento instantáneo de bases de datos y garantizando conectividad segura tanto "
        "de forma local como de forma remota en la red de área local."
    )

    add_h2("2.1 Diagrama de Arquitectura Local y Remota")
    add_code_block(doc, 
        "[ ARQUITECTURA LOCAL ]\n"
        "Computadora Host (10.50.149.121)\n"
        "  └── Docker Engine 29.x\n"
        "        └── Contenedor: campuscloud-sqlserver (Puerto: 1434 -> 1433)\n"
        "              └── Base de Datos: CampusCloud\n"
        "              └── Volumen Persistente: campuscloud-sqlserver-data (/var/opt/mssql)\n"
        "Cliente Local (SSMS / DBeaver) ──> localhost:1434 ──> Motor SQL Server\n\n"
        "[ ARQUITECTURA REMOTA COLABORATIVA ]\n"
        "Cliente Remoto (Laptop Compañero / PC B)\n"
        "  └── Cliente SQL (SSMS / Azure Data Studio / DBeaver)\n"
        "        └── Conexión TCP: 10.50.149.121:1434 (Usuario: user_consulta)\n"
        "              └── Servidor Host (PC A) ──> Docker ──> SQL Server ──> CampusCloud"
    )

    add_h2("2.2 Identificación de Componentes de la Arquitectura")
    arch_table = doc.add_table(rows=1, cols=3)
    arch_headers = ["Componente", "Valor / Identificador", "Función en la Arquitectura"]
    arch_data = [
        ["Host del Servidor", "PC Local del Estudiante (Windows 11)", "Hospeda el Docker Engine y la red de área local."],
        ["Dirección IP Servidor", "10.50.149.121 (Adaptador Wi-Fi)", "Punto de acceso para conexiones remotas colaborativas."],
        ["Puerto Publicado", "1434:1433 (Host:Contenedor)", "Evita conflictos con instancias locales previas en el puerto 1433."],
        ["Contenedor Docker", "campuscloud-sqlserver", "Aísla el motor Microsoft SQL Server 2025 en Ubuntu 24.04 LTS."],
        ["Volumen Persistente", "campuscloud-sqlserver-data", "Persistencia de archivos de base de datos (/var/opt/mssql)."],
        ["Clientes SQL", "SSMS, Azure Data Studio, DBeaver, sqlcmd", "Herramientas de conexión, administración y ejecución de consultas."],
        ["Base de Datos", "CampusCloud", "Instancia lógica que hospeda las tablas y relaciones del sistema."]
    ]
    format_table(arch_table, [1.5, 2.2, 2.8], arch_headers, arch_data)

    # ==========================================================
    # 4.4 CONFIGURACIÓN DEL SERVICIO
    # ==========================================================
    add_h1("3. Configuración del Servicio")
    add_p(
        "El servicio fue desplegado mediante Docker Compose para garantizar reproducibilidad e inmutabilidad en "
        "los parámetros de ejecución. A continuación, se detalla el fragmento relevante de configuración utilizado:"
    )

    add_code_block(doc,
        "services:\n"
        "  sqlserver-cloud:\n"
        "    image: mcr.microsoft.com/mssql/server:2025-CU8-ubuntu-24.04\n"
        "    container_name: campuscloud-sqlserver\n"
        "    restart: always\n"
        "    environment:\n"
        "      ACCEPT_EULA: \"Y\"\n"
        "      MSSQL_SA_PASSWORD: ${MSSQL_SA_PASSWORD}\n"
        "    ports:\n"
        "      - \"${SQLSERVER_PORT}:1433\"\n"
        "    volumes:\n"
        "      - sqlserver_data:/var/opt/mssql\n"
        "    networks:\n"
        "      - campuscloud_net\n"
        "    healthcheck:\n"
        "      test: [\"CMD-SHELL\", \"/opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P '${MSSQL_SA_PASSWORD}' -C -Q 'SELECT 1' || exit 1\"]\n"
        "      interval: 10s\n"
        "      timeout: 5s\n"
        "      retries: 5\n"
        "      start_period: 15s"
    )

    add_h2("3.1 Matriz de Configuración del Servicio")
    cfg_table = doc.add_table(rows=1, cols=3)
    cfg_headers = ["Aspecto", "Configuración Aplicada", "Descripción Técnica"]
    cfg_data = [
        ["Imagen", "mcr.microsoft.com/mssql/server:2025-CU8-ubuntu-24.04", "Imagen oficial de Microsoft para SQL Server 2025 en Linux."],
        ["Contenedor", "campuscloud-sqlserver", "Nombre único para administración de ciclo de vida del contenedor."],
        ["Puertos", "1434 (Host) -> 1433 (Contenedor)", "Mapeo bidireccional TCP expuesto en 0.0.0.0."],
        ["Variables Entorno", "ACCEPT_EULA=Y, MSSQL_SA_PASSWORD=*****", "Aceptación de licencia y clave SA con complejidad obligatoria."],
        ["Volumen", "campuscloud-sqlserver-data", "Mapeado a /var/opt/mssql para evitar pérdida de datos."],
        ["Operación", "docker compose up -d / down / restart", "Comandos estándar para arranque, detención y reinicio."],
        ["Conexión", "localhost,1434 (Local) | 10.50.149.121,1434 (Remoto)", "Autenticación SQL Server con SA y usuarios creados."]
    ]
    format_table(cfg_table, [1.4, 2.4, 2.7], cfg_headers, cfg_data)

    # ==========================================================
    # 4.5 MODELO DE DATOS CAMPUSCLOUD
    # ==========================================================
    add_h1("4. Modelo de Datos CampusCloud")
    add_p(
        "El modelo relacional de CampusCloud fue normalizado en Tercera Forma Normal (3FN), estructurando "
        "tres entidades principales que reflejan los procesos de trámites y solicitudes universitarias:"
    )

    add_code_block(doc,
        "+-----------------------+           +-----------------------+\n"
        "|      Estudiantes      |           |       Servicios       |\n"
        "+-----------------------+           +-----------------------+\n"
        "| PK  IdEstudiante (INT)|           | PK  IdServicio (INT)  |\n"
        "|     Matricula (UK)    |           |     NombreServicio    |\n"
        "|     Nombre            |           |     Descripcion       |\n"
        "|     Correo (UK)       |           |     Activo (BIT)      |\n"
        "+-----------+-----------+           +-----------+-----------+\n"
        "            | 1                                 | 1\n"
        "            |                                   |\n"
        "            | N                                 | N\n"
        "+-----------v-----------------------------------v-----------+\n"
        "|                        Solicitudes                        |\n"
        "+-----------------------------------------------------------+\n"
        "| PK  IdSolicitud (INT IDENTITY)                            |\n"
        "| FK  IdEstudiante (INT REFERENCES Estudiantes)             |\n"
        "| FK  IdServicio   (INT REFERENCES Servicios)               |\n"
        "|     FechaSolicitud (DATETIME DEFAULT GETDATE())           |\n"
        "|     Estado (VARCHAR(30) DEFAULT 'Pendiente')              |\n"
        "+-----------------------------------------------------------+"
    )

    model_table = doc.add_table(rows=1, cols=3)
    model_headers = ["Tabla", "Campos y Restricciones", "Propósito en el Sistema"]
    model_data = [
        ["Estudiantes", "IdEstudiante (PK, IDENTITY), Matricula (UQ), Nombre, Correo (UQ)", "Registro y autenticación de datos básicos de los alumnos."],
        ["Servicios", "IdServicio (PK, IDENTITY), NombreServicio, Descripcion, Activo (BIT)", "Catálogo de trámites académicos y servicios disponibles."],
        ["Solicitudes", "IdSolicitud (PK, IDENTITY), IdEstudiante (FK), IdServicio (FK), Fecha, Estado", "Gestión y seguimiento del historial de trámites tramitados."]
    ]
    format_table(model_table, [1.3, 2.7, 2.5], model_headers, model_data)

    # ==========================================================
    # 4.6 CREACIÓN Y MANIPULACIÓN DE DATOS
    # ==========================================================
    add_h1("5. Creación y Manipulación de Datos")
    add_p(
        "Se implementaron y ejecutaron satisfactoriamente operaciones de manipulación de datos (CRUD) "
        "cumpliendo rigurosamente con los volúmenes mínimos requeridos en la evaluación técnica:"
    )
    add_bullet("10 registros insertados, verificando unicidad de matrículas y correos.", "Tabla Estudiantes: ")
    add_bullet("5 trámites registrados con estado lógico activo (1).", "Tabla Servicios: ")
    add_bullet("15 trámites registrados con fechas escalonadas y diversos estados.", "Tabla Solicitudes: ")

    add_h2("5.1 Evidencia de Operaciones CRUD")
    crud_table = doc.add_table(rows=1, cols=3)
    crud_headers = ["Operación", "Sentencia SQL Representativa", "Finalidad y Resultado"]
    crud_data = [
        ["INSERT", "INSERT INTO Estudiantes (Matricula, Nombre, Correo) VALUES ('2026011', 'Kevin Duran', 'kevin@campus.edu');", "Alta de nuevo estudiante. Se insertó correctamente con ID generado automáticamente."],
        ["SELECT", "SELECT IdSolicitud, IdEstudiante, Estado FROM Solicitudes WHERE Estado = 'Pendiente';", "Filtro operativo. Recuperó 4 solicitudes en espera de dictamen."],
        ["UPDATE", "UPDATE Solicitudes SET Estado = 'Aprobada' WHERE IdSolicitud = 4;", "Modificación de estado. Se actualizó el estado de la solicitud 4 a 'Aprobada'."],
        ["DELETE", "DELETE FROM Estudiantes WHERE Matricula = '2026011';", "Eliminación controlada. Removió el registro de prueba manteniendo la integridad referencial."]
    ]
    format_table(crud_table, [1.1, 2.9, 2.5], crud_headers, crud_data)

    add_h2("5.2 Consultas Relacionales (JOINs)")
    add_p("Se diseñaron y ejecutaron 3 consultas complejas para relacionar la información inter-tabla:")
    add_code_block(doc,
        "-- Consulta 1: Estudiante que realizó la solicitud, servicio y estado actual\n"
        "SELECT e.Matricula, e.Nombre AS Estudiante, s.NombreServicio, sol.FechaSolicitud, sol.Estado\n"
        "FROM Solicitudes sol\n"
        "INNER JOIN Estudiantes e ON sol.IdEstudiante = e.IdEstudiante\n"
        "INNER JOIN Servicios s ON sol.IdServicio = s.IdServicio;\n\n"
        "-- Consulta 2: Total de solicitudes emitidas por tipo de servicio\n"
        "SELECT s.NombreServicio, COUNT(sol.IdSolicitud) AS TotalSolicitudes\n"
        "FROM Servicios s\n"
        "LEFT JOIN Solicitudes sol ON s.IdServicio = sol.IdServicio\n"
        "GROUP BY s.NombreServicio;\n\n"
        "-- Consulta 3: Solicitudes pendientes con correo de contacto del estudiante\n"
        "SELECT e.Nombre, e.Correo, s.NombreServicio, sol.Estado\n"
        "FROM Solicitudes sol\n"
        "JOIN Estudiantes e ON sol.IdEstudiante = e.IdEstudiante\n"
        "JOIN Servicios s ON sol.IdServicio = s.IdServicio\n"
        "WHERE sol.Estado = 'Pendiente';"
    )

    # ==========================================================
    # 4.7 PERSISTENCIA
    # ==========================================================
    add_h1("6. Persistencia de Datos")
    add_p(
        "Por la naturaleza de la arquitectura Docker, la capa de lectura y escritura de un contenedor es efímera. "
        "Si un contenedor de base de datos se destruye sin un volumen externo montado, los archivos de datos (.mdf y .ldf) "
        "se pierden de forma permanente. Para solucionar esto, CampusCloud monta el volumen persistente "
        "campuscloud-sqlserver-data en el directorio interno /var/opt/mssql."
    )
    add_callout(doc, 
        "Flujo de comprobación de persistencia ejecutado con éxito: "
        "Insertar registro de prueba ('Prueba Persistencia') -> Verificar existencia (11 registros) -> "
        "Detener y reiniciar contenedor (docker restart campuscloud-sqlserver) -> Reconectar al servicio -> "
        "Consultar nuevamente -> Registro intacto confirmado.",
        "PRUEBA DE PERSISTENCIA VERIFICADA"
    )

    # ==========================================================
    # 4.8 USUARIOS, ROLES Y PRIVILEGIOS
    # ==========================================================
    add_h1("7. Usuarios, Roles y Privilegios")
    add_p(
        "En cumplimiento con las mejores prácticas de ciberseguridad y el Principio de Mínimo Privilegio (PoLP), "
        "se definieron roles de base de datos para restringir las capacidades según el perfil de cada usuario:"
    )

    perm_table = doc.add_table(rows=1, cols=4)
    perm_headers = ["Operación", "Rol Administrador (user_admin)", "Rol Operador (user_operador)", "Rol Consulta (user_consulta)"]
    perm_data = [
        ["SELECT", "Sí (Permitido)", "Sí (Permitido)", "Sí (Permitido)"],
        ["INSERT", "Sí (Permitido)", "Sí (Permitido)", "No (Denegado)"],
        ["UPDATE", "Sí (Permitido)", "Sí (Permitido)", "No (Denegado)"],
        ["DELETE", "Sí (Permitido)", "Sí (Permitido)", "No (Denegado)"],
        ["CREATE TABLE", "Sí (Permitido)", "No (Denegado)", "No (Denegado)"],
        ["Administrar Roles", "Sí (Permitido)", "No (Denegado)", "No (Denegado)"]
    ]
    format_table(perm_table, [1.5, 1.7, 1.7, 1.6], perm_headers, perm_data)

    add_h2("7.1 Evidencia Técnica de Permisos Permitidos vs. Rechazados")
    add_code_block(doc,
        "-- 1. Operación Permitida para user_consulta:\n"
        "SELECT TOP 1 Nombre FROM Estudiantes;\n"
        "--> Resultado: 'Mariano Silva' (Ejecución exitosa)\n\n"
        "-- 2. Operación Denegada para user_consulta:\n"
        "INSERT INTO Estudiantes (Matricula, Nombre, Correo) VALUES ('2026999', 'Prueba', 'p@campus.edu');\n"
        "--> Respuesta del motor SQL Server:\n"
        "Msg 229, Level 14, State 5, Server 6ff1e30f06cd, Line 1\n"
        "The INSERT permission was denied on the object 'Estudiantes', database 'CampusCloud', schema 'dbo'."
    )

    # ==========================================================
    # 4.9 CONEXIÓN REMOTA
    # ==========================================================
    add_h1("8. Conexión Remota Colaborativa")
    add_p(
        "Se documenta la prueba cruzada realizada entre el Estudiante A (Servidor en IP 10.50.149.121) y el "
        "Estudiante B (Cliente remoto). El Estudiante B se conectó al servidor utilizando el usuario de solo lectura "
        "user_consulta sobre el puerto 1434, ejecutando consultas de lectura y comprobando el bloqueo en operaciones de escritura."
    )
    add_bullet(
        "Porque localhost (127.0.0.1) es la dirección de loopback local. Si el Estudiante B escribe localhost, "
        "su cliente buscará el servicio en su propia máquina. Para comunicarse en red LAN, es indispensable utilizar la IP del servidor.",
        "¿Por qué no se utiliza localhost en conexión remota? "
    )
    add_bullet(
        "La conexión local viaja a través del socket/pila de red interna del sistema operativo sin salir de la máquina. "
        "La remota involucra resolución ARP, enrutamiento de paquetes TCP/IP, hardware de red (switches/routers) y filtrado de firewall.",
        "Diferencia entre conexión local y remota: "
    )
    add_bullet(
        "Reglas restrictivas en el Firewall de Windows que descartan paquetes entrantes en el puerto 1434, "
        "aislamiento de clientes (AP Isolation) en routers Wi-Fi institucionales y cambios dinámicos de IP por DHCP.",
        "Problemas de red que podrían impedir la conexión: "
    )

    # ==========================================================
    # 4.10 PROBLEMAS ENCONTRADOS Y SOLUCIONES
    # ==========================================================
    add_h1("9. Problemas Encontrados y Soluciones Aplicadas")
    add_p("A continuación, se documentan 4 situaciones reales diagnosticadas y resueltas durante el proyecto:")

    prob_table = doc.add_table(rows=1, cols=4)
    prob_headers = ["Problema", "Causa Identificada", "Solución Aplicada", "Resultado"]
    prob_data = [
        [
            "Conflicto de enlace en puerto 1433",
            "Existía otro contenedor previo (redsocial-sql) ocupando el puerto 1433 del host.",
            "Se modificó el puerto expuesto del host en docker-compose.yml asignando 1434:1433.",
            "Contenedor SQL Server 2025 inició sin errores y accesible en localhost,1434."
        ],
        [
            "Error 'Página no encontrada' en navegador al abrir 127.0.0.1:5432",
            "Confusión entre protocolo binario de base de datos y protocolo HTTP de navegadores web.",
            "Se explicó que las bases de datos no son páginas web; se utilizó pgAdmin (8082) y SSMS para SQL Server.",
            "Conexión exitosa desde los clientes gráficos correspondientes."
        ],
        [
            "Ruta duplicada en docker compose",
            "Al ejecutar -f compose/docker-compose.yml estando ya dentro del directorio compose/, Docker buscó compose/compose/.",
            "Se ejecutó docker compose up -d directamente dentro de la carpeta o saliendo a raíz con cd ..",
            "Despliegue automático sin errores de ruta."
        ],
        [
            "Cambios no visibles en VS Code",
            "VS Code mantenía un búfer con cambios sin guardar en memoria, bloqueando la lectura del disco.",
            "Se ejecutó el comando 'File: Revert File' para descartar el borrador y recargar desde el disco.",
            "Visualización inmediata del archivo unificado."
        ]
    ]
    format_table(prob_table, [1.4, 1.7, 1.9, 1.5], prob_headers, prob_data)

    # ==========================================================
    # 4.11 DE NUESTRA NUBE LOCAL A LA NUBE REAL
    # ==========================================================
    add_h1("10. De Nuestra Nube Local a la Nube Real")
    add_p(
        "A continuación se contrasta la Nube Académica Local implementada frente a los principales servicios "
        "administrados de bases de datos relacionales en la nube pública:"
    )

    cloud_table = doc.add_table(rows=1, cols=5)
    cloud_headers = ["Elemento", "Nube Académica Local", "AWS (Amazon RDS)", "Azure (Azure SQL DB)", "Google Cloud (Cloud SQL)"]
    cloud_data = [
        ["Motor de BD", "SQL Server 2025 en Docker", "Amazon RDS for SQL Server", "Azure SQL Database / Managed Instance", "Cloud SQL for SQL Server"],
        ["Servidor / Host", "PC física del estudiante", "Instancia EC2 gestionada por AWS", "Servidor lógico PaaS gestionado", "Compute Engine gestionado por Google"],
        ["Almacenamiento", "Volumen local Docker", "Volúmenes EBS gp3 / io2", "Almacenamiento Premium SSD", "Persistent Disk SSD escalable"],
        ["Host / Endpoint", "localhost o 10.50.149.121", "endpoint.rds.amazonaws.com", "servidor.database.windows.net", "IP administrada en Google VPC"],
        ["Puerto", "1434 (Host)", "1433 (Estándar RDS)", "1433 (Estándar Azure)", "1433 (Estándar GCP)"],
        ["Admin del SO", "Estudiante (100% manual)", "Asumido por AWS", "Asumido por Microsoft", "Asumido por Google Cloud"],
        ["Actualizaciones", "Manual (docker pull/recreate)", "Ventanas automáticas de mantenimiento", "Actualizaciones continuas Zero-Downtime", "Mantenimiento programado por GCP"],
        ["Respaldos", "Manual vía scripts / copia", "Snapshots automáticos y PITR", "Copias automáticas con retención LTR", "Backups automáticos con retención"],
        ["Seguridad Red", "Firewall de Windows", "Security Groups y VPC Subnets", "Reglas de Firewall Azure y VNet", "Cloud SQL Auth Proxy y VPC"],
        ["Disponibilidad", "Depende del encendido de PC", "Multi-AZ con réplicas sincrónicas", "SLA 99.99% con redundancia de zona", "Failover automático multi-zona"],
        ["Escalamiento", "Limitado a hardware de PC", "Vertical por cambio de clase de instancia", "Dinámico Serverless / vCores elásticos", "Ajuste de CPU/RAM con reinicio breve"]
    ]
    format_table(cloud_table, [1.1, 1.3, 1.4, 1.4, 1.3], cloud_headers, cloud_data)

    # ==========================================================
    # 4.12 ¿QUÉ ADMINISTRA CADA UNO?
    # ==========================================================
    add_h1("11. ¿Qué Administra Cada Uno? (Responsabilidad Compartida)")
    add_p(
        "Al adoptar un servicio administrado en la nube (DBaaS), la organización delega las capas inferiores de la "
        "infraestructura física y de plataforma al proveedor, conservando la responsabilidad sobre los datos y la seguridad lógica:"
    )

    resp_table = doc.add_table(rows=1, cols=3)
    resp_headers = ["Nivel / Tarea", "Nube Académica Local (Implementación)", "Servicio Administrado en la Nube"]
    resp_data = [
        ["Hardware y Servidor Físico", "Estudiante / Organización", "Proveedor Cloud (AWS / Azure / GCP)"],
        ["Red Física y Energía Eléctrica", "Estudiante / Organización", "Proveedor Cloud"],
        ["Sistema Operativo del Host", "Estudiante / Organización", "Proveedor Cloud"],
        ["Instalación y Parches del Motor SQL", "Estudiante (Docker Compose)", "Proveedor Cloud"],
        ["Respaldos y Alta Disponibilidad", "Estudiante (Manual)", "Proveedor Cloud (Configurado por Cliente)"],
        ["Seguridad de Red (Reglas y Firewalls)", "Estudiante (Firewall local)", "Responsabilidad Compartida (VPC/Reglas del Cliente)"],
        ["Diseño de Tablas y Esquema", "Estudiante / Organización", "Cliente / Organización"],
        ["Usuarios, Roles y Permisos", "Estudiante / Organización", "Cliente / Organización"],
        ["Consultas SQL y Optimización", "Estudiante / Organización", "Cliente / Organización"]
    ]
    format_table(resp_table, [2.0, 2.2, 2.3], resp_headers, resp_data)

    # ==========================================================
    # 4.13 CONCLUSIONES
    # ==========================================================
    add_h1("12. Conclusiones Técnicas")
    add_p(
        "La implementación de CampusCloud en la Nube Académica Local proporcionó una visión técnica profunda y "
        "fundamentada sobre el funcionamiento de las bases de datos relacionales empresariales y el ciclo de vida de los contenedores. "
        "La adopción de Docker y Docker Compose permitió comprender de forma práctica la necesidad del almacenamiento "
        "persistente desacoplado, la resolución de conflictos de puertos de red y el gobierno de la seguridad mediante el "
        "principio de mínimo privilegio. Administrar SQL Server 2025 desde su capa de infraestructura exigió asumir tareas críticas "
        "que en entornos tradicionales de TI requieren una dedicación intensiva, tales como el mantenimiento de volúmenes, la configuración "
        "de variables de entorno sensibles y el diagnóstico de conectividad en redes locales."
    )
    add_p(
        "Esta experiencia local constituye un puente formativo insustituible hacia la nube pública administrada (DBaaS). "
        "Al comparar nuestra solución con plataformas líderes como Amazon RDS, Microsoft Azure SQL y Google Cloud SQL, "
        "resulta evidente el inmenso valor de transferir la carga de mantenimiento físico, parches del sistema operativo, "
        "respaldos automatizados y alta disponibilidad hacia proveedores con acuerdos de nivel de servicio (SLAs) del 99.99%. "
        "No obstante, comprender a fondo los componentes que operan detrás de cada servicio —redes virtuales, almacenamiento "
        "en bloque, esquemas relacionales y roles de acceso— capacita al futuro profesional de TI para diseñar, dimensionar y "
        "migrar soluciones hacia la nube con criterio técnico riguroso, evitando considerar a los servicios cloud como 'cajas negras' "
        "y garantizando la integridad, seguridad y eficiencia operativa de las bases de datos institucionales."
    )

    # ==========================================================
    # 4.14 FUENTES DE INFORMACIÓN
    # ==========================================================
    add_h1("13. Fuentes de Información")
    add_bullet("Documentación técnica de Microsoft SQL Server en contenedores Linux. Microsoft Learn. https://learn.microsoft.com/es-es/sql/linux/", "Microsoft Corporation (2025). ")
    add_bullet("Docker Compose file specification, volumes and networking reference. Docker Docs. https://docs.docker.com/compose/", "Docker Inc. (2026). ")
    add_bullet("Amazon Relational Database Service (RDS) User Guide for Microsoft SQL Server. AWS Docs. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html", "Amazon Web Services (2026). ")
    add_bullet("Azure SQL Database: PaaS Architecture, SLA and Security Overview. Microsoft Learn. https://learn.microsoft.com/es-es/azure/azure-sql/", "Microsoft Azure (2026). ")
    add_bullet("Cloud SQL for SQL Server: Architecture, Storage and High Availability. Google Cloud Docs. https://cloud.google.com/sql/docs/sqlserver", "Google Cloud (2026). ")

    # Save docx
    output_path = r"c:\REPOSITORIOS\CampusCloud\docs\ReporteTecnicoIntegrador_CampusCloud.docx"
    doc.save(output_path)
    print(f"Document successfully created at: {output_path}")

if __name__ == "__main__":
    create_report()
