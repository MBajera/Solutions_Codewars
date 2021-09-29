def format_duration(seconds):
    if seconds == 0:
        return "now"
    time = [[0 ,'second'],[0, 'minute'], [0, 'hour'], [0,'day'], [0,'year']]
    units = [60,60,24,365, seconds+1]
    i = 0
    while seconds >= units[i]:
        time[i][0] = seconds % units[i]
        seconds = int(seconds/units[i])
        i += 1
    time[i][0] = seconds
    ans = []
    for elem in time[::-1]:
        if elem[0] > 0:
            if elem[0] > 1:
                ans.append(f"{elem[0]} {elem[1]}s")
            else:
                ans.append(f"{elem[0]} {elem[1]}")
    if len(ans) < 2:
        return ans[0]
    else:
        for x in range(len(ans)):
            if x == len(ans)-1:
                pass
            elif x == len(ans)-2:
                ans[x] += ' and'
            else:
                ans[x] += ','
    return ' '.join(ans)
