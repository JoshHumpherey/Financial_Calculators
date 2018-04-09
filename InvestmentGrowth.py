import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
from matplotlib.ticker import FuncFormatter

fields = ('Annual Contribution', 'Growth Rate', 'Current Age', 'Retirement Age')

def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"0")
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries

def CalculatePortfolio(entries):
    contribution = (int(entries['Annual Contribution'].get()))
    growthRate = (float(entries['Growth Rate'].get()))
    currentAge = (int(entries['Current Age'].get()))
    retirementAge = (int(entries['Retirement Age'].get()))
    balance = 0
    portfolioSpread = [balance]
    ageSpread = [currentAge]

    while (currentAge <= retirementAge):
        balance = balance + contribution
        balance = balance + balance*growthRate
        currentAge = currentAge + 1

        ageSpread.append(currentAge)
        portfolioSpread.append(balance)

    PlotChart(ageSpread,portfolioSpread)

def PlotChart(ageSpread,portfolioSpread):
        formatter = FuncFormatter(millions)
        fig,ax = plt.subplots()
        ax.yaxis.set_major_formatter(formatter)
        plt.bar(ageSpread,portfolioSpread)
        plt.xlabel('Age')
        plt.ylabel('Portfolio Value')
        plt.title('Investment Growth Calculator')
        plt.show()

def millions(x, pos):
    'The two args are the value and tick position'
    return '$%1.1fM' % (x*1e-6)


if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))
   b1 = Button(root, text='Calculate',command=(lambda e=ents: CalculatePortfolio(e)))



   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
