import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import sys

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

pp.pprint(data)

#row=["Michigan","Is","Awesome"]
# x = raw_input('What is your name?')
# print x

row = [sys.argv[1],sys.argv[2],sys.argv[3]]

sheet.insert_row(row,2)

print(sheet.row_count)

