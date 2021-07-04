import pygame
import sys
import clarify
from time import sleep
from pygame.locals import *




def floorpic(s, time_start):
    pygame.init()
    pygame.mixer.init()


    do = 'mp3/do.mp3'
    re = 'mp3/re.mp3'
    mi = 'mp3/mi.mp3'
    fa = 'mp3/fa.mp3'
    so = 'mp3/so.mp3'
    la = 'mp3/la.mp3'
    si = 'mp3/si.mp3'
    
    screen = s
    
    screenWidth=1200
    screenHeight=900
    '''
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    #pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    '''

    black = 'ps/black.png'
    black = pygame.image.load(black)
    black = pygame.transform.scale(black, (screenWidth, screenHeight))
    
    floor8_clear=False
    floor9_clear=False
    floor10_clear=False
    M_clear = False
    floor=8
    clear_num = 0
    button_width = 18
    button_height = 18

    anscode8 = '3   2   7   4   '
    anscode9 = '3   6   0   8   '
    anscode10 = '1   6   5   8   '
    anscodeM = '443121'

    code8 = str()
    code9 = str()
    code10 = str()
    codeM = str()

    ############
    def get_number(key):
        if key == K_0:
            return '0'
        elif key == K_1:
            return '1'
        elif key == K_2:
            return '2'
        elif key == K_3:
            return '3'
        elif key == K_4:
            return '4'
        elif key == K_5:
            return '5'
        elif key == K_6:
            return '6'
        elif key == K_7:
            return '7'
        elif key == K_8:
            return '8'
        elif key == K_9:
            return '9'

    def get_present_code(floor):
        if floor == 8:
            return code8
        elif floor == 9:
            return code9
        elif floor == 10:
            return code10 
    def floor_clear(floor):
        if floor == 8:
            floor8_clear = True
        elif floor == 9:
            floor9_clear = True
        elif floor == 10:
            floor10_clear = True 

    def get_ans_code(floor):
        if floor == 8:
            return anscode8
        elif floor == 9:
            return anscode9
        elif floor == 10:
            return anscode10
    def draw(floor, floor8_clear, floor9_clear, floor10_clear, M_clear):
        pic = get_pic(floor, floor8_clear, floor9_clear, floor10_clear, M_clear)
        pic = pygame.image.load(pic)
        pic = pygame.transform.scale(pic, (screenWidth, screenHeight))
        drawScreen(pic)
        pygame.display.update()
    def drawScreen(pic):
        screen.blit(pic, (0,0))
        pygame.display.update()
    
    def get_pic(floor, floor8_clear, floor9_clear, floor10_clear, M_clear):
        if M_clear == True:
            if floor8_clear==False and floor9_clear==False and floor10_clear==False:
                floor8_pic = 'ps/M8F.png'
                floor9_pic = 'ps/M9F.png'
                floor10_pic = 'ps/M10F.png'
            elif floor8_clear==False and floor9_clear==False and floor10_clear==True:
                floor8_pic = 'ps/M8F_10.png'
                floor9_pic = 'ps/M9F_10.png'
                floor10_pic = 'ps/M10F_10.png'
            elif floor8_clear==False and floor9_clear==True and floor10_clear==False:
                floor8_pic = 'ps/M8F_9.png'
                floor9_pic = 'ps/M9F_9.png'
                floor10_pic = 'ps/M10F_9.png'
            elif floor8_clear==True and floor9_clear==False and floor10_clear==False:
                floor8_pic = 'ps/M8F_8.png'
                floor9_pic = 'ps/M9F_8.png'
                floor10_pic = 'ps/M10F_8.png'
            elif floor8_clear==True and floor9_clear==True and floor10_clear==False:
                floor8_pic = 'ps/M8F_89.png'
                floor9_pic = 'ps/M9F_89.png'
                floor10_pic = 'ps/M10F_89.png'
            elif floor8_clear==True and floor9_clear==False and floor10_clear==True:
                floor8_pic = 'ps/M8F_810.png'
                floor9_pic = 'ps/M9F_810.png'
                floor10_pic = 'ps/M10F_810.png'
            elif floor8_clear==False and floor9_clear==True and floor10_clear==True:
                floor8_pic = 'ps/M8F_910.png'
                floor9_pic = 'ps/M9F_910.png'
                floor10_pic = 'ps/M10F_910.png'
            elif floor8_clear==True and floor9_clear==True and floor10_clear==True:
                floor8_pic = 'ps/M8F_8910.png'
                floor9_pic = 'ps/M9F_8910.png'
                floor10_pic = 'ps/M10F_8910.png'
        elif M_clear == False:
            if floor8_clear==False and floor9_clear==False and floor10_clear==False:
                floor8_pic = 'ps/8F.png'
                floor9_pic = 'ps/9F.png'
                floor10_pic = 'ps/10F.png'
            elif floor8_clear==False and floor9_clear==False and floor10_clear==True:
                floor8_pic = 'ps/8F_10.png'
                floor9_pic = 'ps/9F_10.png'
                floor10_pic = 'ps/10F_10.png'
            elif floor8_clear==False and floor9_clear==True and floor10_clear==False:
                floor8_pic = 'ps/8F_9.png'
                floor9_pic = 'ps/9F_9.png'
                floor10_pic = 'ps/10F_9.png'
            elif floor8_clear==True and floor9_clear==False and floor10_clear==False:
                floor8_pic = 'ps/8F_8.png'
                floor9_pic = 'ps/9F_8.png'
                floor10_pic = 'ps/10F_8.png'
            elif floor8_clear==True and floor9_clear==True and floor10_clear==False:
                floor8_pic = 'ps/8F_89.png'
                floor9_pic = 'ps/9F_89.png'
                floor10_pic = 'ps/10F_89.png'
            elif floor8_clear==True and floor9_clear==False and floor10_clear==True:
                floor8_pic = 'ps/8F_810.png'
                floor9_pic = 'ps/9F_810.png'
                floor10_pic = 'ps/10F_810.png'
            elif floor8_clear==False and floor9_clear==True and floor10_clear==True:
                floor8_pic = 'ps/8F_910.png'
                floor9_pic = 'ps/9F_910.png'
                floor10_pic = 'ps/10F_910.png'
            elif floor8_clear==True and floor9_clear==True and floor10_clear==True:
                floor8_pic = 'ps/8F_8910.png'
                floor9_pic = 'ps/9F_8910.png'
                floor10_pic = 'ps/10F_8910.png'
    
        if floor == 8:
            return floor8_pic
        elif floor == 9:
            return floor9_pic
        elif floor == 10:
            return floor10_pic
        
    #########    
    draw(floor, floor8_clear, floor9_clear, floor10_clear, M_clear)
    
    while clear_num < 3 or M_clear == False:

        ######timer
        '''remain_time = 90*60 - ( int((pygame.time.get_ticks() - time_start)/1000) )
        min_counter = remain_time//60
        sec_counter = remain_time % 60'''
        ######
                    
        '''pic = get_pic(floor, floor8_clear, floor9_clear, floor10_clear)
        pic = pygame.image.load(pic)
        pic = pygame.transform.scale(pic, (screenWidth, screenHeight))
        drawScreen(pic)'''
        
        #print('run2')
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 913 < pygame.mouse.get_pos()[0] < 938 and 556 < pygame.mouse.get_pos()[1] < 581:  #8
                    floor = 8
                    code8 = ''
                    code9 = ''
                    code10 = ''
                    #print('8')
                    screen.blit(black, (0,0))
                    pygame.display.update()
                    sleep(0.5)
                    draw(floor, floor8_clear, floor9_clear, floor10_clear, M_clear)
                elif 870 < pygame.mouse.get_pos()[0] < 895 and 521 < pygame.mouse.get_pos()[1] < 546:  #9
                    floor = 9
                    code8 = ''
                    code9 = ''
                    code10 = ''
                    #print('9')
                    screen.blit(black, (0,0))
                    pygame.display.update()
                    sleep(0.5)
                    draw(floor, floor8_clear, floor9_clear, floor10_clear, M_clear)
                elif 913 < pygame.mouse.get_pos()[0] < 938 and 520 < pygame.mouse.get_pos()[1] < 545:  #10
                    floor = 10
                    code8 = ''
                    code9 = ''
                    code10 = ''
                    #print('10')
                    screen.blit(black, (0,0))
                    pygame.display.update()
                    sleep(0.5)
                    draw(floor, floor8_clear, floor9_clear, floor10_clear, M_clear)

                elif 870 < pygame.mouse.get_pos()[0] < 895 and 676 < pygame.mouse.get_pos()[1] < 701:  #1
                    codeM += '1'
                    pygame.mixer.music.load(do)
                    pygame.mixer.music.play()
                    pygame.event.wait()
                elif 913 < pygame.mouse.get_pos()[0] < 938 and 676 < pygame.mouse.get_pos()[1] < 701:  #2
                    codeM += '2'
                    pygame.mixer.music.load(re)
                    pygame.mixer.music.play()
                    pygame.event.wait()
                elif 870 < pygame.mouse.get_pos()[0] < 895 and 637 < pygame.mouse.get_pos()[1] < 662:  #3
                    codeM += '3'
                    pygame.mixer.music.load(mi)
                    pygame.mixer.music.play()
                    pygame.event.wait()
                elif 913 < pygame.mouse.get_pos()[0] < 938 and 637 < pygame.mouse.get_pos()[1] < 662:  #4
                    codeM += '4'
                    pygame.mixer.music.load(fa)
                    pygame.mixer.music.play()
                    pygame.event.wait()
                elif 870 < pygame.mouse.get_pos()[0] < 895 and 598 < pygame.mouse.get_pos()[1] < 623:  #5
                    codeM += '5'
                    pygame.mixer.music.load(so)
                    pygame.mixer.music.play()
                    pygame.event.wait()
                elif 913 < pygame.mouse.get_pos()[0] < 938 and 598 < pygame.mouse.get_pos()[1] < 623:  #6
                    codeM += '6'
                    pygame.mixer.music.load(la)
                    pygame.mixer.music.play()
                    pygame.event.wait()
                elif 870 < pygame.mouse.get_pos()[0] < 895 and 556 < pygame.mouse.get_pos()[1] < 581:  #7
                    codeM += '7'
                    pygame.mixer.music.load(si)
                    pygame.mixer.music.play()
                    pygame.event.wait()
                    
            elif event.type == pygame.KEYDOWN:
                if event.key == K_e:
                    pygame.quit()
                else:
                    if floor == 8 and floor8_clear == False:
                        try:
                            code8 += get_number(event.key)
                            code8 += '   '
                        except:
                            pass
                    elif floor == 9 and floor9_clear == False:
                        try:
                            code9 += get_number(event.key)
                            code9 += '   '
                        except:
                            pass
                    elif floor == 10 and floor10_clear == False:
                        try:
                            code10 += get_number(event.key)
                            code10 += '   '
                        except:
                            pass
                    print(get_present_code(floor))
                    
            if len(get_present_code(floor)) == 16 :
                if get_present_code(floor) == get_ans_code(floor) :
                 #floor_clear(floor)
                    if floor==8:
                        floor8_clear = True
                        clear_num += 1
                    elif floor==9:
                        floor9_clear = True
                        clear_num += 1
                    elif floor==10:
                        floor10_clear = True
                        clear_num += 1
                code8 = ''
                code9 = ''
                code10 = ''
                draw(floor, floor8_clear, floor9_clear, floor10_clear, M_clear)
            if anscodeM in codeM :
                M_clear = True
                draw(floor, floor8_clear, floor9_clear, floor10_clear, M_clear)
                    
                
        text_font = pygame.font.SysFont(None, 60)
        text = text_font.render(get_present_code(floor), True, (255, 255, 255))
        screen.blit(text, (400, 570))

        pygame.display.update()
    
    cla = clarify.Clarify_scene(screen)
    cla.run()



if __name__=='__main__':
    floorpic(s)

