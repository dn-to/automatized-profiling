Scripts python-bash:

---> _Autobackup_: Make a .tar from a directory. Then, call python to make a log if the process was successful or not.

---> _CheckCountErrores_: Review if there is any error(s) in a file. Then, send them to python and generate a log with current datetime. 

---> _ReviewProcess_: Review if a specific process is running. Send an alert with python in case that THE process isn't running.

---> _RenameFilesMass_: Two bash scripts. The first one is to create 10 files in a row. With the second one, find all the .txt files and send it to python, which rename those files adding datetime: "datetime_originalName.txt".

---> _CheckDUAlert_: Review du from a specific directory. If the du it's over from the umbral, it sends an alert with python, adding the 5 files with more weight in that directory. 

-------------------------------*

**** PROJECT WITH CRON/LAUNCHD ****
*------------------------------
CLEANSING OLD FILES: As its name says, the objective of this project is to find all the files that have more than X days in the specific directory and delete it. 
Find the files with the bash script, then send it to python and create a log with the files that were deleted.
Also, cron this job.
With cron, (Cron directory):
    * developingCronTab: this file is the cronjob, raw.
    * cron.log: the "error-log" file.

With launchctl, (Launchd directory):
    First, the file plist must be on the "user/library/launchAgents/---.plist". The file is: com.danito.cleansing-files.plist
    *launchd_err_out.log: "error-log"
    *launchd_out.log: it has everything that the scripts has as output.
    Comment: to see the log of launchctl, you need to put "log stream | grep plist name"
