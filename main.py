#!/usr/local/bin/python2.7

import argparse

parser = argparse.ArgumentParser(description='helper amortization schedule')
parser.add_argument('-loan', type=float, help='current loan value', required=True)
parser.add_argument('-rate', type=float, help='current rate percentage', default=0.03)
parser.add_argument('-principal', type=float, help='current monthly principal', default=1381)
parser.add_argument('-v', help='verbose monthly', action='store_true')

args = parser.parse_args()

def p(before, a,b = 10):
  b += 1
  return ("%s${:<%d,.2f}" % (before, b)).format(a)

def p2(a,b = 10):
    return ("{:<%d,}" % b).format(a)

verbose = args.v
rate = args.rate
loan=args.loan
months = 0;
interest_paid = 0.0;
month = 1;

while loan > 0:
  months += 1;
  month_interest = (loan * rate) / 12.0;
  interest_paid += month_interest;
  loan -= args.principal - month_interest;
  if verbose and (months < 5 or months % (5 if months < 100 else 10) == 0):
    print "month", p2(month, 3), p("interest=", month_interest, 6), p("principal=", args.principal - month_interest, 8), p("total interest=", interest_paid, 9), p("remaining=", loan, 11);

  month += 1;

print p2(months,3), " months", p2(months/12.0, 3), p(" years. Total Interest paid: ", interest_paid)
