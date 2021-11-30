def deleted(text):
  if text.count(" ")>0:
    text = text.replace(" "," ")
    text = text.upper()
  else:
    text = "TEKSTS NESATUR VAJADZĪGO BURTU."
  return text
