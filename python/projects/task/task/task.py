
class task:
    counter=0
    def __init__(self,task_name,ownor,worker,production_date,execution_date,description=""):
        task.counter+=1
        self.task_namber=task.counter
        self.task_name=task_name
        self.ownor=ownor
        self.worker=worker
        self.production_date=production_date
        self.execution_date=execution_date
        self.status=False
        self.description=description
        

    def set_task_namber(self,new):
        self.task_namber=new
    def get_task_namber(self):
        return self.task_namber
    
    def set_task_name(self,new):
        self.task_name=new
    def get_task_name(self):
        return self.task_name
    
    def set_ownor(self,new):
        self.ownor=new
    def get_ownor(self):
        return self.ownor
    
    def set_worker(self,new):
        self.worker=new
    def get_worker(self):
        return self.worker
    
    def set_production_date(self,new):
        self.production_date=new
    def get_production_date(self):
        return self.production_date
    
    def set_execution_date(self,new):
        self.execution_date=new
    def get_execution_date(self):
        return self.execution_date
    
    def set_status(self,new):
        self.status=new
    def get_status(self):
        return self.status
    
    def set_description(self,new):
        self.description=new
    def get_description(self):
        return self.description
    

    


    

        

