import pygame
import sys
import mainai
import tkinter as tk
import zoomschedule
import os
speaking = False
mbd = False
display=False
html = ''
pygame.init()

win = pygame.display.set_mode((900, 500))
pygame.display.set_caption('thinkcode')
logo=pygame.image.load('storage files\\thinkodelogo.png')
pygame.display.set_icon(logo)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mbd = True
        if event.type == pygame.MOUSEBUTTONUP:
            mbd = False
    mouseposx, mouseposy = pygame.mouse.get_pos()
    zoomschedule.schedulezoom()
    displayrect=pygame.Rect(50,50,300,300)
    buttonpresser = pygame.Rect(mouseposx, mouseposy, 10, 10)
    pygame.draw.rect(win, (0, 0, 255), buttonpresser)
    note1bar1 = pygame.image.load('storage files/noteeditholder.png')
    note1bar = pygame.transform.scale(note1bar1, (250, 20))
    win.fill((16, 16, 16))
    speakbutton = pygame.Rect(300, 450, 50, 50)
    schedulebutton=pygame.Rect(660,450, 159, 50)
    pygame.draw.rect(win, (0,122,204), schedulebutton)
    button1=pygame.image.load('storage files\\schedule.png')
    pygame.draw.rect(win, (16, 16, 16), speakbutton)
    noteframemain = pygame.Rect(650, 0, 250, 500)
    pygame.draw.rect(win, (0, 122, 204), noteframemain)
    miciconimage = pygame.image.load('storage files/micicon.png')
    micicon = pygame.transform.scale(miciconimage, (50, 50))
    win.blit(button1,(660,450))
    win.blit(micicon, (300, 450))
    win.blit(note1bar, (650, 65))
    pygame.font.init()
    html2=html
    html3=html2.replace('#','')
    html4=html3.replace('\n','')
    myfont = pygame.font.SysFont('Verdana', 30)
    htmldisplayer = myfont.render(f'{html4}', False, (255, 255, 255))
    win.blit(htmldisplayer, (200, 100))
    if display:
        pygame.quit()
        window=tk.Tk()
        l1=tk.Label(window,text='hour(24 hr format):').grid(row=1,column=1)
        e1=tk.Entry(window)
        e1.grid(row=2,column=1)
        l3 = tk.Label(window, text='minute:').grid(row=1,column=2)
        e2 = tk.Entry(window)
        e2.grid(row=2,column=2)
        l4=tk.Label(window, text='meeting link:').grid(row=1,column=3)
        e3= tk.Entry(window)
        e3.grid(row=2,column=3)
        def btp():
            with open('storage files\\hour.txt', 'w') as f:
                f.write(f'{e1.get()}')
            with open('storage files\\minute.txt', 'w') as f:
                f.write(f'{e2.get()}')
            with open('storage files\\link.txt', 'w') as f:
                f.write(f'{e3.get()}')
            mainai.speak('please run the program again to auto join your meetings')
            sys.exit()
        b1=tk.Button(window, text='done', command=btp).grid()


        window.mainloop()

    if buttonpresser.colliderect(schedulebutton):
        click= pygame.mouse.get_pressed(3)[0]
        if click:
            pygame.time.delay(100)
            display=True
    if buttonpresser.colliderect(speakbutton):
        click = pygame.mouse.get_pressed(3)[0]
        myfont = pygame.font.SysFont('Verdana', 20)
        status = myfont.render('', False, (255, 255, 255))
        win.blit(status, (270, 410))
        myfont = pygame.font.SysFont('Verdana', 20)
        status = myfont.render('listening', True, (255, 0, 0))
        if click:
            pygame.time.delay(100)
            win.blit(status, (270, 410))
            mainai.querytaker()
    else:
        myfont = pygame.font.SysFont('Verdana', 20)
        status = myfont.render('', False, (255, 255, 255))
        win.blit(status, (270, 410))
    pygame.font.init()
    myfont = pygame.font.SysFont('Verdana', 30)
    notestitle = myfont.render('Notes', False, (0, 0, 0))
    win.blit(notestitle, (660, 10))
    with open('storage files\\newnote.txt', 'r')as file:
        try:
            with open(f'note files\\{file.read()}.note', 'r')as f:
                fileread1 = f.read()
                fileread2 = fileread1.splitlines()
                pygame.font.init()
                myfont = pygame.font.SysFont('Verdana', 20)
                note1 = myfont.render(f'{fileread2[1]}', False, (0, 0, 0))
                note2= myfont.render(f'{fileread2[2]}',False, (0,0,0))
                note3= myfont.render(f'{fileread2[3]}', False, (0,0,0))
                win.blit(note2, (660, 120))
                win.blit(note1, (660, 90))
        except:
            myfont = pygame.font.SysFont('Comic sans MS', 18)
            note1 = myfont.render('did not get any note files', False, (255, 255, 255))
            win.blit(note1, (652, 90))
    pygame.display.flip()
sys.exit()
