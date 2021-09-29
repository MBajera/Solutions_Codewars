def make_readable(seconds):
    output = [0,0,0]
    if seconds >= 3600:
        output[0] = int(seconds/3600)
        seconds -= 3600 * output[0]
    if seconds >= 60:
        output[1] = int(seconds / 60)
        seconds -= 60 * output[1]
    output[2] = seconds
    ans = ""
    for item in output:
        if item < 10:
            ans += "0"+str(item)+":"
        else:
            ans += str(item) + ":"
    return ans[:-1]

print(make_readable(86399), "23:59:59")
print(make_readable(359999), "99:59:59")
