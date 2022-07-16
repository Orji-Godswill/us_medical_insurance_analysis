import utils


lst1 = ['yes', 'yes', 'no', 'yes', 'no', 'no']
lst3 = ['200', '300', '250.214', '350', '600', '450.75']


obj = utils.PatientThatSmoke()

obj2 = utils.PatientsByRegion()


y = obj.charge(lst1, lst3)

x = obj2.region(lst1)

print(y[-1])
print(x['no'])

non_s = y[-1]/x['no']
print(non_s)
