# The game starts here.
# code red! comment out all code red things on launch

label start:

    jump start_real 
    # code red uncomment the above for launch!

    menu:
        "For playtesting"

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
                
                "set number of times been outside with Svetlana after dinner":
                    $ outside = int(renpy.input("No. times been outside", allow="0123456789", length=2))

                    "Number of post-dinner Sveta convos: [outside]"

                    jump start

        "jump to a scene":
            menu:
                "start":
                    jump start_real

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

label start_real:

    ## these temp variables reset with every loop
    $ freedom = 0
    $ giftbought = ""
    $ papped = False
    $ svetheart = 0
    $ convincesvet = 0
    $ kissnow = False
    $ random = 0

    ## loop starts here

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

        RL "'--and I'm going to be maybe thirty minutes early! So excited to meet Ilya for real!'"

        ##play audio 
        "textsent.mp3"

        show zzrl resigned

        RL "Though I'm not sure Ilya's particularly excited to meet me..."

    elif loop == 1:
        RL "Ottawa? Didn't I get on the flight back to LA?"

        Pilot "...and thank you for flying with Air Canada."

        RL "Was...all of that a dream...?"
    
    elif loop == 2:
        RL "Ottawa? Oh my god, did I actually dream of Shane's cottage again??"

        Pilot "...and thank you for flying with Air Canada."

        RL "It feels too real to be just a dream...oh shit, is it the Ambien? That's one of the side effects, right? But I've never had such vivid dreams with Ambien before...?"

        RL "Shit, maybe I'm getting mutant powers of precognition. I guess seeing the future is better than turning blue...but why would I get Irene's power instead of my own...?"

        RL "No, wait, actually, it's more like Groundhog Day or something. Except if it's Groundhog Day, does that mean I'm a terrible person and I need to improve myself??"

        RL "Also, why would I be stuck in the day I'm going to Shane's cottage? ...oh no, am I supposed to get Ilya to like me??"
        
        RL "Fuck, guess I'm stuck forever."
    
    elif loop == 3:
        RL "...okay. Guess we can rule out the Ambien being the problem then."

        RL "So what {i}is{/i} the problem then...??"
    
    else:

        ## is this just pointlessly asking Rose to record more lines...? is it better to be sequentially different and then exactly the same for players to safely ignore?

        $ random = renpy.random.randint(1, 4) 

        if random == 1:
            RL "Guess we're doing this again..."

        elif random == 2:
            RL "Let's start from the very beginnning~ A very good place to start~"

            RL "If you read you begin with A, B, C~ If you're stuck in a time loop, sing with me~"

        elif random == 3:
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

            if giftshopvisit == 0:

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

            RL "Shane's not gonna be happy about this tomorrow...assuming there's gonna be a tomorrow..."

            RL "Hmm, where {i}should{/i} I go? I suppose I can still pick up my rental and drive around Ottawa--"

            Girl "Oh my god, is that Rose Landry??"

            ##play audio
            "phonecamera.mp3"

            RL "Damn it! Ah, well, fingers crossed there {i}isn't{/i} gonna be a tomorrow..."

            $ papped = True

    if loop == 0:
        RL "Now where's the car rental place... Ah, there we are!"
    
    elif loop == 1:
        RL "Now where's the car rental...oh, exactly where I thought it would be. Huh."
    
    else:
        pass

    jump ctdoor

label giftshop:

    if giftshopvisit == 1:
        RL "Let's see what they stock at...Otta-welcomes You? Really?"

        $ giftshopvisit += 1

    menu:
        "What are you buying?"

        "Vodka":

            $ giftbought = "vodka"

            "You've obtained vodka!"

        "Eye-wateringly expensive vodka":

            $ giftbought = "vodkaplus"

            "You've obtained expensive vodka!"

        "Roses":

            $ giftbought = "roses"

            "you've obtained roses!"

        "lilies":

            $ giftbought = "lily"

            "you've obtained lilies!"

    Cashier "Here's your receipt thank you for shopping at Otta-welcomes you have a nice day."

    menu:
        "Keep browsing?"

        "Yes":

            $ papped = True

            RL "Maybe I'll just keep looking--"

            Girl "Oh my god, is that Rose Landry??"

            ##play audio
            "phonecamera.mp3"

            RL "Damn it! Time to get out of here..."

        "No":
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

        RL "Matter of fact--oh, there's Shane's cottage, finally!"

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
        "play whatever actual music should be in this scene"

        RL "...if I didn't enjoy driving, this time loop would be actual hell."

        ##play audio
        "cardoor.mp3"

        scene bg ctdoor

        show zzrl flat
        with fade
    
    else:
        ##play music
        "play whatever actual music should be in this scene"

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
                    RL "Huh, can't believe I didn't find out about this before."

                    RL "But I do know that--yup, the door's unlocked."

                    jump bargein
                
                elif loop == 0:
                    pass

                else:
                    RL "Well, this didn't happen in my dream...I don't think..."

                show zzrl smile
                
                RL "Tsk tsk Shane Hollander! I was promised a fancy cottage with all the latest amenities! Better hope I don't leave a bad review on Airbnb."

                show zzrl surprised

                RL "Though the only visitor he gets probably doesn't bother with the doorbell, and just waltzes right in like--oh! The door's unlocked."

                jump entrance
            
            elif doorbell == 1 and loop == 1:

                $ doorbell += 1

                ##play audio 
                "click.mp3"

                RL "Oh, the doorbell's not working."

                RL "...Just like in my dream..."

                jump entrance
    
            elif doorbell == 1:

                $ doorbell += 1

                ##play audio 
                "click.mp3"

                RL "Still broken huh."

                RL "Guess I'm going in anyway."
            
                jump bargein

            elif doorbell == 2:

                $ doorbell += 1

                show zzrl resigned

                RL "Just going to...keep doing the thing that I know doesn't work, I guess."

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

                RL "Ugh, I didn't drive two hours just to wait out here with only this hypnotically ugly sculpture for company, maybe--oh! The door's unlocked."

                jump entrance
            
            elif knock == 0:

                $ knock += 1

                ##play audio 
                "knock.mp3"

                RL "..."

                if loop == 1:
                    $ pt += "knock, "

                    RL "The door was unlocked, in my dream, I wonder if--oh, it {i}is{/i}."

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

                RL "And then in my dream, I think...the door was unlocked, and--oh, it {i}is{/i} unlocked."

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

            RL "Next time, I swear I'm buying an airhorn at the gift shop." ## potentially add an air horn for lols

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

    SH "{size=-10}...there someone at the door??"

    IR "{size=-10}Thunder. Cat. Delivery. Ignore it."

    ##play audio 
    "knockloud3.mp3"

    SH "{size=-10}What? No, I think that's...{/size} {size=-5}There's someone at the door, is that--"

    $ freedom += 1

    scene bg ctentrance
   
    show zzsh flat at center
    show zzir flat at midright
    show zzrl flat
    with fade

    jump entrancepass

label bargein:
    
    $ bargecount += 1

    ## this part is purely for fun and can be edited away if it's not actually fun and is just making more work for Rose

    if bargecount == 1:

        RL "Hey guys! It's Rose! I'm early!"
    
    elif bargecount == 2:

        RL "Bitches in the HOUSE!!"
    
    elif bargecount == 3:

        RL "NO ONE EXPECTS THE LANDRY INQUISITION!"
    
    elif bargecount == 4:

        RL "Your moon~ Your moon and your man~"

        RL "Don't moon~ Don't moon me again~"
    
    elif bargecount == 5:

        RL "Incoming!!"

        $ bargecount = 1

    jump entrance
    
