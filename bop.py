# pip install pypiwin32
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice").Speak
speak("Hello, I am your enemy. I will now irritate you: ")
while True:
	try:speak(__import__('random').choice(['bop', 'dop','pop']))
	except KeyboardInterrupt:print('No!')
	except SystemExit:print('No!!!')
