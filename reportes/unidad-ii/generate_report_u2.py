import os
import sys
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

def create_report():
    doc = docx.Document()

    # Configurar mÃ¡rgenes de 1 pulgada (2.54 cm)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Paleta de colores institucionales
    navy = RGBColor(0x1B, 0x36, 0x5D)
    dark_gray = RGBColor(0x33, 0x41, 0x55)
    charcoal = RGBColor(0x1E, 0x29, 0x3B)
    caption_color = RGBColor(0x47, 0x55, 0x69)

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = "Calibri"
        run.font.size = Pt(16)
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
        run.font.size = Pt(13)
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
        run.font.size = Pt(10.5)
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
            r_bold.font.size = Pt(10.5)
            r_bold.font.bold = True
            r_bold.font.color.rgb = charcoal
        r_text = p.add_run(text)
        r_text.font.name = "Calibri"
        r_text.font.size = Pt(10.5)
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
            r_cap.font.size = Pt(9.5)
            r_cap.font.italic = True
            r_cap.font.color.rgb = caption_color

    base_proj = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    evid_dir = os.path.join(base_proj, "evidencias", "unidad-ii")

    # ==========================================================
    # 1. PORTADA INSTITUCIONAL
    # ==========================================================
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(36)
    p_title.paragraph_format.space_after = Pt(8)
    r_inst = p_title.add_run("UNIVERSIDAD TECNOLÃ“GICA DE TULA-TEPEJI\n")
    r_inst.font.name = "Calibri"
    r_inst.font.size = Pt(16)
    r_inst.font.bold = True
    r_inst.font.color.rgb = navy

    r_sub = p_title.add_run("Ãrea de TecnologÃ­as de la InformaciÃ³n â€¢ Bases de Datos en la Nube\n\n")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(12)
    r_sub.font.bold = True
    r_sub.font.color.rgb = dark_gray

    r_main = p_title.add_run("OPERACIÃ“N CAMPUSCLOUD\nPROTOCOLO NoSQL: DEFENSA DE LA ARQUITECTURA DE DATOS\n")
    r_main.font.name = "Calibri"
    r_main.font.size = Pt(18)
    r_main.font.bold = True
    r_main.font.color.rgb = navy

    r_act = p_title.add_run("Actividad de EvaluaciÃ³n 2 â€¢ Unidad II: Bases de Datos No Relacionales en la Nube (55 %)\n")
    r_act.font.name = "Calibri"
    r_act.font.size = Pt(12)
    r_act.font.italic = True
    r_act.font.color.rgb = dark_gray

    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_meta.paragraph_format.space_before = Pt(40)
    p_meta.paragraph_format.space_after = Pt(24)

    meta_text = (
        "ALUMNO: Mariano Calzadilla Alvarez\n"
        "MATRÃCULA: 24300700\n"
        "CARRERA: IngenierÃ­a en TecnologÃ­as de la InformaciÃ³n e InnovaciÃ³n Digital\n"
        "GRUPO / CUATRIMESTRE: 7Â° Cuatrimestre\n"
        "DOCENTE: Mtro. de Asignatura de Bases de Datos en la Nube\n"
        "FECHA DE ENTREGA: Noviembre de 2026\n"
        "ESTADO DE LA MISIÃ“N: COMPLETADA CON Ã‰XITO"
    )
    r_meta = p_meta.add_run(meta_text)
    r_meta.font.name = "Calibri"
    r_meta.font.size = Pt(10.5)
    r_meta.font.color.rgb = charcoal

    doc.add_page_break()

    # ==========================================================
    # 2. PROBLEMA Y SELECCIÃ“N DE MODELOS
    # ==========================================================
    add_h1("1. Problema y SelecciÃ³n de Modelos NoSQL")
    add_p("Durante la Unidad I, el ecosistema CampusCloud consolidÃ³ una base de datos relacional sobre Microsoft SQL Server 2022 (con rÃ©plica en PostgreSQL), sustentando las entidades fundamentales de 'Estudiantes', 'Servicios' y 'Solicitudes'. Sin embargo, la expansiÃ³n operativa hacia una Nube AcadÃ©mica Integral generÃ³ tres requerimientos que pusieron en jaque el modelo tabular tradicional:")
    
    add_bullet(" La rigidez de las tablas relacionales obligaba a alterar el esquema ('ALTER TABLE') cada vez que un servicio requerÃ­a requisitos particulares, aranceles o dependencias distintas, provocando columnas dispersas ('sparse columns') con excesivos valores nulos.", "A. Heterogeneidad en el CatÃ¡logo de Servicios: ")
    add_bullet(" Determinar la afinidad entre estudiantes, sus alianzas para proyectos y la recomendaciÃ³n cruzada de servicios requerÃ­a consultas 'JOIN' recursivas y complejas que degradaban el motor SQL Server.", "B. Red Compleja de Alianzas y Conexiones AcadÃ©micas: ")
    add_bullet(" El flujo continuo de interacciones, descargas de constancias y auditorÃ­a de accesos generaba un volumen de escrituras concurrente que saturaba el 'Transaction Log' (.ldf) de SQL Server.", "C. TelemetrÃ­a y Registro de Eventos Masivos: ")

    add_p("En observancia del briefing oficial de la misiÃ³n, no se sustituyÃ³ SQL Server; en su lugar, se adoptÃ³ el paradigma de Persistencia PolÃ­glota (Polyglot Persistence) integrando tres tecnologÃ­as complementarias:")

    headers_mod = ["Paradigma NoSQL", "Motor Elegido", "Caso de Uso en CampusCloud", "JustificaciÃ³n TÃ©cnica"]
    rows_mod = [
        ["Documental", "MongoDB 9.0 Community", "CatÃ¡logo dinÃ¡mico de servicios extendidos", "Almacena documentos BSON semiestructurados con arrays de requisitos y subdocumentos de especificaciones tÃ©cnicas sin alterar el esquema central."],
        ["Grafos", "Neo4j 5 Community", "Red de alianzas, afinidades y recomendaciÃ³n", "Modela directamente a los estudiantes y servicios como nodos y sus interacciones como aristas tipadas con propiedades, optimizando algoritmos de grafos."],
        ["Columnas Anchas", "Apache Cassandra 4.1", "BitÃ¡cora masiva de telemetrÃ­a y auditorÃ­a", "Escritura append-only ultrarrÃ¡pida en disco (SSTables), consultas por particiÃ³n de estudiante ('matricula') y orden temporal descendente."]
    ]
    add_custom_table(headers_mod, rows_mod, [1.2, 1.2, 2.0, 2.1])

    # ==========================================================
    # 3. ARQUITECTURA DE CAMPUSCLOUD
    # ==========================================================
    add_h1("2. Arquitectura del Sistema CampusCloud")
    add_p("La infraestructura se encuentra completamente contenida en Docker bajo una red puente comÃºn ('campuscloud-db-net'), garantizando comunicaciÃ³n directa vÃ­a DNS entre los servicios, aislamiento perimetral y persistencia mediante volÃºmenes nombrados independientes:")

    add_code_block(doc, 
"""+---------------------------------------------------------------------------------+
|                       ESTACIÃ“N HOST WINDOWS (DOCKER ENGINE)                     |
|                                                                                 |
|   RED DOCKER PUENTE: campuscloud-db-net                                         |
|                                                                                 |
|   +-----------------------+     +-----------------------+                       |
|   | campuscloud-sqlserver |     |   campuscloud-mongodb |                       |
|   | SQL Server 2022       |     |   MongoDB 9.0         |                       |
|   | Puerto: 1434:1433     |     |   Puerto: 27017:27017 |                       |
|   | Vol: sqlserver_data   |     |   Vol: mongo_data     |                       |
|   +-----------+-----------+     +-----------+-----------+                       |
|               |                             |                                   |
|               +--------------+--------------+                                   |
|                              |                                                  |
|   +-----------+-----------+  |  +-----------+-----------+                       |
|   |   campuscloud-neo4j   |  |  | campuscloud-cassandra |                       |
|   |   Neo4j 5 Community   |  |  | Apache Cassandra 4.1  |                       |
|   |   Puertos: 7474/7687  |  |  | Puerto: 9042:9042     |                       |
|   |   Vol: neo4j_data     |  |  | Vol: cassandra_data   |                       |
|   +-----------------------+  |  +-----------------------+                       |
|                              v                                                  |
|               +-----------------------------+                                   |
|               |  SEGURIDAD Y PERSISTENCIA   |                                   |
|               |  Variables de Entorno .env  |                                   |
|               +-----------------------------+                                   |
+---------------------------------------------------------------------------------+""")

    add_callout(doc, 
        "La arquitectura mantiene independencia total entre motores: cada uno cuenta con su volumen de almacenamiento persistente montado en disco y sus puertos expuestos hacia el host.", 
        "PRINCIPIO DE CONTENCIÃ“N Y AISLAMIENTO"
    )

    # ==========================================================
    # 4. CONFIGURACIÃ“N DOCKER Y PROTECCIÃ“N DE SECRETOS
    # ==========================================================
    add_h1("3. ConfiguraciÃ³n General de Despliegue en Docker Compose")
    add_p("La orquestaciÃ³n de la plataforma se unificÃ³ en el archivo 'docker/compose.yaml', complementado por la plantilla 'docker/.env.example'. Se aplicaron directivas estrictas de seguridad para proteger secretos:")
    add_bullet("El archivo '.env' con contraseÃ±as operativas locales queda excluido en '.gitignore'.", "ExclusiÃ³n en Control de Versiones: ")
    add_bullet("Se configuraron lÃ­mites de memoria ('MAX_HEAP_SIZE: 1024M', 'HEAP_NEWSIZE: 256M') para que Cassandra coexista con SQL Server, MongoDB y Neo4j sin saturar la RAM del host.", "GestiÃ³n de Recursos en Apache Cassandra: ")
    add_bullet("Cada servicio cuenta con variables parametrizadas con valores por defecto seguros para pruebas reproducibles.", "ParametrizaciÃ³n Limpia: ")

    img_docker = os.path.join(evid_dir, "generales", "01_docker_compose_ps.png")
    add_figure(img_docker, "Figura 1: Interfaz grÃ¡fica de Docker Desktop mostrando los 6 contenedores de CampusCloud activos, saludables y con sus puertos expuestos.")

    # ==========================================================
    # 5. EVIDENCIAS: MONGODB
    # ==========================================================
    add_h1("4. MisiÃ³n 2: MongoDB â€” Sector Documental")
    add_p("Se creÃ³ la colecciÃ³n 'detalles_servicios' en la base de datos 'CampusCloud', incorporando validaciÃ³n de esquemas 'JSON Schema' e Ã­ndices secundarios sobre 'codigo' (Ãºnico) e 'id_servicio_sql' para asegurar la correlaciÃ³n lÃ³gica con la tabla relacional.")
    
    add_h2("4.1 Carga Documental de Servicios")
    add_p("Se insertaron 8 documentos que cubren 4 categorÃ­as distintas ('Academico', 'Administrativo', 'Extracurricular', 'Salud_Estudiantil'), enriqueciendo con subdocumentos y arrays los 5 servicios originales de SQL Server:")
    add_bullet("Certificado de Estudios: modalidades ['En LÃ­nea', 'Ventanilla'], arancel $150.00, tiempo 3 dÃ­as.", "1. SRV-ACAD-01: ")
    add_bullet("ReexpediciÃ³n de Credencial: modalidades ['Presencial'], arancel $120.00, tiempo 5 dÃ­as.", "2. SRV-ADM-02: ")
    add_bullet("InscripciÃ³n a Taller: modalidades ['Presencial', 'Mixta'], arancel $0.00, tiempo 1 dÃ­a.", "3. SRV-EXT-03: ")
    add_bullet("Baja Temporal: modalidades ['Ventanilla', 'En LÃ­nea'], arancel $0.00, tiempo 10 dÃ­as.", "4. SRV-ADM-04: ")
    add_bullet("AsesorÃ­a AcadÃ©mica: modalidades ['Presencial', 'En LÃ­nea'], arancel $0.00, tiempo 2 dÃ­as.", "5. SRV-ACAD-05: ")
    add_bullet("Servicios complementarios: Bolsa de Trabajo, Servicio MÃ©dico y PrÃ©stamo Digital.", "6-8. Complementarios: ")

    add_h2("4.2 Consultas con Filtros Avanzados")
    add_p("Se desarrollaron y validaron 3 consultas estratÃ©gicas:")
    add_bullet("Filtra documentos donde el array 'modalidades' contiene 'En LÃ­nea' ('modalidades: \"En LÃ­nea\"'). RetornÃ³ 5 servicios activos.", "Consulta 1 (Array): ")
    add_bullet("Filtra por propiedad de subdocumento 'especificaciones.tiempo_estimado_dias: { $lte: 2 }'. RetornÃ³ 3 servicios inmediatos.", "Consulta 2 (Subdocumento): ")
    add_bullet("Operadores '$and' y '$or' para recuperar servicios gratuitos de categorÃ­as acadÃ©mica o extracurricular. RetornÃ³ 3 servicios coincidentes.", "Consulta 3 (LÃ³gica Compuesta): ")

    img_mongo_1 = os.path.join(evid_dir, "mongodb", "01_mongo_insert_find.png")
    add_figure(img_mongo_1, "Figura 2: Explorador de documentos BSON en MongoDB Compass sobre la colecciÃ³n detalles_servicios con el filtro { modalidades: 'En LÃ­nea' }.")

    add_h2("4.3 ActualizaciÃ³n y EliminaciÃ³n Controlada")
    add_p("Se demostraron transiciones verificables antes y despuÃ©s de cada operaciÃ³n:")
    add_bullet("Se aplicÃ³ '$set' para reducir el tiempo de entrega de 3 a 2 dÃ­as y '$addToSet' para insertar el requisito 'IdentificaciÃ³n oficial escaneada en formato PDF' sin duplicidad.", "ActualizaciÃ³n SRV-ACAD-01: ")
    add_bullet("Se ejecutÃ³ 'deleteOne({ codigo: \"SRV-ACAD-08\" })'. El conteo total de documentos transitÃ³ de 8 a 7.", "EliminaciÃ³n SRV-ACAD-08: ")

    add_h2("4.4 Pipeline de AgregaciÃ³n AnalÃ­tica")
    add_p("Mediante las etapas '$match', '$group', '$project' y '$sort', se computaron las mÃ©tricas consolidadas por categorÃ­a:")

    headers_agg = ["CategorÃ­a", "Total Servicios", "Tiempo Promedio (DÃ­as)", "Costo Promedio ($)", "Servicios Agrupados"]
    rows_agg = [
        ["Academico", "2", "2.0", "$75.00", "Certificado de Estudios, AsesorÃ­a AcadÃ©mica"],
        ["Administrativo", "2", "7.5", "$60.00", "ReexpediciÃ³n de Credencial, Baja Temporal"],
        ["Extracurricular", "2", "2.0", "$0.00", "InscripciÃ³n a Taller, Bolsa de Trabajo y EstadÃ­as"],
        ["Salud_Estudiantil", "1", "1.0", "$0.00", "Servicio MÃ©dico y PsicolÃ³gico"]
    ]
    add_custom_table(headers_agg, rows_agg, [1.4, 1.0, 1.2, 1.1, 1.8])

    img_mongo_2 = os.path.join(evid_dir, "mongodb", "02_mongo_update_aggregation.png")
    add_figure(img_mongo_2, "Figura 3: Constructor de Agregaciones en MongoDB Compass desplegando las etapas $match, $group y $sort con sus mÃ©tricas calculadas.")

    # ==========================================================
    # 6. EVIDENCIAS: NEO4J
    # ==========================================================
    add_h1("5. MisiÃ³n 3: Neo4j â€” Red de Grafos Vengadora")
    add_p("El mÃ³dulo de grafos de CampusCloud modela las interacciones sociales y acadÃ©micas de la comunidad universitaria. Se crearon 11 nodos y 17 aristas tipadas:")
    add_bullet("Mariano Calzadilla Alvarez (24300700), Ana Martinez (2026002), Carlos Gomez (2026003), Diana Lopez (2026004), Eduardo Hernandez (2026005) y Fernanda Torres (2026006).", "6 Nodos :Estudiante: ")
    add_bullet("Certificado de Estudios, ReexpediciÃ³n de Credencial, InscripciÃ³n a Taller, Baja Temporal y AsesorÃ­a AcadÃ©mica.", "5 Nodos :Servicio: ")
    add_bullet("':SOLICITA' (con propiedades de fecha, estado y calificaciÃ³n), ':COLABORA_CON' (proyectos y afinidad), ':TIENE_INTERES_EN' y ':PRERREQUISITO_DE'.", "17 Relaciones: ")

    add_h2("5.1 Consultas Cypher EstratÃ©gicas")
    add_p("Se formularon tres consultas para explotar el modelo de grafo:")
    add_bullet("Recupera el historial de servicios de Mariano Calzadilla Alvarez ('24300700'), mostrando sus calificaciones (5 estrellas en Certificado y 4 en Taller).", "1. Historial del Alumno: ")
    add_bullet("Identifica quÃ© alumnos estÃ¡n inscritos al mismo taller mediante el patrÃ³n '(e1)-[:SOLICITA]->(s)<-[:SOLICITA]-(e2)'. Se detectÃ³ conexiÃ³n directa entre Mariano Calzadilla Alvarez, Carlos Gomez y Fernanda Torres.", "2. DetecciÃ³n de CompaÃ±eros: ")
    add_bullet("Algoritmo que localiza quÃ© servicios han calificado con 4 o 5 estrellas los colaboradores directos de Mariano Calzadilla Alvarez que Ã©l aÃºn no ha solicitado, sugiriendo con Ã©xito 'AsesorÃ­a AcadÃ©mica' recomendada por Ana Martinez.", "3. RecomendaciÃ³n Colaborativa: ")

    img_neo4j_1 = os.path.join(evid_dir, "neo4j", "01_neo4j_cypher_shell.png")
    add_figure(img_neo4j_1, "Figura 4: EjecuciÃ³n en cypher-shell verificando 11 nodos, 17 relaciones y el algoritmo de recomendaciÃ³n colaborativa.")

    add_h2("5.2 VisualizaciÃ³n GrÃ¡fica de la Red")
    add_p("En Neo4j Browser, se ejecutÃ³ la consulta global para visualizar la red completa de relaciones. La interfaz despliega los nodos :Estudiante y :Servicio, permitiendo explorar interactivamente los atributos del estudiante Mariano Calzadilla Alvarez (matrÃ­cula 24300700) y sus trayectorias:")

    img_neo4j_2 = os.path.join(evid_dir, "neo4j", "02_neo4j_browser_graph.png")
    add_figure(img_neo4j_2, "Figura 5: VisualizaciÃ³n interactiva en Neo4j Browser desplegando la red de alianzas, solicitudes de servicio y el inspector de propiedades.")

    # ==========================================================
    # 7. EVIDENCIAS: CASSANDRA
    # ==========================================================
    add_h1("6. MisiÃ³n 4: Apache Cassandra â€” Sector Columnas Anchas")
    add_p("Para la ingesta continua de eventos y auditorÃ­a, se desplegÃ³ Apache Cassandra 4.1 con el keyspace 'campuscloud_logs' y la tabla 'eventos_estudiante'.")

    add_h2("6.1 DiseÃ±o Orientado a Consultas (Query-Driven Design)")
    add_p("En Cassandra, la clave primaria define la distribuciÃ³n fÃ­sica y a la velocidad de acceso:")
    add_bullet("Al definir '((matricula))' como Partition Key, el 'Murmur3Partitioner' almacena todas las acciones de un estudiante en un Ãºnico nodo del cluster, evitando escaneos globales distribuidos.", "Partition Key: ")
    add_bullet("Con '(fecha_hora, id_evento) WITH CLUSTERING ORDER BY (fecha_hora DESC)', los eventos se ordenan fÃ­sicamente en las SSTables del mÃ¡s reciente al mÃ¡s antiguo, permitiendo lecturas instantÃ¡neas de la actividad reciente.", "Clustering Keys: ")

    add_h2("6.2 InserciÃ³n Masiva y Consultas")
    add_p("Se insertaron 15 eventos cubriendo a Mariano Calzadilla Alvarez (24300700), Ana Martinez (2026002) y Carlos Gomez (2026003). Se ejecutaron exitosamente:")
    add_bullet("RecuperaciÃ³n de los 5 eventos de Mariano Calzadilla Alvarez ordenados secuencialmente de forma descendente.", "Consulta por ParticiÃ³n: ")
    add_bullet("Filtrado temporal 'WHERE matricula = \"24300700\" AND fecha_hora >= \"2026-11-01\" AND fecha_hora <= \"2026-11-05\"', recuperando 3 eventos.", "Consulta por Intervalo: ")

    img_cass_1 = os.path.join(evid_dir, "cassandra", "01_cassandra_cqlsh_select.png")
    add_figure(img_cass_1, "Figura 6: Cliente TablePlus conectado a Apache Cassandra ejecutando consulta CQL por clave de particiÃ³n (matricula) y clustering temporal descendente.")

    add_h2("6.3 Operaciones UPDATE, DELETE y Mecanismo de Tombstones")
    add_bullet("En CQL, todo UPDATE y DELETE requiere suministrar la Clave Primaria Completa. Si no existe, Cassandra ejecuta un Upsert atÃ³mico sin realizar lecturas previas en disco.", "RestricciÃ³n de Primary Key: ")
    add_bullet("El borrado no destruye inmediatamente los datos de la SSTable; escribe un 'Tombstone' que oculta el registro hasta que la compactaciÃ³n y el periodo 'gc_grace_seconds' purgan los bloques de almacenamiento.", "Tombstones: ")

    img_cass_2 = os.path.join(evid_dir, "cassandra", "02_cassandra_update_delete.png")
    add_figure(img_cass_2, "Figura 7: Consola interactiva cqlsh ejecutando modificaciÃ³n atÃ³mica de telemetrÃ­a y eliminaciÃ³n controlada demostrando el mecanismo de tombstones.")

    # ==========================================================
    # 8. PERSISTENCIA Y DIAGNÃ“STICO
    # ==========================================================
    add_h1("7. MisiÃ³n 5: Seguridad, Persistencia y DiagnÃ³stico de Incidencias")
    add_p("Se ejecutaron pruebas destructivas controladas para demostrar la resiliencia de la plataforma:")
    add_bullet("Se detuvieron y reiniciaron los contenedores con 'docker restart campuscloud-mongodb' y 'docker restart campuscloud-neo4j'. Los 7 documentos y 11 nodos permanecieron intactos gracias al montaje en los volÃºmenes de Docker.", "Persistencia en VolÃºmenes: ")
    add_bullet("MongoDB opera bajo autenticaciÃ³n obligatoria ('admin'), Neo4j con contraseÃ±a cifrada y SQL Server con contraseÃ±as seguras no triviales.", "Control de Acceso: ")

    add_h2("7.1 Incidencia TÃ©cnica Diagnosticada y Resuelta")
    add_p("Durante la fase de integraciÃ³n con el repositorio de trabajo, se presentÃ³ el siguiente error crÃ­tico:")
    add_code_block(doc, 
"""Error downloading object: docker_images/neo.tar (4d87078): Smudge error: 
[4d87078e...] Object does not exist on the server: [404] Object does not exist on the server
fatal: docker_images/neo.tar: smudge filter lfs failed""")
    add_p("DiagnÃ³stico: El repositorio colaborativo contenÃ­a un puntero Git LFS hacia un archivo binario de 592 MB no disponible en el almacenamiento remoto de GitHub.")
    add_p("SoluciÃ³n Preventiva: Se ajustÃ³ la configuraciÃ³n local de Git mediante 'git config --local filter.lfs.smudge \"git-lfs smudge --skip -- %f\"' y '$env:GIT_LFS_SKIP_SMUDGE=\"1\"', resolviendo el bloqueo de descarga y permitiendo un merge impecable sin degradar el proyecto.")

    # ==========================================================
    # 9. COMPARACIÃ“N LOCAL VS NUBE
    # ==========================================================
    add_h1("8. ComparaciÃ³n: Despliegue Local vs Servicios Administrados en la Nube")
    add_p("Es fundamental no confundir Docker Compose con un servicio administrado de nube. Docker es una herramienta de virtualizaciÃ³n liviana a nivel de sistema operativo (IaaS simulada), mientras que los servicios DBaaS (Database as a Service) de los tres grandes proveedores de nube ofrecen caracterÃ­sticas de nivel empresarial:")

    headers_cloud = ["Aspecto TÃ©cnico", "Despliegue Local Docker", "AWS (Amazon Web Services)", "Microsoft Azure", "Google Cloud (GCP)"]
    rows_cloud = [
        ["Motor Documental", "MongoDB 9.0 Community", "Amazon DocumentDB", "Azure Cosmos DB (Mongo API)", "Google Cloud Firestore"],
        ["Motor de Grafos", "Neo4j 5 Community", "Amazon Neptune", "Azure Cosmos DB (Gremlin)", "Spanner Graph"],
        ["Columnas Anchas", "Apache Cassandra 4.1", "Amazon Keyspaces (Cassandra)", "Azure Managed Cassandra", "Google Cloud Bigtable"],
        ["Alta Disponibilidad", "Nula (Monohost)", "Multi-AZ automÃ¡tico", "Multi-RegiÃ³n con 99.999% SLA", "Multi-Zona / Global"],
        ["Copias de Seguridad", "Manuales por script", "Continuas con PITR", "AutomÃ¡ticas periÃ³dicas", "Snapshots periÃ³dicos"],
        ["Parches y Mantenimiento", "Responsabilidad del Alumno", "100% Gestionado por AWS", "100% Gestionado por Azure", "100% Gestionado por GCP"]
    ]
    add_custom_table(headers_cloud, rows_cloud, [1.2, 1.3, 1.4, 1.3, 1.3])

    add_h2("8.1 Matriz de Responsabilidad Compartida")
    add_p("En un servicio administrado en la nube, el proveedor asume la infraestructura fÃ­sica, los hipervisores, la red, el sistema operativo y la redundancia de discos. El cliente conserva exclusivamente la responsabilidad sobre el diseÃ±o del esquema de datos, la optimizaciÃ³n de las consultas, la configuraciÃ³n de polÃ­ticas de acceso (IAM / RBAC) y el cifrado de datos sensibles.")

    # ==========================================================
    # 10. CONCLUSIONES Y REFERENCIAS
    # ==========================================================
    add_h1("9. Conclusiones y Referencias")
    add_p("La implementaciÃ³n de la arquitectura NoSQL para CampusCloud demuestra que ningÃºn motor de base de datos es superior de forma absoluta, sino que la excelencia de un arquitecto de software radica en seleccionar el motor adecuado para cada caso de uso. SQL Server garantiza la consistencia transaccional del expediente de los estudiantes; MongoDB flexibiliza las caracterÃ­sticas cambiantes de los trÃ¡mites; Neo4j visibiliza las comunidades y redes de afinidad acadÃ©mica; y Apache Cassandra ofrece la escala y velocidad requerida para la auditorÃ­a de eventos masivos.")
    
    add_h2("Referencias BibliogrÃ¡ficas (Formato APA 7ma EdiciÃ³n)")
    add_bullet("Amazon Relational Database Service and Keyspaces Developer Guide. Amazon Web Services Documentation. https://docs.aws.amazon.com/keyspaces/", "Amazon Web Services. (2026). ")
    add_bullet("Apache Cassandra Documentation and Architecture Overview (v4.1). The Apache Software Foundation. https://cassandra.apache.org/doc/latest/", "Apache Software Foundation. (2026). ")
    add_bullet("Azure Cosmos DB: Distributed NoSQL and Multi-Model Cloud Database. Microsoft Learn. https://learn.microsoft.com/azure/cosmos-db/", "Microsoft Azure. (2026). ")
    add_bullet("MongoDB Manual: Aggregation Operations, Document Validation and Indexing. MongoDB Inc. https://www.mongodb.com/docs/manual/", "MongoDB Inc. (2026). ")
    add_bullet("The Neo4j Cypher Manual: Graph Database Modeling and Query Optimization. Neo4j Graph Data Platform. https://neo4j.com/docs/cypher-manual/current/", "Neo4j Inc. (2026). ")

    # Guardar documento Word
    output_docx = os.path.abspath(os.path.join(os.path.dirname(__file__), "Calzadilla_Mariano_ReportePracticas_NoSQL.docx"))
    doc.save(output_docx)
    print(f"[OK] Reporte DOCX generado exitosamente en: {output_docx}")

    # Copiar DOCX a la raÃ­z del proyecto
    root_docx = os.path.join(base_proj, "Calzadilla_Mariano_ReportePracticas_NoSQL.docx")
    import shutil
    shutil.copy2(output_docx, root_docx)

    # Convertir a PDF si docx2pdf / Word COM estÃ¡ disponible
    output_pdf = os.path.abspath(os.path.join(os.path.dirname(__file__), "Calzadilla_Mariano_ReportePracticas_NoSQL.pdf"))
    try:
        from docx2pdf import convert
        print(f"Convirtiendo DOCX a PDF...")
        convert(output_docx, output_pdf)
        print(f"[OK] Reporte PDF generado exitosamente en: {output_pdf}")
        
        # Copiar PDF a la raÃ­z del proyecto
        root_pdf = os.path.join(base_proj, "Calzadilla_Mariano_ReportePracticas_NoSQL.pdf")
        shutil.copy2(output_pdf, root_pdf)
        print(f"[OK] Reporte PDF copiado a la raÃ­z: {root_pdf}")
    except Exception as e:
        print(f"[AVISO] No se pudo convertir automÃ¡ticamente a PDF mediante docx2pdf: {e}")

if __name__ == "__main__":
    create_report()
