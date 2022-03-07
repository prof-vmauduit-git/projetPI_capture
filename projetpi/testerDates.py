#!/usr/bin/env python
# scipt  testerDates.py

#### import librairie pour date et time
from datetime import datetime

ladate = datetime.now()

#print "ladate : %s %s" % ladate.strftime("%x") % ladate.strftime("%X")
#print "ladate : %s" % ladate.strftime("%x")
print ("ladate : " + ladate.strftime("%x") + " " + ladate.strftime("%X"))


