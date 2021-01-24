# Monitor de eventos

El *Monitor de eventos* está escrito en Python. 

```
#!/usr/bin/env python3
import fnmatch
import os
import redis
import sys
import time

print("Hola mundo")
if len(sys.argv) == 2:
  dirpath=sys.argv[1]
else:
  dirpath=os.getcwd()

if not os.path.isdir(dirpath):
  print("%s no es un directorio"%(dirpath))
  os.exit(2)
print("Directorio a monitorear -> %s"%(dirpath))
os.chdir(dirpath)
while True:
  print(len(fnmatch.filter(os.listdir(dirpath), '*.txt')))
  time.sleep(30)
```

Este script es desplegado dentro de un contenedor, el cual es posteriormente ejecutado por `docker-compose`.
