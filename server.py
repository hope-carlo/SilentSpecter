
BANNER = r"""
   _____ _ _            _        _____                  _             
  / ____| (_)          | |      / ____|                | |            
 | (___ | |_  ___ _ __ | |_ ___| (___   ___  ___   ___ | | _____ _ __ 
  \___ \| | |/ _ \ '_ \| __/ _ \\___ \ / _ \/ __| / _ \| |/ / _ \ '__|
  ____) | | |  __/ | | | ||  __/____) |  __/\__ \| (_) |   <  __/ |   
 |_____/|_|_|\___|_| |_|\__\___|_____/ \___||___(_)___/|_|\_\___|_|   

        Remote Access Toolkit | by Ethical Hackers, for Hackers
"""
print(BANNER)

import Pyro4
from rat.agent import RAT

def main():
    daemon = Pyro4.Daemon()
    uri = daemon.register(RAT(auth_token="my_secure_token"))
    print("RAT ready. URI:", uri)
    daemon.requestLoop()

if __name__ == "__main__":
    main()
