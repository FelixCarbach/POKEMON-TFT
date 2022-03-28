#HEAD
import pygame
import sys
from random import randint
from funktionen import *
from farben import *
from pokemon import *
from musik import *

font = pygame.font.get_fonts()



pygame.init()
events = pygame.event.get()
clock = pygame.time.Clock()


'EINFÜGEN VON DINGEN'


'Einfügen der Arena'

draw_spielfeld(arena)

draw_shop(arena)
draw_shopg(arena)


pygame.mixer.music.load("musik/chill.mp3")

'Screen-Einstellungen'
screen = pygame.display.set_mode((1500, 800))

'''font1 = pygame.font.SysFont('freesans', 72)
img1 = font1.render('gold', True, gelb)'''


mx, my = pygame.mouse.get_pos()

'Große While-Schleife'
while True:
  'print(pygame.mouse.get_pos())'
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  screen.blit(arena, (arena_x, arena_y))   

  screen.blit(reroll, (reroll_x, reroll_y))
  screen.blit(rerollg, (reroll_xg, reroll_yg))

  #screen.blit(img1, (500, 500))

  "Chill-Musik"
  
  pygame.mixer.music.play(-1,0.0)
  pygame.mixer.music.set_volume(1)

  'Darstellen der Pokemon'    


  
  'Shop-Slot 1'
  serpifeu_shop1, serpifeu_shop_x1, serpifeu_shop_y1, eins, eins, fünf, screen, shop_slot_1_rar, shop_slot_1_var_common = show_Pokemon1(serpifeu_shop1, serpifeu_shop_x1, serpifeu_shop_y1, eins, eins, fünf, screen, shop_slot_1_rar, shop_slot_1_var_common)

  floink_shop1, floink_shop_x1, floink_shop_y1, zwei, eins, fünf, screen, shop_slot_1_rar, shop_slot_1_var_common = show_Pokemon1(floink_shop1, floink_shop_x1, floink_shop_y1, zwei, eins, fünf, screen, shop_slot_1_rar, shop_slot_1_var_common)

  ottaro_shop1, ottaro_shop_x1, ottaro_shop_y1, drei, eins, fünf, screen, shop_slot_1_rar, shop_slot_1_var_common = show_Pokemon1(ottaro_shop1, ottaro_shop_x1, ottaro_shop_y1, drei, eins, fünf, screen, shop_slot_1_rar, shop_slot_1_var_common)

  strawickl_shop1, strawickl_shop_x1, strawickl_shop_y1, eins, fünf, acht, screen, shop_slot_1_rar, shop_slot_1_var_uncommon = show_Pokemon1(strawickl_shop1, strawickl_shop_x1, strawickl_shop_y1, eins, fünf, acht, screen, shop_slot_1_rar, shop_slot_1_var_uncommon)

  toxiped_shop1, toxiped_shop_x1, toxiped_shop_y1, zwei, fünf, acht, screen, shop_slot_1_rar, shop_slot_1_var_uncommon = show_Pokemon1(toxiped_shop1, toxiped_shop_x1, toxiped_shop_y1, zwei, fünf, acht, screen, shop_slot_1_rar, shop_slot_1_var_uncommon)

  praktibalk_shop1, praktibalk_shop_x1, praktibalk_shop_y1, drei, fünf, acht, screen, shop_slot_1_rar, shop_slot_1_var_uncommon = show_Pokemon1(praktibalk_shop1, praktibalk_shop_x1, praktibalk_shop_y1, drei, fünf, acht, screen, shop_slot_1_rar, shop_slot_1_var_uncommon)

  klikk_shop1, klikk_shop_x1, klikk_shop_y1, eins, acht, zehn, screen, shop_slot_1_rar, shop_slot_1_var_rare = show_Pokemon1(klikk_shop1, klikk_shop_x1, klikk_shop_y1, eins, acht, zehn, screen, shop_slot_1_rar, shop_slot_1_var_rare)

  kiesling_shop1, kiesling_shop_x1, kiesling_shop_y1, zwei, acht, zehn, screen, shop_slot_1_rar, shop_slot_1_var_rare = show_Pokemon1(kiesling_shop1, kiesling_shop_x1, kiesling_shop_y1, zwei, acht, zehn, screen, shop_slot_1_rar, shop_slot_1_var_rare)

  milza_shop1, milza_shop_x1, milza_shop_y1, drei, acht, zehn, screen, shop_slot_1_rar, shop_slot_1_var_rare = show_Pokemon1(milza_shop1, milza_shop_x1, milza_shop_y1, drei, acht, zehn, screen, shop_slot_1_rar, shop_slot_1_var_rare)

  ganovil_shop1, ganovil_shop_x1, ganovil_shop_y1, eins, zehn, elf, screen, shop_slot_1_rar, shop_slot_1_var_epic = show_Pokemon1(ganovil_shop1, ganovil_shop_x1, ganovil_shop_y1, eins, zehn, elf, screen, shop_slot_1_rar, shop_slot_1_var_epic)

  rotomurf_shop1, rotomurf_shop_x1, rotomurf_shop_y1, zwei, zehn, elf, screen, shop_slot_1_rar, shop_slot_1_var_epic = show_Pokemon1(rotomurf_shop1, rotomurf_shop_x1, rotomurf_shop_y1, zwei, zehn, elf, screen, shop_slot_1_rar, shop_slot_1_var_epic)

  makabaja_shop1, makabaja_shop_x1, makabaja_shop_y1, drei, zehn, elf, screen, shop_slot_1_rar, shop_slot_1_var_epic = show_Pokemon1(makabaja_shop1, makabaja_shop_x1, makabaja_shop_y1, drei, zehn, elf, screen, shop_slot_1_rar, shop_slot_1_var_epic)

  'Shop-Slot 2'
  serpifeu_shop2, serpifeu_shop_x2, serpifeu_shop_y2, eins, eins, fünf, screen, shop_slot_2_rar, shop_slot_2_var_common = show_Pokemon2(serpifeu_shop2, serpifeu_shop_x2, serpifeu_shop_y2, eins, eins, fünf, screen, shop_slot_2_rar, shop_slot_2_var_common)

  floink_shop2, floink_shop_x2, floink_shop_y2, zwei, eins, fünf, screen, shop_slot_2_rar, shop_slot_2_var_common = show_Pokemon2(floink_shop2, floink_shop_x2, floink_shop_y2, zwei, eins, fünf, screen, shop_slot_2_rar, shop_slot_2_var_common)

  ottaro_shop2, ottaro_shop_x2, ottaro_shop_y2, drei, eins, fünf, screen, shop_slot_2_rar, shop_slot_2_var_common = show_Pokemon2(ottaro_shop2, ottaro_shop_x2, ottaro_shop_y2, drei, eins, fünf, screen, shop_slot_2_rar, shop_slot_2_var_common)

  strawickl_shop2, strawickl_shop_x2, strawickl_shop_y2, eins, fünf, acht, screen, shop_slot_2_rar, shop_slot_2_var_uncommon = show_Pokemon2(strawickl_shop2, strawickl_shop_x2, strawickl_shop_y2, eins, fünf, acht, screen, shop_slot_2_rar, shop_slot_2_var_uncommon)

  toxiped_shop2, toxiped_shop_x2, toxiped_shop_y2, zwei, fünf, acht, screen, shop_slot_2_rar, shop_slot_2_var_uncommon = show_Pokemon2(toxiped_shop2, toxiped_shop_x2, toxiped_shop_y2, zwei, fünf, acht, screen, shop_slot_2_rar, shop_slot_2_var_uncommon)

  praktibalk_shop2, praktibalk_shop_x2, praktibalk_shop_y2, drei, fünf, acht, screen, shop_slot_2_rar, shop_slot_2_var_uncommon = show_Pokemon2(praktibalk_shop2, praktibalk_shop_x2, praktibalk_shop_y2, drei, fünf, acht, screen, shop_slot_2_rar, shop_slot_2_var_uncommon)

  klikk_shop2, klikk_shop_x2, klikk_shop_y2, eins, acht, zehn, screen, shop_slot_2_rar, shop_slot_2_var_rare = show_Pokemon2(klikk_shop2, klikk_shop_x2, klikk_shop_y2, eins, acht, zehn, screen, shop_slot_2_rar, shop_slot_2_var_rare)

  kiesling_shop2, kiesling_shop_x2, kiesling_shop_y2, zwei, acht, zehn, screen, shop_slot_2_rar, shop_slot_2_var_rare = show_Pokemon2(kiesling_shop2, kiesling_shop_x2, kiesling_shop_y2, zwei, acht, zehn, screen, shop_slot_2_rar, shop_slot_2_var_rare)

  milza_shop2, milza_shop_x2, milza_shop_y2, drei, acht, zehn, screen, shop_slot_2_rar, shop_slot_2_var_rare = show_Pokemon2(milza_shop2, milza_shop_x2, milza_shop_y2, drei, acht, zehn, screen, shop_slot_2_rar, shop_slot_2_var_rare)

  ganovil_shop2, ganovil_shop_x2, ganovil_shop_y2, eins, zehn, elf, screen, shop_slot_2_rar, shop_slot_2_var_epic = show_Pokemon2(ganovil_shop2, ganovil_shop_x2, ganovil_shop_y2, eins, zehn, elf, screen, shop_slot_2_rar, shop_slot_2_var_epic)

  rotomurf_shop2, rotomurf_shop_x2, rotomurf_shop_y2, zwei, zehn, elf, screen, shop_slot_2_rar, shop_slot_2_var_epic = show_Pokemon2(rotomurf_shop2, rotomurf_shop_x2, rotomurf_shop_y2, zwei, zehn, elf, screen, shop_slot_2_rar, shop_slot_2_var_epic)

  makabaja_shop2, makabaja_shop_x2, makabaja_shop_y2, drei, zehn, elf, screen, shop_slot_2_rar, shop_slot_2_var_epic = show_Pokemon2(makabaja_shop2, makabaja_shop_x2, makabaja_shop_y2, drei, zehn, elf, screen, shop_slot_2_rar, shop_slot_2_var_epic)

  'Shop-Slot 3'
  serpifeu_shop3, serpifeu_shop_x3, serpifeu_shop_y3, eins, eins, fünf, screen, shop_slot_3_rar, shop_slot_3_var_common = show_Pokemon3(serpifeu_shop3, serpifeu_shop_x3, serpifeu_shop_y3, eins, eins, fünf, screen, shop_slot_3_rar, shop_slot_3_var_common)

  floink_shop3, floink_shop_x3, floink_shop_y3, zwei, eins, fünf, screen, shop_slot_3_rar, shop_slot_3_var_common = show_Pokemon3(floink_shop3, floink_shop_x3, floink_shop_y3, zwei, eins, fünf, screen, shop_slot_3_rar, shop_slot_3_var_common)

  ottaro_shop3, ottaro_shop_x3, ottaro_shop_y3, drei, eins, fünf, screen, shop_slot_3_rar, shop_slot_3_var_common = show_Pokemon3(ottaro_shop3, ottaro_shop_x3, ottaro_shop_y3, drei, eins, fünf, screen, shop_slot_3_rar, shop_slot_3_var_common)

  strawickl_shop3, strawickl_shop_x3, strawickl_shop_y3, eins, fünf, acht, screen, shop_slot_3_rar, shop_slot_3_var_uncommon = show_Pokemon3(strawickl_shop3, strawickl_shop_x3, strawickl_shop_y3, eins, fünf, acht, screen, shop_slot_3_rar, shop_slot_3_var_uncommon)

  toxiped_shop3, toxiped_shop_x3, toxiped_shop_y3, zwei, fünf, acht, screen, shop_slot_3_rar, shop_slot_3_var_uncommon = show_Pokemon3(toxiped_shop3, toxiped_shop_x3, toxiped_shop_y3, zwei, fünf, acht, screen, shop_slot_3_rar, shop_slot_3_var_uncommon)

  praktibalk_shop3, praktibalk_shop_x3, praktibalk_shop_y3, drei, fünf, acht, screen, shop_slot_3_rar, shop_slot_3_var_uncommon = show_Pokemon3(praktibalk_shop3, praktibalk_shop_x3, praktibalk_shop_y3, drei, fünf, acht, screen, shop_slot_3_rar, shop_slot_3_var_uncommon)

  klikk_shop3, klikk_shop_x3, klikk_shop_y3, eins, acht, zehn, screen, shop_slot_3_rar, shop_slot_3_var_rare = show_Pokemon3(klikk_shop3, klikk_shop_x3, klikk_shop_y3, eins, acht, zehn, screen, shop_slot_3_rar, shop_slot_3_var_rare)

  kiesling_shop3, kiesling_shop_x3, kiesling_shop_y3, zwei, acht, zehn, screen, shop_slot_3_rar, shop_slot_3_var_rare = show_Pokemon3(kiesling_shop3, kiesling_shop_x3, kiesling_shop_y3, zwei, acht, zehn, screen, shop_slot_3_rar, shop_slot_3_var_rare)

  milza_shop3, milza_shop_x3, milza_shop_y3, drei, acht, zehn, screen, shop_slot_3_rar, shop_slot_3_var_rare = show_Pokemon3(milza_shop3, milza_shop_x3, milza_shop_y3, drei, acht, zehn, screen, shop_slot_3_rar, shop_slot_3_var_rare)

  ganovil_shop3, ganovil_shop_x3, ganovil_shop_y3, eins, zehn, elf, screen, shop_slot_3_rar, shop_slot_3_var_epic = show_Pokemon3(ganovil_shop3, ganovil_shop_x3, ganovil_shop_y3, eins, zehn, elf, screen, shop_slot_3_rar, shop_slot_3_var_epic)

  rotomurf_shop3, rotomurf_shop_x3, rotomurf_shop_y3, zwei, zehn, elf, screen, shop_slot_3_rar, shop_slot_3_var_epic = show_Pokemon3(rotomurf_shop3, rotomurf_shop_x3, rotomurf_shop_y3, zwei, zehn, elf, screen, shop_slot_3_rar, shop_slot_3_var_epic)

  makabaja_shop3, makabaja_shop_x3, makabaja_shop_y3, drei, zehn, elf, screen, shop_slot_3_rar, shop_slot_3_var_epic = show_Pokemon3(makabaja_shop3, makabaja_shop_x3, makabaja_shop_y3, drei, zehn, elf, screen, shop_slot_3_rar, shop_slot_3_var_epic)

  'Shop-Slot 4'
  serpifeu_shop4, serpifeu_shop_x4, serpifeu_shop_y4, eins, eins, fünf, screen, shop_slot_4_rar, shop_slot_4_var_common = show_Pokemon4(serpifeu_shop4, serpifeu_shop_x4, serpifeu_shop_y4, eins, eins, fünf, screen, shop_slot_4_rar, shop_slot_4_var_common)

  floink_shop4, floink_shop_x4, floink_shop_y4, zwei, eins, fünf, screen, shop_slot_4_rar, shop_slot_4_var_common = show_Pokemon4(floink_shop4, floink_shop_x4, floink_shop_y4, zwei, eins, fünf, screen, shop_slot_4_rar, shop_slot_4_var_common)

  ottaro_shop4, ottaro_shop_x4, ottaro_shop_y4, drei, eins, fünf, screen, shop_slot_4_rar, shop_slot_4_var_common = show_Pokemon4(ottaro_shop4, ottaro_shop_x4, ottaro_shop_y4, drei, eins, fünf, screen, shop_slot_4_rar, shop_slot_4_var_common)

  strawickl_shop4, strawickl_shop_x4, strawickl_shop_y4, eins, fünf, acht, screen, shop_slot_4_rar, shop_slot_4_var_uncommon = show_Pokemon4(strawickl_shop4, strawickl_shop_x4, strawickl_shop_y4, eins, fünf, acht, screen, shop_slot_4_rar, shop_slot_4_var_uncommon)

  toxiped_shop4, toxiped_shop_x4, toxiped_shop_y4, zwei, fünf, acht, screen, shop_slot_4_rar, shop_slot_4_var_uncommon = show_Pokemon4(toxiped_shop4, toxiped_shop_x4, toxiped_shop_y4, zwei, fünf, acht, screen, shop_slot_4_rar, shop_slot_4_var_uncommon)

  praktibalk_shop4, praktibalk_shop_x4, praktibalk_shop_y4, drei, fünf, acht, screen, shop_slot_4_rar, shop_slot_4_var_uncommon = show_Pokemon4(praktibalk_shop4, praktibalk_shop_x4, praktibalk_shop_y4, drei, fünf, acht, screen, shop_slot_4_rar, shop_slot_4_var_uncommon)

  klikk_shop4, klikk_shop_x4, klikk_shop_y4, eins, acht, zehn, screen, shop_slot_4_rar, shop_slot_4_var_rare = show_Pokemon4(klikk_shop4, klikk_shop_x4, klikk_shop_y4, eins, acht, zehn, screen, shop_slot_4_rar, shop_slot_4_var_rare)

  kiesling_shop4, kiesling_shop_x4, kiesling_shop_y4, zwei, acht, zehn, screen, shop_slot_4_rar, shop_slot_4_var_rare = show_Pokemon4(kiesling_shop4, kiesling_shop_x4, kiesling_shop_y4, zwei, acht, zehn, screen, shop_slot_4_rar, shop_slot_4_var_rare)

  milza_shop4, milza_shop_x4, milza_shop_y4, drei, acht, zehn, screen, shop_slot_4_rar, shop_slot_4_var_rare = show_Pokemon4(milza_shop4, milza_shop_x4, milza_shop_y4, drei, acht, zehn, screen, shop_slot_4_rar, shop_slot_4_var_rare)

  ganovil_shop4, ganovil_shop_x4, ganovil_shop_y4, eins, zehn, elf, screen, shop_slot_4_rar, shop_slot_4_var_epic = show_Pokemon4(ganovil_shop4, ganovil_shop_x4, ganovil_shop_y4, eins, zehn, elf, screen, shop_slot_4_rar, shop_slot_4_var_epic)

  rotomurf_shop4, rotomurf_shop_x4, rotomurf_shop_y4, zwei, zehn, elf, screen, shop_slot_4_rar, shop_slot_4_var_epic = show_Pokemon4(rotomurf_shop4, rotomurf_shop_x4, rotomurf_shop_y4, zwei, zehn, elf, screen, shop_slot_4_rar, shop_slot_4_var_epic)

  makabaja_shop4, makabaja_shop_x4, makabaja_shop_y4, drei, zehn, elf, screen, shop_slot_4_rar, shop_slot_4_var_epic = show_Pokemon4(makabaja_shop4, makabaja_shop_x4, makabaja_shop_y4, drei, zehn, elf, screen, shop_slot_4_rar, shop_slot_4_var_epic)

  'Shop-Slot 5'
  serpifeu_shop5, serpifeu_shop_x5, serpifeu_shop_y5, eins, eins, fünf, screen, shop_slot_5_rar, shop_slot_5_var_common = show_Pokemon5(serpifeu_shop5, serpifeu_shop_x5, serpifeu_shop_y5, eins, eins, fünf, screen, shop_slot_5_rar, shop_slot_5_var_common)

  floink_shop5, floink_shop_x5, floink_shop_y5, zwei, eins, fünf, screen, shop_slot_5_rar, shop_slot_5_var_common = show_Pokemon5(floink_shop5, floink_shop_x5, floink_shop_y5, zwei, eins, fünf, screen, shop_slot_5_rar, shop_slot_5_var_common)

  ottaro_shop5, ottaro_shop_x5, ottaro_shop_y5, drei, eins, fünf, screen, shop_slot_5_rar, shop_slot_5_var_common = show_Pokemon5(ottaro_shop5, ottaro_shop_x5, ottaro_shop_y5, drei, eins, fünf, screen, shop_slot_5_rar, shop_slot_5_var_common)

  strawickl_shop5, strawickl_shop_x5, strawickl_shop_y5, eins, fünf, acht, screen, shop_slot_5_rar, shop_slot_5_var_uncommon = show_Pokemon5(strawickl_shop5, strawickl_shop_x5, strawickl_shop_y5, eins, fünf, acht, screen, shop_slot_5_rar, shop_slot_5_var_uncommon)

  toxiped_shop5, toxiped_shop_x5, toxiped_shop_y5, zwei, fünf, acht, screen, shop_slot_5_rar, shop_slot_5_var_uncommon = show_Pokemon5(toxiped_shop5, toxiped_shop_x5, toxiped_shop_y5, zwei, fünf, acht, screen, shop_slot_5_rar, shop_slot_5_var_uncommon)

  praktibalk_shop5, praktibalk_shop_x5, praktibalk_shop_y5, drei, fünf, acht, screen, shop_slot_5_rar, shop_slot_5_var_uncommon = show_Pokemon5(praktibalk_shop5, praktibalk_shop_x5, praktibalk_shop_y5, drei, fünf, acht, screen, shop_slot_5_rar, shop_slot_5_var_uncommon)

  klikk_shop5, klikk_shop_x5, klikk_shop_y5, eins, acht, zehn, screen, shop_slot_5_rar, shop_slot_5_var_rare = show_Pokemon5(klikk_shop5, klikk_shop_x5, klikk_shop_y5, eins, acht, zehn, screen, shop_slot_5_rar, shop_slot_5_var_rare)

  kiesling_shop5, kiesling_shop_x5, kiesling_shop_y5, zwei, acht, zehn, screen, shop_slot_5_rar, shop_slot_5_var_rare = show_Pokemon5(kiesling_shop5, kiesling_shop_x5, kiesling_shop_y5, zwei, acht, zehn, screen, shop_slot_5_rar, shop_slot_5_var_rare)

  milza_shop5, milza_shop_x5, milza_shop_y5, drei, acht, zehn, screen, shop_slot_5_rar, shop_slot_5_var_rare = show_Pokemon5(milza_shop5, milza_shop_x5, milza_shop_y5, drei, acht, zehn, screen, shop_slot_5_rar, shop_slot_5_var_rare)

  ganovil_shop5, ganovil_shop_x5, ganovil_shop_y5, eins, zehn, elf, screen, shop_slot_5_rar, shop_slot_5_var_epic = show_Pokemon5(ganovil_shop5, ganovil_shop_x5, ganovil_shop_y5, eins, zehn, elf, screen, shop_slot_5_rar, shop_slot_5_var_epic)

  rotomurf_shop5, rotomurf_shop_x5, rotomurf_shop_y5, zwei, zehn, elf, screen, shop_slot_5_rar, shop_slot_5_var_epic = show_Pokemon5(rotomurf_shop5, rotomurf_shop_x5, rotomurf_shop_y5, zwei, zehn, elf, screen, shop_slot_5_rar, shop_slot_5_var_epic)

  makabaja_shop5, makabaja_shop_x5, makabaja_shop_y5, drei, zehn, elf, screen, shop_slot_5_rar, shop_slot_5_var_epic = show_Pokemon5(makabaja_shop5, makabaja_shop_x5, makabaja_shop_y5, drei, zehn, elf, screen, shop_slot_5_rar, shop_slot_5_var_epic)
  
  'Spawnen der Pokemon'

  'Shop-Slot 1'  

  Spawning_serpifeu1, Spawning_serpifeu2, Spawning_serpifeu3, Spawning_serpiroyal1, serpifeu_x1, serpifeu_y1, serpifeu1, serpifeu_x2, serpifeu_y2, serpifeu2, serpifeu_x3, serpifeu_y3, serpifeu3, eins, eins, fünf, eins1, screen, shop_slot_1_var_common, shop_slot_1_rar, gold = spawn_Pokemon1_common(Spawning_serpifeu1, Spawning_serpifeu2, Spawning_serpifeu3, Spawning_serpiroyal1, serpifeu_x1, serpifeu_y1, serpifeu1, serpifeu_x2, serpifeu_y2, serpifeu2, serpifeu_x3, serpifeu_y3, serpifeu3, eins, eins, fünf, eins1, screen, shop_slot_1_var_common, shop_slot_1_rar, gold)

  Spawning_floink1, Spawning_floink2, Spawning_floink3, Spawning_flambirex1, floink_x1, floink_y1, floink1, floink_x2, floink_y2, floink2, floink_x3, floink_y3, floink3, zwei, eins, fünf, eins1, screen, shop_slot_1_var_common, shop_slot_1_rar, gold= spawn_Pokemon1_common(Spawning_floink1, Spawning_floink2, Spawning_floink3, Spawning_flambirex1, floink_x1, floink_y1, floink1, floink_x2, floink_y2, floink2, floink_x3, floink_y3, floink3, zwei, eins, fünf, eins1, screen, shop_slot_1_var_common, shop_slot_1_rar, gold)

  Spawning_ottaro1, Spawning_ottaro2, Spawning_ottaro3, Spawning_admurai1, ottaro_x1, ottaro_y1, ottaro1, ottaro_x2, ottaro_y2, ottaro2, ottaro_x3, ottaro_y3, ottaro3, drei, eins, fünf, eins1, screen, shop_slot_1_var_common, shop_slot_1_rar, gold= spawn_Pokemon1_common(Spawning_ottaro1, Spawning_ottaro2, Spawning_ottaro3, Spawning_admurai1, ottaro_x1, ottaro_y1, ottaro1, ottaro_x2, ottaro_y2, ottaro2, ottaro_x3, ottaro_y3, ottaro3, drei, eins, fünf, eins1, screen, shop_slot_1_var_common, shop_slot_1_rar, gold)

  Spawning_strawickl1, Spawning_strawickl2, Spawning_strawickl3, Spawning_matrifol1, strawickl_x1, strawickl_y1, strawickl1, strawickl_x2, strawickl_y2, strawickl2, strawickl_x3, strawickl_y3, strawickl3, eins, fünf, acht, zwei2, screen, shop_slot_1_var_uncommon, shop_slot_1_rar, gold = spawn_Pokemon1_common(Spawning_strawickl1, Spawning_strawickl2, Spawning_strawickl3, Spawning_matrifol1, strawickl_x1, strawickl_y1, strawickl1, strawickl_x2, strawickl_y2, strawickl2, strawickl_x3, strawickl_y3, strawickl3, eins, fünf, acht, zwei2, screen, shop_slot_1_var_uncommon, shop_slot_1_rar, gold)

  Spawning_toxiped1, Spawning_toxiped2, Spawning_toxiped3, Spawning_cerapendra1, toxiped_x1, toxiped_y1, toxiped1, toxiped_x2, toxiped_y2, toxiped2, toxiped_x3, toxiped_y3, toxiped3, zwei, fünf, acht, zwei2, screen, shop_slot_1_var_uncommon, shop_slot_1_rar, gold = spawn_Pokemon1_common(Spawning_toxiped1, Spawning_toxiped2, Spawning_toxiped3, Spawning_cerapendra1, toxiped_x1, toxiped_y1, toxiped1, toxiped_x2, toxiped_y2, toxiped2, toxiped_x3, toxiped_y3, toxiped3, zwei, fünf, acht, zwei2, screen, shop_slot_1_var_uncommon, shop_slot_1_rar, gold)

  Spawning_praktibalk1, Spawning_praktibalk2, Spawning_praktibalk3, Spawning_meistagrif1, praktibalk_x1, praktibalk_y1, praktibalk1, praktibalk_x2, praktibalk_y2, praktibalk2, praktibalk_x3, praktibalk_y3, praktibalk3, drei, fünf, acht, zwei2, screen, shop_slot_1_var_uncommon, shop_slot_1_rar, gold = spawn_Pokemon1_common(Spawning_praktibalk1, Spawning_praktibalk2, Spawning_praktibalk3, Spawning_meistagrif1, praktibalk_x1, praktibalk_y1, praktibalk1, praktibalk_x2, praktibalk_y2, praktibalk2, praktibalk_x3, praktibalk_y3, praktibalk3, drei, fünf, acht, zwei2, screen, shop_slot_1_var_uncommon, shop_slot_1_rar, gold)

  Spawning_klikk1, Spawning_klikk2, Spawning_klikk3, Spawning_klikdiklak1, klikk_x1, klikk_y1, klikk1, klikk_x2, klikk_y2, klikk2, klikk_x3, klikk_y3, klikk3, eins, acht, zehn, drei3, screen, shop_slot_1_var_rare, shop_slot_1_rar, gold = spawn_Pokemon1_common(Spawning_klikk1, Spawning_klikk2, Spawning_klikk3, Spawning_klikdiklak1, klikk_x1, klikk_y1, klikk1, klikk_x2, klikk_y2, klikk2, klikk_x3, klikk_y3, klikk3, eins, acht, zehn, drei3, screen, shop_slot_1_var_rare, shop_slot_1_rar, gold)

  Spawning_kiesling1, Spawning_kiesling2, Spawning_kiesling3, Spawning_brokkolos1, kiesling_x1, kiesling_y1, kiesling1, kiesling_x2, kiesling_y2, kiesling2, kiesling_x3, kiesling_y3, kiesling3, zwei, acht, zehn, drei3, screen, shop_slot_1_var_rare, shop_slot_1_rar, gold = spawn_Pokemon1_common(Spawning_kiesling1, Spawning_kiesling2, Spawning_kiesling3, Spawning_brokkolos1, kiesling_x1, kiesling_y1, kiesling1, kiesling_x2, kiesling_y2, kiesling2, kiesling_x3, kiesling_y3, kiesling3, zwei, acht, zehn, drei3, screen, shop_slot_1_var_rare, shop_slot_1_rar, gold)

  Spawning_milza1, Spawning_milza2, Spawning_milza3, Spawning_maxax1, milza_x1, milza_y1, milza1, milza_x2, milza_y2, milza2, milza_x3, milza_y3, milza3, drei, acht, zehn, drei3, screen, shop_slot_1_var_rare, shop_slot_1_rar, gold = spawn_Pokemon1_common(Spawning_milza1, Spawning_milza2, Spawning_milza3, Spawning_maxax1, milza_x1, milza_y1, milza1, milza_x2, milza_y2, milza2, milza_x3, milza_y3, milza3, drei, acht, zehn, drei3, screen, shop_slot_1_var_rare, shop_slot_1_rar, gold)

  Spawning_ganovil1, Spawning_ganovil2, Spawning_ganovil3, Spawning_rabigator1, ganovil_x1, ganovil_y1, ganovil1, ganovil_x2, ganovil_y2, ganovil2, ganovil_x3, ganovil_y3, ganovil3, eins, zehn, elf, vier4, screen, shop_slot_1_var_epic, shop_slot_1_rar, gold = spawn_Pokemon1_common(Spawning_ganovil1, Spawning_ganovil2, Spawning_ganovil3, Spawning_rabigator1, ganovil_x1, ganovil_y1, ganovil1, ganovil_x2, ganovil_y2, ganovil2, ganovil_x3, ganovil_y3, ganovil3, eins, zehn, elf, vier4, screen, shop_slot_1_var_epic, shop_slot_1_rar, gold)

  Spawning_rotomurf1, Spawning_rotomurf2, Spawning_rotomurf3, Spawning_stalobor21, rotomurf_x1, rotomurf_y1, rotomurf1, rotomurf_x2, rotomurf_y2, rotomurf2, rotomurf_x3, rotomurf_y3, rotomurf3, zwei, zehn, elf, vier4, screen, shop_slot_1_var_epic, shop_slot_1_rar, gold = spawn_Pokemon1_common(Spawning_rotomurf1, Spawning_rotomurf2, Spawning_rotomurf3, Spawning_stalobor21, rotomurf_x1, rotomurf_y1, rotomurf1, rotomurf_x2, rotomurf_y2, rotomurf2, rotomurf_x3, rotomurf_y3, rotomurf3, zwei, zehn, elf, vier4, screen, shop_slot_1_var_epic, shop_slot_1_rar, gold)

  Spawning_makabaja1, Spawning_makabaja2, Spawning_makabaja3, Spawning_echnatoll21, makabaja_x1, makabaja_y1, makabaja1, makabaja_x2, makabaja_y2, makabaja2, makabaja_x3, makabaja_y3, makabaja3, drei, zehn, elf, vier4, screen, shop_slot_1_var_epic, shop_slot_1_rar, gold = spawn_Pokemon1_common(Spawning_makabaja1, Spawning_makabaja2, Spawning_makabaja3, Spawning_echnatoll21, makabaja_x1, makabaja_y1, makabaja1, makabaja_x2, makabaja_y2, makabaja2, makabaja_x3, makabaja_y3, makabaja3, drei, zehn, elf, vier4, screen, shop_slot_1_var_epic, shop_slot_1_rar, gold)

  'Shop-Slot 2'

  Spawning_serpifeu1, Spawning_serpifeu2, Spawning_serpifeu3, Spawning_serpiroyal1, serpifeu_x1, serpifeu_y1, serpifeu1, serpifeu_x2, serpifeu_y2, serpifeu2, serpifeu_x3, serpifeu_y3, serpifeu3, eins, eins, fünf, eins1, screen, shop_slot_2_var_common, shop_slot_2_rar, gold = spawn_Pokemon2_common(Spawning_serpifeu1, Spawning_serpifeu2, Spawning_serpifeu3, Spawning_serpiroyal1, serpifeu_x1, serpifeu_y1, serpifeu1, serpifeu_x2, serpifeu_y2, serpifeu2, serpifeu_x3, serpifeu_y3, serpifeu3, eins, eins, fünf, eins1, screen, shop_slot_2_var_common, shop_slot_2_rar, gold)

  Spawning_floink1, Spawning_floink2, Spawning_floink3, Spawning_flambirex1, floink_x1, floink_y1, floink1, floink_x2, floink_y2, floink2, floink_x3, floink_y3, floink3, zwei, eins, fünf, eins1, screen, shop_slot_2_var_common, shop_slot_2_rar, gold= spawn_Pokemon2_common(Spawning_floink1, Spawning_floink2, Spawning_floink3, Spawning_flambirex1, floink_x1, floink_y1, floink1, floink_x2, floink_y2, floink2, floink_x3, floink_y3, floink3, zwei, eins, fünf, eins1, screen, shop_slot_2_var_common, shop_slot_2_rar, gold)

  Spawning_ottaro1, Spawning_ottaro2, Spawning_ottaro3, Spawning_admurai1, ottaro_x1, ottaro_y1, ottaro1, ottaro_x2, ottaro_y2, ottaro2, ottaro_x3, ottaro_y3, ottaro3, drei, eins, fünf, eins1, screen, shop_slot_2_var_common, shop_slot_2_rar, gold= spawn_Pokemon2_common(Spawning_ottaro1, Spawning_ottaro2, Spawning_ottaro3, Spawning_admurai1, ottaro_x1, ottaro_y1, ottaro1, ottaro_x2, ottaro_y2, ottaro2, ottaro_x3, ottaro_y3, ottaro3, drei, eins, fünf, eins1, screen, shop_slot_2_var_common, shop_slot_2_rar, gold)

  Spawning_strawickl1, Spawning_strawickl2, Spawning_strawickl3, Spawning_matrifol1, strawickl_x1, strawickl_y1, strawickl1, strawickl_x2, strawickl_y2, strawickl2, strawickl_x3, strawickl_y3, strawickl3, eins, fünf, acht, zwei2, screen, shop_slot_2_var_uncommon, shop_slot_2_rar, gold = spawn_Pokemon2_common(Spawning_strawickl1, Spawning_strawickl2, Spawning_strawickl3, Spawning_matrifol1, strawickl_x1, strawickl_y1, strawickl1, strawickl_x2, strawickl_y2, strawickl2, strawickl_x3, strawickl_y3, strawickl3, eins, fünf, acht, zwei2, screen, shop_slot_2_var_uncommon, shop_slot_2_rar, gold)

  Spawning_toxiped1, Spawning_toxiped2, Spawning_toxiped3, Spawning_cerapendra1, toxiped_x1, toxiped_y1, toxiped1, toxiped_x2, toxiped_y2, toxiped2, toxiped_x3, toxiped_y3, toxiped3, zwei, fünf, acht, zwei2, screen, shop_slot_2_var_uncommon, shop_slot_2_rar, gold = spawn_Pokemon2_common(Spawning_toxiped1, Spawning_toxiped2, Spawning_toxiped3, Spawning_cerapendra1, toxiped_x1, toxiped_y1, toxiped1, toxiped_x2, toxiped_y2, toxiped2, toxiped_x3, toxiped_y3, toxiped3, zwei, fünf, acht, zwei2, screen, shop_slot_2_var_uncommon, shop_slot_2_rar, gold)

  Spawning_praktibalk1, Spawning_praktibalk2, Spawning_praktibalk3, Spawning_meistagrif1, praktibalk_x1, praktibalk_y1, praktibalk1, praktibalk_x2, praktibalk_y2, praktibalk2, praktibalk_x3, praktibalk_y3, praktibalk3, drei, fünf, acht, zwei2, screen, shop_slot_2_var_uncommon, shop_slot_2_rar, gold = spawn_Pokemon2_common(Spawning_praktibalk1, Spawning_praktibalk2, Spawning_praktibalk3, Spawning_meistagrif1, praktibalk_x1, praktibalk_y1, praktibalk1, praktibalk_x2, praktibalk_y2, praktibalk2, praktibalk_x3, praktibalk_y3, praktibalk3, drei, fünf, acht, zwei2, screen, shop_slot_2_var_uncommon, shop_slot_2_rar, gold)

  Spawning_klikk1, Spawning_klikk2, Spawning_klikk3, Spawning_klikdiklak1, klikk_x1, klikk_y1, klikk1, klikk_x2, klikk_y2, klikk2, klikk_x3, klikk_y3, klikk3, eins, acht, zehn, drei3, screen, shop_slot_2_var_rare, shop_slot_2_rar, gold = spawn_Pokemon2_common(Spawning_klikk1, Spawning_klikk2, Spawning_klikk3, Spawning_klikdiklak1, klikk_x1, klikk_y1, klikk1, klikk_x2, klikk_y2, klikk2, klikk_x3, klikk_y3, klikk3, eins, acht, zehn, drei3, screen, shop_slot_2_var_rare, shop_slot_2_rar, gold)

  Spawning_kiesling1, Spawning_kiesling2, Spawning_kiesling3, Spawning_brokkolos1, kiesling_x1, kiesling_y1, kiesling1, kiesling_x2, kiesling_y2, kiesling2, kiesling_x3, kiesling_y3, kiesling3, zwei, acht, zehn, drei3, screen, shop_slot_2_var_rare, shop_slot_2_rar, gold = spawn_Pokemon2_common(Spawning_kiesling1, Spawning_kiesling2, Spawning_kiesling3, Spawning_brokkolos1, kiesling_x1, kiesling_y1, kiesling1, kiesling_x2, kiesling_y2, kiesling2, kiesling_x3, kiesling_y3, kiesling3, zwei, acht, zehn, drei3, screen, shop_slot_2_var_rare, shop_slot_2_rar, gold)

  Spawning_milza1, Spawning_milza2, Spawning_milza3, Spawning_maxax1, milza_x1, milza_y1, milza1, milza_x2, milza_y2, milza2, milza_x3, milza_y3, milza3, drei, acht, zehn, drei3, screen, shop_slot_2_var_rare, shop_slot_2_rar, gold = spawn_Pokemon2_common(Spawning_milza1, Spawning_milza2, Spawning_milza3, Spawning_maxax1, milza_x1, milza_y1, milza1, milza_x2, milza_y2, milza2, milza_x3, milza_y3, milza3, drei, acht, zehn, drei3, screen, shop_slot_2_var_rare, shop_slot_2_rar, gold)

  Spawning_ganovil1, Spawning_ganovil2, Spawning_ganovil3, Spawning_rabigator1, ganovil_x1, ganovil_y1, ganovil1, ganovil_x2, ganovil_y2, ganovil2, ganovil_x3, ganovil_y3, ganovil3, eins, zehn, elf, vier4, screen, shop_slot_2_var_epic, shop_slot_2_rar, gold = spawn_Pokemon2_common(Spawning_ganovil1, Spawning_ganovil2, Spawning_ganovil3, Spawning_rabigator1, ganovil_x1, ganovil_y1, ganovil1, ganovil_x2, ganovil_y2, ganovil2, ganovil_x3, ganovil_y3, ganovil3, eins, zehn, elf, vier4, screen, shop_slot_2_var_epic, shop_slot_2_rar, gold)

  Spawning_rotomurf1, Spawning_rotomurf2, Spawning_rotomurf3, Spawning_stalobor21, rotomurf_x1, rotomurf_y1, rotomurf1, rotomurf_x2, rotomurf_y2, rotomurf2, rotomurf_x3, rotomurf_y3, rotomurf3, zwei, zehn, elf, vier4, screen, shop_slot_2_var_epic, shop_slot_2_rar, gold = spawn_Pokemon2_common(Spawning_rotomurf1, Spawning_rotomurf2, Spawning_rotomurf3, Spawning_stalobor21, rotomurf_x1, rotomurf_y1, rotomurf1, rotomurf_x2, rotomurf_y2, rotomurf2, rotomurf_x3, rotomurf_y3, rotomurf3, zwei, zehn, elf, vier4, screen, shop_slot_2_var_epic, shop_slot_2_rar, gold)

  Spawning_makabaja1, Spawning_makabaja2, Spawning_makabaja3, Spawning_echnatoll21, makabaja_x1, makabaja_y1, makabaja1, makabaja_x2, makabaja_y2, makabaja2, makabaja_x3, makabaja_y3, makabaja3, drei, zehn, elf, vier4, screen, shop_slot_2_var_epic, shop_slot_2_rar, gold = spawn_Pokemon2_common(Spawning_makabaja1, Spawning_makabaja2, Spawning_makabaja3, Spawning_echnatoll21, makabaja_x1, makabaja_y1, makabaja1, makabaja_x2, makabaja_y2, makabaja2, makabaja_x3, makabaja_y3, makabaja3, drei, zehn, elf, vier4, screen, shop_slot_2_var_epic, shop_slot_2_rar, gold)

  'Shop-Slot 3'

  Spawning_serpifeu1, Spawning_serpifeu2, Spawning_serpifeu3, Spawning_serpiroyal1, serpifeu_x1, serpifeu_y1, serpifeu1, serpifeu_x2, serpifeu_y2, serpifeu2, serpifeu_x3, serpifeu_y3, serpifeu3, eins, eins, fünf, eins1, screen, shop_slot_3_var_common, shop_slot_3_rar, gold = spawn_Pokemon3_common(Spawning_serpifeu1, Spawning_serpifeu2, Spawning_serpifeu3, Spawning_serpiroyal1, serpifeu_x1, serpifeu_y1, serpifeu1, serpifeu_x2, serpifeu_y2, serpifeu2, serpifeu_x3, serpifeu_y3, serpifeu3, eins, eins, fünf, eins1, screen, shop_slot_3_var_common, shop_slot_3_rar, gold)

  Spawning_floink1, Spawning_floink2, Spawning_floink3, Spawning_flambirex1, floink_x1, floink_y1, floink1, floink_x2, floink_y2, floink2, floink_x3, floink_y3, floink3, zwei, eins, fünf, eins1, screen, shop_slot_3_var_common, shop_slot_3_rar, gold= spawn_Pokemon3_common(Spawning_floink1, Spawning_floink2, Spawning_floink3, Spawning_flambirex1, floink_x1, floink_y1, floink1, floink_x2, floink_y2, floink2, floink_x3, floink_y3, floink3, zwei, eins, fünf, eins1, screen, shop_slot_3_var_common, shop_slot_3_rar, gold)

  Spawning_ottaro1, Spawning_ottaro2, Spawning_ottaro3, Spawning_admurai1, ottaro_x1, ottaro_y1, ottaro1, ottaro_x2, ottaro_y2, ottaro2, ottaro_x3, ottaro_y3, ottaro3, drei, eins, fünf, eins1, screen, shop_slot_3_var_common, shop_slot_3_rar, gold= spawn_Pokemon3_common(Spawning_ottaro1, Spawning_ottaro2, Spawning_ottaro3, Spawning_admurai1, ottaro_x1, ottaro_y1, ottaro1, ottaro_x2, ottaro_y2, ottaro2, ottaro_x3, ottaro_y3, ottaro3, drei, eins, fünf, eins1, screen, shop_slot_3_var_common, shop_slot_3_rar, gold)

  Spawning_strawickl1, Spawning_strawickl2, Spawning_strawickl3, Spawning_matrifol1, strawickl_x1, strawickl_y1, strawickl1, strawickl_x2, strawickl_y2, strawickl2, strawickl_x3, strawickl_y3, strawickl3, eins, fünf, acht, zwei2, screen, shop_slot_3_var_uncommon, shop_slot_3_rar, gold = spawn_Pokemon3_common(Spawning_strawickl1, Spawning_strawickl2, Spawning_strawickl3, Spawning_matrifol1, strawickl_x1, strawickl_y1, strawickl1, strawickl_x2, strawickl_y2, strawickl2, strawickl_x3, strawickl_y3, strawickl3, eins, fünf, acht, zwei2, screen, shop_slot_3_var_uncommon, shop_slot_3_rar, gold)

  Spawning_toxiped1, Spawning_toxiped2, Spawning_toxiped3, Spawning_cerapendra1, toxiped_x1, toxiped_y1, toxiped1, toxiped_x2, toxiped_y2, toxiped2, toxiped_x3, toxiped_y3, toxiped3, zwei, fünf, acht, zwei2, screen, shop_slot_3_var_uncommon, shop_slot_3_rar, gold = spawn_Pokemon3_common(Spawning_toxiped1, Spawning_toxiped2, Spawning_toxiped3, Spawning_cerapendra1, toxiped_x1, toxiped_y1, toxiped1, toxiped_x2, toxiped_y2, toxiped2, toxiped_x3, toxiped_y3, toxiped3, zwei, fünf, acht, zwei2, screen, shop_slot_3_var_uncommon, shop_slot_3_rar, gold)

  Spawning_praktibalk1, Spawning_praktibalk2, Spawning_praktibalk3, Spawning_meistagrif1, praktibalk_x1, praktibalk_y1, praktibalk1, praktibalk_x2, praktibalk_y2, praktibalk2, praktibalk_x3, praktibalk_y3, praktibalk3, drei, fünf, acht, zwei2, screen, shop_slot_3_var_uncommon, shop_slot_3_rar, gold = spawn_Pokemon3_common(Spawning_praktibalk1, Spawning_praktibalk2, Spawning_praktibalk3, Spawning_meistagrif1, praktibalk_x1, praktibalk_y1, praktibalk1, praktibalk_x2, praktibalk_y2, praktibalk2, praktibalk_x3, praktibalk_y3, praktibalk3, drei, fünf, acht, zwei2, screen, shop_slot_3_var_uncommon, shop_slot_3_rar, gold)

  Spawning_klikk1, Spawning_klikk2, Spawning_klikk3, Spawning_klikdiklak1, klikk_x1, klikk_y1, klikk1, klikk_x2, klikk_y2, klikk2, klikk_x3, klikk_y3, klikk3, eins, acht, zehn, drei3, screen, shop_slot_3_var_rare, shop_slot_3_rar, gold = spawn_Pokemon3_common(Spawning_klikk1, Spawning_klikk2, Spawning_klikk3, Spawning_klikdiklak1, klikk_x1, klikk_y1, klikk1, klikk_x2, klikk_y2, klikk2, klikk_x3, klikk_y3, klikk3, eins, acht, zehn, drei3, screen, shop_slot_3_var_rare, shop_slot_3_rar, gold)

  Spawning_kiesling1, Spawning_kiesling2, Spawning_kiesling3, Spawning_brokkolos1, kiesling_x1, kiesling_y1, kiesling1, kiesling_x2, kiesling_y2, kiesling2, kiesling_x3, kiesling_y3, kiesling3, zwei, acht, zehn, drei3, screen, shop_slot_3_var_rare, shop_slot_3_rar, gold = spawn_Pokemon3_common(Spawning_kiesling1, Spawning_kiesling2, Spawning_kiesling3, Spawning_brokkolos1, kiesling_x1, kiesling_y1, kiesling1, kiesling_x2, kiesling_y2, kiesling2, kiesling_x3, kiesling_y3, kiesling3, zwei, acht, zehn, drei3, screen, shop_slot_3_var_rare, shop_slot_3_rar, gold)

  Spawning_milza1, Spawning_milza2, Spawning_milza3, Spawning_maxax1, milza_x1, milza_y1, milza1, milza_x2, milza_y2, milza2, milza_x3, milza_y3, milza3, drei, acht, zehn, drei3, screen, shop_slot_3_var_rare, shop_slot_3_rar, gold = spawn_Pokemon3_common(Spawning_milza1, Spawning_milza2, Spawning_milza3, Spawning_maxax1, milza_x1, milza_y1, milza1, milza_x2, milza_y2, milza2, milza_x3, milza_y3, milza3, drei, acht, zehn, drei3, screen, shop_slot_3_var_rare, shop_slot_3_rar, gold)

  Spawning_ganovil1, Spawning_ganovil2, Spawning_ganovil3, Spawning_rabigator1, ganovil_x1, ganovil_y1, ganovil1, ganovil_x2, ganovil_y2, ganovil2, ganovil_x3, ganovil_y3, ganovil3, eins, zehn, elf, vier4, screen, shop_slot_3_var_epic, shop_slot_3_rar, gold = spawn_Pokemon3_common(Spawning_ganovil1, Spawning_ganovil2, Spawning_ganovil3, Spawning_rabigator1, ganovil_x1, ganovil_y1, ganovil1, ganovil_x2, ganovil_y2, ganovil2, ganovil_x3, ganovil_y3, ganovil3, eins, zehn, elf, vier4, screen, shop_slot_3_var_epic, shop_slot_3_rar, gold)

  Spawning_rotomurf1, Spawning_rotomurf2, Spawning_rotomurf3, Spawning_stalobor21, rotomurf_x1, rotomurf_y1, rotomurf1, rotomurf_x2, rotomurf_y2, rotomurf2, rotomurf_x3, rotomurf_y3, rotomurf3, zwei, zehn, elf, vier4, screen, shop_slot_3_var_epic, shop_slot_3_rar, gold = spawn_Pokemon3_common(Spawning_rotomurf1, Spawning_rotomurf2, Spawning_rotomurf3, Spawning_stalobor21, rotomurf_x1, rotomurf_y1, rotomurf1, rotomurf_x2, rotomurf_y2, rotomurf2, rotomurf_x3, rotomurf_y3, rotomurf3, zwei, zehn, elf, vier4, screen, shop_slot_3_var_epic, shop_slot_3_rar, gold)

  Spawning_makabaja1, Spawning_makabaja2, Spawning_makabaja3, Spawning_echnatoll21, makabaja_x1, makabaja_y1, makabaja1, makabaja_x2, makabaja_y2, makabaja2, makabaja_x3, makabaja_y3, makabaja3, drei, zehn, elf, vier4, screen, shop_slot_3_var_epic, shop_slot_3_rar, gold = spawn_Pokemon3_common(Spawning_makabaja1, Spawning_makabaja2, Spawning_makabaja3, Spawning_echnatoll21, makabaja_x1, makabaja_y1, makabaja1, makabaja_x2, makabaja_y2, makabaja2, makabaja_x3, makabaja_y3, makabaja3, drei, zehn, elf, vier4, screen, shop_slot_3_var_epic, shop_slot_3_rar, gold)

  'Shop-Slot 4'

  Spawning_serpifeu1, Spawning_serpifeu2, Spawning_serpifeu3, Spawning_serpiroyal1, serpifeu_x1, serpifeu_y1, serpifeu1, serpifeu_x2, serpifeu_y2, serpifeu2, serpifeu_x3, serpifeu_y3, serpifeu3, eins, eins, fünf, eins1, screen, shop_slot_4_var_common, shop_slot_4_rar, gold = spawn_Pokemon4_common(Spawning_serpifeu1, Spawning_serpifeu2, Spawning_serpifeu3, Spawning_serpiroyal1, serpifeu_x1, serpifeu_y1, serpifeu1, serpifeu_x2, serpifeu_y2, serpifeu2, serpifeu_x3, serpifeu_y3, serpifeu3, eins, eins, fünf, eins1, screen, shop_slot_4_var_common, shop_slot_4_rar, gold)

  Spawning_floink1, Spawning_floink2, Spawning_floink3, Spawning_flambirex1, floink_x1, floink_y1, floink1, floink_x2, floink_y2, floink2, floink_x3, floink_y3, floink3, zwei, eins, fünf, eins1, screen, shop_slot_4_var_common, shop_slot_4_rar, gold= spawn_Pokemon4_common(Spawning_floink1, Spawning_floink2, Spawning_floink3, Spawning_flambirex1, floink_x1, floink_y1, floink1, floink_x2, floink_y2, floink2, floink_x3, floink_y3, floink3, zwei, eins, fünf, eins1, screen, shop_slot_4_var_common, shop_slot_4_rar, gold)

  Spawning_ottaro1, Spawning_ottaro2, Spawning_ottaro3, Spawning_admurai1, ottaro_x1, ottaro_y1, ottaro1, ottaro_x2, ottaro_y2, ottaro2, ottaro_x3, ottaro_y3, ottaro3, drei, eins, fünf, eins1, screen, shop_slot_4_var_common, shop_slot_4_rar, gold= spawn_Pokemon4_common(Spawning_ottaro1, Spawning_ottaro2, Spawning_ottaro3, Spawning_admurai1, ottaro_x1, ottaro_y1, ottaro1, ottaro_x2, ottaro_y2, ottaro2, ottaro_x3, ottaro_y3, ottaro3, drei, eins, fünf, eins1, screen, shop_slot_4_var_common, shop_slot_4_rar, gold)

  Spawning_strawickl1, Spawning_strawickl2, Spawning_strawickl3, Spawning_matrifol1, strawickl_x1, strawickl_y1, strawickl1, strawickl_x2, strawickl_y2, strawickl2, strawickl_x3, strawickl_y3, strawickl3, eins, fünf, acht, zwei2, screen, shop_slot_4_var_uncommon, shop_slot_4_rar, gold = spawn_Pokemon4_common(Spawning_strawickl1, Spawning_strawickl2, Spawning_strawickl3, Spawning_matrifol1, strawickl_x1, strawickl_y1, strawickl1, strawickl_x2, strawickl_y2, strawickl2, strawickl_x3, strawickl_y3, strawickl3, eins, fünf, acht, zwei2, screen, shop_slot_4_var_uncommon, shop_slot_4_rar, gold)
  

  Spawning_toxiped1, Spawning_toxiped2, Spawning_toxiped3, Spawning_cerapendra1, toxiped_x1, toxiped_y1, toxiped1, toxiped_x2, toxiped_y2, toxiped2, toxiped_x3, toxiped_y3, toxiped3, zwei, fünf, acht, zwei2, screen, shop_slot_4_var_uncommon, shop_slot_4_rar, gold = spawn_Pokemon4_common(Spawning_toxiped1, Spawning_toxiped2, Spawning_toxiped3, Spawning_cerapendra1, toxiped_x1, toxiped_y1, toxiped1, toxiped_x2, toxiped_y2, toxiped2, toxiped_x3, toxiped_y3, toxiped3, zwei, fünf, acht, zwei2, screen, shop_slot_4_var_uncommon, shop_slot_4_rar, gold)

  Spawning_praktibalk1, Spawning_praktibalk2, Spawning_praktibalk3, Spawning_meistagrif1, praktibalk_x1, praktibalk_y1, praktibalk1, praktibalk_x2, praktibalk_y2, praktibalk2, praktibalk_x3, praktibalk_y3, praktibalk3, drei, fünf, acht, zwei2, screen, shop_slot_4_var_uncommon, shop_slot_4_rar, gold = spawn_Pokemon4_common(Spawning_praktibalk1, Spawning_praktibalk2, Spawning_praktibalk3, Spawning_meistagrif1, praktibalk_x1, praktibalk_y1, praktibalk1, praktibalk_x2, praktibalk_y2, praktibalk2, praktibalk_x3, praktibalk_y3, praktibalk3, drei, fünf, acht, zwei2, screen, shop_slot_4_var_uncommon, shop_slot_4_rar, gold)

  Spawning_klikk1, Spawning_klikk2, Spawning_klikk3, Spawning_klikdiklak1, klikk_x1, klikk_y1, klikk1, klikk_x2, klikk_y2, klikk2, klikk_x3, klikk_y3, klikk3, eins, acht, zehn, drei3, screen, shop_slot_4_var_rare, shop_slot_4_rar, gold = spawn_Pokemon4_common(Spawning_klikk1, Spawning_klikk2, Spawning_klikk3, Spawning_klikdiklak1, klikk_x1, klikk_y1, klikk1, klikk_x2, klikk_y2, klikk2, klikk_x3, klikk_y3, klikk3, eins, acht, zehn, drei3, screen, shop_slot_4_var_rare, shop_slot_4_rar, gold)

  Spawning_kiesling1, Spawning_kiesling2, Spawning_kiesling3, Spawning_brokkolos1, kiesling_x1, kiesling_y1, kiesling1, kiesling_x2, kiesling_y2, kiesling2, kiesling_x3, kiesling_y3, kiesling3, zwei, acht, zehn, drei3, screen, shop_slot_4_var_rare, shop_slot_4_rar, gold = spawn_Pokemon4_common(Spawning_kiesling1, Spawning_kiesling2, Spawning_kiesling3, Spawning_brokkolos1, kiesling_x1, kiesling_y1, kiesling1, kiesling_x2, kiesling_y2, kiesling2, kiesling_x3, kiesling_y3, kiesling3, zwei, acht, zehn, drei3, screen, shop_slot_4_var_rare, shop_slot_4_rar, gold)

  Spawning_milza1, Spawning_milza2, Spawning_milza3, Spawning_maxax1, milza_x1, milza_y1, milza1, milza_x2, milza_y2, milza2, milza_x3, milza_y3, milza3, drei, acht, zehn, drei3, screen, shop_slot_4_var_rare, shop_slot_4_rar, gold = spawn_Pokemon4_common(Spawning_milza1, Spawning_milza2, Spawning_milza3, Spawning_maxax1, milza_x1, milza_y1, milza1, milza_x2, milza_y2, milza2, milza_x3, milza_y3, milza3, drei, acht, zehn, drei3, screen, shop_slot_4_var_rare, shop_slot_4_rar, gold)

  Spawning_ganovil1, Spawning_ganovil2, Spawning_ganovil3, Spawning_rabigator1, ganovil_x1, ganovil_y1, ganovil1, ganovil_x2, ganovil_y2, ganovil2, ganovil_x3, ganovil_y3, ganovil3, eins, zehn, elf, vier4, screen, shop_slot_4_var_epic, shop_slot_4_rar, gold = spawn_Pokemon4_common(Spawning_ganovil1, Spawning_ganovil2, Spawning_ganovil3, Spawning_rabigator1, ganovil_x1, ganovil_y1, ganovil1, ganovil_x2, ganovil_y2, ganovil2, ganovil_x3, ganovil_y3, ganovil3, eins, zehn, elf, vier4, screen, shop_slot_4_var_epic, shop_slot_4_rar, gold)

  Spawning_rotomurf1, Spawning_rotomurf2, Spawning_rotomurf3, Spawning_stalobor21, rotomurf_x1, rotomurf_y1, rotomurf1, rotomurf_x2, rotomurf_y2, rotomurf2, rotomurf_x3, rotomurf_y3, rotomurf3, zwei, zehn, elf, vier4, screen, shop_slot_4_var_epic, shop_slot_4_rar, gold = spawn_Pokemon4_common(Spawning_rotomurf1, Spawning_rotomurf2, Spawning_rotomurf3, Spawning_stalobor21, rotomurf_x1, rotomurf_y1, rotomurf1, rotomurf_x2, rotomurf_y2, rotomurf2, rotomurf_x3, rotomurf_y3, rotomurf3, zwei, zehn, elf, vier4, screen, shop_slot_4_var_epic, shop_slot_4_rar, gold)

  Spawning_makabaja1, Spawning_makabaja2, Spawning_makabaja3, Spawning_echnatoll21, makabaja_x1, makabaja_y1, makabaja1, makabaja_x2, makabaja_y2, makabaja2, makabaja_x3, makabaja_y3, makabaja3, drei, zehn, elf, vier4, screen, shop_slot_4_var_epic, shop_slot_4_rar, gold = spawn_Pokemon4_common(Spawning_makabaja1, Spawning_makabaja2, Spawning_makabaja3, Spawning_echnatoll21, makabaja_x1, makabaja_y1, makabaja1, makabaja_x2, makabaja_y2, makabaja2, makabaja_x3, makabaja_y3, makabaja3, drei, zehn, elf, vier4, screen, shop_slot_4_var_epic, shop_slot_4_rar, gold)

  'Shop-Slot 5'    

  Spawning_serpifeu1, Spawning_serpifeu2, Spawning_serpifeu3, Spawning_serpiroyal1, serpifeu_x1, serpifeu_y1, serpifeu1, serpifeu_x2, serpifeu_y2, serpifeu2, serpifeu_x3, serpifeu_y3, serpifeu3, eins, eins, fünf, eins1, screen, shop_slot_5_var_common, shop_slot_5_rar, gold = spawn_Pokemon5_common(Spawning_serpifeu1, Spawning_serpifeu2, Spawning_serpifeu3, Spawning_serpiroyal1, serpifeu_x1, serpifeu_y1, serpifeu1, serpifeu_x2, serpifeu_y2, serpifeu2, serpifeu_x3, serpifeu_y3, serpifeu3, eins, eins, fünf, eins1, screen, shop_slot_5_var_common, shop_slot_5_rar, gold)

  Spawning_floink1, Spawning_floink2, Spawning_floink3, Spawning_flambirex1, floink_x1, floink_y1, floink1, floink_x2, floink_y2, floink2, floink_x3, floink_y3, floink3, zwei, eins, fünf, eins1, screen, shop_slot_5_var_common, shop_slot_5_rar, gold= spawn_Pokemon5_common(Spawning_floink1, Spawning_floink2, Spawning_floink3, Spawning_flambirex1, floink_x1, floink_y1, floink1, floink_x2, floink_y2, floink2, floink_x3, floink_y3, floink3, zwei, eins, fünf, eins1, screen, shop_slot_5_var_common, shop_slot_5_rar, gold)

  Spawning_ottaro1, Spawning_ottaro2, Spawning_ottaro3, Spawning_admurai1, ottaro_x1, ottaro_y1, ottaro1, ottaro_x2, ottaro_y2, ottaro2, ottaro_x3, ottaro_y3, ottaro3, drei, eins, fünf, eins1, screen, shop_slot_5_var_common, shop_slot_5_rar, gold= spawn_Pokemon5_common(Spawning_ottaro1, Spawning_ottaro2, Spawning_ottaro3, Spawning_admurai1, ottaro_x1, ottaro_y1, ottaro1, ottaro_x2, ottaro_y2, ottaro2, ottaro_x3, ottaro_y3, ottaro3, drei, eins, fünf, eins1, screen, shop_slot_5_var_common, shop_slot_5_rar, gold)

  Spawning_strawickl1, Spawning_strawickl2, Spawning_strawickl3, Spawning_matrifol1, strawickl_x1, strawickl_y1, strawickl1, strawickl_x2, strawickl_y2, strawickl2, strawickl_x3, strawickl_y3, strawickl3, eins, fünf, acht, zwei2, screen, shop_slot_5_var_uncommon, shop_slot_5_rar, gold = spawn_Pokemon5_common(Spawning_strawickl1, Spawning_strawickl2, Spawning_strawickl3, Spawning_matrifol1, strawickl_x1, strawickl_y1, strawickl1, strawickl_x2, strawickl_y2, strawickl2, strawickl_x3, strawickl_y3, strawickl3, eins, fünf, acht, zwei2, screen, shop_slot_5_var_uncommon, shop_slot_5_rar, gold)

  Spawning_toxiped1, Spawning_toxiped2, Spawning_toxiped3, Spawning_cerapendra1, toxiped_x1, toxiped_y1, toxiped1, toxiped_x2, toxiped_y2, toxiped2, toxiped_x3, toxiped_y3, toxiped3, zwei, fünf, acht, zwei2, screen, shop_slot_5_var_uncommon, shop_slot_5_rar, gold = spawn_Pokemon5_common(Spawning_toxiped1, Spawning_toxiped2, Spawning_toxiped3, Spawning_cerapendra1, toxiped_x1, toxiped_y1, toxiped1, toxiped_x2, toxiped_y2, toxiped2, toxiped_x3, toxiped_y3, toxiped3, zwei, fünf, acht, zwei2, screen, shop_slot_5_var_uncommon, shop_slot_5_rar, gold)

  Spawning_praktibalk1, Spawning_praktibalk2, Spawning_praktibalk3, Spawning_meistagrif1, praktibalk_x1, praktibalk_y1, praktibalk1, praktibalk_x2, praktibalk_y2, praktibalk2, praktibalk_x3, praktibalk_y3, praktibalk3, drei, fünf, acht, zwei2, screen, shop_slot_5_var_uncommon, shop_slot_5_rar, gold = spawn_Pokemon5_common(Spawning_praktibalk1, Spawning_praktibalk2, Spawning_praktibalk3, Spawning_meistagrif1, praktibalk_x1, praktibalk_y1, praktibalk1, praktibalk_x2, praktibalk_y2, praktibalk2, praktibalk_x3, praktibalk_y3, praktibalk3, drei, fünf, acht, zwei2, screen, shop_slot_5_var_uncommon, shop_slot_5_rar, gold)

  Spawning_klikk1, Spawning_klikk2, Spawning_klikk3, Spawning_klikdiklak1, klikk_x1, klikk_y1, klikk1, klikk_x2, klikk_y2, klikk2, klikk_x3, klikk_y3, klikk3, eins, acht, zehn, drei3, screen, shop_slot_5_var_rare, shop_slot_5_rar, gold = spawn_Pokemon5_common(Spawning_klikk1, Spawning_klikk2, Spawning_klikk3, Spawning_klikdiklak1, klikk_x1, klikk_y1, klikk1, klikk_x2, klikk_y2, klikk2, klikk_x3, klikk_y3, klikk3, eins, acht, zehn, drei3, screen, shop_slot_5_var_rare, shop_slot_5_rar, gold)

  Spawning_kiesling1, Spawning_kiesling2, Spawning_kiesling3, Spawning_brokkolos1, kiesling_x1, kiesling_y1, kiesling1, kiesling_x2, kiesling_y2, kiesling2, kiesling_x3, kiesling_y3, kiesling3, zwei, acht, zehn, drei3, screen, shop_slot_5_var_rare, shop_slot_5_rar, gold = spawn_Pokemon5_common(Spawning_kiesling1, Spawning_kiesling2, Spawning_kiesling3, Spawning_brokkolos1, kiesling_x1, kiesling_y1, kiesling1, kiesling_x2, kiesling_y2, kiesling2, kiesling_x3, kiesling_y3, kiesling3, zwei, acht, zehn, drei3, screen, shop_slot_5_var_rare, shop_slot_5_rar, gold)

  Spawning_milza1, Spawning_milza2, Spawning_milza3, Spawning_maxax1, milza_x1, milza_y1, milza1, milza_x2, milza_y2, milza2, milza_x3, milza_y3, milza3, drei, acht, zehn, drei3, screen, shop_slot_5_var_rare, shop_slot_5_rar, gold = spawn_Pokemon5_common(Spawning_milza1, Spawning_milza2, Spawning_milza3, Spawning_maxax1, milza_x1, milza_y1, milza1, milza_x2, milza_y2, milza2, milza_x3, milza_y3, milza3, drei, acht, zehn, drei3, screen, shop_slot_5_var_rare, shop_slot_5_rar, gold)

  Spawning_ganovil1, Spawning_ganovil2, Spawning_ganovil3, Spawning_rabigator1, ganovil_x1, ganovil_y1, ganovil1, ganovil_x2, ganovil_y2, ganovil2, ganovil_x3, ganovil_y3, ganovil3, eins, zehn, elf, vier4, screen, shop_slot_5_var_epic, shop_slot_5_rar, gold = spawn_Pokemon5_common(Spawning_ganovil1, Spawning_ganovil2, Spawning_ganovil3, Spawning_rabigator1, ganovil_x1, ganovil_y1, ganovil1, ganovil_x2, ganovil_y2, ganovil2, ganovil_x3, ganovil_y3, ganovil3, eins, zehn, elf, vier4, screen, shop_slot_5_var_epic, shop_slot_5_rar, gold)

  Spawning_rotomurf1, Spawning_rotomurf2, Spawning_rotomurf3, Spawning_stalobor21, rotomurf_x1, rotomurf_y1, rotomurf1, rotomurf_x2, rotomurf_y2, rotomurf2, rotomurf_x3, rotomurf_y3, rotomurf3, zwei, zehn, elf, vier4, screen, shop_slot_5_var_epic, shop_slot_5_rar, gold = spawn_Pokemon5_common(Spawning_rotomurf1, Spawning_rotomurf2, Spawning_rotomurf3, Spawning_stalobor21, rotomurf_x1, rotomurf_y1, rotomurf1, rotomurf_x2, rotomurf_y2, rotomurf2, rotomurf_x3, rotomurf_y3, rotomurf3, zwei, zehn, elf, vier4, screen, shop_slot_5_var_epic, shop_slot_5_rar, gold)

  Spawning_makabaja1, Spawning_makabaja2, Spawning_makabaja3, Spawning_echnatoll21, makabaja_x1, makabaja_y1, makabaja1, makabaja_x2, makabaja_y2, makabaja2, makabaja_x3, makabaja_y3, makabaja3, drei, zehn, elf, vier4, screen, shop_slot_5_var_epic, shop_slot_5_rar, gold = spawn_Pokemon5_common(Spawning_makabaja1, Spawning_makabaja2, Spawning_makabaja3, Spawning_echnatoll21, makabaja_x1, makabaja_y1, makabaja1, makabaja_x2, makabaja_y2, makabaja2, makabaja_x3, makabaja_y3, makabaja3, drei, zehn, elf, vier4, screen, shop_slot_5_var_epic, shop_slot_5_rar, gold)

  'Bewegen eines Pokemon'

  serpifeu_x1, serpifeu_y1 = move_Pokemon( serpifeu_x1, serpifeu_y1)
  serpifeu_x2, serpifeu_y2 = move_Pokemon( serpifeu_x2, serpifeu_y2)
  serpifeu_x3, serpifeu_y3 = move_Pokemon( serpifeu_x3, serpifeu_y3)
  efoserp_x1, efoserp_y1 = move_Pokemon( efoserp_x1, efoserp_y1)
  efoserp_x2, efoserp_y2 = move_Pokemon( efoserp_x2, efoserp_y2)
  efoserp_x3, efoserp_y3 = move_Pokemon( efoserp_x3, efoserp_y3)
  serpiroyal_x1, serpiroyal_y1 = move_Pokemon( serpiroyal_x1, serpiroyal_y1)

  floink_x1, floink_y1 = move_Pokemon( floink_x1, floink_y1)
  floink_x2, floink_y2 = move_Pokemon( floink_x2, floink_y2)
  floink_x3, floink_y3 = move_Pokemon( floink_x3, floink_y3)
  ferkokel_x1, ferkokel_y1 = move_Pokemon( ferkokel_x1, ferkokel_y1)
  ferkokel_x2, ferkokel_y2 = move_Pokemon( ferkokel_x2, ferkokel_y2)
  ferkokel_x3, ferkokel_y3 = move_Pokemon( ferkokel_x3, ferkokel_y3)
  flambirex_x1, flambirex_y1 = move_Pokemon( flambirex_x1, flambirex_y1)

  ottaro_x1, ottaro_y1 = move_Pokemon(ottaro_x1, ottaro_y1)
  ottaro_x2, ottaro_y2 = move_Pokemon(ottaro_x2, ottaro_y2)
  ottaro_x3, ottaro_y3 = move_Pokemon(ottaro_x3, ottaro_y3)
  zwottronin_x1, zwottronin_y1 = move_Pokemon(zwottronin_x1, zwottronin_y1)
  zwottronin_x2, zwottronin_y2 = move_Pokemon(zwottronin_x2, zwottronin_y2)
  zwottronin_x3, zwottronin_y3 = move_Pokemon(zwottronin_x3, zwottronin_y3)
  admurai_x1, admurai_y1 = move_Pokemon(admurai_x1, admurai_y1)

  strawickl_x1, strawickl_y1 = move_Pokemon(strawickl_x1, strawickl_y1)
  strawickl_x2, strawickl_y2 = move_Pokemon(strawickl_x2, strawickl_y2)
  strawickl_x3, strawickl_y3 = move_Pokemon(strawickl_x3, strawickl_y3)
  folikon_x1, folikon_y1 = move_Pokemon(folikon_x1, folikon_y1)
  folikon_x2, folikon_y2 = move_Pokemon(folikon_x2, folikon_y2)
  folikon_x3, folikon_y3 = move_Pokemon(folikon_x3, folikon_y3)
  matrifol_x1, matrifol_y1 = move_Pokemon(matrifol_x1, matrifol_y1)

  toxiped_x1, toxiped_y1 = move_Pokemon(toxiped_x1, toxiped_y1)
  toxiped_x2, toxiped_y2 = move_Pokemon(toxiped_x2, toxiped_y2)
  toxiped_x3, toxiped_y3 = move_Pokemon(toxiped_x3, toxiped_y3)
  rollum_x1, rollum_y1 = move_Pokemon(rollum_x1, rollum_y1)
  rollum_x2, rollum_y2 = move_Pokemon(rollum_x2, rollum_y2)
  rollum_x3, rollum_y3 = move_Pokemon(rollum_x3, rollum_y3)
  cerapendra_x1, cerapendra_y1 = move_Pokemon(cerapendra_x1, cerapendra_y1)

  praktibalk_x1, praktibalk_y1 = move_Pokemon(praktibalk_x1, praktibalk_y1)
  praktibalk_x2, praktibalk_y2 = move_Pokemon(praktibalk_x2, praktibalk_y2)
  praktibalk_x3, praktibalk_y3 = move_Pokemon(praktibalk_x3, praktibalk_y3)
  strepoli_x1, strepoli_y1 = move_Pokemon(strepoli_x1, strepoli_y1)
  strepoli_x2, strepoli_y2 = move_Pokemon(strepoli_x2, strepoli_y2)
  strepoli_x3, strepoli_y3 = move_Pokemon(strepoli_x3, strepoli_y3)
  meistagrif_x1, meistagrif_y1 = move_Pokemon(meistagrif_x1, meistagrif_y1)

  klikk_x1, klikk_y1 = move_Pokemon(klikk_x1, klikk_y1)
  klikk_x2, klikk_y2 = move_Pokemon(klikk_x2, klikk_y2)
  klikk_x3, klikk_y3 = move_Pokemon(klikk_x3, klikk_y3)
  kliklak_x1, kliklak_y1 = move_Pokemon(kliklak_x1, kliklak_y1)
  kliklak_x2, kliklak_y2 = move_Pokemon(kliklak_x2, kliklak_y2)
  kliklak_x3, kliklak_y3 = move_Pokemon(kliklak_x3, kliklak_y3)
  klikdiklak_x1, klikdiklak_y1 = move_Pokemon(klikdiklak_x1, klikdiklak_y1)

  kiesling_x1, kiesling_y1 = move_Pokemon(kiesling_x1, kiesling_y1)
  kiesling_x2, kiesling_y2 = move_Pokemon(kiesling_x2, kiesling_y2)
  kiesling_x3, kiesling_y3 = move_Pokemon(kiesling_x3, kiesling_y3)
  sedimantur_x1, sedimantur_y1 = move_Pokemon(sedimantur_x1, sedimantur_y1)
  sedimantur_x2, sedimantur_y2 = move_Pokemon(sedimantur_x2, sedimantur_y2)
  sedimantur_x3, sedimantur_y3 = move_Pokemon(sedimantur_x3, sedimantur_y3)
  brokkolos_x1, brokkolos_y1 = move_Pokemon(brokkolos_x1, brokkolos_y1)

  milza_x1, milza_y1 = move_Pokemon(milza_x1, milza_y1)
  milza_x2, milza_y2 = move_Pokemon(milza_x2, milza_y2)
  milza_x3, milza_y3 = move_Pokemon(milza_x3, milza_y3)
  sharfax_x1, sharfax_y1 = move_Pokemon(sharfax_x1, sharfax_y1)
  sharfax_x2, sharfax_y2 = move_Pokemon(sharfax_x2, sharfax_y2)
  sharfax_x3, sharfax_y3 = move_Pokemon(sharfax_x3, sharfax_y3)
  maxax_x1, maxax_y1 = move_Pokemon(maxax_x1, maxax_y1)

  ganovil_x1, ganovil_y1 = move_Pokemon(ganovil_x1, ganovil_y1)
  ganovil_x2, ganovil_y2 = move_Pokemon(ganovil_x2, ganovil_y2)
  ganovil_x3, ganovil_y3 = move_Pokemon(ganovil_x3, ganovil_y3)
  rokkaiman_x1, rokkaiman_y1 = move_Pokemon(rokkaiman_x1, rokkaiman_y1)
  rokkaiman_x2, rokkaiman_y2 = move_Pokemon(rokkaiman_x2, rokkaiman_y2)
  rokkaiman_x3, rokkaiman_y3 = move_Pokemon(rokkaiman_x3, rokkaiman_y3)
  rabigator_x1, rabigator_y1 = move_Pokemon(rabigator_x1, rabigator_y1)

  rotomurf_x1, rotomurf_y1 = move_Pokemon(rotomurf_x1, rotomurf_y1)
  rotomurf_x2, rotomurf_y2 = move_Pokemon(rotomurf_x2, rotomurf_y2)
  rotomurf_x3, rotomurf_y3 = move_Pokemon(rotomurf_x3, rotomurf_y3)
  stalobor_x1, stalobor_y1 = move_Pokemon(stalobor_x1, stalobor_y1)
  stalobor_x2, stalobor_y2 = move_Pokemon(stalobor_x2, stalobor_y2)
  stalobor_x3, stalobor_y3 = move_Pokemon(stalobor_x3, stalobor_y3)
  stalobor2_x1, stalobor2_y1 = move_Pokemon(stalobor2_x1, stalobor2_y1)

  makabaja_x1, makabaja_y1 = move_Pokemon(makabaja_x1, makabaja_y1)
  makabaja_x2, makabaja_y2 = move_Pokemon(makabaja_x2, makabaja_y2)
  makabaja_x3, makabaja_y3 = move_Pokemon(makabaja_x3, makabaja_y3)
  echnatoll_x1, echnatoll_y1 = move_Pokemon(echnatoll_x1, echnatoll_y1)
  echnatoll_x2, echnatoll_y2 = move_Pokemon(echnatoll_x2, echnatoll_y2)
  echnatoll_x3, echnatoll_y3 = move_Pokemon(echnatoll_x3, echnatoll_y3)
  echnatoll2_x1, echnatoll2_y1 = move_Pokemon(echnatoll2_x1, echnatoll2_y1)


  'Droppen eines Pokemon'
  
  serpifeu_x1, serpifeu_y1 = drop_Pokemon_bench(serpifeu_x1, serpifeu_y1)
  serpifeu_x2, serpifeu_y2 = drop_Pokemon_bench(serpifeu_x2, serpifeu_y2)
  serpifeu_x3, serpifeu_y3 = drop_Pokemon_bench(serpifeu_x3, serpifeu_y3)
  efoserp_x1, efoserp_y1 = drop_Pokemon_bench(efoserp_x1, efoserp_y1)
  efoserp_x2, efoserp_y2 = drop_Pokemon_bench(efoserp_x2, efoserp_y2)
  efoserp_x3, efoserp_y3 = drop_Pokemon_bench(efoserp_x3, efoserp_y3)
  serpiroyal_x1, serpiroyal_y1 = drop_Pokemon_bench(serpiroyal_x1, serpiroyal_y1)

  floink_x1, floink_y1 = drop_Pokemon_bench(floink_x1, floink_y1)
  floink_x2, floink_y2 = drop_Pokemon_bench(floink_x2, floink_y2)
  floink_x3, floink_y3 = drop_Pokemon_bench(floink_x3, floink_y3)
  ferkokel_x1, ferkokel_y1 = drop_Pokemon_bench(ferkokel_x1, ferkokel_y1)
  ferkokel_x2, ferkokel_y2 = drop_Pokemon_bench(ferkokel_x2, ferkokel_y2)
  ferkokel_x3, ferkokel_y3 = drop_Pokemon_bench(ferkokel_x3, ferkokel_y3)
  flambirex_x1, flambirex_y1 = drop_Pokemon_bench(flambirex_x1, flambirex_y1)

  ottaro_x1, ottaro_y1 = drop_Pokemon_bench(ottaro_x1, ottaro_y1)
  ottaro_x2, ottaro_y2 = drop_Pokemon_bench(ottaro_x2, ottaro_y2)
  ottaro_x3, ottaro_y3 = drop_Pokemon_bench(ottaro_x3, ottaro_y3)
  zwottronin_x1, zwottronin_y1 = drop_Pokemon_bench(zwottronin_x1, zwottronin_y1)
  zwottronin_x2, zwottronin_y2 = drop_Pokemon_bench(zwottronin_x2, zwottronin_y2)
  zwottronin_x3, zwottronin_y3 = drop_Pokemon_bench(zwottronin_x3, zwottronin_y3)
  admurai_x1, admurai_y1 = drop_Pokemon_bench(admurai_x1, admurai_y1)

  strawickl_x1, strawickl_y1 = drop_Pokemon_bench(strawickl_x1, strawickl_y1)
  strawickl_x2, strawickl_y2 = drop_Pokemon_bench(strawickl_x2, strawickl_y2)
  strawickl_x3, strawickl_y3 = drop_Pokemon_bench(strawickl_x3, strawickl_y3)
  folikon_x1, folikon_y1 = drop_Pokemon_bench(folikon_x1, folikon_y1)
  folikon_x2, folikon_y2 = drop_Pokemon_bench(folikon_x2, folikon_y2)
  folikon_x3, folikon_y3 = drop_Pokemon_bench(folikon_x3, folikon_y3)
  matrifol_x1, matrifol_y1 = drop_Pokemon_bench(matrifol_x1, matrifol_y1)

  toxiped_x1, toxiped_y1 = drop_Pokemon_bench(toxiped_x1, toxiped_y1)
  toxiped_x2, toxiped_y2 = drop_Pokemon_bench(toxiped_x2, toxiped_y2)
  toxiped_x3, toxiped_y3 = drop_Pokemon_bench(toxiped_x3, toxiped_y3)
  rollum_x1, rollum_y1 = drop_Pokemon_bench(rollum_x1, rollum_y1)
  rollum_x2, rollum_y2 = drop_Pokemon_bench(rollum_x2, rollum_y2)
  rollum_x3, rollum_y3 = drop_Pokemon_bench(rollum_x3, rollum_y3)
  cerapendra_x1, cerapendra_y1 = drop_Pokemon_bench(cerapendra_x1, cerapendra_y1)

  praktibalk_x1, praktibalk_y1 = drop_Pokemon_bench(praktibalk_x1, praktibalk_y1)
  praktibalk_x2, praktibalk_y2 = drop_Pokemon_bench(praktibalk_x2, praktibalk_y2)
  praktibalk_x3, praktibalk_y3 = drop_Pokemon_bench(praktibalk_x3, praktibalk_y3)
  strepoli_x1, strepoli_y1 = drop_Pokemon_bench(strepoli_x1, strepoli_y1)
  strepoli_x2, strepoli_y2 = drop_Pokemon_bench(strepoli_x2, strepoli_y2)
  strepoli_x3, strepoli_y3 = drop_Pokemon_bench(strepoli_x3, strepoli_y3)
  meistagrif_x1, meistagrif_y1 = drop_Pokemon_bench(meistagrif_x1, meistagrif_y1)

  klikk_x1, klikk_y1 = drop_Pokemon_bench(klikk_x1, klikk_y1)
  klikk_x2, klikk_y2 = drop_Pokemon_bench(klikk_x2, klikk_y2)
  klikk_x3, klikk_y3 = drop_Pokemon_bench(klikk_x3, klikk_y3)
  kliklak_x1, kliklak_y1 = drop_Pokemon_bench(kliklak_x1, kliklak_y1)
  kliklak_x2, kliklak_y2 = drop_Pokemon_bench(kliklak_x2, kliklak_y2)
  kliklak_x3, kliklak_y3 = drop_Pokemon_bench(kliklak_x3, kliklak_y3)
  klikdiklak_x1, klikdiklak_y1 = drop_Pokemon_bench(klikdiklak_x1, klikdiklak_y1)

  kiesling_x1, kiesling_y1 = drop_Pokemon_bench(kiesling_x1, kiesling_y1)
  kiesling_x2, kiesling_y2 = drop_Pokemon_bench(kiesling_x2, kiesling_y2)
  kiesling_x3, kiesling_y3 = drop_Pokemon_bench(kiesling_x3, kiesling_y3)
  sedimantur_x1, sedimantur_y1 = drop_Pokemon_bench(sedimantur_x1, sedimantur_y1)
  sedimantur_x2, sedimantur_y2 = drop_Pokemon_bench(sedimantur_x2, sedimantur_y2)
  sedimantur_x3, sedimantur_y3 = drop_Pokemon_bench(sedimantur_x3, sedimantur_y3)
  brokkolos_x1, brokkolos_y1 = drop_Pokemon_bench(brokkolos_x1, brokkolos_y1)

  milza_x1, milza_y1 = drop_Pokemon_bench(milza_x1, milza_y1)
  milza_x2, milza_y2 = drop_Pokemon_bench(milza_x2, milza_y2)
  milza_x3, milza_y3 = drop_Pokemon_bench(milza_x3, milza_y3)
  sharfax_x1, sharfax_y1 = drop_Pokemon_bench(sharfax_x1, sharfax_y1)
  sharfax_x2, sharfax_y2 = drop_Pokemon_bench(sharfax_x2, sharfax_y2)
  sharfax_x3, sharfax_y3 = drop_Pokemon_bench(sharfax_x3, sharfax_y3)
  maxax_x1, maxax_y1 = drop_Pokemon_bench(maxax_x1, maxax_y1)

  ganovil_x1, ganovil_y1 = drop_Pokemon_bench(ganovil_x1, ganovil_y1)
  ganovil_x2, ganovil_y2 = drop_Pokemon_bench(ganovil_x2, ganovil_y2)
  ganovil_x3, ganovil_y3 = drop_Pokemon_bench(ganovil_x3, ganovil_y3)
  rokkaiman_x1, rokkaiman_y1 = drop_Pokemon_bench(rokkaiman_x1, rokkaiman_y1)
  rokkaiman_x2, rokkaiman_y2 = drop_Pokemon_bench(rokkaiman_x2, rokkaiman_y2)
  rokkaiman_x3, rokkaiman_y3 = drop_Pokemon_bench(rokkaiman_x3, rokkaiman_y3)
  rabigator_x1, rabigator_y1 = drop_Pokemon_bench(rabigator_x1, rabigator_y1)

  rotomurf_x1, rotomurf_y1 = drop_Pokemon_bench(rotomurf_x1, rotomurf_y1)
  rotomurf_x2, rotomurf_y2 = drop_Pokemon_bench(rotomurf_x2, rotomurf_y2)
  rotomurf_x3, rotomurf_y3 = drop_Pokemon_bench(rotomurf_x3, rotomurf_y3)
  stalobor_x1, stalobor_y1 = drop_Pokemon_bench(stalobor_x1, stalobor_y1)
  stalobor_x2, stalobor_y2 = drop_Pokemon_bench(stalobor_x2, stalobor_y2)
  stalobor_x3, stalobor_y3 = drop_Pokemon_bench(stalobor_x3, stalobor_y3)
  stalobor2_x1, stalobor2_y1 = drop_Pokemon_bench(stalobor2_x1, stalobor2_y1)

  makabaja_x1, makabaja_y1 = drop_Pokemon_bench(makabaja_x1, makabaja_y1)
  makabaja_x2, makabaja_y2 = drop_Pokemon_bench(makabaja_x2, makabaja_y2)
  makabaja_x3, makabaja_y3 = drop_Pokemon_bench(makabaja_x3, makabaja_y3)
  echnatoll_x1, echnatoll_y1 = drop_Pokemon_bench(echnatoll_x1, echnatoll_y1)
  echnatoll_x2, echnatoll_y2 = drop_Pokemon_bench(echnatoll_x2, echnatoll_y2)
  echnatoll_x3, echnatoll_y3 = drop_Pokemon_bench(echnatoll_x3, echnatoll_y3)
  echnatoll2_x1, echnatoll2_y1 = drop_Pokemon_bench(echnatoll2_x1, echnatoll2_y1)
  


  serpifeu_x1, serpifeu_y1 = drop_Pokemon_arena(serpifeu_x1, serpifeu_y1)
  serpifeu_x2, serpifeu_y2 = drop_Pokemon_arena(serpifeu_x2, serpifeu_y2)
  serpifeu_x3, serpifeu_y3 = drop_Pokemon_arena(serpifeu_x3, serpifeu_y3)
  efoserp_x1, efoserp_y1 = drop_Pokemon_arena(efoserp_x1, efoserp_y1)
  efoserp_x2, efoserp_y2 = drop_Pokemon_arena(efoserp_x2, efoserp_y2)
  efoserp_x3, efoserp_y3 = drop_Pokemon_arena(efoserp_x3, efoserp_y3)
  serpiroyal_x1, serpiroyal_y1 = drop_Pokemon_arena(serpiroyal_x1, serpiroyal_y1)

  floink_x1, floink_y1 = drop_Pokemon_arena(floink_x1, floink_y1)
  floink_x2, floink_y2 = drop_Pokemon_arena(floink_x2, floink_y2)
  floink_x3, floink_y3 = drop_Pokemon_arena(floink_x3, floink_y3)
  ferkokel_x1, ferkokel_y1 = drop_Pokemon_arena(ferkokel_x1, ferkokel_y1)
  ferkokel_x2, ferkokel_y2 = drop_Pokemon_arena(ferkokel_x2, ferkokel_y2)
  ferkokel_x3, ferkokel_y3 = drop_Pokemon_arena(ferkokel_x3, ferkokel_y3)
  flambirex_x1, flambirex_y1 = drop_Pokemon_arena(flambirex_x1, flambirex_y1)

  ottaro_x1, ottaro_y1 = drop_Pokemon_arena(ottaro_x1, ottaro_y1)
  ottaro_x2, ottaro_y2 = drop_Pokemon_arena(ottaro_x2, ottaro_y2)
  ottaro_x3, ottaro_y3 = drop_Pokemon_arena(ottaro_x3, ottaro_y3)
  zwottronin_x1, zwottronin_y1 = drop_Pokemon_arena(zwottronin_x1, zwottronin_y1)
  zwottronin_x2, zwottronin_y2 = drop_Pokemon_arena(zwottronin_x2, zwottronin_y2)
  zwottronin_x3, zwottronin_y3 = drop_Pokemon_arena(zwottronin_x3, zwottronin_y3)
  admurai_x1, admurai_y1 = drop_Pokemon_arena(admurai_x1, admurai_y1)

  strawickl_x1, strawickl_y1 = drop_Pokemon_arena(strawickl_x1, strawickl_y1)
  strawickl_x2, strawickl_y2 = drop_Pokemon_arena(strawickl_x2, strawickl_y2)
  strawickl_x3, strawickl_y3 = drop_Pokemon_arena(strawickl_x3, strawickl_y3)
  folikon_x1, folikon_y1 = drop_Pokemon_arena(folikon_x1, folikon_y1)
  folikon_x2, folikon_y2 = drop_Pokemon_arena(folikon_x2, folikon_y2)
  folikon_x3, folikon_y3 = drop_Pokemon_arena(folikon_x3, folikon_y3)
  matrifol_x1, matrifol_y1 = drop_Pokemon_arena(matrifol_x1, matrifol_y1)

  toxiped_x1, toxiped_y1 = drop_Pokemon_arena(toxiped_x1, toxiped_y1)
  toxiped_x2, toxiped_y2 = drop_Pokemon_arena(toxiped_x2, toxiped_y2)
  toxiped_x3, toxiped_y3 = drop_Pokemon_arena(toxiped_x3, toxiped_y3)
  rollum_x1, rollum_y1 = drop_Pokemon_arena(rollum_x1, rollum_y1)
  rollum_x2, rollum_y2 = drop_Pokemon_arena(rollum_x2, rollum_y2)
  rollum_x3, rollum_y3 = drop_Pokemon_arena(rollum_x3, rollum_y3)
  cerapendra_x1, cerapendra_y1 = drop_Pokemon_arena(cerapendra_x1, cerapendra_y1)

  praktibalk_x1, praktibalk_y1 = drop_Pokemon_arena(praktibalk_x1, praktibalk_y1)
  praktibalk_x2, praktibalk_y2 = drop_Pokemon_arena(praktibalk_x2, praktibalk_y2)
  praktibalk_x3, praktibalk_y3 = drop_Pokemon_arena(praktibalk_x3, praktibalk_y3)
  strepoli_x1, strepoli_y1 = drop_Pokemon_arena(strepoli_x1, strepoli_y1)
  strepoli_x2, strepoli_y2 = drop_Pokemon_arena(strepoli_x2, strepoli_y2)
  strepoli_x3, strepoli_y3 = drop_Pokemon_arena(strepoli_x3, strepoli_y3)
  meistagrif_x1, meistagrif_y1 = drop_Pokemon_arena(meistagrif_x1, meistagrif_y1)

  klikk_x1, klikk_y1 = drop_Pokemon_arena(klikk_x1, klikk_y1)
  klikk_x2, klikk_y2 = drop_Pokemon_arena(klikk_x2, klikk_y2)
  klikk_x3, klikk_y3 = drop_Pokemon_arena(klikk_x3, klikk_y3)
  kliklak_x1, kliklak_y1 = drop_Pokemon_arena(kliklak_x1, kliklak_y1)
  kliklak_x2, kliklak_y2 = drop_Pokemon_arena(kliklak_x2, kliklak_y2)
  kliklak_x3, kliklak_y3 = drop_Pokemon_arena(kliklak_x3, kliklak_y3)
  klikdiklak_x1, klikdiklak_y1 = drop_Pokemon_arena(klikdiklak_x1, klikdiklak_y1)

  kiesling_x1, kiesling_y1 = drop_Pokemon_arena(kiesling_x1, kiesling_y1)
  kiesling_x2, kiesling_y2 = drop_Pokemon_arena(kiesling_x2, kiesling_y2)
  kiesling_x3, kiesling_y3 = drop_Pokemon_arena(kiesling_x3, kiesling_y3)
  sedimantur_x1, sedimantur_y1 = drop_Pokemon_arena(sedimantur_x1, sedimantur_y1)
  sedimantur_x2, sedimantur_y2 = drop_Pokemon_arena(sedimantur_x2, sedimantur_y2)
  sedimantur_x3, sedimantur_y3 = drop_Pokemon_arena(sedimantur_x3, sedimantur_y3)
  brokkolos_x1, brokkolos_y1 = drop_Pokemon_arena(brokkolos_x1, brokkolos_y1)

  milza_x1, milza_y1 = drop_Pokemon_arena(milza_x1, milza_y1)
  milza_x2, milza_y2 = drop_Pokemon_arena(milza_x2, milza_y2)
  milza_x3, milza_y3 = drop_Pokemon_arena(milza_x3, milza_y3)
  sharfax_x1, sharfax_y1 = drop_Pokemon_arena(sharfax_x1, sharfax_y1)
  sharfax_x2, sharfax_y2 = drop_Pokemon_arena(sharfax_x2, sharfax_y2)
  sharfax_x3, sharfax_y3 = drop_Pokemon_arena(sharfax_x3, sharfax_y3)
  maxax_x1, maxax_y1 = drop_Pokemon_arena(maxax_x1, maxax_y1)

  ganovil_x1, ganovil_y1 = drop_Pokemon_arena(ganovil_x1, ganovil_y1)
  ganovil_x2, ganovil_y2 = drop_Pokemon_arena(ganovil_x2, ganovil_y2)
  ganovil_x3, ganovil_y3 = drop_Pokemon_arena(ganovil_x3, ganovil_y3)
  rokkaiman_x1, rokkaiman_y1 = drop_Pokemon_arena(rokkaiman_x1, rokkaiman_y1)
  rokkaiman_x2, rokkaiman_y2 = drop_Pokemon_arena(rokkaiman_x2, rokkaiman_y2)
  rokkaiman_x3, rokkaiman_y3 = drop_Pokemon_arena(rokkaiman_x3, rokkaiman_y3)
  rabigator_x1, rabigator_y1 = drop_Pokemon_arena(rabigator_x1, rabigator_y1)

  rotomurf_x1, rotomurf_y1 = drop_Pokemon_arena(rotomurf_x1, rotomurf_y1)
  rotomurf_x2, rotomurf_y2 = drop_Pokemon_arena(rotomurf_x2, rotomurf_y2)
  rotomurf_x3, rotomurf_y3 = drop_Pokemon_arena(rotomurf_x3, rotomurf_y3)
  stalobor_x1, stalobor_y1 = drop_Pokemon_arena(stalobor_x1, stalobor_y1)
  stalobor_x2, stalobor_y2 = drop_Pokemon_arena(stalobor_x2, stalobor_y2)
  stalobor_x3, stalobor_y3 = drop_Pokemon_arena(stalobor_x3, stalobor_y3)
  stalobor2_x1, stalobor2_y1 = drop_Pokemon_arena(stalobor2_x1, stalobor2_y1)

  makabaja_x1, makabaja_y1 = drop_Pokemon_arena(makabaja_x1, makabaja_y1)
  makabaja_x2, makabaja_y2 = drop_Pokemon_arena(makabaja_x2, makabaja_y2)
  makabaja_x3, makabaja_y3 = drop_Pokemon_arena(makabaja_x3, makabaja_y3)
  echnatoll_x1, echnatoll_y1 = drop_Pokemon_arena(echnatoll_x1, echnatoll_y1)
  echnatoll_x2, echnatoll_y2 = drop_Pokemon_arena(echnatoll_x2, echnatoll_y2)
  echnatoll_x3, echnatoll_y3 = drop_Pokemon_arena(echnatoll_x3, echnatoll_y3)
  echnatoll2_x1, echnatoll2_y1 = drop_Pokemon_arena(echnatoll2_x1, echnatoll2_y1)

  'Replacen eines Pokemon'

  serpifeu_x1, serpifeu_y1, serpifeu_x2, serpifeu_y2, serpifeu_x3, serpifeu_y3, efoserp_x1, efoserp_y1, efoserp_x2, efoserp_y2, efoserp_x3, efoserp_y3, serpiroyal_x1, serpiroyal_y1, floink_x1, floink_y1, floink_x2, floink_y2, floink_x3, floink_y3, ferkokel_x1, ferkokel_y1, ferkokel_x2, ferkokel_y2, ferkokel_x3, ferkokel_y3, flambirex_x1, flambirex_y1, ottaro_x1, ottaro_y1, ottaro_x2, ottaro_y2, ottaro_x3, ottaro_y3, zwottronin_x1, zwottronin_y1, zwottronin_x2, zwottronin_y2, zwottronin_x3, zwottronin_y3, admurai_x1, admurai_y1 = replace_Pokemon(serpifeu_x1, serpifeu_y1, serpifeu_x2, serpifeu_y2, serpifeu_x3, serpifeu_y3, efoserp_x1, efoserp_y1, efoserp_x2, efoserp_y2, efoserp_x3, efoserp_y3, serpiroyal_x1, serpiroyal_y1, floink_x1, floink_y1, floink_x2, floink_y2, floink_x3, floink_y3, ferkokel_x1, ferkokel_y1, ferkokel_x2, ferkokel_y2, ferkokel_x3, ferkokel_y3, flambirex_x1, flambirex_y1, ottaro_x1, ottaro_y1, ottaro_x2, ottaro_y2, ottaro_x3, ottaro_y3, zwottronin_x1, zwottronin_y1, zwottronin_x2, zwottronin_y2, zwottronin_x3, zwottronin_y3, admurai_x1, admurai_y1)

  'Entwickeln eines Pokemon'
  
  'Erste Entwicklung'

  Spawning_serpifeu1, Spawning_serpifeu2, Spawning_serpifeu3, Spawning_efoserp1, Spawning_efoserp2, Spawning_efoserp3, Spawning_serpiroyal1, efoserp_x1, efoserp_x2, efoserp_x3, serpifeu_x1, serpifeu_x2, serpifeu_x3, efoserp_y1, efoserp_y2, efoserp_y3, serpifeu_y1, serpifeu_y2, serpifeu_y3, efoserp1, efoserp2, efoserp3, eins, zwei, drei, eins, screen=evolve_Pokemon1(Spawning_serpifeu1, Spawning_serpifeu2, Spawning_serpifeu3, Spawning_efoserp1, Spawning_efoserp2, Spawning_efoserp3, Spawning_serpiroyal1, efoserp_x1, efoserp_x2, efoserp_x3, serpifeu_x1, serpifeu_x2, serpifeu_x3, efoserp_y1, efoserp_y2, efoserp_y3, serpifeu_y1, serpifeu_y2, serpifeu_y3, efoserp1, efoserp2, efoserp3, eins, zwei, drei, eins, screen)

  Spawning_floink1, Spawning_floink2, Spawning_floink3, Spawning_ferkokel1, Spawning_ferkokel2, Spawning_ferkokel3, Spawning_flambirex1, ferkokel_x1, ferkokel_x2, ferkokel_x3, floink_x1, floink_x2, floink_x3, ferkokel_y1, ferkokel_y2, ferkokel_y3, floink_y1, floink_y2, floink_y3, ferkokel1, ferkokel2, ferkokel3, acht, neun, zehn, eins, screen=evolve_Pokemon1(Spawning_floink1, Spawning_floink2, Spawning_floink3, Spawning_ferkokel1, Spawning_ferkokel2, Spawning_ferkokel3, Spawning_flambirex1, ferkokel_x1, ferkokel_x2, ferkokel_x3, floink_x1, floink_x2, floink_x3, ferkokel_y1, ferkokel_y2, ferkokel_y3, floink_y1, floink_y2, floink_y3, ferkokel1, ferkokel2, ferkokel3, acht, neun, zehn, eins, screen) 

  Spawning_ottaro1, Spawning_ottaro2, Spawning_ottaro3, Spawning_zwottronin1, Spawning_zwottronin2, Spawning_zwottronin3, Spawning_admurai1, zwottronin_x1, zwottronin_x2, zwottronin_x3, ottaro_x1, ottaro_x2, ottaro_x3, zwottronin_y1, zwottronin_y2, zwottronin_y3, ottaro_y1, ottaro_y2, ottaro_y3, zwottronin1, zwottronin2, zwottronin3, fünfzehn, sechzehn, siebzehn, eins, screen=evolve_Pokemon1(Spawning_ottaro1, Spawning_ottaro2, Spawning_ottaro3, Spawning_zwottronin1, Spawning_zwottronin2, Spawning_zwottronin3, Spawning_admurai1, zwottronin_x1, zwottronin_x2, zwottronin_x3, ottaro_x1, ottaro_x2, ottaro_x3, zwottronin_y1, zwottronin_y2, zwottronin_y3, ottaro_y1, ottaro_y2, ottaro_y3, zwottronin1, zwottronin2, zwottronin3, fünfzehn, sechzehn, siebzehn, eins, screen)

  Spawning_strawickl1, Spawning_strawickl2, Spawning_strawickl3, Spawning_folikon1, Spawning_folikon2, Spawning_folikon3, Spawning_matrifol1, folikon_x1, folikon_x2, folikon_x3, strawickl_x1, strawickl_x2, strawickl_x3, folikon_y1, folikon_y2, folikon_y3, strawickl_y1, strawickl_y2, strawickl_y3, folikon1, folikon2, folikon3, zweiundzwanzig, dreiundzwanzig, vierundzwanzig, eins, screen=evolve_Pokemon1(Spawning_strawickl1, Spawning_strawickl2, Spawning_strawickl3, Spawning_folikon1, Spawning_folikon2, Spawning_folikon3, Spawning_matrifol1, folikon_x1, folikon_x2, folikon_x3, strawickl_x1, strawickl_x2, strawickl_x3, folikon_y1, folikon_y2, folikon_y3, strawickl_y1, strawickl_y2, strawickl_y3, folikon1, folikon2, folikon3, zweiundzwanzig, dreiundzwanzig, vierundzwanzig, eins, screen)

  Spawning_toxiped1, Spawning_toxiped2, Spawning_toxiped3, Spawning_rollum1, Spawning_rollum2, Spawning_rollum3, Spawning_cerapendra1, rollum_x1, rollum_x2, rollum_x3, toxiped_x1, toxiped_x2, toxiped_x3, rollum_y1, rollum_y2, rollum_y3, toxiped_y1, toxiped_y2, toxiped_y3, rollum1, rollum2, rollum3, neunundzwanzig, dreißig, einunddreißig, eins, screen=evolve_Pokemon1(Spawning_toxiped1, Spawning_toxiped2, Spawning_toxiped3, Spawning_rollum1, Spawning_rollum2, Spawning_rollum3, Spawning_cerapendra1, rollum_x1, rollum_x2, rollum_x3, toxiped_x1, toxiped_x2, toxiped_x3, rollum_y1, rollum_y2, rollum_y3, toxiped_y1, toxiped_y2, toxiped_y3, rollum1, rollum2, rollum3, neunundzwanzig, dreißig, einunddreißig, eins, screen)

  Spawning_praktibalk1, Spawning_praktibalk2, Spawning_praktibalk3, Spawning_strepoli1, Spawning_strepoli2, Spawning_strepoli3, Spawning_meistagrif1, strepoli_x1, strepoli_x2, strepoli_x3, praktibalk_x1, praktibalk_x2, praktibalk_x3, strepoli_y1, strepoli_y2, strepoli_y3, praktibalk_y1, praktibalk_y2, praktibalk_y3, strepoli1, strepoli2, strepoli3, sechsunddreißig, siebenunddreißig, achtunddreißig, eins, screen=evolve_Pokemon1(Spawning_praktibalk1, Spawning_praktibalk2, Spawning_praktibalk3, Spawning_strepoli1, Spawning_strepoli2, Spawning_strepoli3, Spawning_meistagrif1, strepoli_x1, strepoli_x2, strepoli_x3, praktibalk_x1, praktibalk_x2, praktibalk_x3, strepoli_y1, strepoli_y2, strepoli_y3, praktibalk_y1, praktibalk_y2, praktibalk_y3, strepoli1, strepoli2, strepoli3, sechsunddreißig, siebenunddreißig, achtunddreißig, eins, screen)

  Spawning_klikk1, Spawning_klikk2, Spawning_klikk3, Spawning_kliklak1, Spawning_kliklak2, Spawning_kliklak3, Spawning_klikdiklak1, kliklak_x1, kliklak_x2, kliklak_x3, klikk_x1, klikk_x2, klikk_x3, kliklak_y1, kliklak_y2, kliklak_y3, klikk_y1, klikk_y2, klikk_y3, kliklak1, kliklak2, kliklak3, dreiundvierzig, vierundvierzig, fünfundvierzig, eins, screen=evolve_Pokemon1(Spawning_klikk1, Spawning_klikk2, Spawning_klikk3, Spawning_kliklak1, Spawning_kliklak2, Spawning_kliklak3, Spawning_klikdiklak1, kliklak_x1, kliklak_x2, kliklak_x3, klikk_x1, klikk_x2, klikk_x3, kliklak_y1, kliklak_y2, kliklak_y3, klikk_y1, klikk_y2, klikk_y3, kliklak1, kliklak2, kliklak3, dreiundvierzig, vierundvierzig, fünfundvierzig, eins, screen)

  Spawning_kiesling1, Spawning_kiesling2, Spawning_kiesling3, Spawning_sedimantur1, Spawning_sedimantur2, Spawning_sedimantur3, Spawning_brokkolos1, sedimantur_x1, sedimantur_x2, sedimantur_x3, kiesling_x1, kiesling_x2, kiesling_x3, sedimantur_y1, sedimantur_y2, sedimantur_y3, kiesling_y1, kiesling_y2, kiesling_y3, sedimantur1, sedimantur2, sedimantur3, fünfzig, einundfünfzig, zweiundfünfzig, eins, screen=evolve_Pokemon1(Spawning_kiesling1, Spawning_kiesling2, Spawning_kiesling3, Spawning_sedimantur1, Spawning_sedimantur2, Spawning_sedimantur3, Spawning_brokkolos1, sedimantur_x1, sedimantur_x2, sedimantur_x3, kiesling_x1, kiesling_x2, kiesling_x3, sedimantur_y1, sedimantur_y2, sedimantur_y3, kiesling_y1, kiesling_y2, kiesling_y3, sedimantur1, sedimantur2, sedimantur3, fünfzig, einundfünfzig, zweiundfünfzig, eins, screen)

  Spawning_milza1, Spawning_milza2, Spawning_milza3, Spawning_sharfax1, Spawning_sharfax2, Spawning_sharfax3, Spawning_maxax1, sharfax_x1, sharfax_x2, sharfax_x3, milza_x1, milza_x2, milza_x3, sharfax_y1, sharfax_y2, sharfax_y3, milza_y1, milza_y2, milza_y3, sharfax1, sharfax2, sharfax3, siebenundfünfzig, achtundfünfzig, neunundfünfzig, eins, screen=evolve_Pokemon1(Spawning_milza1, Spawning_milza2, Spawning_milza3, Spawning_sharfax1, Spawning_sharfax2, Spawning_sharfax3, Spawning_maxax1, sharfax_x1, sharfax_x2, sharfax_x3, milza_x1, milza_x2, milza_x3, sharfax_y1, sharfax_y2, sharfax_y3, milza_y1, milza_y2, milza_y3, sharfax1, sharfax2, sharfax3, siebenundfünfzig, achtundfünfzig, neunundfünfzig, eins, screen)

  Spawning_ganovil1, Spawning_ganovil2, Spawning_ganovil3, Spawning_rokkaiman1, Spawning_rokkaiman2, Spawning_rokkaiman3, Spawning_rabigator1, rokkaiman_x1, rokkaiman_x2, rokkaiman_x3, ganovil_x1, ganovil_x2, ganovil_x3, rokkaiman_y1, rokkaiman_y2, rokkaiman_y3, ganovil_y1, ganovil_y2, ganovil_y3, rokkaiman1, rokkaiman2, rokkaiman3, vierundsechzig, fünfundsechzig, sechsundsechzig, eins, screen=evolve_Pokemon1(Spawning_ganovil1, Spawning_ganovil2, Spawning_ganovil3, Spawning_rokkaiman1, Spawning_rokkaiman2, Spawning_rokkaiman3, Spawning_rabigator1, rokkaiman_x1, rokkaiman_x2, rokkaiman_x3, ganovil_x1, ganovil_x2, ganovil_x3, rokkaiman_y1, rokkaiman_y2, rokkaiman_y3, ganovil_y1, ganovil_y2, ganovil_y3, rokkaiman1, rokkaiman2, rokkaiman3, vierundsechzig, fünfundsechzig, sechsundsechzig, eins, screen)

  Spawning_rotomurf1, Spawning_rotomurf2, Spawning_rotomurf3, Spawning_stalobor1, Spawning_stalobor2, Spawning_stalobor3, Spawning_stalobor21, stalobor_x1, stalobor_x2, stalobor_x3, rotomurf_x1, rotomurf_x2, rotomurf_x3, stalobor_y1, stalobor_y2, stalobor_y3, rotomurf_y1, rotomurf_y2, rotomurf_y3, stalobor1, stalobor2, stalobor3, einundsiebzig, zweiundsiebzig, dreiundsiebzig, eins, screen=evolve_Pokemon1(Spawning_rotomurf1, Spawning_rotomurf2, Spawning_rotomurf3, Spawning_stalobor1, Spawning_stalobor2, Spawning_stalobor3, Spawning_stalobor21, stalobor_x1, stalobor_x2, stalobor_x3, rotomurf_x1, rotomurf_x2, rotomurf_x3, stalobor_y1, stalobor_y2, stalobor_y3, rotomurf_y1, rotomurf_y2, rotomurf_y3, stalobor1, stalobor2, stalobor3, einundsiebzig, zweiundsiebzig, dreiundsiebzig, eins, screen)

  Spawning_makabaja1, Spawning_makabaja2, Spawning_makabaja3, Spawning_echnatoll1, Spawning_echnatoll2, Spawning_echnatoll3, Spawning_echnatoll21, echnatoll_x1, echnatoll_x2, echnatoll_x3, makabaja_x1, makabaja_x2, makabaja_x3, echnatoll_y1, echnatoll_y2, echnatoll_y3, makabaja_y1, makabaja_y2, makabaja_y3, echnatoll1, echnatoll2, echnatoll3, achtundsiebzig, neunundsiebzig, achtzig, eins, screen=evolve_Pokemon1(Spawning_makabaja1, Spawning_makabaja2, Spawning_makabaja3, Spawning_echnatoll1, Spawning_echnatoll2, Spawning_echnatoll3, Spawning_echnatoll21, echnatoll_x1, echnatoll_x2, echnatoll_x3, makabaja_x1, makabaja_x2, makabaja_x3, echnatoll_y1, echnatoll_y2, echnatoll_y3, makabaja_y1, makabaja_y2, makabaja_y3, echnatoll1, echnatoll2, echnatoll3, achtundsiebzig, neunundsiebzig, achtzig, eins, screen)

  'Zweite Entwicklung'

  Spawning_efoserp1, Spawning_efoserp2, Spawning_efoserp3, Spawning_serpiroyal1, serpiroyal_x1, efoserp_x1, efoserp_x2, efoserp_x3, serpiroyal_y1, efoserp_y1, efoserp_y2, efoserp_y3, serpiroyal1, vier, fünf, sechs, eins, screen = evolve_Pokemon2(Spawning_efoserp1, Spawning_efoserp2, Spawning_efoserp3, Spawning_serpiroyal1, serpiroyal_x1, efoserp_x1, efoserp_x2, efoserp_x3, serpiroyal_y1, efoserp_y1, efoserp_y2, efoserp_y3, serpiroyal1, vier, fünf, sechs, eins, screen)

  Spawning_ferkokel1, Spawning_ferkokel2, Spawning_ferkokel3, Spawning_flambirex1, flambirex_x1, ferkokel_x1, ferkokel_x2, ferkokel_x3, flambirex_y1, ferkokel_y1, ferkokel_y2, ferkokel_y3, flambirex1, elf, zwölf, dreizehn, eins, screen = evolve_Pokemon2(Spawning_ferkokel1, Spawning_ferkokel2, Spawning_ferkokel3, Spawning_flambirex1, flambirex_x1, ferkokel_x1, ferkokel_x2, ferkokel_x3, flambirex_y1, ferkokel_y1, ferkokel_y2, ferkokel_y3, flambirex1, elf, zwölf, dreizehn, eins, screen)

  Spawning_zwottronin1, Spawning_zwottronin2, Spawning_zwottronin3, Spawning_admurai1, admurai_x1, zwottronin_x1, zwottronin_x2, zwottronin_x3, admurai_y1, zwottronin_y1, zwottronin_y2, zwottronin_y3, admurai1, achtzehn, neunzehn, zwanzig, eins, screen = evolve_Pokemon2(Spawning_zwottronin1, Spawning_zwottronin2, Spawning_zwottronin3, Spawning_admurai1, admurai_x1, zwottronin_x1, zwottronin_x2, zwottronin_x3, admurai_y1, zwottronin_y1, zwottronin_y2, zwottronin_y3, admurai1, achtzehn, neunzehn, zwanzig, eins, screen)

  Spawning_folikon1, Spawning_folikon2, Spawning_folikon3, Spawning_matrifol1, matrifol_x1, folikon_x1, folikon_x2, folikon_x3, matrifol_y1, folikon_y1, folikon_y2, folikon_y3, matrifol1, fünfundzwanzig, sechsundzwanzig, siebenundzwanzig, eins, screen = evolve_Pokemon2(Spawning_folikon1, Spawning_folikon2, Spawning_folikon3, Spawning_matrifol1, matrifol_x1, folikon_x1, folikon_x2, folikon_x3, matrifol_y1, folikon_y1, folikon_y2, folikon_y3, matrifol1, fünfundzwanzig, sechsundzwanzig, siebenundzwanzig, eins, screen)

  Spawning_rollum1, Spawning_rollum2, Spawning_rollum3, Spawning_cerapendra1, cerapendra_x1, rollum_x1, rollum_x2, rollum_x3, cerapendra_y1, rollum_y1, rollum_y2, rollum_y3, cerapendra1, zweiunddreißig, dreiunddreißig, vierunddreißig, eins, screen = evolve_Pokemon2(Spawning_rollum1, Spawning_rollum2, Spawning_rollum3, Spawning_cerapendra1, cerapendra_x1, rollum_x1, rollum_x2, rollum_x3, cerapendra_y1, rollum_y1, rollum_y2, rollum_y3, cerapendra1, zweiunddreißig, dreiunddreißig, vierunddreißig, eins, screen)

  Spawning_strepoli1, Spawning_strepoli2, Spawning_strepoli3, Spawning_meistagrif1, meistagrif_x1, strepoli_x1, strepoli_x2, strepoli_x3, meistagrif_y1, strepoli_y1, strepoli_y2, strepoli_y3, meistagrif1, neununddreißig, vierzig, einundvierzig, eins, screen = evolve_Pokemon2(Spawning_strepoli1, Spawning_strepoli2, Spawning_strepoli3, Spawning_meistagrif1, meistagrif_x1, strepoli_x1, strepoli_x2, strepoli_x3, meistagrif_y1, strepoli_y1, strepoli_y2, strepoli_y3, meistagrif1, neununddreißig, vierzig, einundvierzig, eins, screen)

  Spawning_kliklak1, Spawning_kliklak2, Spawning_kliklak3, Spawning_klikdiklak1, klikdiklak_x1, kliklak_x1, kliklak_x2, kliklak_x3, klikdiklak_y1, kliklak_y1, kliklak_y2, kliklak_y3, klikdiklak1, sechsundvierzig, vierzig, achtundvierzig, eins, screen = evolve_Pokemon2(Spawning_kliklak1, Spawning_kliklak2, Spawning_kliklak3, Spawning_klikdiklak1, klikdiklak_x1, kliklak_x1, kliklak_x2, kliklak_x3, klikdiklak_y1, kliklak_y1, kliklak_y2, kliklak_y3, klikdiklak1, sechsundvierzig, vierzig, achtundvierzig, eins, screen)

  Spawning_sedimantur1, Spawning_sedimantur2, Spawning_sedimantur3, Spawning_brokkolos1, brokkolos_x1, sedimantur_x1, sedimantur_x2, sedimantur_x3, brokkolos_y1, sedimantur_y1, sedimantur_y2, sedimantur_y3, brokkolos1, dreiundfünfzig, vierzig, fünfundfünfzig, eins, screen = evolve_Pokemon2(Spawning_sedimantur1, Spawning_sedimantur2, Spawning_sedimantur3, Spawning_brokkolos1, brokkolos_x1, sedimantur_x1, sedimantur_x2, sedimantur_x3, brokkolos_y1, sedimantur_y1, sedimantur_y2, sedimantur_y3, brokkolos1, dreiundfünfzig, vierzig, fünfundfünfzig, eins, screen)

  Spawning_sharfax1, Spawning_sharfax2, Spawning_sharfax3, Spawning_maxax1, maxax_x1, sharfax_x1, sharfax_x2, sharfax_x3, maxax_y1, sharfax_y1, sharfax_y2, sharfax_y3, maxax1, sechzig, vierzig, zweiundsechzig, eins, screen = evolve_Pokemon2(Spawning_sharfax1, Spawning_sharfax2, Spawning_sharfax3, Spawning_maxax1, maxax_x1, sharfax_x1, sharfax_x2, sharfax_x3, maxax_y1, sharfax_y1, sharfax_y2, sharfax_y3, maxax1, sechzig, vierzig, zweiundsechzig, eins, screen)

  Spawning_rokkaiman1, Spawning_rokkaiman2, Spawning_rokkaiman3, Spawning_rabigator1, rabigator_x1, rokkaiman_x1, rokkaiman_x2, rokkaiman_x3, rabigator_y1, rokkaiman_y1, rokkaiman_y2, rokkaiman_y3, rabigator1, siebenundsechzig, vierzig, neunundsechzig, eins, screen = evolve_Pokemon2(Spawning_rokkaiman1, Spawning_rokkaiman2, Spawning_rokkaiman3, Spawning_rabigator1, rabigator_x1, rokkaiman_x1, rokkaiman_x2, rokkaiman_x3, rabigator_y1, rokkaiman_y1, rokkaiman_y2, rokkaiman_y3, rabigator1, siebenundsechzig, vierzig, neunundsechzig, eins, screen)

  Spawning_stalobor1, Spawning_stalobor2, Spawning_stalobor3, Spawning_stalobor21, stalobor2_x1, stalobor_x1, stalobor_x2, stalobor_x3, stalobor2_y1, stalobor_y1, stalobor_y2, stalobor_y3, stalobor21, vierundsiebzig, vierzig, sechsundsiebzig, eins, screen = evolve_Pokemon2(Spawning_stalobor1, Spawning_stalobor2, Spawning_stalobor3, Spawning_stalobor21, stalobor2_x1, stalobor_x1, stalobor_x2, stalobor_x3, stalobor2_y1, stalobor_y1, stalobor_y2, stalobor_y3, stalobor21, vierundsiebzig, vierzig, sechsundsiebzig, eins, screen)

  Spawning_echnatoll1, Spawning_echnatoll2, Spawning_echnatoll3, Spawning_echnatoll21, echnatoll2_x1, echnatoll_x1, echnatoll_x2, echnatoll_x3, echnatoll2_y1, echnatoll_y1, echnatoll_y2, echnatoll_y3, echnatoll21, einundachtzig, vierzig, dreiundachtzig, eins, screen = evolve_Pokemon2(Spawning_echnatoll1, Spawning_echnatoll2, Spawning_echnatoll3, Spawning_echnatoll21, echnatoll2_x1, echnatoll_x1, echnatoll_x2, echnatoll_x3, echnatoll2_y1, echnatoll_y1, echnatoll_y2, echnatoll_y3, echnatoll21, einundachtzig, vierzig, dreiundachtzig, eins, screen)

  'Verkaufen eines Pokemon'

  Spawning_serpifeu1, serpifeu_x1, serpifeu_y1, eins, eins1, gold = sell_Pokemon(Spawning_serpifeu1, serpifeu_x1, serpifeu_y1, eins, eins1, gold)
  Spawning_serpifeu2, serpifeu_x2, serpifeu_y2, zwei, eins1, gold = sell_Pokemon(Spawning_serpifeu2, serpifeu_x2, serpifeu_y2, zwei, eins1, gold)
  Spawning_serpifeu3, serpifeu_x3, serpifeu_y3, drei, eins1, gold = sell_Pokemon(Spawning_serpifeu3, serpifeu_x3, serpifeu_y3, drei, eins1, gold)
  Spawning_efoserp1, efoserp_x1, efoserp_y1, vier, drei3, gold = sell_Pokemon(Spawning_efoserp1, efoserp_x1, efoserp_y1, vier, drei3, gold)
  Spawning_efoserp2, efoserp_x2, efoserp_y2, fünf, drei3, gold = sell_Pokemon(Spawning_efoserp2, efoserp_x2, efoserp_y2, fünf, drei3, gold)
  Spawning_efoserp3, efoserp_x3, efoserp_y3, sechs, drei3, gold = sell_Pokemon(Spawning_efoserp3, efoserp_x3, efoserp_y3, sechs, drei3, gold)
  Spawning_serpiroyal1, serpiroyal_x1, serpiroyal_y1, sieben, neun9, gold = sell_Pokemon(Spawning_serpiroyal1, serpiroyal_x1, serpiroyal_y1, sieben, neun9, gold)

  Spawning_floink1, floink_x1, floink_y1, acht, eins1, gold= sell_Pokemon(Spawning_floink1, floink_x1, floink_y1, acht, eins1, gold)
  Spawning_floink2, floink_x2, floink_y2, neun, eins1, gold = sell_Pokemon(Spawning_floink2, floink_x2, floink_y2, neun, eins1, gold)
  Spawning_floink3, floink_x3, floink_y3, zehn , eins1, gold= sell_Pokemon(Spawning_floink3, floink_x3, floink_y3, zehn, eins1, gold)
  Spawning_ferkokel1, ferkokel_x1, ferkokel_y1, elf, drei3, gold = sell_Pokemon(Spawning_ferkokel1, ferkokel_x1, ferkokel_y1, elf, drei3, gold)
  Spawning_ferkokel2, ferkokel_x2, ferkokel_y2, zwölf, drei3, gold = sell_Pokemon(Spawning_ferkokel2, ferkokel_x2, ferkokel_y2, zwölf, drei3, gold)
  Spawning_ferkokel3, ferkokel_x3, ferkokel_y3, dreizehn, drei3, gold = sell_Pokemon(Spawning_ferkokel3, ferkokel_x3, ferkokel_y3, dreizehn, drei3, gold)
  Spawning_flambirex1, flambirex_x1, flambirex_y1, vierzehn, neun9, gold = sell_Pokemon(Spawning_flambirex1, flambirex_x1, flambirex_y1, vierzehn, neun9, gold)

  Spawning_ottaro1, ottaro_x1, ottaro_y1, fünfzehn, eins1, gold = sell_Pokemon(Spawning_ottaro1, ottaro_x1, ottaro_y1, fünfzehn, eins1, gold)
  Spawning_ottaro2, ottaro_x2, ottaro_y2, sechzehn, eins1, gold = sell_Pokemon(Spawning_ottaro2, ottaro_x2, ottaro_y2, sechzehn, eins1, gold)
  Spawning_ottaro3, ottaro_x3, ottaro_y3, siebzehn, eins1, gold = sell_Pokemon(Spawning_ottaro3, ottaro_x3, ottaro_y3, siebzehn, eins1, gold)
  Spawning_zwottronin1, zwottronin_x1, zwottronin_y1, achtzehn, drei3, gold = sell_Pokemon(Spawning_zwottronin1, zwottronin_x1, zwottronin_y1, achtzehn, drei3, gold)
  Spawning_zwottronin2, zwottronin_x2, zwottronin_y2, neunzehn, drei3, gold = sell_Pokemon(Spawning_zwottronin2, zwottronin_x2, zwottronin_y2, neunzehn, drei3, gold)
  Spawning_zwottronin3, zwottronin_x3, zwottronin_y3, zwanzig, drei3, gold = sell_Pokemon(Spawning_zwottronin3, zwottronin_x3, zwottronin_y3, zwanzig, drei3, gold)
  Spawning_admurai1, admurai_x1, admurai_y1, einundzwanzig, neun9, gold = sell_Pokemon(Spawning_admurai1, admurai_x1, admurai_y1, einundzwanzig, neun9, gold)

  Spawning_strawickl1, strawickl_x1, strawickl_y1, zweiundzwanzig, zwei2, gold = sell_Pokemon(Spawning_strawickl1, strawickl_x1, strawickl_y1, zweiundzwanzig, zwei2, gold)
  Spawning_strawickl2, strawickl_x2, strawickl_y2, dreiundzwanzig, zwei2, gold = sell_Pokemon(Spawning_strawickl2, strawickl_x2, strawickl_y2, dreiundzwanzig, zwei2, gold)
  Spawning_strawickl3, strawickl_x3, strawickl_y3, vierundzwanzig, zwei2, gold = sell_Pokemon(Spawning_strawickl3, strawickl_x3, strawickl_y3, vierundzwanzig, zwei2, gold)
  Spawning_folikon1, folikon_x1, folikon_y1, fünfundzwanzig, sechs6, gold = sell_Pokemon(Spawning_folikon1, folikon_x1, folikon_y1, fünfundzwanzig, sechs6, gold)
  Spawning_folikon2, folikon_x2, folikon_y2, sechsundzwanzig, sechs6, gold = sell_Pokemon(Spawning_folikon2, folikon_x2, folikon_y2, sechsundzwanzig, sechs6, gold)
  Spawning_folikon3, folikon_x3, folikon_y3, siebenundzwanzig, sechs6, gold = sell_Pokemon(Spawning_folikon3, folikon_x3, folikon_y3, siebenundzwanzig, sechs6, gold)
  Spawning_matrifol1, matrifol_x1, matrifol_y1, achtundzwanzig, achtzehn18, gold = sell_Pokemon(Spawning_matrifol1, matrifol_x1, matrifol_y1, achtundzwanzig, achtzehn18, gold)

  Spawning_toxiped1, toxiped_x1, toxiped_y1, neunundzwanzig, zwei2, gold = sell_Pokemon(Spawning_toxiped1, toxiped_x1, toxiped_y1, neunundzwanzig, zwei2, gold)
  Spawning_toxiped2, toxiped_x2, toxiped_y2, dreißig, zwei2, gold = sell_Pokemon(Spawning_toxiped2, toxiped_x2, toxiped_y2, dreißig, zwei2, gold)
  Spawning_toxiped3, toxiped_x3, toxiped_y3, einunddreißig, zwei2, gold = sell_Pokemon(Spawning_toxiped3, toxiped_x3, toxiped_y3, einunddreißig, zwei2, gold)
  Spawning_rollum1, rollum_x1, rollum_y1, zweiunddreißig, sechs6, gold = sell_Pokemon(Spawning_rollum1, rollum_x1, rollum_y1, zweiunddreißig, sechs6, gold)
  Spawning_rollum2, rollum_x2, rollum_y2, dreiunddreißig, sechs6, gold = sell_Pokemon(Spawning_rollum2, rollum_x2, rollum_y2, dreiunddreißig, sechs6, gold)
  Spawning_rollum3, rollum_x3, rollum_y3, vierunddreißig, sechs6, gold = sell_Pokemon(Spawning_rollum3, rollum_x3, rollum_y3, vierunddreißig, sechs6, gold)
  Spawning_cerapendra1, cerapendra_x1, cerapendra_y1, fünfunddreißig, achtzehn18, gold = sell_Pokemon(Spawning_cerapendra1, cerapendra_x1, cerapendra_y1, fünfunddreißig, achtzehn18, gold)

  Spawning_praktibalk1, praktibalk_x1, praktibalk_y1, sechsunddreißig, zwei2, gold = sell_Pokemon(Spawning_praktibalk1, praktibalk_x1, praktibalk_y1, sechsunddreißig, zwei2, gold)
  Spawning_praktibalk2, praktibalk_x2, praktibalk_y2, siebenunddreißig, zwei2, gold = sell_Pokemon(Spawning_praktibalk2, praktibalk_x2, praktibalk_y2, siebenunddreißig, zwei2, gold)
  Spawning_praktibalk3, praktibalk_x3, praktibalk_y3, achtunddreißig, zwei2, gold = sell_Pokemon(Spawning_praktibalk3, praktibalk_x3, praktibalk_y3, achtunddreißig, zwei2, gold)
  Spawning_strepoli1, strepoli_x1, strepoli_y1, neununddreißig, sechs6, gold = sell_Pokemon(Spawning_strepoli1, strepoli_x1, strepoli_y1, neununddreißig, sechs6, gold)
  Spawning_strepoli2, strepoli_x2, strepoli_y2, vierzig, sechs6, gold = sell_Pokemon(Spawning_strepoli2, strepoli_x2, strepoli_y2, vierzig, sechs6, gold)
  Spawning_strepoli3, strepoli_x3, strepoli_y3, einundvierzig, sechs6, gold = sell_Pokemon(Spawning_strepoli3, strepoli_x3, strepoli_y3, einundvierzig, sechs6, gold)
  Spawning_meistagrif1, meistagrif_x1, meistagrif_y1, zweiundvierzig, achtzehn18, gold = sell_Pokemon(Spawning_meistagrif1, meistagrif_x1, meistagrif_y1, zweiundvierzig, achtzehn18, gold)

  Spawning_klikk1, klikk_x1, klikk_y1, dreiundvierzig, drei3, gold = sell_Pokemon(Spawning_klikk1, klikk_x1, klikk_y1, dreiundvierzig, drei3, gold)
  Spawning_klikk2, klikk_x2, klikk_y2, vierundvierzig, drei3, gold = sell_Pokemon(Spawning_klikk2, klikk_x2, klikk_y2, vierundvierzig, drei3, gold)
  Spawning_klikk3, klikk_x3, klikk_y3, fünfundvierzig, drei3, gold = sell_Pokemon(Spawning_klikk3, klikk_x3, klikk_y3, fünfundvierzig, drei3, gold)
  Spawning_kliklak1, kliklak_x1, kliklak_y1, sechsundvierzig, neun9, gold = sell_Pokemon(Spawning_kliklak1, kliklak_x1, kliklak_y1, sechsundvierzig, neun9, gold)
  Spawning_kliklak2, kliklak_x2, kliklak_y2, vierzig, neun9, gold = sell_Pokemon(Spawning_kliklak2, kliklak_x2, kliklak_y2, siebenundvierzig, neun9, gold)
  Spawning_kliklak3, kliklak_x3, kliklak_y3, achtundvierzig, neun9, gold = sell_Pokemon(Spawning_kliklak3, kliklak_x3, kliklak_y3, achtundvierzig, neun9, gold)
  Spawning_klikdiklak1, klikdiklak_x1, klikdiklak_y1, neunundvierzig, siebenundzwanzig27, gold = sell_Pokemon(Spawning_klikdiklak1, klikdiklak_x1, klikdiklak_y1, neunundvierzig, siebenundzwanzig27, gold)

  Spawning_kiesling1, kiesling_x1, kiesling_y1, fünfzig, drei3, gold = sell_Pokemon(Spawning_kiesling1, kiesling_x1, kiesling_y1, fünfzig, drei3, gold)
  Spawning_kiesling2, kiesling_x2, kiesling_y2, einundfünfzig, drei3, gold = sell_Pokemon(Spawning_kiesling2, kiesling_x2, kiesling_y2, einundfünfzig, drei3, gold)
  Spawning_kiesling3, kiesling_x3, kiesling_y3, zweiundfünfzig, drei3, gold = sell_Pokemon(Spawning_kiesling3, kiesling_x3, kiesling_y3, zweiundfünfzig, drei3, gold)
  Spawning_sedimantur1, sedimantur_x1, sedimantur_y1, dreiundfünfzig, neun9, gold = sell_Pokemon(Spawning_sedimantur1, sedimantur_x1, sedimantur_y1, dreiundfünfzig, neun9, gold)
  Spawning_sedimantur2, sedimantur_x2, sedimantur_y2, vierzig, neun9, gold = sell_Pokemon(Spawning_sedimantur2, sedimantur_x2, sedimantur_y2, vierundfünfzig, neun9, gold)
  Spawning_sedimantur3, sedimantur_x3, sedimantur_y3, fünfundfünfzig, neun9, gold = sell_Pokemon(Spawning_sedimantur3, sedimantur_x3, sedimantur_y3, fünfundfünfzig, neun9, gold)
  Spawning_brokkolos1, brokkolos_x1, brokkolos_y1, sechsundfünfzig, siebenundzwanzig27, gold = sell_Pokemon(Spawning_brokkolos1, brokkolos_x1, brokkolos_y1, sechsundfünfzig, siebenundzwanzig27, gold)

  Spawning_milza1, milza_x1, milza_y1, siebenundfünfzig, drei3, gold = sell_Pokemon(Spawning_milza1, milza_x1, milza_y1, siebenundfünfzig, drei3, gold)
  Spawning_milza2, milza_x2, milza_y2, achtundfünfzig, drei3, gold = sell_Pokemon(Spawning_milza2, milza_x2, milza_y2, achtundfünfzig, drei3, gold)
  Spawning_milza3, milza_x3, milza_y3, neunundfünfzig, drei3, gold = sell_Pokemon(Spawning_milza3, milza_x3, milza_y3, neunundfünfzig, drei3, gold)
  Spawning_sharfax1, sharfax_x1, sharfax_y1, sechzig, neun9, gold = sell_Pokemon(Spawning_sharfax1, sharfax_x1, sharfax_y1, sechzig, neun9, gold)
  Spawning_sharfax2, sharfax_x2, sharfax_y2, vierzig, neun9, gold = sell_Pokemon(Spawning_sharfax2, sharfax_x2, sharfax_y2, einundsechzig, neun9, gold)
  Spawning_sharfax3, sharfax_x3, sharfax_y3, zweiundsechzig, neun9, gold = sell_Pokemon(Spawning_sharfax3, sharfax_x3, sharfax_y3, zweiundsechzig, neun9, gold)
  Spawning_maxax1, maxax_x1, maxax_y1, dreiundsechzig, siebenundzwanzig27, gold = sell_Pokemon(Spawning_maxax1, maxax_x1, maxax_y1, dreiundsechzig, siebenundzwanzig27, gold)

  Spawning_ganovil1, ganovil_x1, ganovil_y1, vierundsechzig, vier4, gold = sell_Pokemon(Spawning_ganovil1, ganovil_x1, ganovil_y1, vierundsechzig, vier4, gold)
  Spawning_ganovil2, ganovil_x2, ganovil_y2, fünfundsechzig, vier4, gold = sell_Pokemon(Spawning_ganovil2, ganovil_x2, ganovil_y2, fünfundsechzig, vier4, gold)
  Spawning_ganovil3, ganovil_x3, ganovil_y3, sechsundsechzig, vier4, gold = sell_Pokemon(Spawning_ganovil3, ganovil_x3, ganovil_y3, sechsundsechzig, vier4, gold)
  Spawning_rokkaiman1, rokkaiman_x1, rokkaiman_y1, siebenundsechzig, zwölf12, gold = sell_Pokemon(Spawning_rokkaiman1, rokkaiman_x1, rokkaiman_y1, siebenundsechzig, zwölf12, gold)
  Spawning_rokkaiman2, rokkaiman_x2, rokkaiman_y2, vierzig, zwölf12, gold = sell_Pokemon(Spawning_rokkaiman2, rokkaiman_x2, rokkaiman_y2, achtundsechzig, zwölf12, gold)
  Spawning_rokkaiman3, rokkaiman_x3, rokkaiman_y3, neunundsechzig, zwölf12, gold = sell_Pokemon(Spawning_rokkaiman3, rokkaiman_x3, rokkaiman_y3, neunundsechzig, zwölf12, gold)
  Spawning_rabigator1, rabigator_x1, rabigator_y1, siebzig, sechsunddreißig36, gold = sell_Pokemon(Spawning_rabigator1, rabigator_x1, rabigator_y1, siebzig, sechsunddreißig36, gold)

  Spawning_rotomurf1, rotomurf_x1, rotomurf_y1, einundsiebzig, vier4, gold = sell_Pokemon(Spawning_rotomurf1, rotomurf_x1, rotomurf_y1, einundsiebzig, vier4, gold)
  Spawning_rotomurf2, rotomurf_x2, rotomurf_y2, zweiundsiebzig, vier4, gold = sell_Pokemon(Spawning_rotomurf2, rotomurf_x2, rotomurf_y2, zweiundsiebzig, vier4, gold)
  Spawning_rotomurf3, rotomurf_x3, rotomurf_y3, dreiundsiebzig, vier4, gold = sell_Pokemon(Spawning_rotomurf3, rotomurf_x3, rotomurf_y3, dreiundsiebzig, vier4, gold)
  Spawning_stalobor1, stalobor_x1, stalobor_y1, vierundsiebzig, zwölf12, gold = sell_Pokemon(Spawning_stalobor1, stalobor_x1, stalobor_y1, vierundsiebzig, zwölf12, gold)
  Spawning_stalobor2, stalobor_x2, stalobor_y2, vierzig, zwölf12, gold = sell_Pokemon(Spawning_stalobor2, stalobor_x2, stalobor_y2, fünfundsiebzig, zwölf12, gold)
  Spawning_stalobor3, stalobor_x3, stalobor_y3, sechsundsiebzig, zwölf12, gold = sell_Pokemon(Spawning_stalobor3, stalobor_x3, stalobor_y3, sechsundsiebzig, zwölf12, gold)
  Spawning_stalobor21, stalobor2_x1, stalobor2_y1, siebenundsiebzig, sechsunddreißig36, gold = sell_Pokemon(Spawning_stalobor21, stalobor2_x1, stalobor2_y1, siebenundsiebzig, sechsunddreißig36, gold)

  Spawning_makabaja1, makabaja_x1, makabaja_y1, achtundsiebzig, vier4, gold = sell_Pokemon(Spawning_makabaja1, makabaja_x1, makabaja_y1, achtundsiebzig, vier4, gold)
  Spawning_makabaja2, makabaja_x2, makabaja_y2, neunundsiebzig, vier4, gold = sell_Pokemon(Spawning_makabaja2, makabaja_x2, makabaja_y2, neunundsiebzig, vier4, gold)
  Spawning_makabaja3, makabaja_x3, makabaja_y3, achtzig, vier4, gold = sell_Pokemon(Spawning_makabaja3, makabaja_x3, makabaja_y3, achtzig, vier4, gold)
  Spawning_echnatoll1, echnatoll_x1, echnatoll_y1, einundachtzig, zwölf12, gold = sell_Pokemon(Spawning_echnatoll1, echnatoll_x1, echnatoll_y1, einundachtzig, zwölf12, gold)
  Spawning_echnatoll2, echnatoll_x2, echnatoll_y2, vierzig, zwölf12, gold = sell_Pokemon(Spawning_echnatoll2, echnatoll_x2, echnatoll_y2, zweiundachtzig, zwölf12, gold)
  Spawning_echnatoll3, echnatoll_x3, echnatoll_y3, dreiundachtzig, zwölf12, gold = sell_Pokemon(Spawning_echnatoll3, echnatoll_x3, echnatoll_y3, dreiundachtzig, zwölf12, gold)
  Spawning_echnatoll21, echnatoll2_x1, echnatoll2_y1, vierundachtzig, sechsunddreißig36, gold = sell_Pokemon(Spawning_echnatoll21, echnatoll2_x1, echnatoll2_y1, vierundachtzig, sechsunddreißig36, gold)

  'Rerollen des Shops'

  shop_slot_1_rar, shop_slot_2_rar, shop_slot_3_rar, shop_slot_4_rar, shop_slot_5_rar, shop_slot_1_var_common, shop_slot_2_var_common, shop_slot_3_var_common, shop_slot_4_var_common, shop_slot_5_var_common, shop_slot_1_var_uncommon, shop_slot_2_var_uncommon, shop_slot_3_var_uncommon, shop_slot_4_var_uncommon, shop_slot_5_var_uncommon, shop_slot_1_var_rare, shop_slot_2_var_rare, shop_slot_3_var_rare, shop_slot_4_var_rare, shop_slot_5_var_rare, shop_slot_1_var_epic, shop_slot_2_var_epic, shop_slot_3_var_epic, shop_slot_4_var_epic, shop_slot_5_var_epic, gold = reroll_Shop(shop_slot_1_rar, shop_slot_2_rar, shop_slot_3_rar, shop_slot_4_rar, shop_slot_5_rar, shop_slot_1_var_common, shop_slot_2_var_common, shop_slot_3_var_common, shop_slot_4_var_common, shop_slot_5_var_common, shop_slot_1_var_uncommon, shop_slot_2_var_uncommon, shop_slot_3_var_uncommon, shop_slot_4_var_uncommon, shop_slot_5_var_uncommon, shop_slot_1_var_rare, shop_slot_2_var_rare, shop_slot_3_var_rare, shop_slot_4_var_rare, shop_slot_5_var_rare, shop_slot_1_var_epic, shop_slot_2_var_epic, shop_slot_3_var_epic, shop_slot_4_var_epic, shop_slot_5_var_epic, gold)
  

  Spawning_serpiroyal1, shop_slot_1_var_common, shop_slot_2_var_common, shop_slot_3_var_common, shop_slot_4_var_common, shop_slot_5_var_common, eins = reroll_Shop2(Spawning_serpiroyal1, shop_slot_1_var_common, shop_slot_2_var_common, shop_slot_3_var_common, shop_slot_4_var_common, shop_slot_5_var_common, eins)

  Spawning_flambirex1, shop_slot_1_var_common, shop_slot_2_var_common, shop_slot_3_var_common, shop_slot_4_var_common, shop_slot_5_var_common, zwei = reroll_Shop2(Spawning_flambirex1, shop_slot_1_var_common, shop_slot_2_var_common, shop_slot_3_var_common, shop_slot_4_var_common, shop_slot_5_var_common, zwei)

  Spawning_admurai1, shop_slot_1_var_common, shop_slot_2_var_common, shop_slot_3_var_common, shop_slot_4_var_common, shop_slot_5_var_common, drei = reroll_Shop2(Spawning_admurai1, shop_slot_1_var_common, shop_slot_2_var_common, shop_slot_3_var_common, shop_slot_4_var_common, shop_slot_5_var_common, drei)

  Spawning_matrifol1, shop_slot_1_var_uncommon, shop_slot_2_var_uncommon, shop_slot_3_var_uncommon, shop_slot_4_var_uncommon, shop_slot_5_var_uncommon, eins = reroll_Shop2(Spawning_matrifol1, shop_slot_1_var_uncommon, shop_slot_2_var_uncommon, shop_slot_3_var_uncommon, shop_slot_4_var_uncommon, shop_slot_5_var_uncommon, eins)

  Spawning_cerapendra1, shop_slot_1_var_uncommon, shop_slot_2_var_uncommon, shop_slot_3_var_uncommon, shop_slot_4_var_uncommon, shop_slot_5_var_uncommon, zwei = reroll_Shop2(Spawning_cerapendra1, shop_slot_1_var_uncommon, shop_slot_2_var_uncommon, shop_slot_3_var_uncommon, shop_slot_4_var_uncommon, shop_slot_5_var_uncommon, zwei)

  Spawning_meistagrif1, shop_slot_1_var_uncommon, shop_slot_2_var_uncommon, shop_slot_3_var_uncommon, shop_slot_4_var_uncommon, shop_slot_5_var_uncommon, drei = reroll_Shop2(Spawning_meistagrif1, shop_slot_1_var_uncommon, shop_slot_2_var_uncommon, shop_slot_3_var_uncommon, shop_slot_4_var_uncommon, shop_slot_5_var_uncommon, drei)

  Spawning_klikdiklak1, shop_slot_1_var_rare, shop_slot_2_var_rare, shop_slot_3_var_rare, shop_slot_4_var_rare, shop_slot_5_var_rare, eins = reroll_Shop2(Spawning_klikdiklak1, shop_slot_1_var_rare, shop_slot_2_var_rare, shop_slot_3_var_rare, shop_slot_4_var_rare, shop_slot_5_var_rare, eins)

  Spawning_brokkolos1, shop_slot_1_var_rare, shop_slot_2_var_rare, shop_slot_3_var_rare, shop_slot_4_var_rare, shop_slot_5_var_rare, zwei = reroll_Shop2(Spawning_brokkolos1, shop_slot_1_var_rare, shop_slot_2_var_rare, shop_slot_3_var_rare, shop_slot_4_var_rare, shop_slot_5_var_rare, zwei)

  Spawning_maxax1, shop_slot_1_var_rare, shop_slot_2_var_rare, shop_slot_3_var_rare, shop_slot_4_var_rare, shop_slot_5_var_rare, drei = reroll_Shop2(Spawning_maxax1, shop_slot_1_var_rare, shop_slot_2_var_rare, shop_slot_3_var_rare, shop_slot_4_var_rare, shop_slot_5_var_rare, drei)

  Spawning_rabigator1, shop_slot_1_var_epic, shop_slot_2_var_epic, shop_slot_3_var_epic, shop_slot_4_var_epic, shop_slot_5_var_epic, eins = reroll_Shop2(Spawning_rabigator1, shop_slot_1_var_epic, shop_slot_2_var_epic, shop_slot_3_var_epic, shop_slot_4_var_epic, shop_slot_5_var_epic, eins)

  Spawning_stalobor21, shop_slot_1_var_epic, shop_slot_2_var_epic, shop_slot_3_var_epic, shop_slot_4_var_epic, shop_slot_5_var_epic, zwei = reroll_Shop2(Spawning_stalobor21, shop_slot_1_var_epic, shop_slot_2_var_epic, shop_slot_3_var_epic, shop_slot_4_var_epic, shop_slot_5_var_epic, zwei)

  Spawning_echnatoll21, shop_slot_1_var_epic, shop_slot_2_var_epic, shop_slot_3_var_epic, shop_slot_4_var_epic, shop_slot_5_var_epic, drei = reroll_Shop2(Spawning_echnatoll21, shop_slot_1_var_epic, shop_slot_2_var_epic, shop_slot_3_var_epic, shop_slot_4_var_epic, shop_slot_5_var_epic, drei)


  Spawning_serpiroyal1, Spawning_flambirex1, Spawning_admurai1, eins, fünf, shop_slot_1_rar, shop_slot_2_rar, shop_slot_3_rar, shop_slot_4_rar, shop_slot_5_rar = reroll_Shop3(Spawning_serpiroyal1, Spawning_flambirex1, Spawning_admurai1, eins, fünf, shop_slot_1_rar, shop_slot_2_rar, shop_slot_3_rar, shop_slot_4_rar, shop_slot_5_rar)

  Spawning_matrifol1, Spawning_cerapendra1, Spawning_meistagrif1, fünf, acht, shop_slot_1_rar, shop_slot_2_rar, shop_slot_3_rar, shop_slot_4_rar, shop_slot_5_rar = reroll_Shop3(Spawning_matrifol1, Spawning_cerapendra1, Spawning_meistagrif1, fünf, acht, shop_slot_1_rar, shop_slot_2_rar, shop_slot_3_rar, shop_slot_4_rar, shop_slot_5_rar)

  Spawning_klikdiklak1, Spawning_brokkolos1, Spawning_maxax1, acht, zehn, shop_slot_1_rar, shop_slot_2_rar, shop_slot_3_rar, shop_slot_4_rar, shop_slot_5_rar = reroll_Shop3(Spawning_klikdiklak1, Spawning_brokkolos1, Spawning_maxax1, acht, zehn, shop_slot_1_rar, shop_slot_2_rar, shop_slot_3_rar, shop_slot_4_rar, shop_slot_5_rar)

  #ally_list, serpifeu_x1, serpifeu_y1, serpifeu1 = check_Pokemon(ally_list, serpifeu_x1, serpifeu_y1, serpifeu1)














  'FUNKTIONEN FÜR GEGNER'


  'Darstellen der Pokemon'
  
  'Shop-Slot 1'
  serpifeu_shop1g, serpifeu_shop_x1g, serpifeu_shop_y1g, eins, eins, fünf, screen, shop_slot_1_rarg, shop_slot_1_var_commong = show_Pokemon1g(serpifeu_shop1g, serpifeu_shop_x1g, serpifeu_shop_y1g, eins, eins, fünf, screen, shop_slot_1_rarg, shop_slot_1_var_commong)

  floink_shop1g, floink_shop_x1g, floink_shop_y1g, zwei, eins, fünf, screen, shop_slot_1_rarg, shop_slot_1_var_commong = show_Pokemon1g(floink_shop1g, floink_shop_x1g, floink_shop_y1g, zwei, eins, fünf, screen, shop_slot_1_rarg, shop_slot_1_var_commong)

  ottaro_shop1g, ottaro_shop_x1g, ottaro_shop_y1g, drei, eins, fünf, screen, shop_slot_1_rarg, shop_slot_1_var_commong = show_Pokemon1g(ottaro_shop1g, ottaro_shop_x1g, ottaro_shop_y1g, drei, eins, fünf, screen, shop_slot_1_rarg, shop_slot_1_var_commong)

  strawickl_shop1g, strawickl_shop_x1g, strawickl_shop_y1g, eins, fünf, acht, screen, shop_slot_1_rarg, shop_slot_1_var_uncommong = show_Pokemon1g(strawickl_shop1g, strawickl_shop_x1g, strawickl_shop_y1g, eins, fünf, acht, screen, shop_slot_1_rarg, shop_slot_1_var_uncommong)

  toxiped_shop1g, toxiped_shop_x1g, toxiped_shop_y1g, zwei, fünf, acht, screen, shop_slot_1_rarg, shop_slot_1_var_uncommong = show_Pokemon1g(toxiped_shop1g, toxiped_shop_x1g, toxiped_shop_y1g, zwei, fünf, acht, screen, shop_slot_1_rarg, shop_slot_1_var_uncommong)

  praktibalk_shop1g, praktibalk_shop_x1g, praktibalk_shop_y1g, drei, fünf, acht, screen, shop_slot_1_rarg, shop_slot_1_var_uncommong = show_Pokemon1g(praktibalk_shop1g, praktibalk_shop_x1g, praktibalk_shop_y1g, drei, fünf, acht, screen, shop_slot_1_rarg, shop_slot_1_var_uncommong)

  klikk_shop1g, klikk_shop_x1g, klikk_shop_y1g, eins, acht, zehn, screen, shop_slot_1_rarg, shop_slot_1_var_rareg = show_Pokemon1g(klikk_shop1g, klikk_shop_x1g, klikk_shop_y1g, eins, acht, zehn, screen, shop_slot_1_rarg, shop_slot_1_var_rareg)

  kiesling_shop1g, kiesling_shop_x1g, kiesling_shop_y1g, zwei, acht, zehn, screen, shop_slot_1_rarg, shop_slot_1_var_rareg = show_Pokemon1g(kiesling_shop1g, kiesling_shop_x1g, kiesling_shop_y1g, zwei, acht, zehn, screen, shop_slot_1_rarg, shop_slot_1_var_rareg)

  milza_shop1g, milza_shop_x1g, milza_shop_y1g, drei, acht, zehn, screen, shop_slot_1_rarg, shop_slot_1_var_rareg = show_Pokemon1g(milza_shop1g, milza_shop_x1g, milza_shop_y1g, drei, acht, zehn, screen, shop_slot_1_rarg, shop_slot_1_var_rareg)

  ganovil_shop1g, ganovil_shop_x1g, ganovil_shop_y1g, eins, zehn, elf, screen, shop_slot_1_rarg, shop_slot_1_var_epicg = show_Pokemon1g(ganovil_shop1g, ganovil_shop_x1g, ganovil_shop_y1g, eins, zehn, elf, screen, shop_slot_1_rarg, shop_slot_1_var_epicg)

  rotomurf_shop1g, rotomurf_shop_x1g, rotomurf_shop_y1g, zwei, zehn, elf, screen, shop_slot_1_rarg, shop_slot_1_var_epicg = show_Pokemon1g(rotomurf_shop1g, rotomurf_shop_x1g, rotomurf_shop_y1g, zwei, zehn, elf, screen, shop_slot_1_rarg, shop_slot_1_var_epicg)

  makabaja_shop1g, makabaja_shop_x1g, makabaja_shop_y1g, drei, zehn, elf, screen, shop_slot_1_rarg, shop_slot_1_var_epicg = show_Pokemon1g(makabaja_shop1g, makabaja_shop_x1g, makabaja_shop_y1g, drei, zehn, elf, screen, shop_slot_1_rarg, shop_slot_1_var_epicg)

  'Shop-Slot 2'
  serpifeu_shop2g, serpifeu_shop_x2g, serpifeu_shop_y2g, eins, eins, fünf, screen, shop_slot_2_rarg, shop_slot_2_var_commong = show_Pokemon2g(serpifeu_shop2g, serpifeu_shop_x2g, serpifeu_shop_y2g, eins, eins, fünf, screen, shop_slot_2_rarg, shop_slot_2_var_commong)

  floink_shop2g, floink_shop_x2g, floink_shop_y2g, zwei, eins, fünf, screen, shop_slot_2_rarg, shop_slot_2_var_commong = show_Pokemon2g(floink_shop2g, floink_shop_x2g, floink_shop_y2g, zwei, eins, fünf, screen, shop_slot_2_rarg, shop_slot_2_var_commong)

  ottaro_shop2g, ottaro_shop_x2g, ottaro_shop_y2g, drei, eins, fünf, screen, shop_slot_2_rarg, shop_slot_2_var_commong = show_Pokemon2g(ottaro_shop2g, ottaro_shop_x2g, ottaro_shop_y2g, drei, eins, fünf, screen, shop_slot_2_rarg, shop_slot_2_var_commong)

  strawickl_shop2g, strawickl_shop_x2g, strawickl_shop_y2g, eins, fünf, acht, screen, shop_slot_2_rarg, shop_slot_2_var_uncommong = show_Pokemon2g(strawickl_shop2g, strawickl_shop_x2g, strawickl_shop_y2g, eins, fünf, acht, screen, shop_slot_2_rarg, shop_slot_2_var_uncommong)

  toxiped_shop2g, toxiped_shop_x2g, toxiped_shop_y2g, zwei, fünf, acht, screen, shop_slot_2_rarg, shop_slot_2_var_uncommong = show_Pokemon2g(toxiped_shop2g, toxiped_shop_x2g, toxiped_shop_y2g, zwei, fünf, acht, screen, shop_slot_2_rarg, shop_slot_2_var_uncommong)

  praktibalk_shop2g, praktibalk_shop_x2g, praktibalk_shop_y2g, drei, fünf, acht, screen, shop_slot_2_rarg, shop_slot_2_var_uncommong = show_Pokemon2g(praktibalk_shop2g, praktibalk_shop_x2g, praktibalk_shop_y2g, drei, fünf, acht, screen, shop_slot_2_rarg, shop_slot_2_var_uncommong)

  klikk_shop2g, klikk_shop_x2g, klikk_shop_y2g, eins, acht, zehn, screen, shop_slot_2_rarg, shop_slot_2_var_rareg = show_Pokemon2g(klikk_shop2g, klikk_shop_x2g, klikk_shop_y2g, eins, acht, zehn, screen, shop_slot_2_rarg, shop_slot_2_var_rareg)

  kiesling_shop2g, kiesling_shop_x2g, kiesling_shop_y2g, zwei, acht, zehn, screen, shop_slot_2_rarg, shop_slot_2_var_rareg = show_Pokemon2g(kiesling_shop2g, kiesling_shop_x2g, kiesling_shop_y2g, zwei, acht, zehn, screen, shop_slot_2_rarg, shop_slot_2_var_rareg)

  milza_shop2g, milza_shop_x2g, milza_shop_y2g, drei, acht, zehn, screen, shop_slot_2_rarg, shop_slot_2_var_rareg = show_Pokemon2g(milza_shop2g, milza_shop_x2g, milza_shop_y2g, drei, acht, zehn, screen, shop_slot_2_rarg, shop_slot_2_var_rareg)

  ganovil_shop2g, ganovil_shop_x2g, ganovil_shop_y2g, eins, zehn, elf, screen, shop_slot_2_rarg, shop_slot_2_var_epicg = show_Pokemon2g(ganovil_shop2g, ganovil_shop_x2g, ganovil_shop_y2g, eins, zehn, elf, screen, shop_slot_2_rarg, shop_slot_2_var_epicg)

  rotomurf_shop2g, rotomurf_shop_x2g, rotomurf_shop_y2g, zwei, zehn, elf, screen, shop_slot_2_rarg, shop_slot_2_var_epicg = show_Pokemon2g(rotomurf_shop2g, rotomurf_shop_x2g, rotomurf_shop_y2g, zwei, zehn, elf, screen, shop_slot_2_rarg, shop_slot_2_var_epicg)

  makabaja_shop2g, makabaja_shop_x2g, makabaja_shop_y2g, drei, zehn, elf, screen, shop_slot_2_rarg, shop_slot_2_var_epicg = show_Pokemon2g(makabaja_shop2g, makabaja_shop_x2g, makabaja_shop_y2g, drei, zehn, elf, screen, shop_slot_2_rarg, shop_slot_2_var_epicg)

  'Shop-Slot 3'
  serpifeu_shop3g, serpifeu_shop_x3g, serpifeu_shop_y3g, eins, eins, fünf, screen, shop_slot_3_rarg, shop_slot_3_var_commong = show_Pokemon3g(serpifeu_shop3g, serpifeu_shop_x3g, serpifeu_shop_y3g, eins, eins, fünf, screen, shop_slot_3_rarg, shop_slot_3_var_commong)

  floink_shop3g, floink_shop_x3g, floink_shop_y3g, zwei, eins, fünf, screen, shop_slot_3_rarg, shop_slot_3_var_commong = show_Pokemon3g(floink_shop3g, floink_shop_x3g, floink_shop_y3g, zwei, eins, fünf, screen, shop_slot_3_rarg, shop_slot_3_var_commong)

  ottaro_shop3g, ottaro_shop_x3g, ottaro_shop_y3g, drei, eins, fünf, screen, shop_slot_3_rarg, shop_slot_3_var_commong = show_Pokemon3g(ottaro_shop3g, ottaro_shop_x3g, ottaro_shop_y3g, drei, eins, fünf, screen, shop_slot_3_rarg, shop_slot_3_var_commong)

  strawickl_shop3g, strawickl_shop_x3g, strawickl_shop_y3g, eins, fünf, acht, screen, shop_slot_3_rarg, shop_slot_3_var_uncommong = show_Pokemon3g(strawickl_shop3g, strawickl_shop_x3g, strawickl_shop_y3g, eins, fünf, acht, screen, shop_slot_3_rarg, shop_slot_3_var_uncommong)

  toxiped_shop3g, toxiped_shop_x3g, toxiped_shop_y3g, zwei, fünf, acht, screen, shop_slot_3_rarg, shop_slot_3_var_uncommong = show_Pokemon3g(toxiped_shop3g, toxiped_shop_x3g, toxiped_shop_y3g, zwei, fünf, acht, screen, shop_slot_3_rarg, shop_slot_3_var_uncommong)

  praktibalk_shop3g, praktibalk_shop_x3g, praktibalk_shop_y3g, drei, fünf, acht, screen, shop_slot_3_rarg, shop_slot_3_var_uncommong = show_Pokemon3g(praktibalk_shop3g, praktibalk_shop_x3g, praktibalk_shop_y3g, drei, fünf, acht, screen, shop_slot_3_rarg, shop_slot_3_var_uncommong)

  klikk_shop3g, klikk_shop_x3g, klikk_shop_y3g, eins, acht, zehn, screen, shop_slot_3_rarg, shop_slot_3_var_rareg = show_Pokemon3g(klikk_shop3g, klikk_shop_x3g, klikk_shop_y3g, eins, acht, zehn, screen, shop_slot_3_rarg, shop_slot_3_var_rareg)

  kiesling_shop3g, kiesling_shop_x3g, kiesling_shop_y3g, zwei, acht, zehn, screen, shop_slot_3_rarg, shop_slot_3_var_rareg = show_Pokemon3g(kiesling_shop3g, kiesling_shop_x3g, kiesling_shop_y3g, zwei, acht, zehn, screen, shop_slot_3_rarg, shop_slot_3_var_rareg)

  milza_shop3g, milza_shop_x3g, milza_shop_y3g, drei, acht, zehn, screen, shop_slot_3_rarg, shop_slot_3_var_rareg = show_Pokemon3g(milza_shop3g, milza_shop_x3g, milza_shop_y3g, drei, acht, zehn, screen, shop_slot_3_rarg, shop_slot_3_var_rareg)

  ganovil_shop3g, ganovil_shop_x3g, ganovil_shop_y3g, eins, zehn, elf, screen, shop_slot_3_rarg, shop_slot_3_var_epicg = show_Pokemon3g(ganovil_shop3g, ganovil_shop_x3g, ganovil_shop_y3g, eins, zehn, elf, screen, shop_slot_3_rarg, shop_slot_3_var_epicg)

  rotomurf_shop3g, rotomurf_shop_x3g, rotomurf_shop_y3g, zwei, zehn, elf, screen, shop_slot_3_rarg, shop_slot_3_var_epicg = show_Pokemon3g(rotomurf_shop3g, rotomurf_shop_x3g, rotomurf_shop_y3g, zwei, zehn, elf, screen, shop_slot_3_rarg, shop_slot_3_var_epicg)

  makabaja_shop3g, makabaja_shop_x3g, makabaja_shop_y3g, drei, zehn, elf, screen, shop_slot_3_rarg, shop_slot_3_var_epicg = show_Pokemon3g(makabaja_shop3g, makabaja_shop_x3g, makabaja_shop_y3g, drei, zehn, elf, screen, shop_slot_3_rarg, shop_slot_3_var_epicg)

  'Shop-Slot 4'
  serpifeu_shop4g, serpifeu_shop_x4g, serpifeu_shop_y4g, eins, eins, fünf, screen, shop_slot_4_rarg, shop_slot_4_var_commong = show_Pokemon4g(serpifeu_shop4g, serpifeu_shop_x4g, serpifeu_shop_y4g, eins, eins, fünf, screen, shop_slot_4_rarg, shop_slot_4_var_commong)

  floink_shop4g, floink_shop_x4g, floink_shop_y4g, zwei, eins, fünf, screen, shop_slot_4_rarg, shop_slot_4_var_commong = show_Pokemon4g(floink_shop4g, floink_shop_x4g, floink_shop_y4g, zwei, eins, fünf, screen, shop_slot_4_rarg, shop_slot_4_var_commong)

  ottaro_shop4g, ottaro_shop_x4g, ottaro_shop_y4g, drei, eins, fünf, screen, shop_slot_4_rarg, shop_slot_4_var_commong = show_Pokemon4g(ottaro_shop4g, ottaro_shop_x4g, ottaro_shop_y4g, drei, eins, fünf, screen, shop_slot_4_rarg, shop_slot_4_var_commong)

  strawickl_shop4g, strawickl_shop_x4g, strawickl_shop_y4g, eins, fünf, acht, screen, shop_slot_4_rarg, shop_slot_4_var_uncommong = show_Pokemon4g(strawickl_shop4g, strawickl_shop_x4g, strawickl_shop_y4g, eins, fünf, acht, screen, shop_slot_4_rarg, shop_slot_4_var_uncommong)

  toxiped_shop4g, toxiped_shop_x4g, toxiped_shop_y4g, zwei, fünf, acht, screen, shop_slot_4_rarg, shop_slot_4_var_uncommong = show_Pokemon4g(toxiped_shop4g, toxiped_shop_x4g, toxiped_shop_y4g, zwei, fünf, acht, screen, shop_slot_4_rarg, shop_slot_4_var_uncommong)

  praktibalk_shop4g, praktibalk_shop_x4g, praktibalk_shop_y4g, drei, fünf, acht, screen, shop_slot_4_rarg, shop_slot_4_var_uncommong = show_Pokemon4g(praktibalk_shop4g, praktibalk_shop_x4g, praktibalk_shop_y4g, drei, fünf, acht, screen, shop_slot_4_rarg, shop_slot_4_var_uncommong)

  klikk_shop4g, klikk_shop_x4g, klikk_shop_y4g, eins, acht, zehn, screen, shop_slot_4_rarg, shop_slot_4_var_rareg = show_Pokemon4g(klikk_shop4g, klikk_shop_x4g, klikk_shop_y4g, eins, acht, zehn, screen, shop_slot_4_rarg, shop_slot_4_var_rareg)

  kiesling_shop4g, kiesling_shop_x4g, kiesling_shop_y4g, zwei, acht, zehn, screen, shop_slot_4_rarg, shop_slot_4_var_rareg = show_Pokemon4g(kiesling_shop4g, kiesling_shop_x4g, kiesling_shop_y4g, zwei, acht, zehn, screen, shop_slot_4_rarg, shop_slot_4_var_rareg)

  milza_shop4g, milza_shop_x4g, milza_shop_y4g, drei, acht, zehn, screen, shop_slot_4_rarg, shop_slot_4_var_rareg = show_Pokemon4g(milza_shop4g, milza_shop_x4g, milza_shop_y4g, drei, acht, zehn, screen, shop_slot_4_rarg, shop_slot_4_var_rareg)

  ganovil_shop4g, ganovil_shop_x4g, ganovil_shop_y4g, eins, zehn, elf, screen, shop_slot_4_rarg, shop_slot_4_var_epicg = show_Pokemon4g(ganovil_shop4g, ganovil_shop_x4g, ganovil_shop_y4g, eins, zehn, elf, screen, shop_slot_4_rarg, shop_slot_4_var_epicg)

  rotomurf_shop4g, rotomurf_shop_x4g, rotomurf_shop_y4g, zwei, zehn, elf, screen, shop_slot_4_rarg, shop_slot_4_var_epicg = show_Pokemon4g(rotomurf_shop4g, rotomurf_shop_x4g, rotomurf_shop_y4g, zwei, zehn, elf, screen, shop_slot_4_rarg, shop_slot_4_var_epicg)

  makabaja_shop4g, makabaja_shop_x4g, makabaja_shop_y4g, drei, zehn, elf, screen, shop_slot_4_rarg, shop_slot_4_var_epicg = show_Pokemon4g(makabaja_shop4g, makabaja_shop_x4g, makabaja_shop_y4g, drei, zehn, elf, screen, shop_slot_4_rarg, shop_slot_4_var_epicg)

  'Shop-Slot 5'
  serpifeu_shop5g, serpifeu_shop_x5g, serpifeu_shop_y5g, eins, eins, fünf, screen, shop_slot_5_rarg, shop_slot_5_var_commong = show_Pokemon5g(serpifeu_shop5g, serpifeu_shop_x5g, serpifeu_shop_y5g, eins, eins, fünf, screen, shop_slot_5_rarg, shop_slot_5_var_commong)

  floink_shop5g, floink_shop_x5g, floink_shop_y5g, zwei, eins, fünf, screen, shop_slot_5_rarg, shop_slot_5_var_commong = show_Pokemon5g(floink_shop5g, floink_shop_x5g, floink_shop_y5g, zwei, eins, fünf, screen, shop_slot_5_rarg, shop_slot_5_var_commong)

  ottaro_shop5g, ottaro_shop_x5g, ottaro_shop_y5g, drei, eins, fünf, screen, shop_slot_5_rarg, shop_slot_5_var_commong = show_Pokemon5g(ottaro_shop5g, ottaro_shop_x5g, ottaro_shop_y5g, drei, eins, fünf, screen, shop_slot_5_rarg, shop_slot_5_var_commong)

  strawickl_shop5g, strawickl_shop_x5g, strawickl_shop_y5g, eins, fünf, acht, screen, shop_slot_5_rarg, shop_slot_5_var_uncommong = show_Pokemon5g(strawickl_shop5g, strawickl_shop_x5g, strawickl_shop_y5g, eins, fünf, acht, screen, shop_slot_5_rarg, shop_slot_5_var_uncommong)

  toxiped_shop5g, toxiped_shop_x5g, toxiped_shop_y5g, zwei, fünf, acht, screen, shop_slot_5_rarg, shop_slot_5_var_uncommong = show_Pokemon5g(toxiped_shop5g, toxiped_shop_x5g, toxiped_shop_y5g, zwei, fünf, acht, screen, shop_slot_5_rarg, shop_slot_5_var_uncommong)

  praktibalk_shop5g, praktibalk_shop_x5g, praktibalk_shop_y5g, drei, fünf, acht, screen, shop_slot_5_rarg, shop_slot_5_var_uncommong = show_Pokemon5g(praktibalk_shop5g, praktibalk_shop_x5g, praktibalk_shop_y5g, drei, fünf, acht, screen, shop_slot_5_rarg, shop_slot_5_var_uncommong)

  klikk_shop5g, klikk_shop_x5g, klikk_shop_y5g, eins, acht, zehn, screen, shop_slot_5_rarg, shop_slot_5_var_rareg = show_Pokemon5g(klikk_shop5g, klikk_shop_x5g, klikk_shop_y5g, eins, acht, zehn, screen, shop_slot_5_rarg, shop_slot_5_var_rareg)

  kiesling_shop5g, kiesling_shop_x5g, kiesling_shop_y5g, zwei, acht, zehn, screen, shop_slot_5_rarg, shop_slot_5_var_rareg = show_Pokemon5g(kiesling_shop5g, kiesling_shop_x5g, kiesling_shop_y5g, zwei, acht, zehn, screen, shop_slot_5_rarg, shop_slot_5_var_rareg)

  milza_shop5g, milza_shop_x5g, milza_shop_y5g, drei, acht, zehn, screen, shop_slot_5_rarg, shop_slot_5_var_rareg = show_Pokemon5g(milza_shop5g, milza_shop_x5g, milza_shop_y5g, drei, acht, zehn, screen, shop_slot_5_rarg, shop_slot_5_var_rareg)

  ganovil_shop5g, ganovil_shop_x5g, ganovil_shop_y5g, eins, zehn, elf, screen, shop_slot_5_rarg, shop_slot_5_var_epicg = show_Pokemon5g(ganovil_shop5g, ganovil_shop_x5g, ganovil_shop_y5g, eins, zehn, elf, screen, shop_slot_5_rarg, shop_slot_5_var_epicg)

  rotomurf_shop5g, rotomurf_shop_x5g, rotomurf_shop_y5g, zwei, zehn, elf, screen, shop_slot_5_rarg, shop_slot_5_var_epicg = show_Pokemon5g(rotomurf_shop5g, rotomurf_shop_x5g, rotomurf_shop_y5g, zwei, zehn, elf, screen, shop_slot_5_rarg, shop_slot_5_var_epicg)

  makabaja_shop5g, makabaja_shop_x5g, makabaja_shop_y5g, drei, zehn, elf, screen, shop_slot_5_rarg, shop_slot_5_var_epicg = show_Pokemon5g(makabaja_shop5g, makabaja_shop_x5g, makabaja_shop_y5g, drei, zehn, elf, screen, shop_slot_5_rarg, shop_slot_5_var_epicg)


  'Spawnen der Pokemon'

  'Shop-Slot 1'  

  Spawning_serpifeu1g, Spawning_serpifeu2g, Spawning_serpifeu3g, Spawning_serpiroyal1g, serpifeu_x1g, serpifeu_y1g, serpifeu1g, serpifeu_x2g, serpifeu_y2g, serpifeu2g, serpifeu_x3g, serpifeu_y3g, serpifeu3g, eins, eins, fünf, eins1, screen, shop_slot_1_var_commong, shop_slot_1_rarg, goldg = spawn_Pokemon1_commong(Spawning_serpifeu1g, Spawning_serpifeu2g, Spawning_serpifeu3g, Spawning_serpiroyal1g, serpifeu_x1g, serpifeu_y1g, serpifeu1g, serpifeu_x2g, serpifeu_y2g, serpifeu2g, serpifeu_x3g, serpifeu_y3g, serpifeu3g, eins, eins, fünf, eins1, screen, shop_slot_1_var_commong, shop_slot_1_rarg, goldg)

  Spawning_floink1g, Spawning_floink2g, Spawning_floink3g, Spawning_flambirex1g, floink_x1g, floink_y1g, floink1g, floink_x2g, floink_y2g, floink2g, floink_x3g, floink_y3g, floink3g, zwei, eins, fünf, eins1, screen, shop_slot_1_var_commong, shop_slot_1_rarg, goldg= spawn_Pokemon1_commong(Spawning_floink1g, Spawning_floink2g, Spawning_floink3g, Spawning_flambirex1g, floink_x1g, floink_y1g, floink1g, floink_x2g, floink_y2g, floink2g, floink_x3g, floink_y3g, floink3g, zwei, eins, fünf, eins1, screen, shop_slot_1_var_commong, shop_slot_1_rarg, goldg)

  Spawning_ottaro1g, Spawning_ottaro2g, Spawning_ottaro3g, Spawning_admurai1g, ottaro_x1g, ottaro_y1g, ottaro1g, ottaro_x2g, ottaro_y2g, ottaro2g, ottaro_x3g, ottaro_y3g, ottaro3g, drei, eins, fünf, eins1, screen, shop_slot_1_var_commong, shop_slot_1_rarg, goldg= spawn_Pokemon1_commong(Spawning_ottaro1g, Spawning_ottaro2g, Spawning_ottaro3g, Spawning_admurai1g, ottaro_x1g, ottaro_y1g, ottaro1g, ottaro_x2g, ottaro_y2g, ottaro2g, ottaro_x3g, ottaro_y3g, ottaro3g, drei, eins, fünf, eins1, screen, shop_slot_1_var_commong, shop_slot_1_rarg, goldg)

  Spawning_strawickl1g, Spawning_strawickl2g, Spawning_strawickl3g, Spawning_matrifol1g, strawickl_x1g, strawickl_y1g, strawickl1g, strawickl_x2g, strawickl_y2g, strawickl2g, strawickl_x3g, strawickl_y3g, strawickl3g, eins, fünf, acht, zwei2, screen, shop_slot_1_var_uncommong, shop_slot_1_rarg, goldg = spawn_Pokemon1_commong(Spawning_strawickl1g, Spawning_strawickl2g, Spawning_strawickl3g, Spawning_matrifol1g, strawickl_x1g, strawickl_y1g, strawickl1g, strawickl_x2g, strawickl_y2g, strawickl2g, strawickl_x3g, strawickl_y3g, strawickl3g, eins, fünf, acht, zwei2, screen, shop_slot_1_var_uncommong, shop_slot_1_rarg, goldg)

  Spawning_toxiped1g, Spawning_toxiped2g, Spawning_toxiped3g, Spawning_cerapendra1g, toxiped_x1g, toxiped_y1g, toxiped1g, toxiped_x2g, toxiped_y2g, toxiped2g, toxiped_x3g, toxiped_y3g, toxiped3g, zwei, fünf, acht, zwei2, screen, shop_slot_1_var_uncommong, shop_slot_1_rarg, goldg = spawn_Pokemon1_commong(Spawning_toxiped1g, Spawning_toxiped2g, Spawning_toxiped3g, Spawning_cerapendra1g, toxiped_x1g, toxiped_y1g, toxiped1g, toxiped_x2g, toxiped_y2g, toxiped2g, toxiped_x3g, toxiped_y3g, toxiped3g, zwei, fünf, acht, zwei2, screen, shop_slot_1_var_uncommong, shop_slot_1_rarg, goldg)

  Spawning_praktibalk1g, Spawning_praktibalk2g, Spawning_praktibalk3g, Spawning_meistagrif1g, praktibalk_x1g, praktibalk_y1g, praktibalk1g, praktibalk_x2g, praktibalk_y2g, praktibalk2g, praktibalk_x3g, praktibalk_y3g, praktibalk3g, drei, fünf, acht, zwei2, screen, shop_slot_1_var_uncommong, shop_slot_1_rarg, goldg = spawn_Pokemon1_commong(Spawning_praktibalk1g, Spawning_praktibalk2g, Spawning_praktibalk3g, Spawning_meistagrif1g, praktibalk_x1g, praktibalk_y1g, praktibalk1g, praktibalk_x2g, praktibalk_y2g, praktibalk2g, praktibalk_x3g, praktibalk_y3g, praktibalk3g, drei, fünf, acht, zwei2, screen, shop_slot_1_var_uncommong, shop_slot_1_rarg, goldg)

  Spawning_klikk1g, Spawning_klikk2g, Spawning_klikk3g, Spawning_klikdiklak1g, klikk_x1g, klikk_y1g, klikk1g, klikk_x2g, klikk_y2g, klikk2g, klikk_x3g, klikk_y3g, klikk3g, eins, acht, zehn, drei3, screen, shop_slot_1_var_rareg, shop_slot_1_rarg, goldg = spawn_Pokemon1_commong(Spawning_klikk1g, Spawning_klikk2g, Spawning_klikk3g, Spawning_klikdiklak1g, klikk_x1g, klikk_y1g, klikk1g, klikk_x2g, klikk_y2g, klikk2g, klikk_x3g, klikk_y3g, klikk3g, eins, acht, zehn, drei3, screen, shop_slot_1_var_rareg, shop_slot_1_rarg, goldg)

  Spawning_kiesling1g, Spawning_kiesling2g, Spawning_kiesling3g, Spawning_brokkolos1g, kiesling_x1g, kiesling_y1g, kiesling1g, kiesling_x2g, kiesling_y2g, kiesling2g, kiesling_x3g, kiesling_y3g, kiesling3g, zwei, acht, zehn, drei3, screen, shop_slot_1_var_rareg, shop_slot_1_rarg, goldg = spawn_Pokemon1_commong(Spawning_kiesling1g, Spawning_kiesling2g, Spawning_kiesling3g, Spawning_brokkolos1g, kiesling_x1g, kiesling_y1g, kiesling1g, kiesling_x2g, kiesling_y2g, kiesling2g, kiesling_x3g, kiesling_y3g, kiesling3g, zwei, acht, zehn, drei3, screen, shop_slot_1_var_rareg, shop_slot_1_rarg, goldg)

  Spawning_milza1g, Spawning_milza2g, Spawning_milza3g, Spawning_maxax1g, milza_x1g, milza_y1g, milza1g, milza_x2g, milza_y2g, milza2g, milza_x3g, milza_y3g, milza3g, drei, acht, zehn, drei3, screen, shop_slot_1_var_rareg, shop_slot_1_rarg, goldg = spawn_Pokemon1_commong(Spawning_milza1g, Spawning_milza2g, Spawning_milza3g, Spawning_maxax1g, milza_x1g, milza_y1g, milza1g, milza_x2g, milza_y2g, milza2g, milza_x3g, milza_y3g, milza3g, drei, acht, zehn, drei3, screen, shop_slot_1_var_rareg, shop_slot_1_rarg, goldg)

  Spawning_ganovil1g, Spawning_ganovil2g, Spawning_ganovil3g, Spawning_rabigator1g, ganovil_x1g, ganovil_y1g, ganovil1g, ganovil_x2g, ganovil_y2g, ganovil2g, ganovil_x3g, ganovil_y3g, ganovil3g, eins, zehn, elf, vier4, screen, shop_slot_1_var_epicg, shop_slot_1_rarg, goldg = spawn_Pokemon1_commong(Spawning_ganovil1g, Spawning_ganovil2g, Spawning_ganovil3g, Spawning_rabigator1g, ganovil_x1g, ganovil_y1g, ganovil1g, ganovil_x2g, ganovil_y2g, ganovil2g, ganovil_x3g, ganovil_y3g, ganovil3g, eins, zehn, elf, vier4, screen, shop_slot_1_var_epicg, shop_slot_1_rarg, goldg)

  Spawning_rotomurf1g, Spawning_rotomurf2g, Spawning_rotomurf3g, Spawning_stalobor21g, rotomurf_x1g, rotomurf_y1g, rotomurf1g, rotomurf_x2g, rotomurf_y2g, rotomurf2g, rotomurf_x3g, rotomurf_y3g, rotomurf3g, zwei, zehn, elf, vier4, screen, shop_slot_1_var_epicg, shop_slot_1_rarg, goldg = spawn_Pokemon1_commong(Spawning_rotomurf1g, Spawning_rotomurf2g, Spawning_rotomurf3g, Spawning_stalobor21g, rotomurf_x1g, rotomurf_y1g, rotomurf1g, rotomurf_x2g, rotomurf_y2g, rotomurf2g, rotomurf_x3g, rotomurf_y3g, rotomurf3g, zwei, zehn, elf, vier4, screen, shop_slot_1_var_epicg, shop_slot_1_rarg, goldg)

  Spawning_makabaja1g, Spawning_makabaja2g, Spawning_makabaja3g, Spawning_echnatoll21g, makabaja_x1g, makabaja_y1g, makabaja1g, makabaja_x2g, makabaja_y2g, makabaja2g, makabaja_x3g, makabaja_y3g, makabaja3g, drei, zehn, elf, vier4, screen, shop_slot_1_var_epicg, shop_slot_1_rarg, goldg = spawn_Pokemon1_commong(Spawning_makabaja1g, Spawning_makabaja2g, Spawning_makabaja3g, Spawning_echnatoll21g, makabaja_x1g, makabaja_y1g, makabaja1g, makabaja_x2g, makabaja_y2g, makabaja2g, makabaja_x3g, makabaja_y3g, makabaja3g, drei, zehn, elf, vier4, screen, shop_slot_1_var_epicg, shop_slot_1_rarg, goldg)

  'Shop-Slot 2'

  Spawning_serpifeu1g, Spawning_serpifeu2g, Spawning_serpifeu3g, Spawning_serpiroyal1g, serpifeu_x1g, serpifeu_y1g, serpifeu1g, serpifeu_x2g, serpifeu_y2g, serpifeu2g, serpifeu_x3g, serpifeu_y3g, serpifeu3g, eins, eins, fünf, eins1, screen, shop_slot_2_var_commong, shop_slot_2_rarg, goldg = spawn_Pokemon2_commong(Spawning_serpifeu1g, Spawning_serpifeu2g, Spawning_serpifeu3g, Spawning_serpiroyal1g, serpifeu_x1g, serpifeu_y1g, serpifeu1g, serpifeu_x2g, serpifeu_y2g, serpifeu2g, serpifeu_x3g, serpifeu_y3g, serpifeu3g, eins, eins, fünf, eins1, screen, shop_slot_2_var_commong, shop_slot_2_rarg, goldg)

  Spawning_floink1g, Spawning_floink2g, Spawning_floink3g, Spawning_flambirex1g, floink_x1g, floink_y1g, floink1g, floink_x2g, floink_y2g, floink2g, floink_x3g, floink_y3g, floink3g, zwei, eins, fünf, eins1, screen, shop_slot_2_var_commong, shop_slot_2_rarg, goldg= spawn_Pokemon2_commong(Spawning_floink1g, Spawning_floink2g, Spawning_floink3g, Spawning_flambirex1g, floink_x1g, floink_y1g, floink1g, floink_x2g, floink_y2g, floink2g, floink_x3g, floink_y3g, floink3g, zwei, eins, fünf, eins1, screen, shop_slot_2_var_commong, shop_slot_2_rarg, goldg)

  Spawning_ottaro1g, Spawning_ottaro2g, Spawning_ottaro3g, Spawning_admurai1g, ottaro_x1g, ottaro_y1g, ottaro1g, ottaro_x2g, ottaro_y2g, ottaro2g, ottaro_x3g, ottaro_y3g, ottaro3g, drei, eins, fünf, eins1, screen, shop_slot_2_var_commong, shop_slot_2_rarg, goldg= spawn_Pokemon2_commong(Spawning_ottaro1g, Spawning_ottaro2g, Spawning_ottaro3g, Spawning_admurai1g, ottaro_x1g, ottaro_y1g, ottaro1g, ottaro_x2g, ottaro_y2g, ottaro2g, ottaro_x3g, ottaro_y3g, ottaro3g, drei, eins, fünf, eins1, screen, shop_slot_2_var_commong, shop_slot_2_rarg, goldg)

  Spawning_strawickl1g, Spawning_strawickl2g, Spawning_strawickl3g, Spawning_matrifol1g, strawickl_x1g, strawickl_y1g, strawickl1g, strawickl_x2g, strawickl_y2g, strawickl2g, strawickl_x3g, strawickl_y3g, strawickl3g, eins, fünf, acht, zwei2, screen, shop_slot_2_var_uncommong, shop_slot_2_rarg, goldg = spawn_Pokemon2_commong(Spawning_strawickl1g, Spawning_strawickl2g, Spawning_strawickl3g, Spawning_matrifol1g, strawickl_x1g, strawickl_y1g, strawickl1g, strawickl_x2g, strawickl_y2g, strawickl2g, strawickl_x3g, strawickl_y3g, strawickl3g, eins, fünf, acht, zwei2, screen, shop_slot_2_var_uncommong, shop_slot_2_rarg, goldg)

  Spawning_toxiped1g, Spawning_toxiped2g, Spawning_toxiped3g, Spawning_cerapendra1g, toxiped_x1g, toxiped_y1g, toxiped1g, toxiped_x2g, toxiped_y2g, toxiped2g, toxiped_x3g, toxiped_y3g, toxiped3g, zwei, fünf, acht, zwei2, screen, shop_slot_2_var_uncommong, shop_slot_2_rarg, goldg = spawn_Pokemon2_commong(Spawning_toxiped1g, Spawning_toxiped2g, Spawning_toxiped3g, Spawning_cerapendra1g, toxiped_x1g, toxiped_y1g, toxiped1g, toxiped_x2g, toxiped_y2g, toxiped2g, toxiped_x3g, toxiped_y3g, toxiped3g, zwei, fünf, acht, zwei2, screen, shop_slot_2_var_uncommong, shop_slot_2_rarg, goldg)

  Spawning_praktibalk1g, Spawning_praktibalk2g, Spawning_praktibalk3g, Spawning_meistagrif1g, praktibalk_x1g, praktibalk_y1g, praktibalk1g, praktibalk_x2g, praktibalk_y2g, praktibalk2g, praktibalk_x3g, praktibalk_y3g, praktibalk3g, drei, fünf, acht, zwei2, screen, shop_slot_2_var_uncommong, shop_slot_2_rarg, goldg = spawn_Pokemon2_commong(Spawning_praktibalk1g, Spawning_praktibalk2g, Spawning_praktibalk3g, Spawning_meistagrif1g, praktibalk_x1g, praktibalk_y1g, praktibalk1g, praktibalk_x2g, praktibalk_y2g, praktibalk2g, praktibalk_x3g, praktibalk_y3g, praktibalk3g, drei, fünf, acht, zwei2, screen, shop_slot_2_var_uncommong, shop_slot_2_rarg, goldg)

  Spawning_klikk1g, Spawning_klikk2g, Spawning_klikk3g, Spawning_klikdiklak1g, klikk_x1g, klikk_y1g, klikk1g, klikk_x2g, klikk_y2g, klikk2g, klikk_x3g, klikk_y3g, klikk3g, eins, acht, zehn, drei3, screen, shop_slot_2_var_rareg, shop_slot_2_rarg, goldg = spawn_Pokemon2_commong(Spawning_klikk1g, Spawning_klikk2g, Spawning_klikk3g, Spawning_klikdiklak1g, klikk_x1g, klikk_y1g, klikk1g, klikk_x2g, klikk_y2g, klikk2g, klikk_x3g, klikk_y3g, klikk3g, eins, acht, zehn, drei3, screen, shop_slot_2_var_rareg, shop_slot_2_rarg, goldg)

  Spawning_kiesling1g, Spawning_kiesling2g, Spawning_kiesling3g, Spawning_brokkolos1g, kiesling_x1g, kiesling_y1g, kiesling1g, kiesling_x2g, kiesling_y2g, kiesling2g, kiesling_x3g, kiesling_y3g, kiesling3g, zwei, acht, zehn, drei3, screen, shop_slot_2_var_rareg, shop_slot_2_rarg, goldg = spawn_Pokemon2_commong(Spawning_kiesling1g, Spawning_kiesling2g, Spawning_kiesling3g, Spawning_brokkolos1g, kiesling_x1g, kiesling_y1g, kiesling1g, kiesling_x2g, kiesling_y2g, kiesling2g, kiesling_x3g, kiesling_y3g, kiesling3g, zwei, acht, zehn, drei3, screen, shop_slot_2_var_rareg, shop_slot_2_rarg, goldg)

  Spawning_milza1g, Spawning_milza2g, Spawning_milza3g, Spawning_maxax1g, milza_x1g, milza_y1g, milza1g, milza_x2g, milza_y2g, milza2g, milza_x3g, milza_y3g, milza3g, drei, acht, zehn, drei3, screen, shop_slot_2_var_rareg, shop_slot_2_rarg, goldg = spawn_Pokemon2_commong(Spawning_milza1g, Spawning_milza2g, Spawning_milza3g, Spawning_maxax1g, milza_x1g, milza_y1g, milza1g, milza_x2g, milza_y2g, milza2g, milza_x3g, milza_y3g, milza3g, drei, acht, zehn, drei3, screen, shop_slot_2_var_rareg, shop_slot_2_rarg, goldg)

  Spawning_ganovil1g, Spawning_ganovil2g, Spawning_ganovil3g, Spawning_rabigator1g, ganovil_x1g, ganovil_y1g, ganovil1g, ganovil_x2g, ganovil_y2g, ganovil2g, ganovil_x3g, ganovil_y3g, ganovil3g, eins, zehn, elf, vier4, screen, shop_slot_2_var_epicg, shop_slot_2_rarg, goldg = spawn_Pokemon2_commong(Spawning_ganovil1g, Spawning_ganovil2g, Spawning_ganovil3g, Spawning_rabigator1g, ganovil_x1g, ganovil_y1g, ganovil1g, ganovil_x2g, ganovil_y2g, ganovil2g, ganovil_x3g, ganovil_y3g, ganovil3g, eins, zehn, elf, vier4, screen, shop_slot_2_var_epicg, shop_slot_2_rarg, goldg)

  Spawning_rotomurf1g, Spawning_rotomurf2g, Spawning_rotomurf3g, Spawning_stalobor21g, rotomurf_x1g, rotomurf_y1g, rotomurf1g, rotomurf_x2g, rotomurf_y2g, rotomurf2g, rotomurf_x3g, rotomurf_y3g, rotomurf3g, zwei, zehn, elf, vier4, screen, shop_slot_2_var_epicg, shop_slot_2_rarg, goldg = spawn_Pokemon2_commong(Spawning_rotomurf1g, Spawning_rotomurf2g, Spawning_rotomurf3g, Spawning_stalobor21g, rotomurf_x1g, rotomurf_y1g, rotomurf1g, rotomurf_x2g, rotomurf_y2g, rotomurf2g, rotomurf_x3g, rotomurf_y3g, rotomurf3g, zwei, zehn, elf, vier4, screen, shop_slot_2_var_epicg, shop_slot_2_rarg, goldg)

  Spawning_makabaja1g, Spawning_makabaja2g, Spawning_makabaja3g, Spawning_echnatoll21g, makabaja_x1g, makabaja_y1g, makabaja1g, makabaja_x2g, makabaja_y2g, makabaja2g, makabaja_x3g, makabaja_y3g, makabaja3g, drei, zehn, elf, vier4, screen, shop_slot_2_var_epicg, shop_slot_2_rarg, goldg = spawn_Pokemon2_commong(Spawning_makabaja1g, Spawning_makabaja2g, Spawning_makabaja3g, Spawning_echnatoll21g, makabaja_x1g, makabaja_y1g, makabaja1g, makabaja_x2g, makabaja_y2g, makabaja2g, makabaja_x3g, makabaja_y3g, makabaja3g, drei, zehn, elf, vier4, screen, shop_slot_2_var_epicg, shop_slot_2_rarg, goldg)

  'Shop-Slot 3'

  Spawning_serpifeu1g, Spawning_serpifeu2g, Spawning_serpifeu3g, Spawning_serpiroyal1g, serpifeu_x1g, serpifeu_y1g, serpifeu1g, serpifeu_x2g, serpifeu_y2g, serpifeu2g, serpifeu_x3g, serpifeu_y3g, serpifeu3g, eins, eins, fünf, eins1, screen, shop_slot_3_var_commong, shop_slot_3_rarg, goldg = spawn_Pokemon3_commong(Spawning_serpifeu1g, Spawning_serpifeu2g, Spawning_serpifeu3g, Spawning_serpiroyal1g, serpifeu_x1g, serpifeu_y1g, serpifeu1g, serpifeu_x2g, serpifeu_y2g, serpifeu2g, serpifeu_x3g, serpifeu_y3g, serpifeu3g, eins, eins, fünf, eins1, screen, shop_slot_3_var_commong, shop_slot_3_rarg, goldg)

  Spawning_floink1g, Spawning_floink2g, Spawning_floink3g, Spawning_flambirex1g, floink_x1g, floink_y1g, floink1g, floink_x2g, floink_y2g, floink2g, floink_x3g, floink_y3g, floink3g, zwei, eins, fünf, eins1, screen, shop_slot_3_var_commong, shop_slot_3_rarg, goldg= spawn_Pokemon3_commong(Spawning_floink1g, Spawning_floink2g, Spawning_floink3g, Spawning_flambirex1g, floink_x1g, floink_y1g, floink1g, floink_x2g, floink_y2g, floink2g, floink_x3g, floink_y3g, floink3g, zwei, eins, fünf, eins1, screen, shop_slot_3_var_commong, shop_slot_3_rarg, goldg)

  Spawning_ottaro1g, Spawning_ottaro2g, Spawning_ottaro3g, Spawning_admurai1g, ottaro_x1g, ottaro_y1g, ottaro1g, ottaro_x2g, ottaro_y2g, ottaro2g, ottaro_x3g, ottaro_y3g, ottaro3g, drei, eins, fünf, eins1, screen, shop_slot_3_var_commong, shop_slot_3_rarg, goldg= spawn_Pokemon3_commong(Spawning_ottaro1g, Spawning_ottaro2g, Spawning_ottaro3g, Spawning_admurai1g, ottaro_x1g, ottaro_y1g, ottaro1g, ottaro_x2g, ottaro_y2g, ottaro2g, ottaro_x3g, ottaro_y3g, ottaro3g, drei, eins, fünf, eins1, screen, shop_slot_3_var_commong, shop_slot_3_rarg, goldg)

  Spawning_strawickl1g, Spawning_strawickl2g, Spawning_strawickl3g, Spawning_matrifol1g, strawickl_x1g, strawickl_y1g, strawickl1g, strawickl_x2g, strawickl_y2g, strawickl2g, strawickl_x3g, strawickl_y3g, strawickl3g, eins, fünf, acht, zwei2, screen, shop_slot_3_var_uncommong, shop_slot_3_rarg, goldg = spawn_Pokemon3_commong(Spawning_strawickl1g, Spawning_strawickl2g, Spawning_strawickl3g, Spawning_matrifol1g, strawickl_x1g, strawickl_y1g, strawickl1g, strawickl_x2g, strawickl_y2g, strawickl2g, strawickl_x3g, strawickl_y3g, strawickl3g, eins, fünf, acht, zwei2, screen, shop_slot_3_var_uncommong, shop_slot_3_rarg, goldg)

  Spawning_toxiped1g, Spawning_toxiped2g, Spawning_toxiped3g, Spawning_cerapendra1g, toxiped_x1g, toxiped_y1g, toxiped1g, toxiped_x2g, toxiped_y2g, toxiped2g, toxiped_x3g, toxiped_y3g, toxiped3g, zwei, fünf, acht, zwei2, screen, shop_slot_3_var_uncommong, shop_slot_3_rarg, goldg = spawn_Pokemon3_commong(Spawning_toxiped1g, Spawning_toxiped2g, Spawning_toxiped3g, Spawning_cerapendra1g, toxiped_x1g, toxiped_y1g, toxiped1g, toxiped_x2g, toxiped_y2g, toxiped2g, toxiped_x3g, toxiped_y3g, toxiped3g, zwei, fünf, acht, zwei2, screen, shop_slot_3_var_uncommong, shop_slot_3_rarg, goldg)

  Spawning_praktibalk1g, Spawning_praktibalk2g, Spawning_praktibalk3g, Spawning_meistagrif1g, praktibalk_x1g, praktibalk_y1g, praktibalk1g, praktibalk_x2g, praktibalk_y2g, praktibalk2g, praktibalk_x3g, praktibalk_y3g, praktibalk3g, drei, fünf, acht, zwei2, screen, shop_slot_3_var_uncommong, shop_slot_3_rarg, goldg = spawn_Pokemon3_commong(Spawning_praktibalk1g, Spawning_praktibalk2g, Spawning_praktibalk3g, Spawning_meistagrif1g, praktibalk_x1g, praktibalk_y1g, praktibalk1g, praktibalk_x2g, praktibalk_y2g, praktibalk2g, praktibalk_x3g, praktibalk_y3g, praktibalk3g, drei, fünf, acht, zwei2, screen, shop_slot_3_var_uncommong, shop_slot_3_rarg, goldg)

  Spawning_klikk1g, Spawning_klikk2g, Spawning_klikk3g, Spawning_klikdiklak1g, klikk_x1g, klikk_y1g, klikk1g, klikk_x2g, klikk_y2g, klikk2g, klikk_x3g, klikk_y3g, klikk3g, eins, acht, zehn, drei3, screen, shop_slot_3_var_rareg, shop_slot_3_rarg, goldg = spawn_Pokemon3_commong(Spawning_klikk1g, Spawning_klikk2g, Spawning_klikk3g, Spawning_klikdiklak1g, klikk_x1g, klikk_y1g, klikk1g, klikk_x2g, klikk_y2g, klikk2g, klikk_x3g, klikk_y3g, klikk3g, eins, acht, zehn, drei3, screen, shop_slot_3_var_rareg, shop_slot_3_rarg, goldg)

  Spawning_kiesling1g, Spawning_kiesling2g, Spawning_kiesling3g, Spawning_brokkolos1g, kiesling_x1g, kiesling_y1g, kiesling1g, kiesling_x2g, kiesling_y2g, kiesling2g, kiesling_x3g, kiesling_y3g, kiesling3g, zwei, acht, zehn, drei3, screen, shop_slot_3_var_rareg, shop_slot_3_rarg, goldg = spawn_Pokemon3_commong(Spawning_kiesling1g, Spawning_kiesling2g, Spawning_kiesling3g, Spawning_brokkolos1g, kiesling_x1g, kiesling_y1g, kiesling1g, kiesling_x2g, kiesling_y2g, kiesling2g, kiesling_x3g, kiesling_y3g, kiesling3g, zwei, acht, zehn, drei3, screen, shop_slot_3_var_rareg, shop_slot_3_rarg, goldg)

  Spawning_milza1g, Spawning_milza2g, Spawning_milza3g, Spawning_maxax1g, milza_x1g, milza_y1g, milza1g, milza_x2g, milza_y2g, milza2g, milza_x3g, milza_y3g, milza3g, drei, acht, zehn, drei3, screen, shop_slot_3_var_rareg, shop_slot_3_rarg, goldg = spawn_Pokemon3_commong(Spawning_milza1g, Spawning_milza2g, Spawning_milza3g, Spawning_maxax1g, milza_x1g, milza_y1g, milza1g, milza_x2g, milza_y2g, milza2g, milza_x3g, milza_y3g, milza3g, drei, acht, zehn, drei3, screen, shop_slot_3_var_rareg, shop_slot_3_rarg, goldg)

  Spawning_ganovil1g, Spawning_ganovil2g, Spawning_ganovil3g, Spawning_rabigator1g, ganovil_x1g, ganovil_y1g, ganovil1g, ganovil_x2g, ganovil_y2g, ganovil2g, ganovil_x3g, ganovil_y3g, ganovil3g, eins, zehn, elf, vier4, screen, shop_slot_3_var_epicg, shop_slot_3_rarg, goldg = spawn_Pokemon3_commong(Spawning_ganovil1g, Spawning_ganovil2g, Spawning_ganovil3g, Spawning_rabigator1g, ganovil_x1g, ganovil_y1g, ganovil1g, ganovil_x2g, ganovil_y2g, ganovil2g, ganovil_x3g, ganovil_y3g, ganovil3g, eins, zehn, elf, vier4, screen, shop_slot_3_var_epicg, shop_slot_3_rarg, goldg)

  Spawning_rotomurf1g, Spawning_rotomurf2g, Spawning_rotomurf3g, Spawning_stalobor21g, rotomurf_x1g, rotomurf_y1g, rotomurf1g, rotomurf_x2g, rotomurf_y2g, rotomurf2g, rotomurf_x3g, rotomurf_y3g, rotomurf3g, zwei, zehn, elf, vier4, screen, shop_slot_3_var_epicg, shop_slot_3_rarg, goldg = spawn_Pokemon3_commong(Spawning_rotomurf1g, Spawning_rotomurf2g, Spawning_rotomurf3g, Spawning_stalobor21g, rotomurf_x1g, rotomurf_y1g, rotomurf1g, rotomurf_x2g, rotomurf_y2g, rotomurf2g, rotomurf_x3g, rotomurf_y3g, rotomurf3g, zwei, zehn, elf, vier4, screen, shop_slot_3_var_epicg, shop_slot_3_rarg, goldg)

  Spawning_makabaja1g, Spawning_makabaja2g, Spawning_makabaja3g, Spawning_echnatoll21g, makabaja_x1g, makabaja_y1g, makabaja1g, makabaja_x2g, makabaja_y2g, makabaja2g, makabaja_x3g, makabaja_y3g, makabaja3g, drei, zehn, elf, vier4, screen, shop_slot_3_var_epicg, shop_slot_3_rarg, goldg = spawn_Pokemon3_commong(Spawning_makabaja1g, Spawning_makabaja2g, Spawning_makabaja3g, Spawning_echnatoll21g, makabaja_x1g, makabaja_y1g, makabaja1g, makabaja_x2g, makabaja_y2g, makabaja2g, makabaja_x3g, makabaja_y3g, makabaja3g, drei, zehn, elf, vier4, screen, shop_slot_3_var_epicg, shop_slot_3_rarg, goldg)

  'Shop-Slot 4'

  Spawning_serpifeu1g, Spawning_serpifeu2g, Spawning_serpifeu3g, Spawning_serpiroyal1g, serpifeu_x1g, serpifeu_y1g, serpifeu1g, serpifeu_x2g, serpifeu_y2g, serpifeu2g, serpifeu_x3g, serpifeu_y3g, serpifeu3g, eins, eins, fünf, eins1, screen, shop_slot_4_var_commong, shop_slot_4_rarg, goldg = spawn_Pokemon4_commong(Spawning_serpifeu1g, Spawning_serpifeu2g, Spawning_serpifeu3g, Spawning_serpiroyal1g, serpifeu_x1g, serpifeu_y1g, serpifeu1g, serpifeu_x2g, serpifeu_y2g, serpifeu2g, serpifeu_x3g, serpifeu_y3g, serpifeu3g, eins, eins, fünf, eins1, screen, shop_slot_4_var_commong, shop_slot_4_rarg, goldg)

  Spawning_floink1g, Spawning_floink2g, Spawning_floink3g, Spawning_flambirex1g, floink_x1g, floink_y1g, floink1g, floink_x2g, floink_y2g, floink2g, floink_x3g, floink_y3g, floink3g, zwei, eins, fünf, eins1, screen, shop_slot_4_var_commong, shop_slot_4_rarg, goldg= spawn_Pokemon4_commong(Spawning_floink1g, Spawning_floink2g, Spawning_floink3g, Spawning_flambirex1g, floink_x1g, floink_y1g, floink1g, floink_x2g, floink_y2g, floink2g, floink_x3g, floink_y3g, floink3g, zwei, eins, fünf, eins1, screen, shop_slot_4_var_commong, shop_slot_4_rarg, goldg)

  Spawning_ottaro1g, Spawning_ottaro2g, Spawning_ottaro3g, Spawning_admurai1g, ottaro_x1g, ottaro_y1g, ottaro1g, ottaro_x2g, ottaro_y2g, ottaro2g, ottaro_x3g, ottaro_y3g, ottaro3g, drei, eins, fünf, eins1, screen, shop_slot_4_var_commong, shop_slot_4_rarg, goldg= spawn_Pokemon4_commong(Spawning_ottaro1g, Spawning_ottaro2g, Spawning_ottaro3g, Spawning_admurai1g, ottaro_x1g, ottaro_y1g, ottaro1g, ottaro_x2g, ottaro_y2g, ottaro2g, ottaro_x3g, ottaro_y3g, ottaro3g, drei, eins, fünf, eins1, screen, shop_slot_4_var_commong, shop_slot_4_rarg, goldg)

  Spawning_strawickl1g, Spawning_strawickl2g, Spawning_strawickl3g, Spawning_matrifol1g, strawickl_x1g, strawickl_y1g, strawickl1g, strawickl_x2g, strawickl_y2g, strawickl2g, strawickl_x3g, strawickl_y3g, strawickl3g, eins, fünf, acht, zwei2, screen, shop_slot_4_var_uncommong, shop_slot_4_rarg, goldg = spawn_Pokemon4_commong(Spawning_strawickl1g, Spawning_strawickl2g, Spawning_strawickl3g, Spawning_matrifol1g, strawickl_x1g, strawickl_y1g, strawickl1g, strawickl_x2g, strawickl_y2g, strawickl2g, strawickl_x3g, strawickl_y3g, strawickl3g, eins, fünf, acht, zwei2, screen, shop_slot_4_var_uncommong, shop_slot_4_rarg, goldg)

  Spawning_toxiped1g, Spawning_toxiped2g, Spawning_toxiped3g, Spawning_cerapendra1g, toxiped_x1g, toxiped_y1g, toxiped1g, toxiped_x2g, toxiped_y2g, toxiped2g, toxiped_x3g, toxiped_y3g, toxiped3g, zwei, fünf, acht, zwei2, screen, shop_slot_4_var_uncommong, shop_slot_4_rarg, goldg = spawn_Pokemon4_commong(Spawning_toxiped1g, Spawning_toxiped2g, Spawning_toxiped3g, Spawning_cerapendra1g, toxiped_x1g, toxiped_y1g, toxiped1g, toxiped_x2g, toxiped_y2g, toxiped2g, toxiped_x3g, toxiped_y3g, toxiped3g, zwei, fünf, acht, zwei2, screen, shop_slot_4_var_uncommong, shop_slot_4_rarg, goldg)

  Spawning_praktibalk1g, Spawning_praktibalk2g, Spawning_praktibalk3g, Spawning_meistagrif1g, praktibalk_x1g, praktibalk_y1g, praktibalk1g, praktibalk_x2g, praktibalk_y2g, praktibalk2g, praktibalk_x3g, praktibalk_y3g, praktibalk3g, drei, fünf, acht, zwei2, screen, shop_slot_4_var_uncommong, shop_slot_4_rarg, goldg = spawn_Pokemon4_commong(Spawning_praktibalk1g, Spawning_praktibalk2g, Spawning_praktibalk3g, Spawning_meistagrif1g, praktibalk_x1g, praktibalk_y1g, praktibalk1g, praktibalk_x2g, praktibalk_y2g, praktibalk2g, praktibalk_x3g, praktibalk_y3g, praktibalk3g, drei, fünf, acht, zwei2, screen, shop_slot_4_var_uncommong, shop_slot_4_rarg, goldg)

  Spawning_klikk1g, Spawning_klikk2g, Spawning_klikk3g, Spawning_klikdiklak1g, klikk_x1g, klikk_y1g, klikk1g, klikk_x2g, klikk_y2g, klikk2g, klikk_x3g, klikk_y3g, klikk3g, eins, acht, zehn, drei3, screen, shop_slot_4_var_rareg, shop_slot_4_rarg, goldg = spawn_Pokemon4_commong(Spawning_klikk1g, Spawning_klikk2g, Spawning_klikk3g, Spawning_klikdiklak1g, klikk_x1g, klikk_y1g, klikk1g, klikk_x2g, klikk_y2g, klikk2g, klikk_x3g, klikk_y3g, klikk3g, eins, acht, zehn, drei3, screen, shop_slot_4_var_rareg, shop_slot_4_rarg, goldg)

  Spawning_kiesling1g, Spawning_kiesling2g, Spawning_kiesling3g, Spawning_brokkolos1g, kiesling_x1g, kiesling_y1g, kiesling1g, kiesling_x2g, kiesling_y2g, kiesling2g, kiesling_x3g, kiesling_y3g, kiesling3g, zwei, acht, zehn, drei3, screen, shop_slot_4_var_rareg, shop_slot_4_rarg, goldg = spawn_Pokemon4_commong(Spawning_kiesling1g, Spawning_kiesling2g, Spawning_kiesling3g, Spawning_brokkolos1g, kiesling_x1g, kiesling_y1g, kiesling1g, kiesling_x2g, kiesling_y2g, kiesling2g, kiesling_x3g, kiesling_y3g, kiesling3g, zwei, acht, zehn, drei3, screen, shop_slot_4_var_rareg, shop_slot_4_rarg, goldg)

  Spawning_milza1g, Spawning_milza2g, Spawning_milza3g, Spawning_maxax1g, milza_x1g, milza_y1g, milza1g, milza_x2g, milza_y2g, milza2g, milza_x3g, milza_y3g, milza3g, drei, acht, zehn, drei3, screen, shop_slot_4_var_rareg, shop_slot_4_rarg, goldg = spawn_Pokemon4_commong(Spawning_milza1g, Spawning_milza2g, Spawning_milza3g, Spawning_maxax1g, milza_x1g, milza_y1g, milza1g, milza_x2g, milza_y2g, milza2g, milza_x3g, milza_y3g, milza3g, drei, acht, zehn, drei3, screen, shop_slot_4_var_rareg, shop_slot_4_rarg, goldg)

  Spawning_ganovil1g, Spawning_ganovil2g, Spawning_ganovil3g, Spawning_rabigator1g, ganovil_x1g, ganovil_y1g, ganovil1g, ganovil_x2g, ganovil_y2g, ganovil2g, ganovil_x3g, ganovil_y3g, ganovil3g, eins, zehn, elf, vier4, screen, shop_slot_4_var_epicg, shop_slot_4_rarg, goldg = spawn_Pokemon4_commong(Spawning_ganovil1g, Spawning_ganovil2g, Spawning_ganovil3g, Spawning_rabigator1g, ganovil_x1g, ganovil_y1g, ganovil1g, ganovil_x2g, ganovil_y2g, ganovil2g, ganovil_x3g, ganovil_y3g, ganovil3g, eins, zehn, elf, vier4, screen, shop_slot_4_var_epicg, shop_slot_4_rarg, goldg)

  Spawning_rotomurf1g, Spawning_rotomurf2g, Spawning_rotomurf3g, Spawning_stalobor21g, rotomurf_x1g, rotomurf_y1g, rotomurf1g, rotomurf_x2g, rotomurf_y2g, rotomurf2g, rotomurf_x3g, rotomurf_y3g, rotomurf3g, zwei, zehn, elf, vier4, screen, shop_slot_4_var_epicg, shop_slot_4_rarg, goldg = spawn_Pokemon4_commong(Spawning_rotomurf1g, Spawning_rotomurf2g, Spawning_rotomurf3g, Spawning_stalobor21g, rotomurf_x1g, rotomurf_y1g, rotomurf1g, rotomurf_x2g, rotomurf_y2g, rotomurf2g, rotomurf_x3g, rotomurf_y3g, rotomurf3g, zwei, zehn, elf, vier4, screen, shop_slot_4_var_epicg, shop_slot_4_rarg, goldg)

  Spawning_makabaja1g, Spawning_makabaja2g, Spawning_makabaja3g, Spawning_echnatoll21g, makabaja_x1g, makabaja_y1g, makabaja1g, makabaja_x2g, makabaja_y2g, makabaja2g, makabaja_x3g, makabaja_y3g, makabaja3g, drei, zehn, elf, vier4, screen, shop_slot_4_var_epicg, shop_slot_4_rarg, goldg = spawn_Pokemon4_commong(Spawning_makabaja1g, Spawning_makabaja2g, Spawning_makabaja3g, Spawning_echnatoll21g, makabaja_x1g, makabaja_y1g, makabaja1g, makabaja_x2g, makabaja_y2g, makabaja2g, makabaja_x3g, makabaja_y3g, makabaja3g, drei, zehn, elf, vier4, screen, shop_slot_4_var_epicg, shop_slot_4_rarg, goldg)

  'Shop-Slot 5'    

  Spawning_serpifeu1g, Spawning_serpifeu2g, Spawning_serpifeu3g, Spawning_serpiroyal1g, serpifeu_x1g, serpifeu_y1g, serpifeu1g, serpifeu_x2g, serpifeu_y2g, serpifeu2g, serpifeu_x3g, serpifeu_y3g, serpifeu3g, eins, eins, fünf, eins1, screen, shop_slot_5_var_commong, shop_slot_5_rarg, goldg = spawn_Pokemon5_commong(Spawning_serpifeu1g, Spawning_serpifeu2g, Spawning_serpifeu3g, Spawning_serpiroyal1g, serpifeu_x1g, serpifeu_y1g, serpifeu1g, serpifeu_x2g, serpifeu_y2g, serpifeu2g, serpifeu_x3g, serpifeu_y3g, serpifeu3g, eins, eins, fünf, eins1, screen, shop_slot_5_var_commong, shop_slot_5_rarg, goldg)

  Spawning_floink1g, Spawning_floink2g, Spawning_floink3g, Spawning_flambirex1g, floink_x1g, floink_y1g, floink1g, floink_x2g, floink_y2g, floink2g, floink_x3g, floink_y3g, floink3g, zwei, eins, fünf, eins1, screen, shop_slot_5_var_commong, shop_slot_5_rarg, goldg= spawn_Pokemon5_commong(Spawning_floink1g, Spawning_floink2g, Spawning_floink3g, Spawning_flambirex1g, floink_x1g, floink_y1g, floink1g, floink_x2g, floink_y2g, floink2g, floink_x3g, floink_y3g, floink3g, zwei, eins, fünf, eins1, screen, shop_slot_5_var_commong, shop_slot_5_rarg, goldg)

  Spawning_ottaro1g, Spawning_ottaro2g, Spawning_ottaro3g, Spawning_admurai1g, ottaro_x1g, ottaro_y1g, ottaro1g, ottaro_x2g, ottaro_y2g, ottaro2g, ottaro_x3g, ottaro_y3g, ottaro3g, drei, eins, fünf, eins1, screen, shop_slot_5_var_commong, shop_slot_5_rarg, goldg= spawn_Pokemon5_commong(Spawning_ottaro1g, Spawning_ottaro2g, Spawning_ottaro3g, Spawning_admurai1g, ottaro_x1g, ottaro_y1g, ottaro1g, ottaro_x2g, ottaro_y2g, ottaro2g, ottaro_x3g, ottaro_y3g, ottaro3g, drei, eins, fünf, eins1, screen, shop_slot_5_var_commong, shop_slot_5_rarg, goldg)

  Spawning_strawickl1g, Spawning_strawickl2g, Spawning_strawickl3g, Spawning_matrifol1g, strawickl_x1g, strawickl_y1g, strawickl1g, strawickl_x2g, strawickl_y2g, strawickl2g, strawickl_x3g, strawickl_y3g, strawickl3g, eins, fünf, acht, zwei2, screen, shop_slot_5_var_uncommong, shop_slot_5_rarg, goldg = spawn_Pokemon5_commong(Spawning_strawickl1g, Spawning_strawickl2g, Spawning_strawickl3g, Spawning_matrifol1g, strawickl_x1g, strawickl_y1g, strawickl1g, strawickl_x2g, strawickl_y2g, strawickl2g, strawickl_x3g, strawickl_y3g, strawickl3g, eins, fünf, acht, zwei2, screen, shop_slot_5_var_uncommong, shop_slot_5_rarg, goldg)

  Spawning_toxiped1g, Spawning_toxiped2g, Spawning_toxiped3g, Spawning_cerapendra1g, toxiped_x1g, toxiped_y1g, toxiped1g, toxiped_x2g, toxiped_y2g, toxiped2g, toxiped_x3g, toxiped_y3g, toxiped3g, zwei, fünf, acht, zwei2, screen, shop_slot_5_var_uncommong, shop_slot_5_rarg, goldg = spawn_Pokemon5_commong(Spawning_toxiped1g, Spawning_toxiped2g, Spawning_toxiped3g, Spawning_cerapendra1g, toxiped_x1g, toxiped_y1g, toxiped1g, toxiped_x2g, toxiped_y2g, toxiped2g, toxiped_x3g, toxiped_y3g, toxiped3g, zwei, fünf, acht, zwei2, screen, shop_slot_5_var_uncommong, shop_slot_5_rarg, goldg)

  Spawning_praktibalk1g, Spawning_praktibalk2g, Spawning_praktibalk3g, Spawning_meistagrif1g, praktibalk_x1g, praktibalk_y1g, praktibalk1g, praktibalk_x2g, praktibalk_y2g, praktibalk2g, praktibalk_x3g, praktibalk_y3g, praktibalk3g, drei, fünf, acht, zwei2, screen, shop_slot_5_var_uncommong, shop_slot_5_rarg, goldg = spawn_Pokemon5_commong(Spawning_praktibalk1g, Spawning_praktibalk2g, Spawning_praktibalk3g, Spawning_meistagrif1g, praktibalk_x1g, praktibalk_y1g, praktibalk1g, praktibalk_x2g, praktibalk_y2g, praktibalk2g, praktibalk_x3g, praktibalk_y3g, praktibalk3g, drei, fünf, acht, zwei2, screen, shop_slot_5_var_uncommong, shop_slot_5_rarg, goldg)

  Spawning_klikk1g, Spawning_klikk2g, Spawning_klikk3g, Spawning_klikdiklak1g, klikk_x1g, klikk_y1g, klikk1g, klikk_x2g, klikk_y2g, klikk2g, klikk_x3g, klikk_y3g, klikk3g, eins, acht, zehn, drei3, screen, shop_slot_5_var_rareg, shop_slot_5_rarg, goldg = spawn_Pokemon5_commong(Spawning_klikk1g, Spawning_klikk2g, Spawning_klikk3g, Spawning_klikdiklak1g, klikk_x1g, klikk_y1g, klikk1g, klikk_x2g, klikk_y2g, klikk2g, klikk_x3g, klikk_y3g, klikk3g, eins, acht, zehn, drei3, screen, shop_slot_5_var_rareg, shop_slot_5_rarg, goldg)

  Spawning_kiesling1g, Spawning_kiesling2g, Spawning_kiesling3g, Spawning_brokkolos1g, kiesling_x1g, kiesling_y1g, kiesling1g, kiesling_x2g, kiesling_y2g, kiesling2g, kiesling_x3g, kiesling_y3g, kiesling3g, zwei, acht, zehn, drei3, screen, shop_slot_5_var_rareg, shop_slot_5_rarg, goldg = spawn_Pokemon5_commong(Spawning_kiesling1g, Spawning_kiesling2g, Spawning_kiesling3g, Spawning_brokkolos1g, kiesling_x1g, kiesling_y1g, kiesling1g, kiesling_x2g, kiesling_y2g, kiesling2g, kiesling_x3g, kiesling_y3g, kiesling3g, zwei, acht, zehn, drei3, screen, shop_slot_5_var_rareg, shop_slot_5_rarg, goldg)

  Spawning_milza1g, Spawning_milza2g, Spawning_milza3g, Spawning_maxax1g, milza_x1g, milza_y1g, milza1g, milza_x2g, milza_y2g, milza2g, milza_x3g, milza_y3g, milza3g, drei, acht, zehn, drei3, screen, shop_slot_5_var_rareg, shop_slot_5_rarg, goldg = spawn_Pokemon5_commong(Spawning_milza1g, Spawning_milza2g, Spawning_milza3g, Spawning_maxax1g, milza_x1g, milza_y1g, milza1g, milza_x2g, milza_y2g, milza2g, milza_x3g, milza_y3g, milza3g, drei, acht, zehn, drei3, screen, shop_slot_5_var_rareg, shop_slot_5_rarg, goldg)

  Spawning_ganovil1g, Spawning_ganovil2g, Spawning_ganovil3g, Spawning_rabigator1g, ganovil_x1g, ganovil_y1g, ganovil1g, ganovil_x2g, ganovil_y2g, ganovil2g, ganovil_x3g, ganovil_y3g, ganovil3g, eins, zehn, elf, vier4, screen, shop_slot_5_var_epicg, shop_slot_5_rarg, goldg = spawn_Pokemon5_commong(Spawning_ganovil1g, Spawning_ganovil2g, Spawning_ganovil3g, Spawning_rabigator1g, ganovil_x1g, ganovil_y1g, ganovil1g, ganovil_x2g, ganovil_y2g, ganovil2g, ganovil_x3g, ganovil_y3g, ganovil3g, eins, zehn, elf, vier4, screen, shop_slot_5_var_epicg, shop_slot_5_rarg, goldg)

  Spawning_rotomurf1g, Spawning_rotomurf2g, Spawning_rotomurf3g, Spawning_stalobor21g, rotomurf_x1g, rotomurf_y1g, rotomurf1g, rotomurf_x2g, rotomurf_y2g, rotomurf2g, rotomurf_x3g, rotomurf_y3g, rotomurf3g, zwei, zehn, elf, vier4, screen, shop_slot_5_var_epicg, shop_slot_5_rarg, goldg = spawn_Pokemon5_commong(Spawning_rotomurf1g, Spawning_rotomurf2g, Spawning_rotomurf3g, Spawning_stalobor21g, rotomurf_x1g, rotomurf_y1g, rotomurf1g, rotomurf_x2g, rotomurf_y2g, rotomurf2g, rotomurf_x3g, rotomurf_y3g, rotomurf3g, zwei, zehn, elf, vier4, screen, shop_slot_5_var_epicg, shop_slot_5_rarg, goldg)

  Spawning_makabaja1g, Spawning_makabaja2g, Spawning_makabaja3g, Spawning_echnatoll21g, makabaja_x1g, makabaja_y1g, makabaja1g, makabaja_x2g, makabaja_y2g, makabaja2g, makabaja_x3g, makabaja_y3g, makabaja3g, drei, zehn, elf, vier4, screen, shop_slot_5_var_epicg, shop_slot_5_rarg, goldg = spawn_Pokemon5_commong(Spawning_makabaja1g, Spawning_makabaja2g, Spawning_makabaja3g, Spawning_echnatoll21g, makabaja_x1g, makabaja_y1g, makabaja1g, makabaja_x2g, makabaja_y2g, makabaja2g, makabaja_x3g, makabaja_y3g, makabaja3g, drei, zehn, elf, vier4, screen, shop_slot_5_var_epicg, shop_slot_5_rarg, goldg)




  'Droppen eines Pokemon'


  serpifeu_x1g, serpifeu_y1g = drop_Pokemon_benchg(serpifeu_x1g, serpifeu_y1g)
  serpifeu_x2g, serpifeu_y2g = drop_Pokemon_benchg(serpifeu_x2g, serpifeu_y2g)
  serpifeu_x3g, serpifeu_y3g = drop_Pokemon_benchg(serpifeu_x3g, serpifeu_y3g)
  efoserp_x1g, efoserp_y1g = drop_Pokemon_benchg(efoserp_x1g, efoserp_y1g)
  efoserp_x2g, efoserp_y2g = drop_Pokemon_benchg(efoserp_x2g, efoserp_y2g)
  efoserp_x3g, efoserp_y3g = drop_Pokemon_benchg(efoserp_x3g, efoserp_y3g)
  serpiroyal_x1g, serpiroyal_y1g = drop_Pokemon_benchg(serpiroyal_x1g, serpiroyal_y1g)

  floink_x1g, floink_y1g = drop_Pokemon_benchg(floink_x1g, floink_y1g)
  floink_x2g, floink_y2g = drop_Pokemon_benchg(floink_x2g, floink_y2g)
  floink_x3g, floink_y3g = drop_Pokemon_benchg(floink_x3g, floink_y3g)
  ferkokel_x1g, ferkokel_y1g = drop_Pokemon_benchg(ferkokel_x1g, ferkokel_y1g)
  ferkokel_x2g, ferkokel_y2g = drop_Pokemon_benchg(ferkokel_x2g, ferkokel_y2g)
  ferkokel_x3g, ferkokel_y3g = drop_Pokemon_benchg(ferkokel_x3g, ferkokel_y3g)
  flambirex_x1g, flambirex_y1g = drop_Pokemon_benchg(flambirex_x1g, flambirex_y1g)

  ottaro_x1g, ottaro_y1g = drop_Pokemon_benchg(ottaro_x1g, ottaro_y1g)
  ottaro_x2g, ottaro_y2g = drop_Pokemon_benchg(ottaro_x2g, ottaro_y2g)
  ottaro_x3g, ottaro_y3g = drop_Pokemon_benchg(ottaro_x3g, ottaro_y3g)
  zwottronin_x1g, zwottronin_y1g = drop_Pokemon_benchg(zwottronin_x1g, zwottronin_y1g)
  zwottronin_x2g, zwottronin_y2g = drop_Pokemon_benchg(zwottronin_x2g, zwottronin_y2g)
  zwottronin_x3g, zwottronin_y3g = drop_Pokemon_benchg(zwottronin_x3g, zwottronin_y3g)
  admurai_x1g, admurai_y1g = drop_Pokemon_benchg(admurai_x1g, admurai_y1g)

  strawickl_x1g, strawickl_y1g = drop_Pokemon_benchg(strawickl_x1g, strawickl_y1g)
  strawickl_x2g, strawickl_y2g = drop_Pokemon_benchg(strawickl_x2g, strawickl_y2g)
  strawickl_x3g, strawickl_y3g = drop_Pokemon_benchg(strawickl_x3g, strawickl_y3g)
  folikon_x1g, folikon_y1g = drop_Pokemon_benchg(folikon_x1g, folikon_y1g)
  folikon_x2g, folikon_y2g = drop_Pokemon_benchg(folikon_x2g, folikon_y2g)
  folikon_x3g, folikon_y3g = drop_Pokemon_benchg(folikon_x3g, folikon_y3g)
  matrifol_x1g, matrifol_y1g = drop_Pokemon_benchg(matrifol_x1g, matrifol_y1g)

  toxiped_x1g, toxiped_y1g = drop_Pokemon_benchg(toxiped_x1g, toxiped_y1g)
  toxiped_x2g, toxiped_y2g = drop_Pokemon_benchg(toxiped_x2g, toxiped_y2g)
  toxiped_x3g, toxiped_y3g = drop_Pokemon_benchg(toxiped_x3g, toxiped_y3g)
  rollum_x1g, rollum_y1g = drop_Pokemon_benchg(rollum_x1g, rollum_y1g)
  rollum_x2g, rollum_y2g = drop_Pokemon_benchg(rollum_x2g, rollum_y2g)
  rollum_x3g, rollum_y3g = drop_Pokemon_benchg(rollum_x3g, rollum_y3g)
  cerapendra_x1g, cerapendra_y1g = drop_Pokemon_benchg(cerapendra_x1g, cerapendra_y1g)

  praktibalk_x1g, praktibalk_y1g = drop_Pokemon_benchg(praktibalk_x1g, praktibalk_y1g)
  praktibalk_x2g, praktibalk_y2g = drop_Pokemon_benchg(praktibalk_x2g, praktibalk_y2g)
  praktibalk_x3g, praktibalk_y3g = drop_Pokemon_benchg(praktibalk_x3g, praktibalk_y3g)
  strepoli_x1g, strepoli_y1g = drop_Pokemon_benchg(strepoli_x1g, strepoli_y1g)
  strepoli_x2g, strepoli_y2g = drop_Pokemon_benchg(strepoli_x2g, strepoli_y2g)
  strepoli_x3g, strepoli_y3g = drop_Pokemon_benchg(strepoli_x3g, strepoli_y3g)
  meistagrif_x1g, meistagrif_y1g = drop_Pokemon_benchg(meistagrif_x1g, meistagrif_y1g)

  klikk_x1g, klikk_y1g = drop_Pokemon_benchg(klikk_x1g, klikk_y1g)
  klikk_x2g, klikk_y2g = drop_Pokemon_benchg(klikk_x2g, klikk_y2g)
  klikk_x3g, klikk_y3g = drop_Pokemon_benchg(klikk_x3g, klikk_y3g)
  kliklak_x1g, kliklak_y1g = drop_Pokemon_benchg(kliklak_x1g, kliklak_y1g)
  kliklak_x2g, kliklak_y2g = drop_Pokemon_benchg(kliklak_x2g, kliklak_y2g)
  kliklak_x3g, kliklak_y3g = drop_Pokemon_benchg(kliklak_x3g, kliklak_y3g)
  klikdiklak_x1g, klikdiklak_y1g = drop_Pokemon_benchg(klikdiklak_x1g, klikdiklak_y1g)

  kiesling_x1g, kiesling_y1g = drop_Pokemon_benchg(kiesling_x1g, kiesling_y1g)
  kiesling_x2g, kiesling_y2g = drop_Pokemon_benchg(kiesling_x2g, kiesling_y2g)
  kiesling_x3g, kiesling_y3g = drop_Pokemon_benchg(kiesling_x3g, kiesling_y3g)
  sedimantur_x1g, sedimantur_y1g = drop_Pokemon_benchg(sedimantur_x1g, sedimantur_y1g)
  sedimantur_x2g, sedimantur_y2g = drop_Pokemon_benchg(sedimantur_x2g, sedimantur_y2g)
  sedimantur_x3g, sedimantur_y3g = drop_Pokemon_benchg(sedimantur_x3g, sedimantur_y3g)
  brokkolos_x1g, brokkolos_y1g = drop_Pokemon_benchg(brokkolos_x1g, brokkolos_y1g)

  milza_x1g, milza_y1g = drop_Pokemon_benchg(milza_x1g, milza_y1g)
  milza_x2g, milza_y2g = drop_Pokemon_benchg(milza_x2g, milza_y2g)
  milza_x3g, milza_y3g = drop_Pokemon_benchg(milza_x3g, milza_y3g)
  sharfax_x1g, sharfax_y1g = drop_Pokemon_benchg(sharfax_x1g, sharfax_y1g)
  sharfax_x2g, sharfax_y2g = drop_Pokemon_benchg(sharfax_x2g, sharfax_y2g)
  sharfax_x3g, sharfax_y3g = drop_Pokemon_benchg(sharfax_x3g, sharfax_y3g)
  maxax_x1g, maxax_y1g = drop_Pokemon_benchg(maxax_x1g, maxax_y1g)

  ganovil_x1g, ganovil_y1g = drop_Pokemon_benchg(ganovil_x1g, ganovil_y1g)
  ganovil_x2g, ganovil_y2g = drop_Pokemon_benchg(ganovil_x2g, ganovil_y2g)
  ganovil_x3g, ganovil_y3g = drop_Pokemon_benchg(ganovil_x3g, ganovil_y3g)
  rokkaiman_x1g, rokkaiman_y1g = drop_Pokemon_benchg(rokkaiman_x1g, rokkaiman_y1g)
  rokkaiman_x2g, rokkaiman_y2g = drop_Pokemon_benchg(rokkaiman_x2g, rokkaiman_y2g)
  rokkaiman_x3g, rokkaiman_y3g = drop_Pokemon_benchg(rokkaiman_x3g, rokkaiman_y3g)
  rabigator_x1g, rabigator_y1g = drop_Pokemon_benchg(rabigator_x1g, rabigator_y1g)

  rotomurf_x1g, rotomurf_y1g = drop_Pokemon_benchg(rotomurf_x1g, rotomurf_y1g)
  rotomurf_x2g, rotomurf_y2g = drop_Pokemon_benchg(rotomurf_x2g, rotomurf_y2g)
  rotomurf_x3g, rotomurf_y3g = drop_Pokemon_benchg(rotomurf_x3g, rotomurf_y3g)
  stalobor_x1g, stalobor_y1g = drop_Pokemon_benchg(stalobor_x1g, stalobor_y1g)
  stalobor_x2g, stalobor_y2g = drop_Pokemon_benchg(stalobor_x2g, stalobor_y2g)
  stalobor_x3g, stalobor_y3g = drop_Pokemon_benchg(stalobor_x3g, stalobor_y3g)
  stalobor2_x1g, stalobor2_y1g = drop_Pokemon_benchg(stalobor2_x1g, stalobor2_y1g)

  makabaja_x1g, makabaja_y1g = drop_Pokemon_benchg(makabaja_x1g, makabaja_y1g)
  makabaja_x2g, makabaja_y2g = drop_Pokemon_benchg(makabaja_x2g, makabaja_y2g)
  makabaja_x3g, makabaja_y3g = drop_Pokemon_benchg(makabaja_x3g, makabaja_y3g)
  echnatoll_x1g, echnatoll_y1g = drop_Pokemon_benchg(echnatoll_x1g, echnatoll_y1g)
  echnatoll_x2g, echnatoll_y2g = drop_Pokemon_benchg(echnatoll_x2g, echnatoll_y2g)
  echnatoll_x3g, echnatoll_y3g = drop_Pokemon_benchg(echnatoll_x3g, echnatoll_y3g)
  echnatoll2_x1g, echnatoll2_y1g = drop_Pokemon_benchg(echnatoll2_x1g, echnatoll2_y1g)
  


  serpifeu_x1g, serpifeu_y1g = drop_Pokemon_arenag(serpifeu_x1g, serpifeu_y1g)
  serpifeu_x2g, serpifeu_y2g = drop_Pokemon_arenag(serpifeu_x2g, serpifeu_y2g)
  serpifeu_x3g, serpifeu_y3g = drop_Pokemon_arenag(serpifeu_x3g, serpifeu_y3g)
  efoserp_x1g, efoserp_y1g = drop_Pokemon_arenag(efoserp_x1g, efoserp_y1g)
  efoserp_x2g, efoserp_y2g = drop_Pokemon_arenag(efoserp_x2g, efoserp_y2g)
  efoserp_x3g, efoserp_y3g = drop_Pokemon_arenag(efoserp_x3g, efoserp_y3g)
  serpiroyal_x1g, serpiroyal_y1g = drop_Pokemon_arenag(serpiroyal_x1g, serpiroyal_y1g)

  floink_x1g, floink_y1g = drop_Pokemon_arenag(floink_x1g, floink_y1g)
  floink_x2g, floink_y2g = drop_Pokemon_arenag(floink_x2g, floink_y2g)
  floink_x3g, floink_y3g = drop_Pokemon_arenag(floink_x3g, floink_y3g)
  ferkokel_x1g, ferkokel_y1g = drop_Pokemon_arenag(ferkokel_x1g, ferkokel_y1g)
  ferkokel_x2g, ferkokel_y2g = drop_Pokemon_arenag(ferkokel_x2g, ferkokel_y2g)
  ferkokel_x3g, ferkokel_y3g = drop_Pokemon_arenag(ferkokel_x3g, ferkokel_y3g)
  flambirex_x1g, flambirex_y1g = drop_Pokemon_arenag(flambirex_x1g, flambirex_y1g)

  ottaro_x1g, ottaro_y1g = drop_Pokemon_arenag(ottaro_x1g, ottaro_y1g)
  ottaro_x2g, ottaro_y2g = drop_Pokemon_arenag(ottaro_x2g, ottaro_y2g)
  ottaro_x3g, ottaro_y3g = drop_Pokemon_arenag(ottaro_x3g, ottaro_y3g)
  zwottronin_x1g, zwottronin_y1g = drop_Pokemon_arenag(zwottronin_x1g, zwottronin_y1g)
  zwottronin_x2g, zwottronin_y2g = drop_Pokemon_arenag(zwottronin_x2g, zwottronin_y2g)
  zwottronin_x3g, zwottronin_y3g = drop_Pokemon_arenag(zwottronin_x3g, zwottronin_y3g)
  admurai_x1g, admurai_y1g = drop_Pokemon_arenag(admurai_x1g, admurai_y1g)

  strawickl_x1g, strawickl_y1g = drop_Pokemon_arenag(strawickl_x1g, strawickl_y1g)
  strawickl_x2g, strawickl_y2g = drop_Pokemon_arenag(strawickl_x2g, strawickl_y2g)
  strawickl_x3g, strawickl_y3g = drop_Pokemon_arenag(strawickl_x3g, strawickl_y3g)
  folikon_x1g, folikon_y1g = drop_Pokemon_arenag(folikon_x1g, folikon_y1g)
  folikon_x2g, folikon_y2g = drop_Pokemon_arenag(folikon_x2g, folikon_y2g)
  folikon_x3g, folikon_y3g = drop_Pokemon_arenag(folikon_x3g, folikon_y3g)
  matrifol_x1g, matrifol_y1g = drop_Pokemon_arenag(matrifol_x1g, matrifol_y1g)

  toxiped_x1g, toxiped_y1g = drop_Pokemon_arenag(toxiped_x1g, toxiped_y1g)
  toxiped_x2g, toxiped_y2g = drop_Pokemon_arenag(toxiped_x2g, toxiped_y2g)
  toxiped_x3g, toxiped_y3g = drop_Pokemon_arenag(toxiped_x3g, toxiped_y3g)
  rollum_x1g, rollum_y1g = drop_Pokemon_arenag(rollum_x1g, rollum_y1g)
  rollum_x2g, rollum_y2g = drop_Pokemon_arenag(rollum_x2g, rollum_y2g)
  rollum_x3g, rollum_y3g = drop_Pokemon_arenag(rollum_x3g, rollum_y3g)
  cerapendra_x1g, cerapendra_y1g = drop_Pokemon_arenag(cerapendra_x1g, cerapendra_y1g)

  praktibalk_x1g, praktibalk_y1g = drop_Pokemon_arenag(praktibalk_x1g, praktibalk_y1g)
  praktibalk_x2g, praktibalk_y2g = drop_Pokemon_arenag(praktibalk_x2g, praktibalk_y2g)
  praktibalk_x3g, praktibalk_y3g = drop_Pokemon_arenag(praktibalk_x3g, praktibalk_y3g)
  strepoli_x1g, strepoli_y1g = drop_Pokemon_arenag(strepoli_x1g, strepoli_y1g)
  strepoli_x2g, strepoli_y2g = drop_Pokemon_arenag(strepoli_x2g, strepoli_y2g)
  strepoli_x3g, strepoli_y3g = drop_Pokemon_arenag(strepoli_x3g, strepoli_y3g)
  meistagrif_x1g, meistagrif_y1g = drop_Pokemon_arenag(meistagrif_x1g, meistagrif_y1g)

  klikk_x1g, klikk_y1g = drop_Pokemon_arenag(klikk_x1g, klikk_y1g)
  klikk_x2g, klikk_y2g = drop_Pokemon_arenag(klikk_x2g, klikk_y2g)
  klikk_x3g, klikk_y3g = drop_Pokemon_arenag(klikk_x3g, klikk_y3g)
  kliklak_x1g, kliklak_y1g = drop_Pokemon_arenag(kliklak_x1g, kliklak_y1g)
  kliklak_x2g, kliklak_y2g = drop_Pokemon_arenag(kliklak_x2g, kliklak_y2g)
  kliklak_x3g, kliklak_y3g = drop_Pokemon_arenag(kliklak_x3g, kliklak_y3g)
  klikdiklak_x1g, klikdiklak_y1g = drop_Pokemon_arenag(klikdiklak_x1g, klikdiklak_y1g)

  kiesling_x1g, kiesling_y1g = drop_Pokemon_arenag(kiesling_x1g, kiesling_y1g)
  kiesling_x2g, kiesling_y2g = drop_Pokemon_arenag(kiesling_x2g, kiesling_y2g)
  kiesling_x3g, kiesling_y3g = drop_Pokemon_arenag(kiesling_x3g, kiesling_y3g)
  sedimantur_x1g, sedimantur_y1g = drop_Pokemon_arenag(sedimantur_x1g, sedimantur_y1g)
  sedimantur_x2g, sedimantur_y2g = drop_Pokemon_arenag(sedimantur_x2g, sedimantur_y2g)
  sedimantur_x3g, sedimantur_y3g = drop_Pokemon_arenag(sedimantur_x3g, sedimantur_y3g)
  brokkolos_x1g, brokkolos_y1g = drop_Pokemon_arenag(brokkolos_x1g, brokkolos_y1g)

  milza_x1g, milza_y1g = drop_Pokemon_arenag(milza_x1g, milza_y1g)
  milza_x2g, milza_y2g = drop_Pokemon_arenag(milza_x2g, milza_y2g)
  milza_x3g, milza_y3g = drop_Pokemon_arenag(milza_x3g, milza_y3g)
  sharfax_x1g, sharfax_y1g = drop_Pokemon_arenag(sharfax_x1g, sharfax_y1g)
  sharfax_x2g, sharfax_y2g = drop_Pokemon_arenag(sharfax_x2g, sharfax_y2g)
  sharfax_x3g, sharfax_y3g = drop_Pokemon_arenag(sharfax_x3g, sharfax_y3g)
  maxax_x1g, maxax_y1g = drop_Pokemon_arenag(maxax_x1g, maxax_y1g)

  ganovil_x1g, ganovil_y1g = drop_Pokemon_arenag(ganovil_x1g, ganovil_y1g)
  ganovil_x2g, ganovil_y2g = drop_Pokemon_arenag(ganovil_x2g, ganovil_y2g)
  ganovil_x3g, ganovil_y3g = drop_Pokemon_arenag(ganovil_x3g, ganovil_y3g)
  rokkaiman_x1g, rokkaiman_y1g = drop_Pokemon_arenag(rokkaiman_x1g, rokkaiman_y1g)
  rokkaiman_x2g, rokkaiman_y2g = drop_Pokemon_arenag(rokkaiman_x2g, rokkaiman_y2g)
  rokkaiman_x3g, rokkaiman_y3g = drop_Pokemon_arenag(rokkaiman_x3g, rokkaiman_y3g)
  rabigator_x1g, rabigator_y1g = drop_Pokemon_arenag(rabigator_x1g, rabigator_y1g)

  rotomurf_x1g, rotomurf_y1g = drop_Pokemon_arenag(rotomurf_x1g, rotomurf_y1g)
  rotomurf_x2g, rotomurf_y2g = drop_Pokemon_arenag(rotomurf_x2g, rotomurf_y2g)
  rotomurf_x3g, rotomurf_y3g = drop_Pokemon_arenag(rotomurf_x3g, rotomurf_y3g)
  stalobor_x1g, stalobor_y1g = drop_Pokemon_arenag(stalobor_x1g, stalobor_y1g)
  stalobor_x2g, stalobor_y2g = drop_Pokemon_arenag(stalobor_x2g, stalobor_y2g)
  stalobor_x3g, stalobor_y3g = drop_Pokemon_arenag(stalobor_x3g, stalobor_y3g)
  stalobor2_x1g, stalobor2_y1g = drop_Pokemon_arenag(stalobor2_x1g, stalobor2_y1g)

  makabaja_x1g, makabaja_y1g = drop_Pokemon_arenag(makabaja_x1g, makabaja_y1g)
  makabaja_x2g, makabaja_y2g = drop_Pokemon_arenag(makabaja_x2g, makabaja_y2g)
  makabaja_x3g, makabaja_y3g = drop_Pokemon_arenag(makabaja_x3g, makabaja_y3g)
  echnatoll_x1g, echnatoll_y1g = drop_Pokemon_arenag(echnatoll_x1g, echnatoll_y1g)
  echnatoll_x2g, echnatoll_y2g = drop_Pokemon_arenag(echnatoll_x2g, echnatoll_y2g)
  echnatoll_x3g, echnatoll_y3g = drop_Pokemon_arenag(echnatoll_x3g, echnatoll_y3g)
  echnatoll2_x1g, echnatoll2_y1g = drop_Pokemon_arenag(echnatoll2_x1g, echnatoll2_y1g)

  

  'Bewegen eines Pokemon'

  serpifeu_x1g, serpifeu_y1g = move_Pokemon(serpifeu_x1g, serpifeu_y1g)
  serpifeu_x2g, serpifeu_y2g = move_Pokemon(serpifeu_x2g, serpifeu_y2g)
  serpifeu_x3g, serpifeu_y3g = move_Pokemon(serpifeu_x3g, serpifeu_y3g)
  efoserp_x1g, efoserp_y1g = move_Pokemon(efoserp_x1g, efoserp_y1g)
  efoserp_x2g, efoserp_y2g = move_Pokemon(efoserp_x2g, efoserp_y2g)
  efoserp_x3g, efoserp_y3g = move_Pokemon(efoserp_x3g, efoserp_y3g)
  serpiroyal_x1g, serpiroyal_y1g = move_Pokemon(serpiroyal_x1g, serpiroyal_y1g)

  floink_x1g, floink_y1g = move_Pokemon(floink_x1g, floink_y1g)
  floink_x2g, floink_y2g = move_Pokemon(floink_x2g, floink_y2g)
  floink_x3g, floink_y3g = move_Pokemon(floink_x3g, floink_y3g)
  ferkokel_x1g, ferkokel_y1g = move_Pokemon(ferkokel_x1g, ferkokel_y1g)
  ferkokel_x2g, ferkokel_y2g = move_Pokemon(ferkokel_x2g, ferkokel_y2g)
  ferkokel_x3g, ferkokel_y3g = move_Pokemon(ferkokel_x3g, ferkokel_y3g)
  flambirex_x1g, flambirex_y1g = move_Pokemon(flambirex_x1g, flambirex_y1g)

  ottaro_x1g, ottaro_y1g = move_Pokemon(ottaro_x1g, ottaro_y1g)
  ottaro_x2g, ottaro_y2g = move_Pokemon(ottaro_x2g, ottaro_y2g)
  ottaro_x3g, ottaro_y3g = move_Pokemon(ottaro_x3g, ottaro_y3g)
  zwottronin_x1g, zwottronin_y1g = move_Pokemon(zwottronin_x1g, zwottronin_y1g)
  zwottronin_x2g, zwottronin_y2g = move_Pokemon(zwottronin_x2g, zwottronin_y2g)
  zwottronin_x3g, zwottronin_y3g = move_Pokemon(zwottronin_x3g, zwottronin_y3g)
  admurai_x1g, admurai_y1g = move_Pokemon(admurai_x1g, admurai_y1g)

  strawickl_x1g, strawickl_y1g = move_Pokemon(strawickl_x1g, strawickl_y1g)
  strawickl_x2g, strawickl_y2g = move_Pokemon(strawickl_x2g, strawickl_y2g)
  strawickl_x3g, strawickl_y3g = move_Pokemon(strawickl_x3g, strawickl_y3g)
  folikon_x1g, folikon_y1g = move_Pokemon(folikon_x1g, folikon_y1g)
  folikon_x2g, folikon_y2g = move_Pokemon(folikon_x2g, folikon_y2g)
  folikon_x3g, folikon_y3g = move_Pokemon(folikon_x3g, folikon_y3g)
  matrifol_x1g, matrifol_y1g = move_Pokemon(matrifol_x1g, matrifol_y1g)

  toxiped_x1g, toxiped_y1g = move_Pokemon(toxiped_x1g, toxiped_y1g)
  toxiped_x2g, toxiped_y2g = move_Pokemon(toxiped_x2g, toxiped_y2g)
  toxiped_x3g, toxiped_y3g = move_Pokemon(toxiped_x3g, toxiped_y3g)
  rollum_x1g, rollum_y1g = move_Pokemon(rollum_x1g, rollum_y1g)
  rollum_x2g, rollum_y2g = move_Pokemon(rollum_x2g, rollum_y2g)
  rollum_x3g, rollum_y3g = move_Pokemon(rollum_x3g, rollum_y3g)
  cerapendra_x1g, cerapendra_y1g = move_Pokemon(cerapendra_x1g, cerapendra_y1g)

  praktibalk_x1g, praktibalk_y1g = move_Pokemon(praktibalk_x1g, praktibalk_y1g)
  praktibalk_x2g, praktibalk_y2g = move_Pokemon(praktibalk_x2g, praktibalk_y2g)
  praktibalk_x3g, praktibalk_y3g = move_Pokemon(praktibalk_x3g, praktibalk_y3g)
  strepoli_x1g, strepoli_y1g = move_Pokemon(strepoli_x1g, strepoli_y1g)
  strepoli_x2g, strepoli_y2g = move_Pokemon(strepoli_x2g, strepoli_y2g)
  strepoli_x3g, strepoli_y3g = move_Pokemon(strepoli_x3g, strepoli_y3g)
  meistagrif_x1g, meistagrif_y1g = move_Pokemon(meistagrif_x1g, meistagrif_y1g)

  klikk_x1g, klikk_y1g = move_Pokemon(klikk_x1g, klikk_y1g)
  klikk_x2g, klikk_y2g = move_Pokemon(klikk_x2g, klikk_y2g)
  klikk_x3g, klikk_y3g = move_Pokemon(klikk_x3g, klikk_y3g)
  kliklak_x1g, kliklak_y1g = move_Pokemon(kliklak_x1g, kliklak_y1g)
  kliklak_x2g, kliklak_y2g = move_Pokemon(kliklak_x2g, kliklak_y2g)
  kliklak_x3g, kliklak_y3g = move_Pokemon(kliklak_x3g, kliklak_y3g)
  klikdiklak_x1g, klikdiklak_y1g = move_Pokemon(klikdiklak_x1g, klikdiklak_y1g)

  kiesling_x1g, kiesling_y1g = move_Pokemon(kiesling_x1g, kiesling_y1g)
  kiesling_x2g, kiesling_y2g = move_Pokemon(kiesling_x2g, kiesling_y2g)
  kiesling_x3g, kiesling_y3g = move_Pokemon(kiesling_x3g, kiesling_y3g)
  sedimantur_x1g, sedimantur_y1g = move_Pokemon(sedimantur_x1g, sedimantur_y1g)
  sedimantur_x2g, sedimantur_y2g = move_Pokemon(sedimantur_x2g, sedimantur_y2g)
  sedimantur_x3g, sedimantur_y3g = move_Pokemon(sedimantur_x3g, sedimantur_y3g)
  brokkolos_x1g, brokkolos_y1g = move_Pokemon(brokkolos_x1g, brokkolos_y1g)

  milza_x1g, milza_y1g = move_Pokemon(milza_x1g, milza_y1g)
  milza_x2g, milza_y2g = move_Pokemon(milza_x2g, milza_y2g)
  milza_x3g, milza_y3g = move_Pokemon(milza_x3g, milza_y3g)
  sharfax_x1g, sharfax_y1g = move_Pokemon(sharfax_x1g, sharfax_y1g)
  sharfax_x2g, sharfax_y2g = move_Pokemon(sharfax_x2g, sharfax_y2g)
  sharfax_x3g, sharfax_y3g = move_Pokemon(sharfax_x3g, sharfax_y3g)
  maxax_x1g, maxax_y1g = move_Pokemon(maxax_x1g, maxax_y1g)

  ganovil_x1g, ganovil_y1g = move_Pokemon(ganovil_x1g, ganovil_y1g)
  ganovil_x2g, ganovil_y2g = move_Pokemon(ganovil_x2g, ganovil_y2g)
  ganovil_x3g, ganovil_y3g = move_Pokemon(ganovil_x3g, ganovil_y3g)
  rokkaiman_x1g, rokkaiman_y1g = move_Pokemon(rokkaiman_x1g, rokkaiman_y1g)
  rokkaiman_x2g, rokkaiman_y2g = move_Pokemon(rokkaiman_x2g, rokkaiman_y2g)
  rokkaiman_x3g, rokkaiman_y3g = move_Pokemon(rokkaiman_x3g, rokkaiman_y3g)
  rabigator_x1g, rabigator_y1g = move_Pokemon(rabigator_x1g, rabigator_y1g)

  rotomurf_x1g, rotomurf_y1g = move_Pokemon(rotomurf_x1g, rotomurf_y1g)
  rotomurf_x2g, rotomurf_y2g = move_Pokemon(rotomurf_x2g, rotomurf_y2g)
  rotomurf_x3g, rotomurf_y3g = move_Pokemon(rotomurf_x3g, rotomurf_y3g)
  stalobor_x1g, stalobor_y1g = move_Pokemon(stalobor_x1g, stalobor_y1g)
  stalobor_x2g, stalobor_y2g = move_Pokemon(stalobor_x2g, stalobor_y2g)
  stalobor_x3g, stalobor_y3g = move_Pokemon(stalobor_x3g, stalobor_y3g)
  stalobor2_x1g, stalobor2_y1g = move_Pokemon(stalobor2_x1g, stalobor2_y1g)

  makabaja_x1g, makabaja_y1g = move_Pokemon(makabaja_x1g, makabaja_y1g)
  makabaja_x2g, makabaja_y2g = move_Pokemon(makabaja_x2g, makabaja_y2g)
  makabaja_x3g, makabaja_y3g = move_Pokemon(makabaja_x3g, makabaja_y3g)
  echnatoll_x1g, echnatoll_y1g = move_Pokemon(echnatoll_x1g, echnatoll_y1g)
  echnatoll_x2g, echnatoll_y2g = move_Pokemon(echnatoll_x2g, echnatoll_y2g)
  echnatoll_x3g, echnatoll_y3g = move_Pokemon(echnatoll_x3g, echnatoll_y3g)
  echnatoll2_x1g, echnatoll2_y1g = move_Pokemon(echnatoll2_x1g, echnatoll2_y1g)
  
  'Entwickeln eines Pokemon'
  
  'Erste Entwicklung'

  Spawning_serpifeu1g, Spawning_serpifeu2g, Spawning_serpifeu3g, Spawning_efoserp1g, Spawning_efoserp2g, Spawning_efoserp3g, Spawning_serpiroyal1g, efoserp_x1g, efoserp_x2g, efoserp_x3g, serpifeu_x1g, serpifeu_x2g, serpifeu_x3g, efoserp_y1g, efoserp_y2g, efoserp_y3g, serpifeu_y1g, serpifeu_y2g, serpifeu_y3g, efoserp1g, efoserp2g, efoserp3g, eins, zwei, drei, zwei, screen=evolve_Pokemon1(Spawning_serpifeu1g, Spawning_serpifeu2g, Spawning_serpifeu3g, Spawning_efoserp1g, Spawning_efoserp2g, Spawning_efoserp3g, Spawning_serpiroyal1g, efoserp_x1g, efoserp_x2g, efoserp_x3g, serpifeu_x1g, serpifeu_x2g, serpifeu_x3g, efoserp_y1g, efoserp_y2g, efoserp_y3g, serpifeu_y1g, serpifeu_y2g, serpifeu_y3g, efoserp1g, efoserp2g, efoserp3g, eins, zwei, drei, zwei, screen)

  Spawning_floink1g, Spawning_floink2g, Spawning_floink3g, Spawning_ferkokel1g, Spawning_ferkokel2g, Spawning_ferkokel3g, Spawning_flambirex1g, ferkokel_x1g, ferkokel_x2g, ferkokel_x3g, floink_x1g, floink_x2g, floink_x3g, ferkokel_y1g, ferkokel_y2g, ferkokel_y3g, floink_y1g, floink_y2g, floink_y3g, ferkokel1g, ferkokel2g, ferkokel3g, acht, neun, zehn, zwei, screen=evolve_Pokemon1(Spawning_floink1g, Spawning_floink2g, Spawning_floink3g, Spawning_ferkokel1g, Spawning_ferkokel2g, Spawning_ferkokel3g, Spawning_flambirex1g, ferkokel_x1g, ferkokel_x2g, ferkokel_x3g, floink_x1g, floink_x2g, floink_x3g, ferkokel_y1g, ferkokel_y2g, ferkokel_y3g, floink_y1g, floink_y2g, floink_y3g, ferkokel1g, ferkokel2g, ferkokel3g, acht, neun, zehn, zwei, screen)

  Spawning_ottaro1g, Spawning_ottaro2g, Spawning_ottaro3g, Spawning_zwottronin1g, Spawning_zwottronin2g, Spawning_zwottronin3g, Spawning_admurai1g, zwottronin_x1g, zwottronin_x2g, zwottronin_x3g, ottaro_x1g, ottaro_x2g, ottaro_x3g, zwottronin_y1g, zwottronin_y2g, zwottronin_y3g, ottaro_y1g, ottaro_y2g, ottaro_y3g, zwottronin1g, zwottronin2g, zwottronin3g, fünfzehn, sechzehn, siebzehn, zwei, screen=evolve_Pokemon1(Spawning_ottaro1g, Spawning_ottaro2g, Spawning_ottaro3g, Spawning_zwottronin1g, Spawning_zwottronin2g, Spawning_zwottronin3g, Spawning_admurai1g, zwottronin_x1g, zwottronin_x2g, zwottronin_x3g, ottaro_x1g, ottaro_x2g, ottaro_x3g, zwottronin_y1g, zwottronin_y2g, zwottronin_y3g, ottaro_y1g, ottaro_y2g, ottaro_y3g, zwottronin1g, zwottronin2g, zwottronin3g, fünfzehn, sechzehn, siebzehn, zwei, screen)

  Spawning_strawickl1g, Spawning_strawickl2g, Spawning_strawickl3g, Spawning_folikon1g, Spawning_folikon2g, Spawning_folikon3g, Spawning_matrifol1g, folikon_x1g, folikon_x2g, folikon_x3g, strawickl_x1g, strawickl_x2g, strawickl_x3g, folikon_y1g, folikon_y2g, folikon_y3g, strawickl_y1g, strawickl_y2g, strawickl_y3g, folikon1g, folikon2g, folikon3g, zweiundzwanzig, dreiundzwanzig, vierundzwanzig, zwei, screen=evolve_Pokemon1(Spawning_strawickl1g, Spawning_strawickl2g, Spawning_strawickl3g, Spawning_folikon1g, Spawning_folikon2g, Spawning_folikon3g, Spawning_matrifol1g, folikon_x1g, folikon_x2g, folikon_x3g, strawickl_x1g, strawickl_x2g, strawickl_x3g, folikon_y1g, folikon_y2g, folikon_y3g, strawickl_y1g, strawickl_y2g, strawickl_y3g, folikon1g, folikon2g, folikon3g, zweiundzwanzig, dreiundzwanzig, vierundzwanzig, zwei, screen)

  Spawning_toxiped1g, Spawning_toxiped2g, Spawning_toxiped3g, Spawning_rollum1g, Spawning_rollum2g, Spawning_rollum3g, Spawning_cerapendra1g, rollum_x1g, rollum_x2g, rollum_x3g, toxiped_x1g, toxiped_x2g, toxiped_x3g, rollum_y1g, rollum_y2g, rollum_y3g, toxiped_y1g, toxiped_y2g, toxiped_y3g, rollum1g, rollum2g, rollum3g, neunundzwanzig, dreißig, einunddreißig, zwei, screen=evolve_Pokemon1(Spawning_toxiped1g, Spawning_toxiped2g, Spawning_toxiped3g, Spawning_rollum1g, Spawning_rollum2g, Spawning_rollum3g, Spawning_cerapendra1g, rollum_x1g, rollum_x2g, rollum_x3g, toxiped_x1g, toxiped_x2g, toxiped_x3g, rollum_y1g, rollum_y2g, rollum_y3g, toxiped_y1g, toxiped_y2g, toxiped_y3g, rollum1g, rollum2g, rollum3g, neunundzwanzig, dreißig, einunddreißig, zwei, screen)

  Spawning_praktibalk1g, Spawning_praktibalk2g, Spawning_praktibalk3g, Spawning_strepoli1g, Spawning_strepoli2g, Spawning_strepoli3g, Spawning_meistagrif1g, strepoli_x1g, strepoli_x2g, strepoli_x3g, praktibalk_x1g, praktibalk_x2g, praktibalk_x3g, strepoli_y1g, strepoli_y2g, strepoli_y3g, praktibalk_y1g, praktibalk_y2g, praktibalk_y3g, strepoli1g, strepoli2g, strepoli3g, sechsunddreißig, siebenunddreißig, achtunddreißig, zwei, screen=evolve_Pokemon1(Spawning_praktibalk1g, Spawning_praktibalk2g, Spawning_praktibalk3g, Spawning_strepoli1g, Spawning_strepoli2g, Spawning_strepoli3g, Spawning_meistagrif1g, strepoli_x1g, strepoli_x2g, strepoli_x3g, praktibalk_x1g, praktibalk_x2g, praktibalk_x3g, strepoli_y1g, strepoli_y2g, strepoli_y3g, praktibalk_y1g, praktibalk_y2g, praktibalk_y3g, strepoli1g, strepoli2g, strepoli3g, sechsunddreißig, siebenunddreißig, achtunddreißig, zwei, screen)

  Spawning_klikk1g, Spawning_klikk2g, Spawning_klikk3g, Spawning_kliklak1g, Spawning_kliklak2g, Spawning_kliklak3g, Spawning_klikdiklak1g, kliklak_x1g, kliklak_x2g, kliklak_x3g, klikk_x1g, klikk_x2g, klikk_x3g, kliklak_y1g, kliklak_y2g, kliklak_y3g, klikk_y1g, klikk_y2g, klikk_y3g, kliklak1g, kliklak2g, kliklak3g, dreiundvierzig, vierundvierzig, fünfundvierzig, zwei, screen=evolve_Pokemon1(Spawning_klikk1g, Spawning_klikk2g, Spawning_klikk3g, Spawning_kliklak1g, Spawning_kliklak2g, Spawning_kliklak3g, Spawning_klikdiklak1g, kliklak_x1g, kliklak_x2g, kliklak_x3g, klikk_x1g, klikk_x2g, klikk_x3g, kliklak_y1g, kliklak_y2g, kliklak_y3g, klikk_y1g, klikk_y2g, klikk_y3g, kliklak1g, kliklak2g, kliklak3g, dreiundvierzig, vierundvierzig, fünfundvierzig, zwei, screen)

  Spawning_kiesling1g, Spawning_kiesling2g, Spawning_kiesling3g, Spawning_sedimantur1g, Spawning_sedimantur2g, Spawning_sedimantur3g, Spawning_brokkolos1g, sedimantur_x1g, sedimantur_x2g, sedimantur_x3g, kiesling_x1g, kiesling_x2g, kiesling_x3g, sedimantur_y1g, sedimantur_y2g, sedimantur_y3g, kiesling_y1g, kiesling_y2g, kiesling_y3g, sedimantur1g, sedimantur2g, sedimantur3g, fünfzig, einundfünfzig, zweiundfünfzig, zwei, screen=evolve_Pokemon1(Spawning_kiesling1g, Spawning_kiesling2g, Spawning_kiesling3g, Spawning_sedimantur1g, Spawning_sedimantur2g, Spawning_sedimantur3g, Spawning_brokkolos1g, sedimantur_x1g, sedimantur_x2g, sedimantur_x3g, kiesling_x1g, kiesling_x2g, kiesling_x3g, sedimantur_y1g, sedimantur_y2g, sedimantur_y3g, kiesling_y1g, kiesling_y2g, kiesling_y3g, sedimantur1g, sedimantur2g, sedimantur3g, fünfzig, einundfünfzig, zweiundfünfzig, zwei, screen)

  Spawning_milza1g, Spawning_milza2g, Spawning_milza3g, Spawning_sharfax1g, Spawning_sharfax2g, Spawning_sharfax3g, Spawning_maxax1g, sharfax_x1g, sharfax_x2g, sharfax_x3g, milza_x1g, milza_x2g, milza_x3g, sharfax_y1g, sharfax_y2g, sharfax_y3g, milza_y1g, milza_y2g, milza_y3g, sharfax1g, sharfax2g, sharfax3g, siebenundfünfzig, achtundfünfzig, neunundfünfzig, zwei, screen=evolve_Pokemon1(Spawning_milza1g, Spawning_milza2g, Spawning_milza3g, Spawning_sharfax1g, Spawning_sharfax2g, Spawning_sharfax3g, Spawning_maxax1g, sharfax_x1g, sharfax_x2g, sharfax_x3g, milza_x1g, milza_x2g, milza_x3g, sharfax_y1g, sharfax_y2g, sharfax_y3g, milza_y1g, milza_y2g, milza_y3g, sharfax1g, sharfax2g, sharfax3g, siebenundfünfzig, achtundfünfzig, neunundfünfzig, zwei, screen)

  Spawning_ganovil1g, Spawning_ganovil2g, Spawning_ganovil3g, Spawning_rokkaiman1g, Spawning_rokkaiman2g, Spawning_rokkaiman3g, Spawning_rabigator1g, rokkaiman_x1g, rokkaiman_x2g, rokkaiman_x3g, ganovil_x1g, ganovil_x2g, ganovil_x3g, rokkaiman_y1g, rokkaiman_y2g, rokkaiman_y3g, ganovil_y1g, ganovil_y2g, ganovil_y3g, rokkaiman1g, rokkaiman2g, rokkaiman3g, vierundsechzig, fünfundsechzig, sechsundsechzig, zwei, screen=evolve_Pokemon1(Spawning_ganovil1g, Spawning_ganovil2g, Spawning_ganovil3g, Spawning_rokkaiman1g, Spawning_rokkaiman2g, Spawning_rokkaiman3g, Spawning_rabigator1g, rokkaiman_x1g, rokkaiman_x2g, rokkaiman_x3g, ganovil_x1g, ganovil_x2g, ganovil_x3g, rokkaiman_y1g, rokkaiman_y2g, rokkaiman_y3g, ganovil_y1g, ganovil_y2g, ganovil_y3g, rokkaiman1g, rokkaiman2g, rokkaiman3g, vierundsechzig, fünfundsechzig, sechsundsechzig, zwei, screen)

  Spawning_rotomurf1g, Spawning_rotomurf2g, Spawning_rotomurf3g, Spawning_stalobor1g, Spawning_stalobor2g, Spawning_stalobor3g, Spawning_stalobor21g, stalobor_x1g, stalobor_x2g, stalobor_x3g, rotomurf_x1g, rotomurf_x2g, rotomurf_x3g, stalobor_y1g, stalobor_y2g, stalobor_y3g, rotomurf_y1g, rotomurf_y2g, rotomurf_y3g, stalobor1g, stalobor2g, stalobor3g, einundsiebzig, zweiundsiebzig, dreiundsiebzig, zwei, screen=evolve_Pokemon1(Spawning_rotomurf1g, Spawning_rotomurf2g, Spawning_rotomurf3g, Spawning_stalobor1g, Spawning_stalobor2g, Spawning_stalobor3g, Spawning_stalobor21g, stalobor_x1g, stalobor_x2g, stalobor_x3g, rotomurf_x1g, rotomurf_x2g, rotomurf_x3g, stalobor_y1g, stalobor_y2g, stalobor_y3g, rotomurf_y1g, rotomurf_y2g, rotomurf_y3g, stalobor1g, stalobor2g, stalobor3g, einundsiebzig, zweiundsiebzig, dreiundsiebzig, zwei, screen)

  Spawning_makabaja1g, Spawning_makabaja2g, Spawning_makabaja3g, Spawning_echnatoll1g, Spawning_echnatoll2g, Spawning_echnatoll3g, Spawning_echnatoll21g, echnatoll_x1g, echnatoll_x2g, echnatoll_x3g, makabaja_x1g, makabaja_x2g, makabaja_x3g, echnatoll_y1g, echnatoll_y2g, echnatoll_y3g, makabaja_y1g, makabaja_y2g, makabaja_y3g, echnatoll1g, echnatoll2g, echnatoll3g, achtundsiebzig, neunundsiebzig, achtzig, zwei, screen=evolve_Pokemon1(Spawning_makabaja1g, Spawning_makabaja2g, Spawning_makabaja3g, Spawning_echnatoll1g, Spawning_echnatoll2g, Spawning_echnatoll3g, Spawning_echnatoll21g, echnatoll_x1g, echnatoll_x2g, echnatoll_x3g, makabaja_x1g, makabaja_x2g, makabaja_x3g, echnatoll_y1g, echnatoll_y2g, echnatoll_y3g, makabaja_y1g, makabaja_y2g, makabaja_y3g, echnatoll1g, echnatoll2g, echnatoll3g, achtundsiebzig, neunundsiebzig, achtzig, zwei, screen)

  'Zweite Entwicklung'

  Spawning_efoserp1g, Spawning_efoserp2g, Spawning_efoserp3g, Spawning_serpiroyal1g, serpiroyal_x1g, efoserp_x1g, efoserp_x2g, efoserp_x3g, serpiroyal_y1g, efoserp_y1g, efoserp_y2g, efoserp_y3g, serpiroyal1g, vier, fünf, sechs, zwei, screen = evolve_Pokemon2(Spawning_efoserp1g, Spawning_efoserp2g, Spawning_efoserp3g, Spawning_serpiroyal1g, serpiroyal_x1g, efoserp_x1g, efoserp_x2g, efoserp_x3g, serpiroyal_y1g, efoserp_y1g, efoserp_y2g, efoserp_y3g, serpiroyal1g, vier, fünf, sechs, zwei, screen)

  Spawning_ferkokel1g, Spawning_ferkokel2g, Spawning_ferkokel3g, Spawning_flambirex1g, flambirex_x1g, ferkokel_x1g, ferkokel_x2g, ferkokel_x3g, flambirex_y1g, ferkokel_y1g, ferkokel_y2g, ferkokel_y3g, flambirex1g, elf, zwölf, dreizehn, zwei, screen = evolve_Pokemon2(Spawning_ferkokel1g, Spawning_ferkokel2g, Spawning_ferkokel3g, Spawning_flambirex1g, flambirex_x1g, ferkokel_x1g, ferkokel_x2g, ferkokel_x3g, flambirex_y1g, ferkokel_y1g, ferkokel_y2g, ferkokel_y3g, flambirex1g, elf, zwölf, dreizehn, zwei, screen)

  Spawning_zwottronin1g, Spawning_zwottronin2g, Spawning_zwottronin3g, Spawning_admurai1g, admurai_x1g, zwottronin_x1g, zwottronin_x2g, zwottronin_x3g, admurai_y1g, zwottronin_y1g, zwottronin_y2g, zwottronin_y3g, admurai1g, achtzehn, neunzehn, zwanzig, zwei, screen = evolve_Pokemon2(Spawning_zwottronin1g, Spawning_zwottronin2g, Spawning_zwottronin3g, Spawning_admurai1g, admurai_x1g, zwottronin_x1g, zwottronin_x2g, zwottronin_x3g, admurai_y1g, zwottronin_y1g, zwottronin_y2g, zwottronin_y3g, admurai1g, achtzehn, neunzehn, zwanzig, zwei, screen)

  Spawning_folikon1g, Spawning_folikon2g, Spawning_folikon3g, Spawning_matrifol1g, matrifol_x1g, folikon_x1g, folikon_x2g, folikon_x3g, matrifol_y1g, folikon_y1g, folikon_y2g, folikon_y3g, matrifol1g, fünfundzwanzig, sechsundzwanzig, siebenundzwanzig, zwei, screen = evolve_Pokemon2(Spawning_folikon1g, Spawning_folikon2g, Spawning_folikon3g, Spawning_matrifol1g, matrifol_x1g, folikon_x1g, folikon_x2g, folikon_x3g, matrifol_y1g, folikon_y1g, folikon_y2g, folikon_y3g, matrifol1g, fünfundzwanzig, sechsundzwanzig, siebenundzwanzig, zwei, screen)

  Spawning_rollum1g, Spawning_rollum2g, Spawning_rollum3g, Spawning_cerapendra1g, cerapendra_x1g, rollum_x1g, rollum_x2g, rollum_x3g, cerapendra_y1g, rollum_y1g, rollum_y2g, rollum_y3g, cerapendra1g, zweiunddreißig, dreiunddreißig, vierunddreißig, zwei, screen = evolve_Pokemon2(Spawning_rollum1g, Spawning_rollum2g, Spawning_rollum3g, Spawning_cerapendra1g, cerapendra_x1g, rollum_x1g, rollum_x2g, rollum_x3g, cerapendra_y1g, rollum_y1g, rollum_y2g, rollum_y3g, cerapendra1g, zweiunddreißig, dreiunddreißig, vierunddreißig, zwei, screen)

  Spawning_strepoli1g, Spawning_strepoli2g, Spawning_strepoli3g, Spawning_meistagrif1g, meistagrif_x1g, strepoli_x1g, strepoli_x2g, strepoli_x3g, meistagrif_y1g, strepoli_y1g, strepoli_y2g, strepoli_y3g, meistagrif1g, neununddreißig, vierzig, einundvierzig, zwei, screen = evolve_Pokemon2(Spawning_strepoli1g, Spawning_strepoli2g, Spawning_strepoli3g, Spawning_meistagrif1g, meistagrif_x1g, strepoli_x1g, strepoli_x2g, strepoli_x3g, meistagrif_y1g, strepoli_y1g, strepoli_y2g, strepoli_y3g, meistagrif1g, neununddreißig, vierzig, einundvierzig, zwei, screen)

  Spawning_kliklak1g, Spawning_kliklak2g, Spawning_kliklak3g, Spawning_klikdiklak1g, klikdiklak_x1g, kliklak_x1g, kliklak_x2g, kliklak_x3g, klikdiklak_y1g, kliklak_y1g, kliklak_y2g, kliklak_y3g, klikdiklak1g, sechsundvierzig, siebenundvierzig, achtundvierzig, zwei, screen = evolve_Pokemon2(Spawning_kliklak1g, Spawning_kliklak2g, Spawning_kliklak3g, Spawning_klikdiklak1g, klikdiklak_x1g, kliklak_x1g, kliklak_x2g, kliklak_x3g, klikdiklak_y1g, kliklak_y1g, kliklak_y2g, kliklak_y3g, klikdiklak1g, sechsundvierzig, siebenundvierzig, achtundvierzig, zwei, screen)

  Spawning_sedimantur1g, Spawning_sedimantur2g, Spawning_sedimantur3g, Spawning_brokkolos1g, brokkolos_x1g, sedimantur_x1g, sedimantur_x2g, sedimantur_x3g, brokkolos_y1g, sedimantur_y1g, sedimantur_y2g, sedimantur_y3g, brokkolos1g, dreiundfünfzig, vierundfünfzig, fünfundfünfzig, zwei, screen = evolve_Pokemon2(Spawning_sedimantur1g, Spawning_sedimantur2g, Spawning_sedimantur3g, Spawning_brokkolos1g, brokkolos_x1g, sedimantur_x1g, sedimantur_x2g, sedimantur_x3g, brokkolos_y1g, sedimantur_y1g, sedimantur_y2g, sedimantur_y3g, brokkolos1g, dreiundfünfzig, vierundfünfzig, fünfundfünfzig, zwei, screen)

  Spawning_sharfax1g, Spawning_sharfax2g, Spawning_sharfax3g, Spawning_maxax1g, maxax_x1g, sharfax_x1g, sharfax_x2g, sharfax_x3g, maxax_y1g, sharfax_y1g, sharfax_y2g, sharfax_y3g, maxax1g, sechzig, einundsechzig, zweiundsechzig, zwei, screen = evolve_Pokemon2(Spawning_sharfax1g, Spawning_sharfax2g, Spawning_sharfax3g, Spawning_maxax1g, maxax_x1g, sharfax_x1g, sharfax_x2g, sharfax_x3g, maxax_y1g, sharfax_y1g, sharfax_y2g, sharfax_y3g, maxax1g, sechzig, einundsechzig, zweiundsechzig, zwei, screen)

  Spawning_rokkaiman1g, Spawning_rokkaiman2g, Spawning_rokkaiman3g, Spawning_rabigator1g, rabigator_x1g, rokkaiman_x1g, rokkaiman_x2g, rokkaiman_x3g, rabigator_y1g, rokkaiman_y1g, rokkaiman_y2g, rokkaiman_y3g, rabigator1g, siebenundsechzig, achtundsechzig, neunundsechzig, zwei, screen = evolve_Pokemon2(Spawning_rokkaiman1g, Spawning_rokkaiman2g, Spawning_rokkaiman3g, Spawning_rabigator1g, rabigator_x1g, rokkaiman_x1g, rokkaiman_x2g, rokkaiman_x3g, rabigator_y1g, rokkaiman_y1g, rokkaiman_y2g, rokkaiman_y3g, rabigator1g, siebenundsechzig, achtundsechzig, neunundsechzig, zwei, screen)

  Spawning_stalobor1g, Spawning_stalobor2g, Spawning_stalobor3g, Spawning_stalobor21g, stalobor2_x1g, stalobor_x1g, stalobor_x2g, stalobor_x3g, stalobor2_y1g, stalobor_y1g, stalobor_y2g, stalobor_y3g, stalobor21g, vierundsiebzig, fünfundsiebzig, sechsundsiebzig, zwei, screen = evolve_Pokemon2(Spawning_stalobor1g, Spawning_stalobor2g, Spawning_stalobor3g, Spawning_stalobor21g, stalobor2_x1g, stalobor_x1g, stalobor_x2g, stalobor_x3g, stalobor2_y1g, stalobor_y1g, stalobor_y2g, stalobor_y3g, stalobor21g, vierundsiebzig, fünfundsiebzig, sechsundsiebzig, zwei, screen)

  Spawning_echnatoll1g, Spawning_echnatoll2g, Spawning_echnatoll3g, Spawning_echnatoll21g, echnatoll2_x1g, echnatoll_x1g, echnatoll_x2g, echnatoll_x3g, echnatoll2_y1g, echnatoll_y1g, echnatoll_y2g, echnatoll_y3g, echnatoll21g, einundachtzig, zweiundachtzig, dreiundachtzig, zwei, screen = evolve_Pokemon2(Spawning_echnatoll1g, Spawning_echnatoll2g, Spawning_echnatoll3g, Spawning_echnatoll21g, echnatoll2_x1g, echnatoll_x1g, echnatoll_x2g, echnatoll_x3g, echnatoll2_y1g, echnatoll_y1g, echnatoll_y2g, echnatoll_y3g, echnatoll21g, einundachtzig, zweiundachtzig, dreiundachtzig, zwei, screen)


  'Verkaufen eines Pokemon'
  
  Spawning_serpifeu1g, serpifeu_x1g, serpifeu_y1g, eins, eins1, goldg = sell_Pokemong(Spawning_serpifeu1g, serpifeu_x1g, serpifeu_y1g, eins, eins1, goldg)
  Spawning_serpifeu2g, serpifeu_x2g, serpifeu_y2g, zwei, eins1, goldg = sell_Pokemong(Spawning_serpifeu2g, serpifeu_x2g, serpifeu_y2g, zwei, eins1, goldg)
  Spawning_serpifeu3g, serpifeu_x3g, serpifeu_y3g, drei, eins1, goldg = sell_Pokemong(Spawning_serpifeu3g, serpifeu_x3g, serpifeu_y3g, drei, eins1, goldg)
  Spawning_efoserp1g, efoserp_x1g, efoserp_y1g, vier, drei3, goldg = sell_Pokemong(Spawning_efoserp1g, efoserp_x1g, efoserp_y1g, vier, drei3, goldg)
  Spawning_efoserp2g, efoserp_x2g, efoserp_y2g, fünf, drei3, goldg = sell_Pokemong(Spawning_efoserp2g, efoserp_x2g, efoserp_y2g, fünf, drei3, goldg)
  Spawning_efoserp3g, efoserp_x3g, efoserp_y3g, sechs, drei3, goldg = sell_Pokemong(Spawning_efoserp3g, efoserp_x3g, efoserp_y3g, sechs, drei3, goldg)
  Spawning_serpiroyal1g, serpiroyal_x1g, serpiroyal_y1g, sieben, neun9, goldg = sell_Pokemong(Spawning_serpiroyal1g, serpiroyal_x1g, serpiroyal_y1g, sieben, neun9, goldg)

  Spawning_floink1g, floink_x1g, floink_y1g, acht, eins1, goldg = sell_Pokemong(Spawning_floink1g, floink_x1g, floink_y1g, acht, eins1, goldg)
  Spawning_floink2g, floink_x2g, floink_y2g, neun, eins1, goldg = sell_Pokemong(Spawning_floink2g, floink_x2g, floink_y2g, neun, eins1, goldg)
  Spawning_floink3g, floink_x3g, floink_y3g, zehn, eins1, goldg = sell_Pokemong(Spawning_floink3g, floink_x3g, floink_y3g, zehn, eins1, goldg)
  Spawning_ferkokel1g, ferkokel_x1g, ferkokel_y1g, elf, drei3, goldg = sell_Pokemong(Spawning_ferkokel1g, ferkokel_x1g, ferkokel_y1g, elf, drei3, goldg)
  Spawning_ferkokel2g, ferkokel_x2g, ferkokel_y2g, zwölf, drei3, goldg = sell_Pokemong(Spawning_ferkokel2g, ferkokel_x2g, ferkokel_y2g, zwölf, drei3, goldg)
  Spawning_ferkokel3g, ferkokel_x3g, ferkokel_y3g, dreizehn, drei3, goldg = sell_Pokemong(Spawning_ferkokel3g, ferkokel_x3g, ferkokel_y3g, dreizehn, drei3, goldg)
  Spawning_flambirex1g, flambirex_x1g, flambirex_y1g, vierzehn, neun9, goldg = sell_Pokemong(Spawning_flambirex1g, flambirex_x1g, flambirex_y1g, vierzehn, neun9, goldg)

  Spawning_ottaro1g, ottaro_x1g, ottaro_y1g, fünfzehn, eins1, goldg = sell_Pokemong(Spawning_ottaro1g, ottaro_x1g, ottaro_y1g, fünfzehn, eins1, goldg)
  Spawning_ottaro2g, ottaro_x2g, ottaro_y2g, sechzehn, eins1, goldg = sell_Pokemong(Spawning_ottaro2g, ottaro_x2g, ottaro_y2g, sechzehn, eins1, goldg)
  Spawning_ottaro3g, ottaro_x3g, ottaro_y3g, siebzehn, eins1, goldg = sell_Pokemong(Spawning_ottaro3g, ottaro_x3g, ottaro_y3g, siebzehn, eins1, goldg)
  Spawning_zwottronin1g, zwottronin_x1g, zwottronin_y1g, achtzehn, drei3, goldg = sell_Pokemong(Spawning_zwottronin1g, zwottronin_x1g, zwottronin_y1g, achtzehn, drei3, goldg)
  Spawning_zwottronin2g, zwottronin_x2g, zwottronin_y2g, neunzehn, drei3, goldg = sell_Pokemong(Spawning_zwottronin2g, zwottronin_x2g, zwottronin_y2g, neunzehn, drei3, goldg)
  Spawning_zwottronin3g, zwottronin_x3g, zwottronin_y3g, zwanzig, drei3, goldg = sell_Pokemong(Spawning_zwottronin3g, zwottronin_x3g, zwottronin_y3g, zwanzig, drei3, goldg)
  Spawning_admurai1g, admurai_x1g, admurai_y1g, einundzwanzig, neun9, goldg = sell_Pokemong(Spawning_admurai1g, admurai_x1g, admurai_y1g, einundzwanzig, neun9, goldg)

  Spawning_strawickl1g, strawickl_x1g, strawickl_y1g, zweiundzwanzig, zwei2, goldg = sell_Pokemong(Spawning_strawickl1g, strawickl_x1g, strawickl_y1g, zweiundzwanzig, zwei2, goldg)
  Spawning_strawickl2g, strawickl_x2g, strawickl_y2g, dreiundzwanzig, zwei2, goldg = sell_Pokemong(Spawning_strawickl2g, strawickl_x2g, strawickl_y2g, dreiundzwanzig, zwei2, goldg)
  Spawning_strawickl3g, strawickl_x3g, strawickl_y3g, vierundzwanzig, zwei2, goldg = sell_Pokemong(Spawning_strawickl3g, strawickl_x3g, strawickl_y3g, vierundzwanzig, zwei2, goldg)
  Spawning_folikon1g, folikon_x1g, folikon_y1g, fünfundzwanzig, sechs6, goldg = sell_Pokemong(Spawning_folikon1g, folikon_x1g, folikon_y1g, fünfundzwanzig, sechs6, goldg)
  Spawning_folikon2g, folikon_x2g, folikon_y2g, sechsundzwanzig, sechs6, goldg = sell_Pokemong(Spawning_folikon2g, folikon_x2g, folikon_y2g, sechsundzwanzig, sechs6, goldg)
  Spawning_folikon3g, folikon_x3g, folikon_y3g, siebenundzwanzig, sechs6, goldg = sell_Pokemong(Spawning_folikon3g, folikon_x3g, folikon_y3g, siebenundzwanzig, sechs6, goldg)
  Spawning_matrifol1g, matrifol_x1g, matrifol_y1g, achtundzwanzig, achtzehn18, goldg = sell_Pokemong(Spawning_matrifol1g, matrifol_x1g, matrifol_y1g, achtundzwanzig, achtzehn18, goldg)

  Spawning_toxiped1g, toxiped_x1g, toxiped_y1g, neunundzwanzig, zwei2, goldg = sell_Pokemong(Spawning_toxiped1g, toxiped_x1g, toxiped_y1g, neunundzwanzig, zwei2, goldg)
  Spawning_toxiped2g, toxiped_x2g, toxiped_y2g, dreißig, zwei2, goldg = sell_Pokemong(Spawning_toxiped2g, toxiped_x2g, toxiped_y2g, dreißig, zwei2, goldg)
  Spawning_toxiped3g, toxiped_x3g, toxiped_y3g, einunddreißig, zwei2, goldg = sell_Pokemong(Spawning_toxiped3g, toxiped_x3g, toxiped_y3g, einunddreißig, zwei2, goldg)
  Spawning_rollum1g, rollum_x1g, rollum_y1g, zweiunddreißig, sechs6, goldg = sell_Pokemong(Spawning_rollum1g, rollum_x1g, rollum_y1g, zweiunddreißig, sechs6, goldg)
  Spawning_rollum2g, rollum_x2g, rollum_y2g, dreiunddreißig, sechs6, goldg = sell_Pokemong(Spawning_rollum2g, rollum_x2g, rollum_y2g, dreiunddreißig, sechs6, goldg)
  Spawning_rollum3g, rollum_x3g, rollum_y3g, vierunddreißig, sechs6, goldg = sell_Pokemong(Spawning_rollum3g, rollum_x3g, rollum_y3g, vierunddreißig, sechs6, goldg)
  Spawning_cerapendra1g, cerapendra_x1g, cerapendra_y1g, fünfunddreißig, achtzehn18, goldg = sell_Pokemong(Spawning_cerapendra1g, cerapendra_x1g, cerapendra_y1g, fünfunddreißig, achtzehn18, goldg)

  Spawning_praktibalk1g, praktibalk_x1g, praktibalk_y1g, sechsunddreißig, zwei2, goldg = sell_Pokemong(Spawning_praktibalk1g, praktibalk_x1g, praktibalk_y1g, sechsunddreißig, zwei2, goldg)
  Spawning_praktibalk2g, praktibalk_x2g, praktibalk_y2g, siebenunddreißig, zwei2, goldg = sell_Pokemong(Spawning_praktibalk2g, praktibalk_x2g, praktibalk_y2g, siebenunddreißig, zwei2, goldg)
  Spawning_praktibalk3g, praktibalk_x3g, praktibalk_y3g, achtunddreißig, zwei2, goldg = sell_Pokemong(Spawning_praktibalk3g, praktibalk_x3g, praktibalk_y3g, achtunddreißig, zwei2, goldg)
  Spawning_strepoli1g, strepoli_x1g, strepoli_y1g, neununddreißig, sechs6, goldg = sell_Pokemong(Spawning_strepoli1g, strepoli_x1g, strepoli_y1g, neununddreißig, sechs6, goldg)
  Spawning_strepoli2g, strepoli_x2g, strepoli_y2g, vierzig, sechs6, goldg = sell_Pokemong(Spawning_strepoli2g, strepoli_x2g, strepoli_y2g, vierzig, sechs6, goldg)
  Spawning_strepoli3g, strepoli_x3g, strepoli_y3g, einundvierzig, sechs6, goldg = sell_Pokemong(Spawning_strepoli3g, strepoli_x3g, strepoli_y3g, einundvierzig, sechs6, goldg)
  Spawning_meistagrif1g, meistagrif_x1g, meistagrif_y1g, zweiundvierzig, achtzehn18, goldg = sell_Pokemong(Spawning_meistagrif1g, meistagrif_x1g, meistagrif_y1g, zweiundvierzig, achtzehn18, goldg)

  Spawning_klikk1g, klikk_x1g, klikk_y1g, dreiundvierzig, drei3, goldg = sell_Pokemong(Spawning_klikk1g, klikk_x1g, klikk_y1g, dreiundvierzig, drei3, goldg)
  Spawning_klikk2g, klikk_x2g, klikk_y2g, vierundvierzig, drei3, goldg = sell_Pokemong(Spawning_klikk2g, klikk_x2g, klikk_y2g, vierundvierzig, drei3, goldg)
  Spawning_klikk3g, klikk_x3g, klikk_y3g, fünfundvierzig, drei3, goldg = sell_Pokemong(Spawning_klikk3g, klikk_x3g, klikk_y3g, fünfundvierzig, drei3, goldg)
  Spawning_kliklak1g, kliklak_x1g, kliklak_y1g, sechsundvierzig, neun9, goldg = sell_Pokemong(Spawning_kliklak1g, kliklak_x1g, kliklak_y1g, sechsundvierzig, neun9, goldg)
  Spawning_kliklak2g, kliklak_x2g, kliklak_y2g, siebenundvierzig, neun9, goldg = sell_Pokemong(Spawning_kliklak2g, kliklak_x2g, kliklak_y2g, siebenundvierzig, neun9, goldg)
  Spawning_kliklak3g, kliklak_x3g, kliklak_y3g, achtundvierzig, neun9, goldg = sell_Pokemong(Spawning_kliklak3g, kliklak_x3g, kliklak_y3g, achtundvierzig, neun9, goldg)
  Spawning_klikdiklak1g, klikdiklak_x1g, klikdiklak_y1g, neunundvierzig, siebenundzwanzig27, goldg = sell_Pokemong(Spawning_klikdiklak1g, klikdiklak_x1g, klikdiklak_y1g, neunundvierzig, siebenundzwanzig27, goldg)

  Spawning_kiesling1g, kiesling_x1g, kiesling_y1g, fünfzig, drei3, goldg = sell_Pokemong(Spawning_kiesling1g, kiesling_x1g, kiesling_y1g, fünfzig, drei3, goldg)
  Spawning_kiesling2g, kiesling_x2g, kiesling_y2g, einundfünfzig, drei3, goldg = sell_Pokemong(Spawning_kiesling2g, kiesling_x2g, kiesling_y2g, einundfünfzig, drei3, goldg)
  Spawning_kiesling3g, kiesling_x3g, kiesling_y3g, zweiundfünfzig, drei3, goldg = sell_Pokemong(Spawning_kiesling3g, kiesling_x3g, kiesling_y3g, zweiundfünfzig, drei3, goldg)
  Spawning_sedimantur1g, sedimantur_x1g, sedimantur_y1g, dreiundfünfzig, neun9, goldg = sell_Pokemong(Spawning_sedimantur1g, sedimantur_x1g, sedimantur_y1g, dreiundfünfzig, neun9, goldg)
  Spawning_sedimantur2g, sedimantur_x2g, sedimantur_y2g, vierundfünfzig, neun9, goldg = sell_Pokemong(Spawning_sedimantur2g, sedimantur_x2g, sedimantur_y2g, vierundfünfzig, neun9, goldg)
  Spawning_sedimantur3g, sedimantur_x3g, sedimantur_y3g, fünfundfünfzig, neun9, goldg = sell_Pokemong(Spawning_sedimantur3g, sedimantur_x3g, sedimantur_y3g, fünfundfünfzig, neun9, goldg)
  Spawning_brokkolos1g, brokkolos_x1g, brokkolos_y1g, sechsundfünfzig, siebenundzwanzig27, goldg = sell_Pokemong(Spawning_brokkolos1g, brokkolos_x1g, brokkolos_y1g, sechsundfünfzig, siebenundzwanzig27, goldg)

  Spawning_milza1g, milza_x1g, milza_y1g, siebenundfünfzig, drei3, goldg = sell_Pokemong(Spawning_milza1g, milza_x1g, milza_y1g, siebenundfünfzig, drei3, goldg)
  Spawning_milza2g, milza_x2g, milza_y2g, achtundfünfzig, drei3, goldg = sell_Pokemong(Spawning_milza2g, milza_x2g, milza_y2g, achtundfünfzig, drei3, goldg)
  Spawning_milza3g, milza_x3g, milza_y3g, neunundfünfzig, drei3, goldg = sell_Pokemong(Spawning_milza3g, milza_x3g, milza_y3g, neunundfünfzig, drei3, goldg)
  Spawning_sharfax1g, sharfax_x1g, sharfax_y1g, sechzig, neun9, goldg = sell_Pokemong(Spawning_sharfax1g, sharfax_x1g, sharfax_y1g, sechzig, neun9, goldg)
  Spawning_sharfax2g, sharfax_x2g, sharfax_y2g, einundsechzig, neun9, goldg = sell_Pokemong(Spawning_sharfax2g, sharfax_x2g, sharfax_y2g, einundsechzig, neun9, goldg)
  Spawning_sharfax3g, sharfax_x3g, sharfax_y3g, zweiundsechzig, neun9, goldg = sell_Pokemong(Spawning_sharfax3g, sharfax_x3g, sharfax_y3g, zweiundsechzig, neun9, goldg)
  Spawning_maxax1g, maxax_x1g, maxax_y1g, dreiundsechzig, siebenundzwanzig27, goldg = sell_Pokemong(Spawning_maxax1g, maxax_x1g, maxax_y1g, dreiundsechzig, siebenundzwanzig27, goldg)

  Spawning_ganovil1g, ganovil_x1g, ganovil_y1g, vierundsechzig, vier4, goldg = sell_Pokemong(Spawning_ganovil1g, ganovil_x1g, ganovil_y1g, vierundsechzig, vier4, goldg)
  Spawning_ganovil2g, ganovil_x2g, ganovil_y2g, fünfundsechzig, vier4, goldg = sell_Pokemong(Spawning_ganovil2g, ganovil_x2g, ganovil_y2g, fünfundsechzig, vier4, goldg)
  Spawning_ganovil3g, ganovil_x3g, ganovil_y3g, sechsundsechzig, vier4, goldg = sell_Pokemong(Spawning_ganovil3g, ganovil_x3g, ganovil_y3g, sechsundsechzig, vier4, goldg)
  Spawning_rokkaiman1g, rokkaiman_x1g, rokkaiman_y1g, siebenundsechzig, zwölf12, goldg = sell_Pokemong(Spawning_rokkaiman1g, rokkaiman_x1g, rokkaiman_y1g, siebenundsechzig, zwölf12, goldg)
  Spawning_rokkaiman2g, rokkaiman_x2g, rokkaiman_y2g, achtundsechzig, zwölf12, goldg = sell_Pokemong(Spawning_rokkaiman2g, rokkaiman_x2g, rokkaiman_y2g, achtundsechzig, zwölf12, goldg)
  Spawning_rokkaiman3g, rokkaiman_x3g, rokkaiman_y3g, neunundsechzig, zwölf12, goldg = sell_Pokemong(Spawning_rokkaiman3g, rokkaiman_x3g, rokkaiman_y3g, neunundsechzig, zwölf12, goldg)
  Spawning_rabigator1g, rabigator_x1g, rabigator_y1g, siebzig, sechsunddreißig36, goldg = sell_Pokemong(Spawning_rabigator1g, rabigator_x1g, rabigator_y1g, siebzig, sechsunddreißig36, goldg)

  Spawning_rotomurf1g, rotomurf_x1g, rotomurf_y1g, einundsiebzig, vier4, goldg = sell_Pokemong(Spawning_rotomurf1g, rotomurf_x1g, rotomurf_y1g, einundsiebzig, vier4, goldg)
  Spawning_rotomurf2g, rotomurf_x2g, rotomurf_y2g, zweiundsiebzig, vier4, goldg = sell_Pokemong(Spawning_rotomurf2g, rotomurf_x2g, rotomurf_y2g, zweiundsiebzig, vier4, goldg)
  Spawning_rotomurf3g, rotomurf_x3g, rotomurf_y3g, dreiundsiebzig, vier4, goldg = sell_Pokemong(Spawning_rotomurf3g, rotomurf_x3g, rotomurf_y3g, dreiundsiebzig, vier4, goldg)
  Spawning_stalobor1g, stalobor_x1g, stalobor_y1g, vierundsiebzig, zwölf12, goldg = sell_Pokemong(Spawning_stalobor1g, stalobor_x1g, stalobor_y1g, vierundsiebzig, zwölf12, goldg)
  Spawning_stalobor2g, stalobor_x2g, stalobor_y2g, fünfundsiebzig, zwölf12, goldg = sell_Pokemong(Spawning_stalobor2g, stalobor_x2g, stalobor_y2g, fünfundsiebzig, zwölf12, goldg)
  Spawning_stalobor3g, stalobor_x3g, stalobor_y3g, sechsundsiebzig, zwölf12, goldg = sell_Pokemong(Spawning_stalobor3g, stalobor_x3g, stalobor_y3g, sechsundsiebzig, zwölf12, goldg)
  Spawning_stalobor21g, stalobor2_x1g, stalobor2_y1g, siebenundsiebzig, sechsunddreißig36, goldg = sell_Pokemong(Spawning_stalobor21g, stalobor2_x1g, stalobor2_y1g, siebenundsiebzig, sechsunddreißig36, goldg)

  Spawning_makabaja1g, makabaja_x1g, makabaja_y1g, achtundsiebzig, vier4, goldg = sell_Pokemong(Spawning_makabaja1g, makabaja_x1g, makabaja_y1g, achtundsiebzig, vier4, goldg)
  Spawning_makabaja2g, makabaja_x2g, makabaja_y2g, neunundsiebzig, vier4, goldg = sell_Pokemong(Spawning_makabaja2g, makabaja_x2g, makabaja_y2g, neunundsiebzig, vier4, goldg)
  Spawning_makabaja3g, makabaja_x3g, makabaja_y3g, achtzig, vier4, goldg = sell_Pokemong(Spawning_makabaja3g, makabaja_x3g, makabaja_y3g, achtzig, vier4, goldg)
  Spawning_echnatoll1g, echnatoll_x1g, echnatoll_y1g, einundachtzig, zwölf12, goldg = sell_Pokemong(Spawning_echnatoll1g, echnatoll_x1g, echnatoll_y1g, einundachtzig, zwölf12, goldg)
  Spawning_echnatoll2g, echnatoll_x2g, echnatoll_y2g, zweiundachtzig, zwölf12, goldg = sell_Pokemong(Spawning_echnatoll2g, echnatoll_x2g, echnatoll_y2g, zweiundachtzig, zwölf12, goldg)
  Spawning_echnatoll3g, echnatoll_x3g, echnatoll_y3g, dreiundachtzig, zwölf12, goldg = sell_Pokemong(Spawning_echnatoll3g, echnatoll_x3g, echnatoll_y3g, dreiundachtzig, zwölf12, goldg)
  Spawning_echnatoll21g, echnatoll2_x1g, echnatoll2_y1g, vierundachtzig, sechsunddreißig36, goldg = sell_Pokemong(Spawning_echnatoll21g, echnatoll2_x1g, echnatoll2_y1g, vierundachtzig, sechsunddreißig36, goldg)



  'Rerollen des Shops'
  
  shop_slot_1_rarg, shop_slot_2_rarg, shop_slot_3_rarg, shop_slot_4_rarg, shop_slot_5_rarg, shop_slot_1_var_commong, shop_slot_2_var_commong, shop_slot_3_var_commong, shop_slot_4_var_commong, shop_slot_5_var_commong, shop_slot_1_var_uncommong, shop_slot_2_var_uncommong, shop_slot_3_var_uncommong, shop_slot_4_var_uncommong, shop_slot_5_var_uncommong, shop_slot_1_var_rareg, shop_slot_2_var_rareg, shop_slot_3_var_rareg, shop_slot_4_var_rareg, shop_slot_5_var_rareg, shop_slot_1_var_epicg, shop_slot_2_var_epicg, shop_slot_3_var_epicg, shop_slot_4_var_epicg, shop_slot_5_var_epicg, goldg = reroll_Shopg(shop_slot_1_rarg, shop_slot_2_rarg, shop_slot_3_rarg, shop_slot_4_rarg, shop_slot_5_rarg, shop_slot_1_var_commong, shop_slot_2_var_commong, shop_slot_3_var_commong, shop_slot_4_var_commong, shop_slot_5_var_commong, shop_slot_1_var_uncommong, shop_slot_2_var_uncommong, shop_slot_3_var_uncommong, shop_slot_4_var_uncommong, shop_slot_5_var_uncommong, shop_slot_1_var_rareg, shop_slot_2_var_rareg, shop_slot_3_var_rareg, shop_slot_4_var_rareg, shop_slot_5_var_rareg, shop_slot_1_var_epicg, shop_slot_2_var_epicg, shop_slot_3_var_epicg, shop_slot_4_var_epicg, shop_slot_5_var_epicg, goldg)
  

  Spawning_serpiroyal1g, shop_slot_1_var_commong, shop_slot_2_var_commong, shop_slot_3_var_commong, shop_slot_4_var_commong, shop_slot_5_var_commong, eins = reroll_Shop2(Spawning_serpiroyal1g, shop_slot_1_var_commong, shop_slot_2_var_commong, shop_slot_3_var_commong, shop_slot_4_var_commong, shop_slot_5_var_commong, eins)

  Spawning_flambirex1g, shop_slot_1_var_commong, shop_slot_2_var_commong, shop_slot_3_var_commong, shop_slot_4_var_commong, shop_slot_5_var_commong, zwei = reroll_Shop2(Spawning_flambirex1g, shop_slot_1_var_commong, shop_slot_2_var_commong, shop_slot_3_var_commong, shop_slot_4_var_commong, shop_slot_5_var_commong, zwei)

  Spawning_admurai1g, shop_slot_1_var_commong, shop_slot_2_var_commong, shop_slot_3_var_commong, shop_slot_4_var_commong, shop_slot_5_var_commong, drei = reroll_Shop2(Spawning_admurai1g, shop_slot_1_var_commong, shop_slot_2_var_commong, shop_slot_3_var_commong, shop_slot_4_var_commong, shop_slot_5_var_commong, drei)

  Spawning_matrifol1g, shop_slot_1_var_uncommong, shop_slot_2_var_uncommong, shop_slot_3_var_uncommong, shop_slot_4_var_uncommong, shop_slot_5_var_uncommong, eins = reroll_Shop2(Spawning_matrifol1g, shop_slot_1_var_uncommong, shop_slot_2_var_uncommong, shop_slot_3_var_uncommong, shop_slot_4_var_uncommong, shop_slot_5_var_uncommong, eins)

  Spawning_cerapendra1g, shop_slot_1_var_uncommong, shop_slot_2_var_uncommong, shop_slot_3_var_uncommong, shop_slot_4_var_uncommong, shop_slot_5_var_uncommong, zwei = reroll_Shop2(Spawning_cerapendra1g, shop_slot_1_var_uncommong, shop_slot_2_var_uncommong, shop_slot_3_var_uncommong, shop_slot_4_var_uncommong, shop_slot_5_var_uncommong, zwei)

  Spawning_meistagrif1g, shop_slot_1_var_uncommong, shop_slot_2_var_uncommong, shop_slot_3_var_uncommong, shop_slot_4_var_uncommong, shop_slot_5_var_uncommong, drei = reroll_Shop2(Spawning_meistagrif1g, shop_slot_1_var_uncommong, shop_slot_2_var_uncommong, shop_slot_3_var_uncommong, shop_slot_4_var_uncommong, shop_slot_5_var_uncommong, drei)

  Spawning_klikdiklak1g, shop_slot_1_var_rareg, shop_slot_2_var_rareg, shop_slot_3_var_rareg, shop_slot_4_var_rareg, shop_slot_5_var_rareg, eins = reroll_Shop2(Spawning_klikdiklak1g, shop_slot_1_var_rareg, shop_slot_2_var_rareg, shop_slot_3_var_rareg, shop_slot_4_var_rareg, shop_slot_5_var_rareg, eins)

  Spawning_brokkolos1g, shop_slot_1_var_rareg, shop_slot_2_var_rareg, shop_slot_3_var_rareg, shop_slot_4_var_rareg, shop_slot_5_var_rareg, zwei = reroll_Shop2(Spawning_brokkolos1g, shop_slot_1_var_rareg, shop_slot_2_var_rareg, shop_slot_3_var_rareg, shop_slot_4_var_rareg, shop_slot_5_var_rareg, zwei)

  Spawning_maxax1g, shop_slot_1_var_rareg, shop_slot_2_var_rareg, shop_slot_3_var_rareg, shop_slot_4_var_rareg, shop_slot_5_var_rareg, drei = reroll_Shop2(Spawning_maxax1g, shop_slot_1_var_rareg, shop_slot_2_var_rareg, shop_slot_3_var_rareg, shop_slot_4_var_rareg, shop_slot_5_var_rareg, drei)

  Spawning_rabigator1g, shop_slot_1_var_epicg, shop_slot_2_var_epicg, shop_slot_3_var_epicg, shop_slot_4_var_epicg, shop_slot_5_var_epicg, eins = reroll_Shop2(Spawning_rabigator1g, shop_slot_1_var_epicg, shop_slot_2_var_epicg, shop_slot_3_var_epicg, shop_slot_4_var_epicg, shop_slot_5_var_epicg, eins)

  Spawning_stalobor21g, shop_slot_1_var_epicg, shop_slot_2_var_epicg, shop_slot_3_var_epicg, shop_slot_4_var_epicg, shop_slot_5_var_epicg, zwei = reroll_Shop2(Spawning_stalobor21g, shop_slot_1_var_epicg, shop_slot_2_var_epicg, shop_slot_3_var_epicg, shop_slot_4_var_epicg, shop_slot_5_var_epicg, zwei)

  Spawning_echnatoll21g, shop_slot_1_var_epicg, shop_slot_2_var_epicg, shop_slot_3_var_epicg, shop_slot_4_var_epicg, shop_slot_5_var_epicg, drei = reroll_Shop2(Spawning_echnatoll21g, shop_slot_1_var_epicg, shop_slot_2_var_epicg, shop_slot_3_var_epicg, shop_slot_4_var_epicg, shop_slot_5_var_epicg, drei)


  Spawning_serpiroyal1g, Spawning_flambirex1g, Spawning_admurai1g, eins, fünf, shop_slot_1_rarg, shop_slot_2_rarg, shop_slot_3_rarg, shop_slot_4_rarg, shop_slot_5_rarg = reroll_Shop3(Spawning_serpiroyal1g, Spawning_flambirex1g, Spawning_admurai1g, eins, fünf, shop_slot_1_rarg, shop_slot_2_rarg, shop_slot_3_rarg, shop_slot_4_rarg, shop_slot_5_rarg)

  Spawning_matrifol1g, Spawning_cerapendra1g, Spawning_meistagrif1g, fünf, acht, shop_slot_1_rarg, shop_slot_2_rarg, shop_slot_3_rarg, shop_slot_4_rarg, shop_slot_5_rarg = reroll_Shop3(Spawning_matrifol1g, Spawning_cerapendra1g, Spawning_meistagrif1g, fünf, acht, shop_slot_1_rarg, shop_slot_2_rarg, shop_slot_3_rarg, shop_slot_4_rarg, shop_slot_5_rarg)

  Spawning_klikdiklak1g, Spawning_brokkolos1g, Spawning_maxax1g, acht, zehn, shop_slot_1_rarg, shop_slot_2_rarg, shop_slot_3_rarg, shop_slot_4_rarg, shop_slot_5_rarg = reroll_Shop3(Spawning_klikdiklak1g, Spawning_brokkolos1g, Spawning_maxax1g, acht, zehn, shop_slot_1_rarg, shop_slot_2_rarg, shop_slot_3_rarg, shop_slot_4_rarg, shop_slot_5_rarg)


  gedrueckteTasten = pygame.key.get_pressed()
  if gedrueckteTasten[pygame.K_SPACE]:
    fight = True


  
  #gold_anzeige, screen = show_Gold(gold_anzeige, screen)
  
  
  'FPS-Anzeige' 
  clock.tick(10)
  #print(gold)
  #print(goldg)


  pygame.display.update()
