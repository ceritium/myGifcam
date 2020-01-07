from time import sleep
import time
from os import system
import os
import shutil
########################
#
# Behaviour Variables
#
########################
rebound = True      # Create a video that loops start <=> end

print('Gifconv Ready')

try:
    while True:
        for d in os.listdir('raw'):
            print('Processing ' + d)
            command = "ffmpeg -i raw/" + d + " -vf 'fps=10' -gifflags +transdiff -y tmp/" + d + ".gif"
            os.system(command)
            os.system("mv ./tmp/" + d + ".gif ./gifs/") # cleanup source images
            os.system("rm -rf ./raw/" + d) # cleanup source image
            print('Done ' + d)

        sleep(0.05)
        

except Exception,e:
    print str(e)
