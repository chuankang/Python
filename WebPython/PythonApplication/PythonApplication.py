
#自定义函数
#def power(x,n):
#    s = 1
#         while n > 0:
#             n = n - 1
#             s = s * x
#             return s

#print(power(23,2));

#def power(x):
#    return x*x;
#print (power(5));

#age = 3
#if age >= 18:
#    print('your age is', age)
#    print('adult')
#else:
#    print('your age is', age)
#    print('teenager')

#age = 3
#if age >= 18:
#    print('adult')
#elif age >= 6:
#    print('teenager')
#else:
#    print('kid')

#sum = 0
#for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#    sum = sum + x
#print(sum)

###获取当前日期和时间
##导入datetime类
#from datetime import datetime
#now =datetime.now()
##输出2018-06-22 09:39:40.100139
#print(now)
##输出<class 'datetime.datetime'>
#print(type(now))
#dt = datetime(2018,6,22,9,41)
#print(dt)
#print(dt.timestamp()) #时间戳

###集合类
##namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
#from collections import namedtuple
#Point = namedtuple('point',['x','y'])
#p = Point(1,2)
#print(p.x)

##base64
#import base64
#s = base64.b64encode(b'connsun')
#print(s)
#c =base64.b64decode(b'Y29ubnN1bg==')
#print(c)

##struct
#import struct
#k = struct.pack('>I',10240099)
#print(k)

##XML
#from xml.parsers.expat import ParserCreate
#class DefaultSaxHandler(object):
#    def start_element(self,name,attrs):
#        print('sax:start_element:%s' % (name,str(attrs)))
#    def end_element(self, name):
#        print('sax:end_element: %s' % name)

#    def char_data(self, text):
#        print('sax:char_data: %s' % text)

#xml = r'''<?xml version="1.0"?>
#<ol>
#    <li><a href="/python">Python</a></li>
#    <li><a href="/ruby">Ruby</a></li>
#</ol>
#'''
#handler = DefaultSaxHandler()
#parser = ParserCreate()
#parser.StartElementHandler = handler.start_element
#parser.EndElementHandler = handler.end_element
#parser.CharacterDataHandler = handler.char_data
#parser.Parse(xml)




