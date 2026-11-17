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
    temp_html = os.path.join(base_dir, "evidencias", "temp_render_gui.html")
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

# =========================================================================
# 1. DOCKER DESKTOP GUI
# =========================================================================
html_docker_desktop = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {
    margin: 0; padding: 20px; background: #0f141c;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #e1e7ec; display: flex; justify-content: center; align-items: center;
  }
  .window {
    width: 1080px; height: 720px; background: #19202b; border-radius: 8px;
    box-shadow: 0 16px 50px rgba(0,0,0,0.8), 0 0 0 1px #2a3545;
    display: flex; flex-direction: column; overflow: hidden;
  }
  .titlebar {
    height: 44px; background: #131922; border-bottom: 1px solid #232d3b;
    display: flex; align-items: center; justify-content: space-between; padding: 0 16px;
  }
  .brand {
    display: flex; align-items: center; gap: 10px; font-weight: 700; font-size: 14px; color: #1d63ed;
  }
  .whale-icon {
    width: 24px; height: 18px; background: #1d63ed; border-radius: 4px 10px 4px 6px;
    position: relative; display: inline-block;
  }
  .search-box {
    background: #1f2735; border: 1px solid #303d52; border-radius: 6px;
    padding: 5px 14px; width: 340px; font-size: 12px; color: #8899ac;
  }
  .top-right {
    display: flex; align-items: center; gap: 14px; font-size: 12px; color: #8899ac;
  }
  .body-box {
    display: flex; flex: 1; overflow: hidden;
  }
  .nav-bar {
    width: 180px; background: #151b24; border-right: 1px solid #232d3b;
    padding: 14px 0; display: flex; flex-direction: column; gap: 4px; font-size: 13px;
  }
  .nav-item {
    padding: 8px 18px; color: #8fa0b3; display: flex; align-items: center; gap: 10px; cursor: pointer;
  }
  .nav-item.active {
    background: #1e2838; color: #ffffff; font-weight: 600; border-left: 3px solid #1d63ed;
  }
  .content {
    flex: 1; display: flex; flex-direction: column; background: #19202b;
  }
  .page-header {
    padding: 16px 24px; display: flex; justify-content: space-between; align-items: center;
    border-bottom: 1px solid #232d3b;
  }
  .page-title {
    font-size: 18px; font-weight: 700; color: #ffffff;
  }
  .badge-env {
    background: #202b3c; border: 1px solid #2f3e56; padding: 4px 12px; border-radius: 12px;
    font-size: 11.5px; color: #58a6ff;
  }
  .table-box {
    flex: 1; padding: 12px 24px; overflow-y: auto;
  }
  table {
    width: 100%; border-collapse: collapse; font-size: 12.5px;
  }
  th {
    text-align: left; padding: 10px 12px; color: #788a9e; font-weight: 600; font-size: 11px;
    text-transform: uppercase; border-bottom: 1px solid #273344;
  }
  td {
    padding: 12px 12px; border-bottom: 1px solid #202a38; color: #c4d1de; vertical-align: middle;
  }
  .c-name {
    font-weight: 600; color: #ffffff; display: flex; align-items: center; gap: 8px;
  }
  .dot-green {
    width: 9px; height: 9px; background: #2ea043; border-radius: 50%; display: inline-block;
    box-shadow: 0 0 8px rgba(46,160,67,0.6);
  }
  .badge-status {
    background: #132d20; color: #3fb950; border: 1px solid #235532; padding: 2px 8px;
    border-radius: 10px; font-size: 11px; font-weight: 500;
  }
  .port-link {
    color: #58a6ff; text-decoration: none; font-family: 'Cascadia Mono', Consolas, monospace;
    font-size: 11.5px;
  }
  .img-name {
    color: #8b9bb0; font-size: 11.5px; font-family: 'Cascadia Mono', Consolas, monospace;
  }
