# Alien Invasion
This is the educational project representing the game Alien Invasion

# Contents
- [How it works](#how-it-works)
- [Requirements](#requirements)
- [Quick start](#quick-start)
- [Architecture](#architecture)
- [Overview](#overview)

# How it works
The game is implemented in the Python programming language using the pygame library. The project was implemented according to the OOP paradigm.

# Requirements
```
pygame
```

# Quick start
Install the required dependencies and run the alien_invasion.py file

# Architecture
The project contains 8 files:
* 👾 alien_invasion.py - contains AlienInvasion class (main game class)
* 👽 alien.py - contains Alien class (init aliens, aliens logic)
* 🔫 bullet.py - contains Bullet class (init bullets, bullets logic)
* ⚙️ settings.py - contains Settings class (init main game settings)
* 🚀 ship.py - contains Ship class (init ship, ship logic)
* ▶️ button.py - contains Button class (init button, button logic) 
* 🏆 scoreboard.py - contains Scoreboard class (init scoreboard)
* 📶 game_stats.py - contains GameStats class (init game stats)

The Alien Invasion game contains 8 classes:
```python
class AlienInvasion   # The main class in the game. Main game logic.
```
```python
class Ship(Sprite)    # Create the ship
```
```python
class Settings        # All of the settings in the game
```
```python
class Alien(Sprite)   # Create aliens
```
```python
class Bullet(Sprite)  # Create bullets
```
```python
class GameStats       # Initialize main game stats
```
```python
class Button          # Initialize buttons
```
```python
class Scoreboard      # Initialize scoreboard
```

# Overview

The ship:

![Ship](https://github.com/xmzboy/Alien-Invasion/blob/main/readme_images/ship.PNG)
___

The intro window:

![Intro](https://github.com/xmzboy/Alien-Invasion/blob/main/readme_images/intro.PNG)
___

The Game:

![Game](https://github.com/xmzboy/Alien-Invasion/blob/main/readme_images/game.PNG)
___
