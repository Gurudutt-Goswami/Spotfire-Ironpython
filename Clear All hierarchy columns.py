from Spotfire.Dxp.Application.Visuals import VisualContent
from Spotfire.Dxp.Application import Filters as filters
from Spotfire.Dxp.Application.Filters import FilterTypeIdentifiers

# Get the filter panel on the current active page
filterPanel = Document.ActivePageReference.FilterPanel
# Perform filtering action

for tableGroup in filterPanel.TableGroups:
	for fh in tableGroup.FilterHandles:
	   if fh.Visible:
		#print fh.FilterReference.Name
		if fh.FilterReference.TypeId.Name == "Spotfire.CheckBoxHierarchyFilter":
			#print fh.FilterReference.TypeId.Name
			if (fh.FilterReference.TypeId == FilterTypeIdentifiers.CheckBoxFilter):
				cbFilter = fh.FilterReference.As[filters.CheckBoxFilter]()
				for checkedValues in cbFilter.Values:
						#print fh.FilterReference.TypeId.Name
						cbFilter.Uncheck(checkedValues) 
						cbFilter.IncludeEmpty = False 
			if (fh.FilterReference.TypeId.Name == "Spotfire.CheckBoxHierarchyFilter"):
						fh.FilterReference.As[filters.CheckBoxHierarchyFilter]().UncheckAllNodes()