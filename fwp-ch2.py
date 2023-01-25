# Data Structures

"""
The standard library offers a rich selection of sequence types 
implemented in C:

Container sequences
    list, tuple and collections.deque can hold items of diff types

Flat sequences
    str, bytes, bytesarray, memoryview and array.array hold items of 
    one type

Container seq. hold 'references' to the objects they contain
Flat seq. physically store the value of each item within its own memory

Mutable seq
    list, bytearray, array.array, collections.deque and memoryview

Immutable seq
    tuple, str and bytes
"""

"""List Comprehensions"""

# example with a string
symbols = '$¢£§∞'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

#print(codes)
# [36, 162, 163, 167, 8734]

# same example with a list comprehension
symbols = '$¢£§∞'
codes = [ord(symbol) for symbol in symbols]
#print(codes)
# [36, 162, 163, 167, 8734]

# The ord() function returns an integer representing 
# the Unicode character.

"""
Listcomps vs. map and filter

listcomps do everything the map and filter functions do without
the contortions of the functionally challenged lambda

"""

symbols = '$¢£§∞'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
#print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
#print(beyond_ascii)

"""
Cartesian products
"""

colors = ["black", "white"]
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
# print(tshirts)
# this generates a list of tuples arranged by color, then size
#[('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'),
#('white', 'M'), ('white', 'L')]

for color in colors:
    for size in sizes:
        break
    # print((color, size))

# this generates the list as if the for loops were nested in the same order

"""
('black', 'S')
('black', 'M')
('black', 'L')
('white', 'S')
('white', 'M')
('white', 'L')
"""

tshirts = [(color, size) for size in sizes
                        for color in colors]
# print(tshirts)

#arranged by size, then color
# [('black', 'S'), ('white', 'S'), ('black', 'M'), 
# ('white', 'M'), ('black', 'L'), ('white', 'L')]

"""
Generator expressions

genexp saves memory because it yields items one by one using
the iterator protocol instead of building a whole list just to feed 
a constructor

** same syntax as listcomp but encolsed in parenthesis rather than brackets
"""

symbols = '$¢£§∞'
tuple(ord(symbol) for symbol in symbols)
# (36, 162, 163, 167, 8734)

import array
array.array('I', (ord(symbol) for symbol in symbols))
# array('I', [36, 162, 163, 167, 8734])


"""
Tuples as records

Tuples hold records: each item in the tuple holds the data for one field
and the position of the item give its meaning

"""

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ("Tokyo", 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
    ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    break
    # print('%s/%s' % passport)

for country, _ in traveler_ids:
    break
    # print(country)

# since we're not interested in the second term, we use _ a dummy var
# we assigned everything in line 123 in a single statement. Then at the
# last line the % operator assigned each item in the passport tuple

"""
Tuple unpacking
"""

# parallel assignment
lax_coordinates = (33.9425, -118.408056)
lattitude, longitude = lax_coordinates
# print(lattitude)
# print(longitude)

# prefixing an argument with a star when calling a function
# enables functions to return multiple values in a way that's
#convenient to the caller
# print(divmod(20, 8))
# (2, 4)
t = (20, 8)
# print(divmod(*t))
# (2, 4)
quotient, remainder = divmod(*t)
# print(quotient, remainder)
# (2, 4)

import os

_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
# print(filename)
# 'idrsa.pub'

"""
Nested tuple unpacking
"""

metro_areas = [
('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),  
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)), 
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)), 
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)), 
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

# print('{:15} | {:^9}  | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (lattitude, longitude) in metro_areas:
    if longitude >= 0:
        break
        # print(fmt.format(name, lattitude, longitude))


"""
Named Tuples

collections.namedtuple function is a factory that produces
subclasses of tuple enhanced with field names and a class name
"""

from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# print(tokyo)
# City(name='Tokyo', country='JP', population=36.933,
    #  coordinates=(35.689722, 139.691667))

tokyo.population
# 36.933
tokyo.coordinates
# (35.689722, 139.691667)
tokyo[1]
# 'JP'


from collections import namedtuple
employee = namedtuple('employee', 'name title location team')
Russel = employee('Russel', 'IT Engineer I', 'NY', 'IT')
Beth = employee('Beth', 'HR Generalist', 'Denver', 'People')
Randy = employee('Randy', 'Senior IT Engineer', 'Nova Scotia', 'IT')
Rudabega = employee('Rudabega', 'Sales Manager', 'Miami', 'Sales')

# print(Russel.title)

City._fields # _fields is a tuple with the field names of the class
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
delhi._asdict() # _asdict() returns a collections.OrderedDict built from the tuple
for key, value in delhi._asdict().items():
    break
    # print(key + ':', value)


"""
Slicing
"""

l = [10, 20, 30, 40, 50, 60]
# print(l[:2])
# [10, 20]
# print(l[2:])
# [30, 40, 50, 60]

s = 'bicycle'
# print(s[::3])
# # 'bye'
# print(s[::-1])
# # elcycib
# print(s[::-2])
# 'eccb'


invoice = """
... 0.....6..................................40......52.....55........
... 1909 Pimoroni PiBrella                  $17.50  3      $52.50
... 1489 6mm Tactile Switch x20             $4.95   2      $9.90
... 1510 Panavise Jr. - PV-201              $28.00  1      $28.00
... 1601 PiTFT Mini Kit 320x240             $34.95  1      $34.95
... """

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    break
    # print(item[UNIT_PRICE], item[DESCRIPTION])

"""
Assigning to slices"""

l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)
l[3::2] = [11, 22]
print(l)