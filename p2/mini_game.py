from tkinter import *
import pygame

window = Tk()
window.geometry('600x400+200+100')
window.title("happy anteater")

W = 400
H = 300
WHITE = 0, 0, 0
x = W // 2
y = H // 2
r = 50
def pigame():
    sc = pygame.display.set_mode((W, H))
    sc.fill((205, 133, 63))
    keys = pygame.key.get_pressed()
    pygame.draw.circle(sc, WHITE, (x, y), r)
    pygame.display.update()
    if keys[pygame.K_LEFT]:
        pass
    elif keys[pygame.K_RIGHT]:
        pass


    pygame.display.update()





btn_1 = Button(text="Играть",  bg='DarkGoldenRod', activebackground='Goldenrod', command = pigame)
btn_1.place(x=260, y=160)




window.mainloop()