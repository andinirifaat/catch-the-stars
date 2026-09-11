# Catch the Stars 

A simple beginner-friendly Python game made with **PyGame**.

The player controls a bucket and tries to catch falling stars.

## How to Play

- **Left Arrow** — move the bucket left
- **Right Arrow** — move the bucket right
- Catch a star → **+1 score**
- Miss a star → **-1 life**
- Start with **3 lives**
- The game becomes faster as your score increases
- **R** — restart after Game Over
- **ESC** — quit

## How to Run

Make sure Python is installed.

Install PyGame:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python main.py
```

## Python Concepts Demonstrated

This project intentionally uses basic Python concepts:

- Variables
- `if` conditions
- `while` loops
- `for` loops
- Functions
- Lists
- Dictionaries
- `return`
- Random numbers
- Basic object collision

## How the Game Works

The game repeatedly performs three main steps:

1. **Handle input** — check keyboard and window events.
2. **Update** — move the bucket and falling stars, then check collisions.
3. **Draw** — draw the updated game state on the screen.

This repeating process is called the **game loop**.

## Assets

No external image assets are required.

The bucket, stars, background, text, and other visual elements are generated directly with PyGame drawing functions. This makes the project easy to run and share.


