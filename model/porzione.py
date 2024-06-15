from dataclasses import dataclass


@dataclass
class Porzione:
    portion_id:int
    food_code:int
    portion_default:int
    portion_amount:float
    portion_display_name:str
    factor:float
    increment:float
    multiplier:float
    grains:float
    whole_grains:float
    vegetables:float
    orange_vegetables:float
    drkgreen_vegetables:float
    starchy_vegetables:float
    other_vegetables:float
    fruits:float
    milk:float
    meats:float
    soy:float
    drybeans_peas:float
    oils:float
    solid_fats:float
    added_sugars:float
    alcohol:float
    calories:float
    saturated_fats:float

    def __hash__(self):
        return hash(self.portion_id)

    def __str__(self):
        return f"{self.portion_display_name}"


