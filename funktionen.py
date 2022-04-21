import pygame
from farben import *
from random import randint
from pokemon import *

'''font = pygame.font.get_fonts()
'''
Level1 = True


shop_slot_1_rar = randint(1,10)
shop_slot_2_rar = randint(1,10)
shop_slot_3_rar = randint(1,10)
shop_slot_4_rar = randint(1,10)
shop_slot_5_rar = randint(1,10)

shop_slot_1_var_common = randint(1, 3)
shop_slot_2_var_common = randint(1, 3)
shop_slot_3_var_common = randint(1, 3)
shop_slot_4_var_common = randint(1, 3)
shop_slot_5_var_common = randint(1, 3)

shop_slot_1_var_uncommon = randint(1, 3)
shop_slot_2_var_uncommon = randint(1, 3)
shop_slot_3_var_uncommon = randint(1, 3)
shop_slot_4_var_uncommon = randint(1, 3)
shop_slot_5_var_uncommon = randint(1, 3)

shop_slot_1_var_rare = randint(1, 3)
shop_slot_2_var_rare = randint(1, 3)
shop_slot_3_var_rare = randint(1, 3)
shop_slot_4_var_rare = randint(1, 3)
shop_slot_5_var_rare = randint(1, 3)

shop_slot_1_var_epic = randint(1, 3)
shop_slot_2_var_epic = randint(1, 3)
shop_slot_3_var_epic = randint(1, 3)
shop_slot_4_var_epic = randint(1, 3)
shop_slot_5_var_epic = randint(1, 3)

gold = 100

fight = False

münzwurf = randint(1,2)

if münzwurf == 1:
  starting = "Ich"
if münzwurf == 2:
  starting = "Gegner"





#DEFINIEREN VON FUNKTIONEN

#Shop-Pokemon darstellen

def show_Pokemon1(pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_1_rar, shop_slot_1_var_common):
  if shop_slot_1_rar in range (zahl1, zahl2) and shop_slot_1_var_common == zahl:
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))

  return pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_1_rar, shop_slot_1_var_common

def show_Pokemon2(pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_2_rar, shop_slot_2_var_common):
  if shop_slot_2_rar in range (zahl1, zahl2):
    if shop_slot_2_var_common == zahl:
      screen.blit(pokemon1, (pokemon_x1, pokemon_y1))

  return pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_2_rar, shop_slot_2_var_common

def show_Pokemon3(pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_3_rar, shop_slot_3_var_common):
  if shop_slot_3_rar in range (zahl1, zahl2):
    if shop_slot_3_var_common == zahl:
      screen.blit(pokemon1, (pokemon_x1, pokemon_y1))

  return pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_3_rar, shop_slot_3_var_common

def show_Pokemon4(pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_4_rar, shop_slot_4_var_common):
  if shop_slot_4_rar in range (zahl1, zahl2):
    if shop_slot_4_var_common == zahl:
      screen.blit(pokemon1, (pokemon_x1, pokemon_y1))

  return pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_4_rar, shop_slot_4_var_common

def show_Pokemon5(pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_5_rar, shop_slot_5_var_common):
  if shop_slot_5_rar in range (zahl1, zahl2):
    if shop_slot_5_var_common == zahl:
      screen.blit(pokemon1, (pokemon_x1, pokemon_y1))

  return pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_5_rar, shop_slot_5_var_common
    


#Pokemon spawnen

#Shop-Slot 1

def spawn_Pokemon1_common(Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_1_var_common, shop_slot_1_rar, gold):
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 600 < my < 700 and Level1 == True and shop_slot_1_rar in range (variable1, variable2) and shop_slot_1_var_common == variable and Spawning1 == False and Spawning4 == False and gold >variable3:
    pokemon_x1 = 250
    pokemon_y1 = 645
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))
    Spawning1 = True
    shop_slot_1_var_common = 0
    shop_slot_1_rar = 0
    gold -= variable3

  if pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 600 < my < 700 and Level1 == True and shop_slot_1_rar in range (variable1, variable2) and shop_slot_1_var_common == variable and Spawning1 == True and Spawning2 == False and gold >variable3:
    pokemon_x2 = 250
    pokemon_y2 = 645
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))
    Spawning2 = True
    shop_slot_1_var_common = 0
    shop_slot_1_rar = 0
    gold -= variable3
    
  
  if pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 600 < my < 700 and Level1 == True and shop_slot_1_rar in range (variable1, variable2) and shop_slot_1_var_common == variable and Spawning1 == True and Spawning2 == True and Spawning3 == False and gold >variable3:
    pokemon_x3 = 250
    pokemon_y3 = 645
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))
    Spawning3 = True
    shop_slot_1_var_common = 0
    shop_slot_1_rar = 0
    gold -= variable3


  return Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_1_var_common, shop_slot_1_rar, gold

#Shop-Slot 2

def spawn_Pokemon2_common(Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_2_var_common, shop_slot_2_rar, gold):
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 500 < my < 600 and Level1 == True and shop_slot_2_rar in range (variable1, variable2) and shop_slot_2_var_common == variable and Spawning1 == False and Spawning4 == False and gold >variable3:
    pokemon_x1 = 250
    pokemon_y1 = 645
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))
    Spawning1 = True
    shop_slot_2_var_common = 0
    shop_slot_2_rar = 0
    gold -= variable3

  if pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 500 < my < 600 and Level1 == True and shop_slot_2_rar in range (variable1, variable2) and shop_slot_2_var_common == variable and Spawning1 == True and Spawning2 == False and gold >variable3:
    pokemon_x2 = 250
    pokemon_y2 = 645
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))
    Spawning2 = True
    shop_slot_2_var_common = 0  
    shop_slot_2_rar = 0
    gold -= variable3

  if pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 500 < my < 600 and Level1 == True and shop_slot_2_rar in range (variable1, variable2) and shop_slot_2_var_common == variable and Spawning1 == True and Spawning2 == True and Spawning3 == False and gold >variable3:
    pokemon_x3 = 250
    pokemon_y3 = 645
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))
    Spawning3 = True
    shop_slot_2_var_common = 0  
    shop_slot_2_rar = 0
    gold -= variable3

  if Spawning1:
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))

  if Spawning2:
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))

  if Spawning3:
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))

  return Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_2_var_common, shop_slot_2_rar, gold

#Shop-Slot 3  

def spawn_Pokemon3_common(Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_3_var_common, shop_slot_3_rar, gold):
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 400 < my < 500 and Level1 == True and shop_slot_3_rar in range (variable1, variable2) and shop_slot_3_var_common == variable and Spawning1 == False and Spawning4 == False and gold >variable3:
    pokemon_x1 = 250
    pokemon_y1 = 645
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))
    Spawning1 = True
    shop_slot_3_var_common = 0  
    shop_slot_3_rar = 0
    gold -= variable3

  if pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 400 < my < 500 and Level1 == True and shop_slot_3_rar in range (variable1, variable2) and shop_slot_3_var_common == variable and Spawning1 == True and Spawning2 == False and gold >variable3:
    pokemon_x2 = 250
    pokemon_y2 = 645
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))
    Spawning2 = True
    shop_slot_3_var_common = 0
    shop_slot_3_rar = 0
    gold -= variable3

  if pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 400 < my < 500 and Level1 == True and shop_slot_3_rar in range (variable1, variable2) and shop_slot_3_var_common == variable and Spawning1 == True and Spawning2 == True and Spawning3 == False and gold >variable3:
    pokemon_x3 = 250
    pokemon_y3 = 645
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))
    Spawning3 = True
    shop_slot_3_var_common = 0  
    shop_slot_3_rar = 0
    gold -= variable3

  if Spawning1:
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))

  if Spawning2:
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))

  if Spawning3:
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))

  return Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_3_var_common, shop_slot_3_rar, gold

#Shop-Slot 4

