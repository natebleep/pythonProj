
from urllib.request import urlretrieve 
import os.path
 
URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'
result = os.path.isfile('local_copy.log')

def main():

    if result == False:
        local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)
    
    fh = open(LOCAL_FILE)
    for line in fh:
        element = line.split(' ')
        m = element[3]
        m = m[1:]
        m = m.split(':')
        m = m[0]
        print(m)



if __name__ == "__main__":
    main()