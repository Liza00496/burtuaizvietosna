def deleted(text):
  if text.count("e")>0:
    text = text.replace("e"," ")
    text = text.upper()
  else:
    text = "TEKSTS NESATUR VAJADZĪGO BURTU."
  return text
