from pynput.keyboard import Listener, Controller, Key

keyboard = Controller()
buffer = ""

def on_press(key):
    global buffer
    try:
        char = key.char  # Get the character of the key pressed
        if char:
            buffer += char  # Append the key to the buffer
            if buffer.endswith("a.."):
                # Simulate deleting "a.."
                for _ in range(3):  # Backspace 3 times
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
                buffer = ""  # Clear the buffer
                keyboard.type("ä")  # Type the replacement character

            if buffer.endswith("o.."):
                # Simulate deleting "o.."
                for _ in range(3):  # Backspace 3 times
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
                buffer = ""  # Clear the buffer
                keyboard.type("ö")  # Type the replacement character

            if buffer.endswith("u.."):
                # Simulate deleting "u.."
                for _ in range(3):  # Backspace 3 times
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
                buffer = ""  # Clear the buffer
                keyboard.type("ü")  # Type the replacement character

            if buffer.endswith("A.."):
                # Simulate deleting "A.."
                for _ in range(3):  # Backspace 3 times
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
                buffer = ""  # Clear the buffer
                keyboard.type("Ä")  # Type the replacement character

            if buffer.endswith("O.."):
                # Simulate deleting "O.."
                for _ in range(3):  # Backspace 3 times
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
                buffer = ""  # Clear the buffer
                keyboard.type("Ö")  # Type the replacement character

            if buffer.endswith("U.."):
                # Simulate deleting "U.."
                for _ in range(3):  # Backspace 3 times
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
                buffer = ""  # Clear the buffer
                keyboard.type("Ü")  # Type the replacement character

            if buffer.endswith("sss"):
                # Simulate deleting "sss"
                for _ in range(3):  # Backspace 3 times
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
                buffer = ""  # Clear the buffer
                keyboard.type("ß")  # Type the replacement character

            if buffer.endswith("SSS"):
                # Simulate deleting "SSS"
                for _ in range(3):  # Backspace 3 times
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
                buffer = ""  # Clear the buffer
                keyboard.type("ß")  # Type the replacement character

    except AttributeError:
        pass  # Ignore special keys

with Listener(on_press=on_press) as listener:
    print("Listening for key presses...")
    listener.join()
