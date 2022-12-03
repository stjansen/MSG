Code Assessment MSG 

Je gaat een Patriot luchtverdedigingssysteem simuleren, welke bestaat uit 3 elementen:

- Radar 
- IFF 
- Missile launcher 

De simulatie gaat 20 seconden duren. Elke tijdstap (1s) geeft de radar module als output een regel uit het bijgevoegde csv formaat (zie volgende pagina). De IFF (Identification Friend or Foe) module checkt of er een vijandelijk object is gedetecteerd. Dit is het geval als er meer oneven dan even entries voorkomen in de decimale representatie van de radar-output. Zodra er een vijandelijk object is gedetecteerd zal een missile worden afgeschoten. Een missile heeft een PK (Probability of kill)-ratio van 0.8. Het effect van de missile wordt gesimuleerd door een random-number generator te bevragen en het getal te vergelijken met de PK-ratio. Indien de waarde die je krijgt groter is dan dit ratio dan is er geen hit, en vice-versa voor getallen lager dan de PK-ratio. 

Opdracht

Maak een applicatie die deze simulatie draait op basis van de radar-output.csv. Elke tijdstap moet uitgeprint worden wat de er die tijdstap is gebeurd in de simulatie. Is er een vijand gedetecteerd, missile afgevuurd, en is de dreiging geraakt? 
Werk de opdracht uit in Java en houd rekening met een nette opzet van code opdat de modellen en functionaliteiten later nog (door anderen) uitgebreid kan worden.
Inleveren van jouw uitwerkingen kan met een link naar een git-repository waar jij jouw code bijhoudt. 
Succes!
