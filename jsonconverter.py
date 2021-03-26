from pyexcel_xlsx import get_data; 
import time;
import json; #imports relevant libraries. pyexcel_xlsx is used to pull data from excel sheets

data = get_data("ModernNYT.xlsx") #get_data function from pyexcel_xlsx pulls data from the excel sheet
sheetName = "ModernNYT"; #specifies the sheet in the excel workbook we are running through

data_list = []
# Iterate through each row and append in above list
for i in range(1, len(data[sheetName])):
    data_list.append({
        'clue' : str(data[sheetName][i][5]),
        'answer' : str(data[sheetName][i][6]),
        'day' : str(data[sheetName][i][7]),
        'length' : data[sheetName][i][8]
    })
data_list = {'general': data_list} # Converting to required object
j = json.dumps(data_list, indent=0)
# Write to file
with open('data1.json', 'w') as f:
    f.write(j)