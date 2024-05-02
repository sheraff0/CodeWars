def cuckoo_clock(initial_time, n):
    def tick():
        nonlocal hours, minutes
        plus_hour, minutes = divmod(minutes + 15, 60)
        hours += plus_hour
        if hours > 12:
            hours -= 12

    def cuckoo():
        nonlocal n
        n -= hours if minutes == 0 else 1

    hours, minutes = map(int, initial_time.split(":"))
    if minutes % 15 == 0:
        cuckoo()
    minutes = minutes // 15 * 15

    while n > 0:
        tick()
        cuckoo()

    return ":".join(map("{:02}".format,  (hours, minutes)))


if __name__ == "__main__":
    cuckoo_clock("03:38", 19)
