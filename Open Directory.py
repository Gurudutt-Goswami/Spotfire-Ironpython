import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import FolderBrowserDialog

#choose folder for output
filename=""
folder=FolderBrowserDialog()
result=folder.ShowDialog()
filename=folder.SelectedPath 

#selected folder
print "Selected folder: " + filename