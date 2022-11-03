import pandas as pd
import sys
import pyarrow as pyarrow
import fastparquet as fastparquet
from os import path, listdir, mkdir
import shutil

InDirName = sys.argv[1]
OutDirName = sys.argv[2]

#create folder -> parquet split in 1 Gb
try:
    mkdir(OutDirName)
except:
    shutil.rmtree(OutDirName)
    mkdir(OutDirName)

# navigate in folder and retieve only table of interest
l_files_download = listdir(InDirName)
for file_download in l_files_download:
    if path.isdir("%s/%s/"%(InDirName, file_download)):
        l_files_sub = listdir("%s/%s"%(InDirName, file_download))
        for file_sub in l_files_sub:
            if file_sub == "cpcat_chemicals.txt" or file_sub == "cpcat_index_output.txt" or file_sub == "products.txt":
                
                # skip error rows
                df = pd.read_csv("%s/%s/%s"%(InDirName, file_download, file_sub), sep = "\t", encoding='unicode_escape', low_memory=False, error_bad_lines=False)
                df.to_parquet("%s/%s.parquet"%(OutDirName, file_sub[:-5]))

print(f"csv2parquet: Converting file {InDirName}")