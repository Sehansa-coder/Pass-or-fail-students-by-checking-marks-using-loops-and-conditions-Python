# we use '**' to show that there can be many keywords
def person(name:str,**details):
    print("My name is ",name)
    print(details)
person("sehansa",age=18,city="colobmo")