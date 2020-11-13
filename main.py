import pygame, os
import objects

pygame.init()

win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("chess")

bord = objects.bord()

run = True
dibugmod = False

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        #sluiten van het programa
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            find = False
            for y in range(8):
                for x in range(8):
                    stuk = bord.Getpiece((x, y))
                    zet = bord.GetZet((x, y))
                    if zet != None:
                        Hit = zet.IsInHitbox(pos, dibugmod)
                        if Hit:
                            find = True
                            bord.MovePies(zet.pieslock, zet.location)
                            bord.CleanZetten()
                            break
                    elif stuk != None:
                        Hit = stuk.IsInHitbox(pos, dibugmod)
                        if Hit:
                            find = True
                            Zetten, _ = stuk.MogelijkeZetten(bord, dibugmod)
                            bord.addzetten(Zetten, stuk.locatiebord)
                            break
                if find:
                    break

        if event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_d:
                if dibugmod:
                    dibugmod = False
                else:
                    dibugmod = True
            if event.key == pygame.K_q:
                run = False
            if event.key == pygame.K_ESCAPE:
                bord.CleanZetten()

    #draw board
    win.fill((50,50,50))
    for y in range(8):
        for x in range(4):
            if (y % 2) == 0:
                addwaarde = 75
            else:
                addwaarde = 0
            pygame.draw.rect(win, (255, 255, 255), (x * 150 + addwaarde, y * 75, 75, 75))
    
    #draw objects
    bord.Draw(win, dibugmod)

    #chek voor chek
    chek, team, location, typ = bord.ChekFoorChek(dibugmod)
    if chek:
        print(team, location, typ)

    pygame.display.update()