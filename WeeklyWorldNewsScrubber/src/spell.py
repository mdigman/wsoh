import enchant
d = enchant.Dict("en_US")
a = "Dollar Jackpot"
for each in a.split(' '):
    print d.check(each)
print d.check("Dollar")
print d.check("Egypt")
print d.check("nickel")