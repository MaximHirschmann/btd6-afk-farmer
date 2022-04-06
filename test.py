from calendar import monthcalendar
from time import time, sleep

money_earned = 74
t0 = time()

sleep(5)

print(("ROUND " + str(5)).ljust(30))
print("TIME PASSED:".ljust(30), end = "")
print(round(time() - t0, 2), "s", sep="")
print("MONKEY MONEY EARNED:".ljust(30), end = "")
print(money_earned, "$", sep="")