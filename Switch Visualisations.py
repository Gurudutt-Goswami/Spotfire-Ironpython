from Spotfire.Dxp.Data import * 
from Spotfire.Dxp.Application.Visuals import *

if viz.TypeId == VisualTypeIdentifiers.LineChart:
 viz.TypeId = VisualTypeIdentifiers.BarChart 
elif viz.TypeId == VisualTypeIdentifiers.PieChart:
 viz.TypeId = VisualTypeIdentifiers.BarChart