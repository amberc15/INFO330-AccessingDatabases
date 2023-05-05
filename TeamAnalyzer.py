import sqlite3  # This is the package for all sqlite3 access in Python
import sys      # This helps with command-line parameters
connection = sqlite3.connect("../pokemon.sqlite")

# All the "against" column suffixes:

types = ["bug","dark","dragon","electric","fairy","fight",
    "fire","flying","ghost","grass","ground","ice","normal",
    "poison","psychic","rock","steel","water"]

con = connection.cursor()
#testing = con.execute("SELECT * FROM pokemon").fetchall()
#print(testing)
#columnName = ("SELECT name FROM pokemon")
#print(columnName)


# Take six parameters on the command-line
if len(sys.argv) < 6:
    print("You must give me six Pokemon to analyze!")
    sys.exit()

team = []
for i, arg in enumerate(sys.argv):
    print("Analyzing " + arg)
    if i == 0:
        continue
    pokeName = con.execute("SELECT name FROM pokemon WHERE pokedex_number = " + arg ).fetchone()
    pokeFirstType = con.execute("SELECT type1 FROM pokemon_types_view WHERE name = '" + pokeName[0] + "'").fetchone()
    pokeSecondType = con.execute("SELECT type2 FROM pokemon_types_view WHERE name = '" + pokeName[0] + "'").fetchone()
    strengthsWeaknesses = con.execute("SELECT * FROM pokemon_types_battle_view WHERE type1name = '" + pokeFirstType[0] + "' AND type2name = '" + pokeSecondType[0] + "'").fetchone()
    newStrengthWeakness = strengthsWeaknesses[2:21]
    strongValues = []
    weakValues = []
    for i,value in enumerate(newStrengthWeakness):
        if value < 1.0:
            weakValues.append(types[i])
        if  value > 1.0:
            strongValues.append(types[i])
    print(pokeName[0] + " (" + pokeFirstType[0] + (" ") + pokeSecondType[0]+ ")" + " is strong against " + str(strongValues) + " but weak against " + str(weakValues))
 
    # Analyze the pokemon whose pokedex_number is in "arg"

    # You will need to write the SQL, extract the results, and compare
    # Remember to look at those "against_NNN" column values; greater than 1
    # means the Pokemon is strong against that type, and less than 1 means
    # the Pokemon is weak against that type

 

answer = input("Would you like to save this team? (Y)es or (N)o: ")
if answer.upper() == "Y" or answer.upper() == "YES":
    teamName = input("Enter the team name: ")

    # Write the pokemon team to the "teams" table
    print("Saving " + teamName + " ...")
else:
    print("Bye for now!")

