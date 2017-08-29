import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import sys
import time

print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])


scope=['https://spreadsheets.google.com/feeds']
creds=ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client=gspread.authorize(creds)

sheet = client.open('database').sheet1

pp = pprint.PrettyPrinter()
# data = sheet.get_all_records()
data = sheet.cell(1,1).value
data = sheet.col_values(1)

pp.pprint(data)

var = raw_input("Enter an entry to database ")

#var= "testing this function"
testVar= [] 
testVar= var.split()

print "Current date "  + time.strftime("%x")
 
## Only time representation
print "Current time " + time.strftime("%X")
print (testVar[0]+","+testVar[1])
#row=["Michigan","Is","Awesome"]
#x = raw_input('Input row data')
#print x[1]

row = [sys.argv[1],sys.argv[2],sys.argv[3],time.strftime("%x"),time.strftime("%X")]

sheet.insert_row(row,2)

row = sheet.col_values(1)

print(row)