label entrance:

    if loop == 0:

        scene bg ctentrance

        show zzrl flat
        with fade
        
        RL "Oh geez, Shane, why do you have paintings of...mud smears?...in your doorway? Is this really the view you want to welcome visitors with--"

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

        RL "Oh shi--wait a second..."

    else:
        scene cut boys_doorway
        with fade

        RL "Hi Ilya, hi Shane, hi Shane's ass."

    IR "What?"

    SH "Wha--Rose! Fuck!"

    if loop == 0:

        RL "It's cool, all good, I'm closing my eyes, turning around, backing away--"

        scene black
        with pixellate

        ##play audio 
        "crash.mp3"

        scene cut boys_doorway
        with pixellate

        RL "Whoops, shit, what did I kick--is this a horse?? Oh, sorry, my eyes are open again--"
    
    elif loop == 1:

        RL "...very familar naked butts, too..."

        IR "What are you staring at."

        RL "Nothing! I'm, um--never mind, closing my eyes now!"
    
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

    IR "I was trying to, until {i}someone{/i} interrupted--"

    if loop == 0:
        show zzrl wink

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

    SH "What? You--wait, Rose, what are you even doing here? You're not supposed to get here until...another forty minutes?"

    if loop == 0:
        show zzrl grin

        RL "Yeah, sorry, my flight got in early. I tried texting you but I guess you were...otherwise occupied."

        show zzir smirk

        IR "Yes, Shane's beautiful ass was about to be otherwise occupied by my--"

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

        SH "Sorry, I know I've been... It's just, with Ilya being in Ottawa, and--"

        show zzrl grin
        
        RL "Babe, no, don't apologise! I know you guys don't get much time together, so actually {i}I{/i} should be thanking {i}you{/i} for letting me come up here and interrupt your...alone time."

        show zzsh embarrassed

        SH "Oh my god, stop, it's--whatever. Anyway, Ilya's best friend is coming by for dinner too, so it's only fair."

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

        RL "But hey, it's not so bad. Lots of worse places to be, lots of worse people to see."

        SH "Haha, yeah, I suppose. Anyway, Ilya's best friend is coming by for dinner too, so it's only fair."

        RL "Yes, Svetlana's coming too, I know."

    show zzir eyebrow

    IR "You know Svetlana?" ## should it be Sveta here?

    if loop == 0:
        menu:
            "Yes":
                pass

            "No":
                pass

        RL "Well, not personally. But sometimes hockey media will talk about you two and...ah..." ## 'hockey blogs'...? press? paps??

        show zzir scowl
        show zzsh frown

        SH "Well, obviously she and Ilya aren't--"

        show zzrl hesitant_blush

        RL "Oh, no no, of course not, I just meant--never mind. Sorry."
    
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
        
        RL "Yes--I mean, no, I--I mean, maybe...?"

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

                IR "What do you mean. You read a lot of paparazzi bullshit about her or something?"

                RL "No, no, if only my sources were that mundane."
            
            "No":
                $ random = 11

                show zzrl thoughtful

                RL "Can anyone ever truly know another person?"

                SH "Um. Yes?"

                RL "If you get to know someone a hundred times, but they never get to know you back, does it still matter?"

                IR "...yes."

    SH "Uh. Okay. That's..."
    
    SH "You know what, never mind. Why don't I, um."
    
    SH "I should show you around."

    show zzir eyeroll

    IR "Show her around? For what? She's not even staying here tonight."

    show zzsh annoyed

    SH "{i}Ilya.{/i} It's polite, okay? We're going to be polite."

    menu:
        "Agree to the house tour":

            if papped == True:
                show zzrl smile
                
                RL "Thanks Shane, I'd love a tour of the cottage. This place is--"

                jump paptalk

            if tourloop == 0 and notourloop == 0:

                show zzrl hesitant

                RL "Thanks Shane, I'd love a tour of the cottage. It's bigger than I thought it would be!"

            elif tourloop == 1 or notourloop == 1:

                show zzrl thoughtful

                RL "Thanks Shane, I'd love a tour of the cottage. It's...exactly as big as I thought it would be."

            else:
                show zzrl smile

                RL "House tour, right, cool, let's go! Tell me all about your sexy hardwoods and exposed beams."

                show zzsh hesitant

                SH "...okay, let's. Do...that."

                jump housetour
            
            show zzir smirk

            IR "{size=-10}...that's what he said...before we were rudely interupted by--"

            SH "Ilya, for fuck's sake--go do dinner prep or something! I'm going to show Rose around."

            IR "Oh, now I can dinner prep myself? Yesterday, it's 'Ilya, too much salt, not good for your heart' and 'Ilya, that's not how the stove works, you will burn the cottage down', and today Rose Landry is here and I am allowed in the kitchen all by myself?"

            show zzsh smirk

            SH "Yes, and if you burn the cottage down I'm making you sleep on the ashes of the couch."

            show zzir smirk

            IR "I've slept in more terrible places because of you. Like that time in--"

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
                RL "Maybe Ilya's right, there's no need. Let's sit, have a drink--"

                jump paptalk

            RL "Maybe Ilya's right, there's no need. Let's sit, have a drink, get to know each other!"
            
            if giftbought == "vodka": ## rejig this once the gift stuff is finalised

                RL "Oh, I bought vodka for you guys?"

                show zzir eyeroll 

                IR "Tch, is this the cheap stuff from the airport gift shop? Would rather drink well water."

            elif giftbought == "vodkaplus":

                RL "Oh, I bought vodka for you guys?"

                show zzir eyeroll 

                IR "Tch, expensive vodka is not always good vodka. Clearly money cannot buy good taste."

            ## elif giftbought == "roses": ## cut these?

                ## "rose: oh I bought roses for you two"

                ## "ilya is sooooo gonna be soooo grumpy and passive aggressive about this one"

            ## elif giftbought == "lily":

                ## "rose: oh I bought lilies for you shane! because, hehe, you know..."

                ## "shane is blushy, ilya is begrudgingly accepting of flowers that will remind shane of him at all times"

            else:

                RL "Oh, I brought wine!"

                show zzir eyeroll

                IR "Think I will need something stronger than wine for this..."

            jump teatime

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

    RL "Oh, that's...I mean, I know the Centaurs aren't doing great, but there's, um, potential, right? And...and now they have you, and--"

    show zzir eyeroll

    IR "Yes, now they have me, soon I will be playing full sixty minutes and I will win Ottawa the first cup in twenty years all by myself."

    show zzsh frown
    
    SH "Ilya."

    show zzir smirk

    IR "Oh, you think I cannot play full sixty minutes if I want, Hollander? You doubt my endurance? Because--"

    show zzsh eyeroll

    SH "No one can play the full sixty minutes, asshole."

    IR "--I can prove my endurance to you, right now, if you kick Rose Landry out again--"

    return

label teatime.shane:
    show zzrl hesitant

    RL "So, Shane, how are things? You said you guys were thinking of coming out to your teams, did you think about it some more...?" ## too direct..?

    show zzsh frown

    SH "Oh, um, yeah, I told my team a few weeks after I told you about Ilya. I didn't say...?"

    show zzrl surprised

    RL "No you did {i}not{/i} say! Wait, so they know you're with Ilya?"

    SH "Oh, no, no, fuck no. They just know--I just told them that I was. You know."

    show zzrl hesitant

    RL "Gay...?"

    show zzir smirk

    IR "Super gay."

    show zzsh annoyed

    SH "A totally normal amount of gay, Rozanov, fuck you."

    show zzrl grin

    RL "I think being gay is kinda like...oh, liking chocolate. There's not really a normal amount, you just like what you like."

    show zzir eyebrow

    IR "...And how much do you like chocolate, Rose Landry?"

    show zzrl surprised_blush

    RL "Oh, haha, I mean, we're not talking about me!"

    show zzrl smile

    RL "So, hey, how did it go? You thought some of them would be good about it, right?"

    show zzsh hesitant

    SH "Yeah, I mean, some of them have been alright. And some of them...I mean, look, no one's really said anything to me about it."

    show zzir scowl

    IR "You said everything was fine."

    show zzsh frown

    SH "It {i}is{/i} fine. It's good that no one's said anything, right? I didn't want it to distract from the hockey."

    show zzrl hesitant

    RL "But not everything is about the hockey, though...?"

    show zzir eyeroll

    IR "Not everything is about the hockey? Rose Landry, this is the first time you are meeting Shane Hollander? Let me introduce you to the second best player in the league--"

    show zzsh wry

    SH "Shut up, Rozanov. Look, I know not everything's about hockey, okay?"

    show zzsh frown
    
    SH "It's just. These guys are my team. As long as the hockey's still working, that's the most important thing."

    show zzrl hesitant

    RL "But that's...I mean, what about You Can Play? Didn't some of the Metros join that...? I saw JJ Dagenais did, and Hayden Pike--"

    show zzir smirk

    IR "As if Pike can play. He probably wishes he were gay so that someone will finally say to him--"

    show zzsh annoyed

    SH "Oh, fuck off, Rozanov, Hayden was good about it, okay? I mean, at least until I told him about--"

    return

label teatime.sveta:
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

    show zzsh wry_blush

    SH "I mean, technically we're both in the MLH, so really--"

    show zzir smirk

    IR "We're both in the same league, yes. But also--what is the thing the media says? In our own league?"

    show zzsh smirk

    SH "In a league of our own."

    IR "Yes. We are in a league of our own. Should play against each other only, and not have to play in the same league as dinosaurs like Scott Hunter. Hockey should be for humans--"

    SH "Sure, Rozanov, you can take it up with the commissioner."

    show zzsh smile_blush

    SH "Ah, sorry, Rose, you were asking about Svetlana. Like I told you, she's Ilya's best friend. She lives in Boston, but visits Moscow a lot."

    show zzsh frown

    SH "And Ottawa too. She visits Ottawa a lot too, now. More than I do, probably."

    SH "Which is good. It is. It's--"

    show zzir hesitant

    IR "Sveta also likes the dumb toys she had when she was small. Noisy wind-up things, little animals. Too sentimental to throw them out even after they break."

    IR "Probably why she still likes me, okay?"

    show zzsh frown

    SH "You're not broken--"

    show zzir eyeroll

    IR "Okay, okay, so you are the noisy toy, not me. So she will like you too."

    show zzir smirk

    IR "Very easy to wind up, very fun to play with, like a little animal in--"

    show zzsh annoyed_blush

    SH "{i}Ilya{/i}"

    ##play audio
    "knockloud2.mp3"

    show zzsh flat

    SH "Oh! That's probably her now."

    $ svet_fact2 = True

    jump svet_entrance

label grind_french:

    scene bg room2
    with fade

    "rose spends a couple hours studying french"

    $ french += 1

    if french <= 2:
        "your french is still not great"

    elif french <= 4:
        "your french is getting better!"

    else:
        "duolingo can't get you any better at french! which doesn't necessarily your french is amazing, but it's as good as you're going to get"

    if time == 1:
    
        "rose notices it's time for dinner. she exits the room, walks down the hallway, and gets a faceful of hollanov making out in some alcove"

        scene cut hollanov4
        with fade

        "rose, backing away slowly: Putain de merde!"

        jump dinner_late
    
    else:

        "rose notices it's getting late. she exits the room, walks down the hallway, and gets a faceful of hollanov making out in the room next door with the door open"

        scene cut hollanov4
        with fade

        "rose: really, guys?"

        jump leaving

label grind_hockey:

    scene bg rink
    with fade

    if time == 1:
        "rose spends a couple hours playing hockey. at some point ilya drags shane away to do pre dinner prep or whatever, but rose keeps at it"
    else:
        "rose spends a couple hours playing hockey."

    $ hockey += 1

    if hockey <= 2:
        "your hockey is still not great"

    elif hockey <= 4:
        "your hockey skills are getting better!"

    else:
        "no matter how much hockey you play, you don't seem to gain any muscle or muscle memory, so this is probably as good as you're going to get"
    
    if time == 1:
        "rose notices it's time for dinner. she exits the room, walks down the hallway, and gets a faceful of hollanov making out in some alcove"

        scene cut hollanov4
        with fade

        "rose, backing away slowly: now that's a man in the crease"

        jump dinner_late
    
    else:
        "rose notices it's getting late. she exits the room, walks down the hallway, and gets a faceful of hollanov making out in the room next door with the door open"

        scene cut hollanov4
        with fade

        "rose: really, guys?"

        jump leaving

