#!/root/Desktop/python
import os
#creating menu
print "press 1 To check current date and time."
print "press 2 To create a file."
print "press 3 To create a directory."
print "press 4 To search something on google."
print "press 5 Logout your system."
print "press 6 Shut down your OS."
print "press 7 To check internet connection."
print "press 8 To login on whatsapp on browser."
print "press 9 To check all connected IP in your network."
#entering the choice
choice = raw_input("enter choice")
#applying conditions

if int(choice)==1 :
	os.system('date')
elif int(choice)==2 :
	name = raw_input("enter name of the file")
	os.system('touch name.txt')
elif int(choice)==3 :
	name = raw_input("enter name of the directory")
	os.system('mkdir name')
elif int(choice)==4 :
	toSearch = raw_input("enter keywords to search on google")
	webbrowser.open_new_tab("https://www.google.com/search?q="+toSearch)
elif int(choice)==5 :
	os.system('pkil - KILL u root')
elif int(choice)==6:
	os.system('shutdown -h now')

elif int(choice)==7 :
	os.system('netstat')
elif int(choice)==8 :
	os.system('firefox web.whatsapp.com')
elif int(choice)==9 :
	os.system('ifconfig')
else :
	print"invalid choice"


	
	

