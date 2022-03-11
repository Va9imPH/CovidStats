import requests
from tkinter import *
from datetime import datetime

bgcolor = "#7daa4d"

root = Tk()
root.geometry("400x550")
root.title("Covid Stats")
root["bg"] = bgcolor

def getCovidData():
    response = requests.get(
        url = "https://disease.sh/v3/covid-19/all"
    ).json()
    
    total_cases = response["cases"]
    total_deaths = response["deaths"]
    today_cases = response["todayCases"]
    today_deaths = response["todayDeaths"]
    active = response["active"]
    tests = response["tests"]

    final = "Total Cases: " + str(total_cases) + "\n" + "Total Deaths: " + str(total_deaths) + "\n" + "Today Cases: " + str(today_cases) + "\n" + "Today Deaths: " + str(today_deaths) + "\n" + "Active: " + str(active) + "\n" + "Tests: " + str(tests) + "\n"
    date = datetime.now().strftime("%H:%M:%S")

    label.config(text = "Covid Stats")
    item_label.config(text = final)
    datetime_label.config(text = "Updated at: " + date)

label = Label(root, font = ("quicksand", 27, "bold"), borderwidth = 2, highlightbackground = "black", fg = "white", bg = bgcolor)
label.pack(pady = 20)

item_label = Label(root, font = ("quicksand", 22, "normal"), fg = "white", bg = bgcolor)
item_label.pack(pady = 0)

datetime_label = Label(root, font = ("quicksand", 15, "bold"), fg = "white", bg = bgcolor)
datetime_label.pack(pady = 10)

reload_button = Button(root, font = ("quicksand", 10, "normal"), text = "Reload", command = getCovidData)
reload_button.pack(pady = 20)

getCovidData()

mainloop()