import csv
filename1=input("Enter the CSV file name(with.csv extension):")
with open(filename1,'r') as csvfile:
    csvreader=csv.QUOTE_STRINGSader(csvfile)
    for row in csvreader:
        print(row)