label housetour:

    scene bg room1

    show zzsh flat at center
    show zzrl flat
    with fade

    SH "...and this is one of the two guest rooms on this floor. The bigger guest room is downstairs, but all three have their own TV, king-sized bed, and en-suite bathroom."
    
    SH "This room's got east-facing windows, though, so it gets a lot of sunlight in the mornings. And it's got a great view of the lake."

    show zzrl grin

    RL "Wow, Shane, Ilya's right, you really are Mr Real Estate!"

    show zzsh embarrassed

    SH "Oh, sorry, I guess you don't really need to know all this stuff. I mean, like he said, you're not staying over, so who cares about the guest rooms?"

    menu:
        "Continue the house tour":
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

            ## ask about why not the montreal appartment? and shane can be like, oh that place is chosen for hockey. and rose can point out this house is like the antithesis of a hockey rink

            SH "I...yeah. Thanks, Rose. I love it too."

            if svetpass >= 1:

                menu:
                    "Ask Shane about curtains":
                        $ room1blind = True
                        
                        show zzrl grin

                        RL "Though I gotta say, with all the windows and no curtains? It's got the vibes of like, you love sunlight, sure, but you also love exhibitionism."

                        show zzsh embarrassed

                        SH "{i}Rose{/i}, what, I don't--I mean, this house has blinds! On all the windows!"

                        show zzrl eyebrow

                        RL "Really? Where?"

                        SH "It's, there's a remote, it's in this, uh..."

                        RL "Chunk of half-melted legos?"

                        SH "Artistic...container. It opens like...this?"
                        
                        SH "No, wait, you turn {i}this{/i} bit...and then you press {i}that{/i}..."

                        RL "Oh, it's a puzzle box?"
                        
                        SH "...I don't think it's meant to be. The interior designer said--{i}aha!{/i} Here!"

                        RL "Well, at least the remote looks normal. I assume it doesn't make anything in here explode or--"

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
                "Ask to see the other small guest room":
                    scene bg room2

                    show zzsh flat at center
                    show zzrl flat
                    with fade

                    RL "Okay, we've gone from way too much going on to way too little. This room just has a bed...? Excuse me, what happened to the TV and bathroom I was promised?"

                    SH "Oh, it's all hidden. You wave your hand over this panel here--" ## add a {nw} after voice is added...?
                    
                    ##play sound
                    "switch.mp3"

                    SH "--and the TV slides down from the ceiling. And you wave your hand {i}here--{/i}"

                    ##play sound
                    "switch.mp3"

                    RL "Whoa! I didn't know there was a door there! Oh, that's where the bathroom is!"

                    SH "Yeah, everything's hidden because of the minimalist aesthetic, apparently. The panel for the bathroom lights and floor heating is all hidden near the door here too."

                    if svetpass >= 1:

                        menu:
                            "Ask Shane about curtains":
                                $ room2blind = True
                                
                                RL "Any chance there's curtains hidden too? Cause I gotta say I'm feeling a little exposed in here, if you know what I mean."

                                show zzrl grin

                                RL "Which, hey, maybe that's also meant to be part of the aesthtic, I dunno what you or your guests get up to in the privacy of--"

                                show zzsh embarrassed

                                SH "Oh my god, Rose, I don't--there's blinds! They're just hidden!"

                                SH "You wave your hand over this panel near the bed and--"

                                ##play sound
                                "switch.mp3"

                                show zzsh wry

                                SH "--and look, all the privacy you want."

                                RL "Fun! Although having a motion sensor so close to the bed that might accidentally bring the blinds up and down--"

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

                    RL "Hate to break it to ya', pal, but white is not a colour--"

                    $ shane_room2 = True

                "Ask to see the big guest room":
                    scene bg room3

                    show zzsh flat at center
                    show zzrl flat
                    with fade

                    RL "This one has much more normal decor, I have to say."

                    SH "Yeah, I built this one for my parents. That's why there's two walk-in closets."

                    if svetpass >= 1:

                        menu:
                            "Ask Shane about curtains":
                                $ room3blind = True

                                show zzrl grin
                                
                                RL "Any chance you thought they might want curtains too?"

                                SH "Oh, yeah, there's a remote for the blinds behind the lamp here."

                                show zzrl thoughtful

                                RL "Gotcha. You know, I can't help noticing that this place is completely different from your place in Montreal. I mean, sure, it's an apartment in the city instead of a mansion out by a lake, but..."

                                SH "I guess I mainly picked my apartment in Montreal for how close it is to the rink and how good the security is. It's not like I spend much time there."

                                show zzrl eyebrow

                                RL "You don't spend much time...in the place that you live for most of the year...?"

                                SH "I mean, most of the season, if I'm not at the rink, I'm at the gym, or asleep. And it's not like I have to host the team, cause Hayden does that."

                                SH "Montreal is for hockey, right? The summer, this cottage, is for me."

                                show zzrl hesitant

                                RL "Oh, Shane, babe, that's--"

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

                    SH "That's not--Rose!"

                    RL "Or maybe I should say, what sort of wild, noisy things do you think you're gonna get up to while your parents stay in your guest room?"

                    SH "Oh my god, I just thought they might not want to be disturbed if I have to wake up in the middle of the night for a glass of water, that's all! I wasn't even thinking of Ilya when I designed this place!"

                    show zzrl grin

                    RL "Hey, I didn't say anything about Ilya, I just--"

                    $ shane_room3 = True

        "Stop the house tour":
            $ pt += "fake house tour, "

            if notourloop == 0:
                $ notourloop += 1

                RL "I promise, I do care, I think it's cool that you were so involved in designing every inch of this cottage, y'know?"

                RL "I just also care about {i}you{/i}."

                SH "What?"

                RL "How are {i}you{/i}, Shane? I want a tour of the interiority of Shane Hollander, not just his cottage."

                show zzsh smirk

                SH "I dunno, I don't think Ilya's gonna like me giving you a tour of my interior..."

                show zzrl grin

                RL "Oh my, Shane Hollander! I mean, what if it turns out that I prefer being the peg to the--"

                show zzsh embarrassed

                SH "Rose Landry! You do not! ...do you??"

                RL "Maybe, maybe not, but I don't wanna talk about me today. I wanna talk about my best friend, who I haven't talked to in {i}ages{/i}."

                show zzsh hesitant

                SH "Ah, sorry, I know I haven't been the greatest at keeping in touch. It's just, this year's been... With Ilya in Ottawa..."

                show zzrl wink

                RL "You're spending all your free time driving two hours for a booty call with the new boyfriend?"

                show zzsh embarrassed

                SH "No!"

                show zzsh smile_blush

                SH "I mean, sort of."

                show zzrl smile

                RL "Hey, it's great you're enjoying the honeymoon period, even if it's a little bit long distance, right?"

                show zzsh hesitant

                SH "I...yeah, I guess. I mean, I {i}am{/i} enjoying it, seeing Ilya sometimes, but--"
            
            elif notourloop == 1:
                $ notourloop += 1

                show zzrl smile

                RL "I promise, I do care about your cottage, I just also care about {i}you{/i}."

                show zzrl hesitant

                RL "This is gonna sound strange, but it feels like no matter what I do, I don't get much time to talk to you one-on-one, y'know?"

                show zzsh hesitant

                SH "Ah, sorry, I know I haven't been the greatest at keeping in touch. It's just, this year's been... With Ilya in Ottawa..."

                show zzrl wince

                RL "No, hey, don't apologise, that's not what I meant--"

                show zzrl hesitant

                RL "Never mind. Actually, speaking of Ilya. Oh boy, how do I ask this..."

                RL "How do I make him like me...??"

                show zzsh frown

                SH "Uh..."

                SH "Make him like you...?"

                show zzrl resigned

                RL "Yeah. Look, I know it's totally normal to hate your boyfriend's ex, but I'm not just your ex, I'm your friend, right?"

                SH "You are. You're one of my best friends."

                show zzrl smile

                RL "Right! Same back at you!"
                
                RL "And usually that's good enough for me, I don't need to be besties with all my besties' boyfriends, but...there's extenuating circumstances that I can't explain without sounding crazy."

                RL "So. Coach, what's the play here, what should I be doing to try to make Ilya like me?"

                show zzsh embarrassed

                SH "Hah, I wish I knew."

                show zzsh hesitant

                SH "I mean, it's...it's nice that you want to. You've been the only one I've told about Ilya who's been...been completely positive the whole time. And that's. Really nice."

                SH "So I also want him to like you. But I have no idea how I even made him like {i}me.{/i}"

                show zzsh smile_blush

                SH "I mean, I have some idea, but I don't think that's something you should be, uh, attempting with my boyfriend--"

                show zzrl grin

                RL "Shane Hollander, you mean to say you think the only way to your boyfriend's heart is through his dick?"

                show zzsh wry

                SH "Not the only way! But he and his best friend used to sleep together, so that's not--I mean, I guess so did we, so maybe I shouldn't--"

            else:
                "loop 2 onward stuff here"
            
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
        Meg "Rose. Why is the internet telling me that you're at a secret rendezvous with Shane Hollander at his private residence in Ottawa and that you guys are getting back together and it's breaking the heart of your costar who you've apparently been secretly dating up until now?"

        show zzrl surprised

        RL "What! I am not!"

        Meg "Oh good, so you're not in Ottawa? You're haven't seen Hollander?" ## check canada/show beta -- is it stated that the cottage is in Muskoka, ON? Nearest airport is 2h?

        show zzrl resigned

        RL "...Well. I mean. I am at Shane's cottage, and I have seen Shane. But platonically! As friends!"

        Meg "Yeeeeah. You still want us to firmly deny all rumours about you two, right? Cause I gotta say, it's not bad press--"
        
        show zzrl flat

        RL "Deny, please. Shane doesn't like them."

        Meg "Well, then we better figure out how to get you safely--and more importantly--{i}secretly{/i} evacced outta Ottawa."

        show zzrl resigned

        RL "Right, fine, yes, thank you. I drove up here from the airport in a rental, and I have a flight back to LA at--"

        Meg "Nope nope nope. Firstly, you're going nowhere else in that rental, it's been made."

        RL "Alright. I could...get Shane to drive me out in one of his--"

        scene cut boys_inside ## you could have a different cut scene for this
        with fade

        RL "..."

        RL "Never mind. What if you arrange for someone to drive out to meet me, we could swap cars--"
    
    else:
        Meg "Rose. Why is the internet telling me that you're at a secret rendezvous--"

        show zzrl resigned

        RL "--with Shane Hollander at his private residence in Ottawa and we're getting back together, I know."
        
        Meg "You are?? What happened to deny, deny, deny??"

        RL "No, no, we're not getting back together, we're still just friends. I fucked up and got spotted at the airport. Should have known better..."

        scene cut boys_inside ## you could have a different cut scene for this see above
        with fade

        RL "..."

        RL "I {i}really{/i} should know better about a lot of things, at this point."

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

    IR "С каких это пор ты стучишься?" ## check russian "since when do you knock"

    SV "Поскольку я собираюсь посетить дом вашей Джейн, а не ваш." ## "since I'm visiting your Jane's house. Which is not yours"

    show zzir scowl

    IR "Sveta." ## should this be in cyrillic

    show zzsh hesitant

    SH "Um, it's nice to meet you, Svetlana. Прия́тно... позна... ко́миться...?"

    show zzsv surprised

    SV "Oh, my. Is Ilya teaching you how to be polite? I didn't know he knew how."

    show zzsh embarrassed

    SH "I'm learning from Duolingo, actually."

    show zzsv amused

    SV "Tch, Duolingo. Why talk to that cursed owl when you have your very own Russian tutor?"

    show zzir smirk

    IR "Because when I'm with him, usually his mouth is too busy to--"

    show zzsh annoyed_blush:
        ease 0.1 xoffset 100
        ease 0.1 xoffset 0
    with hpunch ## possibly hpunch is too much we shall see

    SH "Shut it, Rozanov."

    show zzsv smile

    SV "Well, мне тоже приятно познакомиться, {i}Jane{/i}. I've wanted to meet you for the longest time."

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

        "Прия́тно позна ко́миться":

            if svet_fact1 == True: ## come back to this
                RL "Прия́тно позна ко́миться, Svetlana"

                $ svetheart += 2
            
            else:
                $ svetheart += 1

                RL "Прия́тно, um, по..."

                show zzir eyeroll

                IR "And I thought Shane was bad. You do not have the mouth for Russian, Rose Landry."

                show zzsv flirty

                SV "Though perhaps you could, if you have a good teacher. I'm always happy to be of service."

                show zzrl surprised_blush

                RL "Oh, haha, thanks...? And, um, please just call me Rose."

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
        
        "even more deranged convo unlock" if loop >= 4:

            "rose says an even more deranged time loop related thing. everyone nods along, slightly more hesitantly."

            "could also rotate a variety of deranged things for rose to say in this option, which is more things to record but potentially funny"

    IR "Sveta, you brought the good vodka, yes?"

    SV "It's in the car, with all my bags."
    
    IR "...All your bags? How many bags is 'all'? You know you're staying only one night, you're leaving tomorrow."

    SV "I barely got here and you're already telling me to leave? Fine, maybe I'll bring my good vodka home with me."
    
    SV "And also all the frozen pelmeni from Evgenia Mikhailovna, which she made me bring up in a cooler all the way from Boston for her dear Ilyushenka, who--" ## check russian. also pelmeni...?

    show zzsh frown

    SH "Wait, who is this? Who is sending Ilya pelmeni?"

    show zzir scowl

    IR "Okay, shut up, I will go get all your bags now. It can be my training for today."

    show zzsh eyeroll

    SH "Unless each of her bags is 300lbs, it's {i}not{/i} going to count as your training for today." ## check canadian units

    show zzir flat

    IR "Yes, exactly."

    show zzsh eyeroll

    SH "Her bags are not 300lbs each, Rozanov."

    show zzir smirk

    IR "Oh, so you know how heavy Sveta's bags are? You have magic psychic powers now?" ## check russian address

    show zzsh smirk

    SH "I don't need psychic powers to know that her bags are--"
    
    IR "You think her bags are so light, why don't we see how many reps you can bench press them--"

    SH "At least one more rep than you, asshole, that's how many reps--"

    hide zzir
    hide zzsh
    with easeoutleft

    show zzsv unimpressed

    SV "..."
    
    SV "...If they break something trying to bench press my bags, I will break both their heads."

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
            $ svetheart += 1

            show zzrl smile_blush

            RL "Oh, maybe I could show you around the cottage...?"

            RL "Since you're staying the night, I could show you some of the guest rooms?"

            show zzsv flirty

            SV "Mm, yes, you're welcome to show me to any room in this house, Rose, any room at all."

            jump housetour2

        "Offer to let Svetlana relax alone":
            $ pt += "alone 1, "

            RL "Oh, did you drive up all the way from Boston? You must be so tired! If you want to rest and recharge by yourself...?"

            show zzsv smile

            SV "Ah, yes. That's very thoughtful of you, perhaps I'll find a room to take a nap in. See you at dinner, Rose."

            hide zzsv with easeoutright

            if loop <= 1:
                scene bg sunroom

                show zzrl resigned
                with fade

                RL "Right. I guess I could kill some time before dinner checking my email. And reading the script that Megan thinks I should audition for. Oh, shit, and there's the Bulgari contract I was supposed to look through too." ## Megan...??

                show zzrl hesitant

                RL "Or maybe I'll read--what is this--Hockey: A Global History...?"

                show zzrl wince
                
                RL "Really, Shane? This is your idea of a coffee table book? ...Maybe I'll just play some Food Truck Kitty." ## workshop this. marval snap? could transition with an image of the game

                $ foodtruckkitty += 1

                scene cut game
                with fade

                RL "...noooo, why won't Dragon Tabby triple-heart my Sunday Special? I know it likes lettuce and salmon!"

                scene bg sunroom

                show zzrl
                with fade

                RL "Ugh, maybe I should stop playing, how long have I been--"

                scene cut boys_outside4
                with fade

                RL "Whoa! Right in front of Dragon Tabby's salad?"

            elif clearemail == 0:

                scene bg sunroom

                show zzrl resigned
                with fade

                RL "Right. I guess I could kill some time before dinner checking my email--"

                show zzrl hesitant

                RL "--Wait, what if all this has been the universe's way of telling me to work harder? I know told Megan yesterday I'd clear my email inbox, but surely that's, like, too petty a thing to cause...all this..."

                show zzrl wince

                RL "Okay. Fuck. Just in case. Let's read some emails."

                scene bg sunroom

                show zzrl resigned
                with fade

                RL "...what, no, I'm not showing my bare ass on screen for an Victoria's Secret ad, isn't the whole point of Victoria's Secret to cover up my ass?"
                
                RL "Ugh, my eyes are crossing, how long have I been--"

                scene cut boys_outside4
                with fade

                RL "...Now there's an ass that needs covering up."

                $ clearemail += 1
            
            else:
                scene bg sunroom

                show zzrl resigned
                with fade

                RL "Well, clearly there's no point trying to work. Time to figure out the way into Dragon Tabby's triple-heart, once and for all."

                scene cut game
                with fade

                if clearemail == 1:
                    RL "Curse you, RNGesus, why won't you let Dragon Tabby like me?"
                
                    RL "...is this the message from the universe, that no matter what I do, there's some things I can't change...??"

                elif clearemail == 2: ## extraneous? is anyone going to even see these or care??
                    RL "Still can't win Dragon Tabby's triple heart, but it's not going to stop me trying since I'm having fun."
                    
                    RL "...Maybe that's the message I'm supposed to learn from the universe."
                
                else:
                    RL "Here, kitty kitty kitty..."

                scene bg sunroom

                show zzrl flat
                with fade

                RL "Wow, okay, my eyes are crossing, I need to--"

                scene cut boys_outside4
                with fade

                RL "...I need to learn to keep my eyes closed, clearly."

                $ clearemail += 1

            RL "..."

            RL "Okay, they're still going. Maybe it's time to go find Svetlana, it's gotta be almost dinner time."

            jump dinner

