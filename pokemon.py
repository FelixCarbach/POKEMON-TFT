import pygame
from random import randint

Spawning_serpifeu1=False
Spawning_serpifeu2=False
Spawning_serpifeu3=False

Spawning_efoserp1=False
Spawning_efoserp2=False
Spawning_efoserp3=False

Spawning_serpiroyal1=False

Spawning_floink1=False
Spawning_floink2=False
Spawning_floink3=False

Spawning_ferkokel1 = False
Spawning_ferkokel2 = False
Spawning_ferkokel3 = False

Spawning_flambirex1 = False

Spawning_ottaro1=False
Spawning_ottaro2=False
Spawning_ottaro3=False

Spawning_zwottronin1=False
Spawning_zwottronin2=False
Spawning_zwottronin3=False

Spawning_admurai1=False

Spawning_strawickl1=False
Spawning_strawickl2=False
Spawning_strawickl3=False

Spawning_folikon1=False
Spawning_folikon2=False
Spawning_folikon3=False

Spawning_matrifol1=False

Spawning_toxiped1=False
Spawning_toxiped2=False
Spawning_toxiped3=False

Spawning_rollum1=False
Spawning_rollum2=False
Spawning_rollum3=False

Spawning_cerapendra1=False

Spawning_praktibalk1=False
Spawning_praktibalk2=False
Spawning_praktibalk3=False

Spawning_strepoli1=False
Spawning_strepoli2=False
Spawning_strepoli3=False

Spawning_meistagrif1=False

Spawning_klikk1=False
Spawning_klikk2=False
Spawning_klikk3=False

Spawning_kliklak1=False
Spawning_kliklak2=False
Spawning_kliklak3=False

Spawning_klikdiklak1=False

Spawning_kiesling1=False
Spawning_kiesling2=False
Spawning_kiesling3=False

Spawning_sedimantur1=False
Spawning_sedimantur2=False
Spawning_sedimantur3=False

Spawning_brokkolos1=False

Spawning_milza1=False
Spawning_milza2=False
Spawning_milza3=False

Spawning_sharfax1=False
Spawning_sharfax2=False
Spawning_sharfax3=False

Spawning_maxax1=False

Spawning_ganovil1=False
Spawning_ganovil2=False
Spawning_ganovil3=False

Spawning_rokkaiman1=False
Spawning_rokkaiman2=False
Spawning_rokkaiman3=False

Spawning_rabigator1=False

Spawning_rotomurf1=False
Spawning_rotomurf2=False
Spawning_rotomurf3=False

Spawning_stalobor1=False
Spawning_stalobor2=False
Spawning_stalobor3=False

Spawning_stalobor21=False

Spawning_makabaja1=False
Spawning_makabaja2=False
Spawning_makabaja3=False

Spawning_echnatoll1=False
Spawning_echnatoll2=False
Spawning_echnatoll3=False

Spawning_echnatoll21=False


ally_list = []



'#Einfügen von Pokemon'

serpifeu1 = pygame.image.load("POKEMON_Sprites/Back/SerpifeuB.png")
serpifeu_x1 = 1
serpifeu_y1 = 0

serpifeu2 = pygame.image.load("POKEMON_Sprites/Back/SerpifeuB.png")
serpifeu_x2 = 2
serpifeu_y2 = 0

serpifeu3 = pygame.image.load("POKEMON_Sprites/Back/SerpifeuB.png")
serpifeu_x3 = 3
serpifeu_y3 = 0

efoserp1 = pygame.image.load("POKEMON_Sprites/Back/EfoserpB.png")
efoserp_x1 = 4
efoserp_y1= 0

efoserp2 = pygame.image.load("POKEMON_Sprites/Back/EfoserpB.png")
efoserp_x2 = 5
efoserp_y2= 0

efoserp3 = pygame.image.load("POKEMON_Sprites/Back/EfoserpB.png")
efoserp_x3 = 6
efoserp_y3= 0

serpiroyal1 = pygame.image.load("POKEMON_Sprites/Back/SerpiroyalB.png")
serpiroyal_x1 = 7
serpiroyal_y1 = 0




floink1 = pygame.image.load("POKEMON_Sprites/Back/FloinkB.png")
floink_x1 = 8
floink_y1 = 0

floink2 = pygame.image.load("POKEMON_Sprites/Back/FloinkB.png")
floink_x2 = 9
floink_y2 = 0

floink3 = pygame.image.load("POKEMON_Sprites/Back/FloinkB.png")
floink_x3 = 10
floink_y3 = 0

ferkokel1 = pygame.image.load("POKEMON_Sprites/Back/FerkokelB.png")
ferkokel_x1 = 11
ferkokel_y1= 0

ferkokel2 = pygame.image.load("POKEMON_Sprites/Back/FerkokelB.png")
ferkokel_x2 = 12
ferkokel_y2 = 0

ferkokel3 = pygame.image.load("POKEMON_Sprites/Back/FerkokelB.png")
ferkokel_x3 = 13
ferkokel_y3 = 0

flambirex1 = pygame.image.load("POKEMON_Sprites/Back/FlambirexB.png")
flambirex_x1 = 14
flambirex_y1 = 0



ottaro1 = pygame.image.load("POKEMON_Sprites/Back/OttaroB.png")
ottaro_x1 = 15
ottaro_y1 = 0

ottaro2 = pygame.image.load("POKEMON_Sprites/Back/OttaroB.png")
ottaro_x2 = 16
ottaro_y2 = 0

ottaro3 = pygame.image.load("POKEMON_Sprites/Back/OttaroB.png")
ottaro_x3 = 17
ottaro_y3 = 0

zwottronin1 = pygame.image.load("POKEMON_Sprites/Back/ZwottroninB.png")
zwottronin_x1 = 18
zwottronin_y1 = 0

zwottronin2 = pygame.image.load("POKEMON_Sprites/Back/ZwottroninB.png")
zwottronin_x2 = 19
zwottronin_y2 = 0

zwottronin3 = pygame.image.load("POKEMON_Sprites/Back/ZwottroninB.png")
zwottronin_x3 = 20
zwottronin_y3 = 0

admurai1 = pygame.image.load("POKEMON_Sprites/Back/AdmuraiB.png")
admurai_x1 = 21
admurai_y1 = 0



strawickl1 = pygame.image.load("POKEMON_Sprites/Back/StrawicklB.png")
strawickl_x1 = 22
strawickl_y1 = 0

strawickl2 = pygame.image.load("POKEMON_Sprites/Back/StrawicklB.png")
strawickl_x2 = 23
strawickl_y2 = 0

strawickl3 = pygame.image.load("POKEMON_Sprites/Back/StrawicklB.png")
strawickl_x3 = 24
strawickl_y3 = 0

folikon1 = pygame.image.load("POKEMON_Sprites/Back/FolikonB.png")
folikon_x1 = 25
folikon_y1= 0

folikon2 = pygame.image.load("POKEMON_Sprites/Back/FolikonB.png")
folikon_x2 = 26
folikon_y2= 0

