import pygame

################### class piece ###################
class piece(object):
    def __init__(self, name: str, location: tuple):
        #add name
        self.name = name

        #add image
        switcher = {"KB":0, "DB":1, "TB":2, "LB":3, "PB":4, "piB":6, "KW":7, "DW":8, "TW":9, "LW":10, "PW":11, "piW":12}
        images = ['bking.png', 'bqueen.png', 'brook.png', 'bbishop.png', 'bknight.png', 'bpawn.png', 'bpawn.png', 'wking.png', 'wqueen.png', 'wrook.png', 'wbishop.png', 'wknight.png', 'wpawn.png', 'error.png']
        imagenume = switcher.get(name, 13)
        self.image = pygame.image.load('./images/' + images[imagenume])

        #add locatie
        self.locatie = location
        self.locatiebord = (int(round(location[0]/75, 0)), int(round(location[1]/75, 0)))

        #hit box
        self.hitbox = (location[0], location[1], location[0] + 50, location[1] + 50)

        #add aantal bewegingen
        self.moves = 0

        #add tippe en tiem
        switcher = {"KB":"K", "DB":"D", "TB":"T", "LB":"L", "PB":"P", "piB":"pi", "KW":"K", "DW":"D", "TW":"T", "LW":"L", "PW":"P", "piW":"pi"}
        self.type = switcher.get(name, "error")
        switcher = {"KB":"B", "DB":"B", "TB":"B", "LB":"B", "PB":"B", "piB":"B", "KW":"W", "DW":"W", "TW":"W", "LW":"W", "PW":"W", "piW":"W"}
        self.team = switcher.get(name, "error")


    def draw(self, win: pygame.Surface, dibugmod: bool):
        #draw image
        win.blit(self.image, self.locatie)
        if dibugmod:
            #draw hit boxen
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1], 50, 50) , 2)
    
    def IsInHitbox(self, location: tuple, dibugmod: bool):
        #chek of locatie in het box is
        if self.hitbox[0] < location[0] and self.hitbox[1] < location[1] and self.hitbox[2] > location[0] and self.hitbox[3] > location[1]:
            # print dibug info als dibugmod aan staat
            if dibugmod:
                print("hit:", self.name, "type:", self.type, "team:", self.team)
            return True
        else:
            return False

    #move pies naar locatie
    def Move(self, location: tuple):
        #verander locatie
        self.locatie = (location[0], location[1])
        #verander locatie op het bord
        self.locatiebord = (int(round(location[0]/75, 0)), int(round(location[1]/75, 0)))
        #verander locaite hitbox
        self.hitbox = (location[0], location[1], location[0] + 50, location[1] + 50)
        #moves +1
        self.moves += 1

    def MogelijkeZetten(self, bord, debugmod):
        Zetten = []
        chek = False
        #zetten voor pion zwart
        if self.name == "piB":
            #chek voor (x, y+1), (x, y+2)
            locatie = (self.locatiebord[0],self.locatiebord[1]+1)
            if locatie[0] <= 7 and locatie[0] >= 0 and locatie[1] <= 7 and locatie[1] >= 0:
                PosObject = bord.Getpiece(locatie)
                if PosObject == None:
                    Zetten.append(locatie)
                    if self.locatiebord[1] == 1:
                        locatie = (self.locatiebord[0],self.locatiebord[1]+2)
                        PosObject = bord.Getpiece(locatie)
                        if PosObject == None:
                            Zetten.append(locatie)
            #chek voor (x+1, y+1)
            locatie = (self.locatiebord[0]+1, self.locatiebord[1]+1)
            if locatie[0] <= 7 and locatie[0] >= 0 and locatie[1] <= 7 and locatie[1] >= 0:
                PosObject = bord.Getpiece(locatie)
                if PosObject != None and PosObject.team != "B":
                    if PosObject.type != "K":
                        Zetten.append(locatie)
                    else:
                        chek = True
            #chek voor (x-1, y+1)
            locatie = (self.locatiebord[0]-1, self.locatiebord[1]+1)
            if locatie[0] <= 7 and locatie[0] >= 0 and locatie[1] <= 7 and locatie[1] >= 0:
                PosObject = bord.Getpiece(locatie)
                if PosObject != None and PosObject.team != "B":
                    if PosObject.type != "K":
                        Zetten.append(locatie)
                    else:
                        chek = True
            #chek voor (x-1, y-1)
            locatie = (self.locatiebord[0]-1, self.locatiebord[1]-1)
            if locatie[0] <= 7 and locatie[0] >= 0 and locatie[1] <= 7 and locatie[1] >= 0:
                PosObject = bord.Getpiece(locatie)
                if PosObject != None:
                    if PosObject.type == "pi" and PosObject.team == "W" and PosObject.moves == 1:
                        Zetten.append(locatie)
            #chek voor (x+1, y-1)
            locatie = (self.locatiebord[0]+1, self.locatiebord[1]-1)
            if locatie[0] <= 7 and locatie[0] >= 0 and locatie[1] <= 7 and locatie[1] >= 0:
                PosObject = bord.Getpiece(locatie)
                if PosObject != None:
                    if PosObject.type == "pi" and PosObject.team == "W" and PosObject.moves == 1:
                        Zetten.append(locatie)
                

        #zetten voor pion wit
        elif self.name == "piW":
            #chek voor (x, y-1), (x, y-2)
            locatie = (self.locatiebord[0],self.locatiebord[1]-1)
            if locatie[0] <= 7 and locatie[0] >= 0 and locatie[1] <= 7 and locatie[1] >= 0:
                PosObject = bord.Getpiece(locatie)
                if PosObject == None:
                    Zetten.append((self.locatiebord[0], self.locatiebord[1]-1))
                    if self.locatiebord[1] == 6:
                        PosObject = bord.Getpiece((self.locatiebord[0],self.locatiebord[1]-2))
                        if PosObject == None:
                            Zetten.append((self.locatiebord[0], self.locatiebord[1]-2))
            #chek voor (x+1, y-1)
            locatie = (self.locatiebord[0]+1, self.locatiebord[1]-1)
            if locatie[0] <= 7 and locatie[0] >= 0 and locatie[1] <= 7 and locatie[1] >= 0:
                PosObject = bord.Getpiece(locatie)
                if PosObject != None and PosObject.team != "W":
                    if PosObject.type != "K":
                        Zetten.append(locatie)
                    else:
                        chek = True
            #chek voor (x-1, y-1)
            locatie = (self.locatiebord[0]-1, self.locatiebord[1]-1)
            if locatie[0] <= 7 and locatie[0] >= 0 and locatie[1] <= 7 and locatie[1] >= 0:
                PosObject = bord.Getpiece(locatie)
                if PosObject != None and PosObject.team != "W":
                    if PosObject.type != "K":
                        Zetten.append(locatie)
                    else:
                        chek = True
            #chek voor (x-1, y+1)
            locatie = (self.locatiebord[0]-1, self.locatiebord[1]+1)
            if locatie[0] <= 7 and locatie[0] >= 0 and locatie[1] <= 7 and locatie[1] >= 0:
                PosObject = bord.Getpiece(locatie)
                if PosObject != None:
                    if PosObject.type == "pi" and PosObject.team == "B" and PosObject.moves == 1:
                        Zetten.append(locatie)
            #chek voor (x+1, y+1)
            locatie = (self.locatiebord[0]+1, self.locatiebord[1]+1)
            if locatie[0] <= 7 and locatie[0] >= 0 and locatie[1] <= 7 and locatie[1] >= 0:
                PosObject = bord.Getpiece(locatie)
                if PosObject != None:
                    if PosObject.type == "pi" and PosObject.team == "B" and PosObject.moves == 1:
                        Zetten.append(locatie)
        
        #zetten voor King
        elif self.type == "K":
            #(x+1, y+0), (x+0, y+1), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1), (x-1, y), (x, y-1)
            moves = ((1, 0), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1), (-1, 0), (0, -1))
            for move in moves:
                locatie = (self.locatiebord[0]+move[0], self.locatiebord[1]+move[1])
                if locatie[0] <= 7 and locatie[0] >= 0 and locatie[1] <= 7 and locatie[1] >= 0:
                    PosObject = bord.Getpiece(locatie)
                    switcher = {"B": "W", "W": "B"}
                    if PosObject == None or PosObject.team == switcher.get(self.team, "error") and not PosObject.type == "K":
                        if locatie[0] <= 7 and locatie[0] >= 0 and locatie[1] <= 7 and locatie[1] >= 0:
                                Zetten.append(locatie)

        #zetten voor queen
        elif self.type == "D":
            moves = ((1, 0), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1), (-1, 0), (0, -1))
            for move in moves:
                for n in range(1, 8):
                    locatie = (self.locatiebord[0] + move[0]*n, self.locatiebord[1] + move[1]*n)
                    if locatie[0] <= 7 and locatie[0] >= 0 and locatie[1] <= 7 and locatie[1] >= 0:
                        PosObject = bord.Getpiece(locatie)
                        switcher = {"B": "W", "W": "B"}
                        if PosObject == None:
                            Zetten.append(locatie)
                        elif PosObject != None and PosObject.team == switcher.get(self.team, "error"):
                            if PosObject.type == "K":
                                chek = True
                                break
                            else:
                                Zetten.append(locatie)
                                break
                        elif PosObject.team == self.team:
                            break
        
        #zetten voor tooren
        elif self.type == "T":
            moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
            for move in moves:
                for n in range(1, 8):
                    locatie = (self.locatiebord[0] + move[0]*n, self.locatiebord[1] + move[1]*n)
                    if locatie[0] <= 7 and locatie[0] >= 0 and locatie[1] <= 7 and locatie[1] >= 0:
                        PosObject = bord.Getpiece(locatie)
                        switcher = {"B": "W", "W": "B"}
                        if PosObject == None:
                            Zetten.append(locatie)
                        elif PosObject != None and PosObject.team == switcher.get(self.team, "error"):
                            if PosObject.type == "K":
                                chek = True
                                break
                            else:
                                Zetten.append(locatie)
                                break
                        elif PosObject.team == self.team:
                            break
        
        #zetten voor loper
        elif self.type == "L":
            moves = ((1, 1), (-1, -1), (1, -1), (-1, 1))
            for move in moves:
                for n in range(1, 8):
                    locatie = (self.locatiebord[0] + move[0]*n, self.locatiebord[1] + move[1]*n)
                    if locatie[0] <= 7 and locatie[0] >= 0 and locatie[1] <= 7 and locatie[1] >= 0:
                        PosObject = bord.Getpiece(locatie)
                        switcher = {"B": "W", "W": "B"}
                        if PosObject == None:
                            Zetten.append(locatie)
                        elif PosObject != None and PosObject.team == switcher.get(self.team, "error"):
                            if PosObject.type == "K":
                                chek = True
                                break
                            else:
                                Zetten.append(locatie)
                                break
                        elif PosObject.team == self.team:
                            break

        #zetten paard
        elif self.type == "P":
            moves = ((-1,-2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2))
            for move in moves:
                locatie = (self.locatiebord[0] + move[0], self.locatiebord[1] + move[1])
                if locatie[0] <= 7 and locatie[0] >= 0 and locatie[1] <= 7 and locatie[1] >= 0:
                    PosObject = bord.Getpiece(locatie)
                    switcher = {"B": "W", "W": "B"}
                    if PosObject == None:
                        Zetten.append(locatie)
                    elif PosObject.team == switcher.get(self.team, "error"):
                        if PosObject.type != "K":
                            Zetten.append(locatie)
                        else:
                            chek = True
            
        if debugmod:
            print("zetten:", Zetten, "chek:", chek)
        return Zetten, chek

