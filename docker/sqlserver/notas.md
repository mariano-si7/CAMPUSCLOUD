# SQL Server en Docker

## Objetivo

Levantar SQL Server dentro de un contenedor Docker y conectarlo a la misma red donde viven los demas contenedores del proyecto, por ejemplo PostgreSQL y pgAdmin.

## Archivos importantes

- `docker-run.ps1`: script que crea la red si no existe y despues ejecuta el contenedor.
- `.env`: variables reales usadas por Docker. Este archivo no se sube a Git.
- `.env.example`: ejemplo de variables para compartir la configuracion sin exponer contrasenas.

## Variables de entorno

El archivo `.env` debe tener este formato:

```env
ACCEPT_EULA=Y
MSSQL_SA_PASSWORD=CampusCloud123$
```

`ACCEPT_EULA=Y` acepta la licencia de SQL Server dentro del contenedor.

`MSSQL_SA_PASSWORD` define la contrasena del usuario administrador `sa`. SQL Server exige una contrasena fuerte: mayusculas, minusculas, numero y simbolo.

## Comando usado

```powershell
docker network create campuscloud-db-net 2>$null

docker run -d `
  --name campuscloud-sqlserver `
  --network campuscloud-db-net `
  -p 1434:1433 `
  --env-file "$PSScriptRoot\.env" `
  -v campuscloud-sqlserver-data:/var/opt/mssql `
  --restart=always `
  mcr.microsoft.com/mssql/server:2022-latest
```

## Que hace cada parte

`docker network create campuscloud-db-net 2>$null` crea la red compartida entre contenedores. Si ya existe, el error se oculta para que el script pueda continuar.

`docker run` crea y arranca un contenedor nuevo.

`--env-file "$PSScriptRoot\.env"` carga las variables de entorno desde el archivo `.env` ubicado en la misma carpeta del script.

`-d` ejecuta el contenedor en segundo plano.

`--network campuscloud-db-net` conecta SQL Server a la red del proyecto. Gracias a esto, otros contenedores pueden encontrarlo por su nombre: `campuscloud-sqlserver`.

`--name campuscloud-sqlserver` asigna un nombre fijo al contenedor.

`-p 1434:1433` publica el puerto. El puerto `1433` es el puerto interno de SQL Server dentro del contenedor; el puerto `1434` es el puerto que se usa desde la computadora anfitriona.

`-v campuscloud-sqlserver-data:/var/opt/mssql` crea un volumen persistente. La informacion de SQL Server queda guardada aunque el contenedor se elimine.

`--restart always` hace que el contenedor vuelva a iniciar automaticamente si Docker se reinicia.

`mcr.microsoft.com/mssql/server:2022-latest` es la imagen oficial de SQL Server para Linux.

## Como ejecutarlo

Desde PowerShell:

```powershell
cd docker\sqlserver
Copy-Item .env.example .env
.\docker-run.ps1
```

## Como conectarse

Desde la computadora:

- Servidor: `localhost,1434`
- Usuario: `sa`
- Contrasena: la indicada en `MSSQL_SA_PASSWORD`

Desde otro contenedor en la misma red:

- Servidor: `campuscloud-sqlserver,1433`
- Usuario: `sa`
- Contrasena: la indicada en `MSSQL_SA_PASSWORD`

## Comandos utiles

Ver contenedores activos:

```powershell
docker ps
```

Ver logs de SQL Server:

```powershell
docker logs campuscloud-sqlserver
```

Detener el contenedor:

```powershell
docker stop campuscloud-sqlserver
```

Eliminar el contenedor sin borrar datos:

```powershell
docker rm campuscloud-sqlserver
```

Eliminar el volumen de datos:

```powershell
docker volume rm campuscloud-sqlserver-data
```
