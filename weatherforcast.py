from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk, Image
# 									--:Root window loading:--

"""root = Tk()
root.geometry('1900x1200')
#root.attributes('-alpha',0.5) //use if you want the background as transparent :)
load = Image.open('bgbg.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root,image = render)
img.place(x = 0, y = 0)"""""

root = Tk()
root.title("WeatherBug App")
root.geometry("1900x1200")
root['background'] = "SteelBlue1"

new1 = ImageTk.PhotoImage(Image.open('logo.jpg'))
panel = Label(root, image=new1)
panel.place(x=500, y=520)

new2 = ImageTk.PhotoImage(Image.open('company_logo.png'))
panel = Label(root, image=new2)
panel.place(x=10, y=150)
# 											--:Dates:--

dt = datetime.datetime.now()
date = Label(root, text=dt.strftime('%A--'), bg='SteelBlue1', font=("bold", 15))
date.place(x=500, y=130)
month = Label(root, text=dt.strftime('%m %B'), bg='SteelBlue1', font=("bold", 15))
month.place(x=600, y=130)
# 											 --:Time:--

hour = Label(root, text=dt.strftime('%I : %M %p'), bg='SteelBlue1', font=("bold", 15))
hour.place(x=500, y=160)
# 						--:Theme for the respective time the application is used:--

if int((dt.strftime('%I'))) >= 8 & int((dt.strftime('%I'))) <= 5:
	img = ImageTk.PhotoImage(Image.open('moon.jpg'))
	panel = Label(root, image=img)
	panel.place(x=1000, y=230)
else:
	img = ImageTk.PhotoImage(Image.open('sun.jpg'))
	panel = Label(root, image=img)
	panel.place(x=1000, y=230)
# 										 --:City Search:--

city_name = StringVar()
city_entry = Entry(root, textvariable=city_name, width=45)
city_entry.grid(row=1, column=0, ipady=10, stick=W+E+N+S)

def city_name():
	# 									  --:API Call:--

	api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
							+ city_entry.get() + "&units=metric&appid=b03ddcf7e0742269de8c64dffb1280e9")
	api = json.loads(api_request.content)
	# 									--:Temperatures:--

	y = api['main']
	current_temprature = y['temp']
	humidity = y['humidity']
	tempmin = y['temp_min']
	tempmax = y['temp_max']
	# 								     --:Coordinates:--

	x = api['coord']
	longtitude = x['lon']
	latitude = x['lat']
	# 									   --:Country:--

	z = api['sys']
	country = z['country']
	citi = api['name']
	# 					    --:Adding the received info into the screen:--

	lable_temp.configure(text=current_temprature)
	lable_humidity.configure(text=humidity)
	max_temp.configure(text=tempmax)
	min_temp.configure(text=tempmin)
	lable_lon.configure(text=longtitude)
	lable_lat.configure(text=latitude)
	lable_country.configure(text=country)
	lable_citi.configure(text=citi)
# 								     --:Search Bar and Button:--

city_nameButton = Button(root, text="Search", command=city_name)
city_nameButton.grid(row=1, column=1, padx=3, stick='e')
# 							      --:Country Names and Coordinates:--

lable_citi = Label(root, text="...", width=0, bg='SteelBlue1', font=("bold", 15))
lable_citi.place(x=500, y=63)
lable_country = Label(root, text="...", width=0, bg='SteelBlue', font=("bold", 15))
lable_country.place(x=600, y=63)
lable_lon = Label(root, text="...", width=0, bg='SteelBlue1', font=("Helvetica", 15))
lable_lon.place(x=500, y=95)
lable_lat = Label(root, text="...", width=0, bg='SteelBlue1', font=("Helvetica", 15))
lable_lat.place(x=600, y=95)
# 								      --:Current Temperature:--

lable_temp = Label(root, text="...", width=0, bg='SteelBlue1', font=("Helvetica", 110), fg='black')
lable_temp.place(x=500, y=220)
# 								   --:Other temperature details:--

humi = Label(root, text="Humidity: ", width=0, bg='SteelBlue1', font=("bold", 15))
humi.place(x=500, y=400)
lable_humidity = Label(root, text="...", width=0, bg='SteelBlue1', font=("bold", 15))
lable_humidity.place(x=630, y=400)
maxi = Label(root, text="Max. Temp.: ", width=0, bg='SteelBlue1', font=("bold", 15))
maxi.place(x=500, y=430)
max_temp = Label(root, text="...", width=0, bg='SteelBlue1', font=("bold", 15))
max_temp.place(x=630, y=430)
mini = Label(root, text="Min. Temp.: ", width=0, bg='SteelBlue1', font=("bold", 15))
mini.place(x=500, y=460)
min_temp = Label(root, text="...", width=0, bg='SteelBlue1', font=("bold", 15))
min_temp.place(x=630, y=460)
# 											 --:Note:--

note = Label(root, text="All temperatures in degree celsius", bg='SteelBlue1', font=("italic", 10))
note.place(x=550, y=495)
root.mainloop()