def spawn_Pokemon4_common(Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_4_var_common, shop_slot_4_rar, gold):
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 300 < my < 400 and Level1 == True and shop_slot_4_rar in range (variable1, variable2) and shop_slot_4_var_common == variable and Spawning1 == False and Spawning4 == False and gold >variable3:
    pokemon_x1 = 250
    pokemon_y1 = 645
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))
    Spawning1 = True
    shop_slot_4_var_common = 0  
    shop_slot_4_rar = 0
    gold -= variable3

  if pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 300 < my < 400 and Level1 == True and shop_slot_4_rar in range (variable1, variable2) and shop_slot_4_var_common == variable and Spawning1 == True and Spawning2 == False and gold >variable3:
    pokemon_x2 = 250
    pokemon_y2 = 645
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))
    Spawning2 = True
    shop_slot_4_var_common = 0  
    shop_slot_4_rar = 0
    gold -= variable3
  
  if pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 300 < my < 400 and Level1 == True and shop_slot_4_rar in range (variable1, variable2) and shop_slot_4_var_common == variable and Spawning1 == True and Spawning2 == True and Spawning3 == False and gold >variable3:
    pokemon_x3 = 250
    pokemon_y3 = 645
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))
    Spawning3 = True
    shop_slot_4_var_common = 0  
    shop_slot_4_rar = 0
    gold -= variable3

  if Spawning1:
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))

  if Spawning2:
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))

  if Spawning3:
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))

  return Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_4_var_common, shop_slot_4_rar, gold

#Shop-Slot 5

def spawn_Pokemon5_common(Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_5_var_common, shop_slot_5_rar, gold):
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 200 < my < 300 and Level1 == True and shop_slot_5_rar in range (variable1, variable2) and shop_slot_5_var_common == variable and Spawning1 == False and Spawning4 == False and gold >variable3:
    pokemon_x1 = 250
    pokemon_y1 = 645
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))
    Spawning1 = True
    shop_slot_5_var_common = 0 
    shop_slot_5_rar = 0
    gold -= variable3

  if pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 200 < my < 300 and Level1 == True and shop_slot_5_rar in range (variable1, variable2) and shop_slot_5_var_common == variable and Spawning1 == True and Spawning2 == False and gold >variable3:
    pokemon_x2 = 250
    pokemon_y2 = 645
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))
    Spawning2 = True
    shop_slot_5_var_common = 0  
    shop_slot_5_rar = 0
    gold -= variable3

  if pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 200 < my < 300 and Level1 == True and shop_slot_5_rar in range (variable1, variable2) and shop_slot_5_var_common == variable and Spawning1 == True and Spawning2 == True and Spawning3 == False and gold >variable3:
    pokemon_x3 = 250
    pokemon_y3 = 645
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))
    Spawning3 = True
    shop_slot_5_var_common = 0 
    shop_slot_5_rar = 0
    gold -= variable3

  if Spawning1:
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))


  if Spawning2:
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))  

  if Spawning3:
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))

  return Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_5_var_common, shop_slot_5_rar, gold

pulling = False
#Pokemon bewegen
def move_Pokemon(pokemon_x, pokemon_y):
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0] == True and mx > pokemon_x and abs(pokemon_x -mx) < 96 and my > pokemon_y and  abs(my - pokemon_y) < 96:
    pokemon_x = mx - 48
    pokemon_y = my - 48
  return pokemon_x, pokemon_y


#Pokemon droppen

