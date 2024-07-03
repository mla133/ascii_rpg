max_health = 100
current_health = 100

bars = 20
symbol = "█"
remaining_health_symbol = "█"
lost_health_symbol = "░"


color_red =     "\033[91m"
color_purple =  "\033[95m"
color_blue1 =  "\033[34m"
color_blue2 =  "\033[36m"
color_blue3 =  "\033[96m"
color_green1 =  "\033[92m"
color_green2 =  "\033[32m"
color_brown =  "\033[33m"
color_yellow =  "\033[93m"
color_grey =  "\033[37m"
color_default =  "\033[0m"

color_list = (color_red, color_purple, color_blue1, color_blue2, color_blue3, color_green1, color_green2,
            color_brown, color_yellow, color_grey, color_default)

def print_variable_name(variable: object) -> None:
    for name, value in globals().items():
        if id(value) == id(variable):
            return name

def show_colors() -> None:
    for color in color_list:
        print(f"{color}{3 * symbol}", end="")

    print(color_default)

    for color in color_list:
        print(f"{color}{3 * symbol} {print_variable_name(color)}")

show_colors()

while True:
    remaining_health_bars = round(current_health/max_health * bars)
    lost_health_bars = bars - remaining_health_bars

    print(f"HEALTH: {current_health}/{max_health}")
#    print(f"{current_health*'X'}|{(max_health-current_health)*'_'}")
    print(f"|{color_red}{remaining_health_bars*remaining_health_symbol}{lost_health_bars*lost_health_symbol}{color_default}|")
    current_health -= 10
    if current_health < 0:
        quit()
