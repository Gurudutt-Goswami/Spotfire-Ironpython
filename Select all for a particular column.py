#Just replace Location with your column Name

import Spotfire.Dxp.Application.Filters as filters
import Spotfire.Dxp.Application.Filters.ListBoxFilter
from Spotfire.Dxp.Application.Filters import FilterTypeIdentifiers
from Spotfire.Dxp.Data import DataPropertyClass
from System import String
myPanel = Document.ActivePageReference.FilterPanel
myFilter= myPanel.TableGroups[0].GetFilter("Location")
lbFilter = myFilter.FilterReference.As[filters.CheckBoxFilter]()
lbFilter.Reset()
