# Tezos Payout Data Analysis
This repo is a WIP with an aim to analyze the payout data to analyze epochwise trends. The current state allows the user to review sets of epochs for payout amounts and the number of delegators. 

## Requirements
```
contourpy==1.0.6 ; python_version >= '3.7'
cycler==0.11.0 ; python_version >= '3.6'
fonttools==4.38.0 ; python_version >= '3.7'
kiwisolver==1.4.4 ; python_version >= '3.7'
matplotlib==3.6.2
numpy==1.23.5 ; python_version >= '3.8'
packaging==21.3 ; python_version >= '3.6'
pandas==1.5.2
pillow==9.3.0 ; python_version >= '3.7'
pyparsing==3.0.9 ; python_full_version >= '3.6.8'
python-dateutil==2.8.2 ; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'
pytz==2022.6
six==1.16.0 ; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'
```

## How to run
1. `pipenv install`
2. Add <epoch-number>.csv files to `./data` folder. These are the files you want to analyze
3. python main.py

## TODOs
- Paramterize the script
- Add flags to optionally generate figures and output csvs
- Cleanup the code