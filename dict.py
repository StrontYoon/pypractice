# dictionary is internal data type that usage tops python with LIST
#Rooting for hash table, contains data consisted with key and value
#As dictionary is mutability data type, you can decl

#type of dict
ymt = {"shipno": 1, "shipname": 'yamato', "reigon": 'sakura_empire'}
mss = {"shipno": 2, "shipname": 'musasi', "reigon": 'sakura_empire'}
snn = {"shipno": 3, 'shipname' : 'shinano', "reigon": 'sakura_empire'}

#vacant dict
#{}
#dict()


#can input tuple into dict
#dict([("name", "사용자"), ("email", "user@test.com"), ("age", 25)])


#can put tuple to dict by key
snn["shiptype"] = 'BB'


#can get value by key [var][[key]]
print(snn['shiptype'])

#if you use irrelevant key, returns KeyError
#so use .get([key],[default]) to prevent
print(snn.get('shiptype', 'CVL'))

#can update dict by new declaration
snn['shiptype'] = 'CV'
print(snn.get('shiptype', 'BB'))


#multiple data outputs
for key in snn: #using for + fstring
    print(f"{key}: {snn[key]}") # note after here!

#

#fstring?
#if you use f-string with {}, can put variable into expression
print(f'hi {snn["shipname"]}!') #in this case, must be different quotes!
#it is equal to snn["shipname"].__str__() 

#if you need __repr__() value
print(f'hi {snn["shipname"]!r}!')

#if you need to print var name and value (shorter ver.)
num = 1
print(f"{num=}")






# __init__ > method that class execute first
#__str__ > makes different types into string type, makes type compatible
#__repr__ > simply data to string

'''
class test:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hello, my name is {self.name}"


a = 1
b = "hi"
c = [1, 2, 3]
test_ = test("fox")

print(a, b, c, test_)
# 1 hi [1, 2, 3] Hello, my name is fox 출력
'''


#if __name__ == "__main__":
'''namespace == range differentiates obj
python, literally everything is an obj!
to allow same object name, namespace exists.

파이썬 파일을 커맨드라인이나 인터페이스를 통해 직접 실행한 경우
__name__에는 __main__이라는 값(네임스페이스)이 설정됩니다.

하지만 파이썬 파일을 모듈로서 사용, 즉 다른 파일에서 불러와 사용하는 경우
__name__에는 모듈 이름이 설정됩니다.

정리하자면 if __name__ == "__main__" 은 해당 구문이 사용된 파이썬 파일을 직접 실행했을 때만 아래 코드를 실행하겠다 라는 의미입니다.

이는 파이썬 개발자들이 저지를 수 있는 실수를 막아줍니다.

print(__name__)
'''

