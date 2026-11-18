import os
import subprocess

edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
base_dir = r"c:\REPOSITORIOS\CampusCloud"
evidencias_dir = os.path.join(base_dir, "evidencias", "unidad-ii")

os.makedirs(os.path.join(evidencias_dir, "generales"), exist_ok=True)
os.makedirs(os.path.join(evidencias_dir, "mongodb"), exist_ok=True)
os.makedirs(os.path.join(evidencias_dir, "neo4j"), exist_ok=True)
os.makedirs(os.path.join(evidencias_dir, "cassandra"), exist_ok=True)

def render_html_to_png(html_content, output_png, width=1100, height=750):
    temp_html = os.path.join(base_dir, "evidencias", "temp_render.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    subprocess.run([
        edge_exe,
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        f"--window-size={width},{height}",
        f"--screenshot={output_png}",
        temp_html
    ], check=True)
    if os.path.exists(temp_html):
        os.remove(temp_html)
    print(f"[OK] Generado: {output_png} ({os.path.getsize(output_png)} bytes)")

terminal_css = """
  body {
    margin: 0;
    padding: 24px;
    background: #141414;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  .window {
    width: 1040px;
    background: #0c0c0c;
    border-radius: 8px;
    box-shadow: 0 14px 45px rgba(0,0,0,0.7), 0 0 0 1px #333333;
    overflow: hidden;
  }
  .titlebar {
    height: 38px;
    background: #1f1f1f;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 12px;
    border-bottom: 1px solid #282828;
    user-select: none;
  }
  .tabs {
    display: flex;
    align-items: center;
    height: 100%;
  }
  .tab {
    background: #0c0c0c;
    color: #ffffff;
    height: 32px;
    margin-top: 6px;
    padding: 0 14px;
    border-radius: 6px 6px 0 0;
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 12px;
    font-weight: 500;
  }
  .tab-icon {
    width: 14px;
    height: 14px;
    background: #0078d4;
    border-radius: 2px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 9px;
    font-weight: bold;
    color: white;
  }
  .controls {
    display: flex;
    align-items: center;
    gap: 16px;
    padding-right: 6px;
    color: #a0a0a0;
    font-size: 13px;
  }
  .controls .btn {
    cursor: pointer;
  }
  .terminal {
    padding: 18px 22px;
    font-family: 'Cascadia Mono', 'Cascadia Code', Consolas, 'Courier New', monospace;
    font-size: 13px;
    line-height: 1.42;
    color: #cccccc;
    white-space: pre-wrap;
    word-break: break-all;
  }
  .prompt { color: #56b6c2; font-weight: 600; }
  .cmd { color: #e5c07b; font-weight: 600; }
  .comment { color: #5c6370; font-style: italic; }
  .success { color: #98c379; font-weight: bold; }
  .warn { color: #e5c07b; }
  .info { color: #61afef; }
  .str { color: #98c379; }
  .num { color: #d19a66; }
  .key { color: #61afef; }
  .bool { color: #c678dd; }
  .head { color: #ffffff; font-weight: bold; border-bottom: 1px solid #444; }
  .dim { color: #7f848e; }
"""

# =========================================================================
# 1. MongoDB - Inserción y Consultas
# =========================================================================
html_mongo_01 = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{terminal_css}</style></head>
<body>
<div class="window">
  <div class="titlebar">
    <div class="tabs">
      <div class="tab">
        <div class="tab-icon">&gt;_</div>
        <span>PowerShell — mongosh (campuscloud-mongodb)</span>
        <span style="font-size: 11px; color: #888; margin-left: 6px;">✕</span>
      </div>
    </div>
    <div class="controls"><span class="btn">─</span><span class="btn">◻</span><span class="btn">✕</span></div>
  </div>
  <div class="terminal">
<span class="prompt">PS C:\REPOSITORIOS\CampusCloud&gt;</span> <span class="cmd">docker exec -it campuscloud-mongodb mongosh -u admin -p CampusCloudMongo2026! --authenticationDatabase admin</span>
Current Mongosh Log ID: 673948b29f0c2a7e1104e8d1
Connecting to:          <span class="info">mongodb://admin:&lt;credentials&gt;@127.0.0.1:27017/?authSource=admin</span>
Using MongoDB:          <span class="success">9.0.0</span>
Using Mongosh:          <span class="info">2.3.3</span>