folikon3 = pygame.image.load("POKEMON_Sprites/Back/FolikonB.png")
folikon_x3 = 27
folikon_y3= 0

matrifol1 = pygame.image.load("POKEMON_Sprites/Back/MatrifolB.png")
matrifol_x1 = 28
matrifol_y1 = 0


toxiped1 = pygame.image.load("POKEMON_Sprites/Back/ToxipedB.png")
toxiped_x1 = 29
toxiped_y1 = 0

toxiped2 = pygame.image.load("POKEMON_Sprites/Back/ToxipedB.png")
toxiped_x2 = 30
toxiped_y2 = 0

toxiped3 = pygame.image.load("POKEMON_Sprites/Back/ToxipedB.png")
toxiped_x3 = 31
toxiped_y3 = 0

rollum1 = pygame.image.load("POKEMON_Sprites/Back/RollumB.png")
rollum_x1 = 32
rollum_y1= 0

rollum2 = pygame.image.load("POKEMON_Sprites/Back/RollumB.png")
rollum_x2 = 33
rollum_y2= 0

rollum3 = pygame.image.load("POKEMON_Sprites/Back/RollumB.png")
rollum_x3 = 34
rollum_y3= 0

cerapendra1 = pygame.image.load("POKEMON_Sprites/Back/CerapendraB.png")
cerapendra_x1 = 35
cerapendra_y1 = 0


praktibalk1 = pygame.image.load("POKEMON_Sprites/Back/PraktibalkB.png")
praktibalk_x1 = 36
praktibalk_y1 = 0

praktibalk2 = pygame.image.load("POKEMON_Sprites/Back/PraktibalkB.png")
praktibalk_x2 = 37
praktibalk_y2 = 0

praktibalk3 = pygame.image.load("POKEMON_Sprites/Back/PraktibalkB.png")
praktibalk_x3 = 38
praktibalk_y3 = 0

strepoli1 = pygame.image.load("POKEMON_Sprites/Back/StrepoliB.png")
strepoli_x1 = 39
strepoli_y1= 0

strepoli2 = pygame.image.load("POKEMON_Sprites/Back/StrepoliB.png")
strepoli_x2 = 40
strepoli_y2= 0

strepoli3 = pygame.image.load("POKEMON_Sprites/Back/StrepoliB.png")
strepoli_x3 = 41
strepoli_y3= 0

meistagrif1 = pygame.image.load("POKEMON_Sprites/Back/MeistagrifB.png")
meistagrif_x1 = 42
meistagrif_y1 = 0


klikk1 = pygame.image.load("POKEMON_Sprites/Back/KlikkB.png")
klikk_x1 = 43
klikk_y1 = 0

klikk2 = pygame.image.load("POKEMON_Sprites/Back/KlikkB.png")
klikk_x2 = 44
klikk_y2 = 0

klikk3 = pygame.image.load("POKEMON_Sprites/Back/KlikkB.png")
klikk_x3 = 45
klikk_y3 = 0

kliklak1 = pygame.image.load("POKEMON_Sprites/Back/KliklakB.png")
kliklak_x1 = 46
kliklak_y1= 0

kliklak2 = pygame.image.load("POKEMON_Sprites/Back/KliklakB.png")
kliklak_x2 = 47
kliklak_y2= 0

kliklak3 = pygame.image.load("POKEMON_Sprites/Back/KliklakB.png")
kliklak_x3 = 48
kliklak_y3= 0

klikdiklak1 = pygame.image.load("POKEMON_Sprites/Back/KlikdiklakB.png")
klikdiklak_x1 = 49
klikdiklak_y1 = 0


kiesling1 = pygame.image.load("POKEMON_Sprites/Back/KieslingB.png")
kiesling_x1 = 50
kiesling_y1 = 0

kiesling2 = pygame.image.load("POKEMON_Sprites/Back/KieslingB.png")
kiesling_x2 = 51
kiesling_y2 = 0

kiesling3 = pygame.image.load("POKEMON_Sprites/Back/KieslingB.png")
kiesling_x3 = 52
kiesling_y3 = 0

sedimantur1 = pygame.image.load("POKEMON_Sprites/Back/SedimanturB.png")
sedimantur_x1 = 53
sedimantur_y1= 0

sedimantur2 = pygame.image.load("POKEMON_Sprites/Back/SedimanturB.png")
sedimantur_x2 = 54
sedimantur_y2= 0

sedimantur3 = pygame.image.load("POKEMON_Sprites/Back/SedimanturB.png")
sedimantur_x3 = 55
sedimantur_y3= 0

brokkolos1 = pygame.image.load("POKEMON_Sprites/Back/BrokkolosB.png")
brokkolos_x1 = 56
brokkolos_y1 = 0


milza1 = pygame.image.load("POKEMON_Sprites/Back/MilzaB.png")
milza_x1 = 57
milza_y1 = 0

milza2 = pygame.image.load("POKEMON_Sprites/Back/MilzaB.png")
milza_x2 = 58
milza_y2 = 0

milza3 = pygame.image.load("POKEMON_Sprites/Back/MilzaB.png")
milza_x3 = 59
milza_y3 = 0

sharfax1 = pygame.image.load("POKEMON_Sprites/Back/SharfaxB.png")
sharfax_x1 = 60
sharfax_y1= 0

sharfax2 = pygame.image.load("POKEMON_Sprites/Back/SharfaxB.png")
sharfax_x2 = 61
sharfax_y2= 0

sharfax3 = pygame.image.load("POKEMON_Sprites/Back/SharfaxB.png")
sharfax_x3 = 62
sharfax_y3= 0

maxax1 = pygame.image.load("POKEMON_Sprites/Back/MaxaxB.png")
maxax_x1 = 63
maxax_y1 = 0


ganovil1 = pygame.image.load("POKEMON_Sprites/Back/GanovilB.png")
ganovil_x1 = 64
ganovil_y1 = 0

ganovil2 = pygame.image.load("POKEMON_Sprites/Back/GanovilB.png")
ganovil_x2 = 65
ganovil_y2 = 0

ganovil3 = pygame.image.load("POKEMON_Sprites/Back/GanovilB.png")
ganovil_x3 = 66
ganovil_y3 = 0

rokkaiman1 = pygame.image.load("POKEMON_Sprites/Back/RokkaimanB.png")
rokkaiman_x1 = 67
rokkaiman_y1= 0

rokkaiman2 = pygame.image.load("POKEMON_Sprites/Back/RokkaimanB.png")
rokkaiman_x2 = 68
rokkaiman_y2= 0

rokkaiman3 = pygame.image.load("POKEMON_Sprites/Back/RokkaimanB.png")
rokkaiman_x3 = 69
rokkaiman_y3= 0

rabigator1 = pygame.image.load("POKEMON_Sprites/Back/RabigatorB.png")
rabigator_x1 = 70
rabigator_y1 = 0


rotomurf1 = pygame.image.load("POKEMON_Sprites/Back/RotomurfB.png")
rotomurf_x1 = 71
rotomurf_y1 = 0

rotomurf2 = pygame.image.load("POKEMON_Sprites/Back/RotomurfB.png")
rotomurf_x2 = 72
rotomurf_y2 = 0