def drop_Pokemon_bench(pokemon_x, pokemon_y):
  #Bank Slot 1
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== False and 235 <mx < 343 and 644 < my < 750 and mx > pokemon_x and abs((pokemon_x+48) - mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 250
    pokemon_y = 645

  #Bank Slot 2
  elif pygame.mouse.get_pressed()[0]== False and 343 <mx < 450 and 644 < my < 750 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 357
    pokemon_y = 645

  #Bank Slot 3
  elif pygame.mouse.get_pressed()[0]== False and 450 <mx < 555 and 644 < my < 750 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 459
    pokemon_y = 645

  #Bank Slot 4
  elif pygame.mouse.get_pressed()[0]== False and 555 <mx < 662 and 644 < my < 750 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 560
    pokemon_y = 645

  #Bank Slot 5
  elif pygame.mouse.get_pressed()[0]== False and 662 <mx < 768 and 644 < my < 750 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 665
    pokemon_y = 645

  #Bank Slot 6
  elif pygame.mouse.get_pressed()[0]== False and 768 <mx < 877 and 644 < my < 750 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 771
    pokemon_y = 645

  #Bank Slot 7
  elif pygame.mouse.get_pressed()[0]== False and 877 <mx < 983 and 644 < my < 750 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 874
    pokemon_y = 645

  #Bank Slot 8
  elif pygame.mouse.get_pressed()[0]== False and 983 <mx < 1081 and 644 < my < 750 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 977
    pokemon_y = 645

  #Bank Slot 9
  elif pygame.mouse.get_pressed()[0]== False and 1081 <mx < 1203 and 644 < my < 750 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 1083
    pokemon_y = 645
  return pokemon_x, pokemon_y


def drop_Pokemon_arena(pokemon_x, pokemon_y):
  #(1/1)
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== False and 260 <mx < 363 and 578 < my < 645 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 262
    pokemon_y = 562
    
  #(1/2)
  if pygame.mouse.get_pressed()[0]== False and 363 <mx < 464 and 578 < my < 645 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 363
    pokemon_y = 562

  #(1/3)
  if pygame.mouse.get_pressed()[0]== False and 464 <mx < 566 and 578 < my < 645 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 464
    pokemon_y = 562

  #(1/4)
  if pygame.mouse.get_pressed()[0]== False and 566 <mx < 668 and 578 < my < 645 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 566
    pokemon_y = 562

  #(1/5)
  if pygame.mouse.get_pressed()[0]== False and 668 <mx < 770 and 578 < my < 645 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 668
    pokemon_y = 562

  #(1/6)
  if pygame.mouse.get_pressed()[0]== False and 770 <mx < 873 and 578 < my < 645 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 770
    pokemon_y = 562

  #(1/7)
  if pygame.mouse.get_pressed()[0]== False and 873 <mx < 977 and 578 < my < 645 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 873
    pokemon_y = 562

  #(1/8)
  if pygame.mouse.get_pressed()[0]== False and 977 <mx < 1079 and 578 < my < 645 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 977
    pokemon_y = 562

  #(1/9)
  if pygame.mouse.get_pressed()[0]== False and 1079 <mx < 1187 and 578 < my < 645 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 1079
    pokemon_y = 562

    

  #(2/1)
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== False and 279 <mx < 378 and 509 < my < 578 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 273
    pokemon_y = 494
    
  #(2/2)
  if pygame.mouse.get_pressed()[0]== False and 378 <mx < 474 and 509 < my < 578 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 374
    pokemon_y = 494

  #(2/3)
  if pygame.mouse.get_pressed()[0]== False and 474 <mx < 572 and 509 < my < 578 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 470
    pokemon_y = 494

  #(2/4)
  if pygame.mouse.get_pressed()[0]== False and 572 <mx < 670 and 509 < my < 578 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 569
    pokemon_y = 494

  #(2/5)
  if pygame.mouse.get_pressed()[0]== False and 670 <mx < 770 and 509 < my < 578 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 666
    pokemon_y = 494

  #(2/6)
  if pygame.mouse.get_pressed()[0]== False and 770 <mx < 870 and 509 < my < 578 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 771
    pokemon_y = 494

  #(2/7)
  if pygame.mouse.get_pressed()[0]== False and 870 <mx < 969 and 509 < my < 578 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 869
    pokemon_y = 494

  #(2/8)
  if pygame.mouse.get_pressed()[0]== False and 969 <mx < 1068 and 509 < my < 578 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 969
    pokemon_y = 494

  #(2/9)
  if pygame.mouse.get_pressed()[0]== False and 1068 <mx < 1172 and 509 < my < 578 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 1070
    pokemon_y = 494


  #(3/1)
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== False and 296 <mx < 392 and 441 < my < 509 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 293
    pokemon_y = 426
    
  #(3/2)
  if pygame.mouse.get_pressed()[0]== False and 392 <mx < 485 and 441 < my < 509 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 386
    pokemon_y = 426

  #(3/3)
  if pygame.mouse.get_pressed()[0]== False and 485 <mx < 579 and 441 < my < 509 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 482
    pokemon_y = 426

  #(3/4)
  if pygame.mouse.get_pressed()[0]== False and 579 <mx < 672 and 441 < my < 509 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 576
    pokemon_y = 426

  #(3/5)
  if pygame.mouse.get_pressed()[0]== False and 672 <mx < 770 and 441 < my < 509 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 671
    pokemon_y = 426

  #(3/6)
  if pygame.mouse.get_pressed()[0]== False and 770 <mx < 867 and 441 < my < 509 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 768
    pokemon_y = 426

  #(3/7)
  if pygame.mouse.get_pressed()[0]== False and 867 <mx < 963 and 441 < my < 509 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 866
    pokemon_y = 426

  #(3/8)
  if pygame.mouse.get_pressed()[0]== False and 963 <mx < 1038 and 441 < my < 509 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 962
    pokemon_y = 426

  #(3/9)
  if pygame.mouse.get_pressed()[0]== False and 1038 <mx < 1158 and 441 < my < 509 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 1061
    pokemon_y = 426
    

  #(4/1)
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== False and 314 <mx < 405 and 374 < my < 441 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 309
    pokemon_y = 356
    
  #(4/2)
  if pygame.mouse.get_pressed()[0]== False and 405 <mx < 494 and 374 < my < 441 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 401
    pokemon_y = 356

  #(4/3)
  if pygame.mouse.get_pressed()[0]== False and 494 <mx < 585 and 374 < my < 441 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 491
    pokemon_y = 356

  #(4/4)
  if pygame.mouse.get_pressed()[0]== False and 585 <mx < 675 and 374 < my < 441 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 581
    pokemon_y = 356

  #(4/5)
  if pygame.mouse.get_pressed()[0]== False and 675 <mx < 770 and 374 < my < 441 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 674
    pokemon_y = 356

  #(4/6)
  if pygame.mouse.get_pressed()[0]== False and 770 <mx < 864 and 374 < my < 441 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 768
    pokemon_y = 356

  #(4/7)
  if pygame.mouse.get_pressed()[0]== False and 864 <mx < 957 and 374 < my < 441 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 863
    pokemon_y = 356

  #(4/8)
  if pygame.mouse.get_pressed()[0]== False and 957 <mx < 1049 and 374 < my < 441 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 956
    pokemon_y = 356

  #(4/9)
  if pygame.mouse.get_pressed()[0]== False and 1049 <mx < 1143 and 374 < my < 441 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 1050
    pokemon_y = 356
    
  return pokemon_x, pokemon_y

  
  

#Pokemon automatisch versetzten
def replace_Pokemon(serpifeu_x1, serpifeu_y1, serpifeu_x2, serpifeu_y2, serpifeu_x3, serpifeu_y3, efoserp_x1, efoserp_y1, efoserp_x2, efoserp_y2, efoserp_x3, efoserp_y3, serpiroyal_x1, serpiroyal_y1, floink_x1, floink_y1, floink_x2, floink_y2, floink_x3, floink_y3, ferkokel_x1, ferkokel_y1, ferkokel_x2, ferkokel_y2, ferkokel_x3, ferkokel_y3, flambirex_x1, flambirex_y1, ottaro_x1, ottaro_y1, ottaro_x2, ottaro_y2, ottaro_x3, ottaro_y3, zwottronin_x1, zwottronin_y1, zwottronin_x2, zwottronin_y2, zwottronin_x3, zwottronin_y3, admurai_x1, admurai_y1):
  if (serpifeu_x1, serpifeu_y1) == (serpifeu_x2, serpifeu_y2) or (serpifeu_x1, serpifeu_y1) == (serpifeu_x3, serpifeu_y3) or (serpifeu_x1, serpifeu_y1) == (efoserp_x1, efoserp_y1) or (serpifeu_x1, serpifeu_y1) == (efoserp_x2, efoserp_y2) or (serpifeu_x1, serpifeu_y1) == (efoserp_x3, efoserp_y3) or (serpifeu_x1, serpifeu_y1) == (serpiroyal_x1, serpiroyal_y1) or (serpifeu_x1, serpifeu_y1) == (floink_x1, floink_y1) or (serpifeu_x1, serpifeu_y1) == (floink_x2, floink_y2) or (serpifeu_x1, serpifeu_y1) == (floink_x3, floink_y3) or (serpifeu_x1, serpifeu_y1) == (ferkokel_x1, ferkokel_y1) or (serpifeu_x1, serpifeu_y1) == (ferkokel_x2, ferkokel_y2) or (serpifeu_x1, serpifeu_y1) == (ferkokel_x3, ferkokel_y3) or (serpifeu_x1, serpifeu_y1) == (flambirex_x1, flambirex_y1) or (serpifeu_x1, serpifeu_y1) == (ottaro_x1, ottaro_y1) or (serpifeu_x1, serpifeu_y1) == (ottaro_x2, ottaro_y2) or (serpifeu_x1, serpifeu_y1) == (ottaro_x3, ottaro_y3) or (serpifeu_x1, serpifeu_y1) == (zwottronin_x1, zwottronin_y1) or (serpifeu_x1, serpifeu_y1) == (zwottronin_x2, zwottronin_y2) or (serpifeu_x1, serpifeu_y1) == (zwottronin_x3, zwottronin_y3) or (serpifeu_x1, serpifeu_y1) == (admurai_x1, admurai_y1) == (250, 645):
    (serpifeu_x1, serpifeu_y1) = (357, 645)

  return serpifeu_x1, serpifeu_y1, serpifeu_x2, serpifeu_y2, serpifeu_x3, serpifeu_y3, efoserp_x1, efoserp_y1, efoserp_x2, efoserp_y2, efoserp_x3, efoserp_y3, serpiroyal_x1, serpiroyal_y1, floink_x1, floink_y1, floink_x2, floink_y2, floink_x3, floink_y3, ferkokel_x1, ferkokel_y1, ferkokel_x2, ferkokel_y2, ferkokel_x3, ferkokel_y3, flambirex_x1, flambirex_y1, ottaro_x1, ottaro_y1, ottaro_x2, ottaro_y2, ottaro_x3, ottaro_y3, zwottronin_x1, zwottronin_y1, zwottronin_x2, zwottronin_y2, zwottronin_x3, zwottronin_y3, admurai_x1, admurai_y1
  

def evolve_Pokemon1(Spawning1, Spawning2, Spawning3, Spawning4, Spawning5, Spawning6, Spawning7, pokemon_x1, pokemon_x2, pokemon_x3, pokemon_x4, pokemon_x5, pokemon_x6, pokemon_y1, pokemon_y2, pokemon_y3, pokemon_y4, pokemon_y5, pokemon_y6, pokemon1, pokemon2, pokemon3, zahl1, zahl2, zahl3, zahl10, screen):
  if Spawning1 == True and Spawning2 == True and Spawning3 == True and Spawning4 == False and Spawning7 == False and zahl10 == eins:
    Spawning1 = False
    Spawning2 = False
    Spawning3 = False
    Spawning4 = True
    pokemon_x1 = 250
    pokemon_y1 = 645
    pokemon_x4= zahl1
    pokemon_y4= 0
    pokemon_x5= zahl2
    pokemon_y5= 0
    pokemon_x6= zahl3
    pokemon_y6= 0

  elif Spawning1 == True and Spawning2 == True and Spawning3 == True and Spawning4 == False and Spawning7 == False and zahl10 == zwei:
    Spawning1 = False
    Spawning2 = False
    Spawning3 = False
    Spawning4 = True
    pokemon_x1 = 1017
    pokemon_y1 = 25
    pokemon_x4= zahl1
    pokemon_y4= 0
    pokemon_x5= zahl2
    pokemon_y5= 0
    pokemon_x6= zahl3
    pokemon_y6= 0

  
  if Spawning1 == True and Spawning2 == True and Spawning3 == True and Spawning4 == True and Spawning5 == False and Spawning7 == False and zahl10 == eins:
    Spawning1 = False
    Spawning2 = False
    Spawning3 = False
    Spawning5 = True
    pokemon_x2 = 250
    pokemon_y2 = 645
    pokemon_x4= zahl1
    pokemon_y4= 0
    pokemon_x5= zahl2
    pokemon_y5= 0
    pokemon_x6= zahl3
    pokemon_y6= 0

  elif Spawning1 == True and Spawning2 == True and Spawning3 == True and Spawning4 == True and Spawning5 == False and Spawning7 == False and zahl10 == zwei:
    Spawning1 = False
    Spawning2 = False
    Spawning3 = False
    Spawning5 = True
    pokemon_x2 = 1017
    pokemon_y2 = 25
    pokemon_x4= zahl1
    pokemon_y4= 0
    pokemon_x5= zahl2
    pokemon_y5= 0
    pokemon_x6= zahl3
    pokemon_y6= 0

  if Spawning1 == True and Spawning2 == True and Spawning3 == True and Spawning4 == True and Spawning5 == True and Spawning6 == False and Spawning7 == False and zahl10 == eins:
    Spawning1 = False
    Spawning2 = False
    Spawning3 = False
    Spawning6 = True
    pokemon_x3 = 250
    pokemon_y3 = 645
    pokemon_x4= zahl1
    pokemon_y4= 0
    pokemon_x5= zahl2
    pokemon_y5= 0
    pokemon_x6= zahl3
    pokemon_y6= 0

  elif Spawning1 == True and Spawning2 == True and Spawning3 == True and Spawning4 == True and Spawning5 == True and Spawning6 == False and Spawning7 == False and zahl10 == zwei:
    Spawning1 = False
    Spawning2 = False
    Spawning3 = False
    Spawning6 = True
    pokemon_x3 = 1017
    pokemon_y3 = 25
    pokemon_x4= zahl1
    pokemon_y4= 0
    pokemon_x5= zahl2
    pokemon_y5= 0
    pokemon_x6= zahl3
    pokemon_y6= 0


  if Spawning4 == True:
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))
  
  if Spawning5 == True:
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))
  
  if Spawning6 == True:
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))
  

  return Spawning1, Spawning2, Spawning3, Spawning4, Spawning5, Spawning6, Spawning7, pokemon_x1, pokemon_x2, pokemon_x3, pokemon_x4, pokemon_x5, pokemon_x6, pokemon_y1, pokemon_y2, pokemon_y3, pokemon_y4, pokemon_y5, pokemon_y6, pokemon1, pokemon2, pokemon3, zahl1, zahl2, zahl3, zahl10, screen

