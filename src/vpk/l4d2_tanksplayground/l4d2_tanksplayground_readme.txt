Tanks Playground v3.0, by obez - 2017-09-04

Changelog ---------------------------------------------------------------------
  3.0 (2017-09-04):
    Please note:
       The addon system doesn't allow versions with two decimals.
       This is why the version number jumped directly from 2.9 to 3.0 and not 
       2.10.

    # Coop
       - No more crash when joining a game in progress
       - Sorry about that!

Info --------------------------------------------------------------------------

# Coop

Survive the hordes of tanks for 10 minutes until rescue arrives!
Similar to the TankFever series but with less predictability.
13 to 15 tanks at most in Normal, Advanced and Expert modes.


# Survival

Plays more like Helm's Deep survival (with stages) than a classic survival.
The first stage only has Tier 1 weapons but you get better ones once you go up
the tower. Even though tanks are limited to 2 in survival, you'll sometimes get
3 or even 4 tanks at once.

There are 7 stages:
  1. Tower "Garden" & Roof: Beginning
  2. Glass Bridge: Hold the end of the bridge (with bridge door trap)
  3. Peanut Island: Say "Hi!" to Peanut and the "Brain Dead" mower trap
  4. Ladder defense: Defend until the ladder is down
  5. Zombie Run: Fight your way through the horde to reach Pillars Island
  6. Pillars Island: Defend your way into the tower
  7. Submarine Vault: Escape the island in the Submarine! 
     (Can one escape a survival map?)

The timings of the stages are relative to the start of each stage.
If you don't end a stage by going to the next one, the next one won't start.

That means you can either go the shortest path (shortest timing of each stage)
or try to get the best timing at each stage to get the best all around timing.


# Versus (Experimental / For fun / Not throughly tested)

By night so the tank players have a chance to reach players before getting 
sniped.

Coop Info ---------------------------------------------------------------------
I tried a different approach that the one Lain used in his Tank Fever series.
I used a custom finale script which means that:
  - Tank spawns are random (but never too close to the player).
    In the TankFever series, the tank spawns are done at specific places
  - The end credits display the correct values
  - There will be no common infected once the finale is launched.
  - The rescue closet is not working once the finale is launched. To remedy this
    I implemented a script to teleport drowned players to the rescue closet (runs
    every minute) and added more defibrilators around the map. If a players dies
    before the finale has started he will respawn in the closet though.
    When a drowned player is teleported to the rescue closet, a red light lights
    on above the closet for a short time.

Players who already have experience with the Tank Fever series should start on
Normal difficulty. Note that Advanced and Expert modes are beatable. Don't 
expect to beat the map on the first try but if you do, congrats!

The rescue point is chosen randomly among three, all by helicopter:
  - Above the start;
  - North-East, near the red cross;
  - North-West, above the crates (pillars island)

The bots don't heal when there's a tank in play, this is a limitation of the AI.
You need to heal them yourself if you want them to go further :)

Have fun!

Known Issues / Bugs -----------------------------------------------------------
  - Easy mode can become very easy if you kill all the tanks. I believe this is
    because of the time between two tanks spawn that might be higher in Easy.
    I would only recommend this mode for beginners or to discover the map (but
    you can also free roam before starting the finale in Normal difficulty)
  - Survivors who fall after hanging on a ledge, either into the water or on 
    the floor become ragdolls and _cannot_ be defibrilated. They also won't be 
    teleported to the rescue closet.
  - If you get the "Model not precached" error, it might come from a 
    conflicting mod. The Bot Swap mod is known to occasionally provoque it.
  - If everyone dies when the helicopter is here, the bots will keep going to 
    this helicopter in the next games when rescue arrives.

