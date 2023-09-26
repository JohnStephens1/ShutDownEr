import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import os
import time


# my old code, it hurts xd
def get_time():
	while True:
		fancy_time = tk.simpledialog.askstring("ShutDownEr", "Please enter a time:")

		if fancy_time == "":
			return str(0)
		elif 1000000 > int(fancy_time) >= 0 or fancy_time == "":
			return fancy_time
		else:
			tk.messagebox.showinfo("ShutDownEr", "Now bruv u didn't get how dis works now didja bruv, eh?.")


def fancy_time_to_seconds(time):
	seconds = 0

	for i in range(1, len(time) + 1):
		if i == 1:
			seconds += int(time[-i])
		elif i == 2:
			seconds += int(time[-i]) * 10
		elif i == 3:
			seconds += int(time[-i]) * 60
		elif i == 4:
			seconds += int(time[-i]) * 60 * 10
		elif i == 5:
			seconds += int(time[-i]) * 60 * 60
		elif i == 6:
			seconds += int(time[-i]) * 60 * 60 * 10

	return seconds


def fancy_time_to_formatted_time(fancy_time):
	if len(fancy_time) <= 2:
		return fancy_time + "s"
	elif len(fancy_time) <= 4:
		return fancy_time[:-2] + "m" + fancy_time[-2:] + "s"
	elif len(fancy_time) <= 6:
		return fancy_time[:-4] + "h" + str(fancy_time)[-4:-2] + "m" + str(fancy_time)[-2:] + "s"


def run_command(sleep, seconds):
	time.sleep(seconds)
	if sleep:
		os.system("shutdown -h")
	else:
		os.system("shutdown -s -t 0")
	# if sleep:
	# 	time.sleep(seconds)
	# 	os.system("shutdown -h")
	# else:
	# 	os.system("shutdown -s -t {} -c ''".format(seconds))


def main():
	tk.Tk().withdraw()  # what

	fancy_time = get_time()
	seconds = fancy_time_to_seconds(fancy_time)
	formatted_time = fancy_time_to_formatted_time(fancy_time)

	sleep = tk.messagebox.askyesno("ShutDownEr", "pls chos yes 4 slep & no 4 shutzown pls im lazy sorrrieee D:")

	if tk.messagebox.askyesno("ShutDownEr", f"Confirm {'sleep' if sleep else 'shutdown'} in {formatted_time} aka {seconds} seconds."):
		run_command(sleep, seconds)
	else:
		tk.messagebox.showinfo("ShutDownEr", "GREATFUCKINGJOBMANWELLFUCKINGDOWNUGH")


main()
