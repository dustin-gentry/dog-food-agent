from google.adk.agents import Agent

def calculate_dog_food_batch(cooked_protein_g: float) -> dict:
    """Calculate ingredient weights for a 50/30/20 dog food batch.

    Args:
        cooked_protein_g: Cooked weight of the protein ingredient in grams,
            such as cooked chicken. This is food weight, not nutrient grams.
    """
    if not 0 < cooked_protein_g < float("inf"):
        return {"error": "Enter a positive, finite cooked weight in grams."}

    total_batch_g = cooked_protein_g / 0.50

    return {
        "cooked_protein_g": round(cooked_protein_g, 1),
        "carb_ingredient_g": round(total_batch_g * 0.30, 1),
        "vegetable_blend_g": round(total_batch_g * 0.20, 1),
        "total_batch_g": round(total_batch_g, 1),
    }

root_agent = Agent(
    name="dog_food_agent",
    model="gemini-3.6-flash",
    description="Scales a 50/30/20 dog food recipe from cooked protein weight.",
    instruction="""
You help the user scale their dog food recipe by ingredient weight.

The recipe is 50% cooked protein ingredient, 30% carb ingredient,
and 20% vegetable blend. The vegetable blend usually contains broccoli,
green beans, and spinach. Treat it as one combined weight.

If the user hasn't provided the cooked weight of the protein ingredient
in grams, ask for it. If they give a weight without saying whether it's
raw or cooked, confirm it before calculating.

Call calculate_dog_food_batch to do the math. Report the cooked protein
ingredient, carb ingredient, vegetable blend, and total batch weight
in grams. If the tool returns an error, ask the user for a valid weight.

Do not invent a split between individual vegetables or claim that the
recipe is nutritionally complete.
""",
    tools=[calculate_dog_food_batch],
)