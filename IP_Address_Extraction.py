from itertools import count
import re
from collections import Counter

logfile="access_log.txt"

# Below logic will extract invalid IP also
#regexp="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# Both Logics are correct
regexp2= "(?:2[0-5]{2}|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9]?)\\.(?:2[0-5]{2}|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9]?)\\.(?:2[0-5]{2}|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9]?)\\.(?:2[0-5]{2}|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9]?)"
#regexp2="(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"

with open(logfile,'r') as f:
    log=f.read()
    #print(log)
    ip_list = re.findall(regexp2,log)
    print(ip_list)
    #print(Counter(ip_list))