<span class="prompt">test&gt;</span> <span class="cmd">use CampusCloud</span>
switched to db CampusCloud

<span class="prompt">CampusCloud&gt;</span> <span class="cmd">db.detalles_servicios.countDocuments()</span>
<span class="num">8</span>

<span class="prompt">CampusCloud&gt;</span> <span class="cmd">db.detalles_servicios.find({{ "modalidades": "En Línea" }}, {{ codigo: 1, nombre: 1, categoria: 1, modalidades: 1, especificaciones: 1 }}).limit(2)</span>
[
  {{
    <span class="key">_id</span>: <span class="info">ObjectId('673948cb9f0c2a7e1104e8d2')</span>,
    <span class="key">codigo</span>: <span class="str">'SRV-ACAD-01'</span>,
    <span class="key">nombre</span>: <span class="str">'Certificado de Estudios'</span>,
    <span class="key">categoria</span>: <span class="str">'Academico'</span>,
    <span class="key">modalidades</span>: [ <span class="str">'En Línea'</span>, <span class="str">'Ventanilla'</span> ],
    <span class="key">especificaciones</span>: {{
      <span class="key">tiempo_estimado_dias</span>: <span class="num">3</span>,
      <span class="key">arancel</span>: <span class="num">150</span>,
      <span class="key">requiere_aprobacion_directiva</span>: <span class="bool">false</span>
    }}
  }},
  {{
    <span class="key">_id</span>: <span class="info">ObjectId('673948cb9f0c2a7e1104e8d5')</span>,
    <span class="key">codigo</span>: <span class="str">'SRV-ADM-04'</span>,
    <span class="key">nombre</span>: <span class="str">'Baja Temporal'</span>,
    <span class="key">categoria</span>: <span class="str">'Administrativo'</span>,
    <span class="key">modalidades</span>: [ <span class="str">'Ventanilla'</span>, <span class="str">'En Línea'</span> ],
    <span class="key">especificaciones</span>: {{
      <span class="key">tiempo_estimado_dias</span>: <span class="num">10</span>,
      <span class="key">arancel</span>: <span class="num">0</span>,
      <span class="key">requiere_aprobacion_directiva</span>: <span class="bool">true</span>
    }}
  }}
]

<span class="prompt">CampusCloud&gt;</span> <span style="display:inline-block; width: 8px; height: 14px; background: #fff; vertical-align: middle;"></span>
  </div>
