import re

# unit index
WEIGHT = {"g", "lb", "kg" "oz."}
VOLUME = {"mL", "L", "c", "tbs.", "tsp", "fl. oz."}
# make the conversion formulas


class ingredient:
    def __init__(self, name, amount, unit):
        """ingredient class
        used to handle the multiple attributes of each ingredient

        :str | Any name: ingredient name
        :str | Any amount: amount of ingredient
        :str | Any unit: unit of set amount for the ingredient
        """
        self.name = name
        self.amount = amount
        self.unit = unit

    # index of ingredient weight to volume conversion
    # For example, 1 cup of flour
    # (volume measurement) = 120g flour (weight measurement)
    def weightToVolume(self, density: int):
        """
        Mutates the ingredient amount to be in ml

        :ingreditent
        :density | in g/ml
        """

        match self.unit:
            case "g":
                self.amount = self.amount / density
            
            case "lb":
                self.amount /= 454
                self.amount = self.amount / density
            
            case "kg":
                self.amount /= 1000
                self.amount = self.amount / density
            
            case "oz.":
                self.amount /= 28.3495
                self.amount = self.amount / density
            
            case _:
                print("This ingredient does not have a valid unit.")


        return None

    def volumeToWeight(self, density: int):
        """
        Mutates the ingredient amount to be in grams
        density: g/ml
        """
        #note from katrina: i found these conversions on https://www.inchcalculator.com idk how to verify if they accurate lol
        match self.unit:
            case "mL":
                self.amount = self.amount * density
            case "L":
                self.amount = self.amount * density * 100
            case "c":
                #idk what c is
            case "tbsp.":
                self.amount = self.amount * density * 14.787
            case "tsp":
                self.amount = self.amount * density * 4.928922
            case "fl. oz.":
                self.amount = self.amount * density * 29.57353
            case _:
                print("This ingredient does not have a valid unit.")
      
        return None


def IMC():
    """
    Returns the volume of the ingredient
    If the units are a weight measurement, a conversion is made
    :return: None
    """

    recipe = userRecipe()

    print(recipe[0].name, recipe[0].amount, recipe[0].unit)

    conversion = input('''
    Do you have any ingredients you would like to
    convert to a different unit of measurement? (Y/N)
    ''')

    if conversion.upper() == "Y":
        conversionType = input('''
    Enter (1) for Volume to Weight conversions,
    Enter (2) for Weight to Volume conversions
    ''')
        if conversionType == 1:
            items = range(len(recipe))
            for x in items:
                density = int(input("Enter in {}'s density in grams").format(recipe[x].name))
                recipe[x].volumeToWeight(density)

        if conversionType == 2:
            items = range(len(recipe))
            for x in items:
                density = int(input("Enter in {}'s density in grams").format(recipe[x].name))
                recipe[x].weightToVolume(density)

    diffAmount = input('''
    Do you have an ingredient that does
    not meet the required amount in the recipe? (Y/N)
    ''')

    if diffAmount.upper() == "Y":
        scaleMeasurements(recipe)
    
    return None


def userRecipe() -> list[ingredient]:
    """userRecipe function
    Used to get a recipe from the user for use in the IMC
    by storing all ingredients in a list
    """

    recipe = []
    end = False

    while end is False:
        line = input('''
        Enter recipe ingredient and its set
        unit (official symbols only) separated by a space
        (enter 'exit' when done):
        ''')

        if "exit" in line:
            end = True
            break

        lineList = line.split()
        unitsAmounts = []

        match = re.match(r"([0-9]+)([a-z]+)", lineList[1].lower(), re.I)
        if match:
            unitsAmounts = match.groups()

        recipe.append(ingredient(lineList[0].lower(), unitsAmounts[0],
                                 unitsAmounts[1]))

    return recipe


def scaleMeasurements(recipe: list[ingredient]):
    """
    Returns the volume of the ingredient
    If the units are a weight measurement, a conversion is made
    :return: the volume of the ingredient
    """

    leastIngredient = input('''
    Enter the ingredient you have the least
    amount of (in regards to the recipe): ''')

    leastIngredientAmt = input("Enter the amount you have: ")

    items = range(len(recipe))
    scale = 0

    for x in items:
        if leastIngredient.lower() == recipe[x].name:
            scale = leastIngredientAmt / recipe[x].amount

    for x in items:
        recipe[x].amount = recipe[x].amount * scale
    
    return None


IMC()
