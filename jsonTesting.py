import csv  
import json  
  
# Open the CSV  
f = open( 'C:\scratch\Book1.csv', 'rU' )  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "Y","X","PANEL","MARKET","description"))  
# Parse the CSV into JSON  
out = json.dumps( [ row for row in reader ] )  
print('JSON parsed!')
# Save the JSON  
f = open( 'C:\scratch\Book1.json', 'w') 
f.write(out)  
print('JSON saved!') 