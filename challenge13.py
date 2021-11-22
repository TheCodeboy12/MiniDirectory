from challenge1 import PKCS
from Crypto.Cipher import AES
import random
import json
import base64
#we make a json with user data
def write_to_json(filename:str,data:dict):
    with open(filename+'.json','w') as data_file:
        json.dump(kwargs,data_file,indent=4)
    return f'The file have been written to the json file {filename}'
class Directory():    
    def __init__(self,name:str,masterpassword):
        cipher=AES.new(PKCS(bytes(masterpassword,'ascii'), 16),AES.MODE_ECB)
        self.cipher=cipher
        masterpassword=cipher.encrypt(PKCS(bytes(masterpassword,'ascii'),16))
        self.masterpassword=masterpassword
        self.name=name
        # self.db={
        #     'users':[],
        #     'uids':[],
        #     'passwords':[],
        #     'roles':[]
        # }
        
        with open('secrets-'+name+'.json','w') as secrets:
            json.dump({self.name:
            {
                'masterpassword':base64.b64encode(masterpassword).decode('utf-8')}
                }, secrets,indent=4)
                
        return None

    
    def encode(self,uid):
        return f"email={self.db['users'][uid]}@{self.name}.com&uid={self.db['uids'][uid]}&role={self.db['roles'][uid]}"
    
    def check_before_adding_to_db(self,user_id):
        if user_id in self.db['users']:
            return False
        else:
            return True
    
    def encrypt(self,param):
        return self.cipher.encrypt(PKCS(bytes(param,'ascii'),16))
    
    def decrypt(self,param,user):
        assert user.role=='PASSWORD','NOT ADMIN'
        return self.cipher.decrypt(param)
        
    def change_role(userObject,role):
        #role should be from a predefined list
        userObject.role=role
        print(f'the role of {userObject.uid} has been changed to {role}')
        
        
    def add_user(self,username,password,role):
        assert username.isalnum() and password.isalnum() and role.isalnum(),'You are not allowed to use special charecters!'
        if self.check_before_adding_to_db(username)==True:
            self.db['users'].append(self.encrypt(username))
            self.db['passwords'].append(self.encrypt(password))
            self.db['roles'].append(self.encrypt(role))
            self.db['uids'].append(self.db['users'].index(self.encrypt(username)))
        elif self.check_before_adding_to_db(username)==False:
            print('User already exists!')
    class User:
        def __init__(self,uid,password):
            self.id=uid
            self.password=password
            self.role=None
        def Superadmin(self):
            self.role='Admin'
            print('You are now an Admin')


sf=Directory('sf415','PASSWORD')