################### class zet ###################
class zet(object):
    def __init__(self, location: tuple, pieslock):
        #voe een locatie toe
        self.location = location
        #voeg hitbox toe
        x = (self.location[0])*75
        y = (self.location[1])*75
        self.hitbox = (x+5, y+5, x+70, y+70)
        #voeg bij horende pion locatie toe
        self.pieslock = pieslock

    def draw(self, win, debugmod):
        x = (self.location[0])*75
        y = (self.location[1])*75
        pygame.draw.circle(win, (0, 255, 0), (x+37, y+37), 5)
        if debugmod:
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1], 65, 65) , 2)

    def IsInHitbox(self, location: tuple, dibugmod: bool):
        #chek of locatie in het box is
        if self.hitbox[0] < location[0] and self.hitbox[1] < location[1] and self.hitbox[2] > location[0] and self.hitbox[3] > location[1]:
            # print dibug info als dibugmod aan staat
            if dibugmod:
                print("Hit:", self.location, "Pies:", self.pieslock)
            return True
        else:
            return False

################### class bord ###################
class bord(object):
    def __init__(self):
        self.bord = [
            [piece("TB", (12, 12)), piece("PB", (87, 12)), piece("LB", (162, 12)), piece("DB", (237, 12)), piece("KB", (312, 12)), piece("LB", (387, 12)), piece("PB", (462, 12)), piece("TB", (537, 12))],
            [piece("piB", (12, 87)), piece("piB", (87, 87)), piece("piB", (162, 87)), piece("piB", (237, 87)), piece("piB", (312, 87)), piece("piB", (387, 87)), piece("piB", (462, 87)), piece("piB", (537, 87))],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [piece("piW", (12, 462)), piece("piW", (87, 462)), piece("piW", (162, 462)), piece("piW", (237, 462)), piece("piW", (312, 462)), piece("piW", (387, 462)), piece("piW", (462, 462)), piece("piW", (537, 462))],
            [piece("TW", (12, 537)), piece("PW", (87, 537)), piece("LW", (162, 537)), piece("DW", (237, 537)), piece("KW", (312, 537)), piece("LW", (387, 537)), piece("PW", (462, 537)), piece("TW", (537, 537))],
            ]
        
        self.zetten = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ]
    
    def Getpiece(self, location: tuple):
        return self.bord[location[1]][location[0]]
    
    def GetZet(self, location: tuple):
        return self.zetten[location[1]][location[0]]
    
    def Draw(self, win: pygame.Surface, dibugmod: bool):
        for y in range(8):
            for x in range(8):
                stuk = self.bord[y][x]
                zet = self.zetten[y][x]
                if stuk != None:
                    stuk.draw(win, dibugmod)
                if zet != None:
                    zet.draw(win, dibugmod)
    
    def addzetten(self, locaties: list, pieslcok: tuple):
        for y in range(8):
            for x in range(8):
                for locatie in locaties:
                    if locatie[0] == x and locatie[1] == y:
                        self.zetten[y][x] = zet(locatie, pieslcok)
                        break
                    else:
                        self.zetten[y][x] = None
    
    def CleanZetten(self):
        self.zetten = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ]
    
    def MovePies(self, PiesLocation: tuple, TargetLocation: tuple):
        Pies = self.Getpiece(PiesLocation)
        x = (TargetLocation[0]*75)+15
        y = (TargetLocation[1]*75)+15
        Pies.Move((x, y))
        self.bord[PiesLocation[1]][PiesLocation[0]] = None
        self.bord[TargetLocation[1]][TargetLocation[0]] = Pies
    
    def ChekFoorChek(self, debugmod):
        for y in range(8):
            Fout = False
            for x in range(8):
                piece = self.Getpiece((x, y))
                if piece != None:
                    _, chek = piece.MogelijkeZetten(self, False)
                    if chek:
                        Fout = True
                        break
            if Fout:
                break
        
        return chek, piece.team, piece.locatiebord, piece.type

