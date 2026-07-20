# The game starts here.
# code red! comment out all code red things on launch
# TBD needs editing out or writing in

label start:

    jump start_real 
    # code red uncomment the above for launch!

    menu:
        "For playtesting (if you're not playtesting, hit start)"

        "start the game":
            jump start_actual

        "set variables":
            menu:
                "set number of loops":
                    $ loop = int(renpy.input("Which loop are you in", allow="0123456789", length=2))

                    "Number of loops: [loop]"

                    jump start
                
                "number of teatimes had with Shane and Ilya":
                    $ tealoop = int(renpy.input("How many teatimes before Sveta arrives", allow="0123456789", length=2))

                    "Number of teatimes: [tealoop]"

                    jump start
                
                "set various house tour variables":
                    menu:
                        "shane tells you about room 1":
                            if shane_room1 == False:
                                $ shane_room1 = True
                            else:
                                $ shane_room1 = False

                            "shane_room1 is [shane_room1]"
                        
                        "shane tells you about room 2":
                            if shane_room2 == False:
                                $ shane_room2 = True
                            else:
                                $ shane_room2 = False
                            "shane_room2 is [shane_room2]"
                        
                        "shane tells you about room 3":
                            if shane_room3 == False:
                                $ shane_room3 = True
                            else:
                                $ shane_room3 = False
                            "shane_room3 is [shane_room3]"
                        
                        "you tell svetlana about room 1":
                            if svet_room1 == False:
                                $ svet_room1 = True
                            else:
                                $ svet_room1 = False
                            "svet_room1 is [svet_room1]"
                        
                        "you tell svetlana about room 2":
                            if svet_room2 == False:
                                $ svet_room2 = True
                            else:
                                $ svet_room2 = False
                            "svet_room2 is [svet_room2]"
                        
                        "you tell svetlana about room 3":
                            if svet_room3 == False:
                                $ svet_room3 = True
                            else:
                                $ svet_room3 = False
                            "svet_room3 is [svet_room3]"

                        "shane tells you about room 1's blinds":
                            if room1blind == False:
                                $ room1blind = True
                            else:
                                $ room1blind = False

                            "room1blind is [room1blind]"
                        
                        "shane tells you about room 2's blinds":
                            if room2blind == False:
                                $ room2blind = True
                            else:
                                $ room2blind = False

                            "room2blind is [room2blind]"
                        
                        "shane tells you about room 3's blinds":
                            if room3blind == False:
                                $ room3blind = True
                            else:
                                $ room3blind = False

                            "room3blind is [room3blind]"
                    
                    jump start

                "set number of times been outside with Svetlana after dinner":
                    $ outside = int(renpy.input("No. times been outside", allow="0123456789", length=2))

                    "Number of post-dinner Sveta convos: [outside]"

                    jump start
                
                "set last scene variables (includes svetheart and kiss)":
                    menu:
                        "if you stopped housetour and talked about shane moving to the Cens as a free agent":
                            if shanemove == False:
                                $ shanemove = True
                            else:
                                $ shanemove = False

                            "shanemove is [shanemove]"
                        
                        "if you played teatime.shane and learned he came out to his team":
                            if shanetea == False:
                                $ shanetea = True
                            else:
                                $ shanetea = False
                            "shanetea is [shanetea]"
                        
                        "if you stopped housetour and talked about shane asking sveta if ilya is happy":
                            if shanesveta == False:
                                $ shanesveta = True
                            else:
                                $ shanesveta = False
                            "shanesveta is [shanesveta]"
                        
                        "did you kiss this loop?":
                            if kissnow == False:
                                $ kissnow = True
                            else:
                                $ kissnow = False
                            "kissnow is [kissnow]"
                        
                        "how many times have you kissed Sveta":
                            $ kisscount = int(renpy.input("Number of kisses across all loops", allow="0123456789", length=2))

                            "Number of kisses: [kisscount]"
                        
                        "how much svetlana likes you":
                            $ svetheart = int(renpy.input("how much svetlana likes you", allow="0123456789", length=2))

                            "Sveta likes you [svetheart] amount"

                    jump start

                "set freedom":
                    $ freedom = int(renpy.input("No. times avoided Hollanov", allow="0123456789", length=1))

                    "You've avoided Hollanov [freedom] times—3 is the magic number"

                    jump start

        "jump to a scene":
            menu:
                "arriving at cottage door":
                    jump ctdoor

                "teatime":
                    jump teatime

                "Shane's housetour":
                    jump housetour
                
                "Svetlana arrives":
                    jump svet_entrance
                
                "Svetlana's housetour":
                    jump housetour2
                
                "Dinner":
                    jump dinner
                
                "Outdoors with Svetlana":
                    jump outside

                "Leaving":
                    jump leaving

label start_real: # this needs pulling out because of playtesting reasons

    # these temp variables reset with every loop
    $ freedom = 0

    $ giftbought = ""
    $ papped = False
    $ russianpass = False
    $ svetheart = 0
    $ convincesvet = 0
    $ blindsnow = False
    $ kissnow = False
    $ svet_room2 = False

    $ shanemove = False
    $ shanetea = False
    $ shanesveta = False

    $ random = 0

    jump start_actual

label start_actual: 
    # jump here from playtesting

    scene black
    with fade

    Pilot "...we're making fantastic time, and will be arriving at Ottawa International Airport in approximately twenty minutes."

    scene bg plane
    with pixellate

    show zzrl flat

    RL "*Yawn*"
    
    Pilot "The local time is 3:15pm, which means we are nearly thirty minutes ahead of schedule. The weather in Ottawa right now is..."

    if loop == 0:
        RL "Ahead of schedule? I guess I should text Shane..."

        ##play audio 
        "texting.mp3"

        RL "'—and I'm going to be maybe thirty minutes early! So excited to meet Ilya for real!'"

        ##play audio 
        "textsent.mp3"

        show zzrl resigned

        RL "Though I'm not sure Ilya's particularly excited to meet me..."

    elif loop == 1:
        show zzrl surprised

        RL "Ottawa? Didn't I get on the flight back to LA?"

        Pilot "...and thank you for flying with Air Canada."

        show zzrl thoughtful

        RL "Was...all of that a dream...?"
    
    elif loop == 2:
        show zzrl surprised

        RL "Ottawa? Oh my god, did I actually dream of Shane's cottage again??"

        Pilot "...and thank you for flying with Air Canada."

        show zzrl wince

        RL "It feels too real to be just a dream...oh shit, is it the Ambien? Vivid dreaming is one of the side effects, right? But I've never had these side effects before..."

        show zzrl thoughtful

        RL "Or...maybe I'm getting mutant powers of precognition?? I guess seeing the future is better than turning blue...but why would I get someone else's power instead of my own...?"

        RL "No, wait, actually, it's more like Groundhog Day or something. Except if it's Groundhog Day, does that mean I'm a terrible person and I need to improve myself??"

        RL "Also, why would I be stuck in the day I'm going to Shane's cottage? What could I possibly be doing wrong in Shane's cottage?"

        show zzrl wince
        
        RL "...oh no, am I supposed to get Ilya to like me??"

        show zzrl resigned
        
        RL "Fuck, guess I'm stuck forever."
    
    elif loop == 3:
        show zzrl resigned

        RL "...okay. Guess we can rule out the Ambien being the problem then."

        RL "So what {i}is{/i} the problem...??"

        show zzrl thoughtful

        RL "...I wonder if this mean I'll end up back here any time I fall asleep today..." ## come back here to figure out how to better introduce the ambien thing
    
    else:

        ## is this just pointlessly asking Rose to record more lines...? is it better to be sequentially different and then exactly the same for players to safely ignore?

        $ random = renpy.random.randint(1, 4) 

        if random == 1:
            show zzrl resigned
            RL "Guess we're doing this again..."

        elif random == 2: ## check with rose re singing or swap to non-singing line
            RL "Let's start from the very beginnning~ A very good place to start~"

            RL "If you read you begin with A, B, C~ If you're stuck in a time loop, sing with me~"

        elif random == 3:
            show zzrl resigned
            RL "Alright, take...five? Take ten...? Wow, I've lost count."
        
        else:
            RL "Twenty minutes to download a new driving playlist, go go go!"

    jump airport

label airport:

    scene bg airport
    with fade

    if loop == 0:

        show zzrl flat

        RL "I suppose I have time to hang out here for a while..."
    
    elif loop == 1:

        show zzrl flat

        RL "I swear it feels like I was just here..."

        RL "...or maybe every airport starts to look the same after a while..."
    
    else:

        show zzrl flat

        RL "Right. Stay or go?"

    menu:
        "Check out the gift shop":

            if giftshopvisit == 0 and loop <= 1:

                $ giftshopvisit += 1
            
                show zzrl resigned

                RL "Hmm, nothing really exciting here. Guess that's Ottawa for you."

                RL "I should probably go before someone spots me."

            else:

                show zzrl resigned

                RL "Might as well pass the time doing something."

                jump giftshop

        "Leave for the cottage":

            if leaveairport == False:

                show zzrl resigned

                RL "Better go before anyone spots me. Last thing we need is for the paps to go crazy about how I'm meeting up with Shane in secret. Again."
                
                RL "Even if it's technically true."

                $ leaveairport = True
            
            else:

                show zzrl resigned

                RL "Better go."
        
        "Go somewhere other than the cottage" if loop >= 4: ## come back to this, this is fully not necessary

            show zzrl hesitant

            RL "Shane's not gonna be happy about this tomorrow...assuming there {i}is{/i} a tomorrow..."

            RL "Hmm, where should I even go...? What is there to do in Ottawa—"

            Girl "Oh my god, is that Rose Landry??"

            ##play audio
            "phonecamera.mp3"

            show zzrl wince

            RL "Damn it! Never mind, cottage it is."

            show zzrl resigned
            
            RL "...fingers crossed there {i}isn't{/i} gonna be a tomorrow..."

            $ papped = True

    if loop == 0:
        show zzrl flat
        
        RL "Now where's the car rental place... Ah, there we are!"
    
    elif loop == 1:
        show zzrl flat

        RL "Now where's the car rental...oh, exactly where I thought it would be. Huh."
    
    else:
        pass

    jump ctdoor

label giftshop:

    if giftshopvisit == 1:
        show zzrl eyebrow

        RL "Let's see what they stock at...Otta-welcomes You? Really?"

        $ giftshopvisit += 1

    menu:
        "What are you buying?"

        ## TBD more things, food Ilya will like, cigarettes?? little dog toy? fancy sunglasses? chocolate that rose likes and maybe gets to eat

        "Vodka":

            $ giftbought = "vodka"

            "You pick up a bottle of vodka."

        "Eye-wateringly expensive vodka":

            $ giftbought = "vodkaplus"

            "You pck up a bottle of expensive vodka."
        
        "Chocolate":
            $ giftbought = "choc"

            "You pick up a 50 piece box of Canadian Collection Chocolate Classics."

        "Wind-up toy otter": ## TBD you never actually included this

            $ giftbought = "otter"

            "You pick up a cute little otter that claps when you wind it up."
        
        "Airhorn":
            $ giftbought = "horn"

            "You pick up an airhorn. It looks loud."
        
        "An Ilya Rozanov Centaurs jersey" if svetpass >= 3: ## TBD you never actually included this
            $ giftbought = "jersey"

            "It took some digging, but there was indeed an Ilya Rozanov Centaurs jersey in the sports apparel rack. Seems like hockey's just not that popular here."

    menu:
        "Keep browsing?"

        "Yes":

            $ papped = True

            RL "Oh huh, wonder what they have over there—"

            Girl "Oh my god, is that Rose Landry??"

            ##play audio
            "phonecamera.mp3"

            RL "Damn it! Time to get out of here..."

        "No":
            Cashier "—here's your receipt thank you for shopping at Otta-welcomes you have a nice day."

            RL "Right. Thanks. Bye."
    
    jump ctdoor

label ctdoor:

    scene bg ctout
    with fade

    if loop == 0:

        ##play music
        "play music badthings1.mp3"

        show zzrl flat

        RL "...in your arms I'd start a war~ We've both been here before~"

        RL "Matter of fact—oh, there's Shane's cottage, finally!" ## is there a better line for this bit of turning off the road?

        ##stop music
        "stop music badthings1.mp3"

        ##play audio
        "cardoor.mp3"

        scene bg ctdoor

        show zzrl flat
        with fade

        RL "Hmm, Shane still hasn't seen my message... I hope they're at home..."

    elif loop == 1:

        ##play music
        "play music badthings1.mp3"

        show zzrl flat

        RL "...in your arms I'd start a war~ We've both been here...before..."

        RL "..."

        ##stop music
        "stop music badthings1.mp3"

        ##play audio
        "cardoor.mp3"

        scene bg ctdoor

        show zzrl flat
        with fade

        RL "This must be weird deja vu from all the photos Shane's sent me."
    
    elif loop == 2:

        ##play audio
        "play audio badthings2.mp3 that cuts off at 'we've both been here before line'" ## need to listen to make sure this works

        show zzrl wince

        RL "..."

        RL "...a different driving playlist, next time. If there's gonna be a next time, and I'm not just going crazy..."

        ##play audio
        "cardoor.mp3"

        scene bg ctdoor

        show zzrl flat
        with fade

    elif loop == 3:
        ##play audio
        "play audio attss1.mp3: this is the post-chorus in all the things she said that is just 'all the things she said' x10"

        RL "Not sure this playlist is any better..."

        ##play audio
        "cardoor.mp3"

        scene bg ctdoor

        show zzrl flat
        with fade

    elif loop == 4:
        ##play audio
        "play audio attss2.mp3: this is still all the things she said but it's 'yes I've lost my mind ... will I ever be free'"

        RL "...maybe next time I should just do podcasts. Or instrumental music."

        ##play audio
        "cardoor.mp3"

        scene bg ctdoor

        show zzrl flat
        with fade
    
    elif loop == 5:

        ##play music
        "play whatever actual instrumental music should be in this scene"

        RL "...if I didn't enjoy driving, this time loop would be actual hell."

        ##play audio
        "cardoor.mp3"

        scene bg ctdoor

        show zzrl flat
        with fade
    
    else:
        ##play music
        "play whatever actual instrumental music should be in this scene"

        RL "*Humming* ...here we are."

        ##play audio
        "cardoor.mp3"

        scene bg ctdoor

        show zzrl flat
        with fade

    menu:
        "Ring the doorbell":
            $ pt += "doorbell, "

            if doorbell == 0:

                $ doorbell += 1

                ##play audio 
                "click.mp3"

                show zzrl flat

                RL "Oh, the doorbell's not working."

                if loop >= 2:
                    RL "But I'm pretty sure that—yup, the door's unlocked."

                    jump bargein
                
                elif loop == 0:
                    pass

                else:
                    RL "Well, this didn't happen in my dream...I don't think..."

                show zzrl smile
                
                RL "Tsk tsk Shane Hollander! I was promised a fancy cottage with all the latest amenities! Better hope I don't leave a bad review on Airbnb."

                show zzrl surprised

                RL "Though the only visitor he gets probably doesn't bother with the doorbell, and just waltzes right in like—oh! The door's unlocked."

                jump entrance
            
            elif doorbell == 1 and loop == 1:

                $ doorbell += 1

                ##play audio 
                "click.mp3"

                RL "Oh, the doorbell's not working."

                RL "...just like in my dream..."

                jump entrance
    
            elif doorbell == 1:

                $ doorbell += 1

                ##play audio 
                "click.mp3"

                RL "Still broken huh."

                RL "Guess I'm going in anyway."
            
                jump bargein

            elif doorbell == 2: ## could cut this if too many lines and no one ever gets here

                $ doorbell += 1

                show zzrl resigned

                RL "Just going to...keep doing the thing that I know won't work, I guess."

                ##play audio 
                "click.mp3"

                RL "Yup, still doesn't work. Just like dating men and hoping they'll be heterosexual."

                jump bargein
            
            else:
                $ doorbell += 1

                ##play audio 
                "click.mp3"

                show zzrl resigned

                RL "Doorbell's still dead. Shocker."

                jump bargein
        
        "Knock on the door" if knockpass == False:

            if knock == 0 and loop == 0:
                $ pt += "knock, "

                $ knock += 1

                ##play audio 
                "knock.mp3"
                
                RL "..."

                RL "Maybe they're out after all..."

                show zzrl surprised

                RL "Ugh, I didn't drive two hours just to wait out here with only this hypnotically ugly sculpture for company, maybe—oh! The door's unlocked."

                jump entrance
            
            elif knock == 0:

                $ knock += 1

                ##play audio 
                "knock.mp3"

                RL "..."

                if loop == 1:
                    $ pt += "knock, "

                    RL "The door was unlocked, in my dream, I wonder if—oh, it {i}is{/i}."

                    jump entrance

                else:
                    RL "Guess this is just as pointless as the doorbell."

                    menu:
                        "Go in":
                            $ pt += "knock, "

                            jump bargein                            

                        "Knock harder":

                            jump knockharder
            
            elif knock == 1 and loop == 1:
                $ pt += "knock, "
                $ knock += 1

                ##play audio 
                "knock.mp3"

                RL "..."

                RL "Did I...do this in my dream too...?"

                RL "And then in my dream, I think...the door was unlocked, and—oh, it {i}is{/i} unlocked."

                jump entrance
            
            else:
                $ knock += 1

                RL "They didn't hear me last time, but..."

                ##play audio 
                "knock.mp3"

                RL "..."

                RL "Guys, come on, don't make me walk in on you."

                menu:
                    "Go in":
                        $ pt += "knock, "

                        jump bargein                            

                    "Knock harder":

                        jump knockharder
        
        "Knock on the door REALLY HARD" if knockpass == True:
            $ pt += "knockpass, "

            jump knockpass
        
        "Use your airhorn" if giftbought == "horn": ## cut if not funny/people aren't using it
            $ pt += "horn, "
            $ freedom += 1

            RL "...this feels kinda evil, but..." ## make this funnier please

            ##play audio
            "airhorn.mp3"

            IR "{size=-8}FUCK!"

            SH "{size=-8}Ow, fuck, my ass—I can't believe you fucking dropped me—"

            IR "{size=-8}—what the fuck was that! If it's another stupid Canadian bird—"

            SH "{size=-8}—what kind of bird would sound like that??"

            ##play audio
            "dooropen.mp3"

            show zzsh flat at center
            show zzir flat at midright
            with fade

            SH "Rose?!"

            show zzrl grin

            RL "Hey guys! Can I come in?"

            scene bg ctentrance
   
            show zzsh flat at center
            show zzir flat at midright
            show zzrl flat
            with fade

            RL "—that was my car, sorry. Tripped and fell on my horn, oops!"

            jump entrancepass
                        
label knockharder:

    ##play audio 
    "knockloud1.mp3"

    RL "..."

    RL "Really?? Is the sex so good it's blown your minds and your eardrums?"

    menu:
        "Just go in":
            $ pt += "knock, "

            jump bargein

        "Knock even harder":

            ##play audio 
            "knockloud2.mp3"

            RL "..."

            RL "Next time, I swear I'm buying an airhorn at the gift shop."

            menu:
                "Just go in already":
                    $ pt += "knock, "

                    jump bargein

                "Knock even HARDER":
                    $ pt += "knockpass, "

                    $ knockpass = True

                    jump knockpass

