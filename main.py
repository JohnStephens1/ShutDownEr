import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import os
import time


# my old code, it hurts xd
def get_time():
	while True:
		fancy_time = tk.simpledialog.askstring("ShutDownEr", "Please enter a time.")

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


def fancy_time_to_formatted_time(time):
	if len(time) <= 2:
		return time + "s"
	elif len(time) <= 4:
		return time[:-2] + "m:" + time[-2:] + "s"
	elif len(time) <= 6:
		return time[:-4] + "h:" + str(time)[-4:-2] + "m:" + str(time)[-2:] + "s"


# wth even is this
def word_4_a_friend_of_course(sleep):
	if sleep:
		return "sleep"
	else:
		return "shutdown"


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
	time = get_time()
	seconds = fancy_time_to_seconds(time)
	formatted_time = fancy_time_to_formatted_time(time)
	sleep = tk.messagebox.askyesno("ShutDownEr", "pls chos yes 4 slep & no 4 shutzown pls im lazy sorrrieee D:")
	run = tk.messagebox.askyesno("ShutDownEr", "Confirm {mode} in {seconds} aka {pretty_time}.".format(
		mode=word_4_a_friend_of_course(sleep), seconds=str(seconds) + " seconds", pretty_time=formatted_time))
	if run:
		run_command(sleep, seconds)
	else:
		tk.messagebox.showinfo("ShutDownEr", "GREATFUCKINGJOBMANWELLFUCKINGDOWNUGH")


main()
