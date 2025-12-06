import time
from datetime import datetime

num = time.time()
sec = "{:,.4f}".format(num)
sc = "{:.2e}".format(num)
print("Seconds since January 1, 1970: " + sec + " or " + sc +" in scientific notation")
print(datetime.now().strftime("%b %d %Y"))