label knockpass:

    ##play audio 
    "knockloud3.mp3"

    SH "{size=-8}...there someone at the door??"

    IR "{size=-8}Thunder. Cat. Delivery. Ignore it."

    ##play audio 
    "knockloud3.mp3"

    SH "{size=-8}What? No, I think that's...{/size} {size=-5}There's someone at the door, is that—"

    $ freedom += 1

    scene bg ctentrance
   
    show zzsh flat at center
    show zzir flat at midright
    show zzrl flat
    with fade

    ##play audio
    "dooropen.mp3" # this lives here because entrance goes into entrancepass also

    jump entrancepass

label bargein:
    
    $ bargecount += 1

    ##play audio
    "dooropen.mp3"

    if bargecount == 1:

        RL "Hey guys! It's Rose! I'm early!"
    
    elif bargecount == 2:

        RL "NO ONE EXPECTS THE LANDRY INQUISITION!"
    
    elif bargecount == 3:

        RL "I'm BACK!"
    
    elif bargecount == 4: ## check singing with rose, or swap out with non-singing line

        RL "Your moon~ Your moon and your man~"

        RL "Don't moon~ Don't moon me again~"

        $ bargecount = 1

    jump entrance
    
label entrance:

    ##play audio
    "dooropen.mp3"

    if loop == 0:

        scene bg ctentrance

        show zzrl flat
        with fade
        
        RL "Oh look, a painting done in the classic tradition of the rich-and-fancy-house art movement: mud smears."
        
        RL "Really, Shane, is this the view you want to welcome visitors with—"

        scene cut boys_doorway
        with fade

        RL "Oh shit!"
    
    elif loop == 1:
        scene bg ctentrance

        show zzrl flat
        with fade

        RL "These are...very familiar mud smears..."

        scene cut boys_doorway
        with fade

        RL "Oh shi—wait a second..."

    else:
        scene cut boys_doorway
        with fade

        RL "Hi Ilya, hi Shane, hi Shane's ass."

    IR "What?"

    SH "Wha—Rose! Fuck!"

    if loop == 0:

        RL "It's cool, all good, I'm closing my eyes, turning around, backing away—"

        scene black
        with pixellate

        ##play audio 
        "crash.mp3"

        scene cut boys_doorway
        with pixellate

        RL "Whoops, shit, what did I kick—is this a horse?? Oh, sorry, my eyes are open again—"
    
    elif loop == 1:

        RL "...very familar naked butts, too..."

        IR "What are you staring at."

        RL "Nothing! I'm, um—never mind, closing my eyes now!"
    
    else:

        RL "It's cool, it's fine, nothing I haven't seen before."

    scene bg ctentrance
   
    show zzsh embarrassed at center
    show zzir annoyed at midright
    
    show zzrl hesitant_blush
    with fade

    SH "Sorry, fuck, sorry Rose, we're dressed. Sorry you had to see that."

    IR "Sorry? She should be grateful to see your beautiful ass again."

    show zzsh annoyed

    SH "Oh, fuck you, Rozanov."

    IR "I was trying to, until {i}someone{/i} interrupted—"

    if loop == 0:
        show zzrl grin

        RL "Haha, my bad! But hey, great views at your cottage huh, just like you promised."
    
    elif loop == 1:
        show zzrl thoughtful

        RL "Ah, my bad. Pretty sure my subconscious tried to warn me, but..."
    
    elif loop == 2:
        show zzrl resigned

        RL "Sorry, promise I'll try harder not to intrrupt, next time. Or...maybe I should be trying harder to interrupt?"

    else:
        show zzrl resigned

        RL "Yeah, my bad, I'll try to do better next time."

    show zzsh embarrassed # this lives here because there's no need for Shane to be embarrassed if you don't barge in on them

    jump entrancepass

label entrancepass:

    SH "What? You—wait, Rose, what are you even doing here? You're not supposed to get here until...another forty minutes?"

    if loop == 0:
        show zzrl grin

        RL "Yeah, sorry, my flight got in early. I tried texting you but I guess you were...otherwise occupied."

        show zzir smirk

        IR "Yes, Shane's beautiful ass was about to be otherwise occupied by my—"

        show zzsh annoyed

        SH "{i}Ilya!{/i}"
    
    elif loop == 1:
        show zzrl hesitant

        RL "Yeah, sorry, my flight got in early. I tried texting you...no wait, maybe I didn't. Sorry."

    else:
        show zzrl resigned

        RL "Yeah, my grasp on time isn't great today."

    show zzsh smile_blush

    SH "Anyway, uh, welcome to my cottage. Thanks for flying all the way up here just for dinner, I know you've been really busy."

    if loop == 0:
        show zzrl smile

        RL "Hey, it's no problem! If anything, you've been the busy one lately, I feel like we've barely talked all year!"

        show zzsh hesitant

        SH "Sorry, I know I've been... It's just, with Ilya being in Ottawa, and—"

        show zzrl grin
        
        RL "Hey, no, don't apologise! I know you guys don't get much time together, so actually {i}I{/i} should be thanking {i}you{/i} for letting me come up here and interrupt your...alone time."

        show zzsh embarrassed

        SH "Oh my god, stop, it's—whatever. Anyway, Ilya's best friend is coming by for dinner too, so it's only fair."

        show zzrl hesitant

        RL "Right, yes. Svetlana, you said? Svetlana...Vetrova?"

    elif loop == 1:
        show zzrl hesitant

        RL "Yeah. For sure. Happy to be here. You could say it's a dream come true..."

        show zzsh hesitant

        SH "...What?"

        show zzrl smile

        RL "Sorry, nothing! Just happy to see you again!"

        show zzsh flat

        SH "Anyway, Ilya's best friend is coming by for dinner too, so it's only fair."

        RL "Yes, of course, Svetlana."
    
    else:
        RL "The days {i}are{/i} starting to blur together."

        if loop == 3: ## come back to this, this is clunky way to introduce the take a nap
            "{i}Your mind is getting blurry too. How many times have you heard Shane say the same thing now?{/i}"
            
            "{i}Maybe it's okay to zone out a bit. Or just take a nap—you do have an Ambien.{/i}"
            
            show nvl
            centered "Hit 'tab' on your keyboard or click the 'Skip' button below to fast-forward through any dialogue you've seen. Or choose to take a nap, if you're given the option, to restart the loop."
            hide nvl

        RL "But hey, it's not so bad. Lots of worse places to be, lots of worse people to see."

        SH "Haha, yeah, I suppose. Anyway, Ilya's best friend is coming by for dinner too, so it's only fair."

        RL "Yes, Svetlana's coming too, I know."

    show zzir eyebrow

    IR "You know Svetlana?"

    if loop == 0:
        menu:
            "Yes":
                pass

            "No":
                pass

        RL "Well, not personally. But sometimes hockey media will talk about you two and...ah..." ## 'hockey blogs'...? press? paps??

        show zzir frown
        show zzsh frown

        SH "Well, obviously she and Ilya aren't—"

        show zzrl hesitant_blush

        RL "Oh, no no, of course not, I just meant—never mind. Sorry."
    
    elif loop == 1:
        menu:
            "Yes":
                pass

            "No":
                pass

        RL "Well, not personally. But sometimes...hockey...media..."

        show zzrl hesitant

        RL "I mean! Sometimes you think you don't know a person but you, er, actually do...? Like, spiritually, or something."

    elif loop == 2:
        menu:
            "Yes":
                $ random = 10
                pass

            "No":
                $ random = 11
                pass
        
        RL "Yes—I mean, no, I—I mean, maybe...?"

        show zzir eyebrow

        IR "How do you not know whether you know someone or not."

        show zzrl resigned

        RL "...that is a very good question. I wish I had an answer."

    else:
        menu:
            "Yes":
                $ random = 10

                show zzrl resigned

                RL "Yeah, I know her better than you think I do. Better than she thinks I do too, probably."

                show zzir annoyed
                $ ilyaheart -= 1

                IR "What do you mean. You read a lot of paparazzi bullshit about her or something?"

                RL "No, no, if only my sources were that mundane."
            
            "No":
                $ random = 11

                show zzrl thoughtful

                RL "Can anyone ever truly know another person?"

                SH "Um. Yes?"

                RL "I mean, if you meet someone a hundred times, but they never get to know you back, does it still matter?"

                IR "...yes."

    SH "Uh. Okay. That's..."
    
    SH "You know what, never mind. Why don't I, um."
    
    SH "I should show you around."

    show zzir eyeroll

    IR "Show her around? Why? She is flying off again after dinner, not staying here tonight."

    show zzsh annoyed

    SH "{i}Ilya.{/i} It's polite, okay? We're going to be polite."

    menu:
        "Agree to the house tour":

            if papped == True:
                show zzrl smile
                
                RL "Thanks Shane, I'd love a tour of the cottage. This place is—"

                jump paptalk

            if tourloop == 0 and notourloop == 0:

                show zzrl hesitant

                RL "Thanks Shane, I'd love a tour of the cottage. It's bigger than I thought it would be!"

            elif tourloop == 1 or notourloop == 1:

                show zzrl thoughtful

                RL "Thanks Shane, I'd love a tour of the cottage. It's...exactly as big as I thought it would be."

            else:
                show zzrl smile

                RL "House tour, right, let's go! Tell me all about your sexy hard wood and exposed beams."

                show zzsh hesitant

                SH "...okay, let's. Do...that."

                jump housetour
            
            show zzir smirk

            IR "{size=-8}...that's what he said...before we were rudely interupted by—"

            SH "Ilya, for fuck's sake—go do dinner prep or something! I'm going to show Rose around."

            IR "Oh, now I can dinner prep myself? Yesterday, it's 'Ilya, too much salt, not good for your heart' and 'Ilya, that's not how the stove works, you will burn the cottage down', and today Rose Landry is here and I am allowed in the kitchen all by myself?"

            show zzsh smirk

            SH "Yes, and if you burn the cottage down I'm making you sleep on the ashes of the couch."

            show zzir smirk

            IR "I've slept in more terrible places because of you. Like that time in—"

            show zzsh embarrassed

            SH "Go. Prep. Dinner. Ilya!"

            show zzir eyeroll

            IR "Okay, okay, I'm going, have fun with your house show, Mr Real Estate. Break a leg, Rose Landry."

            hide zzir with easeoutright
            
            show zzsh eyeroll

            SH "You don't say 'break a leg' for house tours."

            show zzrl resigned

            RL "...somehow I feel like he meant that literally."

            jump housetour

        "Decline the house tour":

            show zzrl hesitant

            if papped == True:
                RL "Maybe Ilya's right, there's no need. Let's sit, have a drink—"

                jump paptalk

            RL "Maybe Ilya's right, there's no need. Let's sit, have a drink, get to know each other!"
            
            if giftbought == "vodka": ## rejig this once the gift stuff is finalised
            
                RL "Oh, I bought vodka for you guys?"

                show zzir eyeroll 
                $ ilyaheart -= 1

                IR "Tsk, is this the cheap stuff from the airport gift shop? Would rather drink well water."

            elif giftbought == "vodkaplus":

                RL "Oh, I bought vodka for you guys? This is the good stuff, right?"

                show zzir eyeroll 

                IR "Tsk, expensive vodka is not always good vodka. Clearly money cannot buy good taste."

            else:

                RL "Oh, I brought wine!"

                show zzir eyeroll

                IR "Think I will need something stronger than wine for this..."

            jump teatime

        "Take a nap" if loop >= 3:
            show zzrl hesitant

            RL "Actually, I might just take a nap instead."

            SH "Oh, sure. You've got to be tired after your flight. Here, I'll show you one of the guest rooms..."

            scene black
            with fade

            $ loop += 1

            jump start_real

label teatime:
    $ pt += "tea, "

    scene bg dining

    show zzsh flat at center
    show zzir flat at midright
    show zzrl flat
    with fade

    if tealoop == 0:
        $ tealoop += 1

        call teatime.ilya

    elif tealoop == 1:

        $ tealoop += 1

        menu:
            "Talk about Ilya":
                call teatime.ilya

            "Talk about Shane":
                call teatime.shane
    
    elif tealoop == 2:

        $ tealoop += 1

        menu:
            "Talk about Ilya":
                call teatime.ilya

            "Talk about Shane":
                call teatime.shane

            "Talk about Svetlana":
                call teatime.sveta
                
                jump svet_entrance

    ##play audio
    "knockloud2.mp3"

    show zzsh flat

    SH "Oh! That must be Svetlana."

    jump svet_entrance

label teatime.ilya:
    show zzrl hesitant

    RL "So, um, Ilya, how are things? Must be exciting being on a new team this year, huh?"

    IR "...Exciting. Yes, very exciting. Very exciting being bottom of the Eastern Conference and missing playoffs, convenient for making plans for my very long, very exciting summer."

    show zzrl hesitant

    RL "Oh, that's...I mean, I know the Centaurs aren't doing great, but there's, um, potential, right? And...and now they have you, and—"

    show zzir eyeroll

    IR "Yes, now they have me, soon I will be playing full sixty minutes and I will win Ottawa the first cup in twenty years all by myself."

    show zzsh frown
    
    SH "Ilya."

    show zzir smirk

    IR "Oh, you think I cannot play full sixty minutes if I want, Hollander? You doubt my endurance? Because—"

    show zzsh eyeroll

    SH "No one can play the full sixty minutes, asshole."

    IR "—I can prove my endurance to you, right now, if you kick Rose Landry out again—"

    return

label teatime.shane:
    $ shanetea = True

    show zzrl hesitant

    RL "So, Shane, how are things? You said you guys were thinking of coming out to your teams, did you think about it some more...?" ## too direct..?

    show zzsh frown

    SH "Oh, um, yeah, I told my team a few weeks after I told you about Ilya. I didn't say...?"

    show zzrl surprised

    RL "No you did {i}not{/i} say! Wait, so they know you're with Ilya?"

    SH "Oh, no, no, fuck no. They just know—I just told them that I was. You know."

    show zzrl hesitant

    RL "Gay...?"

    show zzir smirk

    IR "Super gay."

    show zzsh eyeroll

    SH "A totally normal amount of gay, Rozanov, fuck you."

    show zzrl grin

    RL "I think being gay is kinda like...oh, liking chocolate. There's not really a normal amount, you just like what you like."

    show zzir eyebrow

    IR "...And how much do {i}you{/i} like chocolate, Rose Landry?"

    show zzrl surprised_blush

    RL "Oh, haha, I mean, we're not talking about me!"

    show zzrl smile

    RL "So, hey, how did it go? You thought some of them would be good about it, right?"

    show zzsh hesitant

    SH "Yeah, I mean, some of them have been alright. And some of them...I mean, look, no one's really said anything to me about it."

    show zzir frown

    IR "You said everything is fine."

    show zzsh frown

    SH "It {i}is{/i} fine. It's good that no one's said anything, right? I didn't want it to distract from the hockey."

    show zzrl hesitant

    RL "But not everything is about the hockey, though...?"

    show zzir eyeroll

    IR "Not everything is about the hockey? Rose Landry, this is the first time you are meeting Shane Hollander? Let me introduce you to the second best player in the league—"

    show zzsh wry

    SH "Shut up, Rozanov. Look, I know not everything's about hockey, okay?"

    show zzsh frown
    
    SH "It's just. These guys are my team. As long as the hockey's still working, that's the most important thing, right?"

    show zzrl hesitant

    RL "Is it...? I dunno, Shane, these guys are the people you see more than anyone else. More than your family. More than Ilya."
    
    RL "If the stuff other than the hockey isn't working, if they're not gonna be good about you being who you are, then..."

    SH "Then what? I get myself traded to another team?"

    RL "No, no, I just mean...look, what about You Can Play? Didn't some of the Metros join that...? I saw JJ Dagenais did, and Hayden Pike—"

    show zzir smirk

    IR "Hah, Pike probably wishes he were gay so that someone will finally say to him that he can play—"

    show zzsh annoyed

    SH "Oh, fuck off, Rozanov, Hayden was good about it, okay? I mean, at least until I told him about—"

    return

label teatime.sveta:
    $ svetatea = True

    show zzrl smile

    RL "So, tell me more about Svetlana!"

    if random == 10:
        show zzir annoyed

        IR "Why? Thought you know all about her."

    else:
        show zzir annoyed

        IR "Why do you care? Thought you don't know her."
    
    show zzsh annoyed

    SH "Ilya."

    show zzir eyeroll

    IR "Fine. She is Russian. Very pretty, very smart. Out of your league, Rose Landry."

    show zzsh frown

    SH "...not out of {i}your{/i} league though."

    show zzir hesitant

    IR "...солнышко. You know I am in {i}your{/i} league now. No one else." ## check russian, check book endearments. should this be in cyrillic? come back to this whole league bit anyway i don't know i like how unsubtle it is and also maybe it's not funny and goes on too long

    show zzsh embarrassed

    SH "...yeah, I know. Sorry."

    show zzsh wry

    SH "I mean, technically we're both in the MLH, so really—"

    show zzir smirk

    IR "We're both in the same league, yes. But also—what is the thing the media says? We are in our own league?"

    show zzsh smirk

    SH "In a league of our own."

    IR "Yes. We are in a league of our own. Should play against each other only, and not have to play in the same league as dinosaurs like Scott Hunter. Hockey should be for humans—"

    SH "Sure, Rozanov, you can take it up with the commissioner."

    show zzsh smile_blush

    SH "Ah, sorry, Rose, you were asking about Svetlana. Like I told you, she's Ilya's best friend. She lives in Boston, but visits Moscow a lot."

    show zzsh frown

    SH "And Ottawa too. She visits Ottawa a lot too, now. More than I do, probably."

    SH "Which is good. It's, uh..."

    show zzir hesitant

    IR "You know, Sveta also likes the dumb toys she had when she was small. Noisy wind-up things, little animals. Too sentimental to throw them out even after they break."

    IR "Probably why she still likes me, okay?"

    show zzsh frown

    SH "You're not broken—"

    show zzir eyeroll

    IR "Okay, okay, so you are the noisy toy, not me. So she will like you too."

    show zzir smirk

    IR "Very easy to wind up, very fun to play with, like a little animal in—"

    show zzsh annoyed_blush

    SH "{i}Ilya{/i}"

    ##play audio
    "knockloud2.mp3"

    show zzsh flat

    SH "Oh! That's probably her now."

    return