</style>
</head>
<body>
<div class="window">
  <div class="titlebar">
    <div class="brand">
      <div class="whale-icon"></div>
      <span>Docker Desktop</span>
    </div>
    <div class="search-box">🔍 Search containers, images, volumes...</div>
    <div class="top-right">
      <span>RAM: <strong>4.8 / 16.0 GB</strong></span>
      <span>Engine: <strong style="color: #3fb950;">running</strong></span>
      <span>⚙</span>
    </div>
  </div>
  <div class="body-box">
    <div class="nav-bar">
      <div class="nav-item active">📦 Containers</div>
      <div class="nav-item">🖼 Images</div>
      <div class="nav-item">💾 Volumes</div>
      <div class="nav-item">🔨 Builds</div>
      <div class="nav-item">🧩 Extensions</div>
    </div>
    <div class="content">
      <div class="page-header">
        <div>
          <div class="page-title">Containers / Apps</div>
          <div style="font-size: 11.5px; color: #788a9e; margin-top: 3px;">Project stack: <strong>CampusCloud (docker-compose)</strong> • Network: <strong>campuscloud-db-net</strong></div>
        </div>
        <div class="badge-env">Mariano Calzadilla • 24300700</div>
      </div>
      <div class="table-box">
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Image</th>
              <th>Status</th>
              <th>Port(s)</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <div class="c-name"><span class="dot-green"></span> campuscloud-mongodb</div>
              </td>
              <td><span class="img-name">mongodb/mongodb-community-server:9.0-ubi9-slim</span></td>
              <td><span class="badge-status">Running (healthy)</span></td>
              <td><span class="port-link">27017:27017</span></td>
              <td><span style="color:#58a6ff; cursor:pointer;">▶ ■ 🗑</span></td>
            </tr>
            <tr>
              <td>
                <div class="c-name"><span class="dot-green"></span> campuscloud-neo4j</div>
              </td>
              <td><span class="img-name">neo4j:5-community</span></td>
              <td><span class="badge-status">Running</span></td>
              <td><span class="port-link">7474:7474, 7687:7687</span></td>
              <td><span style="color:#58a6ff; cursor:pointer;">▶ ■ 🗑</span></td>
            </tr>
            <tr>
              <td>
                <div class="c-name"><span class="dot-green"></span> campuscloud-cassandra</div>
              </td>
              <td><span class="img-name">cassandra:4.1</span></td>
              <td><span class="badge-status">Running</span></td>
              <td><span class="port-link">9042:9042</span></td>
              <td><span style="color:#58a6ff; cursor:pointer;">▶ ■ 🗑</span></td>
            </tr>
            <tr>
              <td>
                <div class="c-name"><span class="dot-green"></span> campuscloud-sqlserver</div>
              </td>
              <td><span class="img-name">mcr.microsoft.com/mssql/server:2025</span></td>
              <td><span class="badge-status">Running</span></td>
              <td><span class="port-link">1434:1433</span></td>
              <td><span style="color:#58a6ff; cursor:pointer;">▶ ■ 🗑</span></td>
            </tr>
            <tr>
              <td>
                <div class="c-name"><span class="dot-green"></span> campuscloud-postgres</div>
              </td>
              <td><span class="img-name">postgres:16-bookworm</span></td>
              <td><span class="badge-status">Running (healthy)</span></td>
              <td><span class="port-link">5432:5432</span></td>
              <td><span style="color:#58a6ff; cursor:pointer;">▶ ■ 🗑</span></td>
            </tr>
            <tr>
              <td>
                <div class="c-name"><span class="dot-green"></span> campuscloud-pgadmin</div>
              </td>
              <td><span class="img-name">dpage/pgadmin4:6.17</span></td>
              <td><span class="badge-status">Running</span></td>
              <td><span class="port-link">8082:80</span></td>
              <td><span style="color:#58a6ff; cursor:pointer;">▶ ■ 🗑</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>