rotomurf3 = pygame.image.load("POKEMON_Sprites/Back/RotomurfB.png")
rotomurf_x3 = 73
rotomurf_y3 = 0

stalobor1 = pygame.image.load("POKEMON_Sprites/Back/StaloborB.png")
stalobor_x1 = 74
stalobor_y1= 0

stalobor2 = pygame.image.load("POKEMON_Sprites/Back/StaloborB.png")
stalobor_x2 = 75
stalobor_y2= 0

stalobor3 = pygame.image.load("POKEMON_Sprites/Back/StaloborB.png")
stalobor_x3 = 76
stalobor_y3= 0

stalobor21 = pygame.image.load("POKEMON_Sprites/Back/Stalobor2B.png")
stalobor2_x1 = 77
stalobor2_y1 = 0


makabaja1 = pygame.image.load("POKEMON_Sprites/Back/MakabajaB.png")
makabaja_x1 = 78
makabaja_y1 = 0

makabaja2 = pygame.image.load("POKEMON_Sprites/Back/MakabajaB.png")
makabaja_x2 = 79
makabaja_y2 = 0

makabaja3 = pygame.image.load("POKEMON_Sprites/Back/MakabajaB.png")
makabaja_x3 = 80
makabaja_y3 = 0

echnatoll1 = pygame.image.load("POKEMON_Sprites/Back/EchnatollB.png")
echnatoll_x1 = 81
echnatoll_y1= 0

echnatoll2 = pygame.image.load("POKEMON_Sprites/Back/EchnatollB.png")
echnatoll_x2 = 82
echnatoll_y2= 0

echnatoll3 = pygame.image.load("POKEMON_Sprites/Back/EchnatollB.png")
echnatoll_x3 = 83
echnatoll_y3= 0

echnatoll21 = pygame.image.load("POKEMON_Sprites/Back/Echnatoll2B.png")
echnatoll2_x1 = 84
echnatoll2_y1 = 0



pokemon_Liste=[(serpifeu_x1, serpifeu_y1), (serpifeu_x2, serpifeu_y2), (serpifeu_x3, serpifeu_y3), (efoserp_x1, efoserp_y1), (efoserp_x2, efoserp_y2), (efoserp_x3, efoserp_y3), (serpiroyal_x1, serpiroyal_y1), (floink_x1, floink_y1), (floink_x2, floink_y2), (floink_x3, floink_y3), (ferkokel_x1, ferkokel_y1), (ferkokel_x2, ferkokel_y2), (ferkokel_x3, ferkokel_y3), (flambirex_x1, flambirex_y1), (ottaro_x1, ottaro_y1), (ottaro_x2, ottaro_y2), (ottaro_x3, ottaro_y3), (zwottronin_x1, zwottronin_y1), (zwottronin_x2, zwottronin_y2), (zwottronin_x3, zwottronin_y3), (admurai_x1, admurai_y1)]

pokemon_Liste2=[serpifeu_x1, serpifeu_x2, serpifeu_x3, floink_x1, ottaro_x1]







'#Einfügen von Shop-Pokemon'

'Shop-Slot 1'
serpifeu_shop1 = pygame.image.load("POKEMON-SHOP_Sprites/serpifeu_shop.png")
serpifeu_shop_x1 = 0
serpifeu_shop_y1 = 600

floink_shop1 = pygame.image.load("POKEMON-SHOP_Sprites/floink_shop.png")
floink_shop_x1 = 0
floink_shop_y1 = 600

ottaro_shop1 = pygame.image.load("POKEMON-SHOP_Sprites/ottaro_shop.png")
ottaro_shop_x1 = 0
ottaro_shop_y1 = 600

strawickl_shop1 = pygame.image.load("POKEMON-SHOP_Sprites/strawickl_shop.png")
strawickl_shop_x1 = 0
strawickl_shop_y1 = 600

toxiped_shop1 = pygame.image.load("POKEMON-SHOP_Sprites/toxiped_shop.png")
toxiped_shop_x1 = 0
toxiped_shop_y1 = 600

praktibalk_shop1 = pygame.image.load("POKEMON-SHOP_Sprites/praktibalk_shop.png")
praktibalk_shop_x1 = 0
praktibalk_shop_y1 = 600

klikk_shop1 = pygame.image.load("POKEMON-SHOP_Sprites/klikk_shop.png")
klikk_shop_x1 = 0
klikk_shop_y1 = 600

kiesling_shop1 = pygame.image.load("POKEMON-SHOP_Sprites/kiesling_shop.png")
kiesling_shop_x1 = 0
kiesling_shop_y1 = 600

milza_shop1 = pygame.image.load("POKEMON-SHOP_Sprites/milza_shop.png")
milza_shop_x1 = 0
milza_shop_y1 = 600

ganovil_shop1 = pygame.image.load("POKEMON-SHOP_Sprites/ganovil_shop.png")
ganovil_shop_x1 = 0
ganovil_shop_y1 = 600

rotomurf_shop1 = pygame.image.load("POKEMON-SHOP_Sprites/rotomurf_shop.png")
rotomurf_shop_x1 = 0
rotomurf_shop_y1 = 600

makabaja_shop1 = pygame.image.load("POKEMON-SHOP_Sprites/makabaja_shop.png")
makabaja_shop_x1 = 0
makabaja_shop_y1 = 600

'Shop-Slot 2'

serpifeu_shop2 = pygame.image.load("POKEMON-SHOP_Sprites/serpifeu_shop.png")
serpifeu_shop_x2 = 0
serpifeu_shop_y2 = 500

floink_shop2 = pygame.image.load("POKEMON-SHOP_Sprites/floink_shop.png")
floink_shop_x2 = 0
floink_shop_y2 = 500

ottaro_shop2 = pygame.image.load("POKEMON-SHOP_Sprites/ottaro_shop.png")
ottaro_shop_x2 = 0
ottaro_shop_y2 = 500

strawickl_shop2 = pygame.image.load("POKEMON-SHOP_Sprites/strawickl_shop.png")
strawickl_shop_x2 = 0
strawickl_shop_y2 = 500

toxiped_shop2 = pygame.image.load("POKEMON-SHOP_Sprites/toxiped_shop.png")
toxiped_shop_x2 = 0
toxiped_shop_y2 = 500

praktibalk_shop2 = pygame.image.load("POKEMON-SHOP_Sprites/praktibalk_shop.png")
praktibalk_shop_x2 = 0
praktibalk_shop_y2 = 500

klikk_shop2 = pygame.image.load("POKEMON-SHOP_Sprites/klikk_shop.png")
klikk_shop_x2 = 0
klikk_shop_y2 = 500

kiesling_shop2 = pygame.image.load("POKEMON-SHOP_Sprites/kiesling_shop.png")
kiesling_shop_x2 = 0
kiesling_shop_y2 = 500

milza_shop2 = pygame.image.load("POKEMON-SHOP_Sprites/milza_shop.png")
milza_shop_x2 = 0
milza_shop_y2 = 500

