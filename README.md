#### Hello everyone! So, i made the community made "plugin" for python to use functionality of the whitelists
> WARNING: This is **not a real plugin**, you need to** install file with plugin first**!
    Also, this only supports **username and password whitelists**, but i will inplement this soon anyway (this means you cant add, remove, whitelist and blacklist people in hwid or ip whitelists)
# Preparing
Firstly, you need to install the file with class you need to use
1. Download the [file in github](https://github.com/alexbomb6666/yaris-example) (yaris.py)
2. Place it in your project directory
3. Add this code to your main .py file: (you need )
```python
import requests
from yaris import Yaris
yaris = Yaris()
yaris.set_public_key(***Your whitelist public key here***) #place your public whitelist key here
yaris.set_private_key(***Your whitelist private key here***) #place your private key here
```
### Reminder
>To use "plugin", you need to install "requests" plugin. To do so, open the console in your code editor and write:
```bash
pip install requests
```
***
# Commands
#### All commands from this message to other message, that says "End of private key requirement cmds" requires to have private key set up. (ohhh my bad english strikes again)
### Reminder
>Almost every command can return json code, that you can use to get the info about the action
```python
json = #command
print(json)
```


Our "plugin" has commands on how to use them. (you need the private key to use it)

## get_wl_info
This command will return your whitelist info 
Example:
```python
print(yaris.get_wl_info())
```
it will give you something like this:
```json
{'information': {'id': '1', 'owner': '76654', 'name': 'Test', 'description': 'yes', 'type': 'Username + Password'}}
```

### Reminder
>To learn how to get the info from json you need to just put the json in variable and give computer the path
```python
json = yaris.get_wl_info() #creating variable with json
print(json['information']['name'])# Will give the name of the whitelist.
print(json['information']['type']) # Will give the type of the whitelist.
# and etc.
```

## add_user(username, password, role)
This command will add a player to your whitelist (you need the private key to use it)
Example:
```python
yaris.add_user("Tetunus", "1111", "Developer")
```

## remove_user(username)
This command will remove the player from your whitelist (again, you need the private key for it)
Example:
```python
yaris.remove_user("Tetunus")
```

## blacklist_user(username, reason)
This command will blacklist user (or just suspend)
Example:
```python
yaris.blacklist_user("Sidge", "Retard lol")
```

### Reminder
> This command won't suspend or blacklist user from your services by itself. You need to use some code to set up (spoiler: just check the returned json from log_in(username, password) for blacklist part of json)

## whitelist_user(username)
This command will basically whitelist user, so your service won't mark his as blacklisted and he will be able to use it
Example:
```python
yaris.whitelist_user("Sidge")
```

#### End of private key requirement cmds
## log_in(username, password)
The name of the command explains itself
Example:
```python
yaris.add_user("Sidge", "1111", "Some dumb dude")
print(yaris.log_in("Sidge", "1111")) # Will give success json
print(yaris.log_in("Sidge", "1234")) # Will give an error since invalid password
```

### Reminder
> You need to use a variable or print() to ensure if logging in is success or failure.

#### That's all! No need to credit me if you are going to use my improvised plugin, but feel free to thank me or ask for a question/help in comments!
