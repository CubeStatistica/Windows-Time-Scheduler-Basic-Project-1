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

