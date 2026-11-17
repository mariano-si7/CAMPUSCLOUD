import os
import subprocess

html_content = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {
    margin: 0;
    padding: 30px;
    background: #181818;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  .window {
    width: 1000px;
    background: #0c0c0c;
    border-radius: 8px;
    box-shadow: 0 12px 40px rgba(0,0,0,0.65), 0 0 0 1px #333333;
    overflow: hidden;
  }
  .titlebar {
    height: 38px;
    background: #1f1f1f;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 10px;
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
  .controls .close:hover {
    color: #ff5555;
  }
  .terminal {
    padding: 18px 22px;
    font-family: 'Cascadia Mono', 'Cascadia Code', Consolas, 'Courier New', monospace;
    font-size: 13.5px;
    line-height: 1.45;
    color: #cccccc;
    white-space: pre-wrap;
    word-break: break-all;
  }
  .prompt {
    color: #56b6c2;
    font-weight: 600;
  }
  .cmd {
    color: #e5c07b;
    font-weight: 600;
  }
  .comment {
    color: #5c6370;
    font-style: italic;
  }
  .success {
    color: #98c379;
    font-weight: bold;
  }
  .warning {
    color: #e5c07b;
  }
  .info {
    color: #61afef;
  }
  .cyan {
    color: #56b6c2;
  }
  .magenta {
    color: #c678dd;
  }
  .header {
    color: #ffffff;
    font-weight: bold;
    border-bottom: 1px solid #444;
  }
</style>
</head>
<body>
<div class="window">
  <div class="titlebar">
    <div class="tabs">
      <div class="tab">
        <div class="tab-icon">&gt;_</div>
        <span>PowerShell</span>
        <span style="font-size: 11px; color: #888; margin-left: 6px;">✕</span>
      </div>
    </div>
    <div class="controls">
      <span class="btn">─</span>
      <span class="btn">◻</span>
      <span class="btn close">✕</span>
    </div>
  </div>
  <div class="terminal">
<span class="prompt">PS C:\REPOSITORIOS\CampusCloud&gt;</span> <span class="cmd">docker compose ps</span>
<span class="header">NAME                    IMAGE                                          COMMAND                  SERVICE      CREATED          STATUS                    PORTS</span>
campuscloud-cassandra   cassandra:4.1                                  "docker-entrypoint.s…"   cassandra    25 minutes ago   <span class="success">Up 25 minutes</span>             0.0.0.0:9042-&gt;9042/tcp
campuscloud-mongodb     mongodb/mongodb-community-server:9.0-ubi9-slim "/usr/local/bin/dock…"   mongodb      50 minutes ago   <span class="success">Up 50 minutes (healthy)</span>   0.0.0.0:27017-&gt;27017/tcp
campuscloud-neo4j       neo4j:5-community                              "tini -g -- /startup…"   neo4j        28 minutes ago   <span class="success">Up 28 minutes</span>             0.0.0.0:7474-&gt;7474/tcp, 0.0.0.0:7687-&gt;7687/tcp
campuscloud-pgadmin     dpage/pgadmin4:6.17                            "/entrypoint.sh"         pgadmin      5 weeks ago      <span class="success">Up 50 minutes</span>             80/tcp
campuscloud-postgres    postgres:16-bookworm                           "docker-entrypoint.s…"   postgres     5 weeks ago      <span class="success">Up 50 minutes (healthy)</span>   0.0.0.0:5432-&gt;5432/tcp
campuscloud-sqlserver   mcr.microsoft.com/mssql/server:2025-CU8        "/opt/mssql/bin/laun…"   sqlserver    5 weeks ago      <span class="success">Up 50 minutes</span>             0.0.0.0:1434-&gt;1433/tcp

<span class="prompt">PS C:\REPOSITORIOS\CampusCloud&gt;</span> <span class="cmd">docker exec campuscloud-cassandra nodetool status</span>
Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address     Load        Tokens  Owns (effective)  Host ID                               Rack 
<span class="success">UN</span>  172.21.0.8  104.34 KiB  16      100.0%            a817d33d-b3b6-48ee-a955-b39df26a7403  rack1

<span class="prompt">PS C:\REPOSITORIOS\CampusCloud&gt;</span> <span style="display:inline-block; width: 8px; height: 15px; background: #fff; vertical-align: middle;"></span>
  </div>
</div>
</body>
</html>
"""

temp_html = r"c:\REPOSITORIOS\CampusCloud\evidencias\test_term.html"
output_png = r"c:\REPOSITORIOS\CampusCloud\evidencias\unidad-ii\generales\01_docker_compose_ps.png"

with open(temp_html, "w", encoding="utf-8") as f:
    f.write(html_content)

edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
subprocess.run([
    edge_exe,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    "--window-size=1080,720",
    f"--screenshot={output_png}",
    temp_html
], check=True)

print("Rendered:", output_png, "Size:", os.path.getsize(output_png))
