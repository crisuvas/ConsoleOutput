from datetime import datetime
now = datetime.now()
print("%02d-%02d-%04d" % (now.day, now.month, now.year))
