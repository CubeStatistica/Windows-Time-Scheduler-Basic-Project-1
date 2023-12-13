color 0a

:: location of your anaconda dir.
set root=C:\Users\Cube Statistica\anaconda3

:: Call the Anaconda prompt.
call %root%\Script\activate.bat

:: Run the code using the anaconda python installation in anaconda prompt.
%root%\python.exe "E:\CubeStatistica\LessonsAndBooks\Windows-Time-Scheduler-Basic-Project-1\Production-Script-Update-DataCSV-File.py"

::pause :: the two colons comments the line of code - but only that line of code

@REM pause This is another way of commenting out but when echo is on which is the default. Can remove @ when echo is off.

pause