import sqlite3

class Client:
    def __init__(self, data_string):
        

        try:
            data = data_string.split(',')
            
            self.first_name = data[0].strip()
            self.last_name = data[1].strip()
            self.id_number = data[2].strip()
            self.phone = data[3].strip()
            self.amount = float(data[4].strip())
            self.date = data[5].strip()  

        except (IndexError, ValueError) as e:
           
              raise ValueError(f"Error in parsing client data: {e}")

    
    
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_id_number(self):
        return self.id_number

    def get_phone(self):
        return self.phone

    def get_amount(self):
        return self.amount
    
    def get_date(self):
        return self.date  


    def updating(self,Client2):
        if self.id_number == Client2.id_number :
          if self.get_first_name() == Client2.get_first_name() and self.get_last_name() == Client2.get_last_name():
              
            self.amount += Client2.amount

            if self.phone != Client2.phone:
                self.phone = Client2.phone

            return "The update is complete"

          else:
              return "Name and ID do not match"
          
    def show(self):
        return f"Client({self.first_name}, {self.last_name}, {self.id_number}, {self.phone}, {self.amount}, {self.date})"
    
    



            

        



        
class ManegDB:
    def __init__(self) -> None:
        self.db=[]
    

    def start(self,csv_name):

        with open(csv_name, "r") as fd:
            lines = fd.read().splitlines()
            for line in lines:
                client=Client(line)
                if  self.get_client_by_id(client.get_id_number()) == False:
                    self.db.append(client)
                else:
                     self.get_client_by_id(client.get_id_number()).updating(client)

        return self.db     



    def get_client_by_id(self,id):
        for client in self.db:
            if client.get_id_number() == id:
                return client
        return False
    
    def get_all(self):
        return self.db
    
    def filter_clients(self, condition):
        filtered_clients = []

        for client in self.db:
            try:
                if eval(condition.replace('=', '==')):
                    filtered_clients.append(client)
            except Exception as e:
                print(f"מחרוזת לא תקינה {e}")
        
        return filtered_clients
            

d=ManegDB()
d.start("db.csv")
print(d.get_client_by_id("123456789"))
