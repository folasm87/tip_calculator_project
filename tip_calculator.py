#cost is cost of the meal
cost = float(raw_input("The cost of the meal is $"))
tax = float(raw_input("The Tax is $"))
tax_value = tax
meal_with_tax = cost + tax
tip_rate = float((raw_input("The tip is %")))
tip_rate /=100
tip = (tip_rate*(meal_with_tax))
tip_value = tip
total = meal_with_tax + tip_value
print "The base cost of your meal was ${0}".format("%0.2f" % cost)
print "You need to pay ${0} for tax".format("%0.2f" % tax)
print "Tipping at a rate of {0}%, you should leave ${1} for a tip.".format("%0.2f" % (tip_rate*100),"%0.2f" %  tip)
print "The grand total of your meal is ${0}.".format("%0.2f" % (cost+tip+tax))