ganovil_shop2 = pygame.image.load("POKEMON-SHOP_Sprites/ganovil_shop.png")
ganovil_shop_x2 = 0
ganovil_shop_y2 = 500

rotomurf_shop2 = pygame.image.load("POKEMON-SHOP_Sprites/rotomurf_shop.png")
rotomurf_shop_x2 = 0
rotomurf_shop_y2 = 500

makabaja_shop2 = pygame.image.load("POKEMON-SHOP_Sprites/makabaja_shop.png")
makabaja_shop_x2 = 0
makabaja_shop_y2 = 500

'Shop-Slot 3'

serpifeu_shop3 = pygame.image.load("POKEMON-SHOP_Sprites/serpifeu_shop.png")
serpifeu_shop_x3 = 0
serpifeu_shop_y3 = 400

floink_shop3 = pygame.image.load("POKEMON-SHOP_Sprites/floink_shop.png")
floink_shop_x3 = 0
floink_shop_y3 = 400

ottaro_shop3 = pygame.image.load("POKEMON-SHOP_Sprites/ottaro_shop.png")
ottaro_shop_x3 = 0
ottaro_shop_y3 = 400

strawickl_shop3 = pygame.image.load("POKEMON-SHOP_Sprites/strawickl_shop.png")
strawickl_shop_x3 = 0
strawickl_shop_y3 = 400

toxiped_shop3 = pygame.image.load("POKEMON-SHOP_Sprites/toxiped_shop.png")
toxiped_shop_x3 = 0
toxiped_shop_y3 = 400

praktibalk_shop3 = pygame.image.load("POKEMON-SHOP_Sprites/praktibalk_shop.png")
praktibalk_shop_x3 = 0
praktibalk_shop_y3 = 400

klikk_shop3 = pygame.image.load("POKEMON-SHOP_Sprites/klikk_shop.png")
klikk_shop_x3 = 0
klikk_shop_y3 = 400

kiesling_shop3 = pygame.image.load("POKEMON-SHOP_Sprites/kiesling_shop.png")
kiesling_shop_x3 = 0
kiesling_shop_y3 = 400

milza_shop3 = pygame.image.load("POKEMON-SHOP_Sprites/milza_shop.png")
milza_shop_x3 = 0
milza_shop_y3 = 400

ganovil_shop3 = pygame.image.load("POKEMON-SHOP_Sprites/ganovil_shop.png")
ganovil_shop_x3 = 0
ganovil_shop_y3 = 400

rotomurf_shop3 = pygame.image.load("POKEMON-SHOP_Sprites/rotomurf_shop.png")
rotomurf_shop_x3 = 0
rotomurf_shop_y3 = 400

makabaja_shop3 = pygame.image.load("POKEMON-SHOP_Sprites/makabaja_shop.png")
makabaja_shop_x3 = 0
makabaja_shop_y3 = 400

'Shop-Slot 4'

serpifeu_shop4 = pygame.image.load("POKEMON-SHOP_Sprites/serpifeu_shop.png")
serpifeu_shop_x4 = 0
serpifeu_shop_y4 = 300

floink_shop4 = pygame.image.load("POKEMON-SHOP_Sprites/floink_shop.png")
floink_shop_x4 = 0
floink_shop_y4 = 300

ottaro_shop4 = pygame.image.load("POKEMON-SHOP_Sprites/ottaro_shop.png")
ottaro_shop_x4 = 0
ottaro_shop_y4 = 300

strawickl_shop4 = pygame.image.load("POKEMON-SHOP_Sprites/strawickl_shop.png")
strawickl_shop_x4 = 0
strawickl_shop_y4 = 300

toxiped_shop4 = pygame.image.load("POKEMON-SHOP_Sprites/toxiped_shop.png")
toxiped_shop_x4 = 0
toxiped_shop_y4 = 300

praktibalk_shop4 = pygame.image.load("POKEMON-SHOP_Sprites/praktibalk_shop.png")
praktibalk_shop_x4 = 0
praktibalk_shop_y4 = 300

klikk_shop4 = pygame.image.load("POKEMON-SHOP_Sprites/klikk_shop.png")
klikk_shop_x4 = 0
klikk_shop_y4 = 300

kiesling_shop4 = pygame.image.load("POKEMON-SHOP_Sprites/kiesling_shop.png")
kiesling_shop_x4 = 0
kiesling_shop_y4 = 300

milza_shop4 = pygame.image.load("POKEMON-SHOP_Sprites/milza_shop.png")
milza_shop_x4 = 0
milza_shop_y4 = 300

ganovil_shop4 = pygame.image.load("POKEMON-SHOP_Sprites/ganovil_shop.png")
ganovil_shop_x4 = 0
ganovil_shop_y4 = 300

rotomurf_shop4 = pygame.image.load("POKEMON-SHOP_Sprites/rotomurf_shop.png")
rotomurf_shop_x4 = 0
rotomurf_shop_y4 = 300

makabaja_shop4 = pygame.image.load("POKEMON-SHOP_Sprites/makabaja_shop.png")
makabaja_shop_x4 = 0
makabaja_shop_y4 = 300

'Shop-Slot 5'

serpifeu_shop5 = pygame.image.load("POKEMON-SHOP_Sprites/serpifeu_shop.png")
serpifeu_shop_x5 = 0
serpifeu_shop_y5 = 200

floink_shop5 = pygame.image.load("POKEMON-SHOP_Sprites/floink_shop.png")
floink_shop_x5 = 0
floink_shop_y5 = 200

ottaro_shop5 = pygame.image.load("POKEMON-SHOP_Sprites/ottaro_shop.png")
ottaro_shop_x5 = 0
ottaro_shop_y5 = 200

strawickl_shop5 = pygame.image.load("POKEMON-SHOP_Sprites/strawickl_shop.png")
strawickl_shop_x5 = 0
strawickl_shop_y5 = 200

toxiped_shop5 = pygame.image.load("POKEMON-SHOP_Sprites/toxiped_shop.png")
toxiped_shop_x5 = 0
toxiped_shop_y5 = 200

praktibalk_shop5 = pygame.image.load("POKEMON-SHOP_Sprites/praktibalk_shop.png")
praktibalk_shop_x5 = 0
praktibalk_shop_y5 = 200

klikk_shop5 = pygame.image.load("POKEMON-SHOP_Sprites/klikk_shop.png")
klikk_shop_x5 = 0
klikk_shop_y5 = 200

kiesling_shop5 = pygame.image.load("POKEMON-SHOP_Sprites/kiesling_shop.png")
kiesling_shop_x5 = 0
kiesling_shop_y5 = 200

milza_shop5 = pygame.image.load("POKEMON-SHOP_Sprites/milza_shop.png")
milza_shop_x5 = 0
milza_shop_y5 = 200

ganovil_shop5 = pygame.image.load("POKEMON-SHOP_Sprites/ganovil_shop.png")
ganovil_shop_x5 = 0
ganovil_shop_y5 = 200

rotomurf_shop5 = pygame.image.load("POKEMON-SHOP_Sprites/rotomurf_shop.png")
rotomurf_shop_x5 = 0
rotomurf_shop_y5 = 200

