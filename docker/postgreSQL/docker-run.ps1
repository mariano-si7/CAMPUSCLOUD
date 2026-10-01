# Script para desplegar PostgreSQL en Docker conectado a campuscloud-db-net

docker run -d `
  --name postgres-campuscloud `
  --network campuscloud-db-net `
  -p 54320:5432 `
  --env-file "$PSScriptRoot\.env" `
  -v campuscloud-postgres-data:/var/lib/postgresql/data `
  --restart=always `
  postgres:alpine
