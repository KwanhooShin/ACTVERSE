import Loader.csvloader
import tkinter
from tkinter import filedialog
import pandas as pd
import glob

# tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
# folder_path = filedialog.askdirectory()

# # assign dataset names
# list_of_names = ['crime', 'username']
#
# # create empty list
# dataframes_list = []
#
# # append datasets into the list
# for i in range(len(list_of_names)):
#     temp_df = pd.read_csv("./csv/" + list_of_names[i] + ".csv")
#     dataframes_list.append(temp_df)

def Easyavatarload():
    tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
    folder_path = filedialog.askopenfilename()
    tmpdf = Loader.csvloader.avatarcsvloader(folder_path)

    return tmpdf

def Easymultiload(mode):
    tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
    folder_path = filedialog.askdirectory()
    csvnamelist = glob.glob(folder_path+'/*.csv')
    dataframe_list = []
    if mode == 'Avatar':
        for i in range(len(csvnamelist)):
            tmpdf = Loader.csvloader.avatarcsvloader(csvnamelist[i])
            dataframe_list.append(tmpdf)
    elif mode == 'General':

        for i in range(len(csvnamelist)):
            tmpdf = Loader.csvloader.generalcsvloader(csvnamelist[i])
            dataframe_list.append(tmpdf)
    return dataframe_list


