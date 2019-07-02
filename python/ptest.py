#!/usr/bin/env python3m
#encoding:utf-8
#第2行是告诉python，本程序采用的编码格式是utf-8;可以显示中文

#第1行是必须写的，它能够引导程序找到python的解析器，也就是说，
#不管你这个文件保存在什么地方，这个程序都能执行，而不用在前面指定python。
print ("this ptest.py aim to learning python")

import operator

def member_test():
    database = [ 
        ['albert','1234'],
        ['dilbert','4242'],
        ['qq','1234']
    ]
    username = input('User name:\n')
    pin = input('PIN code:')
    if [username,pin] in database: print('Access granted')
    
def display_topic():
    topic = input("display content:")
    topic_len = len(topic)
    screen_width = 80
    box_width = topic_len + 6
    leftwidth = (screen_width - box_width) // 2

    print ("")
    print (" " * leftwidth + '+' + '-' * box_width + '+')
    print (" " * leftwidth + '|' + " " * box_width + '|')
    print (" " * leftwidth + '|' + ' ' * 3 + topic + ' ' *3 + '|')
    print (" " * leftwidth + '|' + " " * box_width + '|')
    print (" " * leftwidth + '+' + '-' * box_width + '+')
    print ("")
    
def print_date():
    months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
    ]

    endings = ['st','nd','rd'] + 17 * ['th'] \
            + ['st','nd','rd'] + 7 * ['th']\
            + ['st']
    year = input('Year:') or "2019"
    month = input('Month (1-12):') or "5"
    day = input('Day (1-31):') or "13"
    month_number = int(month)
    day_number = int(day)

    month_name = months[month_number - 1]
    ordinal = day + endings[day_number - 1]
    print(month_name + ' ' + ordinal + ',' + year)
    
def math_test():
    ret = 0
    print ("print math test start:")
    a=-1
    #absolute value
    print ("a={},abs(a)={}".format(a,abs(a)))
    from cmath import sqrt
    a=9
    #square root
    print ("a={},cmath.sqrt(a)={}".format(a,sqrt(a)))

    #float test
    a="3.1415"
    b=float(a)
    print ("b={},type(a)={},type(b)={}".format(b,type(a),type(b)) )

    #math test
    from math import ceil
    from math import floor
    from math import sqrt
    a=4
    b=2.4
    c=2.6
    print ("ceil(2.4)={},floor(2.6)={},sqrt(4)={},pow(2,5)={}".format(ceil(b),floor(c),sqrt(a),pow(2,5)))

    #round test
    a=1.4
    b=1.5
    c=1.12345
    print ("round(1.4)={},round(1.5)={},round(1.12345,3)={}".format(round(a),round(b),round(c,3)))

    return ret

