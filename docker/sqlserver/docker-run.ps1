# Script para desplegar SQL Server 2025 en Docker conectado a campuscloud_net

docker run -d `
  --name campuscloud-sqlserver `
  --network campuscloud-db-net `
  -p 1434:1433 `
  --env-file "$PSScriptRoot\.env" `
  -v campuscloud-sqlserver-data:/var/opt/mssql `
  --restart=always `
  mcr.microsoft.com/mssql/server:2025-CU8-ubuntu-24.04