label housetour:

    scene bg room1

    show zzsh flat at center
    show zzrl flat
    with fade

    SH "...and the exposed ceiling beams, which as you can see match the hardwood floors, are also made of oak."

    SH "So here's one of the two guest rooms on this floor. The bigger guest room is downstairs, but all three have their own TV, king-sized bed, and en-suite bathroom This room's got east-facing windows, so it gets a lot of sunlight in the mornings."

    show zzrl grin

    RL "Wow, Shane, Ilya's right, you really are Mr Real Estate!"

    show zzsh embarrassed

    SH "Oh, sorry, I guess you don't really need to know all this stuff. I mean, like he said, you're not staying over, so who cares about the guest rooms?"

    menu: ## phrase the choice less word of god
        "Continue the house tour": ## different rose dialogue 1st time vs other loops
            $ pt += "house tour, "

            $ tourloop += 1

            show zzrl smile

            RL "No, hey, Shane, it's cool that {i}you{/i} care this much about the guest rooms, y'know? You must have put a whole lot of time and effort into this place."

            show zzsh wry

            SH "Yeah. I finished reading two whole architecture textbooks during the design phase."

            show zzrl grin

            RL "No way!"

            SH "Don't make fun of me."

            show zzrl smile

            RL "I wouldn't! It sounds like you really like being able to build a place exactly how you want it, from the ground up."

            SH "Right, yeah. I've lived in a few places, and there's always something...not quite right about them, you know?"
            
            RL "I know what you mean! The light's always too bright or too dark, or there's a clunking in the walls, or it's got windows in weird places. And it's like, I just wanna be totally comfortable when I'm home!"

            SH "Exactly. I just wanted a place I can be comfortable. A place that..."

            RL "That you can fully relax."

            show zzsh smile

            SH "That, yeah."

            RL "I love it. I'm so glad you have your middle-of-nowhere lakeside mansion with its fancy guest rooms and one million windows. I'm so glad you get to bring Ilya here."
            
            RL "You guys deserve to have all this peace, all this sunlight."

            SH "I...yeah. Thanks, Rose. I love it too."

            if outside >= 3:

                menu:
                    "Ask Shane about curtains":
                        $ room1blind = True
                        
                        show zzrl grin

                        RL "Though I gotta say, with all the windows and no curtains? It's got the vibes of like, you love sunlight, sure, but you also love exhibitionism."

                        show zzsh embarrassed

                        SH "{i}Rose{/i}, what, I don't—I mean, this house has blinds! On all the windows!"

                        show zzrl eyebrow

                        RL "Really? Where?"

                        SH "It's, there's a remote, it's in this, uh..."

                        RL "Chunk of half-melted legos?"

                        SH "Artistic...container. It opens like...this?"
                        
                        SH "No, wait, you turn {i}this{/i} bit...and then you press {i}that{/i}..."

                        RL "Oh, it's a puzzle box?"
                        
                        SH "...I don't think it's meant to be. The interior designer said—{i}aha!{/i} Here!"

                        RL "Well, at least the remote looks normal. I assume it doesn't make anything in here explode or—"

                        ##play audio
                        "knockloud2.mp3"

                        SH "Oh! That must be Svetlana."

                        RL "...wow, we spent more time than expected trying to get to that remote, huh."

                        jump svet_entrance

                    "Carry on the house tour":
                        pass

            RL "I especially love that all your guest rooms have en-suites. Shared bathrooms are the worst."

            SH "Hah, yeah, I know. That was the first thing I decided on for the guest rooms."

            RL "Did you pick the decor as well? I mean, clearly this room is...themed...?"

            SH "Oh yeah, it's, um, post-modern. And no, I didn't pick it, the interior designer did." ## post-modern??

            RL "Oh thank God. I didn't wanna say anthing, especially when we were just talking about you making this place to your exact specifications, but Shane! The decor in this room! Really??"

            show zzsh wry

            SH "I mean, it's just decorations, right? It's not like that stuff matters as much as the layout and materials." ## need actual real estate terminology here
            
            show zzrl grin

            RL "I dunno, I think it kind of matters? Like what even is that thing with all the wires hanging above the door? It looks like it might fall onto your head any time! And is it...ticking? Is it...a bomb?"

            SH "Oh, that's the clock. I think."

            RL "A clock? But it doesn't have hands? Or numbers??"

            SH "I mean, I kinda assume everyone checks their phone if they want to know the time, really."

            $ shane_room1 = True

            SH "Anyway, let me show you some of the other rooms."
            
            menu:
                "See the west-facing guest room":
                    scene bg room2

                    show zzsh flat at center
                    show zzrl flat
                    with fade

                    RL "Okay, we've gone from way too much going on to way too little. This room just has a bed...? Excuse me, what happened to the TV and bathroom I was promised?"

                    SH "Oh, it's all hidden. You wave your hand over this panel here—" ## add a {nw} after voice is added...?
                    
                    ##play sound
                    "switch.mp3"

                    SH "—and the TV slides down from the ceiling. And you wave your hand {i}here—{/i}"

                    ##play sound
                    "switch.mp3"

                    RL "Whoa! I didn't know there was a door there! Oh, that's where the bathroom is!"

                    SH "Yeah, everything's hidden because of the minimalist aesthetic, apparently. The panel for the bathroom lights and floor heating is all hidden near the door here too."

                    if outside >= 3: ## this used to be svetpass >= 1 but i think that just slows the game down

                        menu:
                            "Ask Shane about curtains":
                                $ room2blind = True
                                
                                RL "Any chance there's curtains hidden too? Cause I gotta say I'm feeling a little exposed in here, if you know what I mean."

                                show zzrl grin

                                RL "Which, hey, maybe that's also meant to be part of the aesthtic, I dunno what you or your guests get up to in the privacy of—"

                                show zzsh embarrassed

                                SH "Oh my god, Rose, I don't—there's blinds! They're just hidden!"

                                SH "You wave your hand over this panel near the bed and—"

                                ##play sound
                                "switch.mp3"

                                show zzsh wry

                                SH "—and look, all the privacy you want."

                                RL "Fun! Although having a motion sensor so close to the bed that might accidentally bring the blinds up and down—"

                                ##play audio
                                "knockloud2.mp3"

                                SH "Oh! That must be Svetlana."

                                RL "Better ask if she likes living dangerously."

                                jump svet_entrance

                            "Carry on the house tour":
                                pass

                    RL "Did you have a different interior designer for each room...? Did you fire the last guy after he tried to plant a bomb on your wall?"

                    show zzsh embarrassed

                    SH "Ah, haha, no, but. They gave me a checklist of design elements to, er, find my unique personal style or something, and I just checked everything because it all seemed fine?"
                    
                    SH "And it was the middle of playoffs, so I might have missed a few emails after that..."

                    show zzrl grin

                    RL "Well, Shane, I have to say your unique personal style is a lot more eclectic than your game day suits would have led me to believe."

                    show zzsh wry

                    SH "Shut up, Landry, my stylist makes me wear colours now."

                    RL "Hate to break it to ya', pal, but white is not a colour—"

                    $ shane_room2 = True

                "See the guest room downstairs":
                    scene bg room3

                    show zzsh flat at center
                    show zzrl flat
                    with fade

                    RL "This one has much more normal decor, I have to say."

                    SH "Yeah, I built this one for my parents. That's why there's two walk-in closets."

                    if outside >= 3:

                        menu:
                            "Ask Shane about curtains":
                                $ room3blind = True

                                show zzrl grin
                                
                                RL "Any chance you thought they might want curtains too?"

                                SH "Oh, yeah, there's a remote for the blinds behind the lamp here."

                                show zzrl thoughtful

                                RL "Gotcha. You know, I can't help noticing that this place is completely different from your place in Montreal. I mean, sure, that's an apartment in the city instead of a mansion out by a lake, but..."

                                SH "I guess I mainly picked my apartment in Montreal for how close it is to the rink and how good the security is. It's not like I spend much time there."

                                show zzrl eyebrow

                                RL "You don't spend much time...in the place that you live for most of the year...?"

                                SH "I mean, most of the season, if I'm not at the rink, I'm at the gym, or asleep. And it's not like I have to host the team, cause Hayden does that."

                                SH "Montreal is for hockey, right? And this cottage, the summer, this is for me."

                                show zzrl hesitant

                                RL "Oh, Shane, that's—"

                                ##play audio
                                "knockloud2.mp3"

                                SH "Oh! That must be Svetlana."

                                jump svet_entrance

                            "Carry on the house tour":
                                pass
                    
                    RL "Don't they have their own cottage ten minutes away? Why would they need even one walk-in closet, let alone two of this...size..."

                    RL "..."

                    RL "Shane, why are your trophies in here? No wait, are these Ilya's...?"

                    show zzsh embarrassed

                    SH "Well, he doesn't really have the room where he lives, and he liked the idea of having some of them here. I was supposed to bring mine too, we were gonna renovate and have a trophy room for us both together, but we haven't had the time, so..."

                    show zzsh flat

                    SH "Anyway. This guest room has a spacious bathroom with double shower heads and two vanities. And the room itself is fully soundproofed."

                    RL "Soundproofed? Shane Hollander, what sort of wild, noisy things do you think your parents might get up to in this room?"

                    show zzsh embarrassed

                    SH "That's not—Rose!"

                    RL "Or maybe I should say, what sort of wild, noisy things do you think you're gonna get up to while your parents stay in your guest room?"

                    show zzsh smile_blush

                    SH "Oh my god, I just thought they might not want to be disturbed if I have to wake up in the middle of the night for a glass of water, that's all! I wasn't even thinking of Ilya when I designed this place!"

                    show zzrl grin

                    RL "Hey, I didn't say anything about Ilya, I just—"

                    $ shane_room3 = True

        "Stop the house tour":
            $ pt += "fake house tour, "

            RL "I promise, I do care, I think it's cool that you were so involved in designing every inch of this cottage, y'know?"

            RL "I just also care about {i}you{/i}."

            SH "What?"

            if notourloop == 0:
                $ notourloop += 1

                RL "How are {i}you{/i}, Shane? I want a tour of the interiority of Shane Hollander, not just his cottage."

                show zzsh smirk

                SH "I dunno, I don't think Ilya's gonna like me giving you a tour of my interior..."

                show zzrl grin

                RL "Oh my, Shane Hollander! I mean, what if it turns out that I prefer being the peg to the—" ## this joke not landing

                show zzsh embarrassed

                SH "Rose Landry! You do not! ...do you??"

                RL "Maybe, maybe not, but I don't wanna talk about me today. I wanna talk about my best friend, who I haven't talked to in {i}ages{/i}."

                show zzsh hesitant

                SH "Ah, sorry, I know I haven't been the greatest at keeping in touch. It's just, this year's been... With Ilya in Ottawa..."

                show zzrl grin

                RL "You're spending all your free time driving two hours for a booty call with the new boyfriend?"

                show zzsh embarrassed

                SH "No!"

                show zzsh smile_blush

                SH "I mean, sort of."

                show zzrl smile

                RL "Hey, it's great you're enjoying the honeymoon period, even if it's a little bit long distance, right?"

                show zzsh hesitant

                SH "I...hah, right, yeah, I mean it can't get any better than this—"

                $ random = 2

            else:
                $ notourloop += 1

                menu:
                    "How are you and Ilya doing?":

                        RL "I feel like I haven't talked to you enough lately, y'know? How are you doing, actually? You and Ilya?"

                        show zzsh hesitant

                        SH "Ah, sorry, I know I haven't been the greatest at keeping in touch. It's just, this year's been...with Ilya in Ottawa..."

                        show zzsh smile

                        SH "Anyway, we've been good."

                        show zzrl smile

                        RL "Yeah? I mean, obviously I can see for myself how much y'all are enjoying each other in the summer."

                        if freedom == 0:
                            show zzrl grin 

                            RL "If you know what I mean."

                            show zzsh embarrassed

                            SH "Rose, oh my god, you weren't even supposed to get here for another half an hour at least!"

                            RL "Sorry, my bad. {size=-8} Maybe next time I'll text you just to say I did."

                            show zzrl hesitant

                            RL "But anyway, I meant to ask, how are things during the season...?"
                        
                        else:
                            show zzrl hesitant

                            RL "But what about during the season...?"
                        
                        show zzsh hesitant

                        SH "Ah. Yeah. I mean, it's still pretty good, I guess?"

                        RL "Right, good, that's good. I just thought...I mean, long distance can be hard work, right?"

                        show zzsh frown

                        SH "Yeah, I guess so. But this is as good as it gets, right? There's no closer team to Montreal than Ottawa."

                        if svet_room1 == True:

                            RL "So you haven't considered moving to Ottawa too?"

                            show zzsh eyebrow

                            SH "Moving to {i}Ottawa?{/i}"

                            RL "I mean, you're a free agent in, what, two years? You guys could close the gap, right?"

                            SH "By {i}leaving the Metros?{/i}"

                            RL "Ah, haha, sorry, that's crazy talk, I know, it's just something Svetlana said that—"
                            
                            RL "—I mean, never mind, that's—I know you've always wanted to retire a Metro, and also if you left, the city would probably riot, it's just..."

                            show zzsh frown

                            SH "It's just that Ilya left Boston for me? So why wouldn't I do the same for him?"

                            show zzrl wince

                            RL "Okay, I didn't mean it like that, I know relationships aren't a competition—"

                            SH "But if it {i}were{/i} a competition, Ilya would be winning."

                            show zzrl eyebrow

                            RL "..."

                            RL "Okay, but if relationships {i}were{/i} a competition, you two wouldn't be rivals. You'd be teammates. And you're trying to score the most, um, relationship happiness points {i}together{/i}. Doesn't mean you both have to do the same thing, right?"

                            SH "But you think Ilya's doing more to help our team score—to make us both happiest, fine."

                            RL "...there's no Hart Trophy for relationships, Shane."

                            SH "Right, sure, but—"

                            $ shanemove = True

                            $ random = 1

                        else:

                            show zzrl grin

                            RL "True. Now all you gotta do is get the cup next year and you're golden!"

                            show zzsh wry

                            SH "Don't jinx it, shit."

                            SH "But yeah, with the team, and with Ilya, I think everything's in the right place, y'know? The plan's solid, the rest is just hard work. And I'm not scared of hard work, it's—"

                            show zzsh frown

                            $ random = 2
                    
                    "How can I make Ilya like me?":
                        show zzrl smile

                        RL "I feel like I haven't talked to you enough lately, y'know? How are {i}you{/i}, Shane? And how's Ilya?"

                        show zzsh hesitant

                        SH "Ah, sorry, I know I haven't been the greatest at keeping in touch. It's just, this year's been...with Ilya in Ottawa..."

                        RL "No, hey, don't apologise, I've been busy too! And actually, speaking of Ilya...oh boy, how do I ask this..."

                        show zzrl hesitant

                        RL "How do I make him like me...??"

                        show zzsh frown

                        SH "Uh..."

                        SH "Make him like you...?"

                        show zzrl resigned

                        RL "Yeah. Look, I know it's totally normal to hate your boyfriend's ex. But I'm not just your ex, I'm your friend, right?"

                        SH "You are. You're one of my best friends."

                        show zzrl smile

                        RL "Right back at 'cha!"
                        
                        RL "And like, usually that's good enough for me, I don't need to be besties with all my besties' boyfriends, but...there's extenuating circumstances that I can't explain without sounding crazy."

                        RL "So, Coach, what's the play here? What should I be doing to try to score some platonic points with your guy?"

                        show zzsh embarrassed

                        SH "Hah, shit, I wish I knew."

                        show zzsh hesitant

                        SH "I mean, it's, um, nice that you want to. You're the only one I've told about Ilya who's been happy about it right from the start. And that's. Really nice."

                        SH "So I also want him to like you. But I have no idea how I even made him like {i}me.{/i}"

                        show zzsh smile_blush

                        SH "I mean, I have some idea, but I don't think that's something you should be, uh, attempting with my boyfriend—"

                        show zzrl grin

                        RL "Shane Hollander, you mean to say you think the only way to your boyfriend's heart is through his dick?"

                        show zzsh wry

                        SH "Not the only way! But he and his best friend did use to sleep together, so that's a play that works—I mean, I guess so did you and me, so—"

                        RL "Hey, I'm willing to do what it takes to get that puck in deep. If you know what I mean."

                        show zzsh smile_blush

                        SH "Oh my God, Landry, stop. He likes...hockey? And, um...drinking? Smoking? Food that's bad for him?"

                        show zzrl grin

                        RL "Soooo if I want him to like me I should try to kill him? I mean, I'm happy to try, they did make me do all my own stunts for my last shoot—"

                        show zzsh smirk

                        SH "You mean the two punches they let you throw before you got kidnapped again?"

                        RL "Bet that's still more punches than you've thrown in your career, Hollander, and if you want me to demonstrate—"

                        SH "No thanks, wouldn't want to break your fist with my jaw. Anyway, Ilya also likes dogs, and fashion, and—"

                        show zzsh hesitant

                        $ random = 2
            
                    "Is Ilya doing okay?" if outside >= 1: ## maybe the temp living situation in ottawa for ilya
                        show zzrl smile

                        RL "I feel like I haven't talked to you enough lately, y'know? How are {i}you{/i}, Shane? And how's Ilya?"

                        show zzsh hesitant

                        SH "Ah, sorry, I know I haven't been the greatest at keeping in touch. It's just, this year's been...with Ilya in Ottawa..."

                        show zzrl hesitant

                        RL "Yeah, he's been in Ottawa for a year now, right? Has it been tough for him...?"

                        SH "Tough...? I mean, obviously the Cens aren't good. But they're getting better. Look, we've both been on rebuilding teams before, and Ilya says he likes their chances better now that they've got Hayes, which—"

                        RL "I wasn't asking about the hockey—well, I guess it is kinda about the hockey. Because his team's worse now, and also he doesn't know anyone in this city—"

                        show zzsh frown

                        SH "He knows my parents. And his teammates. I probably know fewer people in Montreal."

                        RL "Right. Yeah. But..."

                        SH "Rose. Do you think Ilya shouldn't have moved here?"

                        if svet_room3 == True:

                            RL "I...I don't know, it's just that Svetlana said—"
                            
                            show zzrl wince

                            RL "I mean, it doesn't matter what {i}I{/i} think, right? I don't know Ilya. But you know Ilya. Do you think he's happy here...?"

                            show zzsh frown

                            SH "I...I don't know. He says he's fine. But..."

                            RL "But he might just be saying it? Yeah, I get that. Still, you can tell if he likes it here by things he does, right?"

                            SH "The things he does...?"

                            RL "If he likes it here, then he might, say, buy a house here that he wants to stay in permanently right? Renovate it exactly how he likes it, like you did with your cottage. Make sure it has space for all his trophies."

                            SH "...how did you know about his trophies?"

                            RL "Oh, haha, that was just a hypothetical! I mean, I don't know Ilya at all, really!"

                            RL "Actually, maybe you should ask someone who {i}does{/i} know him, like—"

                            $ shanesveta = True

                            ##play audio
                            "knockloud2.mp3"

                            RL "Svetlana! That must be her!"

                            SH "Rose—"

                            RL "We should go! And let her in!"
                        
                        else:

                            show zzrl hesitant

                            RL "No, no that's not what I meant. It's just that, er..."

                            show zzsh hesitant

                            SH "Rose, you...you're the only person I've told about Ilya who's been happy for me right from the start. Even my parents weren't...it took them a while to come around to him, you know? And Hayden—"

                            show zzrl hesitant

                            RL "It's not that I—"

                            $ random = 1                     

    if random == 1:
        ##play audio
        "knockloud2.mp3"

        RL "Oh! That must be Svetlana!"

        SH "Rose—"

        RL "We should go! And let her in!"

        jump svet_entrance
    
    else:
        ##play audio
        "knockloud2.mp3"

        SH "Oh! That must be Svetlana."

        jump svet_entrance

