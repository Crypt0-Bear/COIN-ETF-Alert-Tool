
from bs4 import BeautifulSoup
import time

import requests


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

def getLatest():
    url = "https://www.sec.gov/rules/sro/batsbzx.htm"

    r  = requests.get(url)

    data = r.text



    soup = BeautifulSoup(data, "html5lib")


    myTable = soup.findAll("table", { "class" : "mainlist" })

    all_details = myTable[1].find_all('tr')

    rule_name = all_details[3]
    rule_details = all_details[4]
    rule_details = all_details[4].form.find_all('input')
    '''
    rule_details[0] 
    The rule change and date
    rule_details[1]
    hidden input  value Show_form
    rule_details[2]
    name="rule_path" value="/comments/bats-change-date"
    rule_details[3]
    name="file_num" value="bat-change-number" 
    rule_details[4]
    name="title" value="value"


    '''


    rule_name = rule_details[3].get("value")

    rule_info = rule_details[4].get("value")

    dict = {}

    dict['ruleName'] = rule_name
    dict['ruleInfo'] = rule_info
    return dict


def getMatch(ruleInfo):

    match1 = "immediate effectiveness"
    match2 = "bitcoin"

    match1 = match1.lower()

    s = ruleInfo.lower()
    if s.find(match1) != -1 and s.find(match2) != -1  :
        # matched
        return True
    else:
        return False






