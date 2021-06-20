from Spotfire.Dxp.Application.Visuals import *
for vis in Application.Document.ActivePageReference.Visuals: 
  if vis.TypeId==VisualTypeIdentifiers.BarChart: #Check Viz Type like for heat Map use .HeatMap & similar for other visuals
    vis.As[VisualContent]().XAxis.ZoomRange=AxisRange.DefaultRange
    vis.As[VisualContent]().YAxis.ZoomRange=AxisRange.DefaultRange