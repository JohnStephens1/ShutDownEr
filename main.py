import os
import time
import sys

from pathlib import Path
from functools import partial

import threading

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


def shutdown(seconds, sleep):
	time.sleep(seconds)

	if sleep:
		os.system("shutdown -h")
	else:
		os.system("shutdown -s -t 0")
		# os.system(f"shutdown -s -t {seconds} -c ''")


def initialize_shutdown(seconds, sleep):
	threading.Thread(target=shutdown, args=(seconds, sleep), daemon=True).start()

	open_final_window(seconds)


def open_final_window(seconds):
	# man do I hate tkinter ;-;
	window = tk.Tk()

	window.title('ShutDownEr')

	window.iconbitmap(str(ICON_PATH))

	# window.attributes("-topmost", True)
	# window.lift()
	# window.focus_force()
	window.attributes('-topmost', True)
	window.attributes('-topmost', False)
	window.lift()
	window.focus_force()

	window.bind('<Escape>', lambda e: window.destroy())

	label = tk.Label(window, bg='black', fg='white', text='hi :3', font=10)
	label.pack()

	window.title(f'{seconds_to_compact_time_string(seconds)} - Timerrhymer')
	window.after(1000, partial(update_timer, window, seconds))

	window.config(bg='black')
	dark_title_bar(window)
	window.withdraw()
	window.deiconify()

	window.geometry("400x150-0+5")

	window.mainloop()


def update_timer(window, seconds):
	if seconds == 60:
		window.attributes('-topmost', True)
		window.attributes('-topmost', False)

	if seconds > 0:
		seconds -= 1
		time_string = seconds_to_time_string(seconds)

		window.title(f'{time_string} - ShutDownEr')
		window.update()

		window.after(1000, partial(update_timer, window, seconds))
	else:
		# pass? race condition (with a full second buffer tho)
		sys.exit()


def main():
	fancy_time = get_fancy_time()
	seconds = fancy_time_to_seconds(fancy_time)
	time_string = seconds_to_time_string(seconds)

	sleep = tk.messagebox.askyesno("ShutDownEr", "pls chos yes 4 slep & no 4 shutzown pls im lazy sorrrieee D:")

	if tk.messagebox.askyesno("ShutDownEr", f"Confirm {'sleep' if sleep else 'shutdown'} in {time_string} aka {seconds} seconds."):
		initialize_shutdown(seconds, sleep)
	else:
		tk.messagebox.showinfo("ShutDownEr", "GREATFUCKINGJOBMANWELLFUCKINGDOWNUGH")


if __name__ == '__main__':
	main()