label housetour2:
    $ pt += "sveta tour, "

    scene bg room2

    show zzsv flat at center
    show zzrl flat
    with fade

    if room2blind == True:
        menu:
            "close the blinds?"

            "yes":
                "just close the blinds -- there was an additional puzzle layer here, dunno if we actually need it"

                jump blindsclose

                "now, where's that pesky remote?"

                menu:
                    "in the drawer":
                        "nope, it's not there"

                        "svetlana is like, what on earth are you doing? shamefaced, you're about to continue the housetour--but too late!"

                        scene cut hollanov2b
                        with fade

                        "well, you tried"

                        jump dinner

                    "next to the door":
                        "indeed, there it is!"

                        jump blindsclose

                    "beside the lamp":
                        "nope, it's not there"

                        "svetlana is like, what on earth are you doing? shamefaced, you're about to continue the housetour--but too late!"

                        scene cut hollanov2b
                        with fade

                        "well, you tried"

                        jump dinner
            
            "no":
                pass   
    
    else:
        pass

    if svet_tour == 0:
        RL "So...here's a guest room! I think Shane said they all have an en-suite and a king bed."
    
    else:
        RL "...and next, on our totally normal house tour, is this totally normal guest room, with an en-suite and a bed that may or may not be a king."

    SV "A king? Hmm. Certainly this bed could fit two people, if it was you and me, but..."

    if svet_tour == 0:
        show zzrl surprised_blush

        RL "Oh! Um, you and me...?"
    
    else:
        show zzrl smile_blush

        RL "Oh? If it was you and me...?"

    show zzsv amused

    SV "What I mean is, if it was two regular sized women like us instead of, say, two massive hockey players, we could fit comfortably in this bed. But I don't think that makes it a king."

    SV "Though perhaps if it {i}was{/i} you and me, we could fit comfortably in an even smaller bed than this."

    if svet_tour == 0:
        show zzrl smile_blush

        RL "Oh, right, haha, maybe! Um, good thing this is just the guest room then, and not Shane and Ilya's room!"

        show zzsv smile

        SV "Yes, good for them. Now, where is this en-suite...?"
    
    else: ## come back to this if it makes sense to add a flirt/not flirt option here
        show zzrl grin_blush

        RL "I guess there's only one way to find out."

        show zzsv surprised

        SV "Well. {i}Perhaps{/i}."

        show zzsv smile

        SV "But before we start searching for smaller beds to test our hypothesis, we should search for the en-suite. I was promised one, and yet I do not see it?"

    if shane_room2 == True:

        $ svet_room2 = True
        $ svetheart += 1

        RL "The en-suite--oh, that's right, this room has a hidden door right...here! Voila!"

        ##play sound
        "lightswitch.mp3"

        show zzsv amused

        SV "Magic! Will you pull a rabbit out of a hat next?"

        show zzrl grin_blush

        RL "No hat, but I could pull a rabbit out of my suitcase. If you know what I mean." ## cut the if you know what I mean...? or use it more to make it a rose thing

        show zzsv flirty

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

        RL "Oh, haha, thank you. Um, if you've enjoyed the service, please leave a good review at the end of your trip, Ma'am."

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
        "Show Svetlana the other guest room on this floor":
            scene bg room1

            show zzsv smile at center
            show zzrl smile
            with fade

            if room1blind == True:
                menu:
                    "close the blinds?"

                    "yes":

                        "just close the blinds -- there was an additional puzzle layer here, dunno if we actually need it"

                        jump blindsclose

                        "now, where's that pesky remote?"

                        menu:
                            "in the drawer":
                                "indeed, there it is!"

                                jump blindsclose

                            "next to the door":
                                "nope, it's not there"

                                "svetlana is like, what on earth are you doing? shamefaced, you're about to continue the housetour--but too late!"

                                scene cut hollanov2a
                                with fade

                                "well, you tried"

                                jump dinner

                            "beside the lamp":
                                "nope, it's not there"

                                "svetlana is like, what on earth are you doing? shamefaced, you're about to continue the housetour--but too late!"

                                scene cut hollanov2a
                                with fade

                                "well, you tried"

                                jump dinner
                    
                    "no":
                        pass

            if shane_room1 == True:

                $ svet_room1 = True
                $ svetheart += 1

                RL "Now, this room is decorated in the post-modern style, which we hope will be more to your taste, Ma'am, so please enjoy your stay."

                show zzsv amused

                SV "Really. This is the room you think will be more to my taste."

                show zzrl smile

                RL "Haha, I mean...not really. You don't look like a post-modern kinda person."

                SV "No?"

                show zzrl thoughtful

                RL "Well, your style seems more elegant and understated? Shimmery metallics and classic cuts instead of bright pops of colour. Not that fashion style necessarily reflects interior decor preferences, but..." ## i know nothing about clothes and even more nothing about art, help

                SV "Mm. You've been paying attention to me."

                show zzrl hesitant_blush

                RL "Oh, well, sorta...? Mostly I was paying attention to Ilya, but I couldn't help noticing you."

                show zzsv eyebrow
                
                SV "To Ilya?"

                show zzrl thoughtful
                
                RL "It's just...when Shane told me he was dating Ilya, I looked him up--I mean, obviously I already knew who Ilya was, anyone who follows hockey does, but I wasn't really paying attention the same way, y'know?"

                show zzsv eyebrow

                SV "And what way is that?"

                RL "In a...a concerned best friend kind of way, I guess."

                show zzsv thoughtful

                SV "Yes. I understand exactly the way you mean."

                show zzrl surprised

                RL "Oh, you do? But Shane is...ah, that is, Ilya's reputation is more..."

                show zzsv eyebrow

                SV "What about his reputation?"

                show zzrl hesitant_blush

                RL "Oh, well, it's just that...actually, you know what, never mind. Obviously they're both different from how the media portrays them. Sorry."

                show zzsv thoughtful

                SV "Yes, they are. And so are you, I think."

                show zzsv smile

                SV "Anyway, you were just about to tell more about this room, yes?"

                show zzrl hesitant_blush

                RL "Right! Um, as you can see, this room gets a lot of natural light, and a gorgeous view of--"
            
            else:
                RL "And this room is also a guest room, I think, and is...uh.."

                show zzrl surprised

                RL "Wow."

                show zzsv eyebrow

                SV "There is a lot of...post-modern sculptural pieces, shall we say...on the walls."

                RL "{size=-10}Shane, why?"

                show zzrl hesitant

                RL "Well! Good thing this room has more windows than walls! Lots of natural light, and a gorgeous view of--"

            scene cut boys_outside1
            with fade

        "Show Svetlana the guest room downstairs": 
            scene bg room3

            show zzsv smile at center
            show zzrl smile
            with fade

            if room3blind == True:
                menu:
                    "close the blinds?"

                    "yes":
                        "just close the blinds -- there was an additional puzzle layer here, dunno if we actually need it"

                        jump blindsclose

                        "now, where's that pesky remote?"

                        menu:
                            "in the drawer":
                                "nope, it's not there"

                                "svetlana is like, what on earth are you doing? shamefaced, you're about to continue the housetour--but too late!"

                                scene cut hollanov2c
                                with fade

                                "well, you tried"

                                jump dinner

                            "next to the door":
                                "nope, it's not there"

                                "svetlana is like, what on earth are you doing? shamefaced, you're about to continue the housetour--but too late!"

                                scene cut hollanov2c
                                with fade

                                "well, you tried"

                                jump dinner

                            "beside the lamp":
                                "indeed, there it is!"

                                jump blindsclose
            
                    "no":
                        pass
            
            else:
                pass

            if shane_room3 == True:

                $ svet_room3 = True
                $ svetheart += 1

                RL "Now, Ma'am, this is our biggest, fanciest room, we hope it will be to your liking! It comes with a spacious bathroom for two, and even has two walk-in closets!"

                SV "Why does any guest room need one walk-in closet, let alone two? How long does Shane think his guests are staying for?"

                RL "He built this room for his parents, apparently. Even though they have their own cottage ten minutes away."

                SV "My, what a thoughtful son. And how much clothing does he think his parents--"

                SV "..."

                SV "Are these Ilya's trophies in Shane's guest room closet?"

                RL "Oh, yeah, apparently Ilya's house in Ottawa's doesn't have space for all of them...?"

                show zzsv unimpressed

                SV "...No, it doesn't. Because Ilya did not get a place he means to stay for good. So instead he puts all his trophies aside, stashes them in a spare room in Shane's spare house."

                show zzrl hesitant

                RL "Oh, that's...I mean, Shane says it's temporary...? They're planning to renovate a build a proper trophy room for the both of them here...?"

                SV "Is that so."

                show zzsv flat

                SV "Ah, it is what it is. Tell me more about this big, fancy room, Rose."

                RL "Oh, uh, yes Ma'am. It also has lots of natural light, and a gorgeous view of--"
            
            else:

                RL "Well, Ma'am, this room is bigger and cosier! We hope this will be more to your liking!"

                RL "It gets lots of natural light, and has a gorgeous view of--"
            
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

    "svet: ...why are you closing the blinds...?"

    "rose: oh, just so it won't get to warm, what with all this light! so you can be comfortable when you sleep in here later!"

    "svet: right, guess you've decided that this is my room then"

    "the stuff after this was one more additional puzzle layer we may not need"

    jump dinner

    if tourdone == "A" and svet_room1 == True and giftbought == "noise":
        "rose: and i even bought you a white noise machine to make this room better!"

        "svet: alright, i'm impressed"

        $ svetheart += 1
    
    elif tourdone == "B" and svet_room2 == True and giftbought == "pillow":
        "rose: and i even bought you proper pillow for the bed!"

        "svet: very thoughtful of you"

        $ svetheart += 1

    elif tourdone == "C" and svet_room3 == True and giftbought == "clock":
        "rose: and i even bought you a clock! that normal people can read!"

        "svet: i do have a phone, but the clock is very cute i admit"

        $ svetheart += 1

    else:
        "rose: yeeeeah, hope that's alright! anyway we should go down to dinner!"

    
    jump dinner

