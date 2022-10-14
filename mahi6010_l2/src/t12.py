"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-09-24"
-------------------------------------------------------
"""

# receive input from user
time = int(input("Number of seconds: "))

# calculate hours, days, minutes, and seconds
S_P_H = 3600
S_P_M = 60
DAY = int(time // (24 S* S_P_H))
time = time % (24 * S_P_H)
HOUR = int(time // S_P_H)
time %= S_P_H
MINUTES = int(time // S_P_M)
time %= S_P_M
SECONDS = int(time)

# print final time
print("Days: ", DAY, ", Hours: ", HOUR,
      ", Minutes: ", MINUTES, ", Seconds: ", SECONDS)
