cost = 20.00
tax = 3.00
tip_rate = .15
tip = (tip_rate*(cost + tax))
print "The base cost of your meal was ${0}".format("%0.2f" % cost)
print "You need to pay ${0} for tax".format("%0.2f" % tax)
print "Tipping at a rate of {0}%, you should leave ${1} for a tip.".format("%0.2f" % (tip_rate*100),"%0.2f" %  tip)
print "The grand total of your meal is ${0}.".format("%0.2f" % (cost+tip+tax))

