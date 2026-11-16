import os
import shutil
import zipfile

def package_submission():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    folder_name = "Calzadilla_Mariano_NoSQL_Practicas_CampusCloud"
    stage_dir = os.path.join(base_dir, "temp_submission_stage", folder_name)
    zip_output_path = os.path.join(base_dir, f"{folder_name}.zip")

    print(f"Empaquetando entrega reducida para Classroom en: {zip_output_path}")

    # Limpiar staging previo
    if os.path.exists(os.path.dirname(stage_dir)):
        shutil.rmtree(os.path.dirname(stage_dir))
    os.makedirs(stage_dir, exist_ok=True)

    # 1. 01-configuracion/ (compose.yaml y .env.example)
    cfg_dir = os.path.join(stage_dir, "01-configuracion")
    os.makedirs(cfg_dir, exist_ok=True)
    shutil.copy2(os.path.join(base_dir, "docker", "compose.yaml"), os.path.join(cfg_dir, "compose.yaml"))
    shutil.copy2(os.path.join(base_dir, "docker", ".env.example"), os.path.join(cfg_dir, ".env.example"))

    # 2. 02-mongodb/ (scripts .js)
    mongo_dir = os.path.join(stage_dir, "02-mongodb")
    os.makedirs(mongo_dir, exist_ok=True)
    src_mongo = os.path.join(base_dir, "mongodb")
    for f in os.listdir(src_mongo):
        if f.endswith(".js"):
            shutil.copy2(os.path.join(src_mongo, f), os.path.join(mongo_dir, f))

    # 3. 03-neo4j/ (scripts .cypher)
    neo_dir = os.path.join(stage_dir, "03-neo4j")
    os.makedirs(neo_dir, exist_ok=True)
    src_neo = os.path.join(base_dir, "neo4j")
    for f in os.listdir(src_neo):
        if f.endswith(".cypher"):
            shutil.copy2(os.path.join(src_neo, f), os.path.join(neo_dir, f))

    # 4. 04-columnas-anchas/ (scripts .cql)
    cass_dir = os.path.join(stage_dir, "04-columnas-anchas")
    os.makedirs(cass_dir, exist_ok=True)
    src_cass = os.path.join(base_dir, "cassandra")
    for f in os.listdir(src_cass):
        if f.endswith(".cql"):
            shutil.copy2(os.path.join(src_cass, f), os.path.join(cass_dir, f))

    # 5. 05-evidencias/
    evi_dir = os.path.join(stage_dir, "05-evidencias")
    src_evi = os.path.join(base_dir, "evidencias", "unidad-ii")
    if os.path.exists(src_evi):
        shutil.copytree(src_evi, evi_dir, dirs_exist_ok=True)
    else:
        for sub in ["mongodb", "neo4j", "cassandra", "generales"]:
            os.makedirs(os.path.join(evi_dir, sub), exist_ok=True)

    # 6. README.md para la entrega reducida
    readme_content = f"""# Portafolio Reducido de Prácticas NoSQL - CampusCloud
Alumno: Mariano Calzadilla Alvarez (Matrícula: 2026001)
Asignatura: Bases de Datos en la Nube
Unidad II - Actividad de Evaluación 2 (55 %)

## Contenido del Portafolio:
- 01-configuracion/: Archivo compose.yaml integrado y plantilla .env.example
- 02-mongodb/: 6 scripts ejecutables de creación, carga, consultas, actualización, eliminación y agregación
- 03-neo4j/: 3 scripts Cypher de red de grafos, consultas y actualización
- 04-columnas-anchas/: 5 scripts CQL para Apache Cassandra (telemetría y eventos)
- 05-evidencias/: Capturas e índice de ejecución por motor

Repositorio GitHub completo: https://github.com/mariano-si7/CAMPUSCLOUD
"""
    with open(os.path.join(stage_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

    # Crear ZIP
    if os.path.exists(zip_output_path):
        os.remove(zip_output_path)

    with zipfile.ZipFile(zip_output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(os.path.dirname(stage_dir)):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, os.path.dirname(stage_dir))
                zipf.write(full_path, rel_path)

    # Limpiar stage
    shutil.rmtree(os.path.dirname(stage_dir))

    print(f"[OK] Paquete ZIP generado exitosamente: {zip_output_path} ({os.path.getsize(zip_output_path)} bytes)")

    # Mostrar listado de archivos dentro del zip
    with zipfile.ZipFile(zip_output_path, "r") as zipf:
        print("\nArchivos incluidos en el ZIP:")
        for name in zipf.namelist():
            print(f"  - {name}")

if __name__ == "__main__":
    package_submission()
