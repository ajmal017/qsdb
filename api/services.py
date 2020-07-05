
#     connection_success = "Holi"
#     return print(connection_success)
    
#     # requestTick = ib.reqTickByTickData(Forex("EURUSD"), 'BidAsk')
#     # requestTick = ib.reqTickByTickData(Forex("EURUSD"), 'BidAsk')
    

# def connect_to_bittrex(coin_name):
#     url = "https://bittrex.com/api/v1.1/public/getticker?market=USDT-{}".format(coin_name)
#     data = requests.get(url).json()
#     last_price = data.get("result").get("Last")
#     return last_price
    
# def reqTicks():
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     requestTick = ib.reqTickByTickData(Forex("EURUSD"), 'BidAsk')
#     tick = util.tree(requestTick)['Ticker']['bid']
#     return print(tick)

# while True:
#     pass
# connection_success = ib.connect(host='127.0.0.1', port=4002, clientId=2)

# from ib_insync import IB, util, Contract
# import pytz
# import pandas as pd
# from datetime import datetime, timedelta
# from tzlocal import get_localzone

# class Topo():
#     '''Download tick data from the IB API for the session of each day of the week'''
#     def __init__(self):
#         '''Initializes the topo atribuites.'''
#         self.ib=IB()
#         self.clientid = 1
#         self.symbols = ['PA']
#         self.exchanges = ['NYMEX']
#         self.exp =   ['20200721']
#         self.data_type = 'TRADES'
#         self.counter = 0
#         self.data = []
#         self.tz = pytz.timezone('US/Eastern')
#         self.local_tz = get_localzone()
#         self.counter_miss = 0
#         self.days = {0: 'MONDAY', 1: 'TUESDAY', 2: 'WEDNESDAY', 3: 'THURSDAY', 4: 'FRIDAY'}

#     def connect(self):
#         '''Connects to IB Gateway or TWS.'''
#         ib.connect('127.0.0.1', 7497, clientId=self.clientid)

#     def looping(self):
#         ''' Creates the routine for downloading the historical data.'''
#         finish = self.current_time - timedelta(minutes=1) #Initial flag
#         end = self.current_time.astimezone(self.local_tz) + timedelta(seconds=5) #Last date of the last closing in the machine TZ
#         close = self.ib.reqHistoricalTicks(self.contract, '', end, 1000, whatToShow=self.data_type, useRth=False)
#         df_close = util.df(close)
#         last= df_close.iloc[-1,0].tz_convert(self.tz).tz_localize(tz = None) #UTC to TZ parameter
#         while not(finish >= last):
#             if self.counter == 0:
#                 hist = self.ib.reqHistoricalTicks(self.contract,self.startdt, '', 1000, whatToShow=self.data_type, useRth=False)
#                 df = util.df(hist)
#                 if len(hist) > 0:
#                     self.data.append(df)
#                     self.counter = 1
#                     total = (self.current_time - self.startdt).total_seconds() #Difference between the current time and the desired initial date
#                 else:
#                     print('IB is not retreiving current data for {}'.format(self.ticket))
#                     break
#             else:
#                 finish = df.iloc[-1,0].tz_convert(self.tz).tz_localize(tz = None) #First date of the last download in our desired TZ
#                 end = df.iloc[-1,0].tz_convert(self.local_tz).tz_localize(tz = None) #First date of the last download in the machine TZ
#                 hist = self.ib.reqHistoricalTicks(self.contract, end, '', 1000, whatToShow=self.data_type, useRth=False)
#                 if len(hist) == 0:
#                     while len(hist) == 0:
#                         finish = finish + timedelta(minutes=1) #First date of the last download in our desired TZ
#                         end = end + timedelta(minutes=1) #First date of the last download in the machine TZ
#                         hist = self.ib.reqHistoricalTicks(self.contract, end, '', 1000, whatToShow=self.data_type, useRth=False)
#                         self.counter_miss += 1
#                         if len(hist) > 0:
#                             df = util.df(hist)
#                             self.data.append(df)
#                             sec_diff = (self.current_time - finish).total_seconds() # Number of data pending to download
#                             percent = (100 * ((total - sec_diff) / float(total)))  
#                             print(' Progress [%d%%]\r'%percent, end="")
#                         if (finish > self.current_time or finish == last):
#                             percent = 100
#                             print(' Progress [%d%%]\r'%percent, end="")
#                             break
#                 else:
#                     df = util.df(hist)
#                     if df.iloc[-1,0].tz_convert(self.tz).tz_localize(tz = None) == finish:
#                         print('Topo is asking for the same request')
#                     else:
#                         self.data.append(df)
#                         sec_diff = (self.current_time - finish).total_seconds() # Number of data pending to download
#                         percent = (100 * ((total - sec_diff) / float(total)))
#                         if (sec_diff < 0 or finish == last):
#                             percent = 100
#                         print(' Progress [%d%%]\r'%percent, end="")

