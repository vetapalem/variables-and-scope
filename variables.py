#camal case
myPro='new project'
#pascal case
MyName='kiwi'
#snake case
my_er_one='trail'

#multiline declaration
a,b,c=50,80,90
# packing
print(a,b,c)

# One Value to Multiple Variables
d=e=f=45
# print(d,e,f)

#unpacking most important consept
a=[1,2,3,'hello']
g,h,i,j=a
# print(g,h,i,j)

#example 1
#unpacking
ab=[chr(a) for a in range(65,65+26)]
k,l,m,*n=ab
# print(k,l,m,n,sep='\n')
# print(type(n).__name__)

# def au():
#     return 'hello'
# def bu():
#     return 'bye'
# def cu():
#     return 'have a good day'
# for fun in frozenset({au(),bu(),cu()}):
#     print(fun)

def power(num):
    def find_power(p):
        res=num**p
        print('{} of {} is {}'.format(num,p,res))
        return res
    return find_power
def main():
    pow=power(int(input('number:-')))
    r1=pow(int(input('number:-')))
    # print(r1)
# main()
c={a:chr(a) for a in range(65,65+12)}
d=tuple([a for a in range(10)])
def trail(*args,**kwargs):
    print(args,kwargs,sep='\n')
trail(*d,**c)
    