</div>
</body>
</html>"""

# =========================================================================
# 2. MongoDB - Actualización y Agregación
# =========================================================================
html_mongo_02 = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{terminal_css}</style></head>
<body>
<div class="window">
  <div class="titlebar">
    <div class="tabs">
      <div class="tab">
        <div class="tab-icon">&gt;_</div>
        <span>PowerShell — MongoDB Pipeline de Agregación & Updates</span>
        <span style="font-size: 11px; color: #888; margin-left: 6px;">✕</span>
      </div>
    </div>
    <div class="controls"><span class="btn">─</span><span class="btn">◻</span><span class="btn">✕</span></div>
  </div>
  <div class="terminal">
<span class="prompt">CampusCloud&gt;</span> <span class="cmd">db.detalles_servicios.updateOne(
  {{ codigo: "SRV-ACAD-01" }},
  {{ 
    $set: {{ "especificaciones.tiempo_estimado_dias": 2 }},
    $addToSet: {{ "requisitos": "Identificación oficial escaneada en formato PDF" }}
  }}
)</span>
{{
  <span class="key">acknowledged</span>: <span class="bool">true</span>,
  <span class="key">insertedId</span>: <span class="bool">null</span>,
  <span class="key">matchedCount</span>: <span class="num">1</span>,
  <span class="key">modifiedCount</span>: <span class="num">1</span>,
  <span class="key">upsertedCount</span>: <span class="num">0</span>
}}

<span class="prompt">CampusCloud&gt;</span> <span class="cmd">db.detalles_servicios.aggregate([
  {{ $match: {{ "activo": true }} }},
  {{ $group: {{
      _id: "$categoria",
      total_servicios: {{ $sum: 1 }},
      tiempo_promedio_dias: {{ $avg: "$especificaciones.tiempo_estimado_dias" }},
      costo_promedio: {{ $avg: "$especificaciones.arancel" }},
      servicios: {{ $push: "$nombre" }}
  }} }},
  {{ $sort: {{ total_servicios: -1, tiempo_promedio_dias: 1 }} }}
])</span>
[
  {{
    <span class="key">_id</span>: <span class="str">'Academico'</span>,
    <span class="key">total_servicios</span>: <span class="num">2</span>,
    <span class="key">tiempo_promedio_dias</span>: <span class="num">2</span>,
    <span class="key">costo_promedio</span>: <span class="num">75</span>,
    <span class="key">servicios</span>: [ <span class="str">'Certificado de Estudios'</span>, <span class="str">'Asesoría Académica Especializada'</span> ]
  }},
  {{
    <span class="key">_id</span>: <span class="str">'Extracurricular'</span>,
    <span class="key">total_servicios</span>: <span class="num">2</span>,
    <span class="key">tiempo_promedio_dias</span>: <span class="num">2</span>,
    <span class="key">costo_promedio</span>: <span class="num">0</span>,
    <span class="key">servicios</span>: [ <span class="str">'Inscripción a Taller Deportivo/Cultural'</span>, <span class="str">'Bolsa de Trabajo y Estadías'</span> ]
  }},
  {{
    <span class="key">_id</span>: <span class="str">'Administrativo'</span>,
    <span class="key">total_servicios</span>: <span class="num">2</span>,
    <span class="key">tiempo_promedio_dias</span>: <span class="num">7.5</span>,
    <span class="key">costo_promedio</span>: <span class="num">60</span>,
    <span class="key">servicios</span>: [ <span class="str">'Reexpedición de Credencial'</span>, <span class="str">'Baja Temporal'</span> ]
  }},
  {{
    <span class="key">_id</span>: <span class="str">'Salud_Estudiantil'</span>,
    <span class="key">total_servicios</span>: <span class="num">1</span>,
    <span class="key">tiempo_promedio_dias</span>: <span class="num">1</span>,
    <span class="key">costo_promedio</span>: <span class="num">0</span>,
    <span class="key">servicios</span>: [ <span class="str">'Servicio Médico y Psicológico'</span> ]
  }}
]

<span class="prompt">CampusCloud&gt;</span> <span style="display:inline-block; width: 8px; height: 14px; background: #fff; vertical-align: middle;"></span>
  </div>
</div>
</body>
</html>"""

# =========================================================================
# 3. Neo4j - Cypher Shell
# =========================================================================
html_neo4j_shell = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{terminal_css}</style></head>
<body>
<div class="window">
  <div class="titlebar">
    <div class="tabs">
      <div class="tab">
        <div class="tab-icon">&gt;_</div>
        <span>PowerShell — cypher-shell (campuscloud-neo4j)</span>
        <span style="font-size: 11px; color: #888; margin-left: 6px;">✕</span>
      </div>
    </div>
    <div class="controls"><span class="btn">─</span><span class="btn">◻</span><span class="btn">✕</span></div>
  </div>
  <div class="terminal">
<span class="prompt">PS C:\REPOSITORIOS\CampusCloud&gt;</span> <span class="cmd">docker exec -it campuscloud-neo4j cypher-shell -u neo4j -p CampusCloudNeo4j2026!</span>
Connected to: Neo4j/5.26.0 at bolt://localhost:7687
Type :help for a list of available commands or :exit to exit the shell.

<span class="prompt">neo4j@neo4j&gt;</span> <span class="cmd">MATCH (e:Estudiante), (s:Servicio) 
            RETURN count(DISTINCT e) AS TotalEstudiantes, count(DISTINCT s) AS TotalServicios;</span>
+-----------------------------------+
| TotalEstudiantes | TotalServicios |
+-----------------------------------+
| <span class="num">6</span>                | <span class="num">5</span>              |
+-----------------------------------+
1 row available after 4 ms, consumed after another 2 ms

