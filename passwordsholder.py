import json 
from encoding import Coding


class PasswordHolder():
    file_name = 'passwords.json'
    cod = Coding()
    def incert(self, password, from_what):
        
        password = self.cod.coding(password)
        print(password)
        dict_to_write = {from_what: password}

        try:
            with open(self.file_name, 'r') as file:
                passwords_dict = json.load(file)
                print(passwords_dict)
        except:
            passwords_dict = {}
        finally:
            with open(self.file_name, 'w', encoding='UTF-8') as file: 
                passwords_dict[from_what] = password
                json.dump(passwords_dict, file, indent=4)
            
    def take(self, site=''):
        with open(self.file_name, 'r') as file:
            passwords = json.load(file)
            for i in passwords:
                passwords[i]= self.cod.decoding(passwords[i])
        return passwords
        
    def take_one(self, site=''):
        passwords = self.take(self, site)
        if passwords.get(site, False):
            return passwords[site]
        else: 
            return 'Такого сайта нет'    

    def take_all(self):
        passwords = self.take(self)
        passwords = '\n'.join(map(lambda a: ': '.join(a), passwords.items()))
        return passwords
        
a = PasswordHolder()

a.incert('aaaa2231ва','3123олжр1')
a.take()
