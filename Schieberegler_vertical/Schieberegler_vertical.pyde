'''
' Schieberegler
' Simon Hefti, Okt. 2020 verändert von Maria Mannai November 2022
'''

# Globale Variablen:
# movingMode (Boolean): True, wenn der Schieber (Kreis) in Bewegung ist, False wenn nicht
# pointerPos (Integer): Position des Pointers in Pixeln
# pointerVal (Float):   Eingestellter Wert (0 - 100)
movingMode = False
pointerPos = 0
pointerVal = 1.0

# Initialisierung
def setup():
    size(900, 500)
    textSize(64)
    textAlign(CENTER)
    
    
# Sich wiederholende draw() Funktion
def draw():
    background(255)
    ruler1 = draw_ruler(200, 400, 200)

    text(str(pointerVal) + "%", width/2, height/2)

    
# Funktion: Schieberegler generieren
# objX:      X-Position des Reglers
# objY:      Y-Position des Reglers
# objLength: Länge des Reglers
def draw_ruler(objX, objY, objLength):
    global movingMode
    global pointerPos
    global pointerVal
    
    # Schieber einstellen
    pointerRadius = 24
    if pointerPos == 0:
        pointerPos = objY
    
    # Linie zeichnen
    fill(85)
    strokeWeight(6)
    line(objX, objY, objX , objY- objLength)
    fill(185)
    strokeWeight(2)
    
    # Überprüfen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if mouseY > pointerPos - pointerRadius and mouseY < pointerPos + pointerRadius and mouseX > objX - pointerRadius and mouseX < objX + pointerRadius and mousePressed == True:
        movingMode = True
    
    # Wenn keine Maustaste gedrückt ist --> Bewegungsmodus deaktivieren
    if mousePressed == False:
        movingMode = False
        cursor(ARROW)
    
    # Bei aktiviertem Bewegungsmodus
    if movingMode == True:
        cursor(HAND)
        
        # Schieber der Line entlang bewegen
        if mouseY < objY and mouseY > objY - objLength:
            pointerPos = mouseY
        
        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if mouseY < objY:
                pointerPos = objY - objLength
            if mouseY > objY:
                pointerPos = objY

    # Schieber zeichnen            
    circle(objX, pointerPos, pointerRadius)
    
    # Eingestellter Wert anhand der Schieberposition ermitteln
    pointerVal = int(100 / float(objLength) * (objY - pointerPos))
            
