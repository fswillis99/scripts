#!/usr/bin/env python3
"""Generate pose, clothing, and appearance descriptions for AI image prompts."""

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

# --- Hair building blocks ---

HAIR_LENGTHS = [
    "short",
    "chin-length",
    "shoulder-length",
    "long",
    "waist-length",
]

HAIR_COLORS = [
    "jet black",
    "dark brown",
    "warm chestnut",
    "honey blonde",
    "platinum blonde",
    "strawberry blonde",
    "auburn",
    "copper red",
    "ash grey",
    "deep burgundy",
    "ombre dark-to-blonde",
]

HAIR_TEXTURES = [
    "straight",
    "softly wavy",
    "loosely curled",
    "tightly coiled",
    "sleek",
    "textured",
    "windswept",
]

HAIR_ARRANGEMENTS = [
    "worn loose",
    "swept back loosely",
    "pulled into a low bun",
    "in a high ponytail",
    "in a messy updo",
    "parted down the middle",
    "tucked behind one ear",
    "in soft waves around her face",
    "braided over one shoulder",
    "pinned up with a few loose strands framing her face",
]

HAIR_TEMPLATES = [
    lambda length, color, texture, arrangement: f"Her {color} hair is {length} and {texture}, {arrangement}.",
    lambda length, color, texture, arrangement: f"She has {length} {texture} {color} hair, {arrangement}.",
    lambda length, color, texture, arrangement: f"Her {length} {color} hair is {texture}, {arrangement}.",
]

# --- Facial building blocks ---

EYE_COLORS = [
    "dark brown",
    "hazel",
    "green",
    "blue-grey",
    "amber",
    "deep blue",
    "grey",
]

FACIAL_EXPRESSIONS = [
    "a calm, composed expression",
    "a soft smile",
    "a confident, direct expression",
    "a gentle, relaxed look",
    "a subtle, knowing smile",
    "a serene, neutral expression",
    "a warm, open expression",
    "a quietly intense gaze",
]

MAKEUP_STYLES = [
    "minimal makeup",
    "a natural, barely-there look",
    "bold red lips and simple eye makeup",
    "a smoky eye with nude lips",
    "dewy skin with a flush of color on the cheeks",
    "a classic cat-eye liner",
    "glossy lips and mascara",
    "a warm bronze eye look",
    "a monochromatic rose-toned makeup",
]

SKIN_TONES = [
    "fair",
    "light",
    "medium",
    "olive",
    "tan",
    "deep brown",
    "dark",
]

FACIAL_TEMPLATES = [
    lambda eyes, expression, makeup, tone: f"She has {tone} skin and {eyes} eyes, wearing {makeup}, with {expression}.",
    lambda eyes, expression, makeup, tone: f"Her {tone} complexion and {eyes} eyes are complemented by {makeup} and {expression}.",
    lambda eyes, expression, makeup, tone: f"With {tone} skin, {eyes} eyes, and {makeup}, she wears {expression}.",
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


def generate_hair() -> str:
    length = random.choice(HAIR_LENGTHS)
    color = random.choice(HAIR_COLORS)
    texture = random.choice(HAIR_TEXTURES)
    arrangement = random.choice(HAIR_ARRANGEMENTS)
    template = random.choice(HAIR_TEMPLATES)
    return template(length, color, texture, arrangement)


def generate_facial() -> str:
    eyes = random.choice(EYE_COLORS)
    expression = random.choice(FACIAL_EXPRESSIONS)
    makeup = random.choice(MAKEUP_STYLES)
    tone = random.choice(SKIN_TONES)
    template = random.choice(FACIAL_TEMPLATES)
    return template(eyes, expression, makeup, tone)


def main():
    parser = argparse.ArgumentParser(
        description="Generate pose, clothing, and appearance descriptions for AI image prompts."
    )
    parser.add_argument(
        "-n", "--count", type=int, default=5, help="Number of sets to generate (default: 5)"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--pose-only", action="store_true", help="Output pose descriptions only")
    group.add_argument("--clothing-only", action="store_true", help="Output clothing descriptions only")
    group.add_argument("--hair-only", action="store_true", help="Output hair descriptions only")
    group.add_argument("--facial-only", action="store_true", help="Output facial descriptions only")
    args = parser.parse_args()

    for i in range(1, args.count + 1):
        print(f"--- Set {i} ---")
        if args.pose_only:
            print(generate_pose())
        elif args.clothing_only:
            print(generate_clothing())
        elif args.hair_only:
            print(generate_hair())
        elif args.facial_only:
            print(generate_facial())
        else:
            print(generate_pose() + " " + generate_clothing() + " " + generate_hair() + " " + generate_facial())
        print()


if __name__ == "__main__":
    main()
