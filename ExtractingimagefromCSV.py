import csv
import urllib.request
#
with open('datasetCSV.csv', 'r') as csvFile: # reading the CSV File
    reader = csv.reader(csvFile)
    data3 =[x[0] for x in csv.reader(csvFile)]
    if data3[0] == 'content':
        data3.remove('content')
        data4 =data3

def dl_jpeg(url,text):
    full_path = 'Extracted_Image/' + text + '.jpg' #path of the file to download
    urllib.request.urlretrieve(url, full_path)

for x in range(len(data4)):
    text = 'sample' + str(x) #Extracts images with sample0 to the length  of the data
    dl_jpeg(data4[x],text)