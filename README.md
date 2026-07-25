# 🚀 Titled Missile Game

> A 3D physics-based missile simulation game built with [Ursina Engine](https://www.ursinaengine.org/) and Python.

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Ursina](https://img.shields.io/badge/Ursina-8.3%2B-orange)](https://www.ursinaengine.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-In%20Development-yellow)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)]()

---

## 📖 About

**Titled Missile Game** is a 3D physics-based game where you control a missile in a simulated environment. The project features a custom-built physics engine with gravity, collision detection and resolution, all rendered using the Ursina 3D game engine.

The game is currently in active development. The primary target is desktop platforms (Windows, Linux, macOS), with Android support planned for a future release after the core experience is polished.

---

## ✨ Features

- 🎮 **Controllable Missile** — Rotate and maneuver the missile using keyboard input
- 🌍 **Custom Physics Engine** — Gravity, force accumulation, velocity integration
- 💥 **Collision System** — AABB/Box-shape collision detection and resolution
- 🔥 **Visual Feedback** — Fire effect toggles when thrusting
- 🧱 **Modular Architecture** — Clean separation of entities, physics, world, and core systems

---

## 🎮 Controls

| Key | Action |
|-----|--------|
| `W` | Tilt missile up |
| `S` | Tilt missile down |
| `A` | Tilt missile left |
| `D` | Tilt missile right |
| `Space` | Activate thruster (fire) |
| Mouse | Rotate camera (EditorCamera) |
| Scroll | Zoom camera in/out |

---

## 🏗️ Project Structure

```
titledmissilegame/
├── pyproject.toml          # Project metadata & dependencies
├── requirements.txt        # Pip dependencies
├── uv.lock                 # uv lock file
├── .gitignore
├── README.md
│
├── assets/                 # All visual/audio assets
│   ├── models/
│   ├── textures/
│   ├── sounds/
│   ├── music/
│   ├── fonts/
│   └── shaders/
│
├── saves/                  # Save files
│
├── configs/                # Game settings
│   ├── game.json
│   ├── graphics.json
│   └── controls.json
│
├── src/
│   ├── main.py             # Entry point — starts the Ursina app
│   │
│   ├── core/               # Engine-like systems
│   │   └── game.py         # Main game loop & initialization
│   │
│   ├── entities/           # Game objects
│   │   └── missile.py      # Missile entity with visuals & controls
│   │
│   ├── physics/            # Custom physics engine
│   │   ├── world.py        # Physics world (gravity, integration, collision)
│   │   ├── rigidbody.py    # Rigid body component
│   │   ├── collider.py     # Collider component
│   │   ├── shapes.py       # Collision shapes (Box, Sphere, etc.)
│   │   ├── raycast.py      # Raycasting utilities
│   │   └── materials.py    # Physics materials
│   │
│   ├── world/              # World & terrain systems
│   ├── systems/            # Game mechanics (combat, inventory, etc.)
│   ├── ui/                 # HUD & menus
│   └── utils/              # Math, file, debug helpers
│
└── tests/
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.13.5** or higher
- [uv](https://github.com/astral-sh/uv) (recommended) **or** pip

### Installation

#### Using `uv` (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/titledmissilegame.git
cd titledmissilegame

# Install dependencies
uv sync
```

#### Using `pip`

```bash
# Clone the repository
git clone https://github.com/yourusername/titledmissilegame.git
cd titledmissilegame

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Game

```bash
# With uv
uv run python src/main.py

# With pip / activated venv
python src/main.py
```

---

## 🗺️ Roadmap

### ✅ Completed
- [x] Basic project structure
- [x] Empty terrain / plot
- [x] Missile entity with visual components
- [x] Controllable missile (WASD rotation)
- [x] Custom physics engine structure
- [x] Gravity and basic force simulation
- [x] Collision detection (Box shapes)
- [x] Collision resolution (separation & velocity zeroing)

### 🔧 In Progress
- [ ] Complete physics engine
  - [x] Collision detection
  - [x] Collision resolution
  - [ ] Restitution (bounce)
  - [ ] Friction
  - [ ] Torque & angular velocity
  - [ ] Sphere / Capsule / Mesh shapes
  - [ ] Broad phase optimization (QuadTree / BVH)

### 📋 Planned
- [ ] Missile flight mechanics
- [ ] Dedicated camera object following the missile
- [ ] Mouse-controlled camera (orbit + scroll zoom)
- [ ] Missile tilts toward camera look direction
- [ ] Android port (after desktop version is stable)
- [ ] Mobile touch controls

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| [Python 3.13](https://www.python.org/) | Primary language |
| [Ursina Engine 8.3+](https://www.ursinaengine.org/) | 3D rendering & game loop |
| [uv](https://github.com/astral-sh/uv) | Package & environment management |

---

## 🏛️ Architecture

The project follows a modular, component-based architecture:

- **`PhysicsWorld`** — Manages all rigid bodies and colliders. Steps the simulation each frame (force accumulation → velocity integration → collision detection → resolution).
- **`RigidBody`** — Stores mass, velocity, accumulated force, gravity toggle, and static flag for each physics-enabled entity.
- **`Collider`** — Holds a list of shapes attached to an entity. Used in broad/narrow-phase collision checks.
- **`Missile`** — An Ursina `Entity` composed of sub-entities (top body, bottom body, fire effect) with rotation controls.
- **`Game`** — Wires everything together: creates the world, missile, attaches physics components, and dispatches input each frame.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/titledmissilegame/issues).

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Egemen** — [@egemngyk](https://github.com/egemngyk)

---

<p align="center">Made with ❤️ and Python</p>
