from multiprocessing.dummy import Array
from tkinter import *
from tkinter.filedialog import *
import fileinput
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
from ttkwidgets.autocomplete import AutocompleteCombobox
from itertools import groupby
from pyspark.sql.functions import explode
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import plotly.express as px
from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style

def colors_def(sample):
  col_i=0
  colors=[]
  for i in sample:
    if i==sample['Тревожность']:
      if i<=10 and i>=8:
        if col_i%2==0: 
          colors.append('#ff0000')
        else:
          colors.append('#cf0000')
          
      elif i<8 and i>=5:
        if col_i%2==0: 
          colors.append('#ffff00')
        else:
          colors.append('#f0f000')
        
      elif i<5 and i>=0:
        if col_i%2==0: 
          colors.append('#00ff00')
        else:
          colors.append('#02ba02')

    else: 
      if i<=10 and i>=8:
        if col_i%2==0: 
          colors.append('#00ff00')
        else:
          colors.append('#02ba02')
          
      elif i<8 and i>=5:
        if col_i%2==0: 
          colors.append('#ffff00')
        else:
          colors.append('#f0f000')
        
      elif i<5 and i>=0:
        if col_i%2==0: 
          colors.append('#ff0000')
        else:
          colors.append('#cf0000')
    col_i-=1
  return(colors)
    

def generate_gr():
  global canvas_gr
  cb_value=combo_box.get()
  if cb_value=='':
    df_gr=print_df
    print(print_df)
  else:
    df_gr=(print_df.loc[print_df['Из какого вы отдела?'] == cb_value])
  print(df_gr)
  labels=print_df.drop(columns = ['Из какого вы отдела?'],axis = 1).columns
  df=df_gr.mean()
  
  if canvas_gr:
    canvas_gr.get_tk_widget().destroy()
#########################################################
  fig = plt.figure(figsize=(4,4))
  ax = fig.add_subplot(111,polar=True)
  sample=df

  N = len(sample) 
  # colors = np.array(['#4bb2c5','#c5b47f','#EAA228','#579575','#839557','#958c12','#953579','#4b5de4'])
  colors=colors_def(sample)
      
  theta = np.arange(0, 2*np.pi, 2*np.pi/N) 
  bars = ax.bar(theta, sample, width=0.8,color=colors)

  ax.set_xticks(theta)
  ax.set_xticklabels(labels)
  ax.set_title(str(cb_value))

  plt.ylim((None, 10))
  ax.yaxis.grid(True)

################################################   
  canvas_gr = FigureCanvasTkAgg(fig, master = root)
  canvas_gr.draw()
  canvas_gr.get_tk_widget().pack( fill=NONE,anchor='w',expand=False)
  canvas_gr
  # root.after(100, None)
  
  
  
#создание болочки отдела
def otdel_spisok(lst):
  global combo_box
  combo_box = AutocompleteCombobox(root, width=25, completevalues=lst)
  combo_box.pack(side=LEFT, fill=NONE,anchor='nw')

  
  btn_gen = Button(root,text = 'Показать результат' ,command = generate_gr)
  btn_gen.pack(side=LEFT, fill=NONE,anchor='nw')
  
  
  
# открытие файла
def _open():
  global df
  global print_df
  btn_open.destroy()
  op = askopenfilename(parent=root)
  df_start = pd.read_excel(op)
  df_start['Из какого вы отдела?'] = df_start['Из какого вы отдела?'].str.split(',')
  df = df_start.explode('Из какого вы отдела?').drop(['Отметка времени','Ваши комментарии (при желании:))'],axis = 1)
  df['Из какого вы отдела?']=df['Из какого вы отдела?'].str.strip()
  print("________")
  print(df)
  
  print_df=df[['Из какого вы отдела?','Здоровье','Любовь','Сексуальная сфера','Работа','Отдых','Финансы','Смысл жизни','Тревожность']]
  
  
  #Формирование списка отделов
  otdel_list = []
  for i in df['Из какого вы отдела?']:
    if i not in otdel_list:
      otdel_list.append(i)
  lst=[el for el, _ in groupby(otdel_list)]
  otdel_spisok(lst)
  #############################
  
  ##########################################################
  # N = 8
  # theta = np.arange(0.,2 * np.pi, 2 * np.pi / N)
  # radii = np.array(print_df.mean())
  # plt.axes(polar=True)
  # colors = np.array(['#4bb2c5','#c5b47f','#EAA228','#579575','#839557','#958c12','#953579','#4b5de4'])

  
  # plt.show()
  

root = Tk()
canvas_gr = None #создание канваса для графа

root.title("Колесо баланса")
root.geometry("700x400") 
m = Menu(root)
root.config(menu=m)

fm = Menu(m)
m.add_cascade(label="Файл", menu=fm)
fm.add_command(label="Открыть", command=_open)
btn_open = Button(text = 'Открыть', command=_open )
btn_open.pack(anchor='nw')





root.mainloop()