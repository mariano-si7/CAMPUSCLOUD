# Script para desplegar pgAdmin en Docker conectándolo a dos redes

docker run -d `
  --name pgadmin-CampusCloud `
  --network campuscloud-web-net `
  -p 8082:80 `
  --env-file "$PSScriptRoot\.env" `
  -v campuscloud-pgadmin-data:/var/lib/pgadmin `
  --restart=always `
  dpage/pgadmin4:6.17

# Conectar pgAdmin a la red de la base de datos (campuscloud-db-net)
docker network connect campuscloud-db-net pgadmin-CampusCloud
