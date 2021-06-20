'''
Note: 
If you clear all filters and selecting things one by one and no graph is changing then you have to find proper hierarchy for the columns like which column is dependent on other column and then you have to organize it as well.
To organize a filter, right click on filters > organize filters > check only those filters which are independent and leave the rest. A good practice is to align filter in a hierarchal way according to their dependencies.
'''

from Spotfire.Dxp.Application.Visuals import VisualContent
from Spotfire.Dxp.Application import Filters as filters
from Spotfire.Dxp.Application.Filters import FilterTypeIdentifiers

# Get the filter panel on the current active page
filterPanel = Document.ActivePageReference.FilterPanel
# Perform filtering action

for tableGroup in filterPanel.TableGroups:
	for fh in tableGroup.FilterHandles:
	   
		if fh.Visible:
			print fh.FilterReference.Name
			if fh.FilterReference.TypeId.Name == "Spotfire.CheckBoxFilter" or 	fh.FilterReference.TypeId.Name == "Spotfire.CheckBoxHierarchyFilter":
		
				
					#print fh.FilterReference.TypeId.Name
					if (fh.FilterReference.TypeId == FilterTypeIdentifiers.CheckBoxFilter):
						cbFilter = fh.FilterReference.As[filters.CheckBoxFilter]()
				
					#In the following line you have write column names in place of JobID,dept,gender,location
						if fh.FilterReference.Name =="Region" or fh.FilterReference.Name =="Item":
					#print fh.FilterReference.Name 
								for checkedValues in cbFilter.Values:
										#print fh.FilterReference.TypeId.Name
									
										cbFilter.Uncheck(checkedValues) 
										cbFilter.IncludeEmpty = False 
					if (fh.FilterReference.TypeId.Name == "Spotfire.CheckBoxHierarchyFilter"):
						fh.FilterReference.As[filters.CheckBoxHierarchyFilter]().UncheckAllNodes()