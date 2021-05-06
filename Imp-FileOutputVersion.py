import re #Regex
import os #for getting username
import datetime #get datestamp
from pathlib import Path #for seeing if file exists or not
import sys #for exit
##Random Test IP:     221.241.59.100


regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"


def check(Ip): ##see if IP is valid using Regex
    if(re.search(regex, Ip)):
        pass ##no need to do anything if IP is valid
    else:
        f.close() #close file stream
        sys.exit("Invalid Ip address")
        
        
def Printfunc(IP):
    print("\n" + "IP: "  + IP) 
    f =open(filepath,"a")
    f.write("\n" + "IP: "  + IP + "\n")
    f.close()

        
        
def PrintAndAppend(stringtoappend):
    print(stringtoappend)
    f =open(filepath,"a")
    f.write(stringtoappend +"\n")
    f.close()
    
    
def GetBrowserAndCountry():
    Browser = input("what is browser?   ").lower()
    
    ######################Clean up shorthand############################### probably a better way to do this using regex#############
    if Browser.__contains__("chr") and not Browser.__contains__("chrome"):
        Browser = (Browser.replace("chr","Chrome"))
        
    if Browser.__contains__("chrome"):
        Browser = (Browser.replace("chrome","Chrome"))  # i should probably just use regex to search for "/"
        
    if Browser.__contains__("ff") and not Browser.__contains__("ffox"):
        Browser = (Browser.replace("ff","Firefox"))
       
    if Browser.__contains__("ffox") and not Browser.__contains__("Firefox"):   
        Browser = (Browser.replace("ffox","Firefox"))
       
    if Browser.__contains__("firefox"):   
        Browser = (Browser.replace("firefox","Firefox"))

    if Browser.__contains__("saf") and not Browser.__contains__("safari"):
        Browser = (Browser.replace("saf","Safari"))
        
    if Browser.__contains__("safari"):
        Browser =(Browser.replace("safari","Safari"))
        
    if Browser.__contains__("edg") and not Browser.__contains__("edge"):
        Browser = (Browser.replace("edg", "Edge"))
    
    if Browser.__contains__("edge"):
        Browser = (Browser.replace("edge", "Edge"))
        
    if Browser.__contains__("opera"):
        Browser = (Browser.replace("opera", "Opera"))
        
    Country =input ("what is country?   ").upper()
    
    return (Browser), Country 
#####################################################################################################################################################    


###########Create New file or check if one exists################

date =  datetime.datetime.now().strftime("%d-%m-%y")
#print("Todays Date: " + date)
##path C:\Users\JayK\Desktop
filepath = os.path.join("C:\\Users\\" + os.getlogin() + "\\Desktop","Imperva - " + date + ".txt") ##get user name 

##Syntax:  os.path.join(dir_name, base_filename + "." + filename_suffix)

print("Your File path is: " + filepath)



#see if file exists, if it doesn't then make one.        
if Path(filepath).is_file(): 
    print ("File exist")
    f =open(filepath,"a") #by default it is text not binary
else:
    print ("File does not exist...creating one now")
    f =open(filepath, "x")#for a new file. if file already exists then to append use


##########################Body################## 
while True: ##run infinitely until session timeout
    IP = (input("IP address: ?  "))
    check(IP)
    Error_type = (input("Error_type ?  ").lower())

    if Error_type == "ns" or Error_type == "not seen":
        Printfunc(IP)
        string_to_append  = ("\n" + "We can confirm that no traffic is seen on the Imperva portal for the IP provided.")
        PrintAndAppend(string_to_append)
    
    elif Error_type == "seen" or Error_type == "allowed":
        Printfunc(IP)
        string_allowed = ("\n" + "We can confirm that traffic for the IP provided is seen on the Imperva portal and is allowed.")
        PrintAndAppend(string_allowed)

    elif Error_type.__contains__("inv") or Error_type ==  "cookie" or Error_type == "javascript" or Error_type == "js":
        Browser, Country = GetBrowserAndCountry()
        Printfunc(IP)
        
        ##Browser
        browserString = ("Browser: " + Browser) 
        PrintAndAppend(browserString)
        
       ##Country
        CountryString = "Country: "+ Country + "\n"
        PrintAndAppend(CountryString)
        
        
        BlockedString  =  "We can confirm that traffic for the IP provided is currently blocked due to a Javascript or Browser cookie issue."
        PrintAndAppend(BlockedString)
    
    elif Error_type.__contains__("kv") or Error_type.__contains__("vpn") or Error_type.__contains__("host"):
        
        Browser, Country = GetBrowserAndCountry()
        Geo = input("what is geo?   ")
        Printfunc(IP)
        PrintAndAppend("Browser: " + Browser)
        PrintAndAppend("Country: "+ Country)
        PrintAndAppend("Geo Org: " + Geo  +"\n")
        PrintAndAppend("We can confirm the IP provided is currently being blocked due to a VPN or a hosted environment.")
     
    else:
        print("incorrect option \n Options are: \n NS for Not seen \n seen \n inv/cookie/javascript/js \n kv/vpn/host ")
        
    PrintAndAppend("\n------------------------------------------------------------------------------------------------------------------") ##seperator   
    
    ##there is a much better way to copy across std.out and file output, but zzzzzzzzzzzzzzzzzz### 
