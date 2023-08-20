math = float(input("Enter your math grade :"))
science = float(input("Enter your science grade :"))
history = float(input("Enter your history grade :"))
english = float(input("Enter your english grade :"))
if (math>100 or math<0):
    print ("Math not a valid grade")
if (history>100 or history<0):
    print (" History not a valid grade")
if (science>100 or science<0):
    print ("Science not a valid grade")
if (english>100 or english<0):
    print ("English not a valid grade")
avg = (math+history+science+english)/4
if (avg>=90 and avg<=100):
    print("Your final grade is A")

elif (avg>=80 and avg<=90):
    print("Your final grade is B")
elif (avg>=70 and avg<=80):
    print("Your final grade is C")
elif (avg>=60 and avg<=70):
    print("Your final grade is D")
elif(avg<60):
    print("Your final grade is F")
else:
    print("Couldn't calculate grade")
