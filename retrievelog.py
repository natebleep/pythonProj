import datetime
from urllib.request import urlretrieve 
import os.path

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'
result = os.path.isfile('local_copy.log')



requests = 0
req_year = 0

if result == False:
    local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

fh = open(LOCAL_FILE)    
# read the last line of the file
lineList = fh.readlines()
fh.close()
lastLine = lineList[len(lineList)-1]
lastDate = lastLine.split(' ')
lastDate = lastDate[3]
lastDate = lastDate[1:]
lastDate = lastDate.split(':')
lastDate = lastDate[0]
# print('Most recent: \n' + lastDate + '\n')

today = lastDate.split('/')
# print(today)

month = today[1]
datetime_object = datetime.datetime.strptime(month, "%b")
monthNum = datetime_object.month
# print(monthNum)

todayDate = datetime.date(int(today[2]),int(monthNum),int(today[0]))
# print(todayDate, '\n')

# yearAgo = 

#figure out what a 365 days ago is



fh = open(LOCAL_FILE)
for line in fh:
   
    element = line.split(' ')
    if len(element) < 10:
        continue
    m = element[3]
    m = m[1:]
    m = m.split(':')
    m = m[0]
    now = m.split('/')
    
    month = now[1]
    datetime_object = datetime.datetime.strptime(month, "%b")
    monthNum = datetime_object.month
    

    logDate = datetime.date(int(now[2]),int(monthNum),int(now[0]))
    # print(logDate)

    requests += 1
    
    dif = todayDate - logDate
    # print(dif)

    if dif.days <= 365:
        req_year += 1
        
print('Total requests: ' , requests)
print('Requests this year: ', req_year)