label paptalk:
    $ pt += "papped, "

    ##play audio
    "rosephone.mp3"

    show zzrl resigned

    RL "Oh, sorry, it's my agent, let me just get this real quick."

    scene bg backporch ## or some kind of phone bg??

    show zzrl flat 
    with fade

    if papcount == 0:
        Meg "Rose. Why is the internet telling me that you're at a secret rendezvous with Shane Hollander at his private lakeside mansion and that you guys are getting back together??"

        show zzrl surprised

        RL "What! I am not!"

        Meg "Oh good, so you're not in Shane Hollander's house? You're haven't seen him?"

        show zzrl resigned

        RL "...well. I am at Shane's cottage, and I have seen Shane. But platonically! As friends!"

        Meg "Yeeeeah. You still want us to firmly deny all rumours about you two, right? Cause I gotta say, it's not actually bad press—"
        
        show zzrl wince

        RL "Deny, please. Shane doesn't like them."

        Meg "Well, then we better figure out how to get you safely—and more importantly—{i}secretly{/i} evacced outta there."

        show zzrl resigned

        RL "Right, fine, yes, thank you. I drove up here from the airport in a rental, and I have a flight back to LA at—"

        Meg "Nope nope nope. Firstly, you're going nowhere else in that rental, it's been made."

        RL "Alright. I could...get Shane to drive me out in one of his—"

        scene cut boys_inside2 ## you could have a different cut scene for this
        with fade

        RL "..."
    
    else:
        Meg "Rose. Why is the internet telling me that you're at a secret rendezvous—"

        show zzrl resigned

        RL "—with Shane Hollander at his private lakeside mansion and we're getting back together, I know."
        
        Meg "You are?? What happened to deny, deny, deny??"

        RL "No, no, we're not getting back together, we're still just friends. I should have known better, I fucked up and got spotted in public—"

        scene cut boys_inside2 ## you could have a different cut scene for this see above
        with fade

        RL "..."

        RL "—and then spotted a fuck in private, which I should {i}also{/i} have known better about."

        Meg "What?"

    RL "Never mind. What if you arrange for someone to drive out to meet me, we could swap cars—"

    scene bg ctdoor

    show zzsh flat at center
    show zzir flat at midright
    show zzrl resigned
    with fade

    RL "Sorry I gotta cut and run like this guys."

    show zzsh hesitant

    SH "Hey, don't apologise, it's okay."

    show zzir smirk

    IR "Yes. Very, very okay."

    show zzsh wry

    SH "We'll see each other again...sometime..."

    show zzrl smile

    RL "When the hockey and film gods both smile upon us and our schedules align, I know."

    SH "I think if the hockey and film gods both smile upon us, our schedules will get worse, not better."

    IR "Yes, true. Wishing you great career success, Rose Landry. Goodbye."

    $ papcount += 1

    scene bg plane

    show zzrl flat
    with fade

    ## double check if you did anything with actual airportout

    RL "Well. I feel like I'm spending more time in the air than on the ground today...hopefully tomorrow will be better."

    $ loop += 1

    jump start_real

label svet_entrance:

    scene bg ctentrance

    show zzsh flat at midleft
    show zzir flat at center
    show zzrl flat
    with fade

    show zzsv flat at right
    with easeinright

    IR "(Ilya's podficcer get's to choose between 'Здравствуй, здравствуй, день ненастный! Скаких пор стучишься?' and 'Привет, с каких пор стучишься?')"

    SV "(Svetlana's podficcer get's to choose between 'Стучусь к приличным людям, не к тебе.' and 'Я Jane не знаю, чтобы просто так войти.')"

    show zzir frown

    IR "Sveta."

    show zzsh hesitant

    SH "Um, it's nice to meet you, Svetlana. Приятно...познакомиться...?"

    show zzsv surprised

    SV "Oh, my. Is Ilya teaching you how to be polite? I'm surprised he knows how."

    show zzsh embarrassed

    SH "I'm learning from Duolingo, actually."

    show zzsv amused

    SV "Tsk, Duolingo. Why talk to that cursed owl when you have your very own Russian tutor?"

    show zzir smirk

    IR "Because when I'm with him, usually his mouth is too busy to—"

    show zzsh annoyed_blush:
        ease 0.1 xoffset 100
        ease 0.1 xoffset 0
    with hpunch ## possibly hpunch is too much we shall see

    SH "Shut it, Rozanov."

    show zzsv smile

    SV "Well, Взаимно, {i}Jane{/i}. I've wanted to meet you for the longest time."

    show zzrl hesitant

    RL "Jane...?"

    show zzsh embarrassed

    SH "Uh..."

    show zzsv flirty

    SV "Ah. Of course, it is nice to meet you too, Rose Landry, I've also wanted to meet you for the longest time."

    menu:
        "Nice to meet you too":

            RL "Oh, just Rose, please. And it's a pleasure to meet you, Svetlana"

            SV "Oh, the pleasure is all mine, Rose."

            show zzir eyeroll

            IR "...Okay. Boring introductions done now. Time to drink."

        "приятно познакомиться":

            if russian >= 1:
                $ russianpass = True
                $ yayrussian = True

                RL "приятно познакомиться, Svetlana."

                $ svetheart += 2
                show sv_heart at right, blip

                show zzsv surprised

                SV "Взаимно, Rose Landry. I did not expect you to also be learning Russian."

                show zzsh frown

                SH "Yeah, Rose, since when do you speak Russian?"

                show zzrl smile

                RL "Since, oh, today. And it's just Rose, please."

                show zzsv flirty

                SV "Well, Rose, you have a very clever tongue. And I'm flattered you learned a little Russian just for...today."

                show zzir eyeroll

                IR "Yes, very clever, now you can have great conversation with Russian babies. Oops, sorry, no Russian babies here today."

                show zzrl grin

                RL "No Russian babies, only Russian babes, am I right?" ## if you know what i mean?? this the running joke but maybe not obvious enough

                show zzsv amused

                SV "Right."

                IR "Wrong. Enough, I need a drink."
            
            else:
                RL "Прия́тно—um, по..."

                $ svetheart += 1
                show sv_heart at right, blip

                show zzir eyeroll

                IR "And I thought Shane was bad. You do not have the mouth for Russian, Rose Landry."

                show zzsv flirty

                SV "Though if you want a mouth for Russian, I'm happy to be of service. I promise I'm a better teacher than Duolingo."

                show zzrl surprised_blush

                RL "Oh, haha, thanks. And, um, please just call me Rose."

                show zzir eyeroll

                IR "Okay, okay, enough with the boring introductions. Time to drink."
                
        "Still nice to meet you" if loop >= 2:

            RL "Yup, really nice to meet you again, Svetlana."

            show zzsv eyebrow

            SV "Oh? Have we met before? I can't imagine I would forget that."

            show zzrl wince

            RL "Haha, oh, I mean, clearly we've never met before, but I just feel like I already know you! Somehow!"

            show zzsv amused

            SV "Is that so?"

            show zzir eyeroll

            IR "Okay, enough with the bad flirting. I need a drink."
        
        ## "TBD even more deranged convo unlock" if loop >= 4:

    IR "Sveta, you brought настойки, yes?"

    SV "It's in the car, with all my bags."
    
    IR "...all your bags. How many bags is 'all'? You know you're staying only one night, you're leaving tomorrow."

    SV "I barely got here and you're already telling me to leave? Fine, maybe I'll bring my good vodka home with me."
    
    SV "And also all the frozen pelmeni from Evgenia Mikhailovna, which she made me bring up in a cooler all the way from Boston for her dear Ilyushenka, who—"

    show zzsh frown

    SH "Wait, who is this? Who is sending Ilya pelmeni?"

    show zzir frown

    IR "Okay, shut up, I will go get all your bags now. It can be my training for today."

    show zzsh eyeroll

    SH "Unless each of her bags is 300lbs, it's {i}not{/i} going to count as your training for today." ## check canadian units, and also check...athlete physiology

    show zzir flat

    IR "Yes, exactly."

    show zzsh eyeroll

    SH "Her bags are not 300lbs each, Rozanov."

    show zzir smirk

    IR "Oh, so you know how heavy Sveta's bags are? You have magic psychic powers now?"

    show zzsh smirk

    SH "I don't need psychic powers to know that her bags are—"
    
    IR "You think her bags are so light, why don't we see how many reps you can bench press them—"

    SH "At least one more rep than you, asshole, that's how many reps—"

    hide zzir
    hide zzsh
    with easeoutleft

    show zzsv unimpressed at center
    with ease

    SV "..."
    
    SV "...if they break something trying to bench press my bags, I will break both their heads."

    if loop == 0:

        show zzrl smile

        RL "Haha, they remind me of puppies."

        show zzsv amused

        SV "Puppies, yes, constantly snapping at each other's heels and in desperate need of house training."

        show zzrl grin
        
        RL "Exactly! Snapping at each other's heels, sniffing at each other's butts..." ## ehhhh not sure about this line

        show zzsv amused

        SV "Hah! Well then, while those two young pups play with each other outside, what should us two old bitches do in here?" ## ehhhh not sure about this line too
    
    else:

        if loop == 1:
            show zzrl hesitant

            RL "I...I don't think they'll break anything, but something tells me they might not actually remember to bring your bags in."

        else:
            show zzrl resigned

            RL "They won't break anything in your bags. They'll barely remember your bags at all."

        show zzsv amused

        SV "Yes, they terrible about distracting each other. Yapping at each other like puppies."

        show zzrl grin

        RL "Yes! That's what I said!"

        if loop == 1:
            show zzrl hesitant

            RL "Or...I mean...I thought I said...?"
        
        elif loop == 2:
            show zzrl wince

            RL "To them, I mean. Not to you, obviously, because we've obviously never spoken before."
        
        else:
            pass

        SV "Well, you can say it again. Now, while they're out playing in the yard, what should we do in here?"

    menu:
        "Offer to show Svetlana around":

            show zzrl smile_blush

            RL "Oh, maybe I could show you around the cottage...?"

            RL "Since you're staying the night, I could show you some of the guest rooms?"

            show zzsv flirty
            $ svetheart += 1
            show sv_heart at center, blip

            SV "Mm, yes, you're welcome to show me to any room in this house, Rose, any room at all."

            jump housetour2

        "Offer to let Svetlana relax alone":
            jump chillalone
        
        "Take a nap" if loop >= 3:
            show zzrl hesitant

            RL "Actually, I might just take a nap instead."

            show zzsv smile

            SV "Sensible. I might do the same."

            scene black
            with fade

            $ loop += 1

            jump start_real

label chillalone:

    RL "Oh, did you drive up all the way from Boston? You must be so tired! If you want to rest and recharge by yourself...?"

    show zzsv smile

    SV "Ah, yes. That's very thoughtful of you, perhaps I'll find a room to take a nap in. See you at dinner, Rose."

    hide zzsv with easeoutright

    ## code in loop 0-1

    if aloneloop == 0:
        $ aloneloop += 1

        scene bg sunroom

        show zzrl resigned
        with fade

        RL "I guess I should kill some time checking my email. And reading the script that Megan thinks I should audition for. Oh, shit, and there's the Bulgari contract I was supposed to look through too."

        RL "...or maybe I'll just play some Food Truck Kitty."
    
    elif aloneloop == 1:
        $ aloneloop += 1
        scene bg sunroom

        show zzrl resigned
        with fade

        RL "I guess I should kill some time checking my email—wait, what if all this has been the universe's way of telling me to work harder?"

        show zzrl hesitant

        RL "I mean, surely not. I haven't procrastinated so hard that I broke the space-time continuum...have I??"
    
    else:
        $ aloneloop += 1
        scene bg sunroom

        show zzrl resigned
        with fade

        RL "...right, what now?" ## come back to this

    menu: ## maybe cut some of these if no one ever gets here
        "Do work":
            $ pt += "work alone, "
            if clearemail == 0:

                RL "I should probably try to be responsible."

                scene cut work
                with fade

                RL "...no, I'm not showing my bare ass on screen for a Victoria's Secret ad. Isn't the whole point of Victoria's Secret to cover up my ass?"

                scene bg sunroom
                show zzrl resigned
                with fade
                
                RL "Ugh, my eyes are crossing, how long have I been—"

                scene cut boys_outside4
                with fade

                RL "...Now there's an ass that needs covering up."

            elif clearemail == 1:
                RL "I did tell Megan that I'd let her know about the script by tomorrow. And I've always suspected she's got evil superpowers..."

                scene cut work
                with fade

                RL "Why am I getting kidnapped in this one too?? Megan, I said no more kidnapping scripts!"

                scene bg sunroom
                show zzrl resigned
                with fade

                RL "And done. Megan, are you happy now—"

                scene cut boys_outside4
                with fade

                RL "...if you're watching this, Megan, you close your third eye right now. Don't perv on my friends."

            else:
                RL "Guess it's good to be caught up once I break out of this time loop."

                scene cut work
                with fade

                RL "...at least I don't have to reply to emails today, since that would be pointless. Not that it's not pointless most other days too..."

                scene bg sunroom
                show zzrl resigned
                with fade

                RL "Wow, okay, my eyes are crossing, I need to—"

                scene cut boys_outside4
                with fade

                RL "...I need to learn to keep my eyes closed, clearly."

            $ clearemail += 1

        "Play Food Truck Kitty":
            $ pt += "kitty, "
            if foodtruckkitty == 0:
                scene cut game
                with fade

                RL "...noooo, why won't Dragon Tabby triple-heart my Sunday Special? I know it likes lettuce and salmon!"

                scene bg sunroom
                show zzrl resigned
                with fade

                RL "Ugh, maybe I should stop playing, how long have I been—"

                scene cut boys_outside4
                with fade

                RL "Whoa! Right in front of Dragon Tabby's salad?"
            
            elif foodtruckkitty == 1:
                scene cut game
                with fade

                RL "Curse you, RNGesus, why won't you let Dragon Tabby like me?"

                scene bg sunroom
                show zzrl resigned
                with fade

                RL "...so no matter what I do, there's some things I can't change. Is that the lesson I'm supposed to learn here, universe—"

                scene cut boys_outside4
                with fade

                RL "...fine. Consider this lesson learnt."
            
            else:
                scene cut game
                with fade

                RL "Here, kitty kitty kitty..."

                scene bg sunroom
                show zzrl smile
                with fade

                RL "You know what, kudos to whoever made this game. It's still really fun even though I've played this so many times—"

                scene cut boys_outside4
                with fade
            
                RL "...aaaaaand {i}this{/i} part's still fun too."
            
            $ foodtruckkitty += 1

    RL "..."

    RL "Okay, they're still going. Maybe it's time to go find Svetlana, it's gotta be almost dinner time."

    jump dinner

label housetour2: ## flirty loop 1 and write new rose loop 2+ where she is less surprised
    $ pt += "sveta tour, "

    scene bg room2

    show zzsv flat at center
    show zzrl flat
    with fade
   
    SV "Hmm, what's this room?"

    if outside >=3:
        menu:
            "Close the blinds?"

            "yes":
                if room2blind == True:
                    jump blindsclose

                else:
                    SV "...what are you doing?"

                    RL "Just looking for...nothing! Never mind!"

                    SV "...okay. So...would you like to tell me about this room?"
            
            "no":
                pass

    RL "It's one of the three guest rooms here. I think Shane said they all have an en-suite and a king bed."

    SV "A king? Hmm. Certainly this bed could fit two people, if it was you and me, but..."

    show zzrl surprised_blush

    RL "Oh! You and me, huh?"

    show zzsv amused

    SV "What I mean is, if it was two regular sized women like us instead of, say, two massive hockey players, we could fit comfortably in this bed. But I don't think that makes it a king."

    SV "Though perhaps if it {i}was{/i} you and me, we could fit comfortably in an even smaller bed than this."

    show zzrl smile_blush

    RL "Right, haha, maybe! Good thing this is just the guest room then, and not Shane and Ilya's room!"

    show zzsv smile

    SV "Yes, good for them. Now, where is this en-suite...?"

    if shane_room2 == True:

        $ svet_room2 = True

        RL "The en-suite—oh, that's right, this room has a hidden door right...here! Voila!"

        ##play sound
        "lightswitch.mp3"

        show zzsv amused

        SV "Magic! Will you pull a rabbit out of a hat next?"

        show zzrl grin_blush

        RL "No hat, but I could pull a rabbit out of my suitcase. If you know what I mean." ## cut the if you know what I mean...? or use it more to make it a rose thing

        show zzsv flirty
        $ svetheart += 1
        show sv_heart at center, blip

        SV "Hah! Now that's a trick I'd love to see."

        RL "Too bad I've left my magic wand at home. Conjuring up this bathroom is the only trick I've got."

        show zzsv eyebrow

        SV "Hmm, better try again, because I'm not sure I approve of this bathroom. Brick flooring and stone bath mats, really?"

        show zzrl smile

        RL "Gives you cold feet just looking at it, right? Don't worry, for my next trick, I'm going to heat up the floor with just a wave of my hand!"

        ##play sound
        "lightswitch.mp3"

        RL "Voila!"

        show zzsv amused

        SV "My goodness, you're even more magical than I thought."

        show zzrl smile_blush

        RL "Haha, um, if you've enjoyed our service, please leave a good review at the end of your trip, Ma'am."

        show zzrl grin_blush
        
        RL "Anyway, let me magic you away to the next room!"
    
    else:
        show zzrl surprised

        RL "Oh, huh! You're right, there doesn't seem to be one...?"

        show zzsv amused

        SV "Ah, no king bed, and no en-suite. How disappointing, this hotel room does not have all the listed amenities, I shall have to leave a bad review."

        show zzrl grin

        RL "Our sincerest apologies, Ma'am, I will definitely be highlighting your concerns to management. Perhaps I could show you to a different room instead?"

    menu:
        "Show Svetlana the east-facing guest room":
            scene bg room1

            show zzsv eyebrow at center
            show zzrl smile
            with fade

            SV "This room is...well."

            if outside >=3:
                menu:
                    "Close the blinds?"

                    "yes":
                        if room1blind == True:
                            jump blindsclose

                        else:
                            SV "...what are you doing?"

                            RL "Just looking for...nothing! Never mind!"

                            SV "...okay. So...would you like to tell me about this room?"
                    
                    "no":
                        pass

            if shane_room1 == True:

                $ svet_room1 = True

                RL "Now, this room is decorated in the post-modern style, which we hope will be more to your taste, Ma'am, so please enjoy your stay."

                show zzsv amused

                SV "Really. This is the room you think will be more to my taste."

                show zzrl smile

                RL "Haha, I mean...not really. You don't look like a post-modern kinda person."

                SV "No?"

                show zzrl thoughtful

                RL "Well, your style seems more elegant and understated? Shimmery metallics and classic cuts instead of bright pops of colour. Not that fashion style necessarily reflects interior decor preferences, but..." ## i know nothing about clothes and even more nothing about art, help

                $ svetheart += 1
                show sv_heart at center, blip

                SV "Mm. You've been paying attention to me."

                show zzrl hesitant_blush

                RL "Oh, well, sorta...? Mostly I was paying attention to Ilya, but I couldn't help noticing you."

                show zzsv eyebrow
                
                SV "To Ilya?"

                show zzrl thoughtful
                
                RL "It's just...when Shane told me he was dating Ilya, I looked him up—I mean, obviously I already knew who Ilya was, anyone who follows hockey does, but I wasn't really paying attention the same way, y'know?"

                show zzsv eyebrow

                SV "And what way is that?"

                RL "In a...a concerned best friend kind of way, I guess."

                show zzsv thoughtful

                SV "Ah, I know what you mean. I was the same."

                show zzrl surprised

                RL "You were the same? As in, you looked up Shane? But he's...I mean, Ilya's reputation is more..."

                show zzsv eyebrow

                SV "Terrible?"

                show zzrl wince_blush

                RL "That's not—I mean, not that I think any of it is true, God knows the media loves to sensationalise, and considering what Ilya's done for Shane, he's obviously, um..."

                show zzsv flat

                SV "Domesticated?"

                show zzrl hesitant_blush

                RL "Devoted. I was going to say, he seems devoted to Shane."

                SV "Yes, devoted to Shane Hollander, who the media likes to say is devoted to hockey more than anything else. Who only understands hockey and nothing else."

                show zzrl wince

                RL "Ah, yeah, I can see why a best friend might be concerned."

                show zzrl hesitant
                
                RL "But look, Shane's not actually a hockey robot, whatever the press likes to say. Sure, he loves hockey, but he loves Ilya too, and I'd swear his love for Ilya is the real thing." ## come back to this
                
                show zzsv flat

                SV "And if he had to choose?"
                
                RL "But why should he have to choose? People are allowed to love more than one thing in their life, right?"

                show zzsv unimpressed

                SV "Mm, that's a very pretty view of life. But Ilya did have to choose, and he chose Shane, he chose Ottawa. Would Shane do the same?"

                RL "...I...I guess I don't.."

                SV "Never mind, enough about them. Let's talk about something else before we fail the Bechdel test." ## THIS IS A PLACEHOLDER

                show zzrl hesitant

                RL "Oh, um, right! Er, speaking of pretty views, get a load of the view from this room! As you can see, the—"
            
            else:
                RL "And this room is also a guest room, I think, and is...uh.."

                show zzrl surprised

                RL "Wow."

                show zzsv eyebrow

                SV "There are a lot of...post-modern sculptural pieces?...on the walls."

                RL "{size=-8}Shane, why?"

                show zzrl hesitant

                RL "Well! Good thing this room has more windows than walls! Lots of natural light, and a gorgeous view of—"

            scene cut boys_outside1
            with fade

        "Show Svetlana the guest room downstairs": 
            scene bg room3

            show zzsv smile at center
            show zzrl smile
            with fade

            SV "Ah, a more normal room."

            if outside >=3:
                menu:
                    "Close the blinds?"

                    "yes":
                        if room3blind == True:
                            jump blindsclose

                        else:
                            SV "...what are you doing?"

                            RL "Just looking for...nothing! Never mind!"

                            SV "...okay. So...would you like to tell me about this room?"
                    
                    "no":
                        pass

            if shane_room3 == True:

                $ svet_room3 = True

                RL "Now, Ma'am, this is our biggest, fanciest room. I hope it will be to your liking!"

                show zzsv amused

                $ svetheart += 1
                show sv_heart at center, blip

                SV "The biggest, fanciest room, all for me?"

                RL "Only the best for our most valued customers! It comes with a spacious bathroom for two, and even has two walk-in closets!"

                SV "Why does any guest room need one walk-in closet, let alone two? How long does Shane think his guests are staying for?"

                RL "He built this room for his parents, apparently. Even though they have their own cottage ten minutes away."

                SV "My, what a thoughtful son. And how much clothing does he think his parents—"

                SV "..."

                SV "Are these Ilya's trophies in Shane's guest room closet?"

                RL "Oh, yeah, apparently Ilya's house in Ottawa's doesn't have space for all of them...?"

                show zzsv unimpressed

                SV "...No, it doesn't. Because Ilya did not get a place he truly means to stay for good. So instead he puts all his trophies aside, stashes them in a spare room in Shane's spare house."

                show zzrl hesitant

                RL "Oh, that's...I mean, Shane says this is temporary...? They're planning to renovate this place to build a proper trophy room for the both of them here...?"

                SV "Is that so."

                show zzsv flat

                SV "Ah, it is what it is. Tell me more about this big, fancy room, Rose."

                RL "Oh, uh, yes Ma'am. It also has lots of natural light, and a gorgeous view of—"
            
            else:

                RL "Well, Ma'am, this room is bigger and cosier! We hope this will be more to your liking!"

                RL "It gets lots of natural light, and has a gorgeous view of—"
            
            scene cut boys_outside3
            with fade

    RL "Oh!"

    SV "Mm, yes, I suppose that is quite a view."

    RL "Maybe we should...head back to the dining room. It must be time for dinner soon."

    SV "Yes. The boys sure look hungry."

    $ svet_tour += 1

    jump dinner

