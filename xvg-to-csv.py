import  re
import string
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-xvg",help="location/to/xvgFile/Name.xvg [default: test.xvg]", default="test.xvg")
parser.add_argument("-csv",help="location/to/save/csvFile/Name.csv [optional, default: xvg file location]", default="nofile")
parser.add_argument("-d",help="digits after decimal point [optional, default: 7]", default=7)
options = parser.parse_args()

#Reading for the header
with open(options.xvg,'r') as f:
   pattern1=re.compile(r'xaxis  label "(.*)"')
   metadata1=pattern1.findall(f.read())
with open(options.xvg,'r') as f:
   pattern2=re.compile(r'yaxis  label "(.*)"')
   metadata2=pattern2.findall(f.read())

# getting the metadatas
meta1 =""
meta2=""
for i in metadata1:
    meta1 += i
for i in metadata2:
    meta2 += i
meta1 = meta1.replace(" ","")
meta2 = meta2.replace(" ","")
header= f'{meta1},{meta2}'
print("columns : %s"%(header))

#Reading XVG data
gen = (r for r in open(options.xvg) if not r[0] in ('@', '#'))
data = np.genfromtxt(gen, delimiter='')

# preparing csv file.
fileName= options.csv
csvFile = fileName
if fileName == 'nofile':
    fileName=options.xvg.split(".")
    fileName = ".".join(fileName[0:-1])
    csvFile = fileName+'.csv'

print(f"writing with {options.d} digits after decimal point")
#Writing CSV
with open(csvFile, 'w') as f:
   f.write("%s\n"%(header))
   np.savetxt(f, data,  fmt=f"%.{options.d}f", delimiter=',')
f.close()
print("DONE --> csv location: "+csvFile)
print("for more options give -h flag")
