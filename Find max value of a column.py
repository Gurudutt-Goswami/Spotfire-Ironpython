activeFilteringSelection = Document.ActiveFilteringSelectionReference.GetSelection(test_data).AsIndexSet()
column = test_data.Columns["Units"]
max = column.RowValues.GetMaxValue(activeFilteringSelection).ValidValue
print max