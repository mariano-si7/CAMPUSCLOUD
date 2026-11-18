import os
import sys
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

# Importar helpers de formato ya existentes en el proyecto
helpers_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "reporte"))
sys.path.append(helpers_dir)
from build_docx_helpers import (
    set_cell_background, set_cell_margins, set_cell_borders,
    add_code_block, add_callout, format_table
)

def create_integrador_report():
    doc = docx.Document()

    # Configuración de márgenes estándar (1 pulgada / 2.54 cm)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Paleta cromática corporativa / institucional
    navy = RGBColor(0x1B, 0x36, 0x5D)        # Azul UTTT Institucional
    dark_gray = RGBColor(0x33, 0x41, 0x55)   # Pizarra Oscura
    charcoal = RGBColor(0x1E, 0x29, 0x3B)    # Texto Principal
    caption_color = RGBColor(0x47, 0x55, 0x69)

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = "Calibri"
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
        run.font.name = "Calibri"
        run.font.size = Pt(12.5)
        run.font.bold = True
        run.font.color.rgb = dark_gray
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = "Calibri"
        run.font.size = Pt(11)
        run.font.bold = True
        run.font.color.rgb = charcoal
        return p

    def add_p(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(text)
        run.font.name = "Calibri"
        run.font.size = Pt(10)
        run.font.color.rgb = charcoal
        return p

    def add_bullet(text, bold_prefix=""):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_bold = p.add_run(bold_prefix)
            r_bold.font.name = "Calibri"
            r_bold.font.size = Pt(10)
            r_bold.font.bold = True
            r_bold.font.color.rgb = charcoal
        r_text = p.add_run(text)
        r_text.font.name = "Calibri"
        r_text.font.size = Pt(10)
        r_text.font.color.rgb = charcoal
        return p

    def add_custom_table(headers, data, col_widths):
        table = doc.add_table(rows=len(data) + 1, cols=len(headers))
        format_table(table, col_widths, headers, data)
        p_space = doc.add_paragraph()
        p_space.paragraph_format.space_before = Pt(2)
        p_space.paragraph_format.space_after = Pt(6)

    def add_figure(image_path, caption_text, width=Inches(6.2)):
        if os.path.exists(image_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(3)
            run_img = p_img.add_run()
            run_img.add_picture(image_path, width=width)

            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(0)
            p_cap.paragraph_format.space_after = Pt(10)
            r_cap = p_cap.add_run(caption_text)
            r_cap.font.name = "Calibri"
            r_cap.font.size = Pt(9)
            r_cap.font.italic = True
            r_cap.font.color.rgb = caption_color

    base_proj = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    evid_dir = os.path.join(base_proj, "evidencias", "unidad-ii")

    # ==========================================================
    # 1. PORTADA INSTITUCIONAL FORMAL
    # ==========================================================
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(40)
    p_title.paragraph_format.space_after = Pt(8)
    
    r_inst = p_title.add_run("UNIVERSIDAD TECNOLÓGICA DE TULA-TEPEJI\n")
    r_inst.font.name = "Calibri"
    r_inst.font.size = Pt(16)
    r_inst.font.bold = True
    r_inst.font.color.rgb = navy

    r_sub = p_title.add_run("Área de Tecnologías de la Información e Innovación Digital\nIngeniería en Desarrollo y Gestión de Software • Bases de Datos en la Nube\n\n")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(11.5)
    r_sub.font.bold = True
    r_sub.font.color.rgb = dark_gray

    r_main = p_title.add_run("AVENGERS INITIATIVE • MISIÓN 03\nINFORME FINAL A S.H.I.E.L.D.\nOPERACIÓN CAMPUSCLOUD: PROTOCOLO DE DEFENSA DE DATOS\n")
    r_main.font.name = "Calibri"
    r_main.font.size = Pt(17)
    r_main.font.bold = True
    r_main.font.color.rgb = navy

    r_act = p_title.add_run("Actividad de Evaluación 3 • Unidad II: Reporte Técnico Integrador de Decisiones, Arquitectura y Resultados NoSQL (25 %)\n")
    r_act.font.name = "Calibri"
    r_act.font.size = Pt(11.5)
    r_act.font.italic = True
    r_act.font.color.rgb = dark_gray

    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_meta.paragraph_format.space_before = Pt(50)
    p_meta.paragraph_format.space_after = Pt(24)

    meta_text = (
        "AGENTE RESPONSABLE: Mariano Calzadilla Alvarez\n"
        "MATRÍCULA INSTITUCIONAL: 24300700\n"
        "GRUPO / CUATRIMESTRE: 7° Cuatrimestre • TIID\n"
        "DOCENTE: Mtro. de Asignatura de Bases de Datos en la Nube\n"
        "REPOSITORIO DE CÓDIGO: https://github.com/mariano-si7/CAMPUSCLOUD\n"
        "FECHA DE ENTREGA: Noviembre de 2026\n"
        "ESTADO DEL EXPEDIENTE: INTEGRACIÓN COMPLETA Y VERIFICADA"
    )
    r_meta = p_meta.add_run(meta_text)
    r_meta.font.name = "Calibri"
    r_meta.font.size = Pt(10.5)
    r_meta.font.color.rgb = charcoal

    doc.add_page_break()

    # ==========================================================
    # 2. INTRODUCCIÓN Y DESCRIPCIÓN DEL PROBLEMA
    # ==========================================================
    add_h1("1. Introducción y Descripción del Problema CampusCloud")
    add_p("El proyecto CampusCloud representa la espina dorsal tecnológica para la gestión académica, administrativa y de servicios en la nube de la Universidad Tecnológica de Tula-Tepeji. Durante la fase inicial (Unidad I), la infraestructura se cimentó sobre un motor relacional tradicional —Microsoft SQL Server 2022 (con réplica en PostgreSQL)— garantizando transaccionalidad estricta y cumplimiento de las propiedades ACID (Atomicidad, Consistencia, Aislamiento y Durabilidad) para los registros vitales de Estudiantes, Servicios y Solicitudes de trámite.")

    add_p("No obstante, la evolución hacia una Nube Académica Integral inteligente planteó requerimientos operativos que excedieron las capacidades del paradigma tabular puro. En el diseño de software moderno, forzar a un único motor relacional a resolver problemáticas divergentes incurre en el antipatrón 'One Size Fits All' (Talla Única), generando cuellos de botella críticos:")

    add_bullet(" La estructura rígida de columnas en SQL Server obligaba a ejecutar sentencias 'ALTER TABLE' cada vez que un servicio institucional incorporaba nuevos atributos, aranceles, flujos mixtos o requisitos específicos. Esto derivó en tablas sobredimensionadas con dispersión de columnas ('sparse columns') y abundancia de valores nulos ('NULLs') que degradaban el almacenamiento y la mantenibilidad.", "A. Heterogeneidad Dinámica en el Catálogo de Servicios: ")
    add_bullet(" Modelar las alianzas entre alumnos, la afinidad para proyectos colaborativos, los prerrequisitos de asignaturas y la recomendación personalizada de servicios requería extensas cadenas de 'JOINs' autorreferenciados. En un motor relacional, los grafos de gran profundidad provocan escaneos de índices masivos y bloqueos en cascada que incrementan la latencia de respuesta.", "B. Complejidad en Redes de Interacción Social y Académica: ")
    add_bullet(" El portal estudiantil genera ráfagas concurrentes de telemetría: autenticaciones, accesos concurrentes, descargas de constancias digitales y trazabilidad de auditoría. Registrar estos eventos masivos en el 'Transaction Log' (.ldf) de SQL Server saturaba las operaciones de escritura e interfería con las transacciones financieras y de calificaciones.", "C. Ingesta Masiva de Eventos y Telemetría: ")

    add_p("Ante esta alerta técnica, la iniciativa CampusCloud adoptó formalmente el principio de Persistencia Políglota (Polyglot Persistence). Bajo este enfoque, no se sustituyó SQL Server; en su lugar, se articuló un ecosistema donde cada modelo de almacenamiento se encarga exactamente del problema para el cual fue diseñado matemáticamente.")

    # ==========================================================
    # 3. MATRIZ FINAL DE SELECCIÓN DE MODELOS Y JUSTIFICACIÓN (MISIÓN 1)
    # ==========================================================
    add_h1("2. Decisión Estratégica: Selección de Modelos NoSQL (Misión 1)")
    add_p("A continuación se presenta la matriz analítica que justifica la distribución de datos en CampusCloud, contrastando la naturaleza del dato, las consultas representativas, las fortalezas y las restricciones inherentes a cada tecnología:")

    headers_m1 = ["Necesidad Operativa", "Tipo de Dato", "Consulta Principal", "Modelo y Gestor", "Ventaja Competitiva", "Limitación Relevante"]
    rows_m1 = [
        [
            "Transacciones Académicas y Matrícula",
            "Estructurado, Relacional Tabular",
            "SELECT e.matricula, s.nombre, sol.estado FROM Solicitudes sol JOIN Estudiantes e ON ...",
            "Relacional\n(SQL Server 2022)",
            "Garantía ACID absoluta, integridad referencial mediante llaves foráneas y consistencia estricta en pagos y calificaciones.",
            "Escalabilidad vertical costosa, rigidez de esquema ante atributos cambiantes y bloqueo en escrituras concurrentes."
        ],
        [
            "Catálogo Flexible de Trámites y Requisitos",
            "Semiestructurado (Documentos BSON)",
            "db.detalles_servicios.find({ modalidades: 'En Línea', 'especificaciones.arancel': 0 })",
            "Documental\n(MongoDB 9.0)",
            "Esquema dinámico; soporta arrays polimórficos de requisitos y subdocumentos jerárquicos embebidos en una sola lectura sin JOINs.",
            "Ausencia de integridad referencial automática entre colecciones; riesgo de inconsistencia si no se valida en aplicación."
        ],
        [
            "Red de Alianzas y Recomendación",
            "Grafos Conexos (Nodos y Aristas Tipadas)",
            "MATCH (yo:Estudiante)-[:COLABORA_CON]-(amigo)-[:SOLICITA]->(s) WHERE ... RETURN s",
            "Grafos\n(Neo4j 5 Community)",
            "Recorrido de relaciones en tiempo de puntero ('Index-Free Adjacency'), optimizando algoritmos de caminos mínimos y recomendación.",
            "No diseñado para agregaciones de analítica masiva ni para ingesta concurrente de flujos de eventos a gran escala."
        ],
        [
            "Auditoría Masiva y Telemetría de Eventos",
            "Columnas Anchas (Wide-Column Store)",
            "SELECT * FROM eventos_estudiante WHERE matricula = '24300700' ORDER BY fecha_hora DESC",
            "Columnas Anchas\n(Apache Cassandra 4.1)",
            "Escrituras append-only ultrarrápidas en memoria (Memtables) persistidas a SSTables; particionado lineal distribuido por estudiante.",
            "Imposibilidad de realizar JOINs, agrupaciones complejas o filtros por columnas que no formen parte de la Primary Key."
        ]
    ]
    add_custom_table(headers_m1, rows_m1, [1.2, 1.1, 1.6, 1.2, 1.5, 1.4])

    add_h2("2.1 Delimitación de Responsabilidades y Enlaces Lógicos")
    add_p("Un principio arquitectónico fundamental de CampusCloud es que SQL Server permanece como la Fuente Única de Verdad (Single Source of Truth) para la identidad jurídica del estudiante ('matricula: 24300700') y los códigos maestros de trámites ('id_servicio'). La información que descansa en los motores NoSQL corresponde exclusivamente a extensiones operativas:")
    add_bullet("Contiene las especificaciones técnicas variables (tiempo estimado, modalidades, aranceles, arrays de documentación requerida y requisitos normativos) que cambian periódicamente según las directivas escolares.", "MongoDB (detalles_servicios): ")
    add_bullet("Almacena la red social y académica de la universidad: vínculos de colaboración entre estudiantes para proyectos de ingeniería, intereses compartidos, valoraciones cualitativas (calificaciones 1-5 estrellas) y cadenas de prerrequisitos de servicios.", "Neo4j (Red de Grafos): ")
    add_bullet("Registra la bitácora inmutable de eventos: cada autenticación, intento fallido, consulta de catálogo, descarga de certificados en PDF y latencias de respuesta en milisegundos de la plataforma.", "Apache Cassandra (eventos_estudiante): ")

    add_callout(doc,
        "ADVERTENCIA TÉCNICA OBLIGATORIA: En un ecosistema de Persistencia Políglota NO existe integridad referencial automática distribuida. Las relaciones entre SQL Server, MongoDB, Neo4j y Cassandra son 'referencias lógicas' basadas en claves compartidas (p. ej., matricula = '24300700'). El motor de base de datos no puede forzar la existencia del registro en otro gestor; dicha coherencia debe ser garantizada por la capa de lógica de negocio o mediante eventos de integración.",
        "PRINCIPIO DE INDEPENDENCIA DE GESTORES"
    )

    # ==========================================================
    # 4. ARQUITECTURA DE CAMPUSCLOUD Y FLUJO DE DATOS (MISIÓN 2)
    # ==========================================================
    add_h1("3. Arquitectura del Sistema CampusCloud (Misión 2)")
    add_p("La arquitectura física de CampusCloud fue desplegada localmente mediante Docker Engine y Docker Desktop, orquestada de forma reproducible bajo una red puente dedicada ('campuscloud-db-net'). Esta red proporciona aislamiento de capa 2 respecto a la red local y permite la resolución automática de nombres DNS internos entre los contenedores.")

    add_code_block(doc,
"""+---------------------------------------------------------------------------------------------------+
|                                 INFRAESTRUCTURA HOST WINDOWS (DOCKER ENGINE)                     |
|                                                                                                   |
|   RED DOCKER AISLADA (BRIDGE): campuscloud-db-net                                                 |
|                                                                                                   |
|   [CLIENTES DE LABORATORIO] -->  Docker Desktop  •  MongoDB Compass  •  Neo4j Browser  •  TablePlus|
|                                         |                  |                 |               |    |
|   +-------------------------------------+------------------+-----------------+---------------+    |
|   |                                     |                  |                 |                    |
|   v (Puerto 1434:1433)                  v (Puerto 27017)   v (7474/7687)     v (Puerto 9042)      |
|   +--------------------------+  +----------------------+  +---------------+  +------------------+ |
|   |  campuscloud-sqlserver   |  | campuscloud-mongodb  |  |campuscloud-   |  |   campuscloud-   | |
|   |  SQL Server 2022 Dev     |  | MongoDB 9.0 Community|  |neo4j (Grafos) |  |cassandra (Logs)  | |
|   |  Base Transaccional ACID |  | Catálogo BSON Dinám. |  |Neo4j 5 Comm.  |  |Cassandra 4.1     | |
|   +-------------+------------+  +-----------+----------+  +-------+-------+  +--------+---------+ |
|                 |                           |                     |                   |           |
|   +-------------v------------+  +-----------v----------+  +-------v-------+  +--------v---------+ |
|   | VOLUMEN EXTERNO:         |  | VOLUMEN EXTERNO:     |  |VOLUMEN EXTERNO|  | VOLUMEN EXTERNO: | |
|   | campuscloud-sqlserver-   |  | campuscloud-mongo-   |  |campuscloud-   |  | campuscloud-     | |
|   | data                     |  | data                 |  |neo4j-data     |  | cassandra-data   | |
|   +--------------------------+  +----------------------+  +---------------+  +------------------+ |
|                                                                                                   |
|   [SERVICIOS CONCEPTUALES NO DESPLEGADOS LOCALMENTE]:                                            |
|   Portal Web Institucional (React/Nginx) • API Gateway (Express) • Message Broker (Apache Kafka) |
+---------------------------------------------------------------------------------------------------+""")

    add_p("En observancia de las restricciones tácticas del Quinjet, se distingue con rigor la implementación real de los servicios conceptuales:")
    add_bullet("Los contenedores de SQL Server, PostgreSQL, pgAdmin, MongoDB, Neo4j y Cassandra se encuentran aprovisionados, configurados con volúmenes nombrados independientes para persistencia física, y sus puertos expuestos hacia el host para interactuar con los clientes gráficos oficiales.", "Servicios Implementados Reales: ")
    add_bullet("El API Gateway, la plataforma web del portal de autoservicio y los clústeres elásticos con replicación multi-datacenter se conciben como componentes de la arquitectura de referencia, cuya función es simulada mediante clientes de escritorio.", "Servicios Conceptuales de Referencia: ")

    img_docker = os.path.join(evid_dir, "generales", "01_docker_compose_ps.png")
    add_figure(img_docker, "Figura 1: Panel oficial de Docker Desktop mostrando los contenedores de CampusCloud activos, asignación de puertos y estado saludable de los motores.")

    # ==========================================================
    # 5. IMPLEMENTACIONES Y CONSULTAS ESENCIALES POR GESTOR (MISIÓN 3)
    # ==========================================================
    add_h1("4. Registro de Tecnologías e Implementaciones (Misión 3)")
    add_p("Cada gestor fue aprovisionado mediante scripts idempotentes almacenados en el repositorio de código. A continuación se desglosan las configuraciones y una consulta estratégica explicada por cada tecnología NoSQL:")

    add_h2("4.1 Microsoft SQL Server 2022 (Núcleo Relacional)")
    add_p("SQL Server conserva el esquema estricto de la Unidad I (`dbo.Estudiantes`, `dbo.Servicios`, `dbo.Solicitudes`). Su persistencia es insustituible porque el sistema requiere consistencia inmediata en la emisión de matrículas escolares, control de cuatrimestres e historial académico oficial. Cualquier alteración de estados se gobierna por restricciones de clave foránea y cheques de validación relacional.")

    add_h2("4.2 MongoDB 9.0 Community — Sector Documental")
    add_p("Se creó la colección 'detalles_servicios' dentro de la base de datos 'CampusCloud', incorporando validación formal de esquemas ('JSON Schema Validator') e índices secundarios sobre 'codigo' (único) e 'id_servicio_sql' para agilizar búsquedas. Se cargaron 8 documentos cubriendo 4 categorías ('Academico', 'Administrativo', 'Extracurricular', 'Salud_Estudiantil').")
    
    add_p("Consulta Esencial Explicada (Pipeline de Agregación Analítica):")
    add_code_block(doc,
"""// Script: mongodb/06-agregacion.js
db.detalles_servicios.aggregate([
  { $match: { "activo": true } },
  { $group: {
      _id: "$categoria",
      total_servicios: { $sum: 1 },
      tiempo_promedio_dias: { $avg: "$especificaciones.tiempo_estimado_dias" },
      costo_promedio: { $avg: "$especificaciones.arancel" },
      servicios: { $push: "$nombre" }
  } },
  { $sort: { total_servicios: -1, tiempo_promedio_dias: 1 } }
]);""")
    add_p("Interpretación Técnica: El pipeline inicia con una etapa '$match' que descarta trámites dados de baja. Luego, la etapa '$group' particiona los documentos según su categoría, calculando en tiempo real la media aritmética del tiempo de entrega y del costo arancelario, y consolidando los títulos en un array mediante '$push'. Finalmente, '$sort' jerarquiza las categorías de mayor demanda y menor tiempo de respuesta, permitiendo a la dirección escolar optimizar los recursos humanos en ventanilla.")

    img_mongo_1 = os.path.join(evid_dir, "mongodb", "01_mongo_insert_find.png")
    add_figure(img_mongo_1, "Figura 2: Explorador de documentos BSON en MongoDB Compass sobre la colección detalles_servicios ejecutando filtro por array de modalidades.")

    img_mongo_2 = os.path.join(evid_dir, "mongodb", "02_mongo_update_aggregation.png")
    add_figure(img_mongo_2, "Figura 3: Constructor de agregaciones en MongoDB Compass reflejando las 3 etapas del pipeline y los resultados analíticos calculados.")

    add_h2("4.3 Neo4j 5 Community — Red de Grafos Vengadora")
    add_p("El modelo de grafos vincula a 6 estudiantes (`Mariano Silva [24300700]`, `Ana Martinez`, `Carlos Gomez`, `Diana Lopez`, `Eduardo Hernandez` y `Fernanda Torres`) con 5 servicios clave, estableciendo 17 relaciones dirigidas con propiedades semánticas (`:SOLICITA`, `:COLABORA_CON`, `:TIENE_INTERES_EN` y `:PRERREQUISITO_DE`).")

    add_p("Consulta Esencial Explicada (Recomendación Colaborativa por Vecindad):")
    add_code_block(doc,
"""// Script: neo4j/02-consultas.cypher (Q3)
MATCH (yo:Estudiante {matricula: '24300700'})-[:COLABORA_CON]-(amigo:Estudiante)
MATCH (amigo)-[r:SOLICITA]->(s:Servicio)
WHERE r.calificacion >= 4
  AND NOT (yo)-[:SOLICITA]->(s)
RETURN s.nombre AS ServicioRecomendado, 
       amigo.nombre AS RecomendadoPor, 
       r.calificacion AS CalificacionOtorgada;""")
    add_p("Interpretación Técnica: Este algoritmo recorre la red en dos saltos: primero localiza a los pares académicos vinculados directamente con Mariano Silva mediante la relación bidireccional ':COLABORA_CON'. En el segundo salto, inspecciona qué servicios han calificado dichos colaboradores con 4 o 5 estrellas, filtrando mediante la cláusula 'NOT (yo)-[:SOLICITA]->(s)' aquellos trámites que Mariano aún no ha solicitado. La consulta devolvió exitosamente 'Asesoría Académica', recomendada por Ana Martínez con 5 estrellas, ilustrando el poder del grafo para personalización académica.")

    img_neo4j_1 = os.path.join(evid_dir, "neo4j", "01_neo4j_cypher_shell.png")
    add_figure(img_neo4j_1, "Figura 4: Consola cypher-shell ejecutando el algoritmo de recomendación colaborativa y el censo de 11 nodos y 17 relaciones.")

    img_neo4j_2 = os.path.join(evid_dir, "neo4j", "02_neo4j_browser_graph.png")
    add_figure(img_neo4j_2, "Figura 5: Interfaz interactiva de Neo4j Browser desplegando la topología de la red estudiantil y el inspector de propiedades del nodo 24300700.")

    add_h2("4.4 Apache Cassandra 4.1 — Sector Columnas Anchas")
    add_p("Para la ingesta masiva de eventos de auditoría y telemetría, se implementó la tabla 'eventos_estudiante' en el keyspace 'campuscloud_logs'. Cassandra exige un modelado estrictamente guiado por las consultas que se pretenden ejecutar ('Query-Driven Design'):")

    add_code_block(doc,
"""// Script: cassandra/01-crear-keyspace-tabla.cql
CREATE TABLE campuscloud_logs.eventos_estudiante (
    matricula text,
    fecha_hora timestamp,
    id_evento uuid,
    modulo text,
    tipo_evento text,
    estado text,
    ip_origen text,
    dispositivo text,
    latencia_ms int,
    id_servicio_sql int,
    detalles text,
    PRIMARY KEY ((matricula), fecha_hora, id_evento)
) WITH CLUSTERING ORDER BY (fecha_hora DESC, id_evento ASC);""")
    add_p("Interpretación Técnica de la Clave Primaria: La 'Partition Key' está compuesta exclusivamente por '((matricula))'. Esto garantiza que el algoritmo de dispersión 'Murmur3Partitioner' asigne todos los eventos de un estudiante específico al mismo nodo físico del clúster, posibilitando lecturas de un solo salto en red. Las 'Clustering Keys' ('fecha_hora DESC, id_evento ASC') ordenan físicamente las filas dentro de las SSTables en disco de manera descendente. De este modo, recuperar la actividad más reciente de un alumno no requiere un 'ORDER BY' computado en memoria, sino una lectura secuencial contigua en disco.")

    img_cass_1 = os.path.join(evid_dir, "cassandra", "01_cassandra_cqlsh_select.png")
    add_figure(img_cass_1, "Figura 6: Cliente visual TablePlus conectado a Cassandra ejecutando consulta particionada por matricula 24300700 con orden temporal descendente.")

    img_cass_2 = os.path.join(evid_dir, "cassandra", "02_cassandra_update_delete.png")
    add_figure(img_cass_2, "Figura 7: Consola cqlsh demostrando la modificación atómica de estado de evento y la eliminación física mediada por Tombstones.")

    # ==========================================================
    # 6. PRUEBAS DE FUNCIONAMIENTO, PERSISTENCIA Y ACCESOS (MISIÓN 4)
    # ==========================================================
    add_h1("5. Validación de Campo: Pruebas, Persistencia y Seguridad (Misión 4)")
    add_p("La operatividad de la plataforma fue sometida a pruebas destructivas controladas y verificaciones funcionales para comprobar la resiliencia de la arquitectura:")

    add_h2("5.1 Prueba de Persistencia de Datos tras Reinicio Destructivo")
    add_p("Objetivo: Garantizar que la destrucción del entorno de ejecución no comprometa los datos almacenados en los motores NoSQL.")
    add_p("Procedimiento: Con los datos cargados en MongoDB y Neo4j, se ejecutó la orden de detención y reinicio de contenedores:")
    add_code_block(doc, "docker restart campuscloud-mongodb campuscloud-neo4j")
    add_p("Resultado Obtenido: Al reconectar con 'mongosh' y 'cypher-shell', se verificó que los 7 documentos de 'detalles_servicios' y los 11 nodos con 17 relaciones en Neo4j permanecían intactos. Esto demostró que el mapeo hacia los volúmenes nombrados externos ('campuscloud-mongo-data' y 'campuscloud-neo4j-data') mantiene los punteros de disco desacoplados del ciclo de vida del contenedor.")

    add_h2("5.2 Control de Acceso y Aislamiento Perimetral")
    add_p("La seguridad de CampusCloud se diseñó en capas defensivas sucesivas:")
    add_bullet("MongoDB opera con autenticación obligatoria habilitada. Intentos de conexión anónima o sin especificar '--authenticationDatabase admin' son rechazados de inmediato con código de error de autenticación.", "Autenticación Criptográfica: ")
    add_bullet("Neo4j exige autenticación mediante el protocolo binario Bolt ('neo4j / CampusCloudNeo4j2026!'), impidiendo el acceso a la interfaz web o a consultas Cypher a usuarios no autorizados.", "Control en Grafo: ")
    add_bullet("Ningún motor expone contraseñas en scripts versionados. Las credenciales residen en el archivo local '.env', el cual se encuentra estrictamente ignorado por Git en el archivo '.gitignore'.", "Protección de Secretos: ")

    add_h2("5.3 Limitaciones Reales Identificadas en el Entorno")
    add_p("Durante la validación de campo se identificaron dos restricciones técnicas inherentes a la arquitectura políglota:")
    add_bullet("En Cassandra, no es posible ejecutar consultas con filtros sobre columnas arbitrarias (p. ej. 'WHERE estado = \"FALLIDO\"') sin especificar la Partition Key, a menos que se fuerce la directiva 'ALLOW FILTERING', la cual degrada severamente el rendimiento en clústeres reales al obligar a escanear todos los nodos de la red.", "Restricción de Filtrado en Cassandra: ")
    add_bullet("Al no existir un motor de transacciones distribuidas (como un coordinador Two-Phase Commit / 2PC), si un estudiante es eliminado de SQL Server, sus documentos en MongoDB, sus nodos en Neo4j y sus logs en Cassandra continúan existiendo, requiriendo un patrón de orquestación Saga o tareas de limpieza periódica para evitar datos huérfanos.", "Falta de Cascada Automática entre Gestores: ")

    # ==========================================================
    # 7. INCIDENCIAS TÉCNICAS Y SOLUCIONES (MISIÓN 5)
    # ==========================================================
    add_h1("6. Protocolo de Seguridad y Contingencia: Incidencias Resueltas (Misión 5)")
    add_p("Durante la fase de integración y despliegue del proyecto, se presentaron dos anomalías técnicas de severidad alta que requirieron diagnóstico formal:")

    add_h2("6.1 Incidencia 1: Bloqueo Crítico por Puntero Git LFS Huérfano")
    add_bullet("Al intentar sincronizar y fusionar el repositorio colaborativo base ('CampusClaude'), Git arrojó un error fatal impidiendo la descarga de objetos y abortando el proceso: 'Smudge error: Object does not exist on the server: [404] fatal: docker_images/neo.tar: smudge filter lfs failed'. Posteriormente, al intentar realizar 'git push origin main', GitHub rechazó la transacción con el código 'GH008: Your push referenced at least 1 unknown Git LFS object'.", "Síntoma: ")
    add_bullet("El repositorio upstream contenía un archivo puntero de Git LFS correspondiente a una imagen de Docker de 592 MB ('docker_images/neo.tar'), pero el archivo binario real jamás fue subido a los servidores de GitHub LFS, dejando un puntero roto que corrompía la descarga y la subida.", "Causa Raíz: ")
    add_bullet("Se confirmó mediante 'git lfs ls-files' que el archivo 'neo.tar' estaba indexado como LFS pero sin correspondencia en el servidor remoto.", "Verificación: ")
    add_bullet("Se reescribió la historia de Git local utilizando 'git filter-branch --force --index-filter \"git rm --cached --ignore-unmatch docker_images/neo.tar\" --prune-empty 1c3ab06..HEAD', se eliminó la directiva LFS en '.gitattributes' y se configuró temporalmente '$env:GIT_LFS_SKIP_SMUDGE=\"1\"'.", "Corrección Aplicada: ")
    add_bullet("El árbol de Git quedó libre de referencias corruptas, el 'git push' a GitHub se ejecutó limpiamente con código 0 y el repositorio recuperó su estabilidad sin perder ningún archivo del proyecto.", "Resultado Verificado: ")

    add_h2("6.2 Incidencia 2: Incompatibilidad de Metadatos de Red en Docker Compose")
    add_bullet("Al ejecutar 'docker compose -f docker/compose.yaml up -d', el motor de Docker abortó el arranque indicando: 'network campuscloud-db-net was found but has incorrect label com.docker.compose.network set to \"\" (expected: \"campuscloud_net\")'.", "Síntoma: ")
    add_bullet("La red puente 'campuscloud-db-net' había sido creada previamente desde la terminal o por otro compose con etiquetas de metadatos distintas. Docker Compose v2 asume por defecto que las redes declaradas deben pertenecer a su propio espacio de nombres a menos que se declare explícitamente lo contrario.", "Causa Raíz: ")
    add_bullet("Se inspeccionó la red con 'docker network inspect campuscloud-db-net' comprobando que el atributo Labels no contenía la firma del proyecto 'docker'.", "Verificación: ")
    add_bullet("Se modificó 'docker/compose.yaml' declarando la red y los volúmenes con el modificador 'external: true':\nnetworks:\n  campuscloud_net:\n    external: true\n    name: ${DOCKER_NETWORK:-campuscloud-db-net}", "Corrección Aplicada: ")
    add_bullet("Docker Compose se enlazó de manera transparente a la red preexistente sin necesidad de destruir los contenedores relacionales ni perder los volúmenes de datos montados.", "Resultado Verificado: ")

    # ==========================================================
    # 8. COMPARACIÓN CLOUD VS LOCAL Y RESPONSABILIDADES (MISIÓN 6)
    # ==========================================================
    add_h1("7. Inteligencia Multicloud: Despliegue Local vs Nube Administrada (Misión 6)")
    add_p("Un error conceptual frecuente en la ingeniería de software es equiparar un contenedor Docker local con un servicio de base de datos en la nube. Docker proporciona virtualización a nivel de sistema operativo (IaaS simplificada), mientras que los proveedores de nube ofrecen servicios completamente administrados (Database as a Service - DBaaS).")

    add_h2("7.1 Matriz Comparativa de Motores y Servicios Cloud")
    headers_cloud = ["Necesidad CampusCloud", "Motor Local Docker", "Amazon Web Services (AWS)", "Microsoft Azure", "Google Cloud Platform (GCP)"]
    rows_cloud = [
        [
            "Datos Flexibles y Catálogo Dinámico",
            "MongoDB 9.0 Community",
            "Amazon DocumentDB\n(Compatible con API MongoDB)",
            "Azure Cosmos DB\n(API para MongoDB con escalado multi-región)",
            "Google Cloud Firestore\n(Base documental serverless distribuida)"
        ],
        [
            "Relaciones de Grafos y Alianzas",
            "Neo4j 5 Community",
            "Amazon Neptune\n(Motor de grafos con APIs Gremlin y SPARQL)",
            "Azure Cosmos DB\n(API Gremlin / Apache TinkerPop)",
            "Google Cloud Spanner Graph\n(Base distribuida con motor de grafos integrado)"
        ],
        [
            "Ingesta Masiva y Telemetría de Eventos",
            "Apache Cassandra 4.1",
            "Amazon Keyspaces\n(Cassandra administrada serverless)",
            "Azure Managed Instance for Apache Cassandra",
            "Google Cloud Bigtable\n(Motor de columnas anchas de alta escala)"
        ]
    ]
    add_custom_table(headers_cloud, rows_cloud, [1.3, 1.2, 1.3, 1.3, 1.3])

    add_h2("7.2 Modelo de Responsabilidad Compartida: Local vs Nube Pública")
    add_p("Al operar en un entorno local con Docker, el estudiante o administrador asume el 100 % de las responsabilidades operativas. En contraste, al migrar a DBaaS en la nube pública, la demarcación de responsabilidades se transforma radicalmente:")

    add_bullet("En el laboratorio local, la alta disponibilidad es nula (falla el equipo host y colapsa el sistema). En la nube, el proveedor ofrece acuerdos de nivel de servicio (SLA) del 99.99 % al 99.999 % mediante replicación multi-zona y multi-región automática.", "1. Disponibilidad y Tolerancia a Fallos: ")
    add_bullet("En Docker, los respaldos dependen de scripts manuales del alumno ('mongodump', 'nodetool snapshot'). En DBaaS, el proveedor gestiona copias continuas con restauración en cualquier punto del tiempo (Point-in-Time Recovery / PITR) y cifrado de snapshots en reposo.", "2. Copias de Seguridad y Recuperación: ")
    add_bullet("En Docker, los parches del sistema operativo base, las actualizaciones de seguridad de los motores y el afinamiento de memoria de la JVM (en Cassandra y Neo4j) son manuales. En la nube, las actualizaciones se aplican en caliente de forma automatizada y transparente.", "3. Parches de Seguridad y Mantenimiento: ")
    add_bullet("El laboratorio local tiene costo de infraestructura cero pero requiere hardware robusto (consumo intensivo de RAM). La nube cobra bajo el modelo 'Pay-as-you-go' o aprovisionamiento por vCPU/Memoria, lo cual exige control riguroso de costes para evitar facturaciones imprevistas.", "4. Economía y Escalabilidad: ")

    # ==========================================================
    # 9. CONCLUSIONES Y REFERENCIAS (MISIÓN 7)
    # ==========================================================
    add_h1("8. Consejo de los Avengers: Conclusiones y Defensa Técnica (Misión 7)")
    
    add_h2("8.1 Conclusiones Originales del Proyecto")
    add_bullet("Ningún motor de bases de datos es universalmente superior; cada tecnología domina un nicho computacional específico. SQL Server es insuperable para transacciones financieras y de matrícula formal donde la inconsistencia es inaceptable. MongoDB otorga la flexibilidad indispensable para que el catálogo de trámites evolucione sin fricción técnica. Neo4j transforma consultas relacionales complejas e intratables en navegaciones intuitivas de punteros en memoria. Y Apache Cassandra resuelve la ingesta masiva de auditoría que colapsaría el búfer de cualquier motor relacional.", "1. Especialización de Paradigmas: ")
    add_bullet("Adoptar Persistencia Políglota amplía radicalmente las capacidades del sistema, pero traslada la complejidad desde el motor de base de datos hacia la capa de arquitectura de software. Al no existir llaves foráneas distribuidas ni transacciones ACID globales, el ingeniero debe diseñar mecanismos de consistencia eventual, manejar fallos parciales y documentar minuciosamente los esquemas conceptuales.", "2. El Costo de la Poliglotía y el Teorema CAP: ")
    add_bullet("Para llevar CampusCloud al siguiente nivel de madurez operativa en un entorno productivo, se propone implementar un bus de eventos distribuido (Apache Kafka) combinado con Change Data Capture (CDC mediante Debezium). De este modo, cualquier inserción de un estudiante en SQL Server publicaría automáticamente un evento en Kafka, propagando la creación del nodo en Neo4j y del documento en MongoDB de forma asíncrona, desacoplada y tolerante a fallos.", "3. Propuesta de Evolución Arquitectónica: ")

    add_h2("8.2 Referencias Bibliográficas (Normas APA 7ma Edición)")
    add_bullet("Amazon Relational Database Service and Managed NoSQL Developer Guides. Amazon Web Services Documentation. https://docs.aws.amazon.com/", "Amazon Web Services. (2026). ")
    add_bullet("Apache Cassandra Documentation: Architecture, CQL Reference and Data Modeling (v4.1). The Apache Software Foundation. https://cassandra.apache.org/doc/latest/", "Apache Software Foundation. (2026). ")
    add_bullet("Azure Cosmos DB: Globally Distributed Multi-Model Database Service Documentation. Microsoft Learn. https://learn.microsoft.com/azure/cosmos-db/", "Microsoft Azure. (2026). ")
    add_bullet("MongoDB 9.0 Manual: Document Validation, Data Modeling and Aggregation Pipeline. MongoDB Inc. https://www.mongodb.com/docs/manual/", "MongoDB Inc. (2026). ")
    add_bullet("The Neo4j Cypher Manual: Graph Database Modeling, Patterns and Performance Optimization. Neo4j Inc. https://neo4j.com/docs/cypher-manual/current/", "Neo4j Inc. (2026). ")
    add_bullet("Database Internals: A Deep Dive into How Distributed Data Systems Work. O'Reilly Media.", "Petrov, A. (2019). ")
    add_bullet("Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems. O'Reilly Media.", "Kleppmann, M. (2017). ")

    # ==========================================================
    # 10. ANEXOS Y ENLACE AL REPOSITORIO DE CÓDIGO
    # ==========================================================
    add_h1("9. Anexos y Repositorio de Código Fuente")
    add_p("Todo el código fuente, los scripts DDL/DML, los archivos de orquestación de Docker y las evidencias gráficas generadas se encuentran versionados y auditados en el repositorio público del estudiante:")
    add_bullet("https://github.com/mariano-si7/CAMPUSCLOUD", "Repositorio Central GitHub: ")
    add_bullet("Contiene 'compose.yaml' y la plantilla segura '.env.example'.", "Directorio 'docker/': ")
    add_bullet("Colección de 6 scripts ejecutables para MongoDB (.js).", "Directorio 'mongodb/': ")
    add_bullet("Scripts Cypher de creación, consultas y actualización de grafos (.cypher).", "Directorio 'neo4j/': ")
    add_bullet("Scripts CQL de keyspaces, tablas, telemetría y particionado (.cql).", "Directorio 'cassandra/': ")
    add_bullet("Documentación detallada de arquitectura, instalación y pruebas.", "Directorio 'docs/': ")
    add_bullet("Capturas oficiales en alta resolución con clientes nativos (MongoDB Compass, Neo4j Browser, TablePlus, Docker Desktop).", "Directorio 'evidencias/unidad-ii/': ")

    # Guardar documento Word en reportes/unidad-ii/
    out_docx_sub = os.path.abspath(os.path.join(os.path.dirname(__file__), "Calzadilla_Mariano_ReporteIntegrador_UnidadII_CampusCloud.docx"))
    doc.save(out_docx_sub)
    print(f"[OK] Reporte Integrador DOCX generado en: {out_docx_sub}")

    # Copiar DOCX a la raíz del proyecto
    out_docx_root = os.path.join(base_proj, "Calzadilla_Mariano_ReporteIntegrador_UnidadII_CampusCloud.docx")
    shutil.copy2(out_docx_sub, out_docx_root)
    print(f"[OK] Reporte Integrador DOCX copiado a la raíz: {out_docx_root}")

    # Convertir a PDF con docx2pdf
    out_pdf_sub = os.path.abspath(os.path.join(os.path.dirname(__file__), "Calzadilla_Mariano_ReporteIntegrador_UnidadII_CampusCloud.pdf"))
    try:
        from docx2pdf import convert
        print("Convirtiendo Reporte Integrador DOCX a PDF...")
        convert(out_docx_sub, out_pdf_sub)
        print(f"[OK] Reporte Integrador PDF generado en: {out_pdf_sub}")

        # Copiar PDF a la raíz del proyecto
        out_pdf_root = os.path.join(base_proj, "Calzadilla_Mariano_ReporteIntegrador_UnidadII_CampusCloud.pdf")
        shutil.copy2(out_pdf_sub, out_pdf_root)
        print(f"[OK] Reporte Integrador PDF copiado a la raíz: {out_pdf_root}")
    except Exception as e:
        print(f"[AVISO] Error al convertir a PDF con docx2pdf: {e}")

if __name__ == "__main__":
    create_integrador_report()
