import sys
import math


def usage():

	print " Syntax: "
	print "$ python sport-tracker-union.py  file_one.gpx file_two.gpx  "

if len(sys.argv)<3:
	usage()
	exit()

find_word = False

in_file = open(sys.argv[1],"r")
print "Leggo file: " + str(in_file)
exp = in_file.read()
in_file.close()

in_file1 = open(sys.argv[2],"r")
print "Leggo file: " + str(in_file1)
exp1 = in_file1.read()
in_file1.close()

a= exp.split("\n")
b= exp1.split("\n")

km_to_add = 0

out_file = open("route.gpx","w")

for out in a:

	if (int(out.find("</trkseg>"))!= -1):
		#print "entro break"
		break
	else:
	   	
		find_km = out.split(" ")
				
		for i in range (len(find_km)):
			#print find_km[i]
			
			if (find_km[i].find("Distance") != -1):
				#print find_km[i+1]
				km_to_add = float(find_km[i+1])
			
		out_file.write(out+"\n")
		
		
		#print "Km to Add: " + str(km_to_add)

for string in b :
	
	if (string.find("trkpt") != -1) or find_word:

		find_word = True
		
		find_km = string.split()
		
		for i in range (len(find_km)):
			#print find_km[i]
			
			if (find_km[i].find("Distance") != -1):
			
		
				distance=float( find_km[i+1]) 
				new_distance = distance + km_to_add
				#print str(new_distance)	
				
				
				
				stringa_new= string[0:string.find("Distance ")-1] + " Distance " + str(new_distance) + " km</desc>"+"\n"
			
				#print stringa_new
				out_file.write(stringa_new)
		else:
			out_file.write(string+"\n")

out_file.close()













