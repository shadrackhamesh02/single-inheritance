# Single inheritance

class brands :
    brandname1 ='Facebook'
    brandname2 ='Amazon'
    brandname3 ='Youtube'
    brandname4 ='Github'

class products(brands):             # base class
    productuse1 ='Social media'
    productuse2 ='Online shopping'
    productuse3 ='Video blog'
    productuse4 ='Developer platform' 

obj = products()                    # derived class
print(obj.brandname1,'is an',obj.productuse1)
print(obj.brandname2,'is an',obj.productuse2)
print(obj.brandname3,'is an',obj.productuse3)
print(obj.brandname4,'is an',obj.productuse4)