label blindsclose:

    $ freedom += 1
    $ blindsnow = True
    $ svetheart += 2 ## no heart blip because cutscene but i will add heart blip if players are confused 

    show zzsv eyebrow

    SV "...why are you suddenly closing the blinds?"

    RL "Just in case! There!"

    scene cut girls_blinds
    with fade

    SV "In case of..."
    
    if blindspass == 0:
        $ blindspass += 1

        RL "In case...it gets too warm! So much sunlight, all these windows, there's, um, a greenhouse effect, right? Wouldn't want the room to be too hot when you're in bed later!"

        SV "...yes, I was also thinking about being in bed. And how hot it could be."

        RL "Oh, haha, right! Except, um, I guess now I've closed the blinds now, so—"

        SV "So now we're in a darkened room all alone. Mm, how should we entertain ourselves until dinner?"

        RL "With...scintillating conversation...?"

        SV "Ah, certainly. I was just thinking of a particularly gorgeous and intruiging...topic of conversation."

        RL "Oh, er, and that's..."

        SV "Your recent Met Gala outfit, of course. What a bold and slightly terrifying interpretation of the theme."

        RL "Oh, hah...um, thanks! I figured a Weeping Angel is still kind of an angel, and I'm already used to being covered in body paint for X-Squad stuff, so..."
    
    else:
        $ blindspass += 1

        RL "In case the surrounds gets too hot. Happens a lot in these parts. And actually, we should stay here for a bit before going down to dinner. With the blinds down."

        SV "...alright. And what should we do while we wait?"

        RL "We could chat...or...."

        SV "Mm, are you suggesting we get up close and personal?"

        RL "Well, we are in a darkened room all alone, so..."

        SV "So, time for a little...private conversation, perhaps?"

        SV "Tell me a secret, Rose. Was it really your idea to go as a Weeping Angel to the Met Gala?"

        RL "...oh, that. Hah, yeah, that was entirely my decision. Didn't think a Met Gala outfit would be so controversial. I mean, angels are celestial beings, right? So I figured it was still on theme..."

    jump dinner

label dinner:

    scene bg dining

    show zzsv amused at center
    show zzrl smile
    with fade

    if blindsnow == True:

        SV "...always so boring and safe. Are stars the only celestial object? Do we really need fifty slightly different sparkly dresses at the Met Gala?"

        RL "Right? Like what about having an outfit inspired by a black hole? A red giant? A—"

    elif freedom == 0:
        RL "...and that was the second time I caught them making out today."

        SV "Mm, from the way Ilya talks, twice is a remarkable show of restraint. They—"
    
    elif freedom == 1:
        RL "...and miraculously, i've only caught them making out once today!"
        
        SV "Only once, in this exhibitionist house, with those exhibitionist boys? That truly is miraculous—"
    
    else:
        RL "...and would you believe I haven't seen Shane or Ilya's naked butt even once today?"

        SV "Oh? Were you expecting to?"

        show zzrl hesitant_blush

        RL "Haha, I mean—"

    show zzsh smile at center
    show zzir smirk at midright
    with easeinright
    show zzsv at midleft
    with ease

    IR "We're back. Did you miss me?" ## come back to this

    show zzsv flat

    SV "Barely noticed you were gone. Where are my bags?"

    show zzsh frown_blush

    SH "Oh, fuck, your bags—sorry, I think we left them next to the car...?"

    if loop <= 1:

        show zzrl grin

        RL "Shane, oh my god, that's literally why you and Ilya went outside! You guys seriously spent the whole time making out?"
    
    else:
        show zzrl grin

        RL "Yeah, you did. While you made out the whole time instead." ## is this superfluous?

    show zzsh embarrassed

    SH "No, what—we—why would you say that we were—"

    IR "Yes, the whole time. I am just too irresistable to Shane, he—"

    show zzsh annoyed_blush:
        ease 0.1 xoffset 100
        ease 0.1 xoffset 0
    with hpunch

    SH "Shut up, Rozanov."

    show zzsv amused

    SV "Yes, shut up, Rozanov. You realise that means you left настойки and pelmeni outside."

    show zzir frown

    IR "Ah, fuck, настойки—"

    SV "I suppose we'll just have to break into your stash here."

    IR "I don't have a stash here, Sveta, that is why I asked you to bring thirty bottles." ## check units? is this a reasonable too many or too few?

    show zzsh frown

    SH "{i}Thirty bottles?{/i} Ilya, did you think we'd be drinking two bottles of vodka a day??"

    show zzir eyeroll

    IR "No, no, some bottles are for your papa. Some are for here. And the rest are for me to bring back."

    show zzsv eyebrow

    SV "So you still haven't found a source for good alcohol in Ottawa? I'm shocked. In Boston you had three."

    show zzir smirk

    IR "Ah, I've only been here for one year. For now, you will just have to keep smuggling the good stuff to me, Sveta. At least until I convince David to reveal {i}his{/i} sources."

    show zzsh annoyed

    SH "My dad? You're saying {i}my dad{/i} is smuggling vodka."

    IR "What, you think David is too good to smuggle vodka? He is not as boring as you think, котик, you are still the champion for most boring Hollander in the family." ## check russian nickname

    menu:
        "Defend Shane":
            show zzrl grin

            RL "Hey, I'm sure Shane could make a great smuggler too! You guys travel so much for games, it wouldn't be too difficult to sneak away to grab a bottle or two, right?"

            show zzir eyeroll

            IR "Oh, so you don't know Shane's pre-game routine? You think Shane is just sitting around in his hotel room doing nothing, twirling his thumb until he has to be on ice?"

            show zzsv unimpressed

            SV "Oh, it's just a joke, Ilya. Anyway, even if Shane did have free time pre-game, he wouldn't be a very reliable source, would he? You two barely even meet up once a month."

        "Defend Shane's dad":
            show zzrl smile

            RL "I'm sure David's getting his drinks from legitimate suppliers. Bet he's getting it from a local craft distillery and just doesn't want Ilya buying out their supplies from under his nose. That's why Miles is always hush-hush about {i}his{/i} sources."

            show zzir annoyed

            IR "Oh, so you think I would buy out David's favourite vodka from under him? What, because I'm best at stealing the puck away from under one Hollander's nose, I will do the same with vodka for another Hollander?"

            show zzsv flat

            SV "Oh, it's clearly a joke, Ilya. After all, if there {i}were{/i} any good craft distilleries, you'd already have sniffed them out like you did in Boston."

        "Say nothing" if loop >=2:
            show zzsv flat

            SV "Well, if you like boring, then you must be enjoying Ottawa so much more than Boston. No?"

    show zzir frown

    IR "Sveta."

    SV "You've at least found a good source for pelmeni, yes? I can go back and reassure Evgenia Mikhailovna that her dearest Ilyushenka is not going to starve to death in a ditch in Ottawa?"

    IR "..."

    show zzsv unimpressed

    SV "No? You draw little Russian grandmothers to you like you draw penalties from insecure D-men. It's been a whole year in Ottawa, and you still haven't charmed a nice old lady into feeding you?" ## check hockey? draw...aggressive D-men?

    show zzir annoyed

    IR "Okay, what is your problem."

    show zzsv flat

    SV "I don't have one. {i}I{/i} still get pelmeni from Evgenia Mikhailovna every month, and you know her cooking cures all ills and fixes all problems."

    if loop >= 1:
        menu:
            "Say nothing":
                IR "David and Yuna Hollander are feeding me, Sveta. You can see I have not starved."

                SV "Oh, you have charmed them?"

                show zzir hesitant

                IR "I..." ## boastful but hesitant instead of hesitant

                show zzsh flat

                SH "Yes. My parents think Ilya's charming, they like him."

                show zzsh frown

                SH "But...I guess they can't make good pelmeni like a Russian grandmother, so...so I'll go get the pelmeni, okay?"

                SH "Sorry, it's on me for forgetting it earlier anyway—"

            "Distract everyone with pelmeni":
                show zzrl hesitant

                RL "Um, hey, you know what? Why don't I go get the pelmeni and vodka from the car?"

                show zzsh frown

                SH "No, I'll go get it. Sorry, it's on me for forgetting it earlier anyway—"

            ## "TBD distract everyone with hockey" if loop >= 3:

    else:
        show zzrl hesitant

        RL "Um, hey, you know what? Why don't I go get the pelmeni and vodka from the car?"

        show zzsh frown

        SH "No, I'll go get it. Sorry, it's on me for forgetting it earlier anyway—"

    show zzir annoyed

    IR "You forget because you were on {i}me{/i}, nothing to be sorry for. {i}I{/i} will go get the vodka and pelmeni, since Sveta has so much to say about it."

    hide zzir with easeoutright

    SH "..."

    RL "Um..."

    show zzsh hesitant
    
    SH "Actually, I think I'll go help Ilya with the bags."

    hide zzsh with easeoutright

    show zzsv flat at center
    with ease

    SV "I wonder how long they'll take with my bags this time."

    RL "Svetlana..."

    SV "I think I'll go outside for a bit as well, get some air. Turns out I'm not so hungry after all."

    if loop >= 2:
        menu:
            "Join her outside":
                pass

            "Stay indoors": 
                jump indoors
            
            "Take a nap" if loop >= 3:
                show zzrl hesitant

                RL "Actually, I might just take a nap instead."

                show zzsv flat

                SV "Yes, this has been rather tiring conversation, hasn't it."

                scene black
                with fade

                $ loop += 1

                jump start_real

    $ pt += "go out, "

    RL "Oh, I'll come with you? I'm not that hungry either."

    show zzsv smile
    $ svetheart += 1
    show sv_heart at center, blip

    SV "If you like. I wouldn't mind the company."

    jump outside

label indoors:
    $ pt += "stay in, "

    RL "Oh, right. I'll come get you when Shane and Ilya get back...?"

    show zzsv smile

    SV "Thank you."

    hide zzsv with easeoutleft

    show zzrl flat

    RL "Right."

    RL "..."

    RL "...gotta say it feels kind of weird to just sit here by myself..."

    if inside >= 2:
        RL "Gonna stay right here this time. And do...something."
    
    else:
        RL "Maybe I should see if the boys want my help with Svetlana's bags..."

        scene bg hallway

        show zzrl flat
        with fade

        if inside == 0:
            RL "...not that Ilya is gonna want my help for anything ever—"

            scene cut boys_frontdoor1
            with fade

            RL "..."

            RL "{size=-8}Nope, they're {i}really{/i} not gonna want my help for that..."
        
        else:
            RL "...no, wait, the last time, didn't they—"

            scene cut boys_frontdoor1
            with fade

            RL "..."

            RL "{size=-8}Yup, they forgot about Svetlana's bags again, didn't they..."

        scene bg dining

        show zzrl flat
        with fade

        show zzrl resigned_blush

        RL "Never mind, maybe I'll just stay here and do...something else. Anything else."
    
    menu:
        "Read your emails":
            $ random = 12
        
        "Eat some chocolates" if giftbought == "choc":
            $ random = 13
        
        "Play Food Truck Kitty":
            $ random = 14

    show zzrl thoughtful

    RL "Actually, since I might have to do this day all over again..."

    if random == 12:
        scene cut work
        with fade

        RL "...and fuck you for saying I need to lose ten pounds to be hot enough to wear spandex on screen. Best Regards, Rose—"

        $ clearemail2 += 1

    elif random == 13:
        RL "I did buy this box of fifty chocolates."

        RL "...the question is do I eat like there's no tomorrow, or eat like there's a slim chance of tomorrow..."

        scene bg dining

        show zzrl grin
        with fade

        RL "...oh my God, this is so good, I wonder if going into a diabetic coma will restart this loop--"
    
    else:
        scene cut game
        with fade

        RL "...five thousand dollars worth of pulls and I {i}still{/i} can't get Dragon Tabby?? Man, even imaginary cats are cruel and capricious—"

        $ foodtruckkitty2 += 1

    SV "Ahem."

    if random == 13:
        pass

    else:
        scene bg dining

        show zzrl flat
        with fade

    show zzsv flat at center
    with easeinleft

    if inside >= 2:
        RL "Oh, you're back!"

        show zzsv unimpressed

        SV "Yes, but the boys aren't, I see. What are they doing with my bags? They better not actually be benchpressing them."

        RL "Yeah, I kinda doubt--"

        show zzsv amused

        SV "Ah, if you want something done right, get someone other than Ilya to help. Come with me, will you? I brought a bit more than I can carry by myself."

        show zzrl resigned

        RL "...oh, of course."

        scene cut boys_frontdoor2
        with fade

        SV "..."

        RL "{size=-8}Maybe let's go out the back and circle around to your car instead."
    
    else:
        RL "Oh, you're back! With your bags...?"

        SV "A few of them, yes. I had a suspicion that the boys would get distracted again, so I went around to the car to check. And I was right."

        RL "Yup, I'm so not surprised. Oh, hey, do you want some help getting the rest of your bags inside?"

        SV "Yes, thank you."

    scene bg dining

    show zzsv smile at center
    show zzrl smile
    with fade

    SV "...a very reasonable amount to pack for three days, if you ask me--"

    $ inside += 1

    jump leaving

