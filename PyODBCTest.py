## Test script for PyODBC

import pyodbc

cnxn = pyodbc.connect(r'Driver={SQL Server};Server=.\SQLEXPRESS;Database=HamsterDB2;Trusted_Connection=yes;')
cursor = cnxn.cursor()
cursor.execute("SELECT HamsterName FROM Hamsters")
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print (row.HamsterName)

##cursor.execute("exec FindAllHamsters")
##while 1:
##    row = cursor.fetchone()
##    if not row:
##        break
##    thePrintString = row.HamsterID + ", " + row.HamsterName + ", " + row.Species
##    print(thePrintString)
##
##cursor.execute("exec FindAHamster 'Ski'")
##
##while 1:
##    row = cursor.fetchone()
##    if not row:
##        break
##    print(" The following hamster has been found:")
##    thePrintString = row.HamsterID + ", " + row.HamsterName + ", " + row.Species
##    print(thePrintString)
##    
##cnxn.close()
