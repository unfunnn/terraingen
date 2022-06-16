# terraingen
A terrain generator with no graphics library based on cellular automata
## How it works
This program uses several layers of celluar automata to generate different layers of terrain. It supports 8 (1 unused) terrain types
Colour  | Type
------------- | -------------
Blue  | Ocean
Green  | Grass
Yellow  | Sand
Light Blue  | Shallow Ocean
Dark Green  | Trees
Purple | Flowers
Grey/Black | Mountains
White | Snow
Cyan (unused) | Even shallower ocean

You will need an ANSI colour supporting terminal for this since I challenged myself to not use any graphics libraries

## How to use
- Set your desired map size in the file 
  - 20 is minimum recommended, 40 is recommended, 150 is maximum recommended
- Set your desired intensity 
  - 0.3 - 0.6 produces the best results
- Edit the functions at the bottom to choose what layers are generated 
  - Some, like snow needing mountains and flowers needing forests, require others being active to work
- Run the file!

There is also an "animation" variable at the top, if you're curious you can turn it on for smaller map sizes (larger maps have intense flicker due to this being in the terminal)
