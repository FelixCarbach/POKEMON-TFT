'''mx, my = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 600 < my < 700 and Level1 == True and shop_slot_1_var_common == 1 and Spawning_serpifeu1 == False:
      Spawning_serpifeu1 = True
      show_Serpifeu1 = False
      serpifeu_x1 = 250
      serpifeu_y1 = 645
      shop_slot_1_var_common == 0
    elif pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 600 < my < 700 and Level1 == True and shop_slot_1_var_common == 1 and Spawning_serpifeu1 == True and Spawning_serpifeu2 == False:
      Spawning_serpifeu2 = True
      show_Serpifeu1 = False
      serpifeu_x2 = 250
      serpifeu_y2 = 645
      shop_slot_1_var_common == 0
    if pygame.mouse.get_pressed()[0]== True and Level1 == True and 0 < mx < 150 and 600 < my < 700 and shop_slot_1_var_common == 2 and Spawning_floink1 == False:
      Spawning_floink1= True
      show_Floink1 = False
      shop_slot_1_var_common == 0
    elif pygame.mouse.get_pressed()[0]== True and Level1 == True and 0 < mx < 150 and 600 < my < 700 and shop_slot_1_var_common == 2 and Spawning_floink1 == True and Spawning_floink2 == False:
      Spawning_floink2= True 
      show_Floink1 = False
      shop_slot_1_var_common == 0

    if pygame.mouse.get_pressed()[0]== True and Level1 == True and 0 < mx < 150 and 600 < my < 700 and shop_slot_1_var_common == 3 and Spawning_ottaro1 == False:
      Spawning_ottaro1= True
      show_Ottaro1= False
      shop_slot_1_var_common == 0
    elif pygame.mouse.get_pressed()[0]== True and Level1 == True and 0 < mx < 150 and 600 < my < 700 and shop_slot_1_var_common == 3 and Spawning_ottaro1 == True and Spawning_ottaro2 == False:
      Spawning_ottaro2= True 
      show_Ottaro1= False
      shop_slot_1_var_common == 0


    if Spawning_serpifeu1 == True:
      screen.blit(serpifeu1, (serpifeu_x1, serpifeu_y1))
    if Spawning_serpifeu2== True:
      screen.blit(serpifeu2, (serpifeu_x2, serpifeu_y2))

    if Spawning_floink1 == True:
      screen.blit(floink1, (floink_x1, floink_y1))
    if Spawning_floink1 == True:
      screen.blit(floink2, (floink_x2, floink_y2))

    if Spawning_ottaro1 == True:
      screen.blit(ottaro2, (ottaro_x2, ottaro_y2))'''








'''def spawn_Pokemon1_common(Spawning1, pokemon_x, pokemon_y, pokemon, screen, shop_slot_1_var_common, spawned):
  mx, my = pygame.mouse.get_pos()
  
  if pygame.mouse.get_pressed()[0]== True and 0 < mx < 150 and 600 < my < 700 and Level1 == True and shop_slot_1_rar in range (1,10) and shop_slot_1_var_common == 2:
    pokemon_x = 250
    pokemon_y = 645
    screen.blit(pokemon, (pokemon_x, pokemon_y))
    spawned = True

  if spawned:
    pokemon_x = 250
    pokemon_y = 645
    screen.blit(pokemon, (pokemon_x, pokemon_y))

  return Spawning1, pokemon_x, pokemon_y, pokemon, screen, shop_slot_1_var_common, spawned  '''     




  '''def sell_Pokemon(Spawning, pokemon_x, pokemon_y, zahl):
  if Spawning == True and pygame.mouse.get_pressed()[0]== False and 1500 - pokemon_x < 230 and 761 - pokemon_y < 191:
    Spawning = False
    pokemon_x = zahl
    pokemon_y = 0
  return Spawning, pokemon_x, pokemon_y, zahl'''