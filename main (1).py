year=int(input("Enter The Year Only : ")) 
if(year%4 == 0 and year%100 != 0 ):
  print ("The {} Year is a Leap Year".format(year))
elif(year%400 == 0):
  print ("The {} Year ia a Leap Year".format(year))
else:
  print ("The {} Year is Not a Leap Year".format(year))