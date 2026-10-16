# Arquitectura Técnica - CampusCloud (Nube Académica Local)

## 1. Diagrama de Arquitectura
```
[ Host Local Windows - IP: 10.50.149.121 ]
  ├── Docker Engine 29.2
  │     └── Contenedor: campuscloud-sqlserver
  │           ├── Motor: Microsoft SQL Server 2025 (Ubuntu 24.04 LTS)
  │           ├── Puerto Interno: 1433/tcp
  │           ├── Puerto Publicado Host: 1434/tcp (0.0.0.0:1434->1433)
  │           └── Base de Datos: CampusCloud
  └── Almacenamiento Persistente
        └── Volumen Docker: campuscloud-sqlserver-data (/var/opt/mssql)
```

## 2. Puntos de Conexión
- **Local (Misma PC):** `localhost,1434`
- **Remoto (Red LAN):** `10.50.149.121,1434`
- **Credenciales Superadministrador:** `sa` / `sqlserver2026!`
- **Usuario Operativo:** `user_admin` / `UserAdmin123!`
- **Usuario Solo Lectura:** `user_consulta` / `UserConsulta123!`
