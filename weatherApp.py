#create a weather app gui

from getWeather import getWeather
from tkinter import *
from tkinter import ttk
import pandas as pd
from PIL import Image, ImageTk
from matplotlib import pyplot as plt


  
  
# Creating App class which will contain
# Label Widgets
class App:
    def __init__(self, master,gui_style) -> None:
  
        # Instantiating master i.e toplevel Widget
        self.master = master
        self.style = gui_style
        self.initSearchFrame()

        


    def initSearchFrame(self):
        #Instantiate app frame one
        self.searchFrame = ttk.Frame(self.master,style='My.TFrame')

        #intantiating labels
        self.titleLabel = ttk.Label(self.searchFrame, text="Weather App",font=("Arial", 25),style='My.TLabel')
        self.cityLabel = ttk.Label(self.searchFrame, text="City",font=("Arial", 20),style='My.TLabel')
        self.countryLabel = ttk.Label(self.searchFrame, text="Country (code)",font=("Arial", 20),style='My.TLabel')

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

        self.info = getWeather(cityName=city,countryCode=countryCode)
        if not bool(self.info):
            self.goToErrorPage()
            return

        #build result frame
        self.resultFrame = ttk.Frame(self.master,style='My.TFrame')
        self.resultTitle = ttk.Label(self.resultFrame,text=self.info.get('name')+" , "+self.info.get('country'),font=("Arial", 25),style='My.TLabel')

        #weather labels
        
        self.weatherDescriptionLabel = ttk.Label(self.resultFrame,text="Weather: "+self.info.get('description'),font=("Arial", 20),style='My.TLabel')
        
        

        icon_image = ImageTk.PhotoImage(Image.open('weather_icon.png'))
        
        self.weatherIconLabel = ttk.Label(self.resultFrame, image = icon_image,style='MyImage.TLabel')
        
        self.tempLabel = ttk.Label(self.resultFrame,text="Temperature: "+str(self.info.get('temp'))+"C",font=("Arial", 20),style='My.TLabel')
        self.maxTempLabel = ttk.Label(self.resultFrame,text="Max: "+str(self.info.get('maxTemp'))+"C",font=("Arial", 20),style='My.TLabel')
        self.minTempLabel = ttk.Label(self.resultFrame,text="Min: "+str(self.info.get('minTemp'))+"C",font=("Arial", 20),style='My.TLabel')

        self.resetButton = ttk.Button(self.resultFrame,text="Reset",command=self.reset)
        
        #pack result frame
        self.resultTitle.pack(pady=10)
        self.weatherDescriptionLabel.pack(pady=10)
        self.weatherIconLabel.pack(pady=10)
        self.tempLabel.pack(pady=10)
        self.maxTempLabel.pack(pady=10)
        self.minTempLabel.pack(pady=10)
        self.resetButton.pack(pady=10)
        

        #destroy old frame and switch to new
        self.searchFrame.destroy()
        self.resultFrame.pack()

    
    def goToErrorPage(self):
        self.errorFrame = ttk.Frame(self.master,style='My.TFrame')

        #error title
        self.errorTitle = ttk.Label(self.errorFrame,text="Error", font=("Arial", 25),style='My.TLabel')
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

    root.configure(bg='#037bfc')
  
    # Setting the geometry i.e Dimensions
    root.geometry("400x500")

    gui_style = ttk.Style()
    gui_style.configure('My.TFrame', background='#037bfc')
    gui_style.configure('My.TLabel', foreground = 'white', background='#037bfc')
    gui_style.configure('MyImage.TLabel', background='#037bfc')
    # Calling our App
    app = App(root,gui_style)
  
    # Mainloop which will cause this toplevel
    # to run infinitely
    root.mainloop()