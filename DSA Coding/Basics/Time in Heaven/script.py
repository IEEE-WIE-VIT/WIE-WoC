time_12 = input()
time_24 = ""
time_8 = ""

# 12-hour to 24-hour conversion
if time_12[8:] == " A.M":
    if time_12[0:2] == "12":
        time_24 = "00" + time_12[2:8]
    else:
        time_24 = time_12[0:8]
elif time_12[8:] == " P.M":
    if time_12[0:2] == "12":
        time_24 = time_12[0:8]
    else:
        time_24 = str(int(time_12[0:2])+12) + time_12[2:8]
elif time_12 == "12:00:00 midnight":
    time_24 = "00:00:00"

# 24-hour to 8-hour conversion hh:mm:ss
if time_24 == "00:00:00":
    time_8 = "08:00:00 midnight"
elif 0 <= int(time_24[0:2]) <= 7:
    time_8 = time_24 + " A.M"
elif time_24 == "08:00:00":
    time_8 = "08:00:00 midmorning"
elif 8 <= int(time_24[0:2]) <= 15:
    time_8 = "0" + str(int(time_12[0:2])-8) + time_24[2:8] + " B.M"
elif time_24 == "16:00:00":
    time_8 = "08:00:00 midevening"
elif 16 <= int(time_24[0:2]) <= 23:
    time_8 = "0" + str(int(time_24[0:2])-16) + time_24[2:8] + " C.M"
print(time_8)
