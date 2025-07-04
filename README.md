# 🧠 Pac-Man with HMM-Enhanced Ghost AI

This project simulates a simplified version of Pac-Man in which the ghost uses a **Hidden Markov Model (HMM)** to estimate Pac-Man’s location based on indirect observations. The ghost then uses **A\*** pathfinding to pursue the most likely position. The goal is to demonstrate how probabilistic reasoning and search algorithms can be integrated into game AI.

---

## 🎮 Features

- A grid-based maze with walls and walkable tiles
- A player-controlled Pac-Man (arrow keys)
- A ghost that:
  - Infers Pac-Man’s position using the **Forward Algorithm**
  - Maintains a belief state (heatmap) over time
  - Navigates toward the most likely location using **A\*** search
- A `pygame` visualizer showing:
  - The maze
  - Pac-Man (yellow)
  - The ghost (red)
  - A blue-shaded belief map showing where the ghost thinks Pac-Man might be

---

## 🧠 Algorithms Used

- **Hidden Markov Model (HMM)**  
  - Forward algorithm for probabilistic belief updates
- **A\* Search**  
  - Maze pathfinding with Manhattan-distance heuristic
- **Grid-based Simulation**  
  - Basic movement logic, collision with walls

---

## 📂 Project Structure

- TBD
