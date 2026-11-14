# Script para desplegar MongoDB Community Server en Docker conectado a campuscloud-db-net

docker run -d `
  --name campuscloud-mongodb `
  --network campuscloud-db-net `
  -p 27017:27017 `
  --env-file "$PSScriptRoot\.env" `
  -v campuscloud-mongo-data:/data/db `
  --restart=always `
  mongodb/mongodb-community-server:9.0-ubi9-slim