def string_test():
    ret=0
    print ("print string test start:")
    # print : set sep and end
    print ("print many sting","this one"+"+","this two.",sep="##",end="end \n")
    #print (ur"\u0062\n")
    print (r"1.stings surround '...' or \"...\"abc")
    print (r"2.escape way: use \ (slash) to escape;use r char to escape")
    print ("     now is \\ before \':\' ")    
    print ("3.joint way: joint two objects ,they must be same type(int or string)")
    num_1=123
    print ("     joint abc and 123 = " + "abc"  + str(num_1))
    print ("4.search and cut string")
    tests1="0123456789abcdef"
    
    print ("    tests1[0]={0}\n\
    tests1[3]={1}\n\
    tests1[3:7]={2}\n\
    tests1[:]={3}\n\
    tests1[:4]={4}\n\
    tests1[8:]={5}\n\
    str( len(tests1) )={6}\n\
    tests1*3={7}\n".format(tests1[0],tests1[3],tests1[3:7],tests1[:],tests1[:4],tests1[8:],\
    str(len(tests1)),tests1*3))

    print ("5.judge max min cmp in ")
    if 'a' in tests1:
        print (" a in tests1 string")
    else:
        print (" not in tests1 string")
    print (" max(tests1)={0}\n min(tests1)={1}\n".format(max(tests1),min(tests1)))
    tests2="0123456"
    tests3="0123456789abcdef123"
    print (" cmp(s1,s2)={0}\n cmp(s1,s3)={1}\n cmp(s1,s1)={2}\n".format(operator.eq(tests1,tests2),\
    operator.eq(tests1,tests3),operator.eq(tests1,tests1)))     
    print ("6.print 3 ways :")
    tests4="abcd1234"
    #字母占位符法:print maybe add the second parameter??
    print (" one print way is min=%d" % int(min(tests4)) +"\tmax={0}".format(max(tests4)) )
    #数字占位符的方法
    print (" two print s4={0}\tsizeof(s4)={2}\ttype(s4)={1}".format(tests4,type(tests4),len(tests4)))
    print ("{name} {} {id} {}".format(1,2,name=3,id=4))
        # print var e
    from math import e
    print ("Euler's constant is roughly {e}".format(e=e))
    print ("{name} is approximately {value:.4f}.".format(value=e,name="e"))
    import math
    print ("{md.__name__} module defines value {md.pi} for π".format(md=math))
    #字典格式化
    print (" three print s4=%(prog)s\tsizeof(s4)=%(sizestr)d" % {"prog":tests4,"sizestr":int(len(tests4))})
    print ("7.string input:")
    tests6=input("now input your name:\n") or 'unknown'
    print ("you input name is {0}".format(tests6))
    
    print ("lastly: string usual function:dir(str) help(str.count)")
    tests5="you-are-good!"
    s5_1=tests5.split("-")  #output is list type
    s5_2="#".join(s5_1) #covert list to string
    s5_3=s5_2.upper()
    print ("  raw="+tests5 + "\ts5_1=" + str(s5_1) + "\n  s5_2=" + str(s5_2) + "\ts5_3=" + str(s5_3))

    print ("8.string encoding:")
    #bytes(string, encoding[, errors])
    #convert string to bytes series
    a="convert string to bytes series"
    b=bytes(a,encoding="utf8")
    c=str(b,encoding="utf8")
    print ("a={},type(a)={},\nb={},type(b)={},\nc={},type(c)={}\
           ".format(a,type(a),b,type(b),c,type(c)))

    # changeable string
    x = bytearray(b"0123456")
    print ("before={}".format(x))
    x[2]=ord(b'a')
    print ("after={},type(x)={}".format(x,type(x)))
    
    
    
    return ret

"""
comment :
    alway ok
"""
def add_func(a,b):
    """
    add function help:
        add_func(num,num)
    """
    c = a + b
    print (c)
    return c
    
def fbs_func(f_n):
    ret=[0,1]
    for i in range(f_n-2):
        ret.append(ret[-2] + ret[-1])
    print (ret)
    # print num fbs 
    a,b=0,1
    for i in range(f_n):
        a,b=b,a+b
    print ("the {0} fbs is {1}".format(f_n,a))

