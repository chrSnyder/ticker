# ticker.py
# this function takes a string and rolls it across one line of terminal output like a stock ticker one time. 


def ticker(text, windowSize, refreshLapse):
	text = " "*windowSize + text
	charLeft = len(text)
	for a in range(len(text)):
		text = text + " "*windowSize
		text = text.replace("\n", " ")
		print("\r"+str(charLeft )+": " +text[0:windowSize], end = "")
		char0 = text[0]
		text = text[1:] + char0
		time.sleep(refreshLapse)
		charLeft -=1
	print("")
