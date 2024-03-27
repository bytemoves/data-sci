class DFG:
    def __init__(self,name,company):
        self.name = name
        self.company = company
        
    def show(self):
        print("Hello my name is" + self.name ,"I Work in" +self.company)
        
        
obj = DFG ("dave","geeks company") 
obj.show()   
        
        
        
