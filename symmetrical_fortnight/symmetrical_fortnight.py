import argparse
import random

def generate_symmetry(text):
    """
    Generate a symmetrical version of the input text.
    Example: "fortnight" becomes "fortnight|thginrof"
    """
    if not text:
        return "Input cannot be empty."
    mirrored = text[::-1]
    return f"{text}|{mirrored}"

def generate_vertical_symmetry(text):
    """
    Generates a vertical mirrored symmetry where characters are reflected vertically.
    Example: "fort" becomes:
    f f
    o o
    r r
    t t
    """
    if not text:
        return "Input cannot be empty."
    return '\n'.join([f"{char} {char}" for char in text])

def generate_random_symmetry(text):
    """
    Generates a random shuffle of the text for a different symmetry-like effect.
    Example: "fortnight" becomes "fortnight|gfninhtort"
    """
    if not text:
        return "Input cannot be empty."
    shuffled = ''.join(random.sample(text, len(text)))
    return f"{text}|{shuffled}"

def main():
    parser = argparse.ArgumentParser(description="Generate symmetrical text patterns.")
    parser.add_argument("text", type=str, nargs='?', help="Text to generate symmetry for")
    parser.add_argument("--type", choices=['default', 'vertical', 'random'], default='default',
                        help="Type of symmetry to generate (default: horizontal)")
    parser.add_argument("--input", type=str, help="Input file containing text")
    parser.add_argument("--output", type=str, help="Output file to save symmetry result")

    args = parser.parse_args()

    # Check if input is from file or command-line
    if args.input:
        with open(args.input, 'r') as file:
            text = file.read().strip()
    elif args.text:
        text = args.text
    else:
        text = input("Enter a word or phrase to generate symmetry: ")

    # Generate the specified type of symmetry
    if args.type == 'default':
        symmetrical_text = generate_symmetry(text)
    elif args.type == 'vertical':
        symmetrical_text = generate_vertical_symmetry(text)
    elif args.type == 'random':
        symmetrical_text = generate_random_symmetry(text)

    # Output to file if specified
    if args.output:
        with open(args.output, 'w') as file:
            file.write(symmetrical_text)
        print(f"Symmetry saved to {args.output}")
    else:
        print(f"Symmetrical version:\n{symmetrical_text}")

if __name__ == "__main__":
    main()