def list_test():
    print ("list test start:")
    list_1=[0,'11',22,"33.free.com"]
    print ("    list_1="+str(list_1))
    print ("    type(list_1)={}".format(type(list_1)))
    print ("    index and cut ops:")
    print ("     index ops:   list_1[0]={0},  list_1[3]={1}".format(list_1[0],list_1[3]))
    print ("     cut ops:     list_1[1:]={0}, list_1[3][3:7]={1}".format(list_1[1:], \
    list_1[3][3:7]))
    print ("     cut ops:     list_1[-2:]={0}, list_1[-3:-2]={1}".format(list_1[-2:],list_1[-3:-2]))
    # reversed list:create new room space
    print ("    reversed ops:   list_1[::-1]={0},  list_1={1}".format(list_1[::-1],list_1))
    # list.reverse() do not create new room space
    print ("    reversed ops: list_1.reverse()={0},  list_1={1}".format(list_1.reverse(),list_1))

    #test long of step
    list_2=[0,1,2,3,4,5,6,7,8,9]  
    print ("    list_2="+str(list_2))
    print ("    list_2[1:9:2]={}\n     list_2[9:2:-2]={}\n     list_2[::-3]={}".format(\
         list_2[1:9:2],list_2[9:2:-2],list_2[::-3]))

    #test value assignment
    a = [0,1,2,3,4,5]
    b = list("abcdefg")
    print(" raw list ={}".format(a))
    a[1]="one step"
    print(" a[1] change list ={}".format(a))
    del a[1]
    print(" del a[1] list ={}".format(a))
    a[3:3]=b
    print(" cut a[3:3] add list ={}".format(a))
    # list way:
    #   append  :add a "value" in the end of list
    #   clear   :clear list all content
    #   copy    :make a list copy
    #   count   : count 'value' in list
    #   extend  :add list in the end
    #   index   :get 'value' 's location
    #   insert  :inside format is (x,'value')   x meams location
    #   pop  :del list last unit
    #   remove  :remove "value"
    #*   list.reverse() || reversed(list) :reverse list ;no ret
    #   list.sort() || sorted(list)    :sort list

    #   advanced sort()
    a = ['88888888','999999999','22','1','4444','333','55555']
    b=sorted(a)
    c=list(reversed(a))
    print(" raw list ={},\n sorted(a)={},\n list(reversed(a))={}\
        ".format(a,b,c))
    a.sort(key=len)
    print(" a.sort(key=len) list ={}".format(a))
    #others key: key=str.lower 
    # https://wiki.python.org/moin/HowTo/Sorting
    a.sort(key=len,reverse=True)
    print(" a.sort(key=len,reverse=True) ={}".format(a))
    
    
    # member test: x in list_2 ->true:false 
    #member_test()
    # "str" * num usage
    #display_topic()
    # list search usage
    #print_date()

    
def tuple_test():
    print ("tuple test start:")
    #a value tuple
    a=12,
    print (" a value tuple = {}\n type(a)={}".format(\
        a,type(a)))

    #cut and index
    tuple_1=(11,"tuple num 2",[3,"list 3 context",789],(44,"tuple 4 is dependable"))
    print ("     tuple_1="+str(tuple_1))
    print ("     tuple cut and search:")
    print ("         tuple_1[2:]={},tuple_1[2][2]={},tuple_1[-1][1]={}".format(tuple_1[2:],tuple_1[2][2],tuple_1[-1][1]))
    print ("     conversion list and tuple:")
    list_t=list(tuple_1)
    print ("         tuple_1->list_t={}".format(list_t))
    tuple_2=tuple(list_t)
    print ("         list_t->tuple_2={}".format(tuple_2))
def dict_test():
    print ("dict test start:")
    # 1. create dict
    print ("\n  1.1 normal create dict")
    weeks={"monday":11,"tuesday":22,"wednesday":33,"thursday":44,"friday":55,"saturday":66,"sunday":77}
    print ("  weeks dict ="+str(weeks))

    print ("  1.2 use tuple to create dict")
    tuptemp=(["master","12000"],["cashier","3500"])
    tupdict=dict(tuptemp)
    print ("   tuptemp={0}\n   tupdict={1}".format(tuptemp,(tupdict)))

    print ("  another way: ")
    tup2dict=dict(name="woker",Age=87,id="0532110")
    print ("   tup2dict" + str(tup2dict))

    print ("\n  1.3 use fromkeys create dict")
    fitness={}.fromkeys(("hight","weight","fitness"),"good")
    print ("  fitness={0}".format(fitness))
    # 2. add items
    
    print ("\n  2 add dict items")
    weeks["end-day"]="ff"
    print ("  weeks dict ="+str(weeks))

    # 3. change value
    
    print ("\n  3 change dict values")
    weeks["monday"]="01"
    print ("  weeks dict =" + str(weeks))
    
    
