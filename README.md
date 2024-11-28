# Asteroids Game

This project is a clone of the [classic Asteroids arcade game](https://en.wikipedia.org/wiki/Asteroids_(video_game)), developed using Python and Pygame. It was created as part of the [Build Asteroids using Python and Pygame](https://www.boot.dev/courses/build-asteroids-python) course offered by [Boot.dev](https://www.boot.dev).

## Features

- **Player Control**: Navigate the spaceship using keyboard inputs.
- **Asteroid Generation**: Randomly generated asteroids that the player must avoid or destroy.
- **Collision Detection**: Interactive collisions between the spaceship, asteroids, and projectiles.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Fustincho/boot.dev-asteroids.git
   cd boot.dev-asteroids
   ```
2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

1. **Start the Game**:
   ```bash
   python main.py
   ```
2. **Controls**:
   - **Move**: Use the WASD keys to navigate the spaceship.
   - **Shoot**: Press the spacebar to fire projectiles at asteroids.
3. **Objective**:
   Destroy as many asteroids as possible without colliding with them.

## Acknowledgments

This project was developed as part of the [Build Asteroids using Python and Pygame](https://www.boot.dev/courses/build-asteroids-python) course by Boot.dev. Special thanks to the course instructor, Sarah Schulte, for her guidance.

## Backlog

- Add a scoring system
- Implement multiple lives and respawning
- Add an explosion effect for the asteroids
- Add acceleration to the player movement
- Make the objects wrap around the screen instead of disappearing
- Add a background image
- Create different weapon types
- Make the asteroids lumpy instead of perfectly round
- Make the ship have a triangular hit box instead of a circular one
- Add a shield power-up
- Add a speed power-up
- Add bombs that can be dropped

