#!/usr/bin/python2.7
d = {'Adam':95,
     'Lisa':85,
     'Bart':59}
print d
print "Adam:", d['Adam']
print "Lisa:",d['Lisa']
print "Bart:",d['Bart']
print d['Adam']
print
print
print d
print len(d)
print d['Adam']
print d.get('Paul')
d = {'Adam':95,
     'Lisa':85,
     'Bart':59,
     'Paul':75}
print d
print len(d)
print d.get('Bart')
dic = {95:'Adam',
       85:'Lisa',
       59:'Bart'}
print dic[95]

d = {'Adam':95,
     'Lisa':85,
     'Bart':59}
print d
d['Paul'] = 72
print d
d['Bart']=60
print d

d = {95:'Adam',
     85:'Lisa',
     59:'Bart'}
d[72] = 'Paul'
print d
for key in d:
    print key

d = {'Adam':95,
     'Lisa':85,
     'Bart':59}
for key in d:
    print key,":",d[key]

