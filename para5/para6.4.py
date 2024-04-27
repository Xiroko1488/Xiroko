class BuidindgError(Exception):
    def __str__(self):
        return f"with so much materials the house cannot build!"

def check_material(amount_of_material, limit_material):
    if amount_of_material > limit_material:
        return "enough material"
    else:
        raise BuidindgError


material= 323
check_material(material, 300)
