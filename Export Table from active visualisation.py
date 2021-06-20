#Replace the file path with forward slash & you are done 

from Spotfire.Dxp.Data.Export import DataWriterTypeIdentifiers
from System.IO import File

writer = Document.Data.CreateDataWriter(DataWriterTypeIdentifiers.ExcelXlsDataWriter)
table = Document.ActiveDataTableReference #OR pass the DataTable as parameter
filtered = Document.ActiveFilteringSelectionReference.GetSelection(table).AsIndexSet() #OR pass the filter
stream = File.OpenWrite("C:/Users/hp/Desktop/guru/nice.csv")
names = []
for col in table.Columns: 
    names.append(col.Name)
writer.Write(stream, table, filtered, names)
stream.Close()
