from map import Map



def run() -> None:
    while True:
        game_map.display_map()
        input("> ")

if __name__ == "__main__":
    map_w, map_h = 30, 15
    game_map = Map(map_w, map_h)
    # If you have a complete map you created manually...
    #custom_map = Map(5,5)
    #cusotm_map.map_data = [
    #    [forest, forest, forest, mountain, mountain],
    #    [plains, forest, forest, pines, mountain],
    #    [plains, forest, forest, pines, pines],
    #    [plains, plains, forest, forest, forest],
    #    [plains, plains, plains, plains, plains]
    #    ]
    run()
