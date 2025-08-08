import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file=pd.read_csv("C:\\Users\\USER\\Downloads\\THE World University Rankings 2016-2025.csv")
# if row file in csv then read in that format 

print(file.head(5))

print(file.isnull().sum())

print(file.dtypes)

# ratios=file["Female to Male Ratio"].dropna().str.split(":",expand=True).astype(float)
# # ratios is dataframe ->expende=true create two col

# # expand=True tells pandas to:
# # Create two new columns instead of putting the result into a single list.
# #file[['Male_Percentage', 'Female_Percentage']] =file['Male:Female Ratio'].str.split(':', expand=True).astype(float)

# split taking everything before :->it's problem that's why we use extract function with regex



# A regex is a special pattern that helps you search, match, or extract specific parts of text.
# # Basic Building Blocks of Regex

# Symbol	        Meaning	                             Example Match
# \d	            A digit (0–9)	                        3, 8, 0
# \w	     A word character (letter, digit, _)	        a, Z, 9, _
# .	       Any character except newline	                a, 1, #
# +	     One or more of the previous thing	           \d+ → 123
# *	         Zero or more	previous thing                             a* → aaa, ''
# {n}	        Exactly n times	                            \d{2} → 45
# {1,n}->it can be anything from 1 to n(include)

# ^	         Start of string	                            ^abc
# $	          End of string	                                xyz$
# []	         Set of characters	                           [aeiou]
# ()	        Capturing group (for extract)	            (\d+):(\d+) ->it is use create group/col
# \s	Whitespace	space, tab


# eg:

# want to extract numbers from a ratio like "55:45".
# ^(\d{1,3})\s*:(\d{1,3})\s* ->it will create two col->: in a regex matches the colon character itself
  
file[["female","male"]]=file["Female to Male Ratio"].astype(str).str.extract(r"(\d{1,3})\s*:\s*(\d{1,3})")
#extracting into two col that's we req two col

file["female"]=pd.to_numeric(file["female"],errors="coerce")

file["male"]=pd.to_numeric(file["male"],errors="coerce")


file["female"].fillna(file["female"].mean(),inplace=True)

file["male"].fillna(file["male"].mean(),inplace=True)

total = file["female"] + file["male"]

file["female"] = file["female"] / total
file["male"] = file["male"] / total

print(file[["male","female"]])

print(file.dtypes)

file["International Students"]=file["International Students"].str.replace("%","",regex=False)

file["International Students"]=pd.to_numeric(file["International Students"],errors="coerce")

print(file["International Students"])

file["International Students"]=file["International Students"]/100

print(file["International Students"])

file.to_excel("universityRanking.xlsx",index=False)



