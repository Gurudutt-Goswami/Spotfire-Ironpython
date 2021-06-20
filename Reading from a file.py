#Modify the path of the file in 6 & 7 line

from System.IO import Path, StreamWriter
from Spotfire.Dxp.Application.Visuals import CrossTablePlot

targetFileName = "C:\Users\hp\Desktop\guru\ test.txt"
aLine=open(r'C:\Users\hp\Desktop\guru\test.txt').read()
 
#Debug
print targetFileName
print aLine
