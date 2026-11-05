# Snake Game (Python Turtle)

A Nokia-style Snake game built with Python's built-in Turtle graphics module.
Steer the snake to eat food and grow longer, without hitting the wall or your own tail.
Your best score is saved between sessions.

![Gameplay]

<img width="451" height="471" alt="image" src="https://github.com/user-attachments/assets/f9cd4bdd-c10d-487b-b10d-7a9d2e94389c" />

## Features
- Classic snake movement on a 600×600 board ⚠️
- Food appears at a random position each time it's eaten
- The snake grows by one segment per food
- Collision detection with the walls and the snake's own tail
- High score saved to `data.txt` and loaded on startup
- Automatic restart after a collision, keeping the high score ⚠️
- Object-oriented design, with each game component in its own class

## How to run
Requires Python 3. No extra packages: Turtle comes with Python.

## Controls
| Key | Action |
|---|---|
| ↑ Up arrow | Move up ⚠️ |
| ↓ Down arrow | Move down |
| ← Left arrow | Move left |
| → Right arrow | Move right |

The snake can't reverse straight into itself (for example, from moving right to moving left).

## Project structure
| File | Purpose |
|---|---|
| `main.py` | Sets up the screen, key bindings and game loop; checks collisions |
| `snake.py` | The snake's body segments, movement, growth and reset |
| `food.py` | The food: random placement after each bite |
| `scoreboard.py` | Current score, high score and saving the high score to file |
| `data.txt` | Stores the high score between sessions |

## What I learned
- Structuring a program with classes and inheritance (extending `Turtle`)
- Building a real-time game loop with `screen.tracer(0)`, `screen.update()` and `time.sleep()`
- Distance-based collision detection
- Reading and writing files to keep data between sessions, with error handling for a missing or empty file
   
   
