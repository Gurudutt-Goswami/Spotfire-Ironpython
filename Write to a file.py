#you can modify path of targetfilename as per your need, also if you don't want to mention & wanted to save file in temp just uncomment line 8
#you can also have a lot more fun connecting this with multiline input field document property

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
