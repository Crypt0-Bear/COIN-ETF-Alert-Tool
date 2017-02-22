from btcEtf import *
'''

   ___               _    __      ___              
  / __|_ _ _  _ _ __| |_ /  \ ___| _ )___ __ _ _ _ 
 | (__| '_| || | '_ |  _| () |___| _ / -_/ _` | '_|
  \___|_|  \_, | .__/\__|\__/    |___\___\__,_|_|  
  ___ _____|__/|_|  _   _         _                
 | __|_   _| __|   /_\ | |___ _ _| |_              
 | _|  | | | _|   / _ \| / -_| '_|  _|             
 |___|_|_|_|_|___/_/ \_|_\___|_|  \__|             
 |_   _/ _ \ / _ \| |                              
   | || (_) | (_) | |__                            
   |_| \___/ \___/|____|                           
   
'''


while True:
    results = getLatest()
    ruleName = results["ruleName"]
    ruleInfo = results["ruleInfo"]
    approved = getMatch(ruleInfo)


    if approved == True:
        #logic if approved 
        print ""
        print "Approved"
        print "Rule Name: " + ruleName
        print "Rule Change: " + ruleInfo
        print ""
        print "Bitcoin to the Moon!"
        print ""
        print ""
        break
    else:
        #logic if no new news
        print "Not Yet"

    #wait 30 seconds then try again
    time.sleep(30)