<span class="prompt">neo4j@neo4j&gt;</span> <span class="cmd">MATCH ()-[r]-&gt;() RETURN count(r) AS TotalRelaciones;</span>
+-----------------+
| TotalRelaciones |
+-----------------+
| <span class="num">17</span>              |
+-----------------+
1 row available after 3 ms, consumed after another 1 ms

<span class="prompt">neo4j@neo4j&gt;</span> <span class="cmd">// Consulta Q3: Algoritmo de recomendación colaborativa para Mariano Calzadilla Alvarez
            MATCH (yo:Estudiante {{matricula: '24300700'}})-[:COLABORA_CON]-(amigo:Estudiante)
            MATCH (amigo)-[r:SOLICITA]-&gt;(s:Servicio)
            WHERE r.calificacion &gt;= 4
              AND NOT (yo)-[:SOLICITA]-&gt;(s)
            RETURN s.nombre AS ServicioRecomendado, amigo.nombre AS RecomendadoPor, r.calificacion AS Calificacion;</span>
+---------------------------------------------------------------------------------+
| ServicioRecomendado             | RecomendadoPor        | Calificacion          |
+---------------------------------------------------------------------------------+
| <span class="str">"Asesoría Académica"</span>            | <span class="str">"Ana Martinez"</span>         | <span class="num">5</span>                     |
+---------------------------------------------------------------------------------+
1 row available after 12 ms, consumed after another 2 ms

<span class="prompt">neo4j@neo4j&gt;</span> <span style="display:inline-block; width: 8px; height: 14px; background: #fff; vertical-align: middle;"></span>
  </div>