def evolve_Pokemon2(Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x4, pokemon_x3, pokemon_x2, pokemon_x1, pokemon_y4, pokemon_y3, pokemon_y2, pokemon_y1, pokemon1, zahl1, zahl2, zahl3, zahl10, screen):
  if Spawning1 == True and Spawning2 == True and Spawning3 == True and Spawning4 == False and zahl10 == eins:
    Spawning1 = False
    Spawning2 = False
    Spawning3 = False
    Spawning4 = True
    pokemon_x4 = 250
    pokemon_y4 = 645
    pokemon_x1 = zahl1
    pokemon_y1=0
    pokemon_x2= zahl2
    pokemon_y2=0
    pokemon_x3=zahl3
    pokemon_y3=0

  elif Spawning1 == True and Spawning2 == True and Spawning3 == True and Spawning4 == False and zahl10 == zwei:
    Spawning1 = False
    Spawning2 = False
    Spawning3 = False
    Spawning4 = True
    pokemon_x4 = 1017
    pokemon_y4 = 25
    pokemon_x1 = zahl1
    pokemon_y1=0
    pokemon_x2= zahl2
    pokemon_y2=0
    pokemon_x3=zahl3
    pokemon_y3=0
  
  if Spawning4 == True:
    screen.blit(pokemon1, (pokemon_x4, pokemon_y4)) 
  
  return Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x4, pokemon_x3, pokemon_x2, pokemon_x1, pokemon_y4, pokemon_y3, pokemon_y2, pokemon_y1, pokemon1, zahl1, zahl2, zahl3, zahl10, screen
  
#Pokemon verkaufen

def sell_Pokemon(Spawning, pokemon_x, pokemon_y, zahl, zahl2, gold):
  if Spawning == True and pygame.mouse.get_pressed()[0]== False and 294 > pokemon_y > -50 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 751 > pokemon_y > 721 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 721 > pokemon_y > 618 and 160 > pokemon_x > -50 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 721 > pokemon_y > 618 and 1500 > pokemon_x > 1190  or Spawning == True and pygame.mouse.get_pressed()[0]== False and 618 > pokemon_y > 545 and 188 > pokemon_x > -50 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 618 > pokemon_y > 545 and 1500 > pokemon_x > 1210 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 545 > pokemon_y > 475 and 204 > pokemon_x > -50 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 545 > pokemon_y > 475 and 1500 > pokemon_x > 1143 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 475 > pokemon_y > 404 and 225 > pokemon_x > -50 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 475 > pokemon_y > 404 and 1500 > pokemon_x > 1130 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 404 > pokemon_y > 294 and 248 > pokemon_x > -50 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 404 > pokemon_y > 294 and 1500 > pokemon_x > 1158:
    Spawning = False
    pokemon_x = zahl
    pokemon_y = 0
    gold += zahl2
  return Spawning, pokemon_x, pokemon_y, zahl, zahl2, gold

#Shop rerollen
def reroll_Shop(shop_slot_1_rar, shop_slot_2_rar, shop_slot_3_rar, shop_slot_4_rar, shop_slot_5_rar, shop_slot_1_var_common, shop_slot_2_var_common, shop_slot_3_var_common, shop_slot_4_var_common, shop_slot_5_var_common, shop_slot_1_var_uncommon, shop_slot_2_var_uncommon, shop_slot_3_var_uncommon, shop_slot_4_var_uncommon, shop_slot_5_var_uncommon, shop_slot_1_var_rare, shop_slot_2_var_rare, shop_slot_3_var_rare, shop_slot_4_var_rare, shop_slot_5_var_rare, shop_slot_1_var_epic, shop_slot_2_var_epic, shop_slot_3_var_epic, shop_slot_4_var_epic, shop_slot_5_var_epic, gold):
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 0 < my < 100 and gold >1:
    shop_slot_1_rar = randint(1,10)
    shop_slot_2_rar = randint(1,10)
    shop_slot_3_rar = randint(1,10)
    shop_slot_4_rar = randint(1,10)
    shop_slot_5_rar = randint(1,10)

    shop_slot_1_var_common = randint(1, 3)
    shop_slot_2_var_common = randint(1, 3)
    shop_slot_3_var_common = randint(1, 3)
    shop_slot_4_var_common = randint(1, 3)
    shop_slot_5_var_common = randint(1, 3)

    shop_slot_1_var_uncommon = randint(1, 3)
    shop_slot_2_var_uncommon = randint(1, 3)
    shop_slot_3_var_uncommon = randint(1, 3)
    shop_slot_4_var_uncommon = randint(1, 3)
    shop_slot_5_var_uncommon = randint(1, 3)
    
    shop_slot_1_var_rare = randint(1, 3)
    shop_slot_2_var_rare = randint(1, 3)
    shop_slot_3_var_rare = randint(1, 3)
    shop_slot_4_var_rare = randint(1, 3)
    shop_slot_5_var_rare = randint(1, 3)
    
    shop_slot_1_var_epic = randint(1, 3)
    shop_slot_2_var_epic = randint(1, 3)
    shop_slot_3_var_epic = randint(1, 3)
    shop_slot_4_var_epic = randint(1, 3)
    shop_slot_5_var_epic = randint(1, 3)
    gold -= 2
  
  return shop_slot_1_rar, shop_slot_2_rar, shop_slot_3_rar, shop_slot_4_rar, shop_slot_5_rar, shop_slot_1_var_common, shop_slot_2_var_common, shop_slot_3_var_common, shop_slot_4_var_common, shop_slot_5_var_common, shop_slot_1_var_uncommon, shop_slot_2_var_uncommon, shop_slot_3_var_uncommon, shop_slot_4_var_uncommon, shop_slot_5_var_uncommon, shop_slot_1_var_rare, shop_slot_2_var_rare, shop_slot_3_var_rare, shop_slot_4_var_rare, shop_slot_5_var_rare, shop_slot_1_var_epic, shop_slot_2_var_epic, shop_slot_3_var_epic, shop_slot_4_var_epic, shop_slot_5_var_epic, gold

