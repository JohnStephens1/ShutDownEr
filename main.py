import os
import time
from sys import exit

import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

# TODO
#  add window post init_shutdown(), closing results in aborted shutdown
#  window starts minimized
#  make window display remaining time
#  add warning for over x seconds once reaching y creates warning 'shutting down in y seconds'


def get_fancy_time():
	while True:
		try:
			fancy_time = tk.simpledialog.askstring("ShutDownEr", "Please enter a time:")

			if fancy_time is None:
				exit()

			fancy_time = fancy_time.replace(" ", "")

			if fancy_time == "":
				return "0"
			elif 1000000 > int(fancy_time) >= 0:
				return fancy_time
			else:
				raise ValueError
		except ValueError:
			tk.messagebox.showinfo("ShutDownEr", "Improper formatting.\n\nPlease enter up to six digits.")


def fancy_time_to_seconds(fancy_time):
	total_seconds = 0

	for pos, digit in enumerate(reversed(f"{fancy_time}")):
		total_seconds += int(digit) * 6 ** (pos // 2) * 10 ** ((pos + 1) // 2)

	return total_seconds


def split_up_seconds(seconds):
	total_minutes, seconds = divmod(seconds, 60)
	total_hours, minutes = divmod(total_minutes, 60)
	days, hours = divmod(total_hours, 24)

	return days, hours, minutes, seconds


def seconds_to_time_string(seconds):
	days, hours, minutes, seconds = split_up_seconds(seconds)

	time_string = ""
	if days:
		time_string = f"{days}d"
	if hours:
		time_string += f"{hours}h"
	if minutes:
		time_string += f"{minutes}m"
	if seconds or not time_string:
		time_string += f"{seconds}s"

	return time_string


def initialize_shutdown(seconds, sleep):
	time.sleep(seconds)

	if sleep:
		os.system("shutdown -h")
	else:
		os.system("shutdown -s -t 0")
		# os.system(f"shutdown -s -t {seconds} -c ''")


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
