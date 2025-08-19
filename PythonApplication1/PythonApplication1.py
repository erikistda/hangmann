import pygame
import sys

# Initialisiert Pygame (muss am Anfang stehen)
pygame.init()

# Definiert die Fenstergr��e
breite = 800
hoehe = 600
fenster = pygame.display.set_mode((breite, hoehe))

# Setzt den Titel des Fensters
pygame.display.set_caption("Mein erstes Pygame-Fenster")

# Die Hauptschleife des Spiels (Game Loop)
# Ohne diese Schleife w�rde das Fenster sofort wieder schliessen
running = True
while running:
    # �berpr�ft alle Ereignisse (Events), die passieren
    for event in pygame.event.get():
        # Wenn das Ereignis "Fenster schliessen" ist (Klick auf X)
        if event.type == pygame.QUIT:
            running = False # Beendet die Schleife

    # F�llt den Hintergrund mit einer Farbe (hier: Farbe in RGB)
    fenster.fill((250, 250, 000))

    # Aktualisiert den gesamten Bildschirm, um �nderungen anzuzeigen
    pygame.display.flip()

# Wenn die Schleife beendet ist, wird das Programm geschlossen
pygame.quit()
sys.exit()
