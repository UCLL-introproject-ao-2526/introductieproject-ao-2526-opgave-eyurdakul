## 18 April 2026 09:00

Ik ben gestart met de ontwikkeling van mijn Blackjack-game in Python. Hiervoor heb ik inmiddels de projectstructuur opgezet door een specifieke folder aan te maken in mijn repository. Daarnaast ben ik begonnen met het doornemen van de Pygame-documentatie.

## 18 April 2026 10:18

Ik heb een basisframework opgezet voor mijn Blackjack-game. Ik heb een venster gemaakt met behulp van Pygame en een achtergrondkleur ingesteld. Daarnaast heb ik een eenvoudige game loop geïmplementeerd die het venster open houdt totdat de gebruiker het sluit. Nu krijg ik een error screen = pygame.display.set_mode((800, 600)) TypeError: size must be a number. Ik ga dit verder onderzoeken en oplossen.

pygame.init() was niet in tutorial, nodig voor font etc
size moet een array zijn.