makabaja_shop5 = pygame.image.load("POKEMON-SHOP_Sprites/makabaja_shop.png")
makabaja_shop_x5 = 0
makabaja_shop_y5 = 200














Spawning_serpifeu1g=False
Spawning_serpifeu2g=False
Spawning_serpifeu3g=False

Spawning_efoserp1g=False
Spawning_efoserp2g=False
Spawning_efoserp3g=False

Spawning_serpiroyal1g=False

Spawning_floink1g=False
Spawning_floink2g=False
Spawning_floink3g=False

Spawning_ferkokel1g = False
Spawning_ferkokel2g = False
Spawning_ferkokel3g = False

Spawning_flambirex1g = False

Spawning_ottaro1g=False
Spawning_ottaro2g=False
Spawning_ottaro3g=False

Spawning_zwottronin1g=False
Spawning_zwottronin2g=False
Spawning_zwottronin3g=False

Spawning_admurai1g=False

Spawning_strawickl1g=False
Spawning_strawickl2g=False
Spawning_strawickl3g=False

Spawning_folikon1g=False
Spawning_folikon2g=False
Spawning_folikon3g=False

Spawning_matrifol1g=False

Spawning_toxiped1g=False
Spawning_toxiped2g=False
Spawning_toxiped3g=False

Spawning_rollum1g=False
Spawning_rollum2g=False
Spawning_rollum3g=False

Spawning_cerapendra1g=False

Spawning_praktibalk1g=False
Spawning_praktibalk2g=False
Spawning_praktibalk3g=False

Spawning_strepoli1g=False
Spawning_strepoli2g=False
Spawning_strepoli3g=False

Spawning_meistagrif1g=False

Spawning_klikk1g=False
Spawning_klikk2g=False
Spawning_klikk3g=False

Spawning_kliklak1g=False
Spawning_kliklak2g=False
Spawning_kliklak3g=False

Spawning_klikdiklak1g=False

Spawning_kiesling1g=False
Spawning_kiesling2g=False
Spawning_kiesling3g=False

Spawning_sedimantur1g=False
Spawning_sedimantur2g=False
Spawning_sedimantur3g=False

Spawning_brokkolos1g=False

Spawning_milza1g=False
Spawning_milza2g=False
Spawning_milza3g=False

Spawning_sharfax1g=False
Spawning_sharfax2g=False
Spawning_sharfax3g=False

Spawning_maxax1g=False

Spawning_ganovil1g=False
Spawning_ganovil2g=False
Spawning_ganovil3g=False

Spawning_rokkaiman1g=False
Spawning_rokkaiman2g=False
Spawning_rokkaiman3g=False

Spawning_rabigator1g=False

Spawning_rotomurf1g=False
Spawning_rotomurf2g=False
Spawning_rotomurf3g=False

Spawning_stalobor1g=False
Spawning_stalobor2g=False
Spawning_stalobor3g=False

Spawning_stalobor21g=False

Spawning_makabaja1g=False
Spawning_makabaja2g=False
Spawning_makabaja3g=False

Spawning_echnatoll1g=False
Spawning_echnatoll2g=False
Spawning_echnatoll3g=False

Spawning_echnatoll21g=False


enemy_list = []

'#Einfügen von Pokemon'

serpifeu1g = pygame.image.load("POKEMON_Sprites/Front/Serpifeu.png")
serpifeu_x1g = 1
serpifeu_y1g = 0

serpifeu2g = pygame.image.load("POKEMON_Sprites/Front/Serpifeu.png")
serpifeu_x2g = 2
serpifeu_y2g = 0

serpifeu3g = pygame.image.load("POKEMON_Sprites/Front/Serpifeu.png")
serpifeu_x3g = 3
serpifeu_y3g = 0

efoserp1g = pygame.image.load("POKEMON_Sprites/Front/Efoserp.png")
efoserp_x1g = 4
efoserp_y1g = 0

efoserp2g = pygame.image.load("POKEMON_Sprites/Front/Efoserp.png")
efoserp_x2g = 5
efoserp_y2g= 0

efoserp3g = pygame.image.load("POKEMON_Sprites/Front/Efoserp.png")
efoserp_x3g = 6
efoserp_y3g= 0

serpiroyal1g = pygame.image.load("POKEMON_Sprites/Front/Serpiroyal.png")
serpiroyal_x1g = 7
serpiroyal_y1g = 0



floink1g = pygame.image.load("POKEMON_Sprites/Front/floink.png")
floink_x1g = 8
floink_y1g = 0

floink2g = pygame.image.load("POKEMON_Sprites/Front/floink.png")
floink_x2g = 9
floink_y2g = 0

floink3g = pygame.image.load("POKEMON_Sprites/Front/floink.png")
floink_x3g = 10
floink_y3g = 0

ferkokel1g = pygame.image.load("POKEMON_Sprites/Front/Ferkokel.png")
ferkokel_x1g = 11
ferkokel_y1g = 0

ferkokel2g = pygame.image.load("POKEMON_Sprites/Front/Ferkokel.png")
ferkokel_x2g = 12
ferkokel_y2g = 0

ferkokel3g = pygame.image.load("POKEMON_Sprites/Front/Ferkokel.png")
ferkokel_x3g = 13
ferkokel_y3g = 0

flambirex1g = pygame.image.load("POKEMON_Sprites/Front/Flambirex.png")
flambirex_x1g = 14
flambirex_y1g = 0



ottaro1g = pygame.image.load("POKEMON_Sprites/Front/Ottaro.png")
ottaro_x1g = 15
ottaro_y1g = 0

ottaro2g = pygame.image.load("POKEMON_Sprites/Front/Ottaro.png")
ottaro_x2g = 16
ottaro_y2g = 0

ottaro3g = pygame.image.load("POKEMON_Sprites/Front/Ottaro.png")
ottaro_x3g = 17
ottaro_y3g = 0

zwottronin1g = pygame.image.load("POKEMON_Sprites/Front/Zwottronin.png")
zwottronin_x1g = 18
zwottronin_y1g = 0

zwottronin2g = pygame.image.load("POKEMON_Sprites/Front/Zwottronin.png")
zwottronin_x2g = 19
zwottronin_y2g = 0

zwottronin3g = pygame.image.load("POKEMON_Sprites/Front/Zwottronin.png")
zwottronin_x3g = 20
zwottronin_y3g = 0

admurai1g = pygame.image.load("POKEMON_Sprites/Front/Admurai.png")
admurai_x1g = 21
admurai_y1g = 0



strawickl1g = pygame.image.load("POKEMON_Sprites/Front/Strawickl.png")
strawickl_x1g = 22
strawickl_y1g = 0

strawickl2g = pygame.image.load("POKEMON_Sprites/Front/Strawickl.png")
strawickl_x2g = 23
strawickl_y2g = 0

strawickl3g = pygame.image.load("POKEMON_Sprites/Front/Strawickl.png")
strawickl_x3g = 24
strawickl_y3g = 0

