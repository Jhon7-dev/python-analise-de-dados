lockdown = True
din = 30
status = 'Em casa ' if lockdown and din <= 100 else 'irra!'
print(status)