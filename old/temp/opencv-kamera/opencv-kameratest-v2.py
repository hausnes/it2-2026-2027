# Source: https://pypi.org/project/opencv-python/
# Install: pip install opencv-python

import cv2

print('''
Dette programmet lar deg ta eit bilete via kameraet du har tilkobla maskina di.

Skriv inn:
- c (for å ta bilete)
- a (for å avslutte programmet)
''')

running = True

while running:
    choice = input("\nKva ynskjer du å gjere? (c for å ta bilete, a for å avslutte)\n")

    if choice == "a":
        running = False

    if choice == "c":
        print("Forsøker å ta eit bilete..")
        filename = input("Kva ynskjer du å ha som filnavn? (utan filtype, som .png): ")
        
        # Initialize the camera
        cam = cv2.VideoCapture(0)
        if not cam.isOpened():
            print("Kameraet kunne ikkje opnast. Ver venleg å sjekke tilkoblinga.")
            continue # The rest of this iteration will not run

        # Read input from the camera
        result, image = cam.read()

        # If input image is detected without any error, show and save the image
        if result:
            cv2.imshow("Webcam Image", image)
            filenameFull = filename + ".png"
            cv2.imwrite(filenameFull, image)
            cv2.waitKey(0)
            cv2.destroyWindow("Webcam Image")
        else:
            print("Klarte ikkje å ta biletet. Ver vennleg og forsøk igjen.")

        # Release the camera
        cam.release()
        print("Ferdig med å ta biletet. Sjekk om det blei som du ville, i mappa du køyrte programmet.")