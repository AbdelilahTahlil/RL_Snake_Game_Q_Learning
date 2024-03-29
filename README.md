# Snake Game using Q-Learning Algorithm
## Overview

I am excited to share with you my very first Reinforcement Learning model! 


I have used for my first project of the kind a classic and old game, the Snake Game. The learning model is based on the [Q-Learning Algorithm](https://en.wikipedia.org/wiki/Q-learning). 

<p float="left", align="middle">
    <img width="300" height="250" src="screenshots/snake_game_plot.gif">
    <img width="300" height="250" src="screenshots/snake_game.gif">
</p>

As it is my first time coding a python game, I was inspired by the work of Patrick Loeber and Michael Sequin. [This is the link to their version of the game and AI Model](https://github.com/python-engineer/snake-ai-pytorch). 

Although both our codes share many similarities, I have added my own touch and made major modifications both on the game environment and the AI agent.

The similarities and the differences are detailed below.

![Table of game similarities and differences](screenshots/table%20of%20similarities.jpg)


## Installation

1. Clone the repository in your target location.
2. Install the requirements.
```
pip install -r requirements.txt
```
3. Run the game. The arguments are optional.
```
python run_game.py --num_obstacles <num_obstacles> --width <width> --height <height> --speed <speed>
```

### Optional arguments:
options:  
 **-h**, **--help** : show help message and exit  
 **--width** : set the width of the game window (default=640)  
  **--height** :                   set the height of game window (default=480)  
  **--num-obstacles** : set the number of obstacles within the game (default=5)  
  **--speed** : set the speed of the snake (default=100)

