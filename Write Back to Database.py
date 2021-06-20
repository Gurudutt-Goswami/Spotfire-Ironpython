from Spotfire.Dxp.Data import *

#these are neccessary imports required to show messagebox
import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import MessageBox, MessageBoxButtons
from System.Windows.Forms import DialogResult

#these are neccessary imports requiered to insert data into sql 
from Spotfire.Dxp.Data.Import import DatabaseDataSource
from Spotfire.Dxp.Data.Import import DatabaseDataSourceSettings
from Spotfire.Dxp.Application.Visuals import TablePlot
from Spotfire.Dxp.Application.Visuals import VisualTypeIdentifiers
from Spotfire.Dxp.Data import IndexSet
from Spotfire.Dxp.Data import RowSelection
from Spotfire.Dxp.Data import DataValueCursor
from Spotfire.Dxp.Data import DataSelection
from Spotfire.Dxp.Data import DataPropertyClass

#tableName='test_data'
#YOU CAN ADD AS MANY COLUMNS AS YOU WANT TO FETCH FROM TABLE
tableName='test_data'
columnToFetch_id='id'
columnToFetch_name='name'
columnToFetch_age='age'
columnToFetch_gender='gender'


activeTable=Document.Data.Tables[tableName]

#GIVES TOTAL NO OF ROW COUNT 
rowCount = activeTable.RowCount
rowsToInclude = IndexSet(rowCount,True)



cursor1 = DataValueCursor.CreateFormatted(activeTable.Columns[columnToFetch_id])
cursor2 = DataValueCursor.CreateFormatted(activeTable.Columns[columnToFetch_name])
cursor3 = DataValueCursor.CreateFormatted(activeTable.Columns[columnToFetch_age])
cursor4 = DataValueCursor.CreateFormatted(activeTable.Columns[columnToFetch_gender])
ctr1 = 0

count=0

#FROM WHICH YOU WANT TO SEARCH AND COMPARE
name = Document.Properties["name"]
#print name

#COLUMN WHICH YOU WANT TO SET 
age = Document.Properties["age"]

ctrl = 0
#print age 


#LOOP REQUIRED TO FETCH ALL VALUES OF COLUMNS 
for row in activeTable.GetRows(rowsToInclude,cursor1,cursor2,cursor3,cursor4):
	#rowIndex = row.Index
	#print rowIndex
	ctrl = ctrl +1
	val2 = cursor2.CurrentValue
	if(val2 == name): 
		count=count+1
		val1 = cursor1.CurrentValue
		#print val1
		vname = cursor2.CurrentValue
		val3 = cursor3.CurrentValue
		val4 = cursor4.CurrentValue
		new_id	= int(val1)+1
	if(ctrl == rowCount):
		break
		
		
#CHECKING WHETHER THAT NAME IS PRESENT IN TABLE OR NOT 
if(count != 0):
	MessageBox.Show("this name is present")
	
	
	#INSERTING DATA INTO TABLE STARTS HERE
	#sqlCommand = "UPDATE empdata SET " + columnToFetch_age + "='" + str(age) + "'WHERE (name=" + name  + ");"
	#sqlCommand = "insert into empdata(name) values ('" +vname +"');"
	sqlCommand = "insert into empdata(id,name,age,gender) values ('"+str(new_id)+"','"+name+"','"+str(age)+"','" +val4+"');"
	#print val2
	#sqlCommand ="create table "+val4+" (id int);"
	dbsettings = DatabaseDataSourceSettings( "System.Data.SqlClient","Server=localhost;Database=OperationsDB;UID=OperationsUser;PWD=OperationsUser",sqlCommand)
	ds = DatabaseDataSource(dbsettings)
	newDataTable = Document.Data.Tables.Add("temp12",ds)
	Document.Data.Tables.Remove(newDataTable)
	#newDataTable = Document.Data.Tables.Add("temp",ds)

	#INSERTING DATA INTO TABLE ENDS HERE
	
	
	MessageBox.Show("Data Inserted Successfully !!")
else:
	MessageBox.Show("this name is not present")