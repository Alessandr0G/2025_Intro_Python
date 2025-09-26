
## Part 1

import math
# Hints: Please don't remove the \n that your TA carefully put in the code!
with open("ans.txt", 'w', encoding="utf-8") as fhandler:
  fhandler.write('This is my first I/O exercise.\n')

with open("ans.txt", 'r+', encoding="utf-8") as fhandler:
  print(fhandler.readlines())
  # Your TA would like accuracy to the fourth decimal here.
  firstline = f'I just remembered that pi is approximately {math.pi:.4f}\n'
  secondline = 'Writing this to this file\n'
  thirdline = 'is a piece of cake!\n'
  fhandler.writelines([firstline,secondline,thirdline])
  # Go to the beginning of file
  fhandler.seek(0)
  # Print the content of file
  print(fhandler.readlines())


  ## Part 2
import pooch
import csv
import urllib.request
import numpy as np
import pandas as pd

datafile = pooch.retrieve(
  'https://unils-my.sharepoint.com/:u:/g/personal/tom_beucler_unil_ch/Eb_v5lBG8RZMpMAeBaNBOmwBZ3s2H5rZW1vXpbY_ggP04w?download=1',
  known_hash='718ee1f243a912187e2cdcee0200b778c02cc39c24acd5ff212be01a5b9fd6ab',
  processor=pooch.Unzip()
)[0]

row = [] # Initializes row to an empty list
with open(datafile, 'r') as fh:
  reader = csv.reader(fh)
  for info in reader:
    row.append(info)

def output_monthindices(month=None):
  """
  This function takes a string "month" as input (e.g., January)
  and outputs the first and last indices of that month
  """
  test = [rowobj[1].split('.')[1] for rowobj in row[1:]]
  truefalse = []
  for obj in test:
    if obj==month:
      truefalse.append(obj)
    else:
      truefalse.append(np.nan)
  return pd.Series(truefalse).first_valid_index(),pd.Series(truefalse).last_valid_index()

# Here, we output the first and last indices of Jan/Feb/Mar
Jan_index = output_monthindices(month='01')
Feb_index = output_monthindices(month='02')
Mar_index = output_monthindices(month='03')

# print(Jan_index, Feb_index, Mar_index)

savefile = ["jan.csv","feb.csv","mar.csv"] # List containing the filenames
indices = [Jan_index, Feb_index, Mar_index]
for i in range(len(indices)):
  with open(savefile[i], 'w') as fh:
    writer = csv.writer(fh)
    for rows in range(indices[i][0],indices[i][1]):
      writer.writerow(row[rows])

#@title Let's print the dates in March
for i in range(len(savefile)):
  df = pd.read_csv(savefile[i]) # Reads the file using pandas
  print("Here we have the head data of month", i+1, ":", df.head(i))

