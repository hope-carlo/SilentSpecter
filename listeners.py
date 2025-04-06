from pynput import keyboard, mouse

class KeyboardMouseListener:
    def __init__(self):
        self.keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
        self.mouse_listener = mouse.Listener(on_click=self.on_click, on_scroll=self.on_scroll)

    def start(self):
        self.keyboard_listener.start()
        self.mouse_listener.start()

    def stop(self):
        self.keyboard_listener.stop()
        self.mouse_listener.stop()

    def on_key_press(self, key):
        try:
            print(f"Key: {key.char}")
        except AttributeError:
            print(f"Special Key: {key}")

    def on_click(self, x, y, button, pressed):
        print(f"Mouse {'pressed' if pressed else 'released'} at {(x, y)} with {button}")

    def on_scroll(self, x, y, dx, dy):
        print(f"Scrolled at {(x, y)} with delta {(dx, dy)}")
