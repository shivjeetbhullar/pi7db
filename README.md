# scrypt (Simple String Encyption)
Simple string encyption package is written in python.</br>
`scrypt` is used for string encryption with password.
# INSTALLATION
Installation with pip
```sh
 $ pip3 install scryp
 ```
# Encrypt String
`encrypt()` function is used for  encrypt string. `encrypt("STRING","PASSWORD")` function takes 2 arguments. 1st Is string for encrypt and second is password string.
```python
from scryp import encrypt
encrypted_string = encrypt('my name','AStrongPassword')

print(encrypted_string)
```
###Output
```shell
5038525S5593225S1479200S5084750S4483825S5038525S4668725
```

# Decrypt String
`decrypt()` function is used for  encrypt string. `decrypt("STRING","PASSWORD")` function takes 2 arguments. 1st Is string for decrypt and second is password string.
```python
from scryp import encrypt,decrypt
encrypted_string = encrypt('my name','AStrongPassword')

decrypted_string = decrypt(encrypted_string,'AStrongPassword')
print(decrypted_string)
```
###Output
```shell
my name
```