Previous updates --------------------------------------------------------------
  2.9 (2016-05-30):
    # Survival
       - Updated my continuous integration script to include automatic cubemap 
         and strings dictionary building
       - No more crash when joining a game in progress
       - Sorry about that!

  2.8 (2016-05-29):
    # Coop
       - Fixed the lag occuring at restart

    # Survival
       - Added a fence at stage 4 to disallow access to ammo before the stage
         has started
       - Stage 5 now has a 3 minutes time limit after which tanks will spawn 
         closer to survivors
       - Records have been reset

  2.7 (2013-12-24):
    # Coop
       - Tweaked the nav to fix the regressions introduced by the Enhanced 
         Mutation System

    # Survival
       - Tweaked the nav around the stage 6 tower
       - Tweaked the stage 7 elevator timings, infected shouldn't drop from
         the tower hole until the sub is ready
       - New infected ladder on the glass tower at stage 1. It activates some 
         time after the tower has opened but before stage 1 ammo runs out
       - Removed the stools at the submarine command center

  2.6 (2013-05-25):
    # Coop
       - Added a defib near the double stairs passage
       - Fixed a minor nav issue
       - Fixed an exploit at the rescue crates on pillars island (thanks Le 
         Phoenix & friends)

    # Survival
       - Fixed the infected coming down the hole too early at Stage 7
       - Fixed some navs around the tower that were blocked
       - Fixed the sub ready hint message showing too early

  2.5 (2013-05-02):
    # Coop
       - Made the STOP signs more visible at the end of the lower glass bridge
       - Added lasers at the beginning
       - Fixed some props floating above ground
       - Fixed some nav issues
       - Expanded the top platform with the two M60s near pillars island. 
          + Changed one of the M60s into a grenade launcher
       - Added another grenade launcher near the glass tower
       - The helicopter cages now activate sooner (sorry Airan!)

    # Survival
       - Stage 7:
          - The vault directions are now more visible (added an emergency light 
            and decals)
          - Infected can come down the tower after the sub is ready
          - Removed the shotgun floating in the air after the vault doors
       - Stage 6 & 7:
          - Tower elevator sound should be better synchronized
       
    # Versus, by night (New / Experimental):
       - Added cars & dumpsters
       - Added infected ladders to climb up inside the glass tower

  2.4 (2013-03-03):
    # Survival
       - Stage 7: New! Down in the Vault:
          - After the Tower Hold, walk down the wooden stairs to the Vault
          - Defend until the elevator is down
          - Escape with the submarine!
       - Shortened stages 3 and 6
       - Stage 1: Added lasers
       - Stage 4: Added pills and adre
       - Stage 4: Fixed an exploit that allowed a player to bypass the ladder 
         (thanks NF)
       - Fireworks fire at each stage end
    # Versus, by night (New / Experimental):
       - Tank Players have more chances to reach players
       - Tank Players can sneak on survivors
       - Note: Taaaank! Mutation has no time limit on tank possession (but 
               tanks are weaker)
    # General:
       - Updated the mod URL to point to the Workshop

  2.3 (2012-12-30):
    # Coop
       - Fixed the bot survivors who weren't entering the helicopters anymore
    # Survival
       - Stage 6 now has an "end"
       - Infected spawn closer to the game area, map is harder and more intense
       - End of Stage 1, down in the tower: Added a CLIP to prevent players 
         from jumping down directly from the top hole to the glass bridge, 
         incaping or killing them.
       - Added a few dumpsters/cars for tanks to play with
       - Stage 6: Opened all the tower walls

  2.2 (2012-12-09):
    # Coop
       - Few nav fixes
       - No more "Ghost Copter" in the skybox
       - Fixed the sloppy animation of the helicopter landing near the red 
         cross
    # Survival
       - Added a switch to teleport dead players at stage 3
       - Stage 4 has more common infected
       - Fixed the zombies falling directly into the water at stage 4 (thanks 
         JezMM)
       - Fixed a few items floating in the air
       - Removed ammo at stage 5 (zombie run)
       - Better lighting overall
       - Tanks spawn closer at Stage 6
    # Both
       - Infected only ladders look better (for Versus Survival and Taaaank 
         mutation)

  2.1 (2012-11-11):
    # Coop:
       - Added some defibs around the map
       - Added more stuff on the high ground over the building next to 
         pillars island
       - Fixed an exploit on pillars island (thanks to Gold_Saint & friends)
    # Survival:
       - Changed the way the stages timing work, now relative to each stage
       - Added 3 more stages after the stage formerly known as the Last Stand
       - Added visual hints and changed the indications to be more precise
       - Optimized the lightmaps scales to have better shadows

  2.0 (2012-09-23):
    # Survival:
       - First version, with stages (a bit like Helm's Deep)
    # Coop:
       - Fixed the buggy water
       - Added some more stuff at the start
       - Removed the glass on the high ground at the north west (pillars 
         island)
       - Fixed some minor texture alignement issues and brushes reflection in 
         the water
    # Both
       - Updated the loading poster, now supports wide screens

  1.2 (2012-07-08):
    - Bots now follow the player to the right rescue vehicule
    - Replaced the L4D2 survivors with the L4D1 ones
    - End music now longer restarts after 5s into the outro
    - Bots can now jump to the ladder at the end of the glass tunnel
    - Added a frame at the entrance of the glass tower
    - Widened a bit the space around the ladders
    - Tweaked the nav so the bots better follow the player
    - Bots will now grab their gear faster at start
    - Golf club and a fourth row of molo/pipe/bile/adre/pills added to the 
      start

  1.1 (2012-07-02)
    - Added Medkits
    - Made the rescue closet door breakable
    - Made the ladders near the red cross easier to see and climb down (should 
      be foolproof)
    - Fixed the nav leading to the secret passage (have you found it yet? :)
    - Added ledges to ease the jump from the plateform near the rescue closet 
      to the block under it
    - Updated the l4dmap URL of the mod in the vpk

  1.0 (2012-06-29)
    - Initial release

Plans -------------------------------------------------------------------------
  No plans for now

Misc notes --------------------------------------------------------------------
  - You should get at most 13 or 14 tanks on a vanilla L4D2 server in Campaign.
    This is due to the limit of the maximum number of players (tanks count as 
    players). If your server is modded and allows more players in play, you 
    should have more tanks.

Thanks to ---------------------------------------------------------------------
  - Lain for coming up with the original idea and giving me his feedback on the
    map before release. If you haven't played his maps yet, check them out:
      - TankFever1 Forever : http://www.l4dmaps.com/details.php?file=9381
      - TankFever4         : http://www.l4dmaps.com/details.php?file=10973
      - TankFever5         : http://www.l4dmaps.com/details.php?file=13814

    They are available on the Workshop too.

  - Feedback and test sessions: Necrofries, Zaphod Beeblebrox, Mister, Balledur
    LeonBlank & Matt (from =TF$=), NF, JezMM, Gold_Saint & friends, Airan,
    Rooky Moon, Eren.

  - The Teleport Dead Players script by The Fish, from Helm's Deep Reborn 1.6.
    http://www.l4dmaps.com/details.php?file=7302
