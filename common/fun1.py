def total_amount(principle, years):
    rate = 3.61 # interest is 3.61%
    si = principle * rate * years / 100
    total = si + principle
    return total

# use - calling
# ans = total_amount(1000, 5)
# print(ans)