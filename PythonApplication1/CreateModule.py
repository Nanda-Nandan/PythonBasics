x=42
def spam():
    print('x is ',x)
def run():
    print('calling spam')
    spam()
print('running')
run()
#save this to moduletest.py variable, if in console type python3 module.py it will simple run it 
#output will be like running,calling spam,x is 42
#if u want to load it and run it just type
import moduletest
#it imports the file ,executes it and made all the content available for us
#we can use moduletest as variable
moduletest.x
moduletest.run()
#if you will declare a variable x in main module or we can say in console that x is different than moduletest.x,basically different modules have different scope
#another syntax
from moduletest import run
#but in this case only run functionality will work
run()#will work
spam()#wont work
x#wont work
#but as per normal process it loads module,executes all,stores everything in memory but only exposes the run function,so efficiency is same for 1st approach and 2nd
#we can verify that everything is in memory.Since we called run it worked,but internally run is calling spam,so if spam is not in memory then it should not have worked.since it is there
#in memory it worked,but unexposed

#import module is one time operation,if you will import second time nothing will happen
#since it stores the module in cache,we can check it
sys.module['moduletest']
#We can delete cache
del sys.module['moduletest']
#Fail of import statement
import moduletest
#if error will be like importerror no module named moduletest then its path error
#by default python searches for specific paths for import,we can find the path
import sys
sys.path
#so there is two way to solve this error
#in sys.path append the string in which directory your file is present,suppose my directory is parent directory of python path directory then i can write like
sys.path.append('..')
#but in this case we have to manually change path whenever we require to import this module
#we can avoid this by placing path in a temporary variable like below
env PYTHONPATH=.. python3#in bash shell,not in python cosole command
#then i can import my module from new set path

#the last two statement always run,so print running always prints when we will import,its not great idea,so we can add a check there
x=42
def spam():
    print('x is ',x)
def run():
    print('calling spam')
    spam()
if(_name_=='_main_'):
    print('running')
    run()

#so everymethod has _name_ property,if it is called from main like python3 moduletest.py it will execute the last two line,else only import will skip that
moduletest._name_


