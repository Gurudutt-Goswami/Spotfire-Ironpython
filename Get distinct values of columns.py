#Run following ironpython just replace “Sample Data” with your tabel name and column name “Region” & "Item" with your column name for which you have to find distinctive values.


#get unique values from column (7.0)
from Spotfire.Dxp.Data import DataValueCursor
from Spotfire.Dxp.Data import IndexSet

tableName = 'Sample Data'
columnName = "Region"
columnName1 = "Item"
dt = Document.Data.Tables[tableName]
cursor = DataValueCursor.Create[str](dt.Columns[columnName])
distinctRows = dt.GetDistinctRows(None,cursor) #none param to grab them by the all
#distinctRows = dt.GetDistinctRows(IndexSet(dt.RowCount,True),cursor) #...or an indexset with all true to get them all.

#get uniques
vals = []
distinctRows.Reset()
while distinctRows.MoveNext():vals.append(cursor.CurrentValue)

#show results

print vals

dt = Document.Data.Tables[tableName]
cursor = DataValueCursor.Create[str](dt.Columns[columnName1])
distinctRows = dt.GetDistinctRows(None,cursor) #none param to grab them by the all
#distinctRows = dt.GetDistinctRows(IndexSet(dt.RowCount,True),cursor) #...or an indexset with all true to get them all.

#get uniques
vals = []
distinctRows.Reset()
while distinctRows.MoveNext():vals.append(cursor.CurrentValue)

#show results


print vals
