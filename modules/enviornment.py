import os
def run(**args):
    print "[*] in enviornment module"
    return str(os.environ)

#print run()