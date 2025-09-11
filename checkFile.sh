#!/bin/bash
yesterdayDate=$(date -v -1d +'%d-%m-%Y')
yesterdayFile="/Users/danito/ProyectoPersonal/Proyectos/Profiling/Reporting_$yesterdayDate"
pathToFile="/Users/danito/ProyectoPersonal/Proyectos/Profiling/data.txt"
todays=$(date +'%d-%m-%Y %H:%M:%S')
todayDate=$(date +'%d-%m-%Y')
todayFile="/Users/danito/ProyectoPersonal/Proyectos/Profiling/Reporting_$todayDate"
reportings="/Users/danito/ProyectoPersonal/Proyectos/Profiling/Reportings"

if [ -d $yesterdayFile ] ; then
	tar -czf "$yesterdayFile.tar" "$yesterdayFile"
	if [ -f "$yesterdayFile.tar" ] ; then
		echo "$todays Se creó la carpeta comprimida."
	else
		echo "$todays Ocurrió un error. No se ha podido crear la carpeta comprimida."
	fi
	mv "$yesterdayFile.tar" "$reportings/Reporting_$yesterdayDate.tar"
	rm -r "$yesterdayFile"
	echo "$todays La carpeta Reporting_$yesterdayDate ha sido comprimida y eliminada.">>/Users/danito/ProyectoPersonal/Proyectos/Profiling/Logs/profiling.log
fi
if [ -f $pathToFile ] ; then
	echo "$todays Se ha encontrado el archivo en la ruta especificada." | tee -a /Users/danito/ProyectoPersonal/Proyectos/Profiling/Logs/checkFile.log /Users/danito/ProyectoPersonal/Proyectos/Profiling/Logs/profiling.log
	if [ -s $pathToFile ] ; then
		echo "$todays Iniciando el flujo de perfilado con python..." | tee -a /Users/danito/ProyectoPersonal/Proyectos/Profiling/Logs/checkFile.log /Users/danito/ProyectoPersonal/Proyectos/Profiling/Logs/profiling.log
		mkdir -p "$todayFile"
		mv $pathToFile "$todayFile"
		/Library/Frameworks/Python.framework/Versions/3.10/bin/python3 /Users/danito/ProyectoPersonal/Proyectos/Profiling/profilingFile.py
	else
		echo "$todays ERROR: El archivo se encuentra vacío. No se puede iniciar el flujo de perfilado." | tee -a /Users/danito/ProyectoPersonal/Proyectos/Profiling/Logs/checkFile.log /Users/danito/ProyectoPersonal/Proyectos/Profiling/Logs/profiling.log
	fi
else
	echo "$todays ERROR: No se ha encontrado el archivo en la ruta especificada." | tee -a /Users/danito/ProyectoPersonal/Proyectos/Profiling/Logs/checkFile.log /Users/danito/ProyectoPersonal/Proyectos/Profiling/Logs/profiling.log
fi

