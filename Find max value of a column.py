#Add test_data as a script parameter & define your table 
#In place of "Units" put your column name for which you want to find max 
activeFilteringSelection = Document.ActiveFilteringSelectionReference.GetSelection(test_data).AsIndexSet()
column = test_data.Columns["Units"]
max = column.RowValues.GetMaxValue(activeFilteringSelection).ValidValue
print max
