# Gesture-based-Tic-Tac-Toe-
 
This project implements a gesture-controlled version of Tic Tac Toe using Python and OpenCV. Players can interact with the game board and make moves using hand gestures detected through a webcam.

## Features

- Real-time hand tracking and gesture recognition using MediaPipe
- Gestures mapped to game controls like placing markers, resetting board etc.  
- Integrated game logic for Tic Tac Toe rules and win conditions
- AI opponent using Minimax algorithm with alpha-beta pruning 
- Interactive GUI and visuals using PyGame

## Getting Started

### Prerequisites

- Python 3.8+
- OpenCV 4.5
- MediaPipe 0.8
- PyGame 2.0

### Installation

1. Clone the repository
   ```
   git clone https://github.com/vedzzz28/Gesture-based-Tic-Tac-Toe-
   ```
2. Install dependencies
   ```
   pip install -r requirements.txt
   ```
   
### Usage

Run the main script:

```
python camera.py
python tic_tac_toe.py
```

Follow on-screen prompts to play the game using hand gestures like pinches, spreads etc.

Use ` Esc` key to quit.

## Gesture Controls

- Move index finger - Move cursor 
- Pinch index finger & thumb - Place marker / Select

## Authors

  - Vedansh Rathi (https://github.com/vedzzz28)
  - Shrey Sharma [Contributor]

## Acknowledgments

- [MediaPipe](https://mediapipe.dev) for hand tracking
- Tutorials and algorithms from OpenCV, PyGame documentation
