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

    # Configurar márgenes de 1 pulgada (2.54 cm)
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
    r_inst = p_title.add_run("UNIVERSIDAD TECNOLÓGICA DE TULA-TEPEJI\n")
    r_inst.font.name = "Calibri"
    r_inst.font.size = Pt(16)
    r_inst.font.bold = True
    r_inst.font.color.rgb = navy

    r_sub = p_title.add_run("Área de Tecnologías de la Información • Bases de Datos en la Nube\n\n")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(12)
    r_sub.font.bold = True
    r_sub.font.color.rgb = dark_gray

    r_main = p_title.add_run("OPERACIÓN CAMPUSCLOUD\nPROTOCOLO NoSQL: DEFENSA DE LA ARQUITECTURA DE DATOS\n")
    r_main.font.name = "Calibri"
    r_main.font.size = Pt(18)
    r_main.font.bold = True
    r_main.font.color.rgb = navy

    r_act = p_title.add_run("Actividad de Evaluación 2 • Unidad II: Bases de Datos No Relacionales en la Nube (55 %)\n")
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
        "MATRÍCULA: 24300700\n"
        "CARRERA: Ingeniería en Tecnologías de la Información e Innovación Digital\n"
        "GRUPO / CUATRIMESTRE: 7° Cuatrimestre\n"
        "DOCENTE: Mtro. de Asignatura de Bases de Datos en la Nube\n"
        "FECHA DE ENTREGA: Noviembre de 2026\n"
        "ESTADO DE LA MISIÓN: COMPLETADA CON ÉXITO"
    )
    r_meta = p_meta.add_run(meta_text)
    r_meta.font.name = "Calibri"
    r_meta.font.size = Pt(10.5)
    r_meta.font.color.rgb = charcoal

    doc.add_page_break()

    # ==========================================================
    # 2. PROBLEMA Y SELECCIÓN DE MODELOS
    # ==========================================================
    add_h1("1. Problema y Selección de Modelos NoSQL")
    add_p("Durante la Unidad I, el ecosistema CampusCloud consolidó una base de datos relacional sobre Microsoft SQL Server 2022 (con réplica en PostgreSQL), sustentando las entidades fundamentales de 'Estudiantes', 'Servicios' y 'Solicitudes'. Sin embargo, la expansión operativa hacia una Nube Académica Integral generó tres requerimientos que pusieron en jaque el modelo tabular tradicional:")
    
    add_bullet(" La rigidez de las tablas relacionales obligaba a alterar el esquema ('ALTER TABLE') cada vez que un servicio requería requisitos particulares, aranceles o dependencias distintas, provocando columnas dispersas ('sparse columns') con excesivos valores nulos.", "A. Heterogeneidad en el Catálogo de Servicios: ")
    add_bullet(" Determinar la afinidad entre estudiantes, sus alianzas para proyectos y la recomendación cruzada de servicios requería consultas 'JOIN' recursivas y complejas que degradaban el motor SQL Server.", "B. Red Compleja de Alianzas y Conexiones Académicas: ")
    add_bullet(" El flujo continuo de interacciones, descargas de constancias y auditoría de accesos generaba un volumen de escrituras concurrente que saturaba el 'Transaction Log' (.ldf) de SQL Server.", "C. Telemetría y Registro de Eventos Masivos: ")

    add_p("En observancia del briefing oficial de la misión, no se sustituyó SQL Server; en su lugar, se adoptó el paradigma de Persistencia Políglota (Polyglot Persistence) integrando tres tecnologías complementarias:")

    headers_mod = ["Paradigma NoSQL", "Motor Elegido", "Caso de Uso en CampusCloud", "Justificación Técnica"]
    rows_mod = [
        ["Documental", "MongoDB 9.0 Community", "Catálogo dinámico de servicios extendidos", "Almacena documentos BSON semiestructurados con arrays de requisitos y subdocumentos de especificaciones técnicas sin alterar el esquema central."],
        ["Grafos", "Neo4j 5 Community", "Red de alianzas, afinidades y recomendación", "Modela directamente a los estudiantes y servicios como nodos y sus interacciones como aristas tipadas con propiedades, optimizando algoritmos de grafos."],
        ["Columnas Anchas", "Apache Cassandra 4.1", "Bitácora masiva de telemetría y auditoría", "Escritura append-only ultrarrápida en disco (SSTables), consultas por partición de estudiante ('matricula') y orden temporal descendente."]
    ]
    add_custom_table(headers_mod, rows_mod, [1.2, 1.2, 2.0, 2.1])

    # ==========================================================
    # 3. ARQUITECTURA DE CAMPUSCLOUD
    # ==========================================================
    add_h1("2. Arquitectura del Sistema CampusCloud")
    add_p("La infraestructura se encuentra completamente contenida en Docker bajo una red puente común ('campuscloud-db-net'), garantizando comunicación directa vía DNS entre los servicios, aislamiento perimetral y persistencia mediante volúmenes nombrados independientes:")

    add_code_block(doc, 
"""+---------------------------------------------------------------------------------+
|                       ESTACIÓN HOST WINDOWS (DOCKER ENGINE)                     |
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
        "PRINCIPIO DE CONTENCIÓN Y AISLAMIENTO"
    )

    # ==========================================================
    # 4. CONFIGURACIÓN DOCKER Y PROTECCIÓN DE SECRETOS
    # ==========================================================
    add_h1("3. Configuración General de Despliegue en Docker Compose")
    add_p("La orquestación de la plataforma se unificó en el archivo 'docker/compose.yaml', complementado por la plantilla 'docker/.env.example'. Se aplicaron directivas estrictas de seguridad para proteger secretos:")
    add_bullet("El archivo '.env' con contraseñas operativas locales queda excluido en '.gitignore'.", "Exclusión en Control de Versiones: ")
    add_bullet("Se configuraron límites de memoria ('MAX_HEAP_SIZE: 1024M', 'HEAP_NEWSIZE: 256M') para que Cassandra coexista con SQL Server, MongoDB y Neo4j sin saturar la RAM del host.", "Gestión de Recursos en Apache Cassandra: ")
    add_bullet("Cada servicio cuenta con variables parametrizadas con valores por defecto seguros para pruebas reproducibles.", "Parametrización Limpia: ")

    img_docker = os.path.join(evid_dir, "generales", "01_docker_compose_ps.png")
    add_figure(img_docker, "Figura 1: Interfaz gráfica de Docker Desktop mostrando los 6 contenedores de CampusCloud activos, saludables y con sus puertos expuestos.")

    # ==========================================================
    # 5. EVIDENCIAS: MONGODB
    # ==========================================================
    add_h1("4. Misión 2: MongoDB — Sector Documental")
    add_p("Se creó la colección 'detalles_servicios' en la base de datos 'CampusCloud', incorporando validación de esquemas 'JSON Schema' e índices secundarios sobre 'codigo' (único) e 'id_servicio_sql' para asegurar la correlación lógica con la tabla relacional.")
    
    add_h2("4.1 Carga Documental de Servicios")
    add_p("Se insertaron 8 documentos que cubren 4 categorías distintas ('Academico', 'Administrativo', 'Extracurricular', 'Salud_Estudiantil'), enriqueciendo con subdocumentos y arrays los 5 servicios originales de SQL Server:")
    add_bullet("Certificado de Estudios: modalidades ['En Línea', 'Ventanilla'], arancel $150.00, tiempo 3 días.", "1. SRV-ACAD-01: ")
    add_bullet("Reexpedición de Credencial: modalidades ['Presencial'], arancel $120.00, tiempo 5 días.", "2. SRV-ADM-02: ")
    add_bullet("Inscripción a Taller: modalidades ['Presencial', 'Mixta'], arancel $0.00, tiempo 1 día.", "3. SRV-EXT-03: ")
    add_bullet("Baja Temporal: modalidades ['Ventanilla', 'En Línea'], arancel $0.00, tiempo 10 días.", "4. SRV-ADM-04: ")
    add_bullet("Asesoría Académica: modalidades ['Presencial', 'En Línea'], arancel $0.00, tiempo 2 días.", "5. SRV-ACAD-05: ")
    add_bullet("Servicios complementarios: Bolsa de Trabajo, Servicio Médico y Préstamo Digital.", "6-8. Complementarios: ")

    add_h2("4.2 Consultas con Filtros Avanzados")
    add_p("Se desarrollaron y validaron 3 consultas estratégicas:")
    add_bullet("Filtra documentos donde el array 'modalidades' contiene 'En Línea' ('modalidades: \"En Línea\"'). Retornó 5 servicios activos.", "Consulta 1 (Array): ")
    add_bullet("Filtra por propiedad de subdocumento 'especificaciones.tiempo_estimado_dias: { $lte: 2 }'. Retornó 3 servicios inmediatos.", "Consulta 2 (Subdocumento): ")
    add_bullet("Operadores '$and' y '$or' para recuperar servicios gratuitos de categorías académica o extracurricular. Retornó 3 servicios coincidentes.", "Consulta 3 (Lógica Compuesta): ")

    img_mongo_1 = os.path.join(evid_dir, "mongodb", "01_mongo_insert_find.png")
    add_figure(img_mongo_1, "Figura 2: Explorador de documentos BSON en MongoDB Compass sobre la colección detalles_servicios con el filtro { modalidades: 'En Línea' }.")

    add_h2("4.3 Actualización y Eliminación Controlada")
    add_p("Se demostraron transiciones verificables antes y después de cada operación:")
    add_bullet("Se aplicó '$set' para reducir el tiempo de entrega de 3 a 2 días y '$addToSet' para insertar el requisito 'Identificación oficial escaneada en formato PDF' sin duplicidad.", "Actualización SRV-ACAD-01: ")
    add_bullet("Se ejecutó 'deleteOne({ codigo: \"SRV-ACAD-08\" })'. El conteo total de documentos transitó de 8 a 7.", "Eliminación SRV-ACAD-08: ")

    add_h2("4.4 Pipeline de Agregación Analítica")
    add_p("Mediante las etapas '$match', '$group', '$project' y '$sort', se computaron las métricas consolidadas por categoría:")

    headers_agg = ["Categoría", "Total Servicios", "Tiempo Promedio (Días)", "Costo Promedio ($)", "Servicios Agrupados"]
    rows_agg = [
        ["Academico", "2", "2.0", "$75.00", "Certificado de Estudios, Asesoría Académica"],
        ["Administrativo", "2", "7.5", "$60.00", "Reexpedición de Credencial, Baja Temporal"],
        ["Extracurricular", "2", "2.0", "$0.00", "Inscripción a Taller, Bolsa de Trabajo y Estadías"],
        ["Salud_Estudiantil", "1", "1.0", "$0.00", "Servicio Médico y Psicológico"]
    ]
    add_custom_table(headers_agg, rows_agg, [1.4, 1.0, 1.2, 1.1, 1.8])

    img_mongo_2 = os.path.join(evid_dir, "mongodb", "02_mongo_update_aggregation.png")
    add_figure(img_mongo_2, "Figura 3: Constructor de Agregaciones en MongoDB Compass desplegando las etapas $match, $group y $sort con sus métricas calculadas.")

    # ==========================================================
    # 6. EVIDENCIAS: NEO4J
    # ==========================================================
    add_h1("5. Misión 3: Neo4j — Red de Grafos Vengadora")
    add_p("El módulo de grafos de CampusCloud modela las interacciones sociales y académicas de la comunidad universitaria. Se crearon 11 nodos y 17 aristas tipadas:")
    add_bullet("Mariano Silva (24300700), Ana Martinez (2026002), Carlos Gomez (2026003), Diana Lopez (2026004), Eduardo Hernandez (2026005) y Fernanda Torres (2026006).", "6 Nodos :Estudiante: ")
    add_bullet("Certificado de Estudios, Reexpedición de Credencial, Inscripción a Taller, Baja Temporal y Asesoría Académica.", "5 Nodos :Servicio: ")
    add_bullet("':SOLICITA' (con propiedades de fecha, estado y calificación), ':COLABORA_CON' (proyectos y afinidad), ':TIENE_INTERES_EN' y ':PRERREQUISITO_DE'.", "17 Relaciones: ")

    add_h2("5.1 Consultas Cypher Estratégicas")
    add_p("Se formularon tres consultas para explotar el modelo de grafo:")
    add_bullet("Recupera el historial de servicios de Mariano Silva ('24300700'), mostrando sus calificaciones (5 estrellas en Certificado y 4 en Taller).", "1. Historial del Alumno: ")
    add_bullet("Identifica qué alumnos están inscritos al mismo taller mediante el patrón '(e1)-[:SOLICITA]->(s)<-[:SOLICITA]-(e2)'. Se detectó conexión directa entre Mariano Silva, Carlos Gomez y Fernanda Torres.", "2. Detección de Compañeros: ")
    add_bullet("Algoritmo que localiza qué servicios han calificado con 4 o 5 estrellas los colaboradores directos de Mariano Silva que él aún no ha solicitado, sugiriendo con éxito 'Asesoría Académica' recomendada por Ana Martinez.", "3. Recomendación Colaborativa: ")

    img_neo4j_1 = os.path.join(evid_dir, "neo4j", "01_neo4j_cypher_shell.png")
    add_figure(img_neo4j_1, "Figura 4: Ejecución en cypher-shell verificando 11 nodos, 17 relaciones y el algoritmo de recomendación colaborativa.")

    add_h2("5.2 Visualización Gráfica de la Red")
    add_p("En Neo4j Browser, se ejecutó la consulta global para visualizar la red completa de relaciones. La interfaz despliega los nodos :Estudiante y :Servicio, permitiendo explorar interactivamente los atributos del estudiante Mariano Silva (matrícula 24300700) y sus trayectorias:")

    img_neo4j_2 = os.path.join(evid_dir, "neo4j", "02_neo4j_browser_graph.png")
    add_figure(img_neo4j_2, "Figura 5: Visualización interactiva en Neo4j Browser desplegando la red de alianzas, solicitudes de servicio y el inspector de propiedades.")

    # ==========================================================
    # 7. EVIDENCIAS: CASSANDRA
    # ==========================================================
    add_h1("6. Misión 4: Apache Cassandra — Sector Columnas Anchas")
    add_p("Para la ingesta continua de eventos y auditoría, se desplegó Apache Cassandra 4.1 con el keyspace 'campuscloud_logs' y la tabla 'eventos_estudiante'.")

    add_h2("6.1 Diseño Orientado a Consultas (Query-Driven Design)")
    add_p("En Cassandra, la clave primaria define la distribución física y a la velocidad de acceso:")
    add_bullet("Al definir '((matricula))' como Partition Key, el 'Murmur3Partitioner' almacena todas las acciones de un estudiante en un único nodo del cluster, evitando escaneos globales distribuidos.", "Partition Key: ")
    add_bullet("Con '(fecha_hora, id_evento) WITH CLUSTERING ORDER BY (fecha_hora DESC)', los eventos se ordenan físicamente en las SSTables del más reciente al más antiguo, permitiendo lecturas instantáneas de la actividad reciente.", "Clustering Keys: ")

    add_h2("6.2 Inserción Masiva y Consultas")
    add_p("Se insertaron 15 eventos cubriendo a Mariano Silva (24300700), Ana Martinez (2026002) y Carlos Gomez (2026003). Se ejecutaron exitosamente:")
    add_bullet("Recuperación de los 5 eventos de Mariano Silva ordenados secuencialmente de forma descendente.", "Consulta por Partición: ")
    add_bullet("Filtrado temporal 'WHERE matricula = \"24300700\" AND fecha_hora >= \"2026-11-01\" AND fecha_hora <= \"2026-11-05\"', recuperando 3 eventos.", "Consulta por Intervalo: ")

    img_cass_1 = os.path.join(evid_dir, "cassandra", "01_cassandra_cqlsh_select.png")
    add_figure(img_cass_1, "Figura 6: Cliente TablePlus conectado a Apache Cassandra ejecutando consulta CQL por clave de partición (matricula) y clustering temporal descendente.")

    add_h2("6.3 Operaciones UPDATE, DELETE y Mecanismo de Tombstones")
    add_bullet("En CQL, todo UPDATE y DELETE requiere suministrar la Clave Primaria Completa. Si no existe, Cassandra ejecuta un Upsert atómico sin realizar lecturas previas en disco.", "Restricción de Primary Key: ")
    add_bullet("El borrado no destruye inmediatamente los datos de la SSTable; escribe un 'Tombstone' que oculta el registro hasta que la compactación y el periodo 'gc_grace_seconds' purgan los bloques de almacenamiento.", "Tombstones: ")

    img_cass_2 = os.path.join(evid_dir, "cassandra", "02_cassandra_update_delete.png")
    add_figure(img_cass_2, "Figura 7: Consola interactiva cqlsh ejecutando modificación atómica de telemetría y eliminación controlada demostrando el mecanismo de tombstones.")

    # ==========================================================
    # 8. PERSISTENCIA Y DIAGNÓSTICO
    # ==========================================================
    add_h1("7. Misión 5: Seguridad, Persistencia y Diagnóstico de Incidencias")
    add_p("Se ejecutaron pruebas destructivas controladas para demostrar la resiliencia de la plataforma:")
    add_bullet("Se detuvieron y reiniciaron los contenedores con 'docker restart campuscloud-mongodb' y 'docker restart campuscloud-neo4j'. Los 7 documentos y 11 nodos permanecieron intactos gracias al montaje en los volúmenes de Docker.", "Persistencia en Volúmenes: ")
    add_bullet("MongoDB opera bajo autenticación obligatoria ('admin'), Neo4j con contraseña cifrada y SQL Server con contraseñas seguras no triviales.", "Control de Acceso: ")

    add_h2("7.1 Incidencia Técnica Diagnosticada y Resuelta")
    add_p("Durante la fase de integración con el repositorio de trabajo, se presentó el siguiente error crítico:")
    add_code_block(doc, 
"""Error downloading object: docker_images/neo.tar (4d87078): Smudge error: 
[4d87078e...] Object does not exist on the server: [404] Object does not exist on the server
fatal: docker_images/neo.tar: smudge filter lfs failed""")
    add_p("Diagnóstico: El repositorio colaborativo contenía un puntero Git LFS hacia un archivo binario de 592 MB no disponible en el almacenamiento remoto de GitHub.")
    add_p("Solución Preventiva: Se ajustó la configuración local de Git mediante 'git config --local filter.lfs.smudge \"git-lfs smudge --skip -- %f\"' y '$env:GIT_LFS_SKIP_SMUDGE=\"1\"', resolviendo el bloqueo de descarga y permitiendo un merge impecable sin degradar el proyecto.")

    # ==========================================================
    # 9. COMPARACIÓN LOCAL VS NUBE
    # ==========================================================
    add_h1("8. Comparación: Despliegue Local vs Servicios Administrados en la Nube")
    add_p("Es fundamental no confundir Docker Compose con un servicio administrado de nube. Docker es una herramienta de virtualización liviana a nivel de sistema operativo (IaaS simulada), mientras que los servicios DBaaS (Database as a Service) de los tres grandes proveedores de nube ofrecen características de nivel empresarial:")

    headers_cloud = ["Aspecto Técnico", "Despliegue Local Docker", "AWS (Amazon Web Services)", "Microsoft Azure", "Google Cloud (GCP)"]
    rows_cloud = [
        ["Motor Documental", "MongoDB 9.0 Community", "Amazon DocumentDB", "Azure Cosmos DB (Mongo API)", "Google Cloud Firestore"],
        ["Motor de Grafos", "Neo4j 5 Community", "Amazon Neptune", "Azure Cosmos DB (Gremlin)", "Spanner Graph"],
        ["Columnas Anchas", "Apache Cassandra 4.1", "Amazon Keyspaces (Cassandra)", "Azure Managed Cassandra", "Google Cloud Bigtable"],
        ["Alta Disponibilidad", "Nula (Monohost)", "Multi-AZ automático", "Multi-Región con 99.999% SLA", "Multi-Zona / Global"],
        ["Copias de Seguridad", "Manuales por script", "Continuas con PITR", "Automáticas periódicas", "Snapshots periódicos"],
        ["Parches y Mantenimiento", "Responsabilidad del Alumno", "100% Gestionado por AWS", "100% Gestionado por Azure", "100% Gestionado por GCP"]
    ]
    add_custom_table(headers_cloud, rows_cloud, [1.2, 1.3, 1.4, 1.3, 1.3])

    add_h2("8.1 Matriz de Responsabilidad Compartida")
    add_p("En un servicio administrado en la nube, el proveedor asume la infraestructura física, los hipervisores, la red, el sistema operativo y la redundancia de discos. El cliente conserva exclusivamente la responsabilidad sobre el diseño del esquema de datos, la optimización de las consultas, la configuración de políticas de acceso (IAM / RBAC) y el cifrado de datos sensibles.")

    # ==========================================================
    # 10. CONCLUSIONES Y REFERENCIAS
    # ==========================================================
    add_h1("9. Conclusiones y Referencias")
    add_p("La implementación de la arquitectura NoSQL para CampusCloud demuestra que ningún motor de base de datos es superior de forma absoluta, sino que la excelencia de un arquitecto de software radica en seleccionar el motor adecuado para cada caso de uso. SQL Server garantiza la consistencia transaccional del expediente de los estudiantes; MongoDB flexibiliza las características cambiantes de los trámites; Neo4j visibiliza las comunidades y redes de afinidad académica; y Apache Cassandra ofrece la escala y velocidad requerida para la auditoría de eventos masivos.")
    
    add_h2("Referencias Bibliográficas (Formato APA 7ma Edición)")
    add_bullet("Amazon Relational Database Service and Keyspaces Developer Guide. Amazon Web Services Documentation. https://docs.aws.amazon.com/keyspaces/", "Amazon Web Services. (2026). ")
    add_bullet("Apache Cassandra Documentation and Architecture Overview (v4.1). The Apache Software Foundation. https://cassandra.apache.org/doc/latest/", "Apache Software Foundation. (2026). ")
    add_bullet("Azure Cosmos DB: Distributed NoSQL and Multi-Model Cloud Database. Microsoft Learn. https://learn.microsoft.com/azure/cosmos-db/", "Microsoft Azure. (2026). ")
    add_bullet("MongoDB Manual: Aggregation Operations, Document Validation and Indexing. MongoDB Inc. https://www.mongodb.com/docs/manual/", "MongoDB Inc. (2026). ")
    add_bullet("The Neo4j Cypher Manual: Graph Database Modeling and Query Optimization. Neo4j Graph Data Platform. https://neo4j.com/docs/cypher-manual/current/", "Neo4j Inc. (2026). ")

    # Guardar documento Word
    output_docx = os.path.abspath(os.path.join(os.path.dirname(__file__), "Calzadilla_Mariano_ReportePracticas_NoSQL.docx"))
    doc.save(output_docx)
    print(f"[OK] Reporte DOCX generado exitosamente en: {output_docx}")

    # Copiar DOCX a la raíz del proyecto
    root_docx = os.path.join(base_proj, "Calzadilla_Mariano_ReportePracticas_NoSQL.docx")
    import shutil
    shutil.copy2(output_docx, root_docx)

    # Convertir a PDF si docx2pdf / Word COM está disponible
    output_pdf = os.path.abspath(os.path.join(os.path.dirname(__file__), "Calzadilla_Mariano_ReportePracticas_NoSQL.pdf"))
    try:
        from docx2pdf import convert
        print(f"Convirtiendo DOCX a PDF...")
        convert(output_docx, output_pdf)
        print(f"[OK] Reporte PDF generado exitosamente en: {output_pdf}")
        
        # Copiar PDF a la raíz del proyecto
        root_pdf = os.path.join(base_proj, "Calzadilla_Mariano_ReportePracticas_NoSQL.pdf")
        shutil.copy2(output_pdf, root_pdf)
        print(f"[OK] Reporte PDF copiado a la raíz: {root_pdf}")
    except Exception as e:
        print(f"[AVISO] No se pudo convertir automáticamente a PDF mediante docx2pdf: {e}")

if __name__ == "__main__":
    create_report()
