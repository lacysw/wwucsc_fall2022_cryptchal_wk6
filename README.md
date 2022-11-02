# WWU Cybersecurity Club Challenge (FALL '22, WEEK 6)

Once again, we have *another* cryptography challenge (hurrah for creativity). Jokes aside, here's the breakdown:

 - There is a Python file called `shidcrypt.py` in the root of this repo. It lives up to its name in terms of security.
 - `shidcrypt.py` takes as input the contents of adjacent file `secret.txt`.
 - `shidcrypt.py` manipulates the contents of `secret.txt` in some way, the output of which has been conveniently placed within adjacent file `output.shd`.
 - But, *gasp*, I accidentally put `secret.txt` in `.gitignore`! The only information we have regarding the contents of `secret.txt` is its format: `wwucsc{some_text_here}`.

## Goal

**The goal:** retrieve the original text of `secret.txt`. You may use any tools you like, but I ask that the solution not be posted in #challenges until ample time has been given for others to complete it.

## How to Play
```bash
# Get challenge
git clone https://github.com/lacysw/wwucsc_fall2022_cryptchal_wk6.git
cd wwucsc_fall2022_cryptchal_wk6

# Write your decrypter (it doesn't have to be in Python)
touch decrypter.py

# Got the flag? DM any of the @Officers!
```

*Note: `secret.txt` contains a Steam key for [Deathloop](https://store.steampowered.com/agecheck/app/1252330/) – our gift to you. The first person to solve the challenge, naturally, gets to redeem the key (or post it in the club Discord if they don't want it). Please leave a message in #challenges if you redeem the key.*

Have fun ;)
