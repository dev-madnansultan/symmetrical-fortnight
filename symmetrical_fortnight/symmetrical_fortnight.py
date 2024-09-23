def generate_symmetry(text):
    """
    Generate a symmetrical version of the input text.
    
    Example: "fortnight" becomes "fortnight|thginrof"
    """
    mirrored = text[::-1]
    return f"{text}|{mirrored}"

def main():
    # User input
    user_text = input("Enter a word or phrase to generate symmetry: ")
    
    # Generate symmetrical text
    symmetrical_text = generate_symmetry(user_text)
    
    # Output the result
    print(f"Symmetrical version: {symmetrical_text}")

if __name__ == "__main__":
    main()
