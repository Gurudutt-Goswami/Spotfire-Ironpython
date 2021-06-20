# Spotfire-Ironpython
This repository contains only Ironpython scripts that one can use in Spotfire to meet some basic features  


### Reset Zoom Sliders
```
from Spotfire.Dxp.Application.Visuals import *
for vis in Application.Document.ActivePageReference.Visuals: 
  if vis.TypeId==VisualTypeIdentifiers.BarChart: #Check Viz Type like for heat Map use .HeatMap & similar for other visuals
    vis.As[VisualContent]().XAxis.ZoomRange=AxisRange.DefaultRange
    vis.As[VisualContent]().YAxis.ZoomRange=AxisRange.DefaultRange
```
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
### Clear All Filters

•	Note: If you clear all filters and selecting things one by one and no graph is changing then you have to find proper hierarchy for the columns like which column is dependent on other column and then you have to organize it as well.
•	To organize a filter, right click on filters > organize filters > check only those filters which are independent and leave the rest. A good practice is to align filter in a hierarchal way according to their dependencies.
