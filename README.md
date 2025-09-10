-------------------------------*

**** PROFILING PROJECT ****
*------------------------------
In this project, the main objective is to practice scripting in Bash and using the  matplolib and pandas libraries in python. The project will serve as an automated data profiling tool.
    Suppose we have a client's system where new data arrives every day. Our system detects the deltas and creates a text file with them, which is then downloaded automatically to our local system. After this, we need to verify if all of these deltas represent valid and clean data.
    This is where our PROFILING PROJECT flow begins: using a cron job, we automatically generate graphs that show the data's validity and cleanliness, allowing for informed decision-making. 

The project will accomplish this by following a specific flow:

1.  **Bash Scripting**: Create a Bash script (**checkFile.sh**) to verify if the file "data.txt" exists. If it does not, an alert will be logged to **checkFile.log**.

2.  **Python Scripting**: Execute a Python script (**profilingFile.py**) to manipulate "data.txt" and convert it into a more readable .csv file. The script will log any errors if the process fails.

3.  **Data Profiling**: Once the new CSV file is ready, the Python script (**profiling.py**)will analyze the data to determine:
    * The total number of rows.
    * The number of rows with and without a name.
    * The most frequent names and last names.
    * The number of unique last names and how many are missing.
    * The number of rows that comply with the Mexican CURP format.
    * Whether any CURP values are duplicated.

4.  **Reporting**: After analyzing the data, the script will:
    * Generate a graph to visually represent the findings.
    * Save all the results to a new file.

5.  **Automation**: Automate the entire process using a cron job or a similar scheduler like Launchd. Create a .tar with the previous profiling folder; after that, remove the directory.
    
