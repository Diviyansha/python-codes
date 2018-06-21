#!/root/Desktop/python
import commands
print "commands"
print "Press 1. Date"
print "Press 2. Calendar"
input= int(raw_input("enter choice"))
if input==1:
	print "Today's date is:",commands.getoutput('date')
elif input==2:
	print "calendar is:"	
	print commands.getoutput('cal')
else:
	print "invalid choice"
