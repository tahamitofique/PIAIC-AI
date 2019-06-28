#4 Days Calculator

from datetime import datetime

startDate = input("Enter a date in (dd/mm/yy) format: ")
endDate = input("Enter a date in (dd/mm/yy) format: ")

finalstartDate = datetime.strptime(startDate,"%d/%m/%Y").date()
finalendDate = datetime.strptime(endDate,"%d/%m/%Y").date()

remainingDays = finalendDate - finalstartDate

print ("There are ", remainingDays.days, "days between ", finalstartDate," and ",finalendDate)