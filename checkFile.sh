#!/bin/bash
pathToFile="/Users/danito/ProyectoPersonal/Proyectos/Profiling/data.txt"
todays=$(date +'%d-%m-%Y %H:%M:%S')
today=$(date +'%d-%m-%Y')
if [ -f $pathToFile ] ; then
	echo "$todays Se ha encontrado el archivo en la ruta especificada." | tee -a checkFile.log profiling.log
	if [ -s $pathToFile ] ; then
		echo "$todays Iniciando el flujo de perfilado con python..." | tee -a checkFile.log profiling.log
		mkdir "Reporting_$today"
	else
		echo "$todays ERROR: El archivo se encuentra vacío. No se puede iniciar el flujo de perfilado." | tee -a checkFile.log profiling.log
	fi
else
	echo "$todays ERROR: No se ha encontrado el archivo en la ruta especificada." | tee -a checkFile.log profiling.log
fi

