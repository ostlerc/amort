#!/usr/local/bin/python2.7

import argparse

parser = argparse.ArgumentParser(description='helper amortization schedule')
parser.add_argument('-loan', type=float, help='current loan value', required=True)
parser.add_argument('-escrow', type=float, help='current float value', default=210.96)

args = parser.parse_args()

def p(before, a,b = 10):
  b += 1
  return ("%s${:<%d,.2f}" % (before, b)).format(a)

def p2(a,b = 10):
    return ("{:<%d,}" % b).format(a)

rate=.03625;
loan=args.loan
months = 0;
interest_paid = 0.0;
month = 1;
escrow = args.escrow
monthly = 1501.05 - escrow;

while loan > 0:
  months += 1;
  month_interest = (loan * rate) / 12.0;
  interest_paid += month_interest;
  loan -= monthly - month_interest;
  if months < 5 or months % (5 if months < 100 else 10) == 0:
    print "month", p2(month, 3), p("interest=", month_interest, 6), p("principal=", monthly - month_interest, 8), p("total interest=", interest_paid, 9), p("remaining=", loan, 11);

  month += 1;

print "took", p2(months,3), " months", p2(months/12,3), p(" years. Total Interest paid:", interest_paid)