folikon1g = pygame.image.load("POKEMON_Sprites/Front/Folikon.png")
folikon_x1g = 25
folikon_y1g = 0

folikon2g = pygame.image.load("POKEMON_Sprites/Front/Folikon.png")
folikon_x2g = 26
folikon_y2g= 0

folikon3g = pygame.image.load("POKEMON_Sprites/Front/Folikon.png")
folikon_x3g = 27
folikon_y3g= 0

matrifol1g = pygame.image.load("POKEMON_Sprites/Front/Matrifol.png")
matrifol_x1g = 28
matrifol_y1g = 0


toxiped1g = pygame.image.load("POKEMON_Sprites/Front/Toxiped.png")
toxiped_x1g = 29
toxiped_y1g = 0

toxiped2g = pygame.image.load("POKEMON_Sprites/Front/Toxiped.png")
toxiped_x2g = 30
toxiped_y2g = 0

toxiped3g = pygame.image.load("POKEMON_Sprites/Front/Toxiped.png")
toxiped_x3g = 31
toxiped_y3g = 0

rollum1g = pygame.image.load("POKEMON_Sprites/Front/Rollum.png")
rollum_x1g = 32
rollum_y1g = 0

rollum2g = pygame.image.load("POKEMON_Sprites/Front/Rollum.png")
rollum_x2g = 33
rollum_y2g= 0

rollum3g = pygame.image.load("POKEMON_Sprites/Front/Rollum.png")
rollum_x3g = 34
rollum_y3g= 0

cerapendra1g = pygame.image.load("POKEMON_Sprites/Front/Cerapendra.png")
cerapendra_x1g = 35
cerapendra_y1g = 0


praktibalk1g = pygame.image.load("POKEMON_Sprites/Front/Praktibalk.png")
praktibalk_x1g = 36
praktibalk_y1g = 0

praktibalk2g = pygame.image.load("POKEMON_Sprites/Front/Praktibalk.png")
praktibalk_x2g = 37
praktibalk_y2g = 0

praktibalk3g = pygame.image.load("POKEMON_Sprites/Front/Praktibalk.png")
praktibalk_x3g = 38
praktibalk_y3g = 0

strepoli1g = pygame.image.load("POKEMON_Sprites/Front/Strepoli.png")
strepoli_x1g = 39
strepoli_y1g = 0

strepoli2g = pygame.image.load("POKEMON_Sprites/Front/Strepoli.png")
strepoli_x2g = 40
strepoli_y2g= 0

strepoli3g = pygame.image.load("POKEMON_Sprites/Front/Strepoli.png")
strepoli_x3g = 41
strepoli_y3g= 0

meistagrif1g = pygame.image.load("POKEMON_Sprites/Front/Meistagrif.png")
meistagrif_x1g = 42
meistagrif_y1g = 0


klikk1g = pygame.image.load("POKEMON_Sprites/Front/Klikk.png")
klikk_x1g = 43
klikk_y1g = 0

klikk2g = pygame.image.load("POKEMON_Sprites/Front/Klikk.png")
klikk_x2g = 44
klikk_y2g = 0

klikk3g = pygame.image.load("POKEMON_Sprites/Front/Klikk.png")
klikk_x3g = 45
klikk_y3g = 0

kliklak1g = pygame.image.load("POKEMON_Sprites/Front/Kliklak.png")
kliklak_x1g = 46
kliklak_y1g = 0

kliklak2g = pygame.image.load("POKEMON_Sprites/Front/Kliklak.png")
kliklak_x2g = 47
kliklak_y2g= 0

kliklak3g = pygame.image.load("POKEMON_Sprites/Front/Kliklak.png")
kliklak_x3g = 48
kliklak_y3g= 0

klikdiklak1g = pygame.image.load("POKEMON_Sprites/Front/Klikdiklak.png")
klikdiklak_x1g = 49
klikdiklak_y1g = 0


kiesling1g = pygame.image.load("POKEMON_Sprites/Front/Kiesling.png")
kiesling_x1g = 50
kiesling_y1g = 0

kiesling2g = pygame.image.load("POKEMON_Sprites/Front/Kiesling.png")
kiesling_x2g = 51
kiesling_y2g = 0

kiesling3g = pygame.image.load("POKEMON_Sprites/Front/Kiesling.png")
kiesling_x3g = 52
kiesling_y3g = 0

sedimantur1g = pygame.image.load("POKEMON_Sprites/Front/Sedimantur.png")
sedimantur_x1g = 53
sedimantur_y1g = 0

sedimantur2g = pygame.image.load("POKEMON_Sprites/Front/Sedimantur.png")
sedimantur_x2g = 54
sedimantur_y2g= 0

sedimantur3g = pygame.image.load("POKEMON_Sprites/Front/Sedimantur.png")
sedimantur_x3g = 55
sedimantur_y3g= 0

brokkolos1g = pygame.image.load("POKEMON_Sprites/Front/Brokkolos.png")
brokkolos_x1g = 56
brokkolos_y1g = 0


milza1g = pygame.image.load("POKEMON_Sprites/Front/Milza.png")
milza_x1g = 57
milza_y1g = 0

milza2g = pygame.image.load("POKEMON_Sprites/Front/Milza.png")
milza_x2g = 58
milza_y2g = 0

milza3g = pygame.image.load("POKEMON_Sprites/Front/Milza.png")
milza_x3g = 59
milza_y3g = 0

sharfax1g = pygame.image.load("POKEMON_Sprites/Front/Sharfax.png")
sharfax_x1g = 69
sharfax_y1g = 0

sharfax2g = pygame.image.load("POKEMON_Sprites/Front/Sharfax.png")
sharfax_x2g = 61
sharfax_y2g= 0

sharfax3g = pygame.image.load("POKEMON_Sprites/Front/Sharfax.png")
sharfax_x3g = 62
sharfax_y3g= 0

maxax1g = pygame.image.load("POKEMON_Sprites/Front/Maxax.png")
maxax_x1g = 63
maxax_y1g = 0


ganovil1g = pygame.image.load("POKEMON_Sprites/Front/Ganovil.png")
ganovil_x1g = 64
ganovil_y1g = 0

ganovil2g = pygame.image.load("POKEMON_Sprites/Front/Ganovil.png")
ganovil_x2g = 65
ganovil_y2g = 0

ganovil3g = pygame.image.load("POKEMON_Sprites/Front/Ganovil.png")
ganovil_x3g = 66
ganovil_y3g = 0

rokkaiman1g = pygame.image.load("POKEMON_Sprites/Front/Rokkaiman.png")
rokkaiman_x1g = 67
rokkaiman_y1g = 0

rokkaiman2g = pygame.image.load("POKEMON_Sprites/Front/Rokkaiman.png")
rokkaiman_x2g = 68
rokkaiman_y2g= 0

rokkaiman3g = pygame.image.load("POKEMON_Sprites/Front/Rokkaiman.png")
rokkaiman_x3g = 69
rokkaiman_y3g= 0

rabigator1g = pygame.image.load("POKEMON_Sprites/Front/Rabigator.png")
rabigator_x1g = 70
rabigator_y1g = 0


