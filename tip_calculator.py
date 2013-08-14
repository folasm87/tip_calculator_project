#import sys
#cost is cost of the meal
#cost = float(raw_input("The cost of the meal is $"))
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-f", "--cost", dest="cost", help="the cost of the meal", type="float")
parser.add_option("-s", "--tax", dest="tax", help="the tax in $", type="float")
parser.add_option("-t", "--tip_rate", dest="tip_rate", help="The tip in terms of percentage", type="float", default= 10.00)
(options, args) = parser.parse_args()
if not (options.cost and options.tax): 
    parser.error("You need to supply arguments for the cost and tax")
#cost = sys.argv[1]
cost = options.cost
cost = float(cost)
#tax = float(raw_input("The Tax is $"))
#tax = sys.argv[2]
tax = options.tax
tax = float(tax)
tax_value = tax
meal_with_tax = cost + tax
meal_with_tax = meal_with_tax
#tip_rate = float((raw_input("The tip is %")))
#tip_rate = float(sys.argv[3])
tip_rate = options.tip_rate
tip_rate /=100
tip = (tip_rate*(meal_with_tax))
tip_value = tip
total = meal_with_tax + tip_value
print "The base cost of your meal was ${0}".format("%0.2f" % cost)
print "You need to pay ${0} for tax".format("%0.2f" % tax)
print "Tipping at a rate of {0}%, you should leave ${1} for a tip.".format("%0.2f" % (tip_rate*100),"%0.2f" %  tip)
print "The grand total of your meal is ${0}.".format("%0.2f" % (cost+tip+tax))

