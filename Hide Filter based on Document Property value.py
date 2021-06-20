#justchecking is document property name & anupam is it's value 
#Region is the column which you want to hide/show
from Spotfire.Dxp.Application.Filters import *
from Spotfire.Dxp.Application import PanelTypeIdentifiers
 
filterPanel = Document.ActivePageReference.FilterPanel
if Document.Properties["justchecking"] == "anupam":
	for tableGroup in filterPanel.TableGroups:
		for fh in tableGroup.FilterHandles:
			if fh.Visible:
				if fh.FilterReference.Name =="Region":
					fh.Visible = False
else:
	for tableGroup in filterPanel.TableGroups:
		for fh in tableGroup.FilterHandles:
				if fh.FilterReference.Name =="Region":
					fh.Visible = True
