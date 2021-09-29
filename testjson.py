import json
class User:
        def __init__(self,uid,password):
            self.id=uid
            self.password=password
            self.role=None
        def Superadmin(self):
            self.role='Admin'
            print('You are now an Admin')
        def write_to_json(self,jsonfile):
            newData={
                self.id:{
                        'email':self.id+'@uber.com',
                        'password':self.password,
                }
            }
            with open(jsonfile+'.json','w') as data_file:
                json.dump(newData, data_file,indent=4)

gabe=User('Gabe', 'Gabe12121')
gabe.write_to_json('test')