label dinner_late:

    scene bg ctentrance

    show zzrl smile
    with fade

    RL "right, i'm sure they'll join us for dinner once they're done with their snack--oh hi, Svetlana."

    show zzsv flat with easeinright

    SV "Hello...Rose. I was beginning to think I drove all the way here to eat dinner alone."

    RL "Oh, no, the boys are here. They're just...busy."

    show zzsv smile

    SV "Well, I certainly won't complain if dinner is just the two of us."

    jump dinner

label dinner:

    scene bg dining

    show zzsv amused at center
    show zzrl flat
    with fade

    if freedom == 0:
        RL "...and that was the second time I caught them making out today."

        SV "Mm, from the way Ilyusha talks, twice is a remarkable show of restraint."
    
    elif freedom == 1:
        RL "...and miraculously, i've only caught them making out once today!"
        
        SV "Only once, in this exhibitionist house, with those exhibitionist boys? You truly are a miracle worker."
    
    else:
        RL "...and would you believe I haven't seen Shane or Ilya's naked butt even once today?"

        SV "Oh? Were you expecting to?"

        show zzrl hesitant_blush

        RL "Haha, I mean--"

    show zzsh smile at center
    show zzir smirk at midright
    with easeinright
    show zzsv at midleft
    with ease

    IR "We're back. Did you miss me?" ## come back to this

    show zzsv flat

    SV "Barely noticed you were gone. Where are my bags?"

    show zzsh frown_blush

    SH "Oh, fuck, your bags--sorry, I think we left them next to the car...?"

    if loop <= 1:

        show zzrl grin

        RL "Shane, oh my god, that's literally why you and Ilya went outside! You guys seriously spent the whole time making out?"
    
    else:
        show zzrl grin

        RL "Yeah, you did. While you made out the whole time instead." ## is this superfluous?

    show zzsh embarrassed

    SH "No, what--we--why would you say that we were--"

    IR "Yes, the whole time. I am just too irresistable to Shane, he--"

    show zzsh annoyed_blush:
        ease 0.1 xoffset 100
        ease 0.1 xoffset 0
    with hpunch

    SH "Shut up, Rozanov."

    show zzsv amused

    SV "Yes, shut up, Rozanov. You realise that means you left the vodka and pelmeni outside."

    show zzir scowl

    IR "Ah, fuck, the vodka--"

    SV "I suppose we'll just have to break into your stash here."

    IR "I don't have a stash here, Sveta, that is why I asked you to bring fifty bottles." ## check units? is this a reasonable too many or too few?

    show zzsh frown

    SH "{i}Fifty bottles?{/i} Ilya, did you think we'd be drinking two bottles of vodka a day??"

    show zzir eyeroll

    IR "No, no, some bottles are for your papa. Some are for here. And the rest are for me to bring back."

    show zzsv eyebrow

    SV "So you still haven't found a source of good vodka in Ottawa? I'm shocked. In Boston you had three."

    show zzir smirk

    IR "Ah, I've only been here for one year. For now, you will just have to keep smuggling the good stuff to me, Sveta. At least until I convince Hollander's papa to reveal {i}his{/i} sources."

    show zzsh annoyed

    SH "My dad? You're saying {i}my dad{/i} is smuggling vodka."

    IR "What, you think David is too good to smuggle vodka? He is not as boring as you think, котик, you are still the champion for most boring Hollander in the family." ## check russian nickname

    menu:
        "Defend Shane":
            show zzrl wink

            RL "Hey, I'm sure Shane could make a great smuggler too! You guys travel so much for games, it wouldn't be too difficult to sneak away to grab a bottle or two, right?"

            show zzir eyeroll

            IR "Oh, so you don't know Shane's pre-game routine? You think Shane is just sitting around in his hotel room doing nothing, twirling his thumb until he has to be on ice?"

            show zzsv unimpressed

            SV "Oh, it's just a joke, Ilya. Anyway, even if Shane did have free time pre-game, he wouldn't be a very reliable source, would he? You two barely even meet up once a month."

        "Defend Shane's dad":
            show zzrl smile

            RL "I'm sure David's getting his alcohol from legitimate suppliers. Bet he's getting it from a local craft brewery and just doesn't want Ilya buying out their supplies from under his nose. That's why Miles is always hush-hush about {i}his{/i} sources." ## check alcohol??? brewery???

            show zzir annoyed

            IR "Oh, so you think I would buy out David's favourite vodka from under him? What, because I'm best at stealing the puck away from under one Hollander's nose, I will do the same with vodka for another Hollander?"

            show zzsv flat

            SV "Oh, it's clearly a joke, Ilya. After all, if there {i}were{/i} any good craft breweries, you'd already have sniffed them out like you did in Boston."

        "Say nothing" if loop >=2:
            show zzsv flat

            SV "Well, if you like boring, then you must be enjoying Ottawa so much more than Boston. No?"

    show zzir scowl

    IR "Sveta."

    SV "You've at least found a good source for pelmeni, yes? I can go back and reassure Evgenia Mikhailovna that her dearest Ilyushenka is not going to starve to death in a ditch in Ottawa?"

    IR "..."

    show zzsv unimpressed

    SV "No? You draw little Russian grandmothers to you like you draw penalties from insecure D-men. It's been a whole year in Ottawa, and you still haven't charmed a nice old lady into feeding you?" ## check hockey? draw...aggressive D-men?

    IR "Что ты вытворяешь, Sveta?" ## check russian

    SV "Tsk, don't be rude, Ilya, your Jane doesn't speak Russian. Nor does Rose."

    if loop >= 1:
        menu:
            "Say nothing":
                IR "David and Yuna Hollander are feeding me, Sveta. You can see I have not starved."

                SV "Oh, you have charmed them?"

                show zzir hesitant

                IR "I..."

                show zzsh flat

                SH "Yes. My parents think Ilya's charming, they like him."

                show zzsh frown

                SH "But...I guess they can't make good pelmeni like a Russian grandmother, so...so I'll go get the pelmeni, okay?"

                SH "Sorry, it's on me for forgetting it earlier anyway--"

            "Distract everyone with pelmeni":
                show zzrl hesitant

                RL "Um, hey, you know what? Why don't I go get the pelmeni and vodka from the car?"

                show zzsh frown

                SH "No, I'll go get it. Sorry, it's on me for forgetting it earlier anyway--"

    else:
        show zzrl hesitant

        RL "Um, hey, you know what? Why don't I go get the pelmeni and vodka from the car?"

        show zzsh frown

        SH "No, I'll go get it. Sorry, it's on me for forgetting it earlier anyway--"

    show zzir annoyed

    IR "You forget because you were on {i}me{/i}, nothing to be sorry for. {i}I{/i} will go get the vodka and pelmeni, since Sveta has so much to say about it."

    hide zzir with easeoutright

    SH "..."

    RL "Um..."

    show zzsh hesitant
    
    SH "Actually, I think I'll go help Ilya with the bags."

    hide zzsh with easeoutright

    show zzsv flat

    SV "I wonder how long they'll take with my bags this time."

    RL "Svetlana..."

    SV "I think I'll go outside for a bit as well, get some air. Turns out I'm not so hungry after all."

    menu:
        "Join her outside":
            $ pt += "go out, "

            $ svetheart += 1

            RL "Oh, I'll come with you? I'm not that hungry either."

            show zzsv smile

            SV "If you like. I wouldn't mind the company."

            jump outside

        "Excuse yourself to study more french" if french >= 1: ## move this into stay indoors
            $ time = 2
            jump grind_french

        "Excuse yourself to train more hockey" if hockey >= 1: ## move this into stay indoors
            $ time = 2
            jump grind_hockey
        
        "Stay indoors": ## come back to this, if this scene is weird on a 3+ playthrough you can add an else statement
            $ pt += "stay in, "

            RL "Oh, right. I'll come get you when Shane and Ilya get back...?"

            show zzsv smile

            SV "Thank you."

            hide zzsv with easeoutleft

            show zzrl flat

            RL "Right. Time to...check my emails...?"

            RL "Maybe I should see if the boys want my help with Svetlana's bags..."

            scene bg hallway

            show zzrl flat
            with fade

            if inside == 0:

                RL "...not that Ilya is gonna want my help for anything ever--"

                scene cut boys_frontdoor
                with fade

                RL "..."

                RL "{size=-10}Nope, they're {i}really{/i} not gonna want my help for that..."
            
            else:

                RL "...except no, wait, the last time, didn't they--"

                scene cut boys_frontdoor
                with fade

                RL "..."

                RL "{size=-10}Yup, they forgot about Svetlana's bags again, didn't they..."

            ## add some sort of walking backwards effect to the image?

            scene bg dining

            show zzrl flat
            with fade

            show zzrl resigned_blush

            RL "Right. Emails."

            show zzrl grin

            RL "Or maybe...more Food Truck Kitty."

            $ foodtruckkitty += 1

            scene cut game
            with fade

            RL "...I swear it's like I never get any faster at making the Triple Salmon Burger Delight no matter how many times I play this level..."

            SV "Ahem."

            scene bg dining

            show zzrl flat
            with fade

            show zzsv flat at center
            with easeinleft

            RL "Oh, you're back!"

            RL "Are those your bags...?"

            SV "Yes, I had a suspicion that the boys would get distracted again, so I went around to the car to check. And I was right."

            RL "Haha, yeah, they're really good at distracting each other, huh? They--"

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

        RL "Oh! Haha, um, I don't really--"

        show zzsv thoughtful

        SV "As to your question. They seem good together, when they {i}are{/i} together."
        
        SV "But for most of the year, they're not."

        show zzrl resigned

        RL "Ah, yeah. That's true. Long distance relationships can be really hard."

        show zzsv unimpressed

        SV "Yes. But who has been having it harder? Who has moved to a new city, is having a terrible time on his new team, now hides away all summer with no one else in this middle-of-nowhere--"

        scene cut boys_inside
        with fade

        SV "..."

        RL "What--whoa! Oookay, turning back around now."

        scene bg backporch

        show zzsv unimpressed at center
        show zzrl grin_blush
        with fade

        SV "...They look good together when they are together, at least."

        RL "Haha, they do seem to be enjoying being in the middle of nowhere with no one else around."

        show zzsv eyebrow

        SV "Oh, you think we're no one to them?"

        show zzrl hesitant_blush

        RL "Um..."

        show zzsv smile

        SV "I'm joking. Ah, I bet they've forgotten my bags {i}again{/i}."

        show zzrl smile

        RL "Let's just go get your bags ourselves."

        show zzsv flat

        SV "Yes. And enough talking about these dumb hockey boys, they're grown men who can do whatever they want. Evidently."

        show zzrl grin

        RL "No problem! I can talk about other dumb hockey boys instead, if you like? Because you know who's {i}not{/i} having a terrible time on his new team? Wyatt Hayes."

        show zzsv surprised

        SV "Hah, yes! He's having a surprisingly good year, isn't he? I didn't realise you followed hockey--"
    
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

        SV "...Perhaps."

        RL "And...and if I said, I agree, long-distance relationships are hard, you'd say, who is having a harder time of this long-distance relationship?"

        RL "Because you think Ilya has it harder, right? And I mean, you have good reason to think so."

        show zzsv thoughtful

        SV "Hmm. You are an extraordinarily perceptive woman, Rose. Or Ilya is telling Shane far more than I thought he was."

        show zzrl smile_blush

        RL "Oh, no, I'm really not! And Ilya's really not."

        show zzrl resigned

        RL "Or, if he is, Shane hasn't told me..."

        show zzsv flat

        SV "Hmm, no need for false modesty, you were hardly off-base--"

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

        RL "Oh, haha, I mean, I have really enjoyed meeting you! But I meant..."

        show zzsv thoughtful

        SV "You meant something like a premonition. You feel like you knew what I would say even though I have not said it."

        show zzrl surprised

        RL "Yes! Exactly!"

        show zzrl thoughtful

        RL "And it's been happening all day! I mean, some things have been different, so maybe it's just...maybe it's just weird deja vu, my subconcious picking up on stuff, and I'm making too much out of it, but..."

        show zzsv eyebrow

        SV "But you don't think your subconscious is that extraordinarily perceptive either."

        show zzrl hesitant

        RL "Well, I do think I'm fairly perceptive, but also...also, I feel like I can predict things that just aren't..."
        
        RL "Like that if we look up at the cottage right now--"

        scene cut boys_inside
        with fade

        RL "--we'll see the boys making out."

        SV "...I have to say, it doesn't take much perception or premonition to predict that."

        RL "...Okay, fair."

        scene bg backporch

        show zzsv thoughtful at center
        show zzrl resigned
        with fade

        RL "So...yeah. Sorry, you probably think I'm crazy."

        SV "Mm, no. I don't."

        SV "I don't believe in premonitions, but...I don't disbelieve, either. You've behaved normally all day, so why should I assume you are crazy on the basis of some...shall we say uncannily accurate insights into my thoughts on Shane and Ilya?"

        SV "Whether that is premonition or perception, only time can tell, no?"

        SV "So tell me, Rose, what happens next?"

        show zzrl hesitant

        RL "Oh! Um, we...go round to the car to pick up your bags, and we...talk about hockey...?"

        show zzrl shy

        RL "I guess that's not much of a prediction, but--"

        show zzsv amused

        SV "But it's something I don't think you're crazy to suggest. In fact, I would gladly test these potential powers of yours. Tell me, Rose, what do you think I think of Wyatt Hayes--"
    
    elif outside == 2:
        
        $ outside += 1

        RL "..."

        SV "..."

        RL "..."

        show zzsv eyebrow

        SV "You seem thoughtful. Dare I--"

        RL "{size=-10}'--ask what you're thinking of?'"
        
        SV "--ask what you're thinking of--oh."

        show zzsv surprised

        SV "Yes. That."

        show zzrl hesitant

        RL "Sorry. I didn't mean to, um--"

        show zzsv flirty

        SV "Read my mind? Careful, you might blush at some of the things I'm thinking about you."

        show zzrl wince_blush

        RL "Oh, I mean, I can't read your mind, but..."

        show zzrl hesitant
        
        RL "Okay, you didn't think I was crazy last time, so I'll just come out and say it. Either I've gained some sort of mutant powers of precognition, or I'm living through some kind of groundhog day, or...something, I don't know, but something strange is going on!"

        show zzsv surprised

        SV "...something...strange?"

        RL "The last time I remember being out here, talking to you, we talked about Shane and Ilya. And you said that they seem good together when they {i}are{/i} together, but they're {i}not{/i} together for a lot of the year."

        RL "And you said that the long distance relationship has been harder for Ilya than for Shane."

        show zzsv eyebrow

        SV "...I said that, did I?"

        RL "Oh, and also, last time, despite the fact that they said they were going out to get your bags, Shane and Ilya were fully making out instead. And as you can see--"

        scene cut boys_inside
        with fade

        RL "--they are."

        SV "...Indeed they are."

        RL "...yeah. I really need to ask Shane why there aren't any curtains in this house."

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

        SV "...and let's keep walking in the meantime. The flashes of Shane's naked ass in the corner of my eye is not helping with my concentration."

        hide zzsv with easeoutleft

        scene bg outback
        with fade

        show zzsv flat at center
        with easeinright

        show zzrl flat
        with fade

        SV "..."

        RL "{size=-10}...why is there a moose, Shane, why?"

        show zzsv amused

        SV "More than one mystery to be solved today, it seems."

        show zzsv thoughtful

        SV "Let's solve the more important one first. What if I ask you some questions you can't possibly know the answers to, unless you've done this before?"

        show zzrl hesitant

        RL "But we {i}haven't{/i} done this before. So there's no way for me to convince you, right...?"

        SV "Not this time, no. But I will tell you the answers, and you might be able to next time, yes?"

        menu:
            "Do the test":
                show zzrl hesitant

                RL "I guess that's true. As long as you ask the same questions each time."

                RL "And as long as you promise not to think I'm crazy if I get everything wrong, and I break out of this loop tomorrow anyway."

                show zzsv flirty

                SV "If you get everything wrong and tomorrow happens anyway, this will be the most unforgettable conversation I've had with a beautiful woman I'm meeting for the first time. That's not so bad, is it?"

                show zzrl smile_blush

                RL "I guess not. We'll laugh about this in twenty years, or something?"

                show zzsv smile

                SV "Exactly. Now, first question."

                jump outside_test

            "Try something else":
                
                show zzrl hesitant

                RL "You can't just...trust me...? You did, before, sorta."

                show zzsv eyebrow

                SV "Did I? What else did you say to convince me?"

                RL "Um...you asked me what we did after this, and I said we went to pick up your bags and talk hockey. And you asked me to predict your hockey opinions."

                show zzsv amused

                SV "We can do that. I should warn you that I have {i}many{/i} hockey opinions though, so you might not have an easy time convincing me that way."

                show zzrl grin

                RL "It might not be easy, but it {i}was{/i} fun! Okay, so, first, your thoughts on Wyatt Hayes--"

                jump preleaving

        call outside_test
        
        if convincesvet == 3:
            jump testpassed

        SV "Well, you haven't exactly proven yourself..."

        show zzrl wince

        RL "I did say we hadn't done this before."

        show zzsv smile

        SV "True, you did say. Perhaps I should have asked you about something that you think has happened before. We talked about hockey too, yes?"

        show zzrl hesitant

        RL "Yeah, while we went to get your bags, since Shane and Ilya are, y'know, distracted."

        SV "Let's do that then. Tell me, Rose, what do you think I think of...say....Wyatt Hayes--"
    
    else:
        $ outside += 1

        show zzsv flirty

        SV "And it sounds, if not impossible, at least improbable, that I should have spoken to you alone three times and only talked about those silly boys every single time. Surely we have better things to talk about."

        show zzrl smile_blush

        RL "Oh, I mean, we also talk about hockey...?"

        show zzsv amused

        SV "That does sound much more probable. Also more fun! So, you follow hockey then?" ## 'follow hockey'? 'watch hockey'? 'are a true fan of hockey'???

        #####

        
        show zzrl hesitant

        RL "Yeah, I--no wait! So you believe me??"

        show zzsv thoughtful

        SV "Maybe the question should be, why do you want me to believe you? Why not tell Shane about this?"

        scene cut boys_inside ## second version
        with fade

        RL "Um..."

        SV "At a time when he might be more receptive. To the idea, I mean."

        RL "Look, Shane's great, but there is no way I'm getting him to believe Groundhog Day is real."

        SV "Mm. Yes. Shane {i}is{/i} great."

        SV "..."

        SV "...ah, perhaps we should have this conversation somewhere else. Shane's ass has not quite faded into the wallpaper for me yet."

        ####

        RL "Why is there a moose. There's such a thing as being too Canadian, Shane."

        "rose: if i'm stuck in a time loop i must be a bad person right?? hypothetically??"

        "svetlana: not necessarily. maybe you need to tell someone a dark secret. save someone's life. kiss your one true love."

        "rose: what? that was not in groundhog day?"

        "svetlana: groundhog day is not the only time loop fic--i mean story--out there--oh look, a distraction!"

        "rose: ...tbh at this point my eyes have kind of started glazing over the moment shane's naked ass shows up in my periphery."

        "rose: so it turns out you are secretly a time loop expert"

        "svetlana: ...who told you my ao3 handle? was it ilya? i'll poison his vodka i swear--"

        if svetpass == False:
            "rose: what? your what--no, i don't have time. tell me how i can convince you i'm in a time loop! hypothetically"
        
        else:
            "rose: no, sveta, you told me this yourself! look, i'm in a time loop, and you're gonna ask me three questions to prove it to you. and i can do it, i swear"
        
        if svetheart == 0:
            show zzsv eyebrow

            "svetlana: ...nothing. time loops are fake. you're a weird one, rose landry--quick look over there!"

            scene cut boys_inside
            with fade

            "rose: ..."

            "svetlana: excuse me, i need to go kill a man"

            jump leaving
    
        else:
            $ freedom += 1

            call outside_test

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
    
    SV "Hmm...the most telling question, I think. Which power ranger did i have a crush on when I was younger?"

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

            SV "I--well. Yes."

            show zzsv thoughtful

            SV "I didn't know whether I wanted her or wanted to be her."

            $ convincesvet += 1

        "Red ranger":
            RL "Red ranger."

            show zzsv amused

            SV "Sorry, but I liked Tanya Sloan best, actually."

            RL "Who?"

            SV "If you're in a time loop, I'm sure you'll have time to look her up."

    return

