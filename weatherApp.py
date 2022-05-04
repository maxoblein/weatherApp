#create a weather app gui
from cgitb import reset
from getWeather import getWeather
from tkinter import *
from tkinter import ttk
import pandas as pd


  
  
# Creating App class which will contain
# Label Widgets
class App:
    def __init__(self, master) -> None:
  
        # Instantiating master i.e toplevel Widget
        self.master = master
        self.initSearchFrame()

        


    def initSearchFrame(self):
        #Instantiate app frame one
        self.searchFrame = ttk.Frame(self.master)

        #intantiating labels
        self.titleLabel = ttk.Label(self.searchFrame, text="Weather App",font=("Arial", 25))
        self.cityLabel = ttk.Label(self.searchFrame, text="City",font=("Arial", 20))
        self.countryLabel = ttk.Label(self.searchFrame, text="Country (code)",font=("Arial", 20))

        #intantiating text entry
        self.textfieldCity = ttk.Entry(self.searchFrame,font=("Arial", 18))

        #instantiatinng the country code selection box
        df = pd.read_csv('countryCodes.csv')
        codes = df['Code'].tolist()
        self.codeCombobox = ttk.Combobox(self.searchFrame,values=codes)

        #intantiating search button and search variables
        self.city = ""
        self.countryCode = ""
        self.searchButton = ttk.Button(self.searchFrame,text='Get weather',command=self.goToResultFrame)

        ##packing frame
        self.titleLabel.pack(pady=15)
        self.cityLabel.pack(pady=15)
        self.textfieldCity.pack(pady=15)
        self.countryLabel.pack(pady=15)
        self.codeCombobox.pack(pady=15)
        self.searchButton.pack(pady=15)

        #adding search frame to root window
        self.searchFrame.pack()

    def goToResultFrame(self):
        
        if self.textfieldCity.get() == "" or self.codeCombobox.get() == "":
            self.goToErrorPage()
            

        #get weather data
        city = self.textfieldCity.get()
        countryCode = self.codeCombobox.get()

        print(city)
        print(countryCode)

        info = getWeather(cityName=city,countryCode=countryCode)
        print(info)

        #build result frame
        self.resultFrame = ttk.Frame(self.master)
        self.resultTitle = ttk.Label(self.resultFrame,text='Result screen',font=("Arial", 25))

        self.resetButton = ttk.Button(self.resultFrame,text="Reset",command=self.reset)
        
        #pack result frame
        self.resultTitle.pack(pady=15)
        self.resetButton.pack(pady=15)
        

        #destroy old frame and switch to new
        self.searchFrame.destroy()
        self.resultFrame.pack()

    
    def goToErrorPage(self):
        self.errorFrame = ttk.Frame(self.master)

        #error title
        self.errorTitle = ttk.Label(self.errorFrame,text="Error", font=("Arial", 25))
        self.resetButton = ttk.Button(self.errorFrame,text="Reset",command=self.errorReset)

        self.errorTitle.pack(pady=15)
        self.resetButton.pack(pady=15)

        self.searchFrame.destroy()
        self.errorFrame.pack()


    def reset(self):
        self.resultFrame.destroy()
        self.initSearchFrame()

    def errorReset(self):
        self.errorFrame.destroy()
        self.initSearchFrame()
        
  
  
if __name__ == "__main__":
  
    # Instantiating top level
    root = Tk()
  
    # Setting the title of the window
    root.title("Weather App")
  
    # Setting the geometry i.e Dimensions
    root.geometry("400x400")
  
    # Calling our App
    app = App(root)
  
    # Mainloop which will cause this toplevel
    # to run infinitely
    root.mainloop()