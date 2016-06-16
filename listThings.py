measurement = input("enter measurement ")
traveltime = input("enter traveltime ")
passes = input("enter passes ")

things = [str(measurement), str(traveltime), str(passes)]
for somevariable in things:
	print (somevariable)

#print (str(measurement) + "mm\n".ljust(8), str(traveltime).ljust(8) + "s\n", str(passes)+"passes".ljust(8))
