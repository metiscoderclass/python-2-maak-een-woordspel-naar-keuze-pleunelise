woord = "zak"
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
    lengtewoord = len(woord)
    lengteggl = len(ggl)
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
            print("Dit zij alle geraden letters: " + str(gl))
            print("Dit zijn je goed geraden letters: " + str(ggl))
            vraag2 = input("Fout, probeer het nog een keer:")
            fouten += 1
            if vraag2 in woord:
                ggl.append(vraag2)
                print("Goed geraden!")
                print("Dit zij alle geraden letters: " + str(gl))
                print("Dit zijn je goed geraden letters: " + str(ggl))

            elif vraag2 not in woord:
                gl.append(vraag2)
                vraag2 = input("Fout, probeer het nog een keer:")
                print("Dit zij alle geraden letters: " + str(gl))
                print("Dit zijn je goed geraden letters: " + str(ggl))
                fouten += 1
            if fouten > 5:
                einde = input("Je hebt 5 fouten kies kies stop om te stoppen:")
                if einde == "stop":
                    break     
            
        if lengteggl == lengtewoord:
            raad = input("Raad het woord met alle goed geraden letters:")
            if raad == woord:
                print("Je hebt het woord goed geraden!")
                break
            else:
               input("Fout, probeer het nog een keer:")



