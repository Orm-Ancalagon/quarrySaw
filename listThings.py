measurement = input("enter measurement ")
traveltime = input("enter traveltime ")
passes = input("enter passes ")

#things = [str(measurement), str(traveltime), str(passes)]

def print_row(measurement, traveltime, passes):
	print(" %-45s %-30s %15s " % (measurement, traveltime, passes))

print_row("Measurement /mm", "Travel-time /s", "Number of Passes")
print_row(measurement, traveltime, passes)

#print (str(measurement) + "mm\n".ljust(8), str(traveltime).ljust(8) + "s\n", str(passes)+"passes".ljust(8))
