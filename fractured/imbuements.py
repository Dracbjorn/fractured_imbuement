from typing import Dict
from typing import List


imbuement_types = [
    "bonus endurance",
    "constitution",
    "critical damage",
    "fortitude",
    "health regeneration",
    "strength",
    "willpower",
    "acid resistance",
    "fire resistance",
    "ice resistance",
    "magic resistance",
    "poison resistance",
    "shock resistance",
    "accuracy",
    "critical chance",
    "detection",
    "dexterity",
    "evasion",
    "lockpicking",
    "luck",
    "perception",
    "stealth",
    "bonus mana",
    "charisma",
    "cooldown reduction",
    "intelligence",
    "lower mana cost",
    "mana regeneration",
]

armor_properties: Dict[str, List[str]] = {
accuracy
acid resistance
health
mana
detection
health regeneration
evasion
fire resistance
ice resistance
fortitude
luck
energy resistance
mana regeneration
willpower
poison resistance
shock resistance
stealth
magical damage reflection
physical damage efllection
cryomancy proficiency
geomancy proficiency
venomancy proficiency
vitrriomancy proficiency
druidcraft proficiency
necromancy proficiency
illusionism proficiency
leadership proficiency
assassination proficiency
hunting proficiency
warfare proficiency
knife fighting proficiency
swordsmanship proficiency
fencing proficiency
mace fighting proficiency
axe fighting proficiency
archery proficiency
abjurration proficiency
aeromancy proficiency
witchcraft proficiency
restoration proficiency
pyromancy proficiency
}

helmet_properties = armor_properties
chest_properties = armor_properties
arms_properties = armor_properties
boots_properties = armor_properties

amulet_properties: Dict[str, List[str]] = {
    "accuracy": ["soul", "destroy", "fire", "order"],
    "wisdom": [],
    "consitution": [],
    "cooldown reduction": [],
    "detection": [],
    "dexteity": [],
    "evasion": [],
    "fortitude": [],
    "intelligence": [],
    "lower mana": [],
    "luck": [],
    "willlpower": [],
    "perception": [],
    "stealth": [],
    "strength": [],
    "witchcraft proficiency": [],
}
shield_properties: Dict[str, List[str]] = {}
weapon_properties: Dict[str, List[str]] = {}
