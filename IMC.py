import re

# unit index
WEIGHT = {"g", "lb", "kg" "oz."}
VOLUME = {"mL", "L", "c", "tbs.", "tsp", "fl. oz."}


class ingredient:
    def __init__(self, name: str, amount: int, unit: str):
        """ingredient class
        used to handle the multiple attributes of each ingredient

        :str name: ingredient name
        :int amount: amount of ingredient
        :str unit: unit of set amount for the ingredient
        """
        self.name = name
        self.amount = amount
        self.unit = unit

    def weightToVolume(self, density: int):
        """weightToVolume function
        Mutates the ingredient amount to be in ml
        :int density: density of ingredient in g/ml
        """

        match self.unit:
            case "g":
                self.amount = self.amount / density
                self.unit = "ml"

            case "lb":
                self.amount /= 454
                self.amount = self.amount / density
                self.unit = "ml"

            case "kg":
                self.amount /= 1000
                self.amount = self.amount / density
                self.unit = "ml"

            case "oz.":
                self.amount /= 28.3495
                self.amount = self.amount / density
                self.unit = "ml"

            case _:
                print(self.name + """
                ingredient is already in a volumetric unit,
                or does not have a valid unit
                within this application.""")

        print("Conversion completed. The ingredient units have been adjusted.")

        return None

    def volumeToWeight(self, density: int):
        """volumeToWeight function
        Mutates the ingredient amount to be in grams
        :int density: g/ml
        """

        match self.unit:
            case "ml":
                self.amount = self.amount * density
                self.unit = "g"
            case "L":
                self.amount = self.amount * density * 100
                self.unit = "g"
            case "c":
                self.amount = self.amount * 0.004227
                self.unit = "g"
            case "tbsp.":
                self.amount = self.amount * density * 14.787
                self.unit = "g"
            case "tsp":
                self.amount = self.amount * density * 4.928922
                self.unit = "g"
            case "fl. oz.":
                self.amount = self.amount * density * 29.57353
                self.unit = "g"
            case _:
                print(self.name + """
                ingredient is already in a volumetric unit,
                or does not have a valid unit
                within this application.""")

        print("Conversion completed. The ingredient units have been adjusted.")

        return None


def IMC(recipe: list[ingredient]):
    """IMC function
    Returns the volume of the ingredient
    If the units are a weight measurement, a conversion is made
    :list: list of ingredient objects
    :return: None
    """
    if recipe == []:
        recipe = userRecipe()

    conversion = input('''
    Do you have any ingredients you would like to
    convert to a different unit of measurement? (Y/N)
    ''')

    if conversion.upper() == "Y":
        conversionType = int(input('''
    Enter (1) for Volume to Weight conversions,
    Enter (2) for Weight to Volume conversions
    '''))
        if conversionType == 1:
            items = range(len(recipe))
            for x in items:
                density = int(input("""
                Enter in """ + recipe[x].name + """ density in grams: """))
                recipe[x].volumeToWeight(density)

        if conversionType == 2:
            items = range(len(recipe))
            for x in items:
                density = int(input("""
                Enter in """ + recipe[x].name + """ density in grams: """))
                recipe[x].weightToVolume(density)

    diffAmount = input('''
    Do you have an ingredient that does
    not meet the required amount in the recipe? (Y/N)
    ''')

    if diffAmount.upper() == "Y":
        scaleMeasurements(recipe)

    items = range(len(recipe))

    for x in items:
        print(recipe[x].name, recipe[x].amount, recipe[x].unit)

    return None


def userRecipe() -> list[ingredient]:
    """userRecipe function
    Used to get a recipe from the user for use in the IMC
    by storing all ingredients in a list
    :return: list of ingredients
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

        recipe.append(ingredient(lineList[0].lower(), int(unitsAmounts[0]),
                                 unitsAmounts[1]))

    return recipe


def scaleMeasurements(recipe: list[ingredient]):
    """scaleMeasurements function
    Returns the volume of the ingredient
    If the units are a weight measurement, a conversion is made
    :return: the volume of the ingredient
    """

    leastIngredient = input('''
    Enter the ingredient you have the least
    amount of (in regards to the recipe): ''')

    leastIngredientAmt = int(input("Enter the amount you have: "))

    items = range(len(recipe))
    scale = 0

    for x in items:
        if leastIngredient.lower() == recipe[x].name:
            scale = leastIngredientAmt / recipe[x].amount

    for x in items:
        recipe[x].amount = recipe[x].amount * scale

    print("Scaling completed. All ingredient measurements have been adjusted.")

    return None