#     def save_data(self):
#         ''' Preparate and save the data in a CSV file in the destination folder.'''
#         print(' ')
#         final = pd.concat(self.data) #Master DataFrame
#         final.columns = map(lambda x: x.capitalize(), final.columns)
#         final = final.rename(columns={'Time': 'Date', 'Price': 'Last', 'Size': 'Volume'})
#         final.drop(columns= ['Tickattriblast', 'Exchange', 'Specialconditions'], inplace=True)
#         final['consec'] = (final.Date != final.Date.shift()).cumsum() + (final.Last != final.Last.shift()).cumsum() #Calculates consecutive values
#         final = final.groupby(['consec', 'Date', 'Last']).sum().reset_index().drop('consec', axis=1) #Compressor
#         final.set_index('Date', inplace=True)
#         final.index = final.index.tz_convert(self.tz).tz_localize(tz = None) #Convert from UTC to TZ parameter
#         if final.iloc[0,0] > 1:
#             final = final.round(2)
#         else:
#             final = final.round(5)
#         alphanumeric = [character for character in str(self.startdt) if character.isalnum()]
#         init_date = ''.join(alphanumeric)
#         alphanumeric = [character for character in str(self.current_time) if character.isalnum()]
#         end_date = ''.join(alphanumeric)
#         final.to_csv('{}_{}-{}_ticks.csv'.format(self.ticket, self.ticket, init_date , end_date)) #Session
#         final.to_csv('{}_master.csv'.format(self.ticket, self.ticket), mode='a', header=False) #Master
        
#     def digging(self):
#         '''Starts the topo'''
#         self.current_time = datetime.now(self.tz) #Test Here
#         while not((self.current_time.weekday() == 4) & (self.current_time.hour > 17)): #Be active during the week, finish at market close
#             self.current_time = datetime.now(self.tz).replace(hour=17, minute=0, second=0, microsecond=0, tzinfo= None) #Test Here
#             if (self.current_time.weekday() <= 4) & (self.current_time.hour == 17) & (self.current_time.minute <= 2):
#                 self.startdt = self.current_time.replace(hour=16, minute=55)
#                 self.start_run = datetime.now(self.tz) #For calculating the time for downloading the session
#                 self.connect()
#                 print('DOWNLOADING SESSION OF {}'.format(self.days[self.current_time.weekday()]))
#                 for symbol, exchange in zip(self.symbols, self.exchanges):
#                     print('Downloading data for {}'.format(symbol))
#                     self.ticket = symbol
#                     self.exch = exchange
#                     self.contract = Contract(secType='CONTFUT', exchange=self.exch, symbol=self.ticket)
#                     self.ib.qualifyContracts(self.contract)
#                     self.looping()
#                     if self.counter > 0: self.save_data()
#                     print('Failed request # {} for {}'.format(self.counter_miss, self.ticket))
#                     self.counter = 0
#                     self.counter_miss = 0
#                     self.data = []
#                 time_run = 'Minutes Running per Session {}'.format(round((datetime.now(self.tz) - self.start_run).total_seconds()/60, 2))
#                 print(time_run)
#                 self.ib.disconnect()
#                 self.ib.sleep(1)    