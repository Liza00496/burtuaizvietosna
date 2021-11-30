text = input("Ievadi tekstu: ")
if text.count("e")>0:
  text = text.replace("e", " ")
  text = text.upper()
  print("Teksts: ", text)
else:
  text = "TEKSTS NESATUR VAJADZĪGO BURTU."
  print(text)