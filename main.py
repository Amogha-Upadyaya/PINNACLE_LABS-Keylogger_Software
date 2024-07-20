from keylogger import KeyLogger
import time
import os

def clear_screen():
    # Clear console screen for better readability
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    keylogger = KeyLogger()
    while True:
        clear_screen()
        print("\nKEYLOGGER CONTROL MENU:\n1. Start Keylogger\n2. Stop Keylogger\n3. Exit")
        try:
            opt = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("\nInvalid Input. Please enter a number between 1 and 3.")
            time.sleep(1)
            continue
        
        if opt == 1:
            if keylogger.listener is None or not keylogger.listener.running:
                keylogger.start()
                print("\nKeylogger Started")
            else:
                print("\nKeylogger is already running")
        
        elif opt == 2:
            if keylogger.listener is not None and keylogger.listener.running:
                keylogger.stop()
                print("\nKeylogger Stopped")
            else:
                print("\nKeylogger is not running")
        
        elif opt == 3:
            if keylogger.listener is not None and keylogger.listener.running:
                keylogger.stop()
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice. Please try again.")
        
        time.sleep(1)

if __name__ == "__main__":
    main()