# Spotfire-Ironpython
This repository contains only Ironpython scripts that one can use in Spotfire to meet some basic features  

### Switch Visualisations
```
from Spotfire.Dxp.Data import * 
from Spotfire.Dxp.Application.Visuals import *

#viz is a script parameter
if viz.TypeId == VisualTypeIdentifiers.LineChart:
 viz.TypeId = VisualTypeIdentifiers.BarChart 
elif viz.TypeId == VisualTypeIdentifiers.PieChart:
 viz.TypeId = VisualTypeIdentifiers.BarChart
```
