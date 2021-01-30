import fnmatch
import os
import redis
import sys
import time
import redis
import logging
#
# Prepacion de la facilidad de logging
#
logging.basicConfig(level=logging.DEBUG,
  filename="/tmp/monitor.log",format='%(asctime)s - %(message)s')
#
# ---
# Validacion de directorio a monitorear
#
if len(sys.argv) == 2:
  dirpath=sys.argv[1]
else:
  dirpath=os.getcwd()
if not os.path.isdir(dirpath):
  logging.error('No existe el directorio %s',dirpath)
  print("%s no es un directorio"%(dirpath))
  os._exit(2)
#
# ---
#
# Preparacion de facilidades para el rastreo y almacenamiento de los datos
#
cache = redis.Redis(host="redis",port=6379)
#
# ---
#
# Obtencion del dato a almacenar
#
logging.debug('Directorio a monitorear %s', dirpath)
print("Directorio a monitorear -> %s"%(dirpath))
os.chdir(dirpath)
totalFiles = len(fnmatch.filter(os.listdir(dirpath), '*.txt'))
logging.debug('Hay %d archivos',totalFiles)
#
# ---
#
# Almacenamiento efectivo de la informacion
#
retries = 5
while True:
  try:
    cache.set('TotalFiles',str(totalFiles))
    logging.debug('Almacenando valor %d',totalFiles)
    break
  except redis.exceptions.ConnectionError as exc:
    if (retries == 0):
      logging.exception("Varios intentos en excepcion de conexion")
      raise exc
    retries = retries - 1
    time.sleep(0.5)
