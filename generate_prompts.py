#!/usr/bin/env python3
"""Generate pose and women's clothing descriptions for AI image prompts."""

import random
import argparse

# --- Pose building blocks ---

BODY_POSITIONS = [
    ("stands", "standing"),
    ("sits", "sitting"),
    ("leans against a wall", "leaning against a wall"),
    ("crouches slightly", "crouching slightly"),
    ("kneels", "kneeling"),
    ("walks forward", "walking forward"),
    ("reclines", "reclining"),
    ("perches on the edge of a surface", "perched on the edge of a surface"),
    ("stands with one leg slightly forward", "standing with one leg slightly forward"),
    ("turns slightly to the side", "turned slightly to the side"),
]

ARM_DETAILS = [
    "hands resting on her hips",
    "arms loosely at her sides",
    "one hand raised to her hair",
    "arms gently crossed",
    "one hand resting on her chin",
    "fingers lightly touching her collarbone",
    "one arm extended toward the camera",
    "hands clasped in front of her",
    "one hand tucked into a pocket",
    "arms slightly behind her, shoulders back",
    "one hand resting on a nearby surface",
    "fingers lightly intertwined in front of her",
]

GAZE_DIRECTIONS = [
    "looking directly into the camera",
    "gazing slightly off to one side",
    "glancing over her shoulder",
    "eyes cast softly downward",
    "looking upward with a gentle expression",
    "head tilted, gaze angled away",
    "eyes half-closed, relaxed expression",
    "looking toward a distant point",
    "making direct eye contact",
    "glancing down with a slight smile",
]

POSE_TEMPLATES = [
    lambda pos, arms, gaze: f"She {pos[0]}, {arms}, {gaze}.",
    lambda pos, arms, gaze: f"{pos[1].capitalize()}, with {arms}, she is {gaze}.",
    lambda pos, arms, gaze: f"She is {pos[1]}, {gaze}, with {arms}.",
]

# --- Clothing building blocks ---

GARMENTS = [
    "sundress",
    "midi skirt and fitted blouse",
    "slip dress",
    "tailored blazer and wide-leg trousers",
    "flowy wrap dress",
    "high-waisted jeans and cropped top",
    "trench coat over a simple dress",
    "bodycon dress",
    "linen co-ord set",
    "oversized knit sweater and mini skirt",
    "silk camisole and wide-leg pants",
    "structured sheath dress",
    "denim jacket over a floral dress",
    "off-shoulder blouse and fitted trousers",
    "pleated midi dress",
]

COLORS = [
    "ivory",
    "deep burgundy",
    "sage green",
    "classic black",
    "soft blush",
    "cobalt blue",
    "warm terracotta",
    "crisp white",
    "dusty mauve",
    "rich emerald",
    "camel",
    "charcoal grey",
    "champagne",
    "navy",
    "rust orange",
]

FABRICS = [
    "linen",
    "flowing chiffon",
    "silk",
    "fitted knit",
    "soft cotton",
    "satin",
    "lightweight wool",
    "jersey",
    "velvet",
    "crepe",
]

CLOTHING_DETAILS = [
    "with a cinched waist",
    "with delicate ruching at the sides",
    "featuring an off-the-shoulder neckline",
    "with a subtle high slit",
    "with tailored lapels",
    "with billowing sleeves",
    "accented with fine stitching",
    "with a draped neckline",
    "with a tie-waist detail",
    "with a wrap front",
    "with subtle pleating",
    "with a deep V-neckline",
    "with flutter sleeves",
    "with a square neckline",
    "with a relaxed, oversized fit",
]

CLOTHING_TEMPLATES = [
    lambda color, fabric, garment, detail: f"She wears a {color} {fabric} {garment} {detail}.",
    lambda color, fabric, garment, detail: f"Her outfit is a {color} {garment} in {fabric} {detail}.",
    lambda color, fabric, garment, detail: f"She is dressed in a {color} {fabric} {garment} {detail}.",
]


def generate_pose() -> str:
    pos = random.choice(BODY_POSITIONS)
    arms = random.choice(ARM_DETAILS)
    gaze = random.choice(GAZE_DIRECTIONS)
    template = random.choice(POSE_TEMPLATES)
    return template(pos, arms, gaze)


def generate_clothing() -> str:
    color = random.choice(COLORS)
    fabric = random.choice(FABRICS)
    garment = random.choice(GARMENTS)
    detail = random.choice(CLOTHING_DETAILS)
    template = random.choice(CLOTHING_TEMPLATES)
    return template(color, fabric, garment, detail)


def main():
    parser = argparse.ArgumentParser(
        description="Generate pose and clothing descriptions for AI image prompts."
    )
    parser.add_argument(
        "-n", "--count", type=int, default=5, help="Number of sets to generate (default: 5)"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--pose-only", action="store_true", help="Output pose descriptions only")
    group.add_argument(
        "--clothing-only", action="store_true", help="Output clothing descriptions only"
    )
    args = parser.parse_args()

    for i in range(1, args.count + 1):
        print(f"--- Set {i} ---")
        if args.pose_only:
            print(generate_pose())
        elif args.clothing_only:
            print(generate_clothing())
        else:
            print(generate_pose() + " " + generate_clothing())
        print()


if __name__ == "__main__":
    main()
