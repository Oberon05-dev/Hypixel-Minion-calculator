minions_list = [
    "----Choose_Minion----",
    "----Farming----",
    "Cactus",
    "Carrot",
    "Cocoa_beans",
    "Melon",
    "Mushroom",
    "Potato",
    "Pumpkin",
    "Sugar_cane",
    "Wheat",

    "----Mining----",
    "Cobelstone",
    "Coal",
    "Lapis",
    "Iron",
    
    "----Combat----",
    "Blaze",
    "Cave_spider",
    "Creeper",
    "Enderman",
    "Ghast",
    "Magma_cube",
    "Skeleton",
    "Slime",
    "Spider",
    "Zombie",
]

minions = {
    "----Choose_Minion----":  [1,1,1,1,1,1,1,1,1],
    "----Farming----":  [1,1,1,1,1,1,1,1,1],
    "Cactus":       [27, 25, 23, 21, 18, 15, 1, 3, 1],
    "Carrot":       [20, 18, 16, 14, 12, 10, 1, 4, 1],
    "Cocoa_beans":  [27, 25, 23, 21, 18, 15, 3, 3, 1],
    "Melon":        [24, 22.5, 21, 18.5, 16, 13, 0.5, 3, 1],
    "Mushroom":     [30, 28, 26, 23, 20, 16, 3, 3, 1],
    "Potato":       [20, 18, 16, 14, 12, 10, 1, 4, 1],
    "Pumpkin":      [32, 30, 27, 24, 20, 16, 4, 1, 1],
    "Sugar_cane":   [22, 20, 18, 16, 14.5, 12, 2, 3, 1],
    "Wheat":        [15, 13, 11, 10, 9, 8, 1, 1, 1],

    "----Mining----":  [1,1,1,1,1,1,1,1,1],
    "Coal":         [15, 13, 12, 10, 9, 7, 2, 1, 2],
    "Cobelstone":   [14, 13, 12, 10, 9, 7, 1, 1, 2],
    "Lapis":        [29, 27, 25, 23, 21, 18, 1, 6, 2],
    "Iron":         [17, 15, 14, 12, 10, 8, 3, 1, 2],

    "----Combat----":   [1,1,1,1,1,1,1,1,1],
    "Blaze":        [33, 31, 28.5, 25, 21, 16.5, 9, 1, 3],
    "Cave_spider":  [26, 24, 22, 20, 17, 13, 3, 1, 3],
    "Creeper":      [27, 25, 23, 21, 18, 14, 4, 1, 3],
    "Enderman":     [32, 30, 28, 25, 22, 18, 10, 1, 3],
    "Ghast":        [50, 47, 44, 41, 38, 32, 16, 1, 3],
    "Magma_cube":   [32, 30, 28, 25, 22, 18, 8, 2, 3],
    "Skeleton":     [26, 24, 22, 20, 17, 13, 2, 1, 3],
    "Slime":        [26, 24, 22, 19, 16, 12, 5, 2, 3],
    "Spider":       [26, 24, 22, 20, 17, 13, 3, 1, 3],
    "Zombie":       [26, 24, 22, 20, 17, 13, 2, 1, 3],
}

# "name": [T1, T3, T5, T7, T9, T11, item_sell, items_per_action, class]
# 1 - Farming
# 2 - Mining
# 3 - Combat
# 4 - Foraging
# 5 - Fishing
# 6 - Special