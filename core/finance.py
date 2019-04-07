import datetime as dt
import os
import pandas as pd
from pandas_datareader import data as pdr
from matplotlib import pyplot
from matplotlib import style
import converthtml
import mail

style.use('ggplot')

today = dt.datetime.today()
start = dt.datetime(today.year, today.month, today.day)
end = dt.datetime(today.year, today.month, today.day)

stocks = ['ZHY.TO', 'VSC.TO', 'XEF.TO', 'ZWA.TO', 'HXS.TO', 'HXT.TO', 'VSB.TO', 'PZD', 'HLPR.TO', 'HCRE.TO']

def get_data(stock, start, end):
    data = (stock, pdr.DataReader(stock, 'yahoo', start, end))
    return data

def plot_data(dataframe):
    pyplot.clf()
    stock_name = dataframe[0]
    df = dataframe[1]
    df['Adj Close'].plot()
    pyplot.title(stock_name)
    create_folder('../resources/{date}'.format(date=dt.datetime.now().date()))
    pyplot.savefig('../resources/{date}/{stock}.png'.format(date=dt.datetime.now().date(),stock=stock_name))

def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(os.path.normpath(path))

for s in stocks:
    df = get_data(s, start, end)
    plot_data(df)

converthtml.get_final_html(stocks)
mail.send_report()
