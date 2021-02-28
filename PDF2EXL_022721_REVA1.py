##Develop by Pankaj Sharma PDF to excel coversion 
## How to extract tabular data from pdf file 

## Step 1 importing important library files 
import pandas as  pd
import tabula as tb


# Step 2 Code Sequence for coverting pdf to csv

df1= ("C:/Python37/PDF2EXL/pdf/ark2021.pdf")
output=("C:/Python37/PDF2EXL/csv/ark2021.csv")

tb.convert_into(df1, output, output_format="csv", pages="all", stream=True)
print(tb.read_pdf(df1, pages ='all'))
df1[1]