label testpassed:
    
    $ pt += "pass test, " 

    show zzsv surprised

    SV "Hmm. You passed the test."
    
    if svetpass == 0:
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

        SV "That's a common reason for time loops, no? Someone dies, you need to save them? Not me, then--maybe someone's put out a hit on Shane? A Boston fan, perhaps--though in that case, they're more likely to put out a hit on Ilya--"

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

        SV "You're already pretty impressive, Rose Landry."

        show zzrl hesitant_blush

        RL "Haha, I...thanks! Now I really need to figure out this time loop so I don't break out of it by accident."               

        $ svetpass += 1

        if svetheart >= 2:

            SV "You know, the other traditional way to break a time loop is with a kiss."

            menu:
                "Lean in...":
                    $ pt += "kiss, "

                    RL "Oh, haha, that's...that's fair! I suppose if it's traditional..."

                    scene cut girls_kiss1
                    with fade

                    $ kissnow = True
                    $ kisscount += 1

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

                    RL "Oh, absolutely, I'll have to--"

                    jump postkiss

                "Don't lean in":
                    $ pt += "don't kiss, "

                    RL "Oh! Is, um, is it? Which movie is that from?"

                    show zzsv amused

                    SV "Movies aren't the only stories with time loops in them, you know."
                    
                    SV "But if you're hoping {i}not{/i} to break out of the loop, perhaps that's best avoided."

                    show zzrl hesitant_blush

                    RL "Haha, yeah, gotta have a bit more of a holiday first!"

                    show zzsv flat

                    SV "So, what happens next?"

                    show zzrl hesitant

                    RL "You mean in the previous loops? Well, we'd...we'd go pick up your bags from the car and talk hockey?"

                    show zzsv smile

                    SV "Sounds great. I wouldn't want to break out of this loop either, if it were me."

                    jump preleaving          
        
        else:
            jump leaving
    
    else:
        "temp dialogue blah blah blah"

        menu:
            "kiss svetlana":
                $ pt += "kiss, "

                jump kiss

            "don't kiss svetlana":
                $ pt += "don't kiss, "
                jump preleaving
        
        RL "Haha, now I really gotta figure out what will stop these loops so I don't do it on purpose."



        show zzsv thoughtful

        SV "Perhaps we're approaching this from the wrong angle. What have you tried doing differently?"

        show zzrl hesitant

        RL "Um, mostly just...saying different things...?"

        show zzrl hesitant_blush

        RL "And even then...I haven't been trying different things to get myself out, really, I've just been...trying to catch up with Shane? Trying to get Ilya to like me?"

        if foodtruckkitty >= 1:
            show zzrl wince

            RL "{size=-10}...playing a bunch of Food Truck Kitty...?"

            show zzsv eyebrow

            SV "What's that?"

            RL "It's...a mobile game...it's just silliness, I probably shouldn't have been wasting my time with it when I'm stuck in a supernatural time loop."

            show zzsv amused

            SV "If you ask me, being stuck in a time loop is the best time to be playing silly mobile games. When else would you have the infinite free time."

            show zzrl grin

            RL "Well, when you put it like that!"
        
        else:

            SV "Unless you can loop back in time all the way to two years ago to stop yourself from dating Shane, I don't think you're getting Ilya to like you."

            show zzrl resigned

            RL "I suppose. Honestly, I wouldn't care so much about Ilya liking me if I didn't think it would make Shane happier if we got along."

            SV "If the solution"

        #######

        
        show zzrl hesitant

        RL "...I guess, but what is there to fix other than myself...?"

        show zzsv flirty

        SV "I suppose personal growth is a common solution. Though you're confident, successful, and seem like a lovely person just as you are, so I find that unlikely."

        show zzrl smile_blush

        RL "Oh! That's--thanks, I mean, no one's perfect, as my dating record probably proves"

        SV "Though you seem lovely just the way you are, so maybe that's not it."

        ########


        RL "I just don't understand how I keep running into Shane and Ilya...you know..."

        SV "Fucking?"

        RL "Hah! I was going to say making out, but mostly because I keep interrupting them before any fucking actually happens. And I'm not doing this on purpose, I swear, I just can't seem to avoid--not that I think it has to be avoided! They're--"

        SV "Hot?"

        show zzrl grin

        RL "I was going to say they're my friends, but yes, they're also hot."

        show zzrl grin

        RL "Don't tell them I said that."

        SV "Why not? You think they won't like it?"

        RL "Oh my god, I was going to say they might die of embarrassment, or really that {i}Shane{/i} might die of embarrassment, but considering how many times I've walked in on his naked ass today..."

        SV "He's still alive, it's true. As is Ilya."

        RL "Ilya doesn't seem like he would care, no. If anything, he seems like...oh, well, I guess I don't know him very well, I shouldn't judge him by--"

        SV "Oh, he deserves plenty of judgement, don't worry. Especially for this."

        RL "Especially for...you don't mean to say he might be doing this on purpose...??"

        SV "I wouldn't put it past him. He likes to show off his pretty things, and Shane is the prettiest thing he has."

        show zzrl hesitant

        RL "Oh, that's... You don't think Ilya really thinks of Shane like that, do you...?"

        show zzsv smile

        SV "Mm, no. And it sounds like you don't either. I'm glad."

        show zzsv thoughtful

        SV "He can't stop himself from pressing on a bruise, sometimes." ## check appropriate use of nickname

        RL "Trying to prove he's a big strong man and not scared of pain? My brothers used to get like that too."

        SV "Hah, yes, you understand. The more it hurts, the more they have to prove."

        RL "And the bruise is...me finding Shane sexually attractive...?"

        SV "Perhaps. Perhaps it's that you have already seen Shane sexually, and now Ilyusha gets to have it be his choice. Or perhaps it's Shane not wanting to be seen with him at all."

        show zzrl eyebrow

        RL "...I feel like not wanting to be seen holding hands is kinda different from not wanting to be seen holding each other's naked dicks."

        SV "Mm. Well. Perhaps Ilyusha is just being petty, then, and wanting you to see what you cannot have. Or perhaps he's angling for a threesome."

        show zzrl surprised

        RL "No way! There's no way he would ever want to sleep with me!"

        #######

        "svet: so tell me what's been going on, lemme help you with it"

        "rose: actually, you already have. i mostly wanted to convince you so i could kiss you."

        if svetheart >= 2:
            "svet: well, you're {i}very{/i} convincing"

            jump kiss

        else:
            "svet: hmm...no thanks"

            "rose: ...oh."

            jump leaving
    

