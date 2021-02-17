import subprocess

subprocess.call(['adb', 'devices'])
subprocess.call(['adb', 'shell', 'input', 'touchscreen', 'swipe', '360', '1093', '330', '1093', '100'])
subprocess.call(['adb', 'shell', 'input', 'touchscreen', 'swipe', '350', '1093', '350', '100', '100'])
