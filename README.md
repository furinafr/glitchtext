# GlitchText CLI

A lightweight Python command-line utility to aestheticize your terminal output with retro VHS-style glitch effects.

## Installation

Save the code to `glitch.py`.

## Usage

Direct argument:
```bash
python glitch.py "Hello World" --intensity 0.2
```

Piping output:
```bash
echo "System Failure imminent" | python glitch.py --intensity 0.5
```

## Features
- ANSI color shifting (Cyan/Magenta/Red).
- Character replacement with block elements.
- Adjustable intensity levels.