def reroll_Shop2(Spawning, shop_slot_1_var_common, shop_slot_2_var_common, shop_slot_3_var_common, shop_slot_4_var_common, shop_slot_5_var_common, zahl):
  if Spawning == True and shop_slot_1_var_common == zahl:
    shop_slot_1_var_common = randint(1, 3)
  if Spawning == True and shop_slot_2_var_common == zahl:
    shop_slot_2_var_common = randint(1, 3)
  if Spawning == True and shop_slot_3_var_common == zahl:
    shop_slot_3_var_common = randint(1, 3)
  if Spawning == True and shop_slot_4_var_common == zahl:
    shop_slot_4_var_common = randint(1, 3)
  if Spawning == True and shop_slot_5_var_common == zahl:
    shop_slot_5_var_common = randint(1, 3)
  return Spawning, shop_slot_1_var_common, shop_slot_2_var_common, shop_slot_3_var_common, shop_slot_4_var_common, shop_slot_5_var_common, zahl

def reroll_Shop3(Spawning1, Spawning2, Spawning3, zahl1, zahl2, rarity1, rarity2, rarity3, rarity4, rarity5):
  if Spawning1 == True and Spawning2 == True and Spawning3 == True and rarity1 in range (zahl1, zahl2):
    rarity1 = randint(1, 10)
  if Spawning1 == True and Spawning2 == True and Spawning3 == True and rarity2 in range (zahl1, zahl2):
    rarity2 = randint(1, 10)
  if Spawning1 == True and Spawning2 == True and Spawning3 == True and rarity3 in range (zahl1, zahl2):
    rarity3 = randint(1, 10)
  if Spawning1 == True and Spawning2 == True and Spawning3 == True and rarity4 in range (zahl1, zahl2):
    rarity4 = randint(1, 10)
  if Spawning1 == True and Spawning2 == True and Spawning3 == True and rarity5 in range (zahl1, zahl2):
    rarity5 = randint(1, 10)
  return Spawning1, Spawning2, Spawning3, zahl1, zahl2, rarity1, rarity2, rarity3, rarity4, rarity5






  

def check_Pokemon(ally_list, pokemon_x, pokemon_y, pokemon):
  if 286 < (pokemon_x -48) < 1165 and 374 < (pokemon_y -48) < 647:
    ally_list += [pokemon]
  for x in ally_list:
    if x == pokemon and (pokemon_x-48) < 286 or (pokemon_x-48) > 1165 and (pokemon_y-48) < 647 or (pokemon_y-48) > 374:
      ally_list -= [pokemon]
  return ally_list, pokemon_x, pokemon_y, pokemon



  


#Einteilung des Spielfelds
#Rechte Kante
def draw_spielfeld(arena):
  arena_x = 0
  arena_y = 0
  
  kante_rechts = pygame.draw.line(arena, schwarz, [1080, 102], [1216, 753], 1)
  #Linke Kante
  kante_links = pygame.draw.line(arena, schwarz, [392, 102], [222, 750], 1)
  #Obere Kante 
  
  #Untere Kante 
  kante_unten = pygame.draw.line(arena, schwarz, [222, 750], [1216, 753], 1)

  #Spalte 1
  spalte1 = pygame.draw.line(arena, schwarz, [468, 102], [333, 750], 1)

  #Spalte 2

  spalte2 = pygame.draw.line(arena, schwarz, [542, 102], [440, 751], 1)

  #Spalte 3
  spalte3 = pygame.draw.line(arena, schwarz, [617, 102], [549, 750], 1)

  #Spalte 4
  spalte4 = pygame.draw.line(arena, schwarz, [690, 102], [659, 751], 1)

  #Spalte 5
  spalte5 = pygame.draw.line(arena, schwarz, [770, 102], [768, 752], 1)

  #Spalte 6
  spalte6 = pygame.draw.line(arena, schwarz, [851, 102], [878, 752], 1)

  #Spalte 7
  spalte7 = pygame.draw.line(arena, schwarz, [930, 102], [987, 752], 1)

  #Spalte 8
  spalte8 = pygame.draw.line(arena, schwarz, [1005, 102], [1097, 752], 1)

  #Reihe 1
  reihe1 = pygame.draw.line(arena, schwarz, [250, 644], [1193, 644], 1)

  #Reihe 2
  reihe2 = pygame.draw.line(arena, schwarz, [269, 576], [1179, 576], 1)

  #Reihe 3
  reihe3 = pygame.draw.line(arena, schwarz, [287, 508], [1165, 508], 1)

  #Reihe 4
  reihe4 = pygame.draw.line(arena, schwarz, [305, 440], [1152, 440], 1)

  #Reihe 5
  reihe5 = pygame.draw.line(arena, rot, [323, 372], [1137, 372], 3)

  #Reihe 6

  reihe6 = pygame.draw.line(arena, schwarz, [338, 304], [1122, 304], 1)

  #Reihe 7

  reihe7 = pygame.draw.line(arena, schwarz, [357, 236], [1108, 236], 1)

  #Reihe 8

  reihe8 = pygame.draw.line(arena, schwarz, [376, 168], [1094, 168], 1)

  #Reihe 9

  reihe9 = pygame.draw.line(arena, schwarz, [393, 102], [1080, 102], 1)

  #Bank gegner

  kante_linksg= pygame.draw.line(arena, schwarz, [434, 102], [444, 53], 1)
  kante_obeng= pygame.draw.line(arena, schwarz, [1097, 53], [444, 53], 1)
  kante_rechtsg= pygame.draw.line(arena, schwarz, [1097,53], [1110, 102])
  kante_unteng= pygame.draw.line(arena, schwarz, [434, 102], [1110, 102], 1)
  spalte1g= pygame.draw.line(arena, schwarz, [513, 102], [519, 53], 1)
  spalte2g= pygame.draw.line(arena, schwarz, [583, 102], [590, 53], 1)
  spalte3g= pygame.draw.line(arena, schwarz, [658, 102], [662, 53], 1)
  spalte4g= pygame.draw.line(arena, schwarz, [731, 102], [732, 53], 1)
  spalte5g= pygame.draw.line(arena, schwarz, [807, 102], [807, 53], 1)
  spalte6g= pygame.draw.line(arena, schwarz, [881, 102], [878, 53], 1)
  spalte7g= pygame.draw.line(arena, schwarz, [954, 102], [948, 53], 1)
  spalte1g= pygame.draw.line(arena, schwarz, [1029, 102], [1019, 53], 1)

  
  




  
  #Eigene Bank 


  #Einfügen vonLayoutbestandteilen
  #Shop
def draw_shop(arena):
  arena_x = 0
  arena_y = 0
  shop = pygame.draw.rect(arena, schwarz, (0, 0, 150, 700))




shop_slot_1_rarg = randint(1,10)
shop_slot_2_rarg = randint(1,10)
shop_slot_3_rarg = randint(1,10)
shop_slot_4_rarg = randint(1,10)
shop_slot_5_rarg = randint(1,10)

shop_slot_1_var_commong = randint(1, 3)
shop_slot_2_var_commong = randint(1, 3)
shop_slot_3_var_commong = randint(1, 3)
shop_slot_4_var_commong = randint(1, 3)
shop_slot_5_var_commong = randint(1, 3)

shop_slot_1_var_uncommong = randint(1, 3)
shop_slot_2_var_uncommong = randint(1, 3)
shop_slot_3_var_uncommong = randint(1, 3)
shop_slot_4_var_uncommong = randint(1, 3)
shop_slot_5_var_uncommong = randint(1, 3)

shop_slot_1_var_rareg = randint(1, 3)
shop_slot_2_var_rareg = randint(1, 3)
shop_slot_3_var_rareg = randint(1, 3)
shop_slot_4_var_rareg = randint(1, 3)
shop_slot_5_var_rareg = randint(1, 3)