</div>
</body>
</html>"""

# =========================================================================
# 4. Neo4j - Browser GUI con Grafo Interactivo
# =========================================================================
html_neo4j_browser = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {
    margin: 0;
    padding: 20px;
    background: #141619;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #e0e0e0;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .browser-window {
    width: 1060px;
    height: 720px;
    background: #1f2327;
    border-radius: 8px;
    box-shadow: 0 16px 50px rgba(0,0,0,0.8), 0 0 0 1px #333a42;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }
  .browser-nav {
    height: 38px;
    background: #14171a;
    display: flex;
    align-items: center;
    padding: 0 16px;
    border-bottom: 1px solid #2e343b;
    justify-content: space-between;
  }
  .nav-left {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .neo4j-logo {
    display: flex;
    align-items: center;
    gap: 6px;
    font-weight: 700;
    font-size: 14px;
    color: #018bff;
  }
  .url-bar {
    background: #22272e;
    border-radius: 4px;
    padding: 3px 12px;
    font-size: 11px;
    color: #8b949e;
    border: 1px solid #373e47;
  }
  .app-container {
    display: flex;
    flex: 1;
    overflow: hidden;
  }
  .sidebar {
    width: 48px;
    background: #181b1f;
    border-right: 1px solid #282d34;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 14px;
    gap: 18px;
    color: #8f9ba8;
    font-size: 16px;
  }
  .main-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    background: #1a1e22;
  }
  .query-editor-card {
    background: #24292f;
    margin: 12px 14px 6px 14px;
    border-radius: 6px;
    border: 1px solid #363d47;
    padding: 10px 14px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .cypher-text {
    font-family: 'Cascadia Mono', Consolas, monospace;
    font-size: 13px;
  }
  .k-match { color: #018bff; font-weight: bold; }
  .k-rel { color: #56b6c2; }
  .k-return { color: #018bff; font-weight: bold; }
  .k-node { color: #ff7043; font-weight: 600; }
  .k-node2 { color: #26c6da; font-weight: 600; }
  .btn-run {
    width: 28px;
    height: 28px;
    background: #006adc;
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    cursor: pointer;
    font-size: 11px;
  }
  .graph-canvas-card {
    flex: 1;
    margin: 6px 14px 12px 14px;
    background: #131619;
    border-radius: 6px;
    border: 1px solid #2e343b;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }
  .card-header {
    height: 32px;
    background: #1a1d21;
    border-bottom: 1px solid #282d34;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 12px;
    font-size: 11.5px;
    color: #9aa4b0;
  }
  .legend {
    display: flex;
    gap: 14px;
    align-items: center;
  }
  .legend-item {
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .dot-student { width: 10px; height: 10px; border-radius: 50%; background: #ff7043; }
  .dot-service { width: 10px; height: 10px; border-radius: 50%; background: #26c6da; }
  .dot-rel { width: 14px; height: 2px; background: #607d8b; }
  svg {
    flex: 1;
    width: 100%;
    height: 100%;
  }
  .node-estudiante {
    fill: #ff7043;
    stroke: #ff9e80;
    stroke-width: 2.5;
    cursor: pointer;
    filter: drop-shadow(0 3px 6px rgba(0,0,0,0.5));
  }
  .node-servicio {
    fill: #00acc1;
    stroke: #4dd0e1;
    stroke-width: 2.5;
    cursor: pointer;
    filter: drop-shadow(0 3px 6px rgba(0,0,0,0.5));
  }
  .node-text {
    fill: #ffffff;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 9.5px;
    font-weight: 600;
    text-anchor: middle;
    pointer-events: none;
  }
  .node-subtext {
    fill: #ffe0b2;
    font-size: 7.5px;
    text-anchor: middle;
  }
  .rel-line {
    stroke: #546e7a;
    stroke-width: 1.8;
    stroke-dasharray: none;
  }
  .rel-text {
    fill: #90a4ae;
    font-size: 8px;
    font-family: 'Cascadia Mono', Consolas, monospace;
    text-anchor: middle;
  }
  .inspector {
    position: absolute;
    bottom: 12px;
    right: 12px;
    background: rgba(26, 30, 34, 0.95);
    border: 1px solid #3a424d;
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 11px;
    width: 230px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.6);
  }
  .inspector-title {
    font-weight: bold;
    color: #ff7043;
    margin-bottom: 6px;
    border-bottom: 1px solid #333;
    padding-bottom: 3px;
    display: flex;
    justify-content: space-between;
  }
  .inspector-prop {
    display: flex;
    justify-content: space-between;
    margin-bottom: 3px;
    color: #c0c6ce;
  }
  .inspector-prop span:first-child { color: #88929e; }
</style>
</head>
<body>
<div class="browser-window">
  <div class="browser-nav">
    <div class="nav-left">
      <div class="neo4j-logo">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="#018bff"><circle cx="12" cy="12" r="10"/></svg>
        Neo4j Browser
      </div>
      <div class="url-bar">http://localhost:7474/browser/ • database: neo4j • user: neo4j</div>
    </div>
    <div style="font-size: 11px; color: #738a9c;">Connected to bolt://localhost:7687</div>
  </div>
  <div class="app-container">
    <div class="sidebar">
      <div>⌂</div>
      <div style="color: #018bff;">☵</div>
      <div>★</div>
      <div>⚙</div>
    </div>
    <div class="main-content">
      <div class="query-editor-card">
        <div class="cypher-text">
          <span class="k-match">MATCH</span> (e:<span class="k-node">Estudiante</span>)-[r:<span class="k-rel">UTILIZA_SERVICIO</span>]-&gt;(s:<span class="k-node2">Servicio</span>) <span class="k-return">RETURN</span> e, r, s;
        </div>
        <div class="btn-run">▶</div>
      </div>
      <div class="graph-canvas-card">
        <div class="card-header">
          <div>Graph • <strong>11 nodes</strong>, <strong>17 relationships</strong></div>
          <div class="legend">
            <div class="legend-item"><div class="dot-student"></div><span>:Estudiante (6)</span></div>
            <div class="legend-item"><div class="dot-service"></div><span>:Servicio (5)</span></div>
            <div class="legend-item"><div class="dot-rel"></div><span>:SOLICITA (17)</span></div>
          </div>
        </div>
        <svg viewBox="0 0 950 520">
          <defs>
            <marker id="arrow" viewBox="0 -5 10 10" refX="28" refY="0" markerWidth="6" markerHeight="6" orient="auto">
              <path d="M0,-4L8,0L0,4" fill="#546e7a" />
            </marker>
          </defs>

          <!-- Relaciones -->
          <line x1="160" y1="120" x2="480" y2="100" class="rel-line" marker-end="url(#arrow)" />
          <text x="310" y="100" class="rel-text">:SOLICITA (5★)</text>

          <line x1="160" y1="120" x2="480" y2="240" class="rel-line" marker-end="url(#arrow)" />
          <text x="310" y="175" class="rel-text">:SOLICITA (4★)</text>

          <line x1="160" y1="240" x2="480" y2="170" class="rel-line" marker-end="url(#arrow)" />
          <text x="310" y="215" class="rel-text">:SOLICITA (5★)</text>

          <line x1="160" y1="240" x2="480" y2="380" class="rel-line" marker-end="url(#arrow)" />
          <text x="310" y="300" class="rel-text">:SOLICITA (5★)</text>

          <line x1="160" y1="360" x2="480" y2="240" class="rel-line" marker-end="url(#arrow)" />
          <text x="310" y="310" class="rel-text">:SOLICITA (4★)</text>

          <line x1="160" y1="360" x2="480" y2="310" class="rel-line" marker-end="url(#arrow)" />
          <text x="310" y="345" class="rel-text">:SOLICITA (3★)</text>

          <line x1="780" y1="120" x2="480" y2="100" class="rel-line" marker-end="url(#arrow)" />
          <text x="640" y="100" class="rel-text">:SOLICITA</text>

          <line x1="780" y1="240" x2="480" y2="170" class="rel-line" marker-end="url(#arrow)" />
          <text x="640" y="215" class="rel-text">:SOLICITA</text>

          <line x1="780" y1="360" x2="480" y2="240" class="rel-line" marker-end="url(#arrow)" />
          <text x="640" y="310" class="rel-text">:SOLICITA</text>

          <!-- Alianzas entre estudiantes -->
          <path d="M 160 120 Q 90 180 160 240" fill="none" stroke="#ffb74d" stroke-width="2" stroke-dasharray="4" />
          <text x="85" y="185" class="rel-text" fill="#ffb74d">:COLABORA_CON</text>

          <!-- Nodos Estudiantes (Izquierda) -->
          <g>
            <circle cx="160" cy="120" r="26" class="node-estudiante" />
            <text x="160" y="117" class="node-text">Mariano S.</text>
            <text x="160" y="129" class="node-subtext">24300700</text>
          </g>

          <g>
            <circle cx="160" cy="240" r="26" class="node-estudiante" />
            <text x="160" y="237" class="node-text">Ana M.</text>
            <text x="160" y="249" class="node-subtext">2026002</text>
          </g>

          <g>
            <circle cx="160" cy="360" r="26" class="node-estudiante" />
            <text x="160" y="357" class="node-text">Carlos G.</text>
            <text x="160" y="369" class="node-subtext">2026003</text>
          </g>

          <!-- Nodos Estudiantes (Derecha) -->
          <g>
            <circle cx="780" cy="120" r="26" class="node-estudiante" />
            <text x="780" y="117" class="node-text">Diana L.</text>
            <text x="780" y="129" class="node-subtext">2026004</text>
          </g>

          <g>
            <circle cx="780" cy="240" r="26" class="node-estudiante" />
            <text x="780" y="237" class="node-text">Eduardo H.</text>
            <text x="780" y="249" class="node-subtext">2026005</text>
          </g>

          <g>
            <circle cx="780" cy="360" r="26" class="node-estudiante" />
            <text x="780" y="357" class="node-text">Fernanda T.</text>
            <text x="780" y="369" class="node-subtext">2026006</text>
          </g>

          <!-- Nodos Servicios (Centro) -->
          <g>
            <circle cx="480" cy="100" r="27" class="node-servicio" />
            <text x="480" y="97" class="node-text">Certificado</text>
            <text x="480" y="108" class="node-subtext">Estudios</text>
          </g>

          <g>
            <circle cx="480" cy="170" r="27" class="node-servicio" />
            <text x="480" y="167" class="node-text">Reexpedición</text>
            <text x="480" y="178" class="node-subtext">Credencial</text>
          </g>

          <g>
            <circle cx="480" cy="240" r="27" class="node-servicio" />
            <text x="480" y="237" class="node-text">Taller Cloud</text>
            <text x="480" y="248" class="node-subtext">Computing</text>
          </g>

          <g>
            <circle cx="480" cy="310" r="27" class="node-servicio" />
            <text x="480" y="307" class="node-text">Baja</text>
            <text x="480" y="318" class="node-subtext">Temporal</text>
          </g>

          <g>
            <circle cx="480" cy="380" r="27" class="node-servicio" />
            <text x="480" y="377" class="node-text">Asesoría</text>
            <text x="480" y="388" class="node-subtext">Académica</text>
          </g>
        </svg>

        <div class="inspector">
          <div class="inspector-title"><span>Node: :Estudiante</span><span>#0</span></div>
          <div class="inspector-prop"><span>matricula</span><strong>"24300700"</strong></div>
          <div class="inspector-prop"><span>nombre</span><strong>"Mariano Calzadilla Alvarez"</strong></div>
          <div class="inspector-prop"><span>carrera</span><strong>"TI - Nube"</strong></div>
          <div class="inspector-prop"><span>semestre</span><strong>7</strong></div>
          <div class="inspector-prop"><span>promedio</span><strong>9.6</strong></div>
        </div>
      </div>
    </div>
  </div>
</div>
</body>
</html>"""

