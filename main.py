import sys
import random
import argparse
from typing import List, Final

class GlitchConfig:
    """Configuration constants for the glitch engine."""
    ANSI_RESET: Final[str] = "\033[0m"
    COLORS: Final[List[str]] = ["\033[91m", "\033[96m", "\033[95m", "\033[0m"]
    GLITCH_CHARS: Final[List[str]] = ["░", "▒", "▓", "█", "│", "─"]

class GlitchEngine:
    """Core logic for applying visual noise and artifacts to text strings."""

    def __init__(self, config: GlitchConfig = GlitchConfig()):
        self.config = config

    def apply_effect(self, text: str, intensity: float = 0.1) -> str:
        """
        Transforms input text with random visual artifacts and ANSI color escapes.
        
        Args:
            text: The raw input string.
            intensity: Probability (0.0 to 1.0) of a character being glitched.
        
        Returns:
            A string formatted with ANSI escape codes and glitch characters.
        """
        intensity = max(0.0, min(1.0, intensity))
        if not text:
            return ""

        result = []
        for char in text:
            if random.random() < intensity:
                result.append(random.choice(self.config.COLORS))
                if random.random() < 0.5:
                    result.extend([char, random.choice(self.config.GLITCH_CHARS)])
                else:
                    result.append(random.choice(self.config.GLITCH_CHARS))
            else:
                result.append(char)

        return f"{''.join(result)}{self.config.ANSI_RESET}"

def main() -> None:
    """CLI Entrypoint with input validation and stream handling."""
    parser = argparse.ArgumentParser(description="High-performance VHS/Text glitch utility.")
    parser.add_argument(
        "text", 
        nargs="?", 
        help="Text to transform. If omitted, reads from stdin."
    )
    parser.add_argument(
        "--intensity", 
        type=float, 
        default=0.1, 
        help="Glitch intensity (0.0 to 1.0). Default 0.1."
    )
    
    args = parser.parse_args()

    try:
        if args.text:
            input_text = args.text
        elif not sys.stdin.isatty():
            input_text = sys.stdin.read().strip()
        else:
            parser.print_help()
            sys.exit(0)

        if not input_text:
            return

        engine = GlitchEngine()
        sys.stdout.write(engine.apply_effect(input_text, args.intensity) + "\n")

    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"Error: {str(e)}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()