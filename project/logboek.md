## 18 April 2026 09:00

Ik ben gestart met de ontwikkeling van mijn Blackjack-game in Python. Hiervoor heb ik inmiddels de projectstructuur opgezet door een specifieke folder aan te maken in mijn repository. Daarnaast ben ik begonnen met het doornemen van de Pygame-documentatie.

## 18 April 2026 10:18

Ik heb een basisframework opgezet voor mijn Blackjack-game. Ik heb een venster gemaakt met behulp van Pygame en een achtergrondkleur ingesteld. Daarnaast heb ik een eenvoudige game loop geïmplementeerd die het venster open houdt totdat de gebruiker het sluit. Nu krijg ik een error screen = pygame.display.set_mode((800, 600)) TypeError: size must be a number. Ik ga dit verder onderzoeken en oplossen.

## 18 April 2026 10:18

Ik kreeg "TypeError: size must be a number" omdat ik de size parameter niet correct had gedefinieerd. Het zou een array moeten zijn. Na het corrigeren van de code naar screen = pygame.display.set_mode([800, 600]) werkt het nu correct. In tutorial was pygame.init() niet opgeroepen waardoor font niet correct werkte. Na het toevoegen van pygame.init() werkt het nu correct. Ik heb al belangrijke methodes toegevoegd en nu is het tijd om de game logica te implementeren.

## 19 April 2026 12:10

Ik heb de tutorial tot het einde gevolgd en wil nu extra functionaliteiten toevoegen. Ik weet niet zeker of ik de bestaande code moet wijzigen of helemaal opnieuw beginnen. De bestaande code heeft geen object-georiënteerde structuur, wat het moeilijk maakt om nieuwe functionaliteiten toe te voegen. Ik denk dat het beter is om helemaal opnieuw te beginnen met een object-georiënteerde aanpak, zodat ik de code beter kan organiseren en uitbreiden in de toekomst. Ik zal dit vragen aan mijn lector voordat ik een beslissing neem.

## 15 Mei 2026 14:30

Ik heb nog geenfeedbackontvangen van mijn docent en besloten verder te gaan met de bestaande code. De code van de tutorial was nogal chaotisch en onoverzichtelijk. Ik heb een paar externe bestanden toegevoegd om de code overzichtelijker te maken. Verder heb ik ook een paar methodes opgekuist. Met de hulp van pygame mixer heb ik ook geluidseffecten toegevoegd aan mijn game. Ik ben tevreden met de vooruitgang die ik heb geboekt.

## 16 Mei 2026 07:45
De gebruikersinterface was niet mooiafgewerkt. Ik heb depositie van deknoppen aangepast. Nu overlappen ze elkaar niet meer en ziet het er een stuk beter uit. Ik heb ook de kleuren van de knoppen aangepast om ze meer in lijn te brengen met het thema van mijn game. Daarnaast heb ik ook een achtergrondafbeelding toegevoegd om de visuele aantrekkingskracht van mijn game te vergroten.

## 16 Mei 2026 08:43
Ok nu begint het leuk te worden. Ik heb twee classen toegevoegd, Deck en Card. Nu heb ik een deck met twee private methodes, shuffle en geef een kaart. Ikzal de kaarten volledig apart houden van de gamelogica.

## 17 Mei 2026 09:04
De belangrijkste wijziging is, een card class heeft nu ook een symbol property. De volgende stap is, een kaart tekenen met symbol. Ik moet nog beslissien of ik dit inCard class wil doen of in een aparte class. Ik denk dat het beter is om dit in een aparte class te doen, zodat ik de kaartlogica gescheiden kan houden van de weergave logica. Ik zal een CardRenderer class maken die verantwoordelijk is voor het tekenen van de kaarten op het scherm. Deze class zal gebruik maken van de symbol property van de Card class om de juiste afbeelding te selecteren voor elke kaart.

## 17 Mei 2026 10:34
Nu worden de kaartjes netjes getekend op het scherm. Ik heb een paar kleine bugs opgelost die ervoor zorgden dat de kaarten niet correct werden weergegeven. Als we eenvierkant willen tekenen en er ontbreken bepaalde parameters, moeten we expliciet meegeven welke parameter het is (bv. mijn_methode(100, 200, width=200)).

## 17 Mei 2026 11:32
De buttons worden nu ook netjes weergegeven in het spelletje maar ik wil eigenlijk de positie van de buttons zelf berekenen in plaats van harcoded waardes te gebruiken. Ik ga een methode schrijven die de positie van de buttons berekent op basis van het aantal buttons en de grootte van het scherm. Op deze manier kan ik gemakkelijk nieuwe buttons toevoegen zonder dat ik me zorgen hoef te maken over de positionering ervan.

## 17 Mei 2026 20:29
De code van tutorials is grotendeels opgekuist. Er zijn nog altijd een paar zaken die ikstorendvind,zoals result ende buttons ineenarray stekenmaar het resultaat istoch stuk beter. Ik denk dat ik klaar benvoor de evaluatie. Er zijn nog eenpaarzaken dieik zil toevoegen maar weet niet goed ofhetkan. Dus na deze als er geenandere commits zijn op mijn logboek, is het niet gelukt.

# 18 Mei 2026 22:53
Ik ben vandaag de hele dag bezig geweest met AI implementatie. Er zijn dus twee libraries waarvan ik gebruik heb gemaakt, gtts en anthropic. Voorlopig werktalles. Ik stuur een prompt naar Claude met scores en de kaarten en krijg een response terug. Response wordt dan uitgelezen doorgttis text to speech engine. Ik vond weleen leuke feature maar we zullen zien of mijn docent dit ook leuk vindt, waarschijnlijk niet maar ik doe het toch.
