import re

# unit index
WEIGHT = {'grams', 'pounds', 'kilograms' 'ounces'}
VOLUME = {'millilitres', 'litres', 'cups', 'tablespoons', 'teaspoons',
          'fluid ounces'}
# make the conversion formulas

class ingredient:
    def __init__(self, name, amount, unit):
        """ingredient class
        used to handle the multiple attributes of each ingredient

        :str name: ingredient name
        :str | Any amount: amount of ingredient
        :str | Any unit: unit of set amount for the ingredient
        """
        self.name = name
        self.amount = amount
        self.unit = unit

    def weight(self):
        """
        Returns the weight of the ingredient
        If the units are volumetric, a conversion is made
        :return: the weight of the ingredient
        """
        if self.unit not in WEIGHT:
            self.volumeToWeight()
        return self.amount + " " + self.unit

    def volume(self):
        """
        Returns the volume of the ingredient
        If the units are a weight measurement, a conversion is made
        :return: the volume of the ingredient
        """
        if self.unit not in VOLUME:
            self.weightToVolume()
        return self.amount + " " + self.unit

    # index of ingredient weight to volume conversion
    # For example, 1 cup of flour
    # (volume measurement) = 120g flour (weight measurement)
    def weightToVolume(self):
        
        return None

    def volumeToWeight(self):
        
        return None


def IMC():
    """
    Returns the volume of the ingredient
    If the units are a weight measurement, a conversion is made
    :return: the volume of the ingredient
    """

    recipe = userRecipe()

    print(recipe[0].name, recipe[0].amount, recipe[0].unit)

    # 
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
                recipe[x].volumeToWeight()

     if conversionType == 2:
            items = range(len(recipe))
            for x in items:
                recipe[x].weightToVolume()

    diffAmount = input('''
    Do you have an ingredient that does
    not meet the required amount in the recipe? (Y/N)
    ''')

    if diffAmount.upper() == "Y":
        scaleMeasurements(recipe)


def userRecipe():
    """userRecipe function
    Used to get a recipe from the user for use in the IMC
    by storing all ingredients in a list
    """

    recipe = []
    end = False

    while end is False:
        line = input('''
        Enter recipe ingredient and its set
        unit separated by a space
        (enter 'exit' when done):
        ''')

        if "exit" in line:
            end = True
            break

        lineList = line.split()
        match = re.match(r"([0-9]+)([a-z]+)", lineList[1].lower(), re.I)
        if match:
            unitsAmounts = match.groups()

        recipe.append(ingredient(lineList[0].lower(), unitsAmounts[0],
                                 unitsAmounts[1]))

    return recipe


def scaleMeasurements(recipe):
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

    for x in items:
        if leastIngredient.lower() == recipe[x].name:
            scale = leastIngredientAmt / recipe[x].amount

    for x in items:
        recipe[x].amount = recipe[x].amount * scale
    return

IMC()
