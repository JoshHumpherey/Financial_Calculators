import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
from matplotlib.ticker import FuncFormatter

fields = ('Annual Contribution', 'Growth Rate', 'Current Age', 'Retirement Age','Current Portfolio Value','Retirement Income')

def make_form(root, fields):
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

def calculate_portfolio(entries):
    contribution = (float(entries['Annual Contribution'].get()))
    growthRate = (float(entries['Growth Rate'].get()))
    currentAge = (int(entries['Current Age'].get()))
    retirementAge = (int(entries['Retirement Age'].get()))
    startingValue = (float(entries['Current Portfolio Value'].get()))
    portfolioSpread = [startingValue]
    ageSpread = [currentAge]
    balance = portfolioSpread[0]

    while (currentAge < retirementAge+1):
        balance = balance + contribution
        balance = balance + balance*growthRate
        currentAge = currentAge + 1
        if currentAge == retirementAge:
            swr = 0.03
            maxIncome = balance*swr
            print("MaxIncome: " , maxIncome)
            entries['Retirement Income'].insert(0,str(round(maxIncome,2)))

        ageSpread.append(currentAge)
        portfolioSpread.append(balance)

    plot_chart(ageSpread,portfolioSpread)

def plot_chart(ageSpread,portfolioSpread):
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
   root.wm_title("Portfolio Growth Estimator")
   ents = make_form(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))
   b1 = Button(root, text='Calculate',command=(lambda e=ents: calculate_portfolio(e)))



   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
