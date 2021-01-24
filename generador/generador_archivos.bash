#!/bin/bash
DIRECTORIO=${1}
if [ "${DIRECTORIO}" == "" ]
then
  DIRECTORIO=$(pwd)
else
  if [ ! -d ${DIRECTORIO} ]; then
    echo "${DIRECTORIO} no es un directorio valido"
    exit 1
  fi
fi
echo "Archivos seran generados en ${DIRECTORIO}"
cd ${DIRECTORIO}
while [ 1 ]
do
  generar_archivo=$((1 + ${RANDOM} % 10))
  echo "Valor de generar_archivos = ${generar_archivo}"
  if [ ${generar_archivo} -le 5 ] # se generara archivo
  then
    echo -n "Se generara archivo con nombre "
    nombre_archivo=$(date +%Y_%m_%d-%H_%M_%S)
    echo "${nombre_archivo}.txt"
    touch ${nombre_archivo}.txt
  fi
  sleep 15
done
