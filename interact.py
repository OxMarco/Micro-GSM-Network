#!/usr/bin/env python
import sqlite3

HLR_DATABASE = "hlr.sqlite3"
db = sqlite3.connect(HLR_DATABASE)
c = db.cursor()
c.execute("SELECT * FROM Subscriber")

print ("ID\t\tcreated\t\tIMSI\t\t\tTMSI\t\textension\n")
while 1:
    subscriber = c.fetchone()
    if not subscriber:
        break
    print ("ID");
    print (subscriber[0]);
    print ("created");
    print (subscriber[1]);
    print ("IMSI");
    print (subscriber[3]);
    print ("TMSI");
    print (subscriber[7]);
    print ("extension");
    print (subscriber[5]); 

db.close()
