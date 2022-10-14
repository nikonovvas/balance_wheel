from tkinter import *
from tkinter.filedialog import *
import fileinput
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
from ttkwidgets.autocomplete import AutocompleteCombobox


def otdel(x):
  return x
  
# открытие файла
def _open():

  op = askopenfilename(parent=root)
  print(op)
  content = pd.read_excel(op)
  print_content=content[['Здоровье','Любовь','Сексуальная сфера','Работа','Отдых','Финансы','Смысл жизни',	'Тревожность']]
  print(print_content.mean())
  otdel(print_content.mean())
  global lst
  lst=['dadsa', 'dasd']
  combo_box = AutocompleteCombobox(root, width=30, completevalues=lst)
  combo_box.pack()
  N = 8
  theta = np.arange(0.,2 * np.pi, 2 * np.pi / N)
  radii = np.array(print_content.mean())
  plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
  colors = np.array(['#4bb2c5','#c5b47f','#EAA228','#579575','#839557','#958c12','#953579','#4b5de4'])
  bars = plt.bar(theta, radii, width=(2*np.pi/N), bottom=0.0, color=colors)
  plt.show()


root = Tk()
root.title("Колесо баланса")
root.minsize(width=500, height=400)
m = Menu(root)
root.config(menu=m)

fm = Menu(m)
m.add_cascade(label="Файл", menu=fm)
fm.add_command(label="Открыть", command=_open)




root.mainloop()