label kiss:
    menu:
        "kiss svetlana":

            scene cut girls_kiss1
            with fade

            $ kissnow = True

            if kisscount == 0:
                "rose's first kiss with svetlana! gasp!"

                $ kisscount += 1

            elif kisscount == 1:
                "rose's second kiss with svetlana! still a great kiss!" 

                $ kisscount += 1
            
            elif kisscount == 2:
                "rose's third kiss with svetlana! maybe we should get an extra cutscene here lol"

                $ kisscount += 1
            
            else:
                "rose has lost count of how many kisses she's had with svetlana. it's okay they're all still special in her heart"

                $ kisscount += 1
            
            "okay time to stop kissing."

        "don't kiss svetlana":
            "your loss, rose"
    
    jump leaving

label postkiss:

    show zzsh frown at center
    show zzir flat at midright
    with easeinright

    show zzsv at midleft
    with ease

    SH "Oh, good, we found you guys. You weren't inside, and you weren't replying to your texts--"

    show zzrl wince_blush

    RL "Sorry Shane, we were, um, distracted."

    show zzir smirk

    IR "Thought you were both eaten by Canadian wolf birds."

    show zzsh eyeroll

    SH "Loons don't eat people, Ilya. Actually, even wolves don't eat people."

    IR "And how do you know that? You know many people that meet Canadian wolves?"

    show zzsh wry

    SH "No--"

    IR "Because they all get eaten!"

    show zzsv amused

    SV "Sorry if you were worried, but I think I still have Ilya muted from the last time he was being annoying at me."

    show zzsh smirk

    SH "If you mute Ilya every time he's annoying, he must be muted on your phone all the time."

    SV "He is. Though I do unmute him when he buys me an appropriate apology present."

    show zzir eyeroll

    IR "Hah, you unmute me when you want to bitch about your clients or gossip about people we know. Which is also all the time."

    show zzsv flat

    SV "Anyway, you should give me your number, Shane. Next time you can text me directly. I'm sure you won't make me want to mute you."

    show zzsh hesitant

    SH "Uh...sure...?"

    SV "Good. Now you, Rose, you should also give me your number."

    show zzir annoyed

    IR "Why do you want Rose Landry's number? There is no reason for you two to text after today."

    if kisscount == 1:
        show zzrl smile_blush

        RL "Oh, sure! Here's my number--"

        show zzrl wince

        RL "Oh shit, is that the time? I gotta go, my flight's in three hours."

    else:
        show zzrl smile_blush

        RL "Sure, here's my number. Hope I {i}can{/i} text you after today."

        if freedom == 3:

            SV "Mm, I have a good feeling about it."

            IR "I do {i}not{/i} have a good feeling about it."

            SH "{size=-10}Shut up, Rozanov. They're having a moment."

            IR "{i}I know.{/i}"
        
        RL "Anyway, I gotta go, I have a flight to catch."
    
    SH "Oh, yeah. Hey, let me walk you to your car?"

    jump walkout

