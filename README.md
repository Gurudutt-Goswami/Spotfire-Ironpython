# Spotfire-Ironpython
This repository contains only Ironpython scripts that one can use in Spotfire to meet some basic features  

# Switch Visualisations
'''
from Spotfire.Dxp.Data import * 
from Spotfire.Dxp.Application.Visuals import *

if viz.TypeId == VisualTypeIdentifiers.LineChart:
 viz.TypeId = VisualTypeIdentifiers.BarChart 
elif viz.TypeId == VisualTypeIdentifiers.PieChart:
 viz.TypeId = VisualTypeIdentifiers.BarChart

'''
### Change URL Collaboration Panel
```
import clr
clr.AddReference ( "System" )
import System
from System import Uri
import Spotfire.Dxp.Application
for panel in Application.Document.ActivePageReference.Panels:
 if panel.Title == "Collaboration":
  panel.Url = Uri ( "http://www.google.com" )
```
