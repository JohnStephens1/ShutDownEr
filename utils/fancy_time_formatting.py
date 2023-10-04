def fancy_time_to_seconds(fancy_time):
    total_seconds = 0

    for pos, digit in enumerate(reversed(f'{fancy_time}')):
        total_seconds += int(digit) * 6 ** (pos // 2) * 10 ** ((pos + 1) // 2)

    return total_seconds


def split_up_seconds(seconds):
    total_minutes, seconds = divmod(seconds, 60)
    total_hours, minutes = divmod(total_minutes, 60)
    days, hours = divmod(total_hours, 24)

    return days, hours, minutes, seconds


def seconds_to_time_string(seconds):
    days, hours, minutes, seconds = split_up_seconds(seconds)

    time_string = ''
    if days:
        time_string = f'{days}d '
    if hours or days:
        time_string += f'{hours}h '
    if minutes or hours or days:
        time_string += f'{minutes}m '
    time_string += f'{seconds}s'

    return time_string


def seconds_to_compact_time_string(seconds):
    days, hours, minutes, seconds = split_up_seconds(seconds)

    time_string = ''
    if days:
        time_string = f'{days}d'
    if hours:
        time_string += f'{hours}h'
    if minutes:
        time_string += f'{minutes}m'
    if seconds or not time_string:
        time_string += f'{seconds}s'

    return time_string
