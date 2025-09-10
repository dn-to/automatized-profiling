#!/bin/bash
yesterdayDate=$(date -v -1d +'%d-%m-%Y')
yesterdayFile="/Users/danito/ProyectoPersonal/Proyectos/Profiling/Reporting_$yesterdayDate"
pathToFile="/Users/danito/ProyectoPersonal/Proyectos/Profiling/data.txt"
todays=$(date +'%d-%m-%Y %H:%M:%S')
today=$(date +'%d-%m-%Y')

if [ -d $yesterdayFile ] ; then
	tar -czf "Reporting_$yesterdayDate.tar" "/Users/danito/ProyectoPersonal/Proyectos/Profiling"
	rm -r "Reporting_$yesterdayDate"
	echo "$todays La carpeta Reporting_$yesterdayDate ha sido comprimida y eliminada.">>./Logs/profiling.log
fi
if [ -f $pathToFile ] ; then
	echo "$todays Se ha encontrado el archivo en la ruta especificada." | tee -a ./Logs/checkFile.log ./Logs/profiling.log
	if [ -s $pathToFile ] ; then
		echo "$todays Iniciando el flujo de perfilado con python..." | tee -a ./Logs/checkFile.log ./Logs/profiling.log
		mkdir "Reporting_$today"
	else
		echo "$todays ERROR: El archivo se encuentra vacío. No se puede iniciar el flujo de perfilado." | tee -a ./Logs/checkFile.log ./Logs/profiling.log
	fi
else
	echo "$todays ERROR: No se ha encontrado el archivo en la ruta especificada." | tee -a ./Logs/checkFile.log ./Logs/profiling.log
fi

