import sys
import random
import argparse

def glitch_text(text, intensity=0.1):
    colors = ['\033[91m', '\033[96m', '\033[95m', '\033[0m']
    glitch_chars = ['░', '▒', '▓', '█', '│', '─']
    result = []
    
    for char in text:
        if random.random() < intensity:
            # Apply color shift
            result.append(random.choice(colors))
            # Randomly jitter or replace char
            if random.random() < 0.5:
                result.append(char)
                result.append(random.choice(glitch_chars))
            else:
                result.append(random.choice(glitch_chars))
        else:
            result.append(char)
            
    return "".join(result) + '\033[0m'

def main():
    parser = argparse.ArgumentParser(description='Apply a VHS glitch effect to text.')
    parser.add_argument('text', nargs='?', help='Text to glitch (reads from stdin if empty)')
    parser.add_argument('--intensity', type=float, default=0.1, help='Glitch intensity (0.0 to 1.0)')
    args = parser.parse_args()

    input_text = args.text if args.text else sys.stdin.read().strip()
    if not input_text:
        return

    print(glitch_text(input_text, args.intensity))

if __name__ == '__main__':
    main()