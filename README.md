# Spotfire-Ironpython

1. This repository contains IronPython scripts for use within the Tibco Spotfire.
2. Also I have a seperate repository (called Spotfire-JS-Jquery) for some basic UI designs in Spotfire TextArea along with codes & screenshots.
3. For more information regarding other services for extending Spotfire capabilities, please refer the Spotfire Technology Network: http://stn.spotfire.com

### Some Important Links

   1. [Ironpython Scripts Collection](https://community.tibco.com/wiki/ironpython-scripting-tibco-spotfire)
   2. <https://spotfired.blogspot.com/>


### This Repository Contains following scripts:
      1. Clear All hierarchy columns.py
      2. Clear a particular column.py
      3. Clear multiple columns.py
      4. Export Table from active visualisation.py
      5. Find max value of a column.py
      6. Get all values of a column.py
      7. Get distinct values of columns.py
      8. Hide Filter based on Document Property value.py
      9. Open Directory.py
      10. Reading from a file.py
      11. Reset Zoom Sliders.py
      12. Select all for a Hierarchy Column.py
      13. Select all for a particular column.py
      14. Send Mail.py
      15. Show Ironpython output in a label.py
      16. Switch Visualisations.py
      17. Write Back to Database.py
      18. Write to a file.py
      19. Yes-No MsgBox.py
      
### Other Basic Things
1. ##### Go to Specific Page 
   Document.ActivePageReference = Document.Pages[2]
2. ##### Get Current Username
````
   from System.Threading import Thread 
   print Thread.CurrentPrincipal.Identity.Name 
````
3. ##### Loop Through Pages
````
   for page in Application.Document.Pages:
   print page.Title
````
4. ##### Use document property directly inside a calculated column to make wild card search on an input field eg.
````
case when Upper([City]) ~= Upper("${wildcard}") then "Y" else "N" end
````
5. ##### When you have blank values due to multiple blank lines in Spotfire & thus Spotfire not considering them as NULL
![Concept](https://user-images.githubusercontent.com/86184439/126883875-8b48a0dc-d7c5-4041-8c0c-adfddcc0ed69.PNG)

