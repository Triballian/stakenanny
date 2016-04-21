#functional_tests

import os
os.chdir('\\Users\\Noe\\workspace\\stakenanny\\src')
#import stakenanny.py

import imp 
imp.load_source('stakenanny','stakenanny.py')
import stakenanny

# Jody set the stakenani.conf to the appropriate path and kept the wallets he did not want to run at None
assert 'turbostake' in stakenanny.envars['coinlist']
# coinlist diplays a list of coins suported buy stakenanny sperated buy a comma, example digicube,turbostake
# check list of supported coins. to be set in coinfig file coinlist=digicube,turbostake coins will be run in the order listed
# check for duplicate listings and duplicate coinlist entry's 
# Jody gets an error complaining that a listed coin is not supported buy stakenanny. Change the config file to reflect what is listed. use coinlist to see what conis are suppored

# He runs the command or batch file python test_stakenany.py on the commandline or link. #the app will provide a batch file for him to use. probably
# the app states that python3 is required to run this app. This is good as even I can make the mistake of using the wrong python vesion
# the app states that another intance of stakenani is already runnig as an exit statement would
# he turns the other instance off. and reruns stakeanny
# stakenanny asks for a username a password to use for wallet remote control
# stakenanny check to see if any of the assigned wallets is already running.
# Stakenanny ask the user if you wants you to restart the running coins with nanny settings enabled. 
# stakenanny turns on each stake coin in the order of presitence you establish. you can check your order by typing
# startup order coin startup order
# you can change your order by typing the name of the wllet and the number of presetence you want for that coin
# the rest of the coins will shift accordingly
# wallet start will start the process of turning on the wallets
# stakenanny gives jody a print of each wallet as it turns on and is ready to start another.
# stakestatus lists all the coins which are currently staking and how much they are staking
# stakestatus spendable tells you how much staked coins is spendable in each wallet for the last 24 hours
# stakestatus yesterday tells you how much each wallet staked as of 12am today from the day before.
# stakestatus sellthird gives you a calculation of 1/3 of what was staked as of 12am today from the day before
# the app automatically displays a summary at the top of the screen.