from Spotfire.Dxp.Data import *

tableName='Sample Data'
columnToFetch='Region'
activeTable=Document.Data.Tables[tableName]
rowCount = activeTable.RowCount
rowsToInclude = IndexSet(rowCount,True)
cursor1 = DataValueCursor.CreateFormatted(activeTable.Columns[columnToFetch])
ctr1 = 0
for row in activeTable.GetRows(rowsToInclude,cursor1):
	rowIndex = row.Index
	val1 = cursor1.CurrentValue
	ctr1 = ctr1 + 1
	print val1
	#if (ctr1 == 5):
	#break