import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

class simple_plotter:
    ''' Plots versus date, i.e. assumes time as x-axis 
    '''
    
    def __init__(self, columns, data, time_format='%Y-%m-%d %H:%M:%S'):
        self.load_data(columns, data, time_format)

    def load_data(self, columns, data, time_format='%Y-%m-%d %H:%M:%S'):
        self.columns = list(columns.values()) 
        xcolumn = str(columns[0])
        self.dataframe = pd.DataFrame( [[ij for ij in i] for i in data] )
        self.dataframe.rename(columns=columns, inplace=True)
        self.dataframe[xcolumn] = pd.to_datetime(self.dataframe[xcolumn], format=time_format) 

    def plot_it(self, xlabel="Date [YYYY-mm-dd]", ylabel="Current [uA]", filename=""):
        self.dataframe.set_index([self.columns[0]], inplace=True)
        self.dataframe.plot(legend=True, xlabel=xlabel, ylabel=ylabel, use_index=True)
        if filename == "":
            plt.show()
        else:
            plt.savefig(filename) 

class simple_plotter_opt:
    ''' Plots versus date, i.e. assumes time as x-axis 
    '''
    
    def __init__(self, columns, data, time_format='%Y-%m-%d %H:%M:%S'):
        self.load_data(columns, data, time_format)

    def load_data(self, columns, data, time_format='%Y-%m-%d %H:%M:%S'):
        self.columns = list(columns.values()) 
        ncols = len(self.columns)
        nrows = len(data)
        xcolumn = str(columns[0])
        self.date = np.zeros(nrows, dtype=np.float)
        self.pred = np.zeros(nrows, dtype=np.float)
        self.meas = np.zeros(nrpws, dtype=np.float)
        i = 0 
        for row in data:
            self.date[i] = matplotlib.dates.date2num(row[0])
            self.pred[i] = row[1]
            self.meas[i] = row[2]
            i = i + 1
        
    def plot_it(self, xlabel="Date [YYYY-mm-dd]", ylabel="Current [uA]", filename=""):
        plt.gcf().autofmt_xdate() 
        plt.ylabel("Current [uA]") 
        plt.plot(self.date,self.pred,'.-',label="predicted", alpha=0.5)
        plt.plot(self.date,self.meas,'.-',label="measured",alpha=0.5) 
        plt.legend()
        if filename == "":
            plt.show()
        else:
            plt.savefig(filename) 