label outside: ## these scenes are so long oh man are they too long??

    scene bg backporch

    show zzsv flat at center
    show zzrl flat
    with fade

    if outside == 0:
        $ outside += 1

        RL "So..."

        SV "Mm?"

        show zzrl hesitant

        RL "You can totally tell me to mind my own business, but what just happened in there...?"

        show zzsv eyebrow

        SV "Hmm. And if I did tell you to mind your own business?"

        show zzrl smile

        RL "I'd say, isn't it a lovely night to take a nice long walk outside? The air is so refreshing, don't you think?"

        show zzsv amused

        SV "Lovely and refreshing, yes."

        show zzsv thoughtful

        SV "You won't ask if I'm upset with Ilya? Not even a little curious?"

        show zzrl hesitant

        RL "I mean, I am, but..."

        RL "Shane says you and Ilya are really close, right? Like childhood best friends? And hey, it's totally normal to think your best friend's boyfriend isn't good enough for him, right?"

        show zzsv eyebrow 

        SV "You think I think Shane's not good enough for Ilya?"

        show zzrl resigned

        RL "I...I don't know? I mean, I don't know you or Ilya, not really. And I don't even know Shane as well as you know Ilya. So if you did think he's not good enough, I guess I couldn't really say you're wrong...?"

        RL "I mean, I think Shane's great! But you probably think Ilya's great too. So, I mean, maybe you know something I don't about why they might not be good together..."

        show zzsv surprised
        
        SV "Hmm."

        show zzsv amused

        SV "You really are lovely and refreshing, Rose."

        show zzrl surprised_blush

        RL "Oh! Haha, um, I don't really—"

        show zzsv thoughtful

        SV "As to your question. They seem good together, when they {i}are{/i} together."
        
        SV "But for most of the year, they're not."

        show zzrl wince

        RL "Ah, yeah. That's true. Long distance relationships can be really hard."

        show zzsv unimpressed

        SV "Yes. But who has been having it harder? Who has moved to a new city, is having a terrible time on his new team, now hides away all summer with no one else in {i}this house{/i} in—"

        scene cut boys_inside
        with fade

        SV "..."

        RL "What—whoa! Oookay, turning back around now."

        scene bg backporch

        show zzsv unimpressed at center
        show zzrl hesitant_blush
        with fade

        SV "...they do look good together when they are together, I suppose."

        RL "Haha, and they do seem to be enjoying being in the middle of nowhere with no one else around...?"

        show zzsv eyebrow

        SV "Oh, you think we're no one to them?"

        RL "Um..."

        show zzsv smile

        SV "I'm joking. Ah, I bet they've forgotten my bags {i}again{/i}."

        show zzrl smile

        RL "Let's just go get your bags ourselves."

        show zzsv flat

        SV "Yes. And enough talking about these dumb hockey boys, they're grown men who can do whatever they want. Evidently."

        show zzrl grin

        RL "I can talk about other dumb hockey boys instead, if you like? Because you know who's {i}not{/i} having a terrible time on his new team? Wyatt Hayes."

        show zzsv surprised

        SV "Hah, yes! He's having a surprisingly good year, isn't he? I didn't realise you followed hockey—"

        jump preleaving
    
    elif outside == 1:
        $ outside += 1

        RL "..."

        SV "..."

        RL "..."

        show zzsv eyebrow

        SV "You seem thoughtful. Dare I ask what you're thinking of?"

        show zzrl hesitant

        RL "Sorry, yeah, it's just...what happened inside..."

        show zzsv flat

        SV "Ah. You want to ask me if I'm upset with Ilya. Or if Ilya's upset with me."

        show zzrl thoughtful

        RL "No, that's not really..."

        show zzrl hesitant

        RL "It just feels like...okay, you can totally tell me to mind my own business if I'm off-base, alright?"

        RL "But if I were to ask you what you think about Shane and Ilya, would you say something like...like they seem good together when they are together. But for most of the year, they're {i}not{/i} together...?"

        show zzsv surprised

        SV "Perhaps."

        RL "And...and if I said, I agree, long-distance relationships are hard, you'd say, who is having a harder time of this long-distance relationship?"

        RL "Because you think Ilya has it harder, right? And I mean, you have good reason to think so."

        show zzsv thoughtful

        SV "Hmm. You are an extraordinarily perceptive woman, Rose. Or Ilya is telling Shane far more than I thought he was."

        show zzrl smile_blush

        RL "Oh, no, I'm really not! And Ilya's probably not."

        show zzrl resigned

        RL "Or, if he is, Shane hasn't told me..."

        show zzsv flat

        SV "Hmm, no need for false modesty, you were hardly off-base—"

        show zzrl surprised

        RL "No, no, that's not it, I'm not fishing for compliments or anything! It's more that..."

        show zzrl resigned

        RL "...oh man, I'm going to sound crazy, please don't think I'm crazy, but..."

        RL "I swear I've dreamed of this whole day before."

        show zzsv surprised

        SV "You've dreamed of this day."

        show zzrl wince

        RL "Not like that, I don't mean I was, like...like fantasizing of coming up here and meeting you and Shane and Ilya, that's really crazy talk."

        show zzsv amused

        SV "A little bit crazy, but maybe a little bit flattering too."

        show zzrl smile_blush

        RL "Oh, haha, I mean, I have really enjoyed meeting you! But I meant—"

        show zzsv thoughtful

        SV "You meant something like a premonition, yes? You are saying you knew what I would say even though I have not said it."

        show zzrl surprised

        RL "Yes! Exactly!"

        show zzrl thoughtful

        RL "And it's been happening all day! I mean, some things have been different, so maybe it's just...maybe it's just weird deja vu, my subconcious picking up on stuff, and I'm making too much out of it, but..."

        show zzsv eyebrow

        SV "But you don't think your subconscious is that extraordinarily perceptive either?"

        show zzrl hesitant

        RL "Well, I do think I'm fairly perceptive, but also...also, I feel like I can predict things that have nothing to do with being perceptive at all."
        
        RL "Like that if we look up at the cottage right now—"

        scene cut boys_inside
        with fade

        RL "—we'll see the boys making out."

        SV "...I have to say, it doesn't take much perception or premonition to predict that."

        RL "...okay, fair."

        scene bg backporch

        show zzsv thoughtful at center
        show zzrl resigned
        with fade

        RL "So...yeah. Sorry, you probably do think I'm crazy."

        SV "Hmm..."
        
        SV "No. No, I don't."

        SV "I don't believe in premonitions, but...I don't {i}not{/i} believe. You've behaved normally all day, so why should I assume you are crazy now because of some...uncannily accurate insights, if you will, into my thoughts on Shane and Ilya?"

        SV "Whether that is premonition or perception, we will have to see."

        SV "So tell me, Rose, what happens next?"

        show zzrl hesitant

        RL "Oh! Um, we...go round to the car to pick up your bags, and we...talk about hockey...?"

        show zzrl wince

        RL "I guess that's not much of a prediction either, but—"

        show zzsv amused

        SV "But it's something I don't think you're crazy to suggest, in any case. In fact, I would gladly test these potential powers of yours. Tell me, Rose, what do you think I think of...let's try Wyatt Hayes—"

        jump preleaving
    
    elif outside == 2:
        
        $ outside += 1

        RL "..."

        SV "..."

        RL "..."

        show zzsv eyebrow

        SV "You seem thoughtful. Dare I—"

        RL "{size=-8}'—ask what you're thinking of?'"
        
        SV "—ask what you're thinking of—oh."

        show zzsv surprised

        SV "Yes. That."

        show zzrl hesitant

        RL "Sorry. I didn't mean to, um—"

        show zzsv flirty

        SV "Read my mind? Careful, you might blush at some of the things I'm thinking about you."

        show zzrl wince_blush

        RL "Oh, haha, I mean, I can't read your mind, but..."

        show zzrl hesitant_blush
        
        RL "Okay, you didn't think I was crazy last time, so I'll just come out and say it. Either I've gained some sort of mutant powers of precognition, or I'm living through some kind of groundhog day, or...something, I don't know, but something strange is going on!"

        show zzsv surprised

        SV "...something...strange?"

        RL "The last time I remember being out here, talking to you, we talked about Shane and Ilya. And you said that they seem good together when they {i}are{/i} together, but they're {i}not{/i} together for a lot of the year."

        RL "And you said that the long distance relationship has been harder for Ilya than for Shane."

        show zzsv eyebrow

        SV "...I said that, did I?"

        RL "Oh, and also, last time, despite the fact that they said they were going out to get your bags, Shane and Ilya were fully making out instead. And as you can see—"

        scene cut boys_inside
        with fade

        RL "—they are."

        SV "...Indeed they are."

        RL "...yeah. I really need to ask Shane next time why there aren't any curtains in this house."

        scene bg backporch

        show zzsv flat at center
        show zzrl hesitant
        with fade

        RL "Anyway, I know it's not proof of...of anything. But I would swear this feels like the third time we're talking out here together, and it feels so real every single time even though it's impossible. And maybe I really am going crazy, but..."

        show zzsv thoughtful

        SV "You certainly haven't seemed crazy today. Even though all the things you mentioned, you could have potentially guessed."

        show zzrl resigned

        RL "I know. You've said that before. But I swear I'm not that good at guessing."

        SV "Hmm. So if you really want prove it to me, you will need to tell me things you cannot guess. Like a test."

        show zzrl hesitant

        RL "A test...?"

        SV "Yes. Let me think."

        SV "...and let's keep walking. The flashes of Shane's ass moving in the corner of my eye is not helping with my concentration."

        hide zzsv with easeoutleft

        scene bg outback

        show zzrl flat
        with fade

        show zzsv flat at center
        with easeinright

        SV "..."

        RL "{size=-8}...why is there a moose, Shane, why?"

        show zzsv amused

        SV "More than one mystery to be solved today, it seems."

        show zzsv thoughtful

        SV "Let's solve the more important one first. What if I ask you some questions you can't possibly know the answers to, unless you've done this before?"

        show zzrl hesitant

        RL "But we {i}haven't{/i} done this before. So there's no way for me to convince you, right...?"

        SV "Not this time, no. But I will tell you the answers, and you might be able to convince me next time, yes?"

        menu:
            "Do the test":
                show zzrl hesitant

                RL "I guess that's true. As long as you ask the same questions each time."

                RL "And as long as you promise not to think I'm crazy if I get everything wrong, and I break free of this loop tomorrow anyway."

                show zzsv flirty

                SV "If you get everything wrong and tomorrow happens anyway, this will be the most unforgettable conversation I've ever had with a beautiful woman I'm meeting for the first time. That's not so bad, is it?"

                show zzrl smile_blush

                RL "I...I guess not. We'll laugh about this in twenty years, or something?"

                show zzsv smile

                SV "Exactly."

                show zzsv thoughtful
                
                SV "Now, first question."

            "Try something else":
                
                show zzrl hesitant

                RL "You can't just...trust me...? You did, before, sorta."

                show zzsv eyebrow

                SV "Did I? What else did you say to convince me?"

                RL "Um...you asked me what we did after this, and I said we went to pick up your bags and talk hockey. And you asked me to predict your hockey opinions."

                show zzsv amused

                SV "We can do that. I should warn you that I have {i}many{/i} hockey opinions though, so you might not have an easy time convincing me that way."

                show zzrl grin

                RL "It might not be easy, but it {i}was{/i} fun! Okay, so, first, your thoughts on Wyatt Hayes—"

                jump preleaving

        jump outside_test

    else:
        $ outside += 1

        RL "..."

        SV "..."

        RL "..."

        show zzsv eyebrow

        SV "You seem thoughtful. Dare I ask what you're thinking of?"

        menu:
            "Shane and Ilya":
                show zzrl hesitant

                RL "About what happened inside..."

                show zzsv flat

                SV "Mm. What do you think happened inside?"

                RL "You seemed worried about Ilya...?"

                SV "Worried? He is rich and successful and in a relationship with Shane Hollander, player with the softest hands in the MLH and also in bed. They are disgustingly in love."

                scene cut boys_inside
                with fade

                SV "See? So in love, so disgusting. Can't keep their hands off each other for even two minutes."

                SV "What is there to worry about?"

                scene bg backporch
                show zzsv flat at center
                show zzrl hesitant
                with fade

                RL "They look really in love, yeah, but you told me—I mean, it seems like maybe...maybe they're good together when they {i}are{/i} together, but usually they're not, right?"

                RL "And maybe the long distance relationship has been harder on Ilya than on Shane...?"

                show zzsv thoughtful

                SV "..."

                SV "Is that what you think? What Shane thinks?"

                RL "Oh, I guess I don't know what Shane thinks. I mean, he seems happy...?"

                RL "But we haven't talked much since he told me he was with Ilya. He gets really locked in during the season, and then the Metros crashed out of the second round of playoffs, so..."

                show zzsv unimpressed

                SV "At least they made they made the playoffs. Ottawa hasn't made the playoffs in more than ten years, and Ilya is good, but he cannot carry the whole team on his back."

                SV "And they want to do this until retirement? How many more seasons until retirement?"

                show zzrl surprised

                RL "Oh, they want to do this until retirement?"

                show zzsv flat

                SV "Mm, I don't know, you'd have to ask Shane."

                SV "Okay, enough talking about them. It is boring, and unlike Ilya, I am {i}not{/i} a fan of boring."

                show zzrl hesitant

                RL "Haha, fair enough. So, um, let's talk about what's going on with the LA Queens! This might just be rumours, but apparently they're planning to draft {i}both{/i} the Buck twins..."

                jump preleaving

            "Svetlana":
                show zzrl thoughtful

                RL "You."

                show zzsv flirty
                
                SV "Oh? Say more."

                menu:
                    "Learn Russian":
                        $ pt += "russian, "
                        $ russian += 1

                        show zzrl smile_blush

                        RL "I was just wondering...I mean, you speak Russian, right? What am I saying, obviously you do—could you teach me?"

                        show zzsv eyebrow

                        SV "...that is an unexpected request."

                        show zzrl wince

                        RL "Sorry, this probably sounds totally out of the blue for you, but—"

                        show zzsv smile

                        SV "Mm, a little, but I would be happy to. Why the interest?"

                        show zzrl hesitant

                        RL "I guess I've been thinking a lot lately about...things I keep saying I wanna do, but haven't done. And one of those things is to learn a foreign language."

                        show zzsv eyebrow

                        SV "And you are deciding on Russian? It is not easy."

                        show zzrl smile

                        RL "Yeah, I might not get far, but hey, let's start from 'nice to meet you' and see how far we get?"

                        show zzsv thoughtful

                        SV "Don't put yourself down so fast. You might get further than you think, if learning Russian really matters to you."

                        RL "Well, you speak it. And Ilya, too, I guess. So that's two people in my life to learn it for."

                        show zzsv flirty

                        SV "Mm, learning Russian for me? I'm flattered. Ilya...will probably be less flattered."

                        show zzsv amused

                        SV "Not going to learn French for Shane?"

                        show zzrl grin

                        RL "Oh God, no, his French is terrible!"

                        SV "Is it? You know, Ilya once told me Shane's French is perfect, I should go tell him—"

                        scene cut boys_inside
                        with fade

                        SV "..."

                        SV "...clearly he is just very biased about Shane."

                        RL "Oh yeah, he's very bi about Shane's ass. If you know what I mean."

                        scene bg backporch
                        show zzsv amused at center
                        show zzrl smile_blush
                        with fade

                        SV "Wow. I can't believe your sense of humour is just like Ilya's. Bad."

                        show zzrl grin

                        RL "Hey, I've got more where that came from and I can keep it coming all night. Just like Ilya. If you know what I mean."

                        SV "Alright, enough. Time for Russian lessons. No more English from you."

                        show zzrl smile

                        RL "Okay, okay, I'll stop. Promise I'll be a good student and not even ask you what 'dick' is in Russian."

                        RL "Should we go back inside? We can go grab your bags from the car too, since I'm sure the boys forgot."

                        show zzsv flirty

                        SV "Yes, let's go back in. And I'll keep your hands and mouth busy, until the boys are done keeping {i}their{/i} hands and mouths busy." ## too forward?? not funny enough??
                        
                        SV "If you know what I mean."

                        scene bg dining

                        if russian == 1:
                            show zzsv amused at center
                            show zzrl smile_blush
                            with fade

                            $ svetheart += 1
                            show sv_heart at center, blip

                            SV "You're not too bad for a beginner. But you might need a lot more one-on-one tutoring."

                            RL "Well in {i}that{/i} case—"
                        
                        elif russian == 2:
                            show zzsv surprised at center
                            show zzrl smile_blush
                            with fade

                            $ svetheart += 1
                            show sv_heart at center, blip

                            SV "I'm genuinely impressed. You're a natural."

                            RL "I have a really motivational teacher, so—"
                        
                        else:
                            show zzsv eyebrow at center
                            show zzrl smile_blush
                            with fade

                            SV "...okay, tell me the truth. You've learned Russian before, haven't you?"

                            RL "Or hey, maybe you're just that good a teacher—"

                        jump leaving

                    "Learn about Svetlana":

                        RL "This is gonna sound strange, but...I guess it feels like I know you and don't know you at the same time?"

                        SV "No, not strange at all, I know exactly what you mean."

                        RL "You do?? Wait, are you also trapped in this time loop??"

                        show zzsv eyebrow

                        SV "...what?"

                        show zzrl wince

                        RL "Nothing, never mind, sorry. Um, what did you mean by that?"

                        show zzsv amused

                        SV "I mean I know Rose Landry, box office darling, the girl everyone wishes was next door. But I don't really know Rose, who I'm meeting today for the first time."

                        if svetheart >= 4: ## you may need to change this if you add more svethearts esp gift option

                            show zzsv thoughtful

                            SV "Or perhaps it's the other way around."

                            show zzrl hesitant

                            RL "The other way around...?"

                            SV "Perhaps I am getting to know Rose, the best friend of my best friend's boyfriend, who I'm meeting today for the first time. And it's movie star Rose Landry that I don't know at all."

                            show zzrl smile

                            RL "Yeah? I think that's the right way around too."

                            show zzrl grin

                            RL "Though that's a terrible tagline! It's like, Rose Landry, the girl who used to sleep with the guy who's sleeping with the guy you used to sleep with."

                            show zzsv amused

                            ## check below if players are always only getting one option and we need another var to help them cycle

                            if blindsnow == True:
                                SV "Yes, a bit clunky. Have you considered 'Rose Landry, the angel who doesn't weep'?"

                                show zzrl grin_blush

                                RL "No, no, I've sworn off body paint, no more angels here."

                                show zzsv flirty

                                SV "Mm, you're more than angelic enough as you are. And you might not weep, but you could still come closer if I close my eyes."

                                RL "Oh, well..."

                                scene cut girls_kiss2
                                with fade

                                RL "..."

                                SV "..."

                                scene bg backporch

                                show zzsv smile_blush at center
                                show zzrl smile_blush
                                with fade

                                SV "Good thing your touch didn't send me back in time."

                                RL "...wait a minute—"

                            elif russianpass == True:
                                SV "Yes, a bit clunky. Doesn't sound as smooth as 'Rose Landry, secret polyglot'."

                                show zzrl smile_blush

                                RL "Oh my God, I barely managed to say hello, now you're just buttering me up."

                                show zzsv flirty

                                SV "That depends. Is it working?"

                                RL "Well..."

                                scene cut girls_kiss2
                                with fade

                                RL "..."

                                SV "..."

                                scene bg backporch

                                show zzsv smile_blush at center
                                show zzrl smile_blush
                                with fade

                                SV "...mm, so you do have a clever tongue—"

                            elif svet_room2 == True:
                                SV "Yes, a bit clunky. Doesn't roll of the tongue as well as 'Rose Landry, proud owner of a wand and a rabbit'." ## red wine supernova ref

                                show zzrl grin_blush

                                RL "Look, a girl gets lonely on those long nights away from home. Might as well take a little magic with me."

                                show zzsv flirty

                                SV "Mm, well you've certainly been very enchanting..."

                                scene cut girls_kiss2
                                with fade

                                RL "..."

                                SV "..."

                                scene bg backporch

                                show zzsv smile_blush at center
                                show zzrl smile_blush
                                with fade

                                RL "...mmm. Wow. Guess you don't even need a wand to cast a spell on me—"
                            
                            else:
                                SV "Yes, a bit clunky. Do you prefer 'Rose Landry, excellent guide to other people's houses'?"

                                show zzrl grin

                                RL "Oh, how kind of you, Ma'am, please don't forget to leave a good review!"

                                SV "'Host was charming and enthusiastic and very lovely, five stars'."

                                show zzrl smile_blush

                                RL "Haha, thank you, we're so glad to hear you're enjoying your stay. Please let me know how else I can be of service."

                                SV "Well, if you're asking..."

                                scene cut girls_kiss2
                                with fade

                                RL "..."

                                SV "..."

                                scene bg backporch

                                show zzsv smile_blush at center
                                show zzrl smile_blush
                                with fade

                                SV "...mm, what excellent personalised service."

                                RL "Haha, wow, if that's my tip for good service—"

                            $ random = 6
                            $ kissnow = True
                            $ kisscount += 1
                            $ freedom += 1
                            
                            jump postkiss

                        else:
                            show zzrl hesitant

                            RL "Ah, right, yeah. And I know of Svetlana Vetrova, daughter of Sergei Vetrov, best friend of Ilya Rozanov. But Svetlana, who I'm also definitely meeting today for the first time, has hidden depths I probably don't know about."

                            SV "I'm surprised you know about my father. Most Americans don't."

                            show zzrl smile_blush

                            RL "I saw his name when I looked you up. And I used to play goalie as a kid, so I already knew of him."

                            show zzsv surprised

                            SV "You were a goalie? Now {i}that{/i} is a hidden depth."

                            show zzrl grin

                            RL "Yeah, I have three brothers who all play hockey, and it turns out I really enjoyed blocking their shots and making them shout and swear. And then they'd get yelled at by my dad for swearing at me."

                            show zzsv flirty

                            SV "Diabolical. You know, it's been a while since I played hockey myself, but I wonder if I could score on you. Or perhaps you'd make me shout and swear too."

                            show zzrl smile_blush

                            RL "Oh, haha, I guess there's only one way to find out! I think there's a rink in the basement, we could go back inside and—"

                            scene cut boys_inside
                            with fade

                            SV "..."

                            RL "...well guess someone's already scoring."

                            scene bg backporch
                            show zzsv eyebrow at center
                            show zzrl grin_blush
                            with fade

                            RL "Maybe we shouldn't head back in quite yet. Actually, why don't we circle around and get your bags from the car? The boys have probably forgotten about them again."

                            show zzsv unimpressed

                            SV "Yes, they probably have."

                            show zzsv smile

                            SV "Anyway, as a goalie yourself, do you have any thoughts on your fellow goalie Wyatt Hayes? If you're following the Ottawa Centaurs, I mean."

                            show zzrl smile

                            RL "I am, yeah! I'm so surprised how well he's been doing, considering he barely played in Toronto..."

                            jump preleaving

            "Time loops":
                # kisses happen easier, lol sveta is charmed by the crazy, which i suppose makes sense given ilya

                show zzrl resigned

                RL "Time loops. Actually, I'm thinking of time loops."

                show zzsv surprised

                SV "What?"

                RL "Let's say, hypothetically, imagine I was stuck in a time loop, and we've had this conversation before, and I wanted to prove it to you."

                RL "How would you suggest I do that? Would you ask me to do a test?"

                show zzsv eyebrow

                SV "A...test?"

                SV "I suppose that is one way to prove you were, let's say, hypothetically, stuck in an imaginary time loop, yes."

                show zzsv thoughtful

                SV "If I asked you questions that you had no way of knowing the answers too, unless you had been asked before..."

                RL "Yes! Exactly! Okay, so, test me! Ask me some questions!"

                if svetheart >= 3:
                    show zzsv amused

                    SV "Mm, alright. A test, for if you're hypothetically stuck in a time loop and want to prove it to me."
                    
                    SV "I suppose I've had stranger conversations with women I'm meeting for the first time. At least this is more interesting than talking about star signs."

                    RL "Great okay—no wait, we gotta keep walking. Here, let's go this way, you keep thinking about your questions..."

                    scene bg outback
                    show zzrl flat
                    with fade

                    show zzsv flat at center
                    with easeinright

                    $ freedom += 1

                    SV "..."

                    SV "I had some questions in mind, but I think now my only question is—"

                    RL "—why is there a moose? Yeah. There's such a thing as being too Canadian, Shane."

                    RL "...um, so, did you really have some questions in mind already? Questions that should be exactly the same each time so I could prove I was really in a time loop."

                    RL "Hypothetically, I mean."

                    show zzsv amused

                    SV "Yes, yes, hypothetically. Okay, here's my first hypothetical question."

                    jump outside_test
                
                else:
                    SV "Hmm, the question I'd like to ask is, why do you want me to believe that you're in a time loop?"
                    
                    SV "If you're let's say, hypothetically, stuck in an imaginary time loop. Why not tell Shane about it, for instance?"

                    show zzrl wince

                    RL "Look, Shane's great, but there is no way I'm getting him to believe time loop stuff is real. I'm pretty sure he hasn't even heard of Groundhog Day before."

                    RL "And in any case, he's busy. See?"

                    scene cut boys_inside
                    with fade

                    SV "..."

                    SV "Yes, I'm seeing."
                    
                    SV "If you did want to tell him, you'd have to pick a time that he might be more receptive."
                    
                    SV "To the idea, I mean."

                    scene bg backporch
                    show zzsv flat at center
                    show zzrl hesitant
                    with fade

                    RL "Right. But I don't want to tell to Shane. I want to talk about this with you."

                    RL "If, I mean, if you wanted to—{size=-8}fuck, how did I say this last time{/size}—if it were true, hypothetically, then—"

                    show zzsv amused

                    SV "Mm, alright, I'll bite. What do we talk about, in this hypothetical time loop of yours? If we've had this conversation before?"

                    RL "Um. We've talked about Shane and Ilya...?"

                    show zzsv flirty

                    SV "Surely it's impossible that I should have spoken to you alone multiple times, out here on this lovely evening, and all we talked abuot was those silly boys."

                    show zzrl wince

                    RL "Ah, haha, yeah, that does sound impossible, huh..."

                    show zzrl hesitant

                    RL "We also talked about hockey? Hypothetically, I mean, if I were in a time loop, maybe we went to pick up your bags from the car and started to chat about...Wyatt Hayes...?"

                    SV "Hayes? Hah, yes, I {i}would{/i} happily talk about him again and again. I've always said that Toronto was wasting him, and—"

                    jump preleaving

