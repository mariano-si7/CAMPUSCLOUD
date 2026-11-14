# Script para desplegar SQL Server en Docker conectado a campuscloud-db-net
docker network create campuscloud-db-net 2>$null

docker run -d `
  --name campuscloud-sqlserver `
  --network campuscloud-db-net `
  -p 1434:1433 `
  --env-file "$PSScriptRoot\.env" `
  -v campuscloud-sqlserver-data:/var/opt/mssql `
  --restart=always `
  mcr.microsoft.com/mssql/server:2022-latest