rotomurf1g = pygame.image.load("POKEMON_Sprites/Front/Rotomurf.png")
rotomurf_x1g = 71
rotomurf_y1g = 0

rotomurf2g = pygame.image.load("POKEMON_Sprites/Front/Rotomurf.png")
rotomurf_x2g = 72
rotomurf_y2g = 0

rotomurf3g = pygame.image.load("POKEMON_Sprites/Front/Rotomurf.png")
rotomurf_x3g = 73
rotomurf_y3g = 0

stalobor1g = pygame.image.load("POKEMON_Sprites/Front/Stalobor.png")
stalobor_x1g = 74
stalobor_y1g = 0

stalobor2g = pygame.image.load("POKEMON_Sprites/Front/Stalobor.png")
stalobor_x2g = 75
stalobor_y2g= 0

stalobor3g = pygame.image.load("POKEMON_Sprites/Front/Stalobor.png")
stalobor_x3g = 76
stalobor_y3g= 0

stalobor21g = pygame.image.load("POKEMON_Sprites/Front/Stalobor2.png")
stalobor2_x1g = 77
stalobor2_y1g = 0


makabaja1g = pygame.image.load("POKEMON_Sprites/Front/Makabaja.png")
makabaja_x1g = 78
makabaja_y1g = 0

makabaja2g = pygame.image.load("POKEMON_Sprites/Front/Makabaja.png")
makabaja_x2g = 79
makabaja_y2g = 0

makabaja3g = pygame.image.load("POKEMON_Sprites/Front/Makabaja.png")
makabaja_x3g = 80
makabaja_y3g = 0

echnatoll1g = pygame.image.load("POKEMON_Sprites/Front/Echnatoll.png")
echnatoll_x1g = 81
echnatoll_y1g = 0

echnatoll2g = pygame.image.load("POKEMON_Sprites/Front/Echnatoll.png")
echnatoll_x2g = 82
echnatoll_y2g= 0

echnatoll3g = pygame.image.load("POKEMON_Sprites/Front/Echnatoll.png")
echnatoll_x3g = 83
echnatoll_y3g= 0

echnatoll21g = pygame.image.load("POKEMON_Sprites/Front/Echnatoll2.png")
echnatoll2_x1g = 84
echnatoll2_y1g = 0



'#Einfügen von Shop-Pokemon'

'Shop-Slot 1'
serpifeu_shop1g = pygame.image.load("POKEMON-SHOP_Sprites/serpifeu_shop.png")
serpifeu_shop_x1g = 1350
serpifeu_shop_y1g = 600

floink_shop1g = pygame.image.load("POKEMON-SHOP_Sprites/floink_shop.png")
floink_shop_x1g = 1350
floink_shop_y1g = 600

ottaro_shop1g = pygame.image.load("POKEMON-SHOP_Sprites/ottaro_shop.png")
ottaro_shop_x1g = 1350
ottaro_shop_y1g = 600

strawickl_shop1g = pygame.image.load("POKEMON-SHOP_Sprites/strawickl_shop.png")
strawickl_shop_x1g = 1350
strawickl_shop_y1g = 600

toxiped_shop1g = pygame.image.load("POKEMON-SHOP_Sprites/toxiped_shop.png")
toxiped_shop_x1g = 1350
toxiped_shop_y1g = 600

praktibalk_shop1g = pygame.image.load("POKEMON-SHOP_Sprites/praktibalk_shop.png")
praktibalk_shop_x1g = 1350
praktibalk_shop_y1g = 600

klikk_shop1g = pygame.image.load("POKEMON-SHOP_Sprites/klikk_shop.png")
klikk_shop_x1g = 1350
klikk_shop_y1g = 600

kiesling_shop1g = pygame.image.load("POKEMON-SHOP_Sprites/kiesling_shop.png")
kiesling_shop_x1g = 1350
kiesling_shop_y1g = 600

milza_shop1g = pygame.image.load("POKEMON-SHOP_Sprites/milza_shop.png")
milza_shop_x1g = 1350
milza_shop_y1g = 600

ganovil_shop1g = pygame.image.load("POKEMON-SHOP_Sprites/ganovil_shop.png")
ganovil_shop_x1g = 1350
ganovil_shop_y1g = 600

rotomurf_shop1g = pygame.image.load("POKEMON-SHOP_Sprites/rotomurf_shop.png")
rotomurf_shop_x1g = 1350
rotomurf_shop_y1g = 600

makabaja_shop1g = pygame.image.load("POKEMON-SHOP_Sprites/makabaja_shop.png")
makabaja_shop_x1g = 1350
makabaja_shop_y1g = 600

'Shop-Slot 2'

serpifeu_shop2g = pygame.image.load("POKEMON-SHOP_Sprites/serpifeu_shop.png")
serpifeu_shop_x2g = 1350
serpifeu_shop_y2g = 500

floink_shop2g = pygame.image.load("POKEMON-SHOP_Sprites/floink_shop.png")
floink_shop_x2g = 1350
floink_shop_y2g = 500

ottaro_shop2g = pygame.image.load("POKEMON-SHOP_Sprites/ottaro_shop.png")
ottaro_shop_x2g = 1350
ottaro_shop_y2g = 500

strawickl_shop2g = pygame.image.load("POKEMON-SHOP_Sprites/strawickl_shop.png")
strawickl_shop_x2g = 1350
strawickl_shop_y2g = 500

toxiped_shop2g = pygame.image.load("POKEMON-SHOP_Sprites/toxiped_shop.png")
toxiped_shop_x2g = 1350
toxiped_shop_y2g = 500

praktibalk_shop2g = pygame.image.load("POKEMON-SHOP_Sprites/praktibalk_shop.png")
praktibalk_shop_x2g = 1350
praktibalk_shop_y2g = 500

klikk_shop2g = pygame.image.load("POKEMON-SHOP_Sprites/klikk_shop.png")
klikk_shop_x2g = 1350
klikk_shop_y2g = 500

kiesling_shop2g = pygame.image.load("POKEMON-SHOP_Sprites/kiesling_shop.png")
kiesling_shop_x2g = 1350
kiesling_shop_y2g = 500

milza_shop2g = pygame.image.load("POKEMON-SHOP_Sprites/milza_shop.png")
milza_shop_x2g = 1350
milza_shop_y2g = 500

ganovil_shop2g = pygame.image.load("POKEMON-SHOP_Sprites/ganovil_shop.png")
ganovil_shop_x2g = 1350
ganovil_shop_y2g = 600

rotomurf_shop2g = pygame.image.load("POKEMON-SHOP_Sprites/rotomurf_shop.png")
rotomurf_shop_x2g = 1350
rotomurf_shop_y2g = 500

makabaja_shop2g = pygame.image.load("POKEMON-SHOP_Sprites/makabaja_shop.png")
makabaja_shop_x2g = 1350
makabaja_shop_y2g = 500

'Shop-Slot 3'

serpifeu_shop3g = pygame.image.load("POKEMON-SHOP_Sprites/serpifeu_shop.png")
serpifeu_shop_x3g = 1350
serpifeu_shop_y3g = 400

