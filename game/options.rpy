## HOME BREW STUFF HERE #################################################

## images #####

image nvl = "gui/nvl.png" ## code red this is purely for that one ambien instruction for players you can make that less ugly and remove this

image credits:
    "credits2.png" with Dissolve(0.5)
    pause 1.0
    "credits1.png" with Dissolve(0.5)
    pause 0.3
    repeat

image credits3:
    "credits3a.png" with Dissolve(0.5)
    pause 1.0
    "credits3b.png" with Dissolve(0.5)
    pause 0.3
    repeat

image credits4:
    "credits4a.png" with Dissolve(0.5)
    pause 1.0
    "credits4b.png" with Dissolve(0.5)
    pause 0.3
    repeat

image credits5:
    "credits5a.png" with Dissolve(0.5)
    pause 1.0
    "credits5b.png" with Dissolve(0.5)
    pause 0.3
    repeat

## characters #####

define RL = Character("Rose", color="#f54dac")
define SV = Character("Svetlana", color="#8c03cb")
define SH = Character("Shane", color="#4d9bf5")
define IR = Character("Ilya", color="#fa9a34")

define Pilot = Character("Pilot", color="#ee1b1b")
define Girl = Character("Random Girl", color="#ee1b1b")
define Cashier = Character("Bored Cashier", color="#ee1b1b")
define Meg = Character("Rose's Agent Megan", color="#ee1b1b")

## flags persistent #####

default loop = 0

default giftshopvisit = 0
default leaveairport = False
default papcount = 0

default doorbell = 0
default knock = 0
default bargecount = 0
default knockpass = False

default tourloop = 0
default notourloop = 0
default shane_room1 = False
default shane_room2 = False
default shane_room3 = False

default tealoop = 0
default svetatea = False ## if you played teatime.sveta and learned she maybe likes wind up animal toys

default svet_tour = 0
default svet_room1 = False ## the rose noticing sveta's style but also because she was concerned-friend about shane dating ilya, and sveta saying 'me too'
default svet_room3 = False ## sveta feeling Some Kind Of Way about ilya stashing all his trophies away in shane's cottage's guest room
default sv_room1loop = 0
default sv_room2loop = 0
default sv_room3loop = 0

default russian = 0
default aloneloop = 0
default clearemail = 0
default clearemail2 = 0
default clearemail3 = 0 # this is for negative numbers
default foodtruckkitty = 0
default foodtruckkitty2 = 0
default foodtruckkitty3 = 0 # this is for negative numbers

default room1blind = False
default room2blind = False
default room3blind = False
default blindspass = 0

default outside = 0
default inside = 0
default svetpass = 0
default kisscount = 0

default yayrussian = False

# flags temp #####

default freedom = 0
default svetheart = 0
default ilyaheart = 0

default giftbought = ""
default papped = False
default russianpass = False
default convincesvet = 0
default blindsnow = False
default kissnow = False
default testpassnow = False
default svet_room2 = False # reference to rabbit in her luggage lol

default shanemove = False # if you stopped housetour and talked about shane moving to the Cens as a free agent
default shanetea = False # if you played teatime.shane and learned he came out to his team
default shanesveta = False # if you stopped housetour and talked about shane asking sveta if ilya is happy

default random = 0
default pt = "" # playtest tracker


## positions and transforms ######

transform midleft:
    yalign 1.0
    xcenter 0.25

transform midright:
    yalign 1.0
    xcenter 0.72

transform blip():
    alpha 0.0
    linear 0.4 alpha 0.7
    pause 0.7
    linear 0.4 alpha 0.0


###############################################################################33
#### THIS IS WHERE THE RENPY DEFAULT STUFF LIVES##############################
## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Roselana time loop")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "1.4"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "Roselanatimeloop"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any
## other number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "Roselanatimeloop-1781408156"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory,
    ## "game/**.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
