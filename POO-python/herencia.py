class vehicle:
  def __init__(self, brand, model, price):
      self.brand = brand
      self.model = model
      self.price = price
      self.disponibilidad = True

  def sell(self):
     if self.disponibilidad:
        self.disponibilidad = False
        print(f" EL vehiculo {self.brand} ha sido vendido")
     else:
        print(f"el vehiculo {self.brand} No esta disponible")

  def check_disponibilidad(self):
     return self.disponibilidad
  
  def get_price (self):
      return self.price
  
  def start_engine(self):
     raise NotImplementedError("Este metodo debe ser implementado la subclase")
  
  
  def stop_engine(self):
     raise NotImplementedError("Este metodo debe ser implementado la subclase")
  
  #herencia
class Car(vehicle):
     def start_engine(self):
        if not self.disponibilidad:
           return f"El motor del coche  {self.brand} esta en marcha"
        else:
           return f"El coche {self.brand} no esta disponible"
     
     def stop_engine(self):
        if self.disponibilidad:
           return f"El motor del coche {self.brand} se ha detenido"
        else:
           return f"El coche  {self.brand} No esta disponible"
      
class Bike(vehicle):
   def start_engine(self):
        if not self.disponibilidad:
           return f"la bicileta  {self.brand} esta en marcha"
        else:
           return f"La bicileta {self.brand} no esta disponible"
     
   def stop_engine(self):
        if self.disponibilidad:
           return f"la bicileta {self.brand} se ha detenido"
        else:
           return f"la bicileta {self.brand} No esta disponible"
        
class Truck(vehicle):
    def start_engine(self):
        if not self.disponibilidad:
           return f"El motor del camion  {self.brand} esta en marcha"
        else:
           return f"El camion {self.brand} no esta disponible"
     
    def stop_engine(self):
        if self.disponibilidad:
           return f"El motor del camion {self.brand} se ha detenido"
        else:
           return f"El camion {self.brand} No esta disponible"
        
class Customer:
    def __init__(self, name):
      self.name = name
      self.purchased_vehicles = []
    
    def buy_vehicle(self, vehicle: vehicle):
       if vehicle.check_disponibilidad():
           vehicle.sell()
           self.purchased_vehicles.append(vehicle)
       else:
          print(f"Lo siento, {vehicle.brand} no esta disponible")

    def inquire_vehicle(self, vehicle: vehicle):
       if vehicle.check_disponibilidad ():
          dispo = "Disponible"
       else:
          dispo = "No disponible"
          print(f"el {vehicle.brand} esta {dispo} y cuesta {vehicle.get_price()}")

class Dealership:
   def __init__(self):
      self.inventory = []
      self.customers = []
      
   def add_vehciles(self, vehicle: vehicle):
      self.inventory.append(vehicle)
      print(f"El {vehicle.brand} ha sido añadido al inventario")

   def register_customers(self, customers: Customer):
      self.customers.append(customers)
      print(f"el {customers.name} ha sido añadido al inventario")

   def show_available_vehicle(self):
      print("Vehiculos disponibles en la tienda ")
   for vehicle in self.inventory:
      if vehicle.check_disponibilidad():
         print(f"- {vehicle.brand} por {vehicle.price ()}")

car1 = Car("Toyota", "Corolla", 2000)
bike1 = Bike("Yamaha", "MT-07", 70000)
truck1 = Truck("Volvo", "FH16",  80000)

customer1 = Customer("Carlos")

Dealership.add_vehciles(car1)
Dealership.add_vehciles(bike1)
Dealership.add_vehciles(truck1)

# mostrar vehiculos disponibles

Dealership.show_available_vehicle()

#cliente consulta vehiculo

customer1.inquire_vehicle(car1)

#cliente comprar vehiculo

customer1.buy_vehicle(car1)

