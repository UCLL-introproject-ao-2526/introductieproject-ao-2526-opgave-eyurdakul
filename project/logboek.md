## 18 April 2026 09:00

Ik ben gestart met de ontwikkeling van mijn Blackjack-game in Python. Hiervoor heb ik inmiddels de projectstructuur opgezet door een specifieke folder aan te maken in mijn repository. Daarnaast ben ik begonnen met het doornemen van de Pygame-documentatie.

## 18 April 2026 10:18

Ik heb een basisframework opgezet voor mijn Blackjack-game. Ik heb een venster gemaakt met behulp van Pygame en een achtergrondkleur ingesteld. Daarnaast heb ik een eenvoudige game loop geïmplementeerd die het venster open houdt totdat de gebruiker het sluit. Nu krijg ik een error screen = pygame.display.set_mode((800, 600)) TypeError: size must be a number. Ik ga dit verder onderzoeken en oplossen.

## 18 April 2026 10:18

Ik kreeg "TypeError: size must be a number" omdat ik de size parameter niet correct had gedefinieerd. Het zou een array moeten zijn. Na het corrigeren van de code naar screen = pygame.display.set_mode([800, 600]) werkt het nu correct. In tutorial was pygame.init() niet opgeroepen waardoor font niet correct werkte. Na het toevoegen van pygame.init() werkt het nu correct. Ik heb al belangrijke methodes toegevoegd en nu is het tijd om de game logica te implementeren.

## 19 April 2026 12:10
Ik heb de tutorial tot het einde gevolgd en wil nu extra functionaliteiten toevoegen. Ik weet niet zeker of ik de bestaande code moet wijzigen of helemaal opnieuw beginnen. De bestaande code heeft geen object-georiënteerde structuur, wat het moeilijk maakt om nieuwe functionaliteiten toe te voegen. Ik denk dat het beter is om helemaal opnieuw te beginnen met een object-georiënteerde aanpak, zodat ik de code beter kan organiseren en uitbreiden in de toekomst. Ik zal dit vragen aan mijn lector voordat ik een beslissing neem.