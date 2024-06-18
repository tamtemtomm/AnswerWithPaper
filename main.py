import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_ALL, DND_FILES
from pandastable import Table

from Doc2Query import Doc2Query
from Query2Doc import Query2Doc


class App(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self):
        super().__init__()
        self.title("App")
        self.geometry("480x480")
        self.TkdndVersion = TkinterDnD._require(self)
        
        self.data_path = './dataset/data.json'
        self.file_path = None
    
    def addLabel(self, text='test', **kwargs):
        obj = ctk.CTkLabel(self, text=text)
        obj.pack(**kwargs)
            
        return obj
        
    def addEntryWidget(self, inputmode=False, width=400, **kwargs):
        obj = ctk.CTkEntry(self,  width=width)
        obj.pack(**kwargs)
        
        if inputmode:
            
            def drop(event):
                # do operations with event.data file
                self.file_path = event.data[1:-1]
                obj.configure(placeholder_text=event.data)
                
            obj.drop_target_register(DND_ALL)
            obj.dnd_bind("<<Drop>>", drop)
            
        return obj
     
    def addButton(self, command, text='test', **kwargs):
        obj = ctk.CTkButton(self, text=text, command=command)
        obj.pack(**kwargs)
        return obj

    def command(self):
        get_query = Doc2Query(query_len = 40)
        get_doc = Query2Doc(self.data_path)
        
        query = get_query(self.file_path)
        result = get_doc(query)
        
        print('Processing the file...')
        print(f'Query   : {query}')
        print(f'Result  : ')
        print(result)
        
        frame = ctk.CTkFrame(self)
        frame.pack(side='top')
        
        self.table = pt = Table(frame, dataframe=result, showtoolbar=True, showstatusbar=True)
        self.table.show()
       
    def run(self):
        self.inputLabel = self.addLabel(text='Input File', side='top')
        self.entryWidget = self.addEntryWidget( inputmode=True, side='top')
        self.startButton = self.addButton(self.command, text='Find', side='top', pady=15)
        

if __name__ == '__main__':
    app = App()
    app.run()
    app.mainloop()
