# Notas y Guía de Despliegue de pgAdmin y PostgreSQL

## 🌐 Redes Docker Creadas
1. `campuscloud-db-net`: Red interna para comunicación entre PostgreSQL y pgAdmin.
2. `campuscloud-web-net`: Red pública/web para acceso desde el navegador local.

---

## 🔑 Credenciales e Inicio de Sesión

### 1. Acceso Web a pgAdmin
- **URL en el navegador**: [http://localhost:8082](http://localhost:8082)
- **Email de login**: `admin@campuscloud.com`
- **Contraseña de login**: `CampusCloud123$`

---

## 🐘 Conexión al Servidor PostgreSQL dentro de pgAdmin

Al hacer clic en **Add New Server** en pgAdmin:

### Pestana General:
- **Name**: `PostgreSQL CampusCloud`

### Pestana Connection:
- **Host name/address**: `postgres-campuscloud` (o `54320` si conectas desde fuera del contenedor)
- **Port**: `5432`
- **Maintenance database**: `postgres` (o `campuscloud_db`)
- **Username**: `postgres`
- **Password**: `CampusCloudPostgres#`
