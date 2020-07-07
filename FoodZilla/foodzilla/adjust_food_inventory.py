import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt
import string
import math
import datetime
import numpy as np
import csv


#function to retrain the model based on the new data
#returns model object
def update_csv(csv_path, value):
    with open(csv_path, 'a') as csvfile:
        spamwriter = csv.writer(csvfile)
        date = datetime.date.today()
        date = date.strftime('%m/%d/%Y')
        temp = date
        spamwriter.writerow([])
        spamwriter.writerow([temp, value])



def retrain(csv_path):
    df = pd.read_csv(csv_path)

    df.head()

    m = Prophet()
    m.fit(df)
    return m

def find_adjusted_food_order(demand_csv, sell_csv, month_after):
    #create models for both inventory and wastage
    date = datetime.date.today() + pd.DateOffset(months=month_after)
    inventory_model = retrain(demand_csv)
    waste_model = retrain(sell_csv)
    inventory = predict_date(date, inventory_model, month_after)
    waste = predict_date(date, waste_model, month_after)

    #return adjusted amount for needed date
    return inventory - waste


def predict_date(date, model, period):

    #make dataframe
    #current date - last date in training + period
    period = int(((pd.to_datetime("today") - list(model.history['ds'])[-1])/np.timedelta64(1, 'M'))) + period
    #period = pd.to_datetime("today") - list(model.history['ds'])[-1] + pd.offsets.MonthOffset(period)
    future = model.make_future_dataframe(periods=50*period)
    #add to tail
    future.tail()

    #make prediction
    forecast = model.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    #change to standard times
    forecast['ds'] = pd.to_datetime(forecast['ds'])
    date_formatted = pd.Timestamp(date)
    list_index = list(forecast['ds']).index(date_formatted)
    return list(forecast['yhat_lower'])[list_index]




def main():


    print(find_adjusted_food_order("./monthly_tomatoes.csv", "./monthly_tomatoes_ooglorp.csv", 2))
    update_csv("./monthly_tomatoes.csv", 69)
    #print(list(forecast['yhat_lower'])[list(forecast['ds']).index(pd.Timestamp('2010-08-10'))]) #how to look up a certain date






main()