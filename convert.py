# Python code to convert a csv file to a xml file.
# Software Engineering I
# Assignment 1b
# Hunter Eason
# Due: 9/18/2017
         
import sys
import csv
         
def readCSV(filename):
        try:
                csvdata = open(filename, 'r')
        except:
                print "File not found. Did you name your file correctly?"

        items = [lines.strip().split(',') for lines in csvdata]
        return items

# Function to convert CSV to XML.
def csv2xml(items):
        csvfile = sys.argv[1]
        xmlfile = sys.argv[2]
        xmldata = open(xmlfile,'w')

        #Write XML version and encoding
        xmldata.write('<?xml version="1.0" encoding="UTF-8"?>' + '\n')
        xmldata.write('<Department>' + "\n")
        i=1
	j=0
	count = 0
        with open(csvfile,'r') as q:
                for line in q:
                        count = count + 1
#        for row in items:
 #               xmldata.write('\t' + '<Record>' + '\n')
#		for index, column in enumerate(row):
#			xmldata.write(l[index]+column+'</StudentID>\n');
#                xmldata.write('\t' + '</Record>' + '\n')
        print 'Count is: ',count
	for x in range(1,count):
                xmldata.write('\t' + '<Record>' + '\n')
                xmldata.write('\n' + '\t\t' + '<StudentID>' + items[i][0] + '</StudentID>' + '\n')
                xmldata.write('\t\t' + '<FirstName>' + items[i][1] + '</FirstName>' + '\n')
                xmldata.write('\t\t' + '<LastName>' + items[i][2] + '</LastName>' + '\n')
                
                xmldata.write('\t' + '</Record>' + '\n')
		print i, j
		i+=1
	
        xmldata.write('</Department>')






#Main function
#Includes and calls functions
def main():
        items = readCSV(sys.argv[1])
        csv2xml(items)
        print "Finished!!"

if __name__ == '__main__':
        main()
