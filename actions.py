import json 
from encoding import Coding


class PasswordHolder():
    file_name = 'passwords.json'
    cod = Coding()

    def take_from_file(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            passwords = json.load(file)
        return passwords

    def write_to_file(self, passwords_dict):
        with open(self.file_name, 'w', encoding='utf-8') as file: 
                json.dump(passwords_dict, file, indent=4)
        
    
    def incert(self, password, from_what):
        
        password = self.cod.coding(password)
        dict_to_write = {from_what: password}
        try:
            passwords_dict = self.take_from_file()
        except:
            passwords_dict = {}
        finally:
            passwords_dict[from_what] = password
            self.write_to_file(passwords_dict)
            
    def take(self):
        with open(self.file_name, 'r') as file:
            passwords = json.load(file)
            for i in passwords:
                passwords[i]= self.cod.decoding(passwords[i])
        return passwords

    def dell_one(self, name):
        password_dict = self.take_from_file()
        del password_dict[name]
        self.write_to_file(password_dict)

    def update_one(self, name, new_password):
        password_dict = self.take_from_file()
        password_dict[name] = self.cod.coding(new_password)
        self.write_to_file(password_dict)
        
a = PasswordHolder()

a.incert('aaaa2231ва','3123олжр1')
a.take()