floink_shop3g = pygame.image.load("POKEMON-SHOP_Sprites/floink_shop.png")
floink_shop_x3g = 1350
floink_shop_y3g = 400

ottaro_shop3g = pygame.image.load("POKEMON-SHOP_Sprites/ottaro_shop.png")
ottaro_shop_x3g = 1350
ottaro_shop_y3g = 400

strawickl_shop3g = pygame.image.load("POKEMON-SHOP_Sprites/strawickl_shop.png")
strawickl_shop_x3g = 1350
strawickl_shop_y3g = 400

toxiped_shop3g = pygame.image.load("POKEMON-SHOP_Sprites/toxiped_shop.png")
toxiped_shop_x3g = 1350
toxiped_shop_y3g = 400

praktibalk_shop3g = pygame.image.load("POKEMON-SHOP_Sprites/praktibalk_shop.png")
praktibalk_shop_x3g = 1350
praktibalk_shop_y3g = 400

klikk_shop3g = pygame.image.load("POKEMON-SHOP_Sprites/klikk_shop.png")
klikk_shop_x3g = 1350
klikk_shop_y3g = 400

kiesling_shop3g = pygame.image.load("POKEMON-SHOP_Sprites/kiesling_shop.png")
kiesling_shop_x3g = 1350
kiesling_shop_y3g = 400

milza_shop3g = pygame.image.load("POKEMON-SHOP_Sprites/milza_shop.png")
milza_shop_x3g = 1350
milza_shop_y3g = 400

ganovil_shop3g = pygame.image.load("POKEMON-SHOP_Sprites/ganovil_shop.png")
ganovil_shop_x3g = 1350
ganovil_shop_y3g = 400

rotomurf_shop3g = pygame.image.load("POKEMON-SHOP_Sprites/rotomurf_shop.png")
rotomurf_shop_x3g = 1350
rotomurf_shop_y3g = 400

makabaja_shop3g = pygame.image.load("POKEMON-SHOP_Sprites/makabaja_shop.png")
makabaja_shop_x3g = 1350
makabaja_shop_y3g = 400

'Shop-Slot 4'

serpifeu_shop4g = pygame.image.load("POKEMON-SHOP_Sprites/serpifeu_shop.png")
serpifeu_shop_x4g = 1350
serpifeu_shop_y4g = 300

floink_shop4g = pygame.image.load("POKEMON-SHOP_Sprites/floink_shop.png")
floink_shop_x4g = 1350
floink_shop_y4g = 300

ottaro_shop4g = pygame.image.load("POKEMON-SHOP_Sprites/ottaro_shop.png")
ottaro_shop_x4g = 1350
ottaro_shop_y4g = 300

strawickl_shop4g = pygame.image.load("POKEMON-SHOP_Sprites/strawickl_shop.png")
strawickl_shop_x4g = 1350
strawickl_shop_y4g = 300

toxiped_shop4g = pygame.image.load("POKEMON-SHOP_Sprites/toxiped_shop.png")
toxiped_shop_x4g = 1350
toxiped_shop_y4g = 300

praktibalk_shop4g = pygame.image.load("POKEMON-SHOP_Sprites/praktibalk_shop.png")
praktibalk_shop_x4g = 1350
praktibalk_shop_y4g = 300

klikk_shop4g = pygame.image.load("POKEMON-SHOP_Sprites/klikk_shop.png")
klikk_shop_x4g = 1350
klikk_shop_y4g = 300

kiesling_shop4g = pygame.image.load("POKEMON-SHOP_Sprites/kiesling_shop.png")
kiesling_shop_x4g = 1350
kiesling_shop_y4g = 300

milza_shop4g = pygame.image.load("POKEMON-SHOP_Sprites/milza_shop.png")
milza_shop_x4g = 1350
milza_shop_y4g = 300

ganovil_shop4g = pygame.image.load("POKEMON-SHOP_Sprites/ganovil_shop.png")
ganovil_shop_x4g = 1350
ganovil_shop_y4g = 300

rotomurf_shop4g = pygame.image.load("POKEMON-SHOP_Sprites/rotomurf_shop.png")
rotomurf_shop_x4g = 1350
rotomurf_shop_y4g = 300

makabaja_shop4g = pygame.image.load("POKEMON-SHOP_Sprites/makabaja_shop.png")
makabaja_shop_x4g = 1350
makabaja_shop_y4g = 300

'Shop-Slot 5'

serpifeu_shop5g = pygame.image.load("POKEMON-SHOP_Sprites/serpifeu_shop.png")
serpifeu_shop_x5g = 1350
serpifeu_shop_y5g = 200

floink_shop5g = pygame.image.load("POKEMON-SHOP_Sprites/floink_shop.png")
floink_shop_x5g = 1350
floink_shop_y5g = 200

ottaro_shop5g = pygame.image.load("POKEMON-SHOP_Sprites/ottaro_shop.png")
ottaro_shop_x5g = 1350
ottaro_shop_y5g = 200

strawickl_shop5g = pygame.image.load("POKEMON-SHOP_Sprites/strawickl_shop.png")
strawickl_shop_x5g = 1350
strawickl_shop_y5g = 200

toxiped_shop5g = pygame.image.load("POKEMON-SHOP_Sprites/toxiped_shop.png")
toxiped_shop_x5g = 1350
toxiped_shop_y5g = 200

praktibalk_shop5g = pygame.image.load("POKEMON-SHOP_Sprites/praktibalk_shop.png")
praktibalk_shop_x5g = 1350
praktibalk_shop_y5g = 200

klikk_shop5g = pygame.image.load("POKEMON-SHOP_Sprites/klikk_shop.png")
klikk_shop_x5g = 1350
klikk_shop_y5g = 200

kiesling_shop5g = pygame.image.load("POKEMON-SHOP_Sprites/kiesling_shop.png")
kiesling_shop_x5g = 1350
kiesling_shop_y5g = 200

milza_shop5g = pygame.image.load("POKEMON-SHOP_Sprites/milza_shop.png")
milza_shop_x5g = 1350
milza_shop_y5g = 200

ganovil_shop5g = pygame.image.load("POKEMON-SHOP_Sprites/ganovil_shop.png")
ganovil_shop_x5g = 1350
ganovil_shop_y5g = 200

rotomurf_shop5g = pygame.image.load("POKEMON-SHOP_Sprites/rotomurf_shop.png")
rotomurf_shop_x5g = 1350
rotomurf_shop_y5g = 200

makabaja_shop5g = pygame.image.load("POKEMON-SHOP_Sprites/makabaja_shop.png")
makabaja_shop_x5g = 1350
makabaja_shop_y5g = 200















arena = pygame.image.load("Layout_assets/arenawild.png")
arena_x = 0
arena_y = 0

reroll = pygame.image.load("Layout_assets/Reroll_button.png")
reroll_x = 0
reroll_y = 0

rerollg = pygame.image.load("Layout_assets/Reroll_button.png")
reroll_xg = 1350
reroll_yg = 0