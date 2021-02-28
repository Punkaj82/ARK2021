##Develop by Pankaj Sharma PDF to excel coversion for tables
##import numpy as np
##import pandas as  pd
import tabula as tb
import tabula

## tb.environment_info()


#Code Sequence for coverting pdf to csv

df1= ("C:/Python37/PDF2EXL/pdf/ark2021.pdf")
output=("C:/Python37/PDF2EXL/csv/ark2021.csv")



tb.convert_into(df1, output, output_format="csv", pages="all", stream=True)
print(tb.read_pdf(df1, pages ='all'))
df1[1]