label outside_test:
    $ pt += "try test, "

    SV "See that butterfly over there? Which flower do you think it lands on?"

    menu:
        "The pink flower":
            RL "The pink one."

            SV "..."

            show zzsv eyebrow

            SV "Well, would you look at that, it did. Though I suppose that could be coincidence..."

            show zzrl smile

            RL "Ask me another question then."

            show zzsv smile

            $ convincesvet += 1

        "The yellow flower":
            RL "The yellow one."

            SV "..."

            SV "Ah, no. It picked the pink flower. Better luck next time."

            RL "Wait, ask me another question! Just in case, for next time."

            show zzsv eyebrow

        "The red flower":
            RL "The red one."

            SV "..."

            SV "Ah, no. It picked the pink flower. Better luck next time."

            RL "Wait, ask me another question! Just in case, for next time."

            show zzsv eyebrow

    SV "Alright. What's my favourite colour?"

    menu:
        "Pink":
            RL "Pink."

            show zzsv amused

            SV "No, it's red, actually. You'll have to remember that for next time."

            RL "I will. Ask me another?"

        "Yellow":
            RL "Yellow."

            show zzsv amused

            SV "No, it's red, actually. You'll have to remember that for next time."

            RL "I will. Ask me another?"

        "Red":
            RL "Red."

            show zzsv surprised

            SV "It...is, yes. Though Ilya might have told you this."

            show zzrl eyebrow

            RL "You think Ilya Rozanov tells me things?"

            show zzsv amused

            SV "Ah, no, fair enough."

            show zzrl smile

            RL "Look, why don't you ask me another question then? Something Ilya won't know?"

            $ convincesvet += 1

    show zzsv thoughtful
    
    SV "Hmm...the most telling question, I think. Which power ranger did I have a crush on when I was younger?"

    menu:
        "Pink ranger":
            RL "Pink ranger."

            show zzsv amused

            SV "Sorry, but I liked Tanya Sloan best, actually."

            RL "Who?"

            SV "If you're in a time loop, I'm sure you'll have time to look her up."

        "Yellow ranger":
            RL "Yellow ranger."

            show zzsv surprised

            SV "I—well. Yes."

            show zzsv thoughtful

            SV "I didn't know whether I wanted her or wanted to be her."

            $ convincesvet += 1

        "Red ranger":
            RL "Red ranger."

            show zzsv amused

            SV "Sorry, but I liked Tanya Sloan best, actually."

            RL "Who?"

            SV "If you're in a time loop, I'm sure you'll have time to look her up."

    if convincesvet == 3:
        jump testpassed
    
    else:
        jump testfailed

label testpassed:
    
    $ pt += "pass test, " 

    show zzsv surprised

    SV "Hmm. You passed the test."
    
    if svetpass == 0:
        $ svetpass += 1

        RL "So you believe me! That I'm stuck in my own Groundhog Day!"

        show zzsv thoughtful

        SV "Let's say I do. What now?"

        show zzrl hesitant

        RL "What now? I guess...we...figure out how to get me out?"

        SV "Do you know why you're trapped? There must be something you need to fix, yes?"

        show zzsv unimpressed

        SV "Ah. Am I going to die?"

        show zzrl surprised

        RL "{i}No!{/i} What??"

        show zzsv eyebrow

        SV "That's a common reason for time loops, no? Someone dies, you need to save them? Not me, then—maybe someone's put out a hit on Shane? A Boston fan, perhaps—though in that case, they're more likely to put out a hit on Ilya—"

        show zzrl wince

        RL "Right, right, like Happy Death Day. No, nope, no one dies today, thank fuck."

        show zzsv amused

        SV "You did seem more relaxed than I would expect, if you were watching someone die repeatedly. But then, you are a good actress."

        show zzrl hesitant_blush

        RL "Thanks. I think."

        show zzsv thoughtful

        SV "Alright, so no deaths. Anything else particularly noteworthy or troubling? Something that should be avoided?"

        show zzrl grin

        RL "Not really...? I mean, the only noteworthy thing is just how many times I walk into Shane and Ilya making out. And I'm starting to wonder if that's just noteworthy for me, and not them."

        RL "And I guess I should avoid it, if only for Shane's peace of mind, but still, that seems..."

        show zzsv amused

        SV "Not quite the stuff time loop movies are made of, no."

        SV "Really, if that's the most troubling thing that happens, why bother breaking the loop? You don't want to take advantage of this relaxing, neverending lakeside holiday?"

        show zzrl grin

        RL "Oh my god, I could. I should! Maybe the universe is telling me to chill out and take a break. Maybe it's time to finally learn a new language like I keep saying I would."

        show zzsv flirty

        SV "Well, if you're looking for a Russian tutor, I'm right here."

        show zzrl smile_blush

        RL "You know what, I might just take you up on it, even if you won't remember making the offer. Maybe I'll impress you with my Russian fluency."  

        show zzsv flirty

        SV "You're already pretty impressive anyway, Rose Landry."

        SV "Also, you know, the other traditional way to break a time loop is with a kiss."

        menu:
            "Lean in...":
                $ pt += "kiss, "

                RL "Oh, haha, that's...that's fair! I suppose if it's traditional..."

                scene cut girls_kiss1
                with fade

                RL "..."

                SV "..."

                $ kissnow = True
                $ kisscount += 1

                $ random = 5

                jump postkiss

            "Don't lean in":
                $ pt += "don't kiss, "

                RL "Oh! Is, um, is it? Which movie is that from?"

                show zzsv amused

                SV "Movies aren't the only stories with time loops in them, you know."
                
                SV "But if you're hoping {i}not{/i} to break out of the loop, perhaps that's best avoided."

                show zzrl hesitant_blush

                RL "Haha, yeah, gotta have a bit more of a holiday first! I guess—"

                $ random = 6

                jump postkiss
    
    elif svetpass == 1:
        $ svetpass += 1

        show zzrl grin

        RL "Yes! I passed! So you believe me now, right? About the time loop?"

        show zzrl hesitant

        RL "Because I still don't know why I'm trapped or how to fix it."

        SV "Hmm, is—"

        RL "You're not going to die, by the way! No one dies!"

        show zzsv eyebrow

        SV "That...wasn't my first thought."

        show zzsv amused

        SV "I mean, it was certainly in the top three, so thank you for reassuring me on that point."

        RL "You were the one who suggested it the last—wait, if that's not your first thought, what's your first thought?"

        show zzrl wince

        RL "Because my first thought was that the universe thinks I need stop being an asshole and improve myself or something, and I have to say I'm feeling {i}some kind of way{/i} about still being stuck."

        show zzsv thoughtful

        SV "Ah, because of Groundhog Day? Mm, considering you're successful, talented, and a delightful person to be around, I think it's unlikely that this is what the universe is trying to tell you."

        show zzsv amused

        SV "Also, if you were even slightly an actual asshole at any point today, I think {i}Ilya{/i} would have told you. At length. With helpful demonstrations. So the fact that you haven't been kicked out Shane's cottage..."

        show zzrl smile_blush

        RL "Haha, yeah, I guess."
        
        RL "I mean, there's probably still stuff I should work on? No one's perfect, right, least of all me...as my dating record probably shows..."

        show zzsv eyebrow

        IR "Surely dating Shane Hollander is more a sign of good taste than bad taste."

        RL "Well, yeah, he's great, but he's also..."

        SV "Gay?"
        
        RL "Yes! And I somehow keep dating gay men again and again—ugh, my dating history is like a time loop, actually!"

        RL "Maybe this is what the universe is trying to tell me! Especially with how Shane and Ilya keep kissing in front of me!"

        show zzsv flirty
        
        SV "Mm, I see. Yes, the universe has trapped you here to teach you to stop kissing gay men. So the only possible way you could break free is..."

        menu:
            "Lean in...": ## should i just make this a very obvious 'kiss' 'don't kiss' menu choice
                $ pt += "kiss, "

                show zzrl smile_blush

                RL "Oh, um, by...kissing...women..."

                scene cut girls_kiss1
                with fade

                RL "..."

                SV "..."

                $ kissnow = True
                $ kisscount += 1

                $ random = 5

                jump postkiss

            "Don't lean in":
                jump nokiss 

    else:
        $ svetpass += 1
        
        show zzrl resigned

        RL "Yeah. This is not my first rodeo."

        SV "Because you're stuck in a time loop. Alright. So what now?"

        RL "We figure out how to get me out. You asked me before if anything stood out as something that I should change, something bad. But aside from, y'know, myself, there's nothing I can think of."

        show zzsv eyebrow

        SV "Rose, I may have only known you for one day, but I am certain you are not a bad person."

        RL "That's what the guy in Groundhog Day probably thought at the start..."

        SV "Well, there's far more time loop fic—I mean, media—I mean, there's far more time loop movies and books out there than just Groundhog Day."

        show zzsv thoughtful

        SV "Anyway, perhaps we're approaching this from the wrong angle. What have you tried doing differently?"

        show zzrl hesitant

        RL "Mostly just saying different things...? Trying to catch up with Shane, trying to get Ilya to like me?"

        if foodtruckkitty + foodtruckkitty2 + foodtruckkitty3 >= 2:
            $ foodtruckkitty3 -= 100
            show zzrl wince

            RL "{size=-8}...and also I've played a bunch of Food Truck Kitty..."

            show zzsv eyebrow

            SV "What's that?"

            RL "It's a mobile game where...never mind, it's silly, I probably shouldn't have been wasting my time with it when I'm stuck in a supernatural time loop."

            show zzsv amused

            SV "If you ask me, being stuck in a time loop is the best time to be playing silly mobile games. When else would you have the infinite free time?"

            show zzrl grin

            RL "Well, when you put it like that!"

            SV "Also, it's far more productive than trying to get Ilya to like you in one day."
        
        elif clearemail + clearemail2 + clearemail3 >= 2:
            $ clearemail3 -= 100
            show zzrl resigned

            RL "And also I've been trying to catch up on work. Haven't suceeded yet, which is maybe that's why I'm still trapped."

            show zzsv eyebrow

            SV "Work? While the universe has forced you to go to an isolated, beautiful lakeside mansion again and again? Have you considered the universe might be telling you {i}not{/i} to work?"

            show zzrl wince

            RL "Okay, that's fair."

            show zzsv amused

            SV "Though if it helps, it sounds less pointless and impossible to achieve then trying to get Ilya to like you in one day."

        else:
            show zzsv eyebrow

            SV "Unless you can loop back in time all the way to two years ago to stop yourself from dating Shane, I don't think you're getting Ilya to like you. Not in a single day."

        show zzrl resigned

        RL "I suppose. Honestly, I wouldn't care so much about Ilya liking me if I didn't think it would make Shane happier if we got along."

        show zzsv amused

        SV "I do think time loops are meant to be solvable. If Shane Hollander's happiness is the solution, then there must be a less impossible way to achieve it. Could you not buy him a box of chocolates or something?"

        show zzrl grin

        RL "Hah, pretty sure that will {i}not{/i} make him any happier. Maybe I'll buy him an Ilya Rozanov jersey instead."

        if freedom == 3:
            SV "I don't think I've ever heard of that as a solution to a time loop, but I suppose there's no harm trying."

            SV "That said, if you did want to try something that's more likely to succeed, a kiss is a common way to break a time loop."
        
        else:
            RL "Though I'm not sure I wanna be even more involved in their sex life than I already am."

            SV "What?"

            RL "I keep walking in on them getting hot and heavy, which I really wish I could avoid—not because I think it's bad or anything! It's just that they're—"

            SV "Hot?"

            RL "I was going to say they're my friends, but you're not wrong. Still shouldn't be watching them kiss though, probably."

            SV "Mm, then again, a kiss {i}is{/i} a common way break a time loop."

        menu:
            "Lean in...": ## should i just make this a very obvious 'kiss' 'don't kiss' menu choice
                $ pt += "kiss, "

                show zzrl smile_blush

                if kisscount >= 1:
                    RL "I've tried it before, but you know what, I'm happy to keep trying."
                
                else:
                    RL "Oh, well, of course I have to try it, then..."

                scene cut girls_kiss1
                with fade

                RL "..."

                SV "..."

                $ kissnow = True
                $ kisscount += 1

                $ random = 5

                jump postkiss

            "Don't lean in":
                jump nokiss                      

label nokiss:
    $ pt += "don't kiss, "

    show zzrl hesitant_blush

    RL "Oh, um, to stop kissing gay men? To...stop watching gay men kiss...?"

    show zzsv amused

    SV "A reasonable thing to try. I'm sure Shane would thank you for the effort."

    SV "Ilya, I'm not so sure. But then, he's not a gay man so maybe he doesn't get a say."

    show zzrl surprised 

    RL "Wait, you think Ilya {i}wants{/i} me to see him kiss Shane...? No way, he seems so, er, possessive."

    SV "True. But he likes to show off his sparkly things, and Shane is the sparkliest thing he has."

    show zzrl hesitant

    RL "Oh, but...you don't think Ilya really thinks of Shane like that, do you?"

    show zzsv smile

    SV "Mm, not quite like that, no."

    show zzsv thoughtful

    SV "But he can't stop himself from pressing on a bruise, either."

    show zzrl smile

    RL "Trying to prove he's a big strong man and not scared of pain? My brothers get like that too."

    show zzsv smile

    SV "Yes, you understand. The more it hurts, the more they have to prove."

    show zzrl hesitant

    RL "And the bruise is...me looking at Shane sexually...?"

    show zzsv thoughtful

    SV "Mm, and now if you are, at least it's Ilya's choice."
    
    SV "Or perhaps it's is getting to be seen with Shane at all."

    show zzrl eyebrow

    RL "...I feel like not being able to have people see you hold hands is kinda different from not being able to have people see you hold each other's naked dicks."

    SV "Mm. Well. Perhaps Ilyusha is just being a petty child then, and wants you to see what you cannot have."

    RL "Oh, that's—"

    $ random = 6

    jump postkiss

label testfailed:
    SV "Well, you haven't exactly proven yourself..."

    if outside == 3:
        show zzrl wince

        RL "I did say we hadn't done this before."

        show zzsv smile

        SV "True, you did say. Perhaps I should have asked you about something that you think {i}has{/i} happened before."

        show zzrl hesitant

        RL "Yeah, we...also talked about hockey? While we went to get your bags, since Shane and Ilya are, y'know, distracted."

        SV "Let's do that then. Tell me, Rose, what do you think I think of...say....Wyatt Hayes—"

    else:
        show zzrl wince

        RL "I know."

        show zzsv eyebrow

        SV "Did I, ah, ask different questions in your previous hypothetical loops"

        show zzrl hesitant

        RL "No, you—aha, it was just a joke, anyway. I thought it seemed like a fun thought exercise! That's all!"

        RL "Let's...let's go get your bags! I bet Shane and Ilya forgot about them again—not that it's happened before or anything, I'm just guessing!"

        SV "Yes, seems like a reasonable guess."

        RL "Hah, yeah, right? Anyway, say, what do you think of Wyatt Hayes?"

    jump preleaving

