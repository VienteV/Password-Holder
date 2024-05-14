import configparser

class Coding():
    
    config = configparser.ConfigParser()
    config.read('keyword.ini')
    key = config['key']['key']
    n = 65535
    
    def coding(self, password):

        key = self.key_len(password)
        password_numbers = [ord(i) for i in password]
        password_coded = [chr((password_numbers[i] + ord(key[i])) % self.n) for i in range(len(password_numbers))]
        return ''.join(password_coded)
    
    def decoding(self, cod_password):

        key = self.key_len(cod_password)
        cod_password_numbers = [ord(i) for i in cod_password]
        password_decoded = [chr((cod_password_numbers[i] - ord(key[i])) % self.n) for i in range(len(cod_password_numbers))]
        return ''.join(password_decoded)

    def key_len(self, password):
   
        if len(password) > len(self.key):
            key = self.key *(len(password) // len(self.key) + 1)
        else:
            key = self.key
        return key

    
