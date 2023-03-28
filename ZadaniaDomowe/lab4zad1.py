import math
def panel(floorLen, floorWidth, panelLen, panelWidth, panelAmmount):
    floorSQ = floorLen*floorWidth
    panelSQ = panelLen*panelWidth

    panelNeeded = floorSQ/panelSQ
    totalPackAmmount = panelNeeded / panelAmmount

    finalPackAmmount = math.ceil(totalPackAmmount + totalPackAmmount*0.1)
    return finalPackAmmount;

print(panel(4,4,0.2,1,10))

