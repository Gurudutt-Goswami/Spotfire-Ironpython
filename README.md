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
