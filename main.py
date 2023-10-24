import os
import sys

from pathlib import Path
from functools import partial

import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

from utils.fancy_time_formatting import *
from utils.dark_title_bar import dark_title_bar


APPLICATION_PATH = Path(os.path.dirname(__file__) if getattr(sys, 'frozen', True) else os.path.dirname(sys.executable))
ICON_PATH = APPLICATION_PATH/'resources/tree.ico'


def get_fancy_time():
	while True:
		try:
			fancy_time = tk.simpledialog.askstring("ShutDownEr", "Please enter a time:")

			if fancy_time is None:
				sys.exit()

			fancy_time = fancy_time.replace(" ", "")

			if fancy_time == "":
				return "0"
			elif 1000000 > int(fancy_time) >= 0:
				return fancy_time
			else:
				raise ValueError
		except ValueError:
			tk.messagebox.showinfo("ShutDownEr", "Improper formatting.\n\nPlease enter up to six digits.")


def shutdown(sleep):
	if sleep:
		os.system("shutdown -h")
	else:
		os.system("shutdown -s -t 0")
		# os.system(f"shutdown -s -t {seconds} -c ''")


def add_five_minutes_to_timer(seconds_array):
	seconds_array[0] += 300


def set_timer_to_zero(seconds_array):
	seconds_array[0] = 0


def open_final_window(seconds, sleep):
	window_width = 400
	window_height = 150
	button_width = 14

	seconds_array = [seconds]

	window = tk.Tk()

	button_settings = {
		'master': window,
		'activebackground': 'grey',
		'fg': 'white',
		'bg': 'black',
		'font': 10,
		'width': button_width
	}

	window.iconbitmap(ICON_PATH)

	window.bind('<Escape>', lambda e: window.destroy())

	text = tk.StringVar()
	text.set('hi :3')

	label = tk.Label(
		master=window,
		textvariable=text,
		bg='black',
		fg='white',
		font=10)
	label.pack(pady=(10, 0))

	butt1 = tk.Button(text='+5 min', command=lambda: add_five_minutes_to_timer(seconds_array), **button_settings)
	butt2 = tk.Button(text='shutdown now', command=lambda: set_timer_to_zero(seconds_array), **button_settings)

	butt1.pack(side=tk.LEFT, padx=(30, 0), pady=(0, 20))
	butt2.pack(side=tk.RIGHT, padx=(0, 30), pady=(0, 20))

	window.title(f'{seconds_to_time_string(seconds)} - ShutDownEr')
	window.after(1000, partial(update_timer, window, seconds_array, text, sleep))

	window.config(bg='black')
	dark_title_bar(window)
	window.withdraw()
	window.deiconify()

	window.geometry(f"{window_width}x{window_height}-0+5")

	window.mainloop()


def update_timer(window, seconds_array, text, sleep):
	seconds = seconds_array[0]

	if seconds == 60 or seconds == 1:
		window.attributes('-topmost', True)
		window.attributes('-topmost', False)

		if seconds == 1:
			text.set('bye :3')
			window.update_idletasks()

	if seconds > 0:
		seconds_array[0] -= 1
		time_string = seconds_to_time_string(seconds_array[0])

		window.title(f'{time_string} - ShutDownEr')
		window.update()

		window.after(1000, partial(update_timer, window, seconds_array, text, sleep))
	else:
		shutdown(sleep)
		window.destroy()


def main():
	fancy_time = get_fancy_time()
	seconds = fancy_time_to_seconds(fancy_time)
	time_string = seconds_to_time_string(seconds)

	sleep = tk.messagebox.askyesno("ShutDownEr", "pls chos yes 4 slep & no 4 shutzown pls im lazy sorrrieee D:")

	if tk.messagebox.askyesno("ShutDownEr", f"Confirm {'sleep' if sleep else 'shutdown'} in {time_string} aka {seconds} seconds."):
		open_final_window(seconds, sleep)
	else:
		tk.messagebox.showinfo("ShutDownEr", "GREATFUCKINGJOBMANWELLFUCKINGDOWNUGH")


if __name__ == '__main__':
	main()
