import re

strk = 'results_n00_z000.bin\nresults_n00_z010.bin\nresults_n00_z020.bin\nresults_n00_z030.bin\nresults_n00_z040.bin\nresults_n00_z050.bin\nresults_n00_z060.bin\nresults_n00_z070.bin\nresults_n00_z080.bin\nresults_n00_z090.bin\nresults_n00_z100.bin\nresults_n05_z000.bin\nresults_n05_z010.bin\nresults_n05_z020.bin\nresults_n05_z030.bin\nresults_n05_z040.bin\nresults_n05_z050.bin\nresults_n05_z060.bin\nresults_n05_z070.bin\nresults_n05_z080.bin\nresults_n05_z090.bin\nresults_n05_z100.bin\nresults_n10_z000.bin\nresults_n10_z010.bin\nresults_n10_z020.bin\nresults_n10_z030.bin\nresults_n10_z040.bin\nresults_n10_z050.bin\nresults_n10_z060.bin\nresults_n10_z070.bin\nresults_n10_z080.bin\nresults_n10_z090.bin\nresults_n10_z100.bin\nresults_n15_z000.bin\nresults_n15_z010.bin\nresults_n15_z020.bin\nresults_n15_z030.bin\nresults_n15_z040.bin\nresults_n15_z050.bin\nresults_n15_z060.bin\nresults_n15_z070.bin\nresults_n15_z080.bin\nresults_n15_z090.bin\nresults_n15_z100.bin\n'

a = 0
n = 0
z = 1

all = re.findall('\d+', strk)
while a != len(all):
    print(f'({all[n]}, {all[z]})')
    a+=1
    n+=2
    z+=2