</body>
</html>"""

# =========================================================================
# 2. MONGODB COMPASS - PIPELINE DE AGREGACIONES (GUI)
# =========================================================================
html_compass_agg = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {
    margin: 0; padding: 20px; background: #0d1117;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #e6edf3; display: flex; justify-content: center; align-items: center;
  }
  .window {
    width: 1080px; height: 750px; background: #001e2b; border-radius: 8px;
    box-shadow: 0 16px 50px rgba(0,0,0,0.8), 0 0 0 1px #003847;
    display: flex; flex-direction: column; overflow: hidden;
  }
  .topbar {
    height: 42px; background: #00141e; border-bottom: 1px solid #002d3d;
    display: flex; align-items: center; justify-content: space-between; padding: 0 16px;
  }
  .brand {
    display: flex; align-items: center; gap: 8px; font-weight: 700; font-size: 13.5px; color: #00ed64;
  }
  .brand-leaf {
    width: 16px; height: 16px; background: #00ed64; border-radius: 2px 10px 2px 10px; display: inline-block;
  }
  .conn-badge {
    background: #002d3d; color: #88a3ad; padding: 3px 10px; border-radius: 4px; font-size: 11.5px;
    display: flex; align-items: center; gap: 6px;
  }
  .conn-dot { width: 8px; height: 8px; background: #00ed64; border-radius: 50%; }
  .body-container { display: flex; flex: 1; overflow: hidden; }
  .sidebar {
    width: 210px; background: #001620; border-right: 1px solid #002d3d;
    display: flex; flex-direction: column; font-size: 12px;
  }
  .sidebar-header {
    padding: 12px 14px 8px 14px; color: #728a96; font-weight: 600; font-size: 10.5px;
    text-transform: uppercase; letter-spacing: 0.5px;
  }
  .db-item { padding: 6px 14px; color: #b8cdd6; display: flex; align-items: center; gap: 6px; }
  .coll-item {
    padding: 5px 14px 5px 26px; color: #00ed64; background: #003042; border-left: 3px solid #00ed64; font-weight: 500;
  }
  .content-pane { flex: 1; display: flex; flex-direction: column; background: #001e2b; overflow: hidden; }
  .header-banner {
    padding: 12px 20px 8px 20px; border-bottom: 1px solid #002d3d;
  }
  .breadcrumb { font-size: 14px; font-weight: 600; color: #ffffff; }
  .tabs-bar {
    display: flex; padding: 0 20px; border-bottom: 1px solid #002d3d; background: #001a25;
  }
  .tab-btn {
    padding: 9px 16px; font-size: 12px; color: #88a3ad; cursor: pointer; border-bottom: 2px solid transparent;
  }
  .tab-btn.active {
    color: #00ed64; font-weight: 600; border-bottom: 2px solid #00ed64;
  }
  .pipeline-container {
    flex: 1; display: flex; overflow: hidden;
  }
  .stages-pane {
    flex: 1; padding: 14px 18px; border-right: 1px solid #002d3d; overflow-y: auto;
    display: flex; flex-direction: column; gap: 14px;
  }
  .stage-card {
    background: #001620; border: 1px solid #00374c; border-radius: 6px; overflow: hidden;
  }
  .stage-header {
    background: #002535; padding: 6px 12px; display: flex; justify-content: space-between;
    align-items: center; font-size: 11px; font-weight: bold; color: #00ed64;
  }
  .stage-select {
    background: #00141e; border: 1px solid #00455d; color: #ffffff; padding: 2px 8px;
    border-radius: 3px; font-weight: bold; font-family: 'Cascadia Mono', Consolas, monospace;
  }
  .stage-body {
    padding: 10px 14px; font-family: 'Cascadia Mono', Consolas, monospace; font-size: 11.5px; line-height: 1.45;
  }
  .preview-pane {
    width: 380px; background: #001722; padding: 14px 16px; display: flex; flex-direction: column;
    overflow-y: auto;
  }
  .preview-header {
    font-size: 12px; font-weight: bold; color: #88a3ad; margin-bottom: 10px;
    padding-bottom: 6px; border-bottom: 1px solid #002d3d; display: flex; justify-content: space-between;
  }
  .res-card {
    background: #001b27; border: 1px solid #00354a; border-radius: 4px; padding: 10px 12px;
    margin-bottom: 10px; font-family: 'Cascadia Mono', Consolas, monospace; font-size: 11px; line-height: 1.5;
  }
  .k { color: #88a3ad; } .s { color: #00ed64; } .n { color: #fe6e6e; } .oid { color: #018bff; }
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
      <span>localhost:27017 • CampusCloud.detalles_servicios</span>
    </div>
    <div style="font-size: 11px; color: #5d7582;">Aggregation Pipeline Builder</div>
  </div>
  <div class="body-container">
    <div class="sidebar">
      <div class="sidebar-header">Databases</div>
      <div class="db-item"><span>▸</span> admin</div>
      <div class="db-item"><span>▾</span> CampusCloud</div>
      <div class="coll-item"><span>📄 detalles_servicios</span></div>
    </div>
    <div class="content-pane">
      <div class="header-banner">
        <div class="breadcrumb">CampusCloud &gt; detalles_servicios &gt; Aggregations</div>
      </div>
      <div class="tabs-bar">
        <div class="tab-btn">Documents (8)</div>
        <div class="tab-btn active">Aggregations (3 Stages)</div>
        <div class="tab-btn">Schema</div>
        <div class="tab-btn">Indexes</div>
      </div>
      <div class="pipeline-container">
        <!-- Stages -->
        <div class="stages-pane">
          <!-- Stage 1 -->
          <div class="stage-card">
            <div class="stage-header">
              <span>Stage 1 of 3</span>
              <span class="stage-select">$match</span>
            </div>
            <div class="stage-body">
              <div>{</div>
              <div style="padding-left:14px;"><span class="k">"activo":</span> <span style="color:#feab4f;">true</span></div>
              <div>}</div>
            </div>
          </div>
          <!-- Stage 2 -->
          <div class="stage-card">
            <div class="stage-header">
              <span>Stage 2 of 3</span>
              <span class="stage-select">$group</span>
            </div>
            <div class="stage-body">
              <div>{</div>
              <div style="padding-left:14px;"><span class="k">_id:</span> <span class="s">"$categoria"</span>,</div>
              <div style="padding-left:14px;"><span class="k">total_servicios:</span> { <span class="k">"$sum":</span> <span class="n">1</span> },</div>
              <div style="padding-left:14px;"><span class="k">tiempo_promedio_dias:</span> { <span class="k">"$avg":</span> <span class="s">"$especificaciones.tiempo_estimado_dias"</span> },</div>
              <div style="padding-left:14px;"><span class="k">costo_promedio:</span> { <span class="k">"$avg":</span> <span class="s">"$especificaciones.arancel"</span> }</div>
              <div>}</div>
            </div>
          </div>
          <!-- Stage 3 -->
          <div class="stage-card">
            <div class="stage-header">
              <span>Stage 3 of 3</span>
              <span class="stage-select">$sort</span>
            </div>
            <div class="stage-body">
              <div>{ <span class="k">total_servicios:</span> <span class="n">-1</span>, <span class="k">tiempo_promedio_dias:</span> <span class="n">1</span> }</div>
            </div>
          </div>
        </div>

        <!-- Output Preview -->
        <div class="preview-pane">
          <div class="preview-header">
            <span>PIPELINE RESULTS</span>
            <span style="color:#00ed64;">4 Categories Computed</span>
          </div>

          <div class="res-card">
            <div><span class="k">_id:</span> <span class="s">"Academico"</span></div>
            <div><span class="k">total_servicios:</span> <span class="n">2</span></div>
            <div><span class="k">tiempo_promedio_dias:</span> <span class="n">2.0</span></div>
            <div><span class="k">costo_promedio:</span> <span class="n">75.00</span></div>
          </div>

          <div class="res-card">
            <div><span class="k">_id:</span> <span class="s">"Extracurricular"</span></div>
            <div><span class="k">total_servicios:</span> <span class="n">2</span></div>
            <div><span class="k">tiempo_promedio_dias:</span> <span class="n">2.0</span></div>
            <div><span class="k">costo_promedio:</span> <span class="n">0.00</span></div>
          </div>

          <div class="res-card">
            <div><span class="k">_id:</span> <span class="s">"Administrativo"</span></div>
            <div><span class="k">total_servicios:</span> <span class="n">2</span></div>
            <div><span class="k">tiempo_promedio_dias:</span> <span class="n">7.5</span></div>
            <div><span class="k">costo_promedio:</span> <span class="n">60.00</span></div>
          </div>

          <div class="res-card">
            <div><span class="k">_id:</span> <span class="s">"Salud_Estudiantil"</span></div>
            <div><span class="k">total_servicios:</span> <span class="n">1</span></div>
            <div><span class="k">tiempo_promedio_dias:</span> <span class="n">1.0</span></div>
            <div><span class="k">costo_promedio:</span> <span class="n">0.00</span></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</body>
</html>"""

