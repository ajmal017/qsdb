from api.models import IBPricesModel
from ib_insync import *
from pandas import *

ib = IB()

def connect():
    
    connection_success = ib.connect('127.0.0.1', 7497, clientId=1)
    return print(connection_success)

def request_data():
    connect()
    contract = Forex('EURUSD')
    bars = ib.reqHistoricalData(
    contract, endDateTime='', durationStr='30 D',
    barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)
    return print(bars)