shop_slot_1_var_epicg = randint(1, 3)
shop_slot_2_var_epicg = randint(1, 3)
shop_slot_3_var_epicg = randint(1, 3)
shop_slot_4_var_epicg = randint(1, 3)
shop_slot_5_var_epicg = randint(1, 3)

goldg=100

#Shop-Pokemon darstellen

def show_Pokemon1g(pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_1_rarg, shop_slot_1_var_commong):
  if Level1==True:
    if shop_slot_1_rarg in range (zahl1, zahl2):
      if shop_slot_1_var_commong == zahl:
        screen.blit(pokemon1, (pokemon_x1, pokemon_y1))

  return pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_1_rarg, shop_slot_1_var_commong
      

def show_Pokemon2g(pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_2_rarg, shop_slot_2_var_commong):
  if Level1==True:
    if shop_slot_2_rarg in range (zahl1, zahl2):
      if shop_slot_2_var_commong == zahl:
        screen.blit(pokemon1, (pokemon_x1, pokemon_y1))

  return pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_2_rarg, shop_slot_2_var_commong

def show_Pokemon3g(pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_3_rarg, shop_slot_3_var_commong):
  if Level1==True:
    if shop_slot_3_rarg in range (zahl1, zahl2):
      if shop_slot_3_var_commong == zahl:
        screen.blit(pokemon1, (pokemon_x1, pokemon_y1))

  return pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_3_rarg, shop_slot_3_var_commong

def show_Pokemon4g(pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_4_rarg, shop_slot_4_var_commong):
  if Level1==True:
    if shop_slot_4_rarg in range (zahl1, zahl2):
      if shop_slot_4_var_commong == zahl:
        screen.blit(pokemon1, (pokemon_x1, pokemon_y1))

  return pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_4_rarg, shop_slot_4_var_commong

def show_Pokemon5g(pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_5_rarg, shop_slot_5_var_commong):
  if Level1==True:
    if shop_slot_5_rarg in range (zahl1, zahl2):
      if shop_slot_5_var_commong == zahl:
        screen.blit(pokemon1, (pokemon_x1, pokemon_y1))

  return pokemon1, pokemon_x1, pokemon_y1, zahl, zahl1, zahl2, screen, shop_slot_5_rarg, shop_slot_5_var_commong




#Pokemon spawnen

#Shop-Slot 1

def spawn_Pokemon1_commong(Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_1_var_commong, shop_slot_1_rarg, goldg):
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== True and 1350 < mx < 1500 and 600 < my < 700 and Level1 == True and shop_slot_1_rarg in range (variable1, variable2) and shop_slot_1_var_commong == variable and Spawning1 == False and Spawning4 == False and goldg >variable3:
    pokemon_x1 = 1017
    pokemon_y1 = 25
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))
    Spawning1 = True
    shop_slot_1_var_commong = 0
    shop_slot_1_rarg = 0
    goldg -= variable3

  if pygame.mouse.get_pressed()[0]== True and 1350 < mx < 1500 and 600 < my < 700 and Level1 == True and shop_slot_1_rarg in range (variable1, variable2) and shop_slot_1_var_commong == variable and Spawning1 == True and Spawning2 == False and goldg >variable3:
    pokemon_x2 = 1017
    pokemon_y2 = 52
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))
    Spawning2 = True
    shop_slot_1_var_commong = 0
    shop_slot_1_rarg = 0
    goldg -= variable3
    
  
  if pygame.mouse.get_pressed()[0]== True and 1350 < mx < 1500 and 600 < my < 700 and Level1 == True and shop_slot_1_rarg in range (variable1, variable2) and shop_slot_1_var_commong == variable and Spawning1 == True and Spawning2 == True and Spawning3 == False and goldg >variable3:
    pokemon_x3 = 1017
    pokemon_y3 = 25
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))
    Spawning3 = True
    shop_slot_1_var_commong = 0
    shop_slot_1_rarg = 0
    goldg -= variable3


  return Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_1_var_commong, shop_slot_1_rarg, goldg

#Shop-Slot 2

def spawn_Pokemon2_commong(Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_2_var_commong, shop_slot_2_rarg, goldg):
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== True and 1350 < mx < 1500 and 500 < my < 600 and Level1 == True and shop_slot_2_rarg in range (variable1, variable2) and shop_slot_2_var_commong == variable and Spawning1 == False and Spawning4 == False and goldg >variable3:
    pokemon_x1 = 1017
    pokemon_y1 = 25
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))
    Spawning1 = True
    shop_slot_2_var_commong = 0
    shop_slot_2_rarg = 0
    goldg -= variable3

  if pygame.mouse.get_pressed()[0]== True and 1350 < mx < 1500 and 500 < my < 600 and Level1 == True and shop_slot_2_rarg in range (variable1, variable2) and shop_slot_2_var_commong == variable and Spawning1 == True and Spawning2 == False and goldg >variable3:
    pokemon_x2 = 1017
    pokemon_y2 = 25
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))
    Spawning2 = True
    shop_slot_2_var_commong = 0  
    shop_slot_2_rarg = 0
    goldg -= variable3

  if pygame.mouse.get_pressed()[0]== True and 1350 < mx < 1500 and 500 < my < 600 and Level1 == True and shop_slot_2_rarg in range (variable1, variable2) and shop_slot_2_var_commong == variable and Spawning1 == True and Spawning2 == True and Spawning3 == False and goldg >variable3:
    pokemon_x3 = 1017
    pokemon_y3 = 25
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))
    Spawning3 = True
    shop_slot_2_var_commong = 0  
    shop_slot_2_rarg = 0
    goldg -= variable3

  if Spawning1:
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))

  if Spawning2:
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))

  if Spawning3:
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))

  return Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_2_var_commong, shop_slot_2_rarg, goldg

#Shop-Slot 3  

def spawn_Pokemon3_commong(Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_3_var_commong, shop_slot_3_rarg, goldg):
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== True and 1350 < mx < 1500 and 400 < my < 500 and Level1 == True and shop_slot_3_rarg in range (variable1, variable2) and shop_slot_3_var_commong == variable and Spawning1 == False and Spawning4 == False and goldg >variable3:
    pokemon_x1 = 1017
    pokemon_y1 = 25
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))
    Spawning1 = True
    shop_slot_3_var_commong = 0  
    shop_slot_3_rarg = 0
    goldg -= variable3

  if pygame.mouse.get_pressed()[0]== True and 1350 < mx < 1500 and 400 < my < 500 and Level1 == True and shop_slot_3_rarg in range (variable1, variable2) and shop_slot_3_var_commong == variable and Spawning1 == True and Spawning2 == False and goldg >variable3:
    pokemon_x2 = 1017
    pokemon_y2 = 25
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))
    Spawning2 = True
    shop_slot_3_var_commong = 0
    shop_slot_3_rarg = 0
    goldg -= variable3

  if pygame.mouse.get_pressed()[0]== True and 1350 < mx < 1500 and 400 < my < 500 and Level1 == True and shop_slot_3_rarg in range (variable1, variable2) and shop_slot_3_var_commong == variable and Spawning1 == True and Spawning2 == True and Spawning3 == False and goldg >variable3:
    pokemon_x3 = 1017
    pokemon_y3 = 25
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))
    Spawning3 = True
    shop_slot_3_var_commong = 0  
    shop_slot_3_rarg = 0
    goldg -= variable3

  if Spawning1:
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))

  if Spawning2:
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))

  if Spawning3:
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))

  return Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_3_var_commong, shop_slot_3_rarg, goldg

#Shop-Slot 4

