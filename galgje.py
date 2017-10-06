woord = "zak"
# letters = ["z","a","k"]
ggl = []
gl = []
fouten = 0
print ("Welkom bij")
print ("""
           __      __    __     __    ____  ____
          / _)    /__\  (  )   / _)  (_  _)(____)
         ( (_-.  /(__)\  )(__ ( (_-..-_)(   )__)
          \___/ (__)(__)(____) \___/\____) (____)""")

while True:
    
    vraag1 =  input("Kies een letter of kies een ? om het woord te raden:")
    lengte = len(vraag1)
    if lengte > 1:
        input("Fout, probeer het nog een keer:")
        fouten += 1
    else:

        if vraag1 in woord:
            ggl.append(vraag1)
            print("Goed geraden!")
            print("Dit zij alle geraden letters: " + str(gl))
            print("Dit zijn je goed geraden letters: " + str(ggl))

        elif vraag1 == "?":
            raad = input("Raad het woord:")

        elif vraag1 not in woord:
            gl.append(vraag1)
            input("Fout, probeer het nog een keer:")
            print("Dit zij alle geraden letters: " + str(gl))
            print("Dit zijn je goed geraden letters: " + str(ggl))
            fouten += 1

        

            if raad == woord:
                print("Je hebt het woord goed geraden!")
                break



