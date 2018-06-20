import commands
print "finding ip please wait.."
ip= commands.getoutput("arp -a|cut -d'(' -f2| cut -d')' -f1")
print ip
