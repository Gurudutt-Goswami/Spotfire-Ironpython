#Replace "Hierarchy" with your hierarchy column name

import Spotfire.Dxp.Application.Filters as filters
import Spotfire.Dxp.Application.Filters.ListBoxFilter
from Spotfire.Dxp.Application.Filters import FilterTypeIdentifiers
from Spotfire.Dxp.Data import DataPropertyClass
from System import String
myPanel = Document.ActivePageReference.FilterPanel
myFilter= myPanel.TableGroups[0].GetFilter("Hierarchy")
lbFilter = myFilter.FilterReference.As[filters.CheckBoxHierarchyFilter]()
lbFilter.Reset()