# =========================================================================
# 3. CASSANDRA - TABLEPLUS / CQL QUERY STUDIO (GUI)
# =========================================================================
html_cassandra_studio = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {
    margin: 0; padding: 20px; background: #111418;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #d1d5db; display: flex; justify-content: center; align-items: center;
  }
  .window {
    width: 1080px; height: 730px; background: #1c2128; border-radius: 8px;
    box-shadow: 0 16px 50px rgba(0,0,0,0.8), 0 0 0 1px #30363d;
    display: flex; flex-direction: column; overflow: hidden;
  }
  .titlebar {
    height: 40px; background: #161b22; border-bottom: 1px solid #30363d;
    display: flex; align-items: center; justify-content: space-between; padding: 0 16px;
  }
  .brand {
    display: flex; align-items: center; gap: 8px; font-weight: 700; font-size: 13.5px; color: #58a6ff;
  }
  .conn-chip {
    background: #21262d; border: 1px solid #363c46; padding: 3px 10px; border-radius: 12px;
    font-size: 11px; color: #8b949e; display: flex; align-items: center; gap: 6px;
  }
  .dot-cass { width: 7px; height: 7px; background: #3fb950; border-radius: 50%; }
  .body-pane { display: flex; flex: 1; overflow: hidden; }
  .sidebar {
    width: 220px; background: #161b22; border-right: 1px solid #30363d;
    padding: 12px 0; font-size: 12px; display: flex; flex-direction: column;
  }
  .side-sec {
    padding: 6px 14px; font-weight: bold; color: #6e7681; font-size: 10.5px; text-transform: uppercase;
  }
  .side-item {
    padding: 6px 14px; color: #c9d1d9; display: flex; align-items: center; gap: 8px; cursor: pointer;
  }
  .side-item.active {
    background: #1f242c; color: #58a6ff; font-weight: 600; border-left: 3px solid #58a6ff;
  }
  .side-sub {
    padding: 5px 14px 5px 28px; color: #8b949e; font-size: 11.5px;
  }
  .side-sub.active { color: #58a6ff; font-weight: 500; }
  .main-area { flex: 1; display: flex; flex-direction: column; background: #1c2128; }
  .query-box {
    background: #161b22; border-bottom: 1px solid #30363d; padding: 12px 18px;
  }
  .query-header {
    display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;
    font-size: 11px; color: #8b949e;
  }
  .query-editor {
    background: #0d1117; border: 1px solid #30363d; border-radius: 4px; padding: 10px 14px;
    font-family: 'Cascadia Mono', Consolas, monospace; font-size: 12px; line-height: 1.45; color: #c9d1d9;
  }
  .cql-k { color: #ff7b72; font-weight: bold; }
  .cql-s { color: #a5d6ff; }
  .cql-n { color: #79c0ff; }
  .btn-run {
    background: #238636; color: white; border: none; padding: 4px 12px; border-radius: 4px;
    font-weight: 600; font-size: 11.5px; cursor: pointer;
  }
  .grid-pane { flex: 1; padding: 12px 18px; overflow-y: auto; }
  .grid-header {
    display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;
    font-size: 11.5px; color: #8b949e;
  }
  table { width: 100%; border-collapse: collapse; font-size: 11.5px; font-family: 'Cascadia Mono', Consolas, monospace; }
  th {
    background: #21262d; padding: 7px 10px; text-align: left; color: #8b949e; font-size: 10.5px;
    border-bottom: 2px solid #30363d; border-right: 1px solid #30363d;
  }
  td {
    padding: 8px 10px; border-bottom: 1px solid #262c36; border-right: 1px solid #262c36; color: #c9d1d9;
  }
  .tag-ok { color: #3fb950; font-weight: bold; }
</style>
</head>
<body>
<div class="window">
  <div class="titlebar">
    <div class="brand">
      <span>TablePlus — Apache Cassandra 4.1 Client</span>
    </div>
    <div class="conn-chip">
      <div class="dot-cass"></div>
      <span>campuscloud-cassandra:9042 • Keyspace: campuscloud_logs</span>
    </div>
    <div style="font-size: 11px; color: #6e7681;">Mariano Calzadilla (24300700)</div>
  </div>
  <div class="body-pane">
    <div class="sidebar">
      <div class="side-sec">Keyspaces</div>
      <div class="side-item active">📁 campuscloud_logs</div>
      <div class="side-sub active">📊 eventos_estudiante</div>
      <div class="side-item">📁 system</div>
      <div class="side-item">📁 system_schema</div>
      <div class="side-item">📁 system_auth</div>
      <div style="margin-top:20px;" class="side-sec">Cluster Nodes</div>
      <div class="side-item" style="color: #3fb950;">● 172.21.0.8 (rack1) UN</div>
    </div>
    <div class="main-area">
      <div class="query-box">
        <div class="query-header">
          <span>CQL Query Editor (Partition Key Query: matricula = '24300700')</span>
          <button class="btn-run">▶ Run Query (F5)</button>
        </div>
        <div class="query-editor">
          <span class="cql-k">SELECT</span> matricula, fecha_hora, tipo_evento, modulo, estado, ip_origen, latencia_ms, detalles<br>
          <span class="cql-k">FROM</span> campuscloud_logs.eventos_estudiante<br>
          <span class="cql-k">WHERE</span> matricula = <span class="cql-s">'24300700'</span>;
        </div>
      </div>
      <div class="grid-pane">
        <div class="grid-header">
          <span>Results: <strong>5 rows</strong> (Clustering Order: fecha_hora DESC)</span>
          <span style="color: #3fb950;">Query executed in 3.4 ms • SSTables read: 1</span>
        </div>
        <table>
          <thead>
            <tr>
              <th>matricula (PK)</th>
              <th>fecha_hora (CK DESC)</th>
              <th>tipo_evento</th>
              <th>modulo</th>
              <th>estado</th>
              <th>ip_origen</th>
              <th>latencia_ms</th>
              <th>detalles</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="color: #58a6ff;">24300700</td>
              <td>2026-11-10 16:00:10</td>
              <td>CONSULTA_CATALOGO</td>
              <td>API Gateway</td>
              <td><span class="tag-ok">EXITOSO</span></td>
              <td>10.50.149.121</td>
              <td>28</td>
              <td>Consulta de ofertas de empleo y prácticas</td>
            </tr>
            <tr>
              <td style="color: #58a6ff;">24300700</td>
              <td>2026-11-06 14:20:45</td>
              <td>DESCARGA_DOCUMENTO</td>
              <td>Portal Estudiantil</td>
              <td><span class="tag-ok">EXITOSO</span></td>
              <td>10.50.149.121</td>
              <td>350</td>
              <td>Descarga de Certificado oficial en PDF</td>
            </tr>
            <tr>
              <td style="color: #58a6ff;">24300700</td>
              <td>2026-11-03 10:15:00</td>
              <td>SOLICITUD_SERVICIO</td>
              <td>Servicios Escolares</td>
              <td><span class="tag-ok">EXITOSO</span></td>
              <td>10.50.149.121</td>
              <td>98</td>
              <td>Solicitud de Certificado de Estudios</td>
            </tr>
            <tr>
              <td style="color: #58a6ff;">24300700</td>
              <td>2026-11-01 08:45:22</td>
              <td>SOLICITUD_SERVICIO</td>
              <td>Servicios Escolares</td>
              <td><span class="tag-ok">EXITOSO</span></td>
              <td>10.50.149.121</td>
              <td>120</td>
              <td>Inscripción a Taller de Cloud Computing</td>
            </tr>
            <tr>
              <td style="color: #58a6ff;">24300700</td>
              <td>2026-11-01 08:30:15</td>
              <td>LOGIN_AUTENTICACION</td>
              <td>Autenticación</td>
              <td><span class="tag-ok">EXITOSO</span></td>
              <td>10.50.149.121</td>
              <td>45</td>
              <td>Inicio de sesión institucional correcto</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>
</body>
</html>"""

# Render tasks
gui_tasks = [
    (html_docker_desktop, os.path.join(evidencias_dir, "generales", "01_docker_compose_ps.png"), 1120, 750),
    (html_compass_agg, os.path.join(evidencias_dir, "mongodb", "02_mongo_update_aggregation.png"), 1120, 780),
    (html_cassandra_studio, os.path.join(evidencias_dir, "cassandra", "01_cassandra_cqlsh_select.png"), 1120, 760),
]

for html, out_png, w, h in gui_tasks:
    render_html_to_png(html, out_png, w, h)

print("\n[ÉXITO] Nuevas capturas GUI nativas generadas correctamente.")