def parallel_iteration_test():
    print ("paralleal iteration test")
    # 1.a[i]+b[i]
    a=[1,2,3,4,5,6]
    b=[9,8,7,6,5,4]
    c=[]
    for i in range(len(a)):
        c.append(a[i]+b[i])
    print (" 1.a[i]+b[i] output new list:"+str(c))

    #2.use zip() function sloved
    d=[]
    for x,y in zip(a,b):
        d.append(x+y)
    print (" 2.zip(a,b):x+y="+str(d))

    #1.use list of num attach another str list
    a=[1,2,3,4,5]
    b=["lili","lucy","zlf"]
    c=[]
    nums=len(a) if len(a)<len(b) else len(b)
    for i in range(nums):
        c.append(str(a[i])+":"+str(b[i]))
    print (" 1.num list + str list ="+str(c))

    #2.use zip() way slove
    d=[]
    for x,y in zip(a,b):
        d.append(str(x)+":"+y)
    print (" 2.zip() slove way:"+str(d))

    #3.use zip() in dict
    weekstest={"monday":11,"tuesday":22,"wednesday":33,"thursday":44,"friday":55,"saturday":66,"sunday":77}
    reverseD={}
    for i,v in weekstest.items():
        reverseD[v]=i
    print (" 3. reverse dict"+str(reverseD))
    reverseT=dict(zip(weekstest.values(),weekstest.keys()))
    print ("  3.1 zip() in dict {0}".format(reverseT))

    #4. replace word in string
    youstring="I love you! you love me? you are so beautiful and goodness! I know you better than you know yourself"
    tmpyou=youstring.split(" ")
    replaceS="you"
    afterS="Wum"
    #
    for i in range(len(tmpyou)):
        if replaceS in tmpyou[i]:
            if replaceS == tmpyou[i]:
                tmpyou[i]=afterS
            else:
                cut=len(replaceS)
                tmpyou[i]=afterS + tmpyou[i][cut:]
    result=" ".join(tmpyou)    
    print (" 4.replace result:{0}".format(result))

    #for i, string in enumerate(tmpyou):
    afterS="wdd"
    rlen=len(replaceS)
    tmpyou=youstring.split(" ")
    for i,string in enumerate(tmpyou):
        if replaceS in string:
            rhead=string.find(replaceS)
            endstring=string[(rlen+rhead):]
            tmpyou[i]= string[:rhead]+afterS+endstring
            
    result=" ".join(tmpyou)    
    print (" 4.1.replace result:{0}".format(result))
    
    #5.print square (1-10)
    numsquare=[]
    for i in range(1,10):
        numsquare.append(i*i)
    print (" 5.(1-10) square:{0}".format(numsquare))
    #simple think;
    #  [x*x for x in range(10) if x 3 == 0] 
    #  [(x, y) for x in range(3) for y in range(3)]
    shortquare=[ x**2 for x in range(1,10)]
    print (" 5.1.(1-10) square:{0}".format(numsquare))

    #special statement
    #   pass :do nothing statement
    #   del :del a define of name
    #   exec :run python statement
    #   eval :caculate result of numbers ,and return it

    pass
    
    a=b="defined name"
    del a
    #print ("type(a)={},type(b)={},{}".format(type(a),type(b),b))

    #exec same name b ,but do not replace ?
    print ("b={}".format(b))
    exec("b=1") 
    print ("exec b={}".format(b))
    
    tmp={"x":4}
    exec("y=8",tmp)
    print ("dict tmp={}".format(list(tmp)))
    
    eret=eval("7+8*2")
    print ("eval()={}".format(eret))

    xret=eval("x*x*x",tmp)
    print ("eval('x*x*x',tmp)={}".format(xret))
    

