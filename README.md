# PINNACLE_LABS-Keylogger_Software
The following repository documents the Keylogger Software task assigned during a Cybersecurity Internship at Pinnacle Labs

# Objective
Develop a keylogger software to track keystrokes and monitor user input, emphasizing security research and protection against keyloggers

# Features
- **Start and Stop Keylogger:** The application provides a simple control menu to start and stop the keylogger.
- **Multi-File Logging:** Logs keystrokes into two distinct files:
  - **Version 1 Log:** Captures all keystrokes in a straightforward text log.
  - **Version 2 Log:** Captures keystrokes with additional formatting for special keys like space, enter, tab, and backspace.
- **Cross-Platform Support:** Compatible with both Windows and Unix-based systems for clearing the console screen.
- **Graceful Exit:** Ensures the keylogger stops logging upon exiting the application.

# Installation
1. Ensure you have Python installed on your system.
2. Install the required dependency `pynput` using the following command:
    ```bash
    pip install pynput
    ```
3. Clone or download this repository to your local machine.

# Usage
1. Navigate to the project directory.
2. Run the `main.py` script to start the application:
    ```bash
    python main.py
    ```

# Modules

## main.py
The main script that provides a command-line interface for starting and stopping the keylogger. It includes a control menu to manage the keylogging process.

## keylogger.py
Contains the `KeyLogger` class, which handles the setup, start, and stop functionalities of the keylogger. It logs keystrokes into two files and formats special keys for better readability in the logs.

### Key Functions:
- `start()`: Starts the keylogging process.
- `stop()`: Stops the keylogging process.
- `on_press(key)`: Logs the key press event.
- `on_release(key)`: Stops the keylogger when the escape key is pressed.

## file_manager.py
Provides a utility function to write keystrokes to the version 2 log file, ensuring that special keys are appropriately formatted.

## config.py
Contains configuration settings, such as the names of the log files used by the keylogger.

# Logging
- **version1_log.txt:** Logs every key press as it occurs.
- **version2_log.txt:** Logs keys with specific formatting for special characters like space, enter, tab, and backspace for improved readability.

# Disclaimer
This project is intended for educational purposes only. The use of keylogging software can be illegal and unethical if used without explicit permission. Please ensure you comply with all applicable laws and regulations when using this software.
