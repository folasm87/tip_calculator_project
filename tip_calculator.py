from optparse import OptionParser
parser = OptionParser()
parser.add_option("-c", "--cost", dest="cost", help="the cost of the meal", type="float")
parser.add_option("-x", "--tax", dest="tax", help="the tax rate", type="float")
parser.add_option("-t", "--tip_rate", dest="tip_rate", help="The tip in terms of percentage", type="float", default= 10.00)
(options, args) = parser.parse_args()
if not (options.cost and options.tax): 
    parser.error("You need to supply arguments for the cost AND tax")
cost = options.cost
tax = options.tax
tax_value = (tax/100)  * cost
meal_with_tax = cost + tax_value
tip_rate = options.tip_rate
tip_value = (tip_rate/100) * (meal_with_tax)
total = meal_with_tax + tip_value
print "The base cost of your meal was ${0}".format("%0.2f" % cost)
print "You need to pay ${0} in tax for a rate of {1}%".format("%0.2f" % tax_value, "%0.2f" % tax)
print "Tipping at a rate of {0}%, you should leave ${1} for a tip.".format("%0.2f" % tip_rate,"%0.2f" %  tip_value)
print "The grand total of your meal is ${0}.".format("%0.2f" % total)