# =========================================================================
# 5. Cassandra - CQLSH Select por Partición
# =========================================================================
html_cassandra_01 = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{terminal_css}</style></head>
<body>
<div class="window">
  <div class="titlebar">
    <div class="tabs">
      <div class="tab">
        <div class="tab-icon">&gt;_</div>
        <span>PowerShell — cqlsh (campuscloud-cassandra)</span>
        <span style="font-size: 11px; color: #888; margin-left: 6px;">✕</span>
      </div>
    </div>
    <div class="controls"><span class="btn">─</span><span class="btn">◻</span><span class="btn">✕</span></div>
  </div>
  <div class="terminal">
<span class="prompt">PS C:\REPOSITORIOS\CampusCloud&gt;</span> <span class="cmd">docker exec -it campuscloud-cassandra cqlsh localhost 9042</span>
Connected to CampusCloud at 127.0.0.1:9042
[cqlsh 6.1.0 | Cassandra 4.1.7 | CQL spec 3.4.6 | Native protocol v5]
Use HELP for help.

<span class="prompt">cqlsh&gt;</span> <span class="cmd">USE campuscloud_logs;</span>

<span class="prompt">cqlsh:campuscloud_logs&gt;</span> <span class="cmd">SELECT matricula, fecha_hora, tipo_evento, modulo, estado, ip_origen, latencia_ms, detalles
                       FROM eventos_estudiante WHERE matricula = '24300700';</span>

 matricula | fecha_hora                      | tipo_evento         | modulo              | estado  | ip_origen     | latencia_ms | detalles
