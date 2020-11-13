#importing required packages
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import os
import re

import cufflinks as cf
import plotly.io as pio
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
cf.go_offline()
pio.renderers.default = 'notebook'

print(os.getcwd())


#importing two datasets
datab =pd.read_csv('QVI_purchase_behaviour.csv')

datat =pd.read_csv('QVI_transaction_data.csv')


#checking data
len(datab)
len(datat)

#checking coulmns names
datab.columns
datat.columns

#changing the column names
datab.columns=['LCardNumber','Lifestage','PCustomer']
datat.columns=['Date','StoreNumber','LCardNumber','TxnID','ProdNumber','ProdName','ProdQuality','TotalSales']

#Datatype of date was changed to Date in excel

#change datatype of date, ProdNumber,LCardNumber and TxnID
datat.Date =datat.Date.astype('category')
datat.ProdNumber =datat.ProdNumber.astype('category')
datat.LCardNumber =datat.LCardNumber.astype('category')
datat.TxnID =datat.TxnID.astype('category')


#merging two datasets
tdata=datat.set_index('LCardNumber').join(datab.set_index('LCardNumber'))
tdata=tdata.reset_index()
tdata=tdata.sort_values(by='Date').reset_index(drop='TRUE')