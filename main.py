@namespace
class SpriteKind:
    Background = SpriteKind.create()
    Brush = SpriteKind.create()
    Canvas = SpriteKind.create()

def on_a_pressed():
    global current_scene, types, correct_types
    if current_scene == "menu":
        if currently_selecte_option_index == 0:
            current_scene = "singleplayer"
            clear_menu()
            generate_string()
        elif currently_selecte_option_index == 1:
            clear_menu()
            add_menu_options("In development...", "-", "-", False, False)
        elif currently_selecte_option_index == 2:
            current_scene = "credit"
            clear_menu()
            add_menu_options("Inspired by MonkeyType",
                "Thanks for Justin's guide",
                "",
                False,
                False)
            show_menu()
    elif current_scene == "singleplayer":
        types += 1
        if test_string[0] == "A":
            correct_types += 1
            sprites.destroy(show_string[0], effects.spray, 50)
            test_string.remove_at(0)
            show_string.remove_at(0)
            music.play(music.melody_playable(music.zapped),
                music.PlaybackMode.IN_BACKGROUND)
        elif test_string[0] == "B":
            scene.camera_shake(8, 100)
            music.play(music.melody_playable(music.small_crash),
                music.PlaybackMode.IN_BACKGROUND)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_countdown_end():
    global textSprite4, textSprite5, textSprite3, textSprite
    clear_menu()
    music.play(music.create_song(hex("""
            0078000408020100001c00010a006400f401640000040000000000000000000000000005000004240000000400012c08000c0001291000140001271c002000012420002400012028002c000125
        """)),
        music.PlaybackMode.IN_BACKGROUND)
    textSprite4 = textsprite.create("Accuracy: " + convert_to_text(Math.floor(correct_types / types * 100)) + "%",
        0,
        5)
    textSprite4.set_max_font_height(9)
    textSprite4.set_position(55, 25)
    textSprite5 = textsprite.create("WPM: " + convert_to_text(correct_types / 10 * 60), 0, 5)
    textSprite5.set_max_font_height(9)
    textSprite5.set_position(40, 45)
    textSprite3 = textsprite.create("Raw: " + convert_to_text(types / 10 * 60), 0, 5)
    textSprite3.set_max_font_height(9)
    textSprite3.set_position(40, 65)
    textSprite = textsprite.create("Press Refresh to restart", 0, 1)
    textSprite.set_max_font_height(9)
    textSprite.set_position(75, 85)
info.on_countdown_end(on_countdown_end)

def clear_menu():
    sprites.destroy(textSprite)
    sprites.destroy(textSprite2)
    sprites.destroy(textSprite3)
    sprites.destroy(textSprite4)
    sprites.destroy(textSprite5)

def on_up_pressed():
    global currently_selecte_option_index
    if show_drawing_menu:
        currently_selecte_option_index = (currently_selecte_option_index + (len(all_options_in_menu) - 1)) % len(all_options_in_menu)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    global current_scene, types, correct_types
    if current_scene == "credit":
        clear_menu()
        current_scene = "menu"
        add_menu_options("Singleplayer", "Multiplayer", "Credit", True, True)
        show_menu()
    elif current_scene == "singleplayer":
        types += 1
        if test_string[0] == "B":
            correct_types += 1
            sprites.destroy(show_string[0], effects.spray, 50)
            test_string.remove_at(0)
            show_string.remove_at(0)
            music.play(music.melody_playable(music.zapped),
                music.PlaybackMode.IN_BACKGROUND)
        elif test_string[0] == "A":
            scene.camera_shake(8, 100)
            music.play(music.melody_playable(music.small_crash),
                music.PlaybackMode.IN_BACKGROUND)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_create_renderable(screen2):
    global index
    if show_drawing_menu:
        index = 0
        while index <= len(all_options_in_menu) - 1:
            if index == currently_selecte_option_index:
                all_options_in_menu[index].set_border(1, 5)
            else:
                all_options_in_menu[index].set_border(0, 5)
            index += 1
spriteutils.create_renderable(100, on_create_renderable)

def add_menu_options(option1: str, option2: str, option3: str, Selectable: bool, Title: bool):
    global all_options_in_menu, textSprite, textSprite2, textSprite3, textSprite4, textSprite5
    all_options_in_menu = []
    textSprite = textsprite.create(option1, 0, 1)
    textSprite.set_position(80, 65)
    if Selectable:
        all_options_in_menu.append(textSprite)
    textSprite2 = textsprite.create(option2, 0, 1)
    textSprite2.set_position(80, 80)
    if Selectable:
        all_options_in_menu.append(textSprite2)
    textSprite3 = textsprite.create(option3, 0, 1)
    textSprite3.set_position(80, 95)
    if Selectable:
        all_options_in_menu.append(textSprite3)
    if Title:
        textSprite4 = textsprite.create("ArcadeType", 0, 5)
    textSprite4.set_position(55, 30)
    textSprite4.set_max_font_height(10)
    textSprite5 = textsprite.create("Ver1.0", 0, 5)
    textSprite5.set_position(139, 110)
def show_menu():
    for value in sprites.all_of_kind(SpriteKind.text):
        value.set_flag(SpriteFlag.INVISIBLE, not (show_drawing_menu))

def on_down_pressed():
    global currently_selecte_option_index
    if show_drawing_menu:
        currently_selecte_option_index = (currently_selecte_option_index + 1) % len(all_options_in_menu)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def generate_string():
    global test_string, show_string, string_generator
    test_string = []
    show_string = []
    for index2 in range(21):
        string_generator = randint(0, 1)
        if string_generator == 0:
            test_string.append("A")
            show_string.append(textsprite.create(test_string[index2], 0, 1))
        else:
            test_string.append("B")
            show_string.append(textsprite.create(test_string[index2], 0, 1))
        show_string[index2].set_position(20 + index2 * 5, 65)
    info.start_countdown(5)
string_generator = 0
index = 0
all_options_in_menu: List[TextSprite] = []
textSprite2: TextSprite = None
textSprite: TextSprite = None
textSprite3: TextSprite = None
textSprite5: TextSprite = None
textSprite4: TextSprite = None
show_string: List[TextSprite] = []
correct_types = 0
test_string: List[str] = []
types = 0
current_scene = ""
currently_selecte_option_index = 0
show_drawing_menu = False
scene.set_background_color(13)
show_drawing_menu = not (show_drawing_menu)
currently_selecte_option_index = 0
add_menu_options("Singleplayer", "Multiplayer", "Credit", True, True)
current_scene = "menu"
show_menu()
MakeyMakey.set_simulator_keymap(MakeyMakey.PlayerNumber.ONE,
    MakeyMakey.MakeyMakeyKey.UP,
    MakeyMakey.MakeyMakeyKey.DOWN,
    MakeyMakey.MakeyMakeyKey.LEFT,
    MakeyMakey.MakeyMakeyKey.RIGHT,
    MakeyMakey.MakeyMakeyKey.F,
    MakeyMakey.MakeyMakeyKey.G)