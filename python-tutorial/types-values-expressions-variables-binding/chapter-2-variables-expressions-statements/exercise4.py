import math
import datetime

# The volume of a sphere with radius r is 4/3 π r3. What is the volume of a sphere with radius 5? Hint: 392.6 is wrong!
print('the radius is ' + str( round( (4/3) * math.pi * 5**3, 2)))

# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

book = 24.95
book = book * .6
copies = 60
totalCost = book * copies + 3 + .75 * (copies - 1)
print('total wholesale cost is ' + str(round(totalCost, 2)) )

# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

startTime = datetime.timedelta(hours=6,minutes=52)
# print(startTime)

firstAndLastMiles = ( 8 * 60 + 15 ) * 2
next3miles = ( 7 * 60 + 12 ) * 3

totalSeconds = firstAndLastMiles + next3miles

endTime = startTime + datetime.timedelta(seconds=totalSeconds)
print('i get home for breakfast at ' + str(endTime))