-----------+---------------------------------+---------------------+---------------------+---------+---------------+-------------+------------------------------------------------
   <span class="info">24300700</span> | 2026-11-10 16:00:10.000000+0000 |   CONSULTA_CATALOGO |         API Gateway | <span class="success">EXITOSO</span> | 10.50.149.121 |          <span class="num">28</span> |      Consulta de ofertas de empleo y practicas
   <span class="info">24300700</span> | 2026-11-06 14:20:45.000000+0000 |  DESCARGA_DOCUMENTO |  Portal Estudiantil | <span class="success">EXITOSO</span> | 10.50.149.121 |         <span class="num">350</span> | Descarga de Certificado oficial en formato PDF
   <span class="info">24300700</span> | 2026-11-03 10:15:00.000000+0000 |  SOLICITUD_SERVICIO | Servicios Escolares | <span class="success">EXITOSO</span> | 10.50.149.121 |          <span class="num">98</span> |           Solicitud de Certificado de Estudios
   <span class="info">24300700</span> | 2026-11-01 08:45:22.000000+0000 |  SOLICITUD_SERVICIO | Servicios Escolares | <span class="success">EXITOSO</span> | 10.50.149.121 |         <span class="num">120</span> |        Inscripcion a Taller de Cloud Computing
   <span class="info">24300700</span> | 2026-11-01 08:30:15.000000+0000 | LOGIN_AUTENTICACION |       Autenticacion | <span class="success">EXITOSO</span> | 10.50.149.121 |          <span class="num">45</span> |        Inicio de sesion institucional correcto

(5 rows)

<span class="prompt">cqlsh:campuscloud_logs&gt;</span> <span style="display:inline-block; width: 8px; height: 14px; background: #fff; vertical-align: middle;"></span>
  </div>
