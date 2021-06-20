from System.IO import Path, StreamWriter
from Spotfire.Dxp.Application.Visuals import CrossTablePlot

targetFileName = "C:/Users/hp/Desktop/guru/test.txt"
#targetFileName = Path.GetTempFileName()

#Write to file 
writer = StreamWriter(targetFileName,True) #True to append
aLine = "|".join(("str1","str2","str3"))
writer.Write(aLine)
writer.Close()

print targetFileName
print aLine