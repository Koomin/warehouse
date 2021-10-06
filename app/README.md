<b> For build and run docker in production server </b><br>
docker-compose -f docker-compose.prod.yml up -d --build<br>
<b>For stop docker and remove volumes</b><br>
docker-compose down -v<br>
<b>Development server</b><br>
docker-compose up -d --build<br>