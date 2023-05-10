namespace SpriteKind {
    export const Background = SpriteKind.create()
    export const Brush = SpriteKind.create()
    export const Canvas = SpriteKind.create()
}

controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    if (current_scene == "menu") {
        if (currently_selecte_option_index == 0) {
            current_scene = "singleplayer"
            clear_menu()
            generate_string()
        } else if (currently_selecte_option_index == 1) {
            clear_menu()
            add_menu_options("In development...", "-", "-", false, false)
        } else if (currently_selecte_option_index == 2) {
            current_scene = "credit"
            clear_menu()
            add_menu_options("Inspired by MonkeyType", "Thanks for Justin's guide", "", false, false)
            show_menu()
        }
        
    } else if (current_scene == "singleplayer") {
        types += 1
        if (test_string[0] == "A") {
            correct_types += 1
            sprites.destroy(show_string[0], effects.spray, 50)
            test_string.removeAt(0)
            show_string.removeAt(0)
            music.play(music.melodyPlayable(music.zapped), music.PlaybackMode.InBackground)
        } else if (test_string[0] == "B") {
            scene.cameraShake(8, 100)
            music.play(music.melodyPlayable(music.smallCrash), music.PlaybackMode.InBackground)
        }
        
    }
    
})
info.onCountdownEnd(function on_countdown_end() {
    
    clear_menu()
    music.play(music.createSong(hex`
            0078000408020100001c00010a006400f401640000040000000000000000000000000005000004240000000400012c08000c0001291000140001271c002000012420002400012028002c000125
        `), music.PlaybackMode.InBackground)
    textSprite4 = textsprite.create("Accuracy: " + convertToText(Math.floor(correct_types / types * 100)) + "%", 0, 5)
    textSprite4.setMaxFontHeight(9)
    textSprite4.setPosition(55, 25)
    textSprite5 = textsprite.create("WPM: " + convertToText(correct_types / 10 * 60), 0, 5)
    textSprite5.setMaxFontHeight(9)
    textSprite5.setPosition(40, 45)
    textSprite3 = textsprite.create("Raw: " + convertToText(types / 10 * 60), 0, 5)
    textSprite3.setMaxFontHeight(9)
    textSprite3.setPosition(40, 65)
    textSprite = textsprite.create("Press Refresh to restart", 0, 1)
    textSprite.setMaxFontHeight(9)
    textSprite.setPosition(75, 85)
})
function clear_menu() {
    sprites.destroy(textSprite)
    sprites.destroy(textSprite2)
    sprites.destroy(textSprite3)
    sprites.destroy(textSprite4)
    sprites.destroy(textSprite5)
}

controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    
    if (show_drawing_menu) {
        currently_selecte_option_index = (currently_selecte_option_index + (all_options_in_menu.length - 1)) % all_options_in_menu.length
    }
    
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    
    if (current_scene == "credit") {
        clear_menu()
        current_scene = "menu"
        add_menu_options("Singleplayer", "Multiplayer", "Credit", true, true)
        show_menu()
    } else if (current_scene == "singleplayer") {
        types += 1
        if (test_string[0] == "B") {
            correct_types += 1
            sprites.destroy(show_string[0], effects.spray, 50)
            test_string.removeAt(0)
            show_string.removeAt(0)
            music.play(music.melodyPlayable(music.zapped), music.PlaybackMode.InBackground)
        } else if (test_string[0] == "A") {
            scene.cameraShake(8, 100)
            music.play(music.melodyPlayable(music.smallCrash), music.PlaybackMode.InBackground)
        }
        
    }
    
})
spriteutils.createRenderable(100, function on_create_renderable(screen2: Image) {
    
    if (show_drawing_menu) {
        index = 0
        while (index <= all_options_in_menu.length - 1) {
            if (index == currently_selecte_option_index) {
                all_options_in_menu[index].setBorder(1, 5)
            } else {
                all_options_in_menu[index].setBorder(0, 5)
            }
            
            index += 1
        }
    }
    
})
function add_menu_options(option1: string, option2: string, option3: string, Selectable: boolean, Title: boolean) {
    
    all_options_in_menu = []
    textSprite = textsprite.create(option1, 0, 1)
    textSprite.setPosition(80, 65)
    if (Selectable) {
        all_options_in_menu.push(textSprite)
    }
    
    textSprite2 = textsprite.create(option2, 0, 1)
    textSprite2.setPosition(80, 80)
    if (Selectable) {
        all_options_in_menu.push(textSprite2)
    }
    
    textSprite3 = textsprite.create(option3, 0, 1)
    textSprite3.setPosition(80, 95)
    if (Selectable) {
        all_options_in_menu.push(textSprite3)
    }
    
    if (Title) {
        textSprite4 = textsprite.create("ArcadeType", 0, 5)
    }
    
    textSprite4.setPosition(55, 30)
    textSprite4.setMaxFontHeight(10)
    textSprite5 = textsprite.create("Ver1.0", 0, 5)
    textSprite5.setPosition(139, 110)
}

function show_menu() {
    for (let value of sprites.allOfKind(SpriteKind.Text)) {
        value.setFlag(SpriteFlag.Invisible, !show_drawing_menu)
    }
}

controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    
    if (show_drawing_menu) {
        currently_selecte_option_index = (currently_selecte_option_index + 1) % all_options_in_menu.length
    }
    
})
function generate_string() {
    
    test_string = []
    show_string = []
    for (let index2 = 0; index2 < 21; index2++) {
        string_generator = randint(0, 1)
        if (string_generator == 0) {
            test_string.push("A")
            show_string.push(textsprite.create(test_string[index2], 0, 1))
        } else {
            test_string.push("B")
            show_string.push(textsprite.create(test_string[index2], 0, 1))
        }
        
        show_string[index2].setPosition(20 + index2 * 5, 65)
    }
    info.startCountdown(5)
}

let string_generator = 0
let index = 0
let all_options_in_menu : TextSprite[] = []
let textSprite2 : TextSprite = null
let textSprite : TextSprite = null
let textSprite3 : TextSprite = null
let textSprite5 : TextSprite = null
let textSprite4 : TextSprite = null
let show_string : TextSprite[] = []
let correct_types = 0
let test_string : string[] = []
let types = 0
let current_scene = ""
let currently_selecte_option_index = 0
let show_drawing_menu = false
scene.setBackgroundColor(13)
show_drawing_menu = !show_drawing_menu
currently_selecte_option_index = 0
add_menu_options("Singleplayer", "Multiplayer", "Credit", true, true)
current_scene = "menu"
show_menu()
MakeyMakey.setSimulatorKeymap(MakeyMakey.PlayerNumber.ONE, MakeyMakey.MakeyMakeyKey.UP, MakeyMakey.MakeyMakeyKey.DOWN, MakeyMakey.MakeyMakeyKey.LEFT, MakeyMakey.MakeyMakeyKey.RIGHT, MakeyMakey.MakeyMakeyKey.F, MakeyMakey.MakeyMakeyKey.G)
