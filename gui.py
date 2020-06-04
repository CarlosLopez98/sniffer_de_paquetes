import tkinter
from tkinter import *
from tkinter import ttk


class MainWindow:

    def __init__(self, n_frames, data=[]):
        self.data = data

        root = tkinter.Tk()
        root.title('Sniffer de paquetes')
        #root.geometry('500x500')

        # Frame superior
        frame_1 = Frame(root)
        frame_1.config(bg='snow')
        frame_1.pack(fill=BOTH, expand=True)

        lbl_preambule = Label(frame_1, text='Preambule')
        lbl_preambule.config(bg='snow', relief=RAISED)
        lbl_preambule.grid(row=0, column=1, sticky=N+S+E+W)

        lbl_source = Label(frame_1, text='Source')
        lbl_source.config(bg='snow', relief=RAISED)
        lbl_source.grid(row=0, column=2, sticky=N+S+E+W)

        lbl_destination = Label(frame_1, text='Destination')
        lbl_destination.config(bg='snow', relief=RAISED)
        lbl_destination.grid(row=0, column=3, sticky=N+S+E+W)

        lbl_type = Label(frame_1, text='Type')
        lbl_type.config(bg='snow', relief=RAISED)
        lbl_type.grid(row=0, column=4, sticky=N+S+E+W)

        # Tabla
        self.var = IntVar()
        for i in range(n_frames):
            for j in range(5):
                Grid.columnconfigure(frame_1, j, weight=1)
            # row 0
            r = Radiobutton(frame_1, variable=self.var, value=i, command=self.show_info)
            r.config(bg='white')
            r.grid(row=i+1, column=0, sticky=N+S+E+W)

            # row 1
            col_1 = Label(frame_1, text=data[i]['preambule'])
            col_1.config(bg='white', width=20, relief=RAISED)
            col_1.grid(row=i+1, column=1, sticky=N+S+E+W)

            # row 2
            col_2 = Label(frame_1, text=data[i]['source'])
            col_2.config(bg='white', width=20, relief=RAISED)
            col_2.grid(row=i+1, column=2, sticky=N+S+E+W)

            # row 3
            col_3 = Label(frame_1, text=data[i]['destination'])
            col_3.config(bg='white', width=20, relief=RAISED)
            col_3.grid(row=i+1, column=3, sticky=N+S+E+W)

            # row 4
            col_3 = Label(frame_1, text=data[i]['type'])
            col_3.config(bg='white', width=20, relief=RAISED)
            col_3.grid(row=i+1, column=4, sticky=N+S+E+W)

        # ----------------------------------------------------------------------
        # Frame central

        frame_2 = Frame(root)
        frame_2.pack(side=TOP, fill=BOTH, expand=True)

        self.treeview = ttk.Treeview(frame_2)
        self.treeview.config(height=5)
        self.treeview.pack(side=LEFT, fill=BOTH, expand=True)

        self.scroll_2 = Scrollbar(frame_2, orient='vertical', command=self.treeview.yview)
        self.scroll_2.pack(side=RIGHT, fill=Y)

        self.payload = self.treeview.insert('', END, text='Payload')
        self.treeview.insert(self.payload, END, iid='payload', text=data[self.var.get()]['payload'])

        summary = data[self.var.get()]['summary'].split('/')
        self.summary = self.treeview.insert('', END, text='Summary')
        for i, summ in enumerate(summary):
            self.treeview.insert(self.summary, END, iid=f'summary{i}', text=summ)

        # ----------------------------------------------------------------------
        # Frame inferior

        frame_3 = LabelFrame(root, text='Datagram')
        frame_3.config(bg='snow', labelanchor=N)
        frame_3.pack(fill=BOTH, expand=True)

        self.lbl_datagram = Label(frame_3, text=data[self.var.get()]['datagram'])
        self.lbl_datagram.config(bg='snow', wraplength=400, justify=LEFT)
        self.lbl_datagram.pack(side=LEFT)

        self.scroll_3 = Scrollbar(frame_3, orient='vertical')
        self.scroll_3.pack(side=RIGHT, fill=Y)

        root.mainloop()


    def show_info(self):
        self.treeview.item('payload', text=self.data[self.var.get()]['payload'])

        for i, summ in enumerate(self.data[self.var.get()]['summary'].split('/')):
            self.treeview.item(f'summary{i}', text=summ)

        self.lbl_datagram['text'] = self.data[self.var.get()]['datagram']