def class_test():
    #add (object) after class name  say it new class
    class Bird(object):
        x=2
        y=[1,2,#test
        3]
        def __init__(self,name="Unknown",id=1,cname="Bird"):
            self.name=name
            self.__encapData()
            self.id=id
            self.cname=cname
            
        def getName(self):
            return self.name
            
        def Color(self,color="none"):
            print ("%s Bird color is %s" % (self.name ,color))
            
        def Age(self,n=1):
            self.num=n
        #   xx.SetLocation((10,77))    
        def SetLocation(self,xy):
            self.latitude, self.longitude = xy
            
        def GetLocation(self):
            return self.latitude, self.longitude
        Location=property(GetLocation,SetLocation)    
        def PrintAge(self):
            print ("{0} is {1} years old".format(self.name,self.num))
        def __encapData(self):
            self.__name="encapsulation"
        @property
        def get__name(self):
            return self.__name

    class Magpie(Bird):
        #re define old function
        def __init__(self,name="Magpie",id=2,cname="xique"):
            Bird.__init__(self,name="Magpie",id=2,cname="xique")
            self.sound = 'Squawk'
        def Color(self,color):
            #super(Magpie,self).Color("green")
            super().Color("green")
            self.LegColor = "black"
            print ("{} Leg Color is {}".format(self.name,self.LegColor))
        @staticmethod
        def static():
            print ("xiatian static function")
        @classmethod
        def clmethod(cls):
            print ("class method in {}".format(cls.y))
        
    print ("Class test")
    #in new instance, new Var replace old Var
    BirdX=Bird('XXX')
    BirdX.x+=1
    print ("BirdX.x={},Bird.x={}".format(BirdX.x,Bird.x))
    #in new instance, changing Var [list] is not only in this instance
    BirdX.y.append(4)
    print ("BirdX.y={},Bird.y={}".format(BirdX.y,Bird.y))

    #display default value
    print ("BirdX.name={},BirdX.id={},BirdX.cname={}".format(BirdX.name,BirdX.id,BirdX.cname))

    #others
    BirdX.Age(90)
    BirdX.Color("red")
    BirdX.PrintAge()
    BirdX.SetLocation((23.12,105.12))
    print (BirdX.GetLocation())

    #property test
    BirdX.Location = 12.56,60.25
    print (BirdX.Location)
    
    #inherit
    X1=Magpie()
    X1.Age(100)
    X1.Color("green")
    X1.PrintAge()   
    
    #class method and static method
    X1.static()
    X1.clmethod()
    
    Magpie.static()
    Magpie.clmethod()

    #encapsulation data and read it;notic get__name do not have ()
    print ("encapData is {}".format(BirdX.get__name))

# below 4 function is store name to  dict ,and find it first middle last name 
def dict_init(data):
    data["first"] = {}
    data["middle"] = {}
    data["last"] = {}

def dict_lookup(data,label,name):
    return data[label].get(name)

def dict_store(data, full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1," ")
    labels = 'first','middle','last'

    for label,name in zip(labels, names):
        people = dict_lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]
def test_dict_search():
    mynames = {}
    dict_init(mynames)
    dict_store(mynames, "kit liu hong")
    result = dict_lookup(mynames, 'middle', 'liu')
    
    print ("data = {}".format(mynames))
    print ("search result = {}".format(result))
def trace_exception():
    print ("trace exception function")
    muffled = False
    try:
        print("try get error in x / y")
        x = int(input("enter x:"))
        y = int(input("enter y:"))
        print(x/y)
    except ZeroDivisionError:
        if muffled:
            print(" y can't be zero")
        else:
            raise ValueError
#raise ... from ... exception context ???:
# except statement will only exec one of them
    except ValueError as e:
        print ("it is not number")
        print (e)
        pass
    except (ZeroDivisionError, TypeError, NameError):
        print ("enter many except error")
    except Exception as e:
# catch all except
        print ("some except error happend:{}".format(e))
    else:
