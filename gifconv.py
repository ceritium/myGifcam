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
num_frame = 8       # Number of frames in Gif
gif_delay = 15      # Frame delay [ms]
rebound = True      # Create a video that loops start <=> end

print('Gifconv Ready')

try:
    while True:
        for d in os.listdir('raw'):
            print('Processing ' + d)
            for i in range(num_frame - 1):
                source = str(num_frame - i - 1) + ".jpg"
                source = source.zfill(8) # pad with zeros
                dest = str(num_frame + i) + ".jpg"
                dest = dest.zfill(8) # pad with zeros
                copyCommand = "cp raw/" + d + "/" + source + " raw/" + d + "/" + dest
                os.system(copyCommand)

            graphicsmagick = "gm convert -delay " + str(gif_delay) + " " + "raw/" + d +"/*.jpg tmp/" + d + ".gif" 
            os.system(graphicsmagick)
            os.system("mv ./tmp/" + d + ".gif ./gifs/") # cleanup source images
            os.system("rm -rf ./raw/" + d) # cleanup source images
            print('Done ' + d)

        sleep(0.05)
        

except Exception,e:
    print str(e)
