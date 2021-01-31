# docker-compose

En este repositorio se encontrarán una serie de archivos que permiten el despliegue de una aplicación como lo indica la figura.

![](figuras/03-Docker-Compose.png "Aplicativo")

Los detalles de la aplicación de la figura anterior y de los archivos en este repositorio se pueden encontrar en este [documento de Google Docs](https://docs.google.com/document/d/1VtM1TKRwUh2RV5pZhgu4c8rhr5iKwcC7mqzXtRbDvkc/edit?usp=sharing).

---

Los archivos relativos al *Generador de eventos* se encuentran en el directorio [generador](generador).

Los archivo del *Monitor de eventos* se encuentran en el directorio [monitor](monitor).

El [docker-compose.yaml](docker-compose.yaml) define tres servicios que modelan el aplicativo representado en la figura arriba.

---

## Ejecución del aplicativo

Para llevar a cabo la ejecución del aplicativo se debe ubicar en el directorio donde se encuentra el `docker-compose.yaml` de este repositorio.
Ahora, ejecutar el comando

```
docker-compose up
```

---

Abrir otra terminal y **asegurarse de estar ubicado en el directorio donde se encuentra el `docker-compose.yaml` de este repositorio**, entonces ejecutar:

```
docker-compose exec monitor bash
```

Después de acceder al `Monitor de eventos` ejecutar el comando

```
tail -f /tmp/monitor.log
```

Esto le permitirá observar las diferentes acciones ejecutadas por el aplicativo monitor escrito en Python.

---

**Abrir una tercera terminal** y ubíquese en el directorio donde esta el `docker-compose.yaml` de este repositorio. 
Ejecute el comando:

```
docker-compose exec redis sh
```

Ahora se encuentra dentro del contenedor que está corriendo la base de datos *Redis*.
Ejecute el comando:

```
redis-cli monitorº
```