def spawn_Pokemon4_commong(Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_4_var_commong, shop_slot_4_rarg, goldg):
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== True and 1350 < mx < 1500 and 300 < my < 400 and Level1 == True and shop_slot_4_rar in range (variable1, variable2) and shop_slot_4_var_commong == variable and Spawning1 == False and Spawning4 == False and goldg >variable3:
    pokemon_x1 = 1017
    pokemon_y1 = 25
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))
    Spawning1 = True
    shop_slot_4_var_commong = 0  
    shop_slot_4_rarg = 0
    goldg -= variable3

  if pygame.mouse.get_pressed()[0]== True and 1350 < mx < 1500 and 300 < my < 400 and Level1 == True and shop_slot_4_rarg in range (variable1, variable2) and shop_slot_4_var_commong == variable and Spawning1 == True and Spawning2 == False and goldg >variable3:
    pokemon_x2 = 1017
    pokemon_y2 = 25
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))
    Spawning2 = True
    shop_slot_4_var_commong = 0  
    shop_slot_4_rarg = 0
    goldg -= variable3
  
  if pygame.mouse.get_pressed()[0]== True and 1350 < mx < 1500 and 300 < my < 400 and Level1 == True and shop_slot_4_rarg in range (variable1, variable2) and shop_slot_4_var_commong == variable and Spawning1 == True and Spawning2 == True and Spawning3 == False and goldg >variable3:
    pokemon_x3 = 1017
    pokemon_y3 = 25
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))
    Spawning3 = True
    shop_slot_4_var_commong = 0  
    shop_slot_4_rarg = 0
    goldg -= variable3

  if Spawning1:
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))

  if Spawning2:
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))

  if Spawning3:
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))

  return Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_4_var_commong, shop_slot_4_rarg, goldg

#Shop-Slot 5

def spawn_Pokemon5_commong(Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_5_var_commong, shop_slot_5_rarg, goldg):
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== True and 1350 < mx < 1500 and 200 < my < 300 and Level1 == True and shop_slot_5_rarg in range (variable1, variable2) and shop_slot_5_var_commong == variable and Spawning1 == False and Spawning4 == False and goldg >variable3:
    pokemon_x1 = 1017
    pokemon_y1 = 25
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))
    Spawning1 = True
    shop_slot_5_var_commong = 0  
    shop_slot_5_rarg = 0
    goldg -= variable3

  if pygame.mouse.get_pressed()[0]== True and 1350 < mx < 1500 and 200 < my < 300 and Level1 == True and shop_slot_5_rarg in range (variable1, variable2) and shop_slot_5_var_commong == variable and Spawning1 == True and Spawning2 == False and goldg >variable3:
    pokemon_x2 = 1017
    pokemon_y2 = 25
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))
    Spawning2 = True
    shop_slot_5_var_commong = 0 
    shop_slot_5_rarg = 0
    goldg -= variable3

  if pygame.mouse.get_pressed()[0]== True and 1350 < mx < 1500 and 200 < my < 300 and Level1 == True and shop_slot_5_rarg in range (variable1, variable2) and shop_slot_5_var_commong == variable and Spawning1 == True and Spawning2 == True and Spawning3 == False and goldg >variable3:
    pokemon_x3 = 1017
    pokemon_y3 = 25
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))
    Spawning3 = True
    shop_slot_5_var_commong = 0  
    shop_slot_5_rarg = 0
    goldg -= variable3

  if Spawning1:
    screen.blit(pokemon1, (pokemon_x1, pokemon_y1))


  if Spawning2:
    screen.blit(pokemon2, (pokemon_x2, pokemon_y2))  

  if Spawning3:
    screen.blit(pokemon3, (pokemon_x3, pokemon_y3))

  return Spawning1, Spawning2, Spawning3, Spawning4, pokemon_x1, pokemon_y1, pokemon1, pokemon_x2, pokemon_y2, pokemon2, pokemon_x3, pokemon_y3, pokemon3, variable, variable1, variable2, variable3, screen, shop_slot_5_var_commong, shop_slot_5_rarg, goldg



def drop_Pokemon_benchg(pokemon_x, pokemon_y):
  #Bank Slot 1
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== False and 440 <mx < 515 and 54 < my < 102 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 428
    pokemon_y = 25

  #Bank Slot 2
  elif pygame.mouse.get_pressed()[0]== False and 515 <mx < 587 and 54 < my < 102 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 55 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 60:
    pokemon_x = 514
    pokemon_y = 30

  #Bank Slot 3
  elif pygame.mouse.get_pressed()[0]== False and 587 <mx < 659 and 54 < my < 102 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 582
    pokemon_y = 25

  #Bank Slot 4
  elif pygame.mouse.get_pressed()[0]== False and 659 <mx < 732 and 54 < my < 102 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 654
    pokemon_y = 25

  #Bank Slot 5
  elif pygame.mouse.get_pressed()[0]== False and 732 <mx < 807 and 54 < my < 102 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 731
    pokemon_y = 25

  #Bank Slot 6
  elif pygame.mouse.get_pressed()[0]== False and 807 <mx < 879 and 54 < my < 102 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 803
    pokemon_y = 25

  #Bank Slot 7
  elif pygame.mouse.get_pressed()[0]== False and 879 <mx < 951 and 54 < my < 102 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 872
    pokemon_y = 25

  #Bank Slot 8
  elif pygame.mouse.get_pressed()[0]== False and 951 <mx < 1025 and 54 < my < 102 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 943
    pokemon_y = 25

  #Bank Slot 9
  elif pygame.mouse.get_pressed()[0]== False and 1025 <mx < 1104 and 54 < my < 102 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 1017
    pokemon_y = 25
  return pokemon_x, pokemon_y


def drop_Pokemon_arenag(pokemon_x, pokemon_y):
  #(1/1)
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== False and 385 <mx < 461 and 104 < my < 170 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 373
    pokemon_y = 87
    
  #(1/2)
  if pygame.mouse.get_pressed()[0]== False and 461 <mx < 536 and 104 < my < 170 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 451
    pokemon_y = 87

  #(1/3)
  if pygame.mouse.get_pressed()[0]== False and 536 <mx < 614 and 104 < my < 170 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 526
    pokemon_y = 87

  #(1/4)
  if pygame.mouse.get_pressed()[0]== False and 614 <mx < 689 and 104 < my < 170 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 604
    pokemon_y = 87

  #(1/5)
  if pygame.mouse.get_pressed()[0]== False and 689 <mx < 770 and 104 < my < 170 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 682
    pokemon_y = 87

  #(1/6)
  if pygame.mouse.get_pressed()[0]== False and 770 <mx < 853 and 104 < my < 170 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 763
    pokemon_y = 87

  #(1/7)
  if pygame.mouse.get_pressed()[0]== False and 853 <mx < 934 and 104 < my < 170 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 845
    pokemon_y = 87

  #(1/8)
  if pygame.mouse.get_pressed()[0]== False and 934 <mx < 1010 and 104 < my < 170 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 925
    pokemon_y = 87

  #(1/9)
  if pygame.mouse.get_pressed()[0]== False and 1010 <mx < 1087 and 104 < my < 170 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 1003
    pokemon_y = 87

    

  #(2/1)
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== False and 367 <mx < 448 and 170 < my < 239 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 357
    pokemon_y = 155
    
  #(2/2)
  if pygame.mouse.get_pressed()[0]== False and 448 <mx < 526 and 170 < my < 239 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 438
    pokemon_y = 155

  #(2/3)
  if pygame.mouse.get_pressed()[0]== False and 526 <mx < 607 and 170 < my < 239 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 517
    pokemon_y = 155

  #(2/4)
  if pygame.mouse.get_pressed()[0]== False and 607 <mx < 685 and 170 < my < 239 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 597
    pokemon_y = 155

  #(2/5)
  if pygame.mouse.get_pressed()[0]== False and 685 <mx < 770 and 170 < my < 239 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 678
    pokemon_y = 155

  #(2/6)
  if pygame.mouse.get_pressed()[0]== False and 770 <mx < 856 and 170 < my < 239 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 763
    pokemon_y = 155

  #(2/7)
  if pygame.mouse.get_pressed()[0]== False and 856 <mx < 939 and 170 < my < 239 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 849
    pokemon_y = 155

  #(2/8)
  if pygame.mouse.get_pressed()[0]== False and 939 <mx < 1020 and 170 < my < 239 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 933
    pokemon_y = 155

  #(2/9)
  if pygame.mouse.get_pressed()[0]== False and 1020 <mx < 1100 and 170 < my < 239 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 1015
    pokemon_y = 155


  #(3/1)
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== False and 349 <mx < 433 and 239 < my < 306 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 342
    pokemon_y = 225
    
  #(3/2)
  if pygame.mouse.get_pressed()[0]== False and 433 <mx < 516 and 239 < my < 306 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 426
    pokemon_y = 225

  #(3/3)
  if pygame.mouse.get_pressed()[0]== False and 516 <mx < 600 and 239 < my < 306 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 508
    pokemon_y = 225

  #(3/4)
  if pygame.mouse.get_pressed()[0]== False and 600 <mx < 682 and 239 < my < 306 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 591
    pokemon_y = 225

  #(3/5)
  if pygame.mouse.get_pressed()[0]== False and 682 <mx < 770 and 239 < my < 306 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 677
    pokemon_y = 225

  #(3/6)
  if pygame.mouse.get_pressed()[0]== False and 770 <mx < 859 and 239 < my < 306 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 765
    pokemon_y = 225

  #(3/7)
  if pygame.mouse.get_pressed()[0]== False and 859 <mx < 946 and 239 < my < 306 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 853
    pokemon_y = 225

  #(3/8)
  if pygame.mouse.get_pressed()[0]== False and 946 <mx < 1029 and 239 < my < 306 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 942
    pokemon_y = 225

  #(3/9)
  if pygame.mouse.get_pressed()[0]== False and 1029 <mx < 1117 and 239 < my < 306 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 1029
    pokemon_y = 225
    

  #(4/1)
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== False and 331 <mx < 420 and 306 < my < 373 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 325
    pokemon_y = 290
    
  #(4/2)
  if pygame.mouse.get_pressed()[0]== False and 420 <mx < 505 and 306 < my < 373 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 412
    pokemon_y = 290

  #(4/3)
  if pygame.mouse.get_pressed()[0]== False and 505 <mx < 592 and 306 < my < 373 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 501
    pokemon_y = 290

  #(4/4)
  if pygame.mouse.get_pressed()[0]== False and 592 <mx < 679 and 306 < my < 373 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 586
    pokemon_y = 290

  #(4/5)
  if pygame.mouse.get_pressed()[0]== False and 679 <mx < 770 and 306 < my < 373 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 675
    pokemon_y = 290

  #(4/6)
  if pygame.mouse.get_pressed()[0]== False and 770 <mx < 861 and 306 < my < 373 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 768
    pokemon_y = 290

  #(4/7)
  if pygame.mouse.get_pressed()[0]== False and 861 <mx < 952 and 306 < my < 373 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 863
    pokemon_y = 290

  #(4/8)
  if pygame.mouse.get_pressed()[0]== False and 952 <mx < 1039 and 306 < my < 373 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 948
    pokemon_y = 290

  #(4/9)
  if pygame.mouse.get_pressed()[0]== False and 1039 <mx < 1131 and 306 < my < 373 and mx > pokemon_x and abs((pokemon_x+48) -mx) < 30 and my > pokemon_y and  abs(my - (pokemon_y+48)) < 30:
    pokemon_x = 1039
    pokemon_y = 290
    
  return pokemon_x, pokemon_y


  
