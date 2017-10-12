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



    if lengteggl == lengtewoord:
        raad = input("Raad het woord met alle goed geraden letters:")
        if raad == woord:
            print("Je hebt het woord goed geraden!")

        else:
            input("Fout, probeer het nog een keer:")




    if lengte > 1:
        fouten += 1
        print("Druk op enter")
        input("Fout, probeer het nog een keer:")

    else:

        if vraag1 in gl:
            print("Je hebt deze letter al geraden al geraden probeer nog een keer.")


        elif vraag1 in woord:
            ggl.append(vraag1)
            print("Goed geraden!")
            print("Dit zij alle geraden letters: " + str(gl))
            print("Dit zijn je goed geraden letters: " + str(ggl))

        elif vraag1 == "?":
            raad = input("Raad het woord:")

        elif vraag1 not in woord:
            gl.append(vraag1)
            fouten += 1
            print("Druk op enter")
            vraag2 = input("Fout, probeer het nog een keer:")
            print("Dit zij alle geraden letters: " + str(gl))
            print("Dit zijn je goed geraden letters: " + str(ggl))
            if vraag1 in gl:
                gl.remove(vraag1)
            print("Druk op enter")



        if fouten == 1:
            print("""
                    |
                    |
                    |
                    |
                    |
                    |""")
        elif fouten == 2:
            print("""
                    ________
                    |
                    |
                    |
                    |
                    |
                    |
                    """)
        elif fouten == 3:
            print("""

                ________
                |/
                |
                |
                |
                |
                |




                """ )

        elif fouten == 4:
            print("""

                ________
                |/  |
                |
                |
                |
                |
                |
                """)

        elif fouten == 5:

            print("""

                ________
                |/  |
                |  ( )
                |  \|/
                |  / \
                |
                |
                """)


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
                einde =input("Je hebt 5 fouten kies stop om te stoppen.")
                if einde == "stop":
                    break
