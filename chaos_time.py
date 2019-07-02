import time


def show_time(hour,minute,seconds):
    if hour < 10:
        hour = "0" + str(hour)
    hour = str(hour)
    if minute < 10:
        minute = "0" + str(minute)
    minute = str(minute)
    if seconds < 10:
        seconds = "0" + str(seconds)
    seconds = str(seconds)

    print("\r" + f'{hour}:{minute}:{seconds}', end='')


# 倒计时
def countdown(countdown_time = "01:01:03"):
    temp = countdown_time.split(":")
    hour,minute,seconds = int(temp[0]),int(temp[1]),int(temp[2])

    while True:
        seconds = seconds - 1
        time.sleep(1)
        if seconds < 0:
            minute = minute - 1
            seconds = 59
            if minute < 0:
                hour = hour - 1
                minute = 59

        # 显示时间
        show_time(hour, minute, seconds)

        if hour == 0 and minute == 0 and seconds == 0:
            break



def main():
    countdown()


if __name__ == '__main__':
    main()