## Table of Contents
1. [Quick Overview](#quick-overview)
2. [Let's Go Through An Example](#lets-go-through-an-example)
   1. [The Time Formatting](#the-time-formatting)
   2. [Hibernate or Shut Down](#hibernate-or-shut-down)
   3. [The Nice Thing...](#the-nice-thing)
3. [How to Install](#how-to-install)
4. [More Tools From Me](#more-tools-from-me)
5. [Support](#support)


## Quick Overview

What is _ShutDownEr_?

- **Enter a time** in an intuitive format
- **Confirm mode.** The default is hibernate, the alternative is shutdown
- **Confirm process.** E.g. 'confirm sleep in 69h 4m 20s'
- **Enjoy the final window.** Subtle in design, depicting the remaining time until shutdown. Simply close this to abort operation.

More details about the time formatting etc. below :)

## Let's Go Through An Example

Upon starting _ShutDownEr_ we're greeted with this window.

![greeting](readme-images/greeting.PNG)

### The Time Formatting

What makes _ShutDownEr_ unique is the way the time is formatted.

A table with examples should be clearer than any explanation:

| Input  | Rendered Time |
|--------|---------------|
|        |               |
| 45     | 45s           |
| 130    | 1m 30s        |
| 4500   | 45m 00s       |
| 13000  | 1h 30m 00s    |
| 123456 | 12h 34m 56s   |

You can even enter things like 90 seconds or 90 minutes.

| Input | Rendered Time |
|-------|---------------|
|       |               |
| 90    | 1m 30s        |
| 9000  | 1h 30m 00s    |
| 9090  | 1h 31m 30s    |

You can also add spaces wherever you like, if that's what you're into.

| Input                         | Rendered Time |
|-------------------------------|---------------|
|                               |               |
| 13000                         | 1h 30m 00s    |
| 1 30 00                       | 1h 30m 00s    |
| &nbsp; 13 &ensp; 0 &ensp; 0 0 | 1h 30m 00s    |

Back to our example. Let's say we want to initiate a shutdown in 12h 34m 56s. So we enter:

![greeting-filled-out](readme-images/greeting-filled-out.PNG)

and hit _enter_ or click _OK_.
<br>

### Hibernate or Shut Down
The two primary modes _ShutDownEr_ operates in are shutting down normally or hibernating, with the latter being the default.
In case you didn't know, hibernating is like sleeping, saving the windows and processes running, but as opposed to sleeping, hibernating

- consumes next to no power
- as a trade-off, takes the same amount to start as a regular shutdown
- but most importantly, your computer doesn't decide to go on a rave in your absence.

Here's a table for a swift overview.


| type      | saves status | fast boot | low energy consumption | that one kid with untreated ADHD |
|-----------|--------------|-----------|------------------------|----------------------------------|
| shut down | &#9744;      | &#9744;   | &#9745;                | &#9744;                          |
| hibernate | &#9745;      | &#9744;   | &#9745;                | &#9744;                          |
| sleep     | &#9745;      | &#9745;   | &#9744;                | &#9745;                          |

This matter is clearly depicted in the following window:

![confirm-sleep](readme-images/confirm-sleep.PNG)

*just hit enter ok*

### Moving On xd

Then, _ShutDownEr_ informs us of the resulting time of the string we entered and asks us for confirmation.

![confirm-init-shutdown](readme-images/confirm-init-shutdown.PNG)

In this example you can clearly see why this time format is substantially simpler than entering the required seconds for example.
<br>

Since the formatted time is correct, let's hit _enter_ again.

![final-window](readme-images/final-window-updated.PNG)

And there we go! Shutdown is initiated, with the remaining time being visible in the title of the window.
Hovering over the windows icon in the taskbar shows us the remaining time as well.

There is also button to add five minutes to the timer, as well as a button to shut down/hibernate immediately.

To abort the shutdown, simply close the window, _ShutDownEr_ will then shut itself down instead *muhahaha*.

You can also quit _ShutDownEr_ by hitting the _Escape_ key.


### The Nice Thing...

...is how simple and flexible it is.

You can enter your desired time in a heartbeat because of the intuitive formatting, hit enter three times, and there ya go.

The remaining time is visible at any point, can be easily increased, and both cancellation and shutdown require but a single click.


## How to Install

Simply download `ShutDownEr.exe` from the _Releases_ section, and you're good to go! No installation required, not even Python.

The first time running the `.exe` file you might get a warning saying that the app isn't recognized since I haven't bought a license, but after clicking 'More Info' and 'Run anyway' the warning shouldn't pop up anymore.

Alternatively, if you prefer using Python to run the program instead, clone the repository and simply run main.py, no additional packages required.


## More Tools From Me

If you enjoyed _ShutDownEr_, feel free to check out my other quality-of-life tools, all free and open-source as well, no ads and no nonsense.

- _Timerrhymer_: https://github.com/JohnStephens1/Timerrhymer
- _4Focus_: https://github.com/JohnStephens1/4Focus

## Support

If you found any of them useful, sharing my tools with people who might profit them as well would be highly appreciated.

Alternatively, any and every donation would mean a lot and help me keep making more tools like them.

https://www.paypal.com/donate/?hosted_button_id=L4X2DFAYMJ72U