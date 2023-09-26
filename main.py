import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import os
import time


def get_time() -> str:
	time = str

	while True:
		time = tk.simpledialog.askstring("ShutDownEr", "Please enter a time: HH:MM:SS")
		if time == "":
			return str(0)
		elif 1000000 > int(time) >= 0 or time == "":
			return time
		else:
			tk.messagebox.showinfo("ShutDownEr", "Now bruv u didn't get how dis works now didja bruv, eh?.")


def convert_time_2_seconds(time) -> int:
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


def convert_time_2_pretty_time(time) -> str:
	if len(time) <= 2:
		return time + "s"
	elif len(time) <= 4:
		return time[:-2] + "m:" + time[-2:] + "s"
	elif len(time) <= 6:
		return time[:-4] + "h:" + str(time)[-4:-2] + "m:" + str(time)[-2:] + "s"


def word_4_a_friend_of_course(schleep) -> str:
	if schleep:
		return "sleep"
	else:
		return "shutdown"


def run_command(schleep, seconds) -> None:
	time.sleep(seconds)
	if schleep:
		os.system("shutdown -h")
	else:
		os.system("shutdown -s -t 0")
	# if schleep:
	# 	time.sleep(seconds)
	# 	os.system("shutdown -h")
	# else:
	# 	os.system("shutdown -s -t {} -c ''".format(seconds))


def main():
	time = str
	pretty_time = str
	schleep = bool
	run = bool

	tk.Tk().withdraw()
	time = get_time()
	seconds = convert_time_2_seconds(time)
	pretty_time = convert_time_2_pretty_time(time)
	schleep = tk.messagebox.askyesno("ShutDownEr", "pls chos yes 4 slep & no 4 shutzown pls im lazy sorrrieee D:")
	run = tk.messagebox.askyesno("ShutDownEr", "Confirm {mode} in {seconds} aka {pretty_time}.".format(
		mode=word_4_a_friend_of_course(schleep), seconds=str(seconds) + " seconds", pretty_time=pretty_time))
	if run:
		run_command(schleep, seconds)
	else:
		tk.messagebox.showinfo("ShutDownEr", "GREATFUCKINGJOBMANWELLFUCKINGDOWNUGH")


main()
