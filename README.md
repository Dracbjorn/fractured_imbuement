# fractured_imbuement
An application used for finding the best alchemical reagents to imbue equipment in Fractured Online.

I'm going to start with creating a command line python application.  Once the logic is there and it works, we can then look at migrating it into a web app potentially.

1. Define Your Goals:

Specify the desired imbuement you want to achieve.
Determine the tier of the imbuement you're aiming for (Tier 1, Tier 2, or Tier 3).

2. Data Preparation:

Create a data structure to represent the properties of each of the 142 reagents, including the aspects and their respective points.
Store the requirements for each imbuement, such as the aspects and their minimum point thresholds.

3. Generate Combinations:

Generate all possible combinations of reagents that can be placed on the imbuing table. This is a combinatorial problem and can be implemented using recursive algorithms or itertools in Python.

4. Filter Combinations:

For each combination generated, calculate the cumulative aspect points for each aspect required by the desired imbuement.
Filter out combinations that do not meet the minimum aspect point requirements for the desired imbuement's tier.

5. Calculate Imbuement Probabilities:

For the remaining combinations, calculate the probability of getting the desired imbuement. This will depend on how many of the required aspects have enough points and whether there is a conflict with other imbuements (like the 50% chance for Accuracy or Wisdom).

6. Select the Best Combination:

Choose the combination that maximizes the probability of getting the desired imbuement.

7. Output:

Provide the list of reagents in the selected combination, along with the calculated probability.


## Psuedo Code for some logic to be expanded on and refined

Steps 2 to 3:

```
from itertools import combinations

def calculate_imbuement_probability(combination, desired_imbuement):
    # Calculate aspect points for the combination
    aspect_points = calculate_aspect_points(combination)
    
    # Check if the combination meets the aspect requirements for the desired imbuement
    if meets_aspect_requirements(aspect_points, desired_imbuement):
        # Calculate the probability of getting the desired imbuement
        probability = calculate_probability(desired_imbuement, aspect_points)
        return probability
    else:
        return 0  # Combination doesn't meet requirements

def find_best_combination(desired_imbuement, reagents):
    best_combination = None
    best_probability = 0
    
    # Generate all combinations of reagents
    for r in range(1, len(reagents) + 1):
        for combination in combinations(reagents, r):
            probability = calculate_imbuement_probability(combination, desired_imbuement)
            if probability > best_probability:
                best_combination = combination
                best_probability = probability
    
    return best_combination, best_probability

# Example usage:
desired_imbuement = {
    "name": "Accuracy",
    "aspects": {"Soul": 2, "Destroy": 2, "Fire": 2, "Order": 2}
}

best_combination, best_probability = find_best_combination(desired_imbuement, reagents)
print("Best Combination:", best_combination)
print("Probability:", best_probability)

```