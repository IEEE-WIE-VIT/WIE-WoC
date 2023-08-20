Intensity = float(input("Enter the intensity of Light : "))
if (Intensity > 50 and Intensity <= 100):
    print("Classification : Brightest")
elif (Intensity > 25 and Intensity <= 50):
    print("Classification : Dark")
elif (Intensity >=0 and Intensity <= 25):
    print("Classification : Light")
else:
    print("The intensity of light should lie between 0 and 100")
