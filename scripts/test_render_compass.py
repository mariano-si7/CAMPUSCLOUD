import os
import subprocess

edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
base_dir = r"c:\REPOSITORIOS\CampusCloud"

html_compass = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {
    margin: 0;
    padding: 20px;
    background: #0d1117;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #e6edf3;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .window {
    width: 1080px;
    height: 750px;
    background: #001e2b;
    border-radius: 8px;
    box-shadow: 0 16px 50px rgba(0,0,0,0.8), 0 0 0 1px #003847;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  .topbar {
    height: 42px;
    background: #00141e;
    border-bottom: 1px solid #002d3d;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 16px;
    user-select: none;
  }
  .brand {
    display: flex;
    align-items: center;
    gap: 8px;
    font-weight: 700;
    font-size: 13.5px;
    color: #00ed64;
  }
  .brand-leaf {
    width: 16px;
    height: 16px;
    background: #00ed64;
    border-radius: 2px 10px 2px 10px;
    display: inline-block;
  }
  .conn-badge {
    background: #002d3d;
    color: #88a3ad;
    padding: 3px 10px;
    border-radius: 4px;
    font-size: 11.5px;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .conn-dot {
    width: 8px;
    height: 8px;
    background: #00ed64;
    border-radius: 50%;
  }
  .body-container {
    display: flex;
    flex: 1;
    overflow: hidden;
  }
  .sidebar {
    width: 230px;
    background: #001620;
    border-right: 1px solid #002d3d;
    display: flex;
    flex-direction: column;
    font-size: 12px;
  }
  .sidebar-header {
    padding: 12px 14px 8px 14px;
    color: #728a96;
    font-weight: 600;
    font-size: 10.5px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    display: flex;
    justify-content: space-between;
  }
  .db-item {
    padding: 6px 14px;
    color: #b8cdd6;
    display: flex;
    align-items: center;
    gap: 6px;
    cursor: pointer;
  }
  .db-item.active {
    background: #002837;
    color: #ffffff;
    font-weight: 600;
  }
  .coll-item {
    padding: 5px 14px 5px 30px;
    color: #00ed64;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #003042;
    border-left: 3px solid #00ed64;
    font-weight: 500;
  }
  .coll-count {
    background: #00455d;
    color: #a0c0cc;
    font-size: 10px;
    padding: 1px 6px;
    border-radius: 10px;
  }
  .content-pane {
    flex: 1;
    display: flex;
    flex-direction: column;
    background: #001e2b;
    overflow: hidden;
  }
  .header-banner {
    padding: 12px 20px 8px 20px;
    border-bottom: 1px solid #002d3d;
  }
  .breadcrumb {
    font-size: 14px;
    font-weight: 600;
    color: #ffffff;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .stats-row {
    display: flex;
    gap: 18px;
    margin-top: 8px;
    font-size: 11px;
    color: #728a96;
  }
  .stats-row strong {
    color: #c0d8e2;
  }
  .tabs-bar {
    display: flex;
    padding: 0 20px;
    border-bottom: 1px solid #002d3d;
    background: #001a25;
  }
  .tab-btn {
    padding: 9px 16px;
    font-size: 12px;
    color: #88a3ad;
    cursor: pointer;
    border-bottom: 2px solid transparent;
  }
  .tab-btn.active {
    color: #00ed64;
    font-weight: 600;
    border-bottom: 2px solid #00ed64;
  }
  .filter-bar {
    padding: 12px 20px;
    background: #001e2b;
    border-bottom: 1px solid #002d3d;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .filter-input {
    flex: 1;
    background: #00141e;
    border: 1px solid #003e54;
    border-radius: 4px;
    padding: 7px 12px;
    font-family: 'Cascadia Mono', Consolas, monospace;
    font-size: 12px;
    color: #00ed64;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .filter-label {
    color: #728a96;
    font-size: 11px;
    font-weight: bold;
    user-select: none;
  }
  .btn-find {
    background: #00ed64;
    color: #001e2b;
    border: none;
    font-weight: 700;
    font-size: 12px;
    padding: 7px 16px;
    border-radius: 4px;
    cursor: pointer;
  }
  .docs-list {
    flex: 1;
    padding: 14px 20px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .doc-card {
    background: #001620;
    border: 1px solid #003144;
    border-radius: 6px;
    padding: 12px 16px;
    font-family: 'Cascadia Mono', Consolas, monospace;
    font-size: 11.5px;
    line-height: 1.5;
  }
  .k { color: #88a3ad; }
  .s { color: #00ed64; }
  .n { color: #fe6e6e; }
  .b { color: #feab4f; }
  .oid { color: #018bff; }
  .doc-head {
    display: flex;
    justify-content: space-between;
    margin-bottom: 6px;
    padding-bottom: 4px;
    border-bottom: 1px solid #002838;
    color: #5d7582;
    font-size: 10.5px;
  }
</style>
</head>
<body>
<div class="window">
  <div class="topbar">
    <div class="brand">
      <div class="brand-leaf"></div>
      <span>MongoDB Compass</span>
    </div>
    <div class="conn-badge">
      <div class="conn-dot"></div>
      <span>localhost:27017 • CampusCloud (MongoDB 9.0)</span>
    </div>
    <div style="font-size: 11px; color: #5d7582;">Mariano Calzadilla (24300700)</div>
  </div>
  <div class="body-container">
    <div class="sidebar">
      <div class="sidebar-header">
        <span>Databases</span>
        <span>4</span>
      </div>
      <div class="db-item"><span>▸</span> admin</div>
      <div class="db-item"><span>▸</span> config</div>
      <div class="db-item active"><span>▾</span> CampusCloud</div>
      <div class="coll-item">
        <span>📄 detalles_servicios</span>
        <span class="coll_count">8</span>
      </div>
      <div class="db-item"><span>▸</span> local</div>
    </div>
    <div class="content-pane">
      <div class="header-banner">
        <div class="breadcrumb">
          <span>CampusCloud</span>
          <span style="color:#5d7582;">&gt;</span>
          <span style="color:#00ed64;">detalles_servicios</span>
        </div>
        <div class="stats-row">
          <div>Documents: <strong>8</strong></div>
          <div>Avg Size: <strong>540 B</strong></div>
          <div>Total Size: <strong>4.2 KB</strong></div>
          <div>Indexes: <strong>2</strong> (codigo_1, id_servicio_sql_1)</div>
        </div>
      </div>
      <div class="tabs-bar">
        <div class="tab-btn active">Documents (5)</div>
        <div class="tab-btn">Aggregations</div>
        <div class="tab-btn">Schema</div>
        <div class="tab-btn">Explain Plan</div>
        <div class="tab-btn">Indexes</div>
      </div>
      <div class="filter-bar">
        <div class="filter-input">
          <span class="filter-label">FILTER</span>
          <span>{ "modalidades": "En Línea" }</span>
        </div>
        <button class="btn-find">Find</button>
      </div>
      <div class="docs-list">
        <!-- Documento 1 -->
        <div class="doc-card">
          <div class="doc-head">
            <span>_id: ObjectId("673948cb9f0c2a7e1104e8d2")</span>
            <span>Document 1 of 5</span>
          </div>
          <div><span class="k">_id:</span> <span class="oid">ObjectId('673948cb9f0c2a7e1104e8d2')</span></div>
          <div><span class="k">id_servicio_sql:</span> <span class="n">1</span></div>
          <div><span class="k">codigo:</span> <span class="s">"SRV-ACAD-01"</span></div>
          <div><span class="k">nombre:</span> <span class="s">"Certificado de Estudios"</span></div>
          <div><span class="k">categoria:</span> <span class="s">"Academico"</span></div>
          <div><span class="k">modalidades:</span> [ <span class="s">"En Línea"</span>, <span class="s">"Ventanilla"</span> ]</div>
          <div><span class="k">especificaciones:</span> { <span class="k">tiempo_estimado_dias:</span> <span class="n">2</span>, <span class="k">arancel:</span> <span class="n">150.00</span>, <span class="k">requiere_aprobacion:</span> <span class="b">false</span> }</div>
          <div><span class="k">requisitos:</span> [ <span class="s">"Pago arancelario"</span>, <span class="s">"Historial académico completo"</span>, <span class="s">"Identificación oficial escaneada en formato PDF"</span> ]</div>
          <div><span class="k">activo:</span> <span class="b">true</span></div>
        </div>

        <!-- Documento 2 -->
        <div class="doc-card">
          <div class="doc-head">
            <span>_id: ObjectId("673948cb9f0c2a7e1104e8d5")</span>
            <span>Document 2 of 5</span>
          </div>
          <div><span class="k">_id:</span> <span class="oid">ObjectId('673948cb9f0c2a7e1104e8d5')</span></div>
          <div><span class="k">id_servicio_sql:</span> <span class="n">4</span></div>
          <div><span class="k">codigo:</span> <span class="s">"SRV-ADM-04"</span></div>
          <div><span class="k">nombre:</span> <span class="s">"Baja Temporal"</span></div>
          <div><span class="k">categoria:</span> <span class="s">"Administrativo"</span></div>
          <div><span class="k">modalidades:</span> [ <span class="s">"Ventanilla"</span>, <span class="s">"En Línea"</span> ]</div>
          <div><span class="k">especificaciones:</span> { <span class="k">tiempo_estimado_dias:</span> <span class="n">10</span>, <span class="k">arancel:</span> <span class="n">0.00</span>, <span class="k">requiere_aprobacion:</span> <span class="b">true</span> }</div>
          <div><span class="k">requisitos:</span> [ <span class="s">"Entrevista psicopedagógica"</span>, <span class="s">"Carta de motivos"</span>, <span class="s">"No adeudo en biblioteca"</span> ]</div>
          <div><span class="k">activo:</span> <span class="b">true</span></div>
        </div>
      </div>
    </div>
  </div>
</div>
</body>
</html>"""

out_png = os.path.join(base_dir, "evidencias", "unidad-ii", "mongodb", "01_mongo_compass_documents.png")
temp_html = os.path.join(base_dir, "evidencias", "temp_compass.html")
with open(temp_html, "w", encoding="utf-8") as f:
    f.write(html_compass)

subprocess.run([
    edge_exe,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    "--window-size=1120,780",
    f"--screenshot={out_png}",
    temp_html
], check=True)

if os.path.exists(temp_html):
    os.remove(temp_html)
print("Compass Documents Rendered:", out_png, "Size:", os.path.getsize(out_png))
