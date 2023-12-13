# Windows-Time-Scheduler-Basic-Project-1


Windows-Time-Scheduler-Basic-Project-1



2023-Dec-13 

1. Have added batch file that runs the python production code script.

2. Now create task in Task scheduler to run the batch file every day at with one 1 interval. Hopefully this is not too many times and does not break something like the csv file. Hopefully not since it is a csv file and an excel file.

**Note.** Issue in the batch file. Need to write the entire path to the python script file for the batch to run. Not just the name of the python scipt file.

3. Corrected the above and added a column in the dataset with the number of rows added when the script ran.

4. Created the task in task scheduler

5. Task Scheduler code execution failed. Code executed however received PermissionError for csv file:

C:\Windows\system32>python E:\CubeStatistica\LessonsAndBooks\Windows-Time-Scheduler-Basic-Project-1\Production-Script-Update-DataCSV-File.py
Traceback (most recent call last):
  File "E:\CubeStatistica\LessonsAndBooks\Windows-Time-Scheduler-Basic-Project-1\Production-Script-Update-DataCSV-File.py", line 27, in <module>
    df.to_csv(file_path, mode="a", header=False, index=False)
  File "C:\Users\Cube Statistica\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\pandas\core\generic.py", line 3902, in to_csv
    return DataFrameRenderer(formatter).to_csv(
  File "C:\Users\Cube Statistica\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\pandas\io\formats\format.py", line 1152, in to_csv
    csv_formatter.save()
  File "C:\Users\Cube Statistica\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\pandas\io\formats\csvs.py", line 247, in save
    with get_handle(
  File "C:\Users\Cube Statistica\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\pandas\io\common.py", line 863, in get_handle
    handle = open(
PermissionError: [Errno 13] Permission denied: 'Production-database.csv'


**I believe the permission error is an issue of microsoft cmd when run from task scheduler. When I run the batch file manually by double clinking on the file it works. When I schedule the same task in task scheduler it does not. There for will try to use another shell program to run the batch file. Will try Anaconda terminal. 

6. We will change the batch file to run in Anaconda termal instead of executing in cmd.

7. This option is not working because the user name I choose has a space. Very unintelligent of me. 

8. Going back to trying run it in windows shell cmd using task scheduler. 

9. Change "configure for" from Windows Vista to Window 10

10. Checked box in General Run with highest privilage. Still not working. This time got the error because cannot simply write python <script_path> need to identify the path to where the python executable exists. however, my path ot the executable has a space in it. That completely messes up when running the shell execution. This was not a problem when running the batch file locally because to run it locally would have to open the folder where the batch file was and double clicked the run.bat file. Because of that did not have to tell the batch file where the python executable was as the code `python <python_script>` would work. Need to find a way either work around the path containg space that points to the python executable or run batch file locally.

11. Wrote the line in run.bat file which sets the current directory to where the batch file is located.  This allowed the batch file to run as if running locally. Now the code `python <python_script>` in batch file works. Found this using Chatgpt:

rem The next line is optional and helps to set the current directory to the script's directory
rem cd /d %~dp0

12. Using the above the code now works in task scheduler when task is scheduled. Though most likely will not work if the csv file to write to is opened. Need to properly test this. Otherwise it now works! Added 3 rows now at row 201.




