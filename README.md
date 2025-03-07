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
      20. Tags for Search on Graphs (ie., Document Property) which will work on Graph
         1.Go to “View > tag” named “New Tag Collection” to “Result” and with in it make two tag “Yes” and “No”.
         2.	Add attached Iron python in document properties > scripts > iron python.
            (Note:Do not forget to add script parameter ”myTable” as Data Table.Name this script as search_python)
         3. Add a textarea and in that , add an input field (string) as “search” and link above iron python created script to that.
         4.	To change a graph acc to search just go to that graph right click > “properties > data > limit data using expression” and write “Result=”Yes” ”.

      
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
5. ##### Want to subtract a single day using ironpython. 
   ##### Note : You can also write following code in single line, this is just for ease of understanding.
````
   a = Document.Properties['StartDate']
   a = a.AddDays(-1)
   Document.Properties['StartDateNew'] = a 
````
6. ##### When you have blank values due to multiple blank lines in Spotfire & thus Spotfire not considering them as NULL
![Concept](https://user-images.githubusercontent.com/86184439/126883875-8b48a0dc-d7c5-4041-8c0c-adfddcc0ed69.PNG)

7. ##### Get Max value of range filter in document property
````
1. Make a string input document property in textarea area & name its div as "uid"

<span id="uid">
Spotfire Id control of string input document property
</span>

2. Write following javascript in the same textarea area to update step 1 document property with date. 
Note the DOMsubtreemodified function is to make sure everytime when something changes in 'fun' section this js runs 

         $("#fun").on("DOMSubtreeModified",function(){

         var d = new Date().getTime()/1000;
         $("#uid input").val(d).blur();
         function value()
         {
            var d = new Date().getTime()/1000;
            $("#uid input").val(d).blur();
         }
         })

3. On the change/set of this date input field call following ironpython script. 
Note testdata is going to be your datatable & id is going to be your column name.

activeFilteringSelection = Document.ActiveFilteringSelectionReference.GetSelection(testdata).AsIndexSet()
column = testdata.Columns["Id"]
max = column.RowValues.GetMaxValue(activeFilteringSelection).ValidValue
#print max
Document.Properties["maxvalue"]=str(max)

````
8. ##### Searching the library
```https://docs.tibco.com/pub/spotfire/7.0.1/doc/html/lib/lib_searching_the_library.htm```


9. ##### lead/lag/intersect function in spotfire
```https://stackoverflow.com/questions/47165178/lag-lead-using-spotfire-custom-expression```

