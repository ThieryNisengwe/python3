from classes.ninja import Ninja
from classes.pirate import Pirate

# make a function that continues the fight till someones health gets to zero 
# step 1 make a function
# step 2 


michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()
jack_sparrow.attack(michelangelo)
michelangelo.show_stats() 