label postkiss: # it is possible no kiss happens prior to this just fyi

    if random == 5:
        scene bg outback

        show zzsv smile_blush at center
        show zzrl smile_blush
        with fade

        RL "Wow."

        SV "Mm. Does it feel like the time loop is broken?"

        RL "I...I have no idea. Um, I guess we just have to keep going with the rest of the day and I'll find out tomorrow...?"

        show zzsv flirty

        SV "Yes, and if it doesn't work maybe you'll have to try again."

        show zzrl grin_blush

        RL "Oh, absolutely, I'll have to—"

    show zzsh frown at center
    show zzir flat at midright
    with easeinright

    show zzsv at midleft
    with ease

    SH "Oh, good, we found you guys. You weren't inside, and you both weren't replying to your texts..."

    show zzir smirk

    IR "Thought you were eaten by Canadian wolf birds. But the only thing you were eating is—"

    show zzsv unimpressed 

    SV "Ilya." ## make these two lines unison?

    show zzsh frown

    SH "Ilya."

    show zzir eyebrow

    IR "Wow, okay, now there are two of you. It's like I am seeing double."

    show zzsh smirk

    SH "Then maybe you should get your eyes checked. Maybe that's why you keep losing to me at Chel—"

    show zzir outraged

    IR "I do not—it is Shane Hollander who keeps losing—"

    show zzsh annoyed

    SH "Only because you keep playing me like shit! In real life—"

    show zzsv amused

    SV "I'm sure in real life he's much better at playing with you."

    show zzsh embarrassed

    SH "Um."
  
    SV "Anyway, sorry we didn't reply to texts. I think I still have Ilya muted from the last time he was being annoying."

    show zzsh smirk

    SH "If you mute Ilya every time he's annoying, he must be muted on your phone all the time."

    SV "He is. Though I do unmute him when he buys me an appropriate apology present."

    show zzir eyeroll

    IR "Hah, you unmute me when you want to bitch about your clients or gossip about people we know. Which is also all the time."

    show zzsv amused

    SV "Yes, I clearly need better people to text. Rose, you should give me your number."

    show zzir annoyed

    IR "Why do you want Rose Landry's number? There is no reason for you two to text after today."

    if svetpass == 1 or outside == 3:
        show zzrl smile_blush

        RL "Oh, sure! Here's my number—"

        show zzrl wince

        RL "Oh shit, is that the time? I gotta go, my flight's in three hours."

    else:
        show zzrl smile_blush

        RL "Sure, here's my number. Hope I {i}can{/i} text you after today."

        if freedom == 3:

            SV "Mm, I have a good feeling about it."

            show zzir frown

            IR "I do {i}not{/i} have a good feeling about it."
        
        RL "Anyway, I gotta go, I have a flight to catch."
    
    SH "Oh, yeah. Hey, let me walk you to your car?"

    jump walkout

label preleaving:

    scene bg dining

    show zzsv smile at center
    show zzrl smile
    with fade

    if outside == 1:
        RL "—and I couldn't believe they drafted him!"

        SV "Exactly, how many more Hues brothers could there possibly be? It's—" 
    
    elif outside == 2:
        RL "—and I couldn't believe that final! The Whitecaps winning their first Isobel Cup in their first year in the league has to be the hockey story of the year!"

        SV "Agreed, but the MWHL cannot continue this one game final nonsense. When will we get—"
    
    elif outside == 3:
        RL "—and if he doesn't want to 'bunch' his girlfriend's 'mox,' I'm sure I know someone who will."

        show zzsv amused

        SV "And who would that be?"

        show zzrl smile_blush

        RL "Oh! Um—"
    
    elif outside == 4:
        RL "—and the red light therapy, fine, it helps with hair thinning and God knows male pattern baldness comes for them all. But what I really can't wrap my head around is the—"

        SV "The WiFi repelling protection amulet?"

        RL "The WiFi repelling protection amulet! I mean, hockey superstition is one thing, but—"
    
    elif outside == 5:
        RL "—and I couldn't help wondering, what if life is basically hockey? You might trade a player, shake up your plays, but it's still the same game over and over—"

        SV "And you pay in sweat and blood for the win, you think it is the most important thing in the world—and it is important, yes, but it also isn't, because—"

        RL "—because the next day and you play the same game all over again! Life is a game—actually, maybe it's not a hockey game, what if it's a video game, what if—"
    
    else:
        RL "—and I couldn't believe how chaotic 2019 was. For Washington to clinch it! Washington!"

        SV "At least there's no way 2020 can be worse. It's—"
    
    jump leaving

label leaving:

    show zzsh flat at center
    show zzir flat at midright
    with easeinright

    show zzsv at midleft
    with ease

    SH "Hey, sorry we took so long—wait, are these Svetlana's bags?"

    if loop == 0:
        show zzrl grin
    
    elif loop == 1:
        show zzrl smile
    
    else:
        show zzrl resigned

    RL "The bags that you and Ilya didn't bring in again? Yup."

    show zzsv amused

    ## fix the following if only sveta picks up bags if rose was chilling alone

    SV "You two were busy, so we decided to help ourselves."

    show zzsh embarrassed

    SH "Oh my god, you saw—"

    show zzir smirk

    IR "Yes, Shane and I always have a busy summer here, so good job helping yourselves. Congrats, big win for feminism."

    show zzsv unimpressed

    SV "Right. Big win, yes, for women in general and Rose specifically, because she is going home with five bottles of your vodka today as thanks for actually helping."

    show zzir annoyed

    IR "Oh, okay, it's like that? I support women's rights and women's wrongs, no problem, she can have five bottles, I will have other twenty-five." ## come back to this

    show zzsh eyebrow

    SH "...seriously, who taught you that??"

    show zzir smirk

    IR "Taught me what, math? Do they not teach you this in Canadian school?"

    show zzsv flat

    SV "I did not actually bring you thirty bottles of vodka, Ilya."

    if loop <= 1:
        show zzrl hesitant

        RL "Actually, I can probably only take one bottle with me on the flight back, so Ilya can keep the rest. Which, speaking of heading back..."
    
    else:
        show zzrl resigned

        RL "It's fine, I don't think I'll get a chance to drink it, anyway. Also, I should go..."

    show zzir outraged

    IR "Sveta! You only bring me five bottles??"

    show zzsh hesitant

    SH "Oh shit, is it already that late? Sorry, Rose, I didn't realise the time—"

    show zzrl smile

    RL "Hey, it's fine, thanks for having me! Even if we didn't quite manage to have dinner together."

    RL "Anyway, it was nice meeting you, Ilya. And nice meeting you too, Svetlana."

    show zzsv flirty

    if kissnow == True:

        SV "Especially nice meeting you, Rose. Let me know if you're ever in Boston, we can go to a game together, perhaps."

        show zzrl grin_blush

        RL "Yes, for sure, same back to you! If you're ever in LA, just let me know!"

        SV "Of course. Let me give you my number."

        show zzir outraged

        IR "You're giving her your number?!"

        show zzsv unimpressed

        SV "If you keep making a fuss, I will give her my number, your vodka, and also all the pelmeni."
    
    else:
        SV "Especially nice meeting you, Rose. Nicer than meeting Ilya, I'm sure."
    
    IR "Okay, I see how it is. I worried about snakes and wolves out in the Canadian wilderness, but all the snakes are in this house—" ## come back to this

    show zzsh smirk

    SH "Canadian wilderness? Rozanov, we're in cottage country. The only thing that might eat you out here in this wilderness is mosquitoes." ## check show check canadian

    show zzsh smile
    
    SH "Anyway, Rose, I'll walk you to your car?"

    jump walkout

label walkout:

    scene bg ctdoor

    show zzsh hesitant at center
    show zzrl flat
    with fade

    SH "Sorry, I feel like you came all the way up here and I still didn't get to see much of you."

    if loop == 0:

        show zzrl grin

        RL "Well, I actually saw a whole lot of {i}you.{/i} And Ilya. If you know what I mean."

        show zzsh embarrassed

        SH "Oh my god, I'm so sorry, I wasn't—"

        show zzrl smile

        RL "Hey, hey no, it's fine! Besides, I've already seen it all, right?"

        show zzsh hesitant_blush
        
        SH "That's...it's different, though. If it's when I'm with Ilya."

        show zzrl grin

        RL "Clearly! Three times in half a day? I could never believe it of the Shane Hollander I dated!"

        show zzsh embarrassed

        SH "Rose, oh my god—"

        show zzrl smile

        RL "Alright, alright, I won't tease anymore. But seriously, I'm always happy to see more of you, okay? I know we didn't get to talk much today, but I'd do it all again."

        SH "...If you did do it all again, I wish you'd see less of me, actually."

        scene bg ctdoor
        show zzsh embarrassed
        show zzrl smile
        with pixellate

        show zzrl surprised

        RL "Whoa! What was that?"

        show zzsh hesitant

        SH "What...? I mean, I said, if you did it all again—"

        ## insert transition here if you wanna make things really clear, or you could wait until after playtest to decide

        show zzrl hesitant

        RL "Oh, haha, no I heard you. Just got lightheaded for a second."

        show zzrl grin
        
        RL "And hey, if you want me to see less of you, take it up with your boyfriend!"

        RL "Or rather, don't take it from your boyfriend, if you know what I mean—"

        show zzsh smile_blush

        SH "That is terrible, Landry. Get outta here already."

        RL "I'm going, I'm going! Love ya', talk to you soon, yeah?"

        show zzsh smile

        SH "Yeah. Thanks for coming, Rose, talk to you soon as I can, promise."

    elif loop == 1:

        show zzrl thoughtful

        RL "You know, it kinda feels like I saw more of you than you thought."

        show zzsh embarrassed

        SH "Oh my god, I'm so sorry, I wasn't—"

        show zzrl surprised

        RL "Oh! I didn't mean in like a nudge-nudge-wink-wink kinda way!"

        show zzrl grin

        RL "I mean, I did see more of you than you thought, nudge-nudge-wink-wink—"

        show zzsh smile_blush

        SH "Knock it off, Landry, I swear you're worse than my rookies sometimes."

        show zzrl smile

        RL "—but I also meant...I dunno, today just feels really familiar? Lots of deja vu, like my subconcious thinks I've seen more of you today than I actually have, or something?"

        show zzsh hesitant

        SH "Uh. I don't know what that means. Is that...a good thing? Bad thing?"

        show zzrl thoughtful

        RL "Hmm! You know what, it doesn't feel like a bad thing, really."

        show zzsh smile

        SH "Okay then. I'm glad you think so. Um, see you around?"

        RL "See you around! Don't be a stranger!"

    elif loop == 2:

        RL "That's okay, I saw lots of you, actually."

        RL "Hey, out of curiosity. Do you know about Groundhog Day?"

        SH "Uh...is that like one of those breast cancer awareness day things? But for groundhogs...?" ## canadian check?? some kind of check

        show zzrl grin

        RL "Oh my god, Shane, no! It's a movie! A classic! How have you not watched it on one of your million flights?"

        show zzsh wry

        SH "You know I mostly watch tape."

        show zzrl smile

        RL "I know, I'm just teasing. Though maybe the next time I'm back here, I'll make you watch it with me..."

        show zzsh hesitant

        SH "Er, I don't usually like animal movies."
        
        SH "And you {i}could{/i} come up again, if you want, but you don't have to? Maybe next summer...? Or really, we can meet in Montreal instead—"

        show zzrl resigned

        RL "I mean, I hope I don't have to come up again, but I think that's out of our control."

        SH "...what?"

        RL "Never mind! Bye Shane! {size=-8}For now..."
    
    else:
        show zzrl grin

        RL "That's okay, I actually saw a whole lot of {i}you.{/i} And Ilya. If you know what I mean."

        if freedom == 3:
            show zzsh hesitant

            SH "You...did?"

            show zzrl surprised

            RL "Yeah, I...huh."

            show zzrl thoughtful

            RL "Maybe I didn't, actually. I didn't actually see that much of you guys today, did I?"

            show zzsh frown

            SH "No, and I really am sorry about that—"

            show zzrl smile

            RL "Hey, no, it's fine! This is still one of the nicest holidays I've had in a while."

            show zzrl hesitant

            RL "And...and if tomorrow I'm back in LA—not that I'm trying to jinx it!—we can both do better about staying in touch, right?"

            show zzsh smile_blush

            SH "Yeah, definitely. It really was nice having you around, and...and getting to be with Ilya in front of other people."

            show zzrl grin

            RL "Oh, believe me, I know you how much you enjoy getting to be with Ilya in front of other people."

            show zzrl smile

            RL "Okay, I really gotta go. Love ya', talk to you soon, yeah?"

            show zzsh smile

            SH "Yeah. Thanks for being here, Rose, talk to you soon."

            jump end
        
        else:
            show zzsh embarrassed

            SH "Oh my god, I'm so sorry, I wasn't—"

            show zzrl smile

            RL "Hey, no, it's fine! This is still one of the nicest holidays I've had in a while."
            
            RL "I'm not even mad about having to do it all over again."

            show zzsh hesitant

            SH "...do it all over again...?"

            RL "Oh, I mean, I'm happy I got to see whatever amount of you I got to see, and I'd be happy to do it all again."

            show zzsh wry

            SH "If you did do it all again, I wish you got to see less of me, actually."

            scene bg ctdoor
            show zzsh wry
            show zzrl smile
            with pixellate

            show zzrl surprised

            RL "Whoa! What was that?"

            show zzsh hesitant

            SH "What...? I mean, I said, if you did it all again—"

            show zzrl thoughtful

            RL "...wait a second..."

            SH "..."
            
            SH "What are we waiting for...?"

            RL "Hmm..."

            RL "Never mind! Bye Shane! {size=-8}For now..."

    ##play audio
    "cardoor.mp3"

    jump airportout

label airportout:

    ## is the transition from previous scene too abrupt? need more car noise to indicate a drive?

    scene bg plane

    show zzrl flat
    with fade

    ## come back to this: need to add some kind of plane annoucement? seatbelt off? check during playtest if too abrupt

    RL "Well. That was...a day."

    if loop == 0:
        RL "I suppose it's not the silliest reason I've flown somewhere. Though I should pop an Ambien and sleep on the flight back to LA if I wanna be fresh for the shoot tomorrow."

    elif loop == 1:
        RL "Wonder if I'll dream of Shane's cottage again if I pop this Ambien. That would be kinda funny."

        RL "...Then again, what if I dream of tomorrow's shoot instead. Ugh. Subconscious, please do me a solid here and pick the fun dream."

    elif loop == 2:
        RL "...I should really try not taking an Ambien, this time."

        RL "Who cares about being fresh for the shoot tomorrow, as long as I manage to be {i}at{/i} the shoot tomorrow"
    
    else: ## should I add a few more loops of dialogue...?
        show zzrl resigned

        RL "And it's probably gonna be the same day again tomorrow."

    scene black
    with fade

    $ loop += 1

    jump start_real

label end:
    ## is the transition from previous scene too abrupt? need more car noise to indicate a drive?
    scene credits
    with fade

    #play music
    "ending.mp3 - though possibly an instrumental is better i dunno"

    RL "..."

    scene credits3

    if kissnow == True:
        $ pt += "sveta text1, "

        ##play audio
        "textping.mp3"

        RL "Siri, play voice note." ## yeah look i've never used siri in my life someone else fix this please

        SV "Hey Rose, this is Svetlana. I just wanted to say, I really did mean it about meeting up again if you're ever in Boston. Or if I'm in LA."

        SV "Or...or we could meet elsewhere too. I drove eight hours for Ilya, and I'd gladly travel more for you—I know we've only just met today, but somehow it feels like I've known you for much longer. I hope you feel the same."

        SV "Anyway, text me when you're back in LA. Fly safe."
    
    elif svetheart >= 4:
        $ pt += "sveta text2, "

        ##play audio
        "textping.mp3"

        RL "Siri, play voice note." ## yeah look i've never used siri in my life someone else fix this please

        SV "Hey Rose, this is Svetlana. I just wanted to say that I really enjoyed meeting you today. It's funny, even though we've only just met, I feel like I've known you for much longer. I hope you feel the same."

        SV "Anyway, text me when you're back in LA. Fly safe."
    
    else:
        RL "*humming*"

    scene credits
    pause 2.0

    scene credits4

    if shanemove == True:
        $ pt += "shane text1, "

        ##play audio
        "textping.mp3"

        RL "Siri, play voice note." ## yeah look i've never used siri in my life someone else fix this please

        SH "Hey, Rose, I was thinking. Some of the stuff you said earlier, about me moving to Ottawa, it..."

        SH "I dunno, Ottawa might not have the cap space in two years, and even if they do are they gonna want to blow it on another star centre when they already have Ilya, and fuck, the guys would flip, Montreal would flip, the MLH would flip—"

        SH "..."

        SH "I mean Ilya would probably flip too. In a good way. I think. Maybe. I dunno, I need to think about this more, and I should probably ask him, but..."

        SH "Fuck, I dunno. Call me when you've got the time? Yeah, and uh, have a good flight."
    
    elif shanesveta == True:
        $ pt += "shane text2, "

        ##play audio
        "textping.mp3"

        RL "Siri, play voice note." ## yeah look i've never used siri in my life someone else fix this please

        SH "Hey, Rose, I was thinking. Some of the stuff you said earlier, about Ilya, it..."

        SH "I'm gonna try to talk to Svetlana, I think. Ilya will probably be happy I want to talk to her, ugh, I don't know if he realises that we'd obviously talk about {i}him{/i}, but maybe he thinks we'll only say nice things. Hah, as if."

        SH "...I mean, I do have a lot of nice things to say about him. Svetlana probably does too. Ugh, I dunno, I should just be able to talk to Ilya and know if he's happy or not, but I guess we don't get to talk much, and..."

        SH "..."

        SH "Fuck, I dunno. Call me when you've got the time? Yeah, and uh, have a good flight."
    
    elif shanetea == True:
        $ pt += "shane text3, "

        ##play audio
        "textping.mp3"

        RL "Siri, play voice note." ## yeah look i've never used siri in my life someone else fix this please

        SH "Hey, Rose, I was thinking. Some of the stuff you said earlier, about the team, it..."

        SH "Like yeah, some of them probably aren't okay with...with the gay stuff...but we're still team, right? You don't have to like a guy to pass him the puck. They're fine in the room, like I said, no one's said anything to my face, so..."

        SH "...so they're probably saying it behind my back, aren't they? Fuck, it shouldn't matter, I don't know why it feels different to lie to them this year when I've always been lying to them, why did I even come out to them when—"

        SH "..."

        SH "Fuck, I dunno. Call me when you've got the time? Yeah, and uh, have a good flight."
    
    else:
        RL "*humming*"

    scene credits
    pause 2.0

    scene credits5

    RL "*humming*" ## TBD if you wanna do ilyahearts and have an ilya text here

    scene bg plane

    show zzrl flat
    with fade

    RL "Well. That was...a day. But I can't help feeling that maybe...maybe tomorrow will be a different day."

    RL "Well, if it's going to actually be tomorrow, I better take that Ambien and sleep as much as I can before tomorrow's shoot."

    scene black
    with fade

    Pilot "...we're making good time, and will be arriving at Los Angeles International Airport in approximately thirty minutes."

    scene bg plane
    with pixellate

    show zzrl flat

    RL "*Yawn*"
    
    Pilot "The local time is 6:25am, which means we are right on time. The weather in LA right now is..."

    show zzrl surprised

    RL "Oh my God, I'm in LA! I'm actually in LA! Holy shit, I made it!!"

    RL "..."

    RL "...wow, it's like I've looped back ten years of my life." ## ending is weak!! fix this unless the epilogue vibes allow for it to be weak iunno

    scene black
    with fade

    centered "This will be an achievement screen for the Player (actual achievement choices TBD making it maybe part of the gallery screen also TBD)! \n\n Svetlana badges: kissed Svetlana in your final loop - [kissnow], impressed her with your russian - [yayrussian] \n\n Shane badges: Shane starts thinking about moving to Ottawa - [shanemove], Shane is encouraged to talk to Svetlana about Ilya - [shanesveta], Shane thinks about how okay he is with his team's response to his coming out - [shanetea] \n\n Ilya badges: TBD  \n\n Other badges...??: How good is your Russian - [russian], how many times you've played Food Truck Kitty - [foodtruckkitty + foodtruckkitty2]"
    
    centered "{b}please screenshot this for playtest purposes{/b} \n\n your journey: [pt] \n\n total loops: [loop]"

    centered "this ends the game! thanks for playing!"

    return