#Shop rerollen
def reroll_Shopg(shop_slot_1_rarg, shop_slot_2_rarg, shop_slot_3_rarg, shop_slot_4_rarg, shop_slot_5_rarg, shop_slot_1_var_commong, shop_slot_2_var_commong, shop_slot_3_var_commong, shop_slot_4_var_commong, shop_slot_5_var_commong,
shop_slot_1_var_uncommong, shop_slot_2_var_uncommong, shop_slot_3_var_uncommong, shop_slot_4_var_uncommong, shop_slot_5_var_uncommong, shop_slot_1_var_rareg, shop_slot_2_var_rareg, shop_slot_3_var_rareg, shop_slot_4_var_rareg, shop_slot_5_var_rareg, shop_slot_1_var_epicg, shop_slot_2_var_epicg, shop_slot_3_var_epicg, shop_slot_4_var_epicg, shop_slot_5_var_epicg, goldg):
  mx, my = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0]== True and 1350 < mx < 1500 and 0 < my < 100 and goldg >1:
    shop_slot_1_rarg = randint(1,10)
    shop_slot_2_rarg = randint(1,10)
    shop_slot_3_rarg = randint(1,10)
    shop_slot_4_rarg = randint(1,10)
    shop_slot_5_rarg = randint(1,10)

    shop_slot_1_var_commong = randint(1, 3)
    shop_slot_2_var_commong = randint(1, 3)
    shop_slot_3_var_commong = randint(1, 3)
    shop_slot_4_var_commong = randint(1, 3)
    shop_slot_5_var_commong = randint(1, 3)

    shop_slot_1_var_uncommong = randint(1, 3)
    shop_slot_2_var_uncommong = randint(1, 3)
    shop_slot_3_var_uncommong = randint(1, 3)
    shop_slot_4_var_uncommong = randint(1, 3)
    shop_slot_5_var_uncommong = randint(1, 3)

    shop_slot_1_var_rareg = randint(1, 3)
    shop_slot_2_var_rareg = randint(1, 3)
    shop_slot_3_var_rareg = randint(1, 3)
    shop_slot_4_var_rareg = randint(1, 3)
    shop_slot_5_var_rareg = randint(1, 3)
    
    shop_slot_1_var_epicg = randint(1, 3)
    shop_slot_2_var_epicg = randint(1, 3)
    shop_slot_3_var_epicg = randint(1, 3)
    shop_slot_4_var_epicg = randint(1, 3)
    shop_slot_5_var_epicg = randint(1, 3)
    goldg-=2
  
  return shop_slot_1_rarg, shop_slot_2_rarg, shop_slot_3_rarg, shop_slot_4_rarg, shop_slot_5_rarg, shop_slot_1_var_commong, shop_slot_2_var_commong, shop_slot_3_var_commong, shop_slot_4_var_commong, shop_slot_5_var_commong, shop_slot_1_var_uncommong, shop_slot_2_var_uncommong, shop_slot_3_var_uncommong, shop_slot_4_var_uncommong, shop_slot_5_var_uncommong, shop_slot_1_var_rareg, shop_slot_2_var_rareg, shop_slot_3_var_rareg, shop_slot_4_var_rareg, shop_slot_5_var_rareg, shop_slot_1_var_epicg, shop_slot_2_var_epicg, shop_slot_3_var_epicg, shop_slot_4_var_epicg, shop_slot_5_var_epicg, goldg



def sell_Pokemong(Spawning, pokemon_x, pokemon_y, zahl, zahl2, goldg):
  if Spawning == True and pygame.mouse.get_pressed()[0]== False and -15 > pokemon_y > -50 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 850 > pokemon_y > 344 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 35 > pokemon_y > -15 and 368 > pokemon_x > -50 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 35 > pokemon_y > -15 and 1500 > pokemon_x > 1076 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 104 > pokemon_y > 35 and 310 > pokemon_x > -50 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 104 > pokemon_y > 35 and 1500 > pokemon_x > 1064 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 173 > pokemon_y > 104 and 290 > pokemon_x > -50 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 173 > pokemon_y > 104 and 1500 > pokemon_x > 1075 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 240 > pokemon_y > 173 and 274 > pokemon_x > -50 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 240 > pokemon_y > 173 and 1500 > pokemon_x > 1087 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 344 > pokemon_y > 240 and 259 > pokemon_x > -50 or Spawning == True and pygame.mouse.get_pressed()[0]== False and 344 > pokemon_y > 240 and 1500 > pokemon_x > 1105:
    Spawning = False
    pokemon_x = zahl
    pokemon_y = 0
    goldg += zahl2
  return Spawning, pokemon_x, pokemon_y, zahl, zahl2, goldg






def draw_shopg(arena):
  arena_x = 0
  arena_y = 0
  shop = pygame.draw.rect(arena, schwarz, (1350, 0, 150, 700))

def get_pokemon_pos(pokemon_x, pokemon_y):
  pokemon_pos = pokemon_x, pokemon_y
  return pokemon_pos

#font1 = pygame.font.SysFont('freesans', 72)

#gold_anzeige = font1.render(gold, True, gelb)

#def show_Gold(gold_anzeige, screen):
  screen.blit(gold_anzeige, (0, 100))
  return gold_anzeige, screen