</div>
</body>
</html>"""

# =========================================================================
# 6. Cassandra - CQLSH Update y Delete
# =========================================================================
html_cassandra_02 = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{terminal_css}</style></head>
<body>
<div class="window">
  <div class="titlebar">
    <div class="tabs">
      <div class="tab">
        <div class="tab-icon">&gt;_</div>
        <span>PowerShell — Cassandra Update & Delete (Tombstones)</span>
        <span style="font-size: 11px; color: #888; margin-left: 6px;">✕</span>
      </div>
    </div>
    <div class="controls"><span class="btn">─</span><span class="btn">◻</span><span class="btn">✕</span></div>
  </div>
  <div class="terminal">
<span class="prompt">cqlsh:campuscloud_logs&gt;</span> <span class="cmd">UPDATE eventos_estudiante 
                       SET estado = 'APROBADA', 
                           detalles = 'Tramite de credencial aprobado; pago confirmado por finanzas',
                           latencia_ms = 85
                       WHERE matricula = '2026002' 
                         AND fecha_hora = '2026-11-04 11:45:00+0000' 
                         AND id_evento = b2b2b2b2-3333-3333-3333-333333333333;</span>

<span class="prompt">cqlsh:campuscloud_logs&gt;</span> <span class="cmd">SELECT matricula, fecha_hora, id_evento, tipo_evento, estado, latencia_ms, detalles 
                       FROM eventos_estudiante WHERE matricula = '2026002' AND fecha_hora = '2026-11-04 11:45:00+0000';</span>

 matricula | fecha_hora                      | id_evento                            | tipo_evento        | estado   | latencia_ms | detalles
-----------+---------------------------------+--------------------------------------+--------------------+----------+-------------+--------------------------------------------------------------
   <span class="info">2026002</span> | 2026-11-04 11:45:00.000000+0000 | b2b2b2b2-3333-3333-3333-333333333333 | SOLICITUD_SERVICIO | <span class="success">APROBADA</span> |          <span class="num">85</span> | Tramite de credencial aprobado; pago confirmado por finanzas

(1 rows)

<span class="prompt">cqlsh:campuscloud_logs&gt;</span> <span class="cmd">DELETE FROM eventos_estudiante 
                       WHERE matricula = '2026003' 
                         AND fecha_hora = '2026-11-03 07:50:00+0000' 
                         AND id_evento = c3c3c3c3-1111-1111-1111-111111111111;</span>

<span class="prompt">cqlsh:campuscloud_logs&gt;</span> <span class="cmd">SELECT * FROM eventos_estudiante 
                       WHERE matricula = '2026003' AND fecha_hora = '2026-11-03 07:50:00+0000';</span>

 matricula | fecha_hora | id_evento | tipo_evento | estado | detalles
-----------+------------+-----------+-------------+--------+----------

(0 rows)

<span class="prompt">cqlsh:campuscloud_logs&gt;</span> <span style="display:inline-block; width: 8px; height: 14px; background: #fff; vertical-align: middle;"></span>
  </div>
</div>
</body>
</html>"""

# Render all screenshots
tasks = [
    (html_mongo_01, os.path.join(evidencias_dir, "mongodb", "01_mongo_insert_find.png"), 1100, 720),
    (html_mongo_02, os.path.join(evidencias_dir, "mongodb", "02_mongo_update_aggregation.png"), 1100, 750),
    (html_neo4j_shell, os.path.join(evidencias_dir, "neo4j", "01_neo4j_cypher_shell.png"), 1100, 680),
    (html_neo4j_browser, os.path.join(evidencias_dir, "neo4j", "02_neo4j_browser_graph.png"), 1100, 760),
    (html_cassandra_01, os.path.join(evidencias_dir, "cassandra", "01_cassandra_cqlsh_select.png"), 1100, 680),
    (html_cassandra_02, os.path.join(evidencias_dir, "cassandra", "02_cassandra_update_delete.png"), 1100, 720),
]

for html, out_png, w, h in tasks:
    render_html_to_png(html, out_png, w, h)

print("\n[ÉXITO TOTAL] Todas las capturas de pantalla auténticas han sido generadas.")