label preleaving:

    scene bg dining

    show zzsv smile at center
    show zzrl smile
    with fade

    if outside == 1:
        RL "--and I couldn't believe they came back in the third after being down three! And then won in OT!"

        SV "I'm not usually a fan of Edmonton, but even I have to admit that was--" ## check hockey
    
    elif outside == 2: ## check more hockey!!
        RL "some other hockey dialogue here"

        SV "sorry someone else is gonna write this"
    
    elif outside == 3:
        RL "still more hockey chitchat"

        SV "still leaving this for someone else to write lol"
    
    else:
        RL "hockey hockey hockey"

        SV "more hockey more hockey"
    
    jump leaving

label leaving:

    show zzsh flat at center
    show zzir flat at midright
    with easeinright

    show zzsv at midleft
    with ease

    SH "Hey, sorry we took so long--wait, are these Svetlana's bags?"

    if loop == 0:
        show zzrl grin
    
    elif loop == 1:
        show zzrl smile
    
    else:
        show zzrl resigned

    RL "The bags that you and Ilya didn't bring in again? Yup."

    show zzsv amused

    SV "We saw you two were busy, so we decided to help ourselves."

    show zzsh embarrassed

    SH "Oh my god, you saw--"

    show zzir smirk

    IR "Yes, Shane and I always have a busy summer here, so good job helping yourselves. Congrats, big win for feminism."

    show zzsv unimpressed

    SV "Right. Big win, yes, for women in general and Rose specifically, because she is going home with five bottles of your vodka today as thanks for actually helping."

    show zzir annoyed

    IR "...Okay, fine, I support women's rights and women's wrongs. She can have five bottles, I will have the other forty-five." ## come back to this

    show zzsh eyebrow

    SH "...Okay, who taught you that?"

    show zzir smirk

    IR "Taught me what, maths? Do they not teach you this in Canadian school?"

    show zzsv flat

    SV "I did not actually bring you fifty bottles of vodka, Ilya."

    if loop <= 1:
        show zzrl hesitant

        RL "Actually, I can probably only take a bottle with me on the flight back, so Ilya can keep the rest of his vodka. Which, speaking of heading back..."
    
    else:
        show zzrl resigned

        RL "It's fine, I don't think I'll get a chance to drink it, anyway. Also, I should go..."

    show zzir outraged

    IR "Sveta! You only bring me five bottles of vodka??"

    show zzsh hesitant

    SH "Oh shit, is it already that late? Sorry, Rose, I didn't realise the time--"

    if freedom == 3 and kissnow == True:

        "svet: hey, actually rose, why don't you stay the night? with me."

        show zzrl smile_blush

        "rose: oh, haha, sure!"

        "hollanov: surprised pikachu face"

        jump end
    
    elif freedom == 3:

        "svet: good luck for tomorrow."

        "rose: you know what, i have a good feeling about it. and even if things don't work out, i don't mind being here again tomorrow."

        "shane: er...so should i still drive you out to the airport, or...?"

        "rose: yeah thanks, please drive me out. {size=-10}Hopefully for the last time."

        jump end
    
    else:
        pass

    show zzrl smile

    RL "Hey, it's fine, thanks for dinner anyway! Even if we didn't quite manage to eat it together."

    RL "Anyway, it was nice meeting you, Ilya. And nice meeting you too, Svetlana."

    show zzsv flirty

    if svetheart >= 2: ## may need to adjust this if kissing happened

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
    
    IR "Okay, I see how it is. I worried about snakes and wolves out in the Canadian wilderness, but all the snakes are in this house--" ## come back to this

    show zzsh smirk

    SH "Canadian wilderness? Rozanov, we're in Muskoka. The only thing that might eat you out here in this wilderness is mosquitoes." ## check show check canadian

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

        show zzrl wink

        RL "Well, I actually saw a whole lot of {i}you.{/i} And Ilya. If you know what I mean."

        show zzsh embarrassed

        SH "Oh my god, I'm so sorry, I wasn't--"

        show zzrl smile

        RL "Hey, hey no, babe it's fine! Besides, I've already seen it all, right?"

        show zzsh hesitant_blush
        
        SH "That's...it's different, though. If it's when I'm with Ilya."

        show zzrl grin

        RL "Clearly! Three times in half a day? I could never believe it of the Shane Hollander I dated!"

        show zzsh embarrassed

        SH "Rose, oh my god--"

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

        SH "What...? I mean, I said, if you did it all again--"

        ## insert transition here if you wanna make things really clear, or you could wait until after playtest to decide

        show zzrl hesitant

        RL "Oh, haha, no I heard you. Just got lightheaded for a second."

        show zzrl grin
        
        RL "And hey, if you want me to see less of you, take it up with your boyfriend!"

        RL "Or rather, don't {i}take it up{/i} with your boyfriend, if you know what I mean--"

        show zzsh smile_blush

        SH "That is terrible, Landry. Get outta here already."

        RL "I'm going, I'm going! Love ya', talk to you soon, yeah?"

        show zzsh smile

        SH "Yeah. Thanks for coming, Rose, talk to you soon as I can, promise."

    elif loop == 1:

        show zzrl thoughtful

        RL "You know, it kinda feels like I saw more of you than you thought."

        show zzsh embarrassed

        SH "Oh my god, I'm so sorry, I wasn't--"

        show zzrl surprised

        RL "Oh! I didn't mean in like a nudge-nudge-wink-wink kinda way!"

        show zzrl grin

        RL "I mean, I did see more of you than you thought, nudge-nudge-wink-wink--"

        show zzsh smile_blush

        SH "Knock it off, Landry, I swear you're worse than my rookies sometimes."

        show zzrl smile

        RL "--but I also meant...I dunno, today just feels really familiar? Lots of deja vu, like my subconcious thinks I've seen more of you today than I actually have, or something?"

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

        RL "I know, I'm just teasing. Though maybe the next time I'm here, I'll make you watch it with me..."

        show zzsh hesitant

        SH "Er, I don't usually like animal movies. And I don't know if you'll be here again soon--not that I didn't enjoy having you up here at the cottage, but if you're gonna be in Montreal--"

        show zzrl resigned

        RL "Oh, don't worry about that. I'm glad you enjoyed having me here, cause I'll be back."

        SH "...what?"

        RL "Never mind! Bye Shane! {size=-10}For now..."
    
    else:

        show zzrl grin

        RL "That's okay, I actually saw a whole lot of {i}you.{/i} And Ilya. If you know what I mean."

        if freedom == 3: ## come back to this when we figure out the arc
            show zzsh hesitant

            SH "You...did?"

            show zzrl surprised

            RL "Yeah, I...huh."

            show zzrl thoughtful

            RL "Maybe I didn't, actually. I didn't actually see much of you guys today, did I?"

            show zzsh frown

            SH "No, and I really am sorry about that--"

            show zzrl smile

            RL "Hey, no, babe it's fine! This is still one of the nicest holidays I've had in a while."

            show zzrl hesitant

            RL "And...and if tomorrow I'm back in LA--not that I'm trying to jinx it or anything! But if I am, we can both do better about trying to stay in touch, right?"

            show zzsh hesitant

            SH "{i}If{/i} you're back in LA...?"

            show zzsh smile_blush

            SH "But yeah, let's be better about it. It really was nice having you around, and...and getting to be with Ilya in front of you."

            show zzrl grin

            RL "Oh, I know you totally enjoy getting to be with Ilya in front of people. Even if you didn't get to as much, this time."

            show zzrl smile

            RL "Okay, I really gotta go. Love ya', talk to you soon, yeah?"

            show zzsh smile

            SH "Yeah. Thanks for being here, Rose, talk to you soon."

            jump end
        
        else:
            show zzsh embarrassed

            SH "Oh my god, I'm so sorry, I wasn't--"

            show zzrl smile

            RL "Hey, no, babe it's fine! This is still one of the nicest holidays I've had in a while."
            
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

            SH "What...? I mean, I said, if you did it all again--"

            show zzrl thoughtful

            RL "...wait a second..."

            SH "..."
            
            SH "What are we waiting for...?"

            RL "Hmm..."

            RL "Never mind! Bye Shane! {size=-10}For now..."

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

    scene black
    with fade

    "you solved the puzzle, well done! rose is free of the loop!"

    if kissnow == True:
        "rose also kissed svetlana this loop, so guess she now has a girlfriend!"
    
    elif kissnow == False and kisscount >= 1:
        "rose somehow failed to kiss svetlana this loop, but she's done it before so we believe she can kiss her again!"
    
    else:
        "roselana are not together but that's on you, bud"
    
    centered "you did: [pt]"
    
    "this ends the game!"

    return

