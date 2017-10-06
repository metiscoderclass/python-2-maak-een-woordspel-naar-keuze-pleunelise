woord = ["zak"]
letters = ["z","a","k"]
ggl = ["",""]
gl = ["",""]
fouten = 0
print ("Welkom bij")
print ("""
           __      __    __     __    ____  ____
          / _)    /__\  (  )   / _)  (_  _)(____)
         ( (_-.  /(__)\  )(__ ( (_-..-_)(   )__)
          \___/ (__)(__)(____) \___/\____) (____)""")

vraag1 =  input("Kies een letter of kies een ? om het woord te raden:")
if vraag1 == letters:
    print("Goedzo, je hebt een letter goed geraden")
    gl + vraag1
     
print ("Dit zijn je goed geraden letters: " + ggl)
print ("Dit zij alle geraden letters: " + gl)



