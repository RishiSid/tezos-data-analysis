import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

DATA = "./data"
CUTOFF = 500 # Amount in XTZ for the filter
OUTPUT = "./output"
FIGURES = "./figures"
MASTER_DF = "master_df.csv"

def init():
    if not os.path.exists(OUTPUT):
        os.makedirs(OUTPUT)
    if not os.path.exists(FIGURES):
        os.makedirs(FIGURES)
    if not os.path.exists(DATA):
        os.makedirs(DATA)

def draw_bar(listx, listy, labelx="", labely="", title="",filename="output"):
    # creating the bar plot
    half_len = int(len(listx)/2)
    c = ["maroon"]*half_len + ["blue"]*half_len
    plt.bar(listx, listy, color =c,width = 0.4)
 
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title)
    for i in range(len(listy)):
        plt.annotate(str(listy[i]), xy=(listx[i],listy[i]), ha='center', va='bottom')
    curr_time = str(int(datetime.timestamp(datetime.now())))
    filename=filename+curr_time+'.png'
    plt.show()
    #plt.savefig(os.path.join(FIGURES,filename))

def sum_by_epochs(master_df):
    epoch_df = master_df.groupby('epoch')['amount'].sum()
    y_ser =  epoch_df.values
    y = [round(ey,1) for ey in epoch_df.values]
    x = epoch_df.index.values
    #print(y)
    #print(x)
    draw_bar(x,y, labelx="Epochs", labely="Amount in XTZ", title="Epochwise Payout Amounts (XTZ)", filename="epoch-amounts")
    #print(epoch_df)

    y1 = round(y_ser[:6].sum(),0)
    y2 = round(y_ser[6:12].sum(),0)
    x1 = "537 - 542"
    x2 = "543 - 548"
    y = [y1, y2]
    x = [x1, x2]
    draw_bar(x,y, labelx="Epochs", labely="Amount in XTZ", title="6-Epoch Group Payout Amounts (XTZ)",filename="six-epoch-amounts")
    
def count_by_epochs(master_df):
    epoch_df = master_df.groupby('epoch')['amount'].count()
    y_ser =  epoch_df.values
    y = [round(ey,1) for ey in epoch_df.values]
    x = epoch_df.index.values
    #print(y)
    #print(x)
    labely = "No. of payouts with amount > " +str(CUTOFF) + " XTZ"
    draw_bar(x,y, labelx="Epochs", labely=labely, title="Epochwise Payout Counts ", filename="payout-counts")
    #print(epoch_df)

    y1 = round(y_ser[:6].sum(),0)
    y2 = round(y_ser[6:12].sum(),0)
    x1 = "537 - 542"
    x2 = "543 - 548"
    y = [y1, y2]
    x = [x1, x2]
    labely = "No. of payouts with amount > " +str(CUTOFF) + " XTZ"
    draw_bar(x,y, labelx="Epochs", labely=labely, title="6-Epoch Group Payout Counts ", filename="six-epoch-payout-counts")

def process_data(files, convert_to_csv = False):
    master_df = pd.DataFrame(columns=['address','epoch', 'type', 'amount'])
    for file in files:
        df = pd.read_csv(os.path.join(DATA,file))
        epoch = int(file.split(".")[0])
        df['amount'] = df['amount'].div(10**6).round(2)
        df = df[(df['amount']>CUTOFF) &  (df['type']!='B')]
        len_df = len(df)
        epoch_list = [epoch] * len_df
        df['epoch'] = epoch_list
        #print(df.iloc[2:10])
        master_df = pd.concat([master_df,df[['address','epoch','type', 'amount']]], ignore_index= True)
        #print(len(master_df))
    if convert_to_csv:
        master_df.to_csv(os.path.join(OUTPUT,MASTER_DF))
    return master_df

def main():
    init()
    files = sorted(os.listdir(DATA))
    mdf = process_data(files, convert_to_csv= True)
    sum_by_epochs(mdf)
    count_by_epochs(mdf)

if __name__ == "__main__":
    main()





