def sleep_in(weekday, vacation):
    return vacation or not weekday

print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(True, True))
print(sleep_in(False, True))
