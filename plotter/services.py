from ib_insync import *

async def connectToIB(): 
    ib = IB()
    print("Starting IB")
    ibConnectionPromise = ib.connectAsync('127.0.0.1', 4002, clientId=1,timeout=4, readonly=False, account='')
    return ibConnectionPromise
    
async def requestTick(ibConnectionPromise):
    ib = await ibConnectionPromise
    currentTimePromise = ib.reqCurrentTimeAsync()
    currentTime = await currentTimePromise
    currentTimeString = currentTime.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    return currentTimeString

async def disconnect_to_ib(ibConnectionPromise):
    ib = await ibConnectionPromise
    ib.disconnect()

    

    
# def get_time(ib): 
#     request_time = ib.reqCurrentTimeAsync()
#     return request_time
# # # from ibapi.client import EClient
# # # from ibapi.wrapper import EWrapper  
# # # from ibapi.contract import Contract
# # # from threading import Thread




# # # # Below are the global variables
# # # # Below are the custom classes and methods 

# # # # Se crea la clase TestWrapper heredada de la Interface EWrapper que funciona como un GET
# # # class TestWrapper(EWrapper):
# # #     # Inicializa una Cola (Queue) de errores
# # #     def init_error(self):
# # #         error_queue = queue.Queue()
# # #         # Accedemos a las propiedade de Ewrapper
# # #         self.my_errors_queue = error_queue
        
# # #     # Chequea el estado de la cola y evalua si retorno un mensaje (verdadero/falso)
# # #     def is_error(self):
# # #         error_exist = not self.my_errors_queue.empty()
# # #         return error_exist
    
# # #     # Usa el valor que entrega is_error y obtiene un mensaje si hay un error
# # #     def get_error(self, timeout=6):
# # #         if self.is_error():
# # #             try:
# # #                 return self.my_errors_queue.get(timeout=timeout)
# # #             except queue.Empty:
# # #                 return None
# # #         return None
    
# # #     # Imprime el error capturado en consola
# # #     def error(self, id, errorCode, errorString):
# # #         ## Overrides the native method
# # #         errormessage = "IB retorna un error con ID: %d y código de error: %d que dice: %s" % (id, errorCode, errorString)
# # #         self.my_errors_queue.put(errormessage)
    
# # #     # Inicializa una Cola (Queue) de hora del servidor
# # #     def init_time(self):
# # #         # Inicializa la Cola
# # #         time_queue = queue.Queue()
# # #         self.my_time_queue = time_queue
# # #         return time_queue
    
# # #     # Obtiene la hora del servidor y la pone en la cola
# # #     def currentTime(self, server_time):
# # #         self.my_time_queue.put(server_time)
    
# # #     # Inicializa una Cola (Queue) de Precios
# # #     def init_price(self):
# # #         price_queue = queue.Queue()
# # #         self.my_price_queue = price_queue
# # #         return price_queue
    
# # #     # Obtiene el precio y lo pone en la cola
# # #     def currentPrice(self, price):
# # #         self.my_price_queue.put(price)

# # # # Se crea la clase TestClient heredada de la Interface EClient que funciona como un POST
# # # class TestClient(EClient):
# # #     # se implementa el argumento wrapper ya que es necesario para obtener mensajes de IB
# # #     def __init__(self, wrapper):
# # #         EClient.__init__(self, wrapper)
        
# # #     # Este método le pide a IB la hora
# # #     def server_clock(self):
# # #         print("Pidiendo la hora en formato Unix")     

# # #         # Crea una cola para almacenar la hora del servidor
# # #         time_storage = self.wrapper.init_time()

# # #         # Crea una petición para obtener la hota del servidor
# # #         self.reqCurrentTime()
        
# # #         # Especificamos un tiempo máximo de espera si no hay conexión 
# # #         max_wait_time = 10
        
# # #         # Vigilamos que la petición que le hicimos al servidor sí funciona, de lo contrario mandamos error
# # #         try:
# # #             requested_time = time_storage.get(timeout = max_wait_time)
# # #         except queue.Empty:
# # #             print("No habían datos en la cola o el tiempo máximo de conexión se alcanzó")
# # #             requested_time = None
            
# # #         # El While cheque que hay un error, si no hay se sale del error y envia la hora
# # #         while self.wrapper.is_error():
# # #             print("Error:")
# # #             print(self.get_error(timeout=5))
# # #         print (requested_time, "<============== Hora Unix")
# # #         return requested_time
    
# # #     # Este método le pide a IB el precio en Tiempo real
# # #     def realtime_tick(self):
# # #         # print("Pidiendo el precio en tiempo real") 
        
# # #         # # Crea una cola para almacenar los precios
# # #         # price_storage = self.wrapper.init_price()
        
# # #         # # print (contract, "<==== Contrato")
# # #         # # Crea una petición para obtener el precio tick by tick
# # #         # # self.reqTickByTickData(1, contract,"BidAsk", 0, True)
# # #         requested_price = self.reqCurrentTime()
# # #         # # Especificamos un tiempo máximo de espera si no hay conexión 
# # #         # max_wait_time = 10
        
# # #         # # Vigilamos que la petición que le hicimos al servidor sí funciona, de lo contrario mandamos error
# # #         # try:
# # #         #     requested_price = price_storage.get(timeout = max_wait_time)
# # #         # except queue.Empty:
# # #         #     print("No habían datos en la cola o el tiempo máximo de conexión se alcanzó")
# # #         #     requested_price = None
            
# # #         # # El While chequea que hay un error, si no hay se sale deñ error y envia la hora
# # #         # while self.wrapper.is_error():
# # #         #     print("Error:")
# # #         #     print(self.get_error(timeout=5))
# # #         # print (requested_price, "<============== Precio en Tiempo Real")
# # #         return requested_price
    
    
    
# # # # Creamos la clase TestApp para implementar TestWrapper y TestClient

# # # class IB(TestWrapper, TestClient):
    
# # #     #Inicializamos las clases que construimos previamente y definimos los atributos de TestApp
# # #     def __init__(self, ipaddress, portid, clientid):
# # #         TestWrapper.__init__(self)
# # #         TestClient.__init__(self, wrapper=self)

# # #         #Sobreescribimos la función para conectarnos al servidor con la IP, Puerto y Client ID 
# # #         self.connect(ipaddress, portid, clientid)

# # #         #Inicializamos un hilo
# # #         thread = Thread(target = self.run)
# # #         thread.start()
# # #         # Fijamos como atributo de clase a _thread y lo hacemos privado con _
# # #         setattr(self, "_thread", thread)

# # #         #Inicializamos init_error de Test Wrapper
# # #         self.init_error()



# # # # Definimos las funciones que ejecutan las clases

# # # def connect_to_ib():
# # #     print("Iniciando IB")
# # #     # Nos conectamos finalmente a IB
# # #     ib = IB("127.0.0.1", 4002, 1)
# # #     print("IB inició con éxito") 
# # #     return ib

# # #     # Hora del servidor obtenida de TestClient
# # # def get_time(ib):
# # #     requested_time = ib.server_clock()
# # #     return requested_time
    
# # # def get_tickbytick(ib):
# # #     requested_tick= ib.realtime_tick()
# # #     return requested_tick
    
    
# # # def create_contract():
# # #     eurusd = Contract()
# # #     eurusd.symbol = "EUR"
# # #     eurusd.exchange = "IDEALPRO"
# # #     eurusd.conId = 12087792
# # #     eurusd.secType = "CASH"
# # #     eurusd.currency = "USD"
# # #     return eurusd
    
    
# # # def disconnect_to_ib(ib):
# # #     ib.disconnect()