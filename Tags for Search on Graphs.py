
from Spotfire.Dxp.Data import TagsColumn, RowSelection, DataValueCursor, IndexSet
import clr
import re
reasonList = Document.Properties["search"].split(',')
tagsColumn = myTable.Columns["Result"].As[TagsColumn]()
filteringRowSelection = Document.ActiveFilteringSelectionReference.GetSelection(myTable)
_reason = DataValueCursor.CreateFormatted(myTable.Columns["Country"])
tagsColumn.Tag("No", filteringRowSelection)
filteredSet = IndexSet(filteringRowSelection.AsIndexSet())
rowsToInclude = IndexSet(myTable.RowCount,True)
rowsToFilter = IndexSet(myTable.RowCount,False)
if (len(Document.Properties["search"]) == 0):
  tagsColumn.Tag("Yes", RowSelection(IndexSet.And(filteredSet,filteringRowSelection.AsIndexSet())))
elif (len(Document.Properties["search"]) > 0):
  for row in myTable.GetRows(filteringRowSelection.AsIndexSet(),_reason):
    reason = _reason.CurrentValue
    reasonFound = 0
    for item in reasonList:
      result = re.findall('\\b'+item.strip()+'\\b', reason, flags=re.IGNORECASE)
      if len(result)>0:
        reasonFound = 1
        break
    if (reasonFound == 0):
      filteredSet.RemoveIndex(int(row.Index))
  tagsColumn.Tag("Yes", RowSelection(IndexSet.And(filteredSet,filteringRowSelection.AsIndexSet())))