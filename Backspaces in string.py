def clean_string(s):
    ans = ""
    for dig in s:
        if dig == "#":
            if len(ans) > 0:
                ans = ans[:-1]
        else: ans += dig
    return ans