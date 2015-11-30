## Test script for PyODBC
print("arcpy")
import arcpy
arcpy.AddMessage("os")
print("OS")
import os
arcpy.AddMessage("Datetime")
print("DateTime")
import datetime
print("pyodbc")
arcpy.AddMessage("Importing pyodbc")
import pyodbc

##theHamName = arcpy.GetParameterAsText(0)
##
##arcpy.AddMessage("Connecting to database")
##cnxn = pyodbc.connect(r'Driver={SQL Server};Server=.\SQLEXPRESS;Database=HamsterDB;Trusted_Connection=yes;')
##cursor = cnxn.cursor()
##arcpy.AddMessage("Getting all hamsters")
##cursor.execute("SELECT HamsterName FROM Hamsters")
##while 1:
##    row = cursor.fetchone()
##    if not row:
##        break
##    arcpy.AddMessage("Hamster name found : " + row.HamsterName)
##
##arcpy.AddMessage("Getting hamster details")
##cursor.execute("exec FindAllHamsters")
##while 1:
##    row = cursor.fetchone()
##    if not row:
##        break
##    thePrintString = "Hamster details: " + row.HamsterID + ", " + row.HamsterName + ", " + row.Species
##    arcpy.AddMessage(thePrintString)
##
##arcpy.AddMessage("Looking for hamster name starting with " + theHamName)
##cursor.execute("exec FindAHamster " + theHamName)
##while 1:
##    row = cursor.fetchone()
##    if not row:
##        break
##    arcpy.AddMessage(" The following hamster has been found:")
##    thePrintString = row.HamsterID + ", " + row.HamsterName + ", " + row.Species
##    arcpy.AddMessage(thePrintString)
##    
##cnxn.close()