# not except happened
        print ("not except happened")
# always run finally        
    finally:
        print ("Enter finally progress")
    
#search number in a sequence : half of separate  way
def search_num(seq, want):
    lower=0
    upper=len(seq)-1
    #print ("seq = {} want = {} lower = {} upper = {}".format(seq,want,lower,upper))
    if (lower == upper) or (want == seq[upper]):
        if want == seq[upper]:
            return 1
        else:
            return -1
    else:
    # maybe plus 1 or 2 can find out number?
        if upper % 2 == 0 :
            middle = (lower + upper + 2) // 2
        else:
            middle = (lower + upper + 1 ) // 2
    #print ("middle = {}".format(middle))
    if want > seq[middle]:
        seq = seq[middle:]
    elif want == seq[middle]:
        return 1
    else:
        seq = seq[:middle]
    return search_num(seq,want)
    
def calc_heat_index(T, RH):
    '''NOAA计算体感温度 参数为气温(摄氏度)和相对湿度(0~100或者0~1)'''
    import math
    if RH < 1:
        RH *= 100
    T = 1.8 * T + 32
    HI = 0.5 * (T + 61 + (T - 68) * 1.2 + RH * 0.094)
    if HI >= 80:  # 如果不小于 80华氏度 则用完整公式重新计算
        HI = -42.379 + 2.04901523 * T + 10.14333127 * RH - .22475541 * T * RH \
             - .00683783 * T * T - .05481717 * RH * RH + .00122874 * T * T * RH \
             + .00085282 * T * RH * RH - .00000199 * T * T * RH * RH
        if RH < 13 and 80 < T < 112:
            ADJUSTMENT = (13 - RH) / 4 * math.sqrt((17 - abs(T - 95)) / 17)
            HI -= ADJUSTMENT
        elif RH > 85 and 80 < T < 87:
            ADJUSTMENT = (RH - 85) * (87 - T) / 50
            HI += ADJUSTMENT
    return round((HI - 32) / 1.8, 2)

__name__ = "traceException"
#function skills:
# specify name args: 
#       store(patient='Mr. Brainsample', hour=10, minute=20, day=13, month=5) 
#       def hello_3(greeting='Hello', name='world'):
# collect args:
#       def print_params(*params):
#       def in_the_middle(x, *y, z):
#       def print_params_3(**params):  print_params_3(x=1, y=2, z=3)
#       def print_params_4(x, y, z=3, *pospar, **keypar):  print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)
# separate args:
#   tuple separate:
#       def add(x, y):
#       params = (1, 2)
#       add(*params)
#   dict separate:       
#       params = {'name': 'Sir Robin', 'greeting': 'Well met'}
#       hello_3(**params)
# reconnect full variable:
#   def xxx():   global x_var
if __name__ == "add":
    add_func(2,7)
elif __name__ == "math":
    math_test()
elif __name__ == "string":
    string_test()
elif __name__ == "tuple":
    tuple_test()
elif __name__ == "fbs":
    fbs_func(10)
elif __name__ == "main":
    fbs_func(19)
elif __name__ == "list":
    list_test()
elif __name__ == "dict":
    dict_test()
elif __name__ == "PI_test":
    parallel_iteration_test()
elif __name__ == "class":
    class_test()
elif __name__ == "dict_search":
    test_dict_search()
elif __name__ == "traceException":
    trace_exception()
elif __name__ == "search_n":
    a = [n for n in range(1,20) ]
    print ("a={}".format(a))
    for num in range(1,20):
        ret = search_num(a,num)
        print ("search {} result = {}".format(num,ret))
elif __name__ == "temperature"     :
    t=input("input temperature(0-100):")
    s=input("input relative humidity(0-100):")
    ret = calc_heat_index(float(t),float(s))
    print ("temperature:{}℃ relative humidity:{}% result={}".format(t,s,ret))
else:
    print ('not run function')

