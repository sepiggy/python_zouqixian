#!/usr/bin/python

if 1>2:
    print "ok"
print "ok"

if True:
    print "True"

if 1+1:
    print 2

if 1-1:
    print 0

def fun():
    return 0

if fun():
    print "ok"
else:
    print "bad"


x = int(raw_input("please input a number: "))
y = int(raw_input("please input a number: "))

if x>=90:
    if y>=90:
        print 'a'
    print "x>=90"
elif x>=80:
    print 'b'
elif x>=70:
    print 'c'
else:
    print 'bad !!!'

