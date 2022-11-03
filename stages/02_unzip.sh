#!/usr/bin/env bash

# Script to unzip files

# Get local path
localpath=$(pwd)
echo "Local path: $localpath"

# Set download path
downloadpath="$localpath/download"
echo "Download path: $downloadpath"

# Raw data path
rawpath="$localpath/raw"
mkdir -p $rawpath
echo "Raw path: $downloadpath"

# move in the download folder
cd $downloadpath

# Set list path
zipfile=(*)
echo "zip path: $zipfile"

# Unzip file
unzip $downloadpath/$zipfile -d $rawpath

# Unzip in the raw folder only data processed 
cd $rawpath/CPCat

zipfile=(*)
echo "zip path: $zipfile"

unzip $zipfile -d $rawpath
echo "Unzip done"
