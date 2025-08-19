"""
My breakout game 
최초작성일 : 2025-08-13
LastUpdate : 2025-08-13

BreakoutLite: a simple Breakout-like Gymnasium environment implemented with pygame.

Features
- Brick wall at the top; break bricks to earn +1 reward each
- Player paddle at bottom; move LEFT/RIGHT/NOOP (Discrete(3))
- Missed ball costs 1 life and -1 reward; episode ends when lives reach 0
- Level clear bonus +10 reward; auto-next-level with harder layout (optional)
- Paddle length can be configured at reset(options) or via method update_paddle_length()
- render_mode: "human" (interactive window with keyboard), "rgb_array" (numpy frame), "none"
- Observation: RGB pixel array (H, W, 3), dtype=uint8

Keyboard (human render only)
- ← / → : move paddle
- SPACE   : (re)launch ball if waiting on paddle
- P       : pause
- R       : reset level
- Q or ESC: quit

Notes
- This environment is intentionally lightweight and self-contained for RL study.
- For training, prefer render_mode="rgb_array"; for playing, use render_mode="human".

"""

import math, random, time
from dataclasses import dataclass
from typing import Optional, Tuple, List

import numpy as np
import pygame
import gymnasium as gym
from gymnasium import spaces

BALL_SPEED_INIT = 1
PADDLE_LEN_INIT = 36
LIVES_INIT = 3

# -----------------------------
# Config data classes
# -----------------------------
@dataclass
class Colors:
    BG = (10, 10, 20)
    PADDLE = (240, 240, 255)
    BALL = (255, 230, 120)
    BRICK_PALETTE = [
        (237,  64,  64), (252, 176,  64), (255, 236,  66),
        ( 87, 213,  87), ( 64, 160, 255), (176,  96, 255)
    ]
    TEXT = (230, 230, 230)


