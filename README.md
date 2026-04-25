<img width="800" height="450" alt="image" src="https://github.com/user-attachments/assets/ebfc79e7-d569-440a-ba9f-f50a40c65a00" />


# Open Design and Technology

## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository

After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example

`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:

- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules

- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name

`Project^2`

## 1.2 Team Members

| Name           | Primary Role                    | Secondary Role | Strengths Brought to the Project |
| -------------- | ------------------------------- | -------------- | -------------------------------- |
| `Mukund Gupta` | `[Electronics / Coding / App ]` | `Fabrication`  | `Programming, Software `         |
| `Manan Gupta`  | `[Electronics / Fabrication]`   | `[Coding]`     | `Material Handling, Hardware`    |

## 1.3 Project Title

`"Project Project"`

`(because Project-or)`

<img width="1600" height="1131" alt="image" src="https://github.com/user-attachments/assets/c64bfbd4-b3b7-43d9-83ad-c203a5aa11bc" />

## 1.4 One-Line Pitch

`A projected, fully customizable game world where a real RC car interacts with and reacts to dynamic virtual obstacles in real time.`

## 1.5 Expanded Project Idea

In 1–2 paragraphs, explain:

- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`This project is a hybrid play system where a physical RC car interacts with a projection-mapped game. A virtual map is projected on the floor, forming a play area. The car's position and orientation are tracked via an arUko marker, which allows us to place its coordinates virtually and get the projected environment to react to the cars movement.
This can be expanded to have levels and form a customizable experience.`

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem

This module does **not** require your project to solve a large social problem.

You are allowed to build:

- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?

Answer the following:

- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
`This is a playful mixed-reality experience where a physical RC car interacts with a projected virtual world. The player moves the car in real space, while the system tracks its position and responds through dynamic visuals like obstacles, paths, and game objectives.

The experience is meant to feel responsive, slightly unpredictable, and engaging, like controlling a real object inside a digital game. Players feel a sense of control, curiosity, and challenge as they navigate through levels. The combination of physical movement and virtual feedback makes it satisfying to experiment with.

Someone would want to try it again because the projected environment can change: new layouts, rules, and mechanics can be introduced easily, making each playthrough feel different.`

## 2.3 Design Persona

Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`We are designing this project as if we are a small creative studio making a playable interactive experience for exhibition visitors and classmates.`

---

# 3. Inspiration

## 3.1 References

List what inspired the project.

| Source Type | Title / Link                                                        | What Inspired You                                                                         |
| ----------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `[Video]`   | `https://www.instagram.com/reel/DW4CT7WCDry/?igsh=cXg3dzAxYmdncDBo` | `How projection mapping can be used to create interactive digital + physical experiences` |
|             |                                                                     |                                                                                           |
|             |                                                                     |                                                                                           |

## 3.2 Original Twist

What makes your project original?

**Response:**  
`The project combines projection mapping and real-time camera tracking to turn any flat surface into a fully customizable game environment. Unlike typical AR or projection setups, the physical car directly interacts with a projected world that can be reconfigured instantly by changing layouts, obstacles, and rules without modifying the hardware.

The key originality lies in treating the projection as a dynamic game engine for a physical object, where the same setup can support multiple game modes and experiences simply by changing the projected system.`

---

# 4. Project Intent

## 4.1 Core Interaction Loop

Describe the main loop of interaction.

Examples:

- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
`track car → map position → check obstacles → send movement → car moves → system reacts → repeat`

## 4.2 Intended Player / Audience

| Question                            | Response                                                                                         |
| ----------------------------------- | ------------------------------------------------------------------------------------------------ |
| Who is this for?                    | `No specific demographic, anyone who is interested`                                              |
| Age range                           | `9+ (but intuitive enough for younger children to play)`                                         |
| Solo or multiplayer                 | `Currently Solo, can be expanded`                                                                |
| Expected duration of one round      | `~three minutes`                                                                                 |
| What should the player feel?        | `Curious, engaged, slightly challenged, and in control of a “real object inside a digital game”` |
| Is explanation required before use? | `minimial (move car to goal, avoid obstacles)`                                                   |

## 4.3 Player Journey

Describe exactly how a player will use the project.

1. **Approach:** `The player sees a projected map on a surface with a physical car placed within it.`
2. **Start:** `The system is already running; the player is told they can control the car.`
3. **First Action:** `The player begins moving the car toward a visible target area.`
4. **Main Interaction:** `The player navigates the car through obstacles while the system tracks its position and updates the projection in real time.`
5. **System Response:** `Obstacles highlight when the car is close, block movement when necessary, and the system reacts visually to the car’s position.`
6. **Win / Lose / End Condition:** `Reaching the target block completes the level and advances to the next one.`
7. **Reset:** `After finishing all 3 levels (or restarting), the game resets to the first level automatically.`

## 4.4 Rules of Play

If your project is a game, list the rules clearly.

- Reach the highlighted target area to complete each level
- Avoid colliding with obstacles
- Movement may be restricted if an obstacle is too close
- Complete all 3 levels to finish the game

---

# 5. Definition of Success

## 5.1 Definition of “Playable”

Your project will be considered complete only if these conditions are met.

- [x] `Player can control the car remotely`
- [x] `Car interacts with the virtual obstacles`
- [x] `Car position is accurately tracked in real time`
- [x] `At least one complete level can be played from start to finish`
- [x] `System responds consistently (movement blocking / visual feedback works reliably)`

## 5.2 Minimum Viable Version

What is the smallest version of this project that still delivers the core experience?

**Response:**  
`User can control the car within a projected play area, where its position is tracked in real time and it interacts with virtual obstacles. The system prevents movement into obstacles and provides feedback, and at least one level includes a clear start and goal condition.`

## 5.3 Stretch Features

What features are nice to have but not essential?

- Customizable maps, where players can create their own obstacle layouts

- Use camera-based color tracking to interact with real-world objects instead of only virtual ones
* More levels with increasing difficulty and different mechanics; Coul more interaction (collecting artefacts)

* [Implemented] Visual effects (animations, feedback when near obstacles, level transitions)

* Sound feedback (collision, success, ambient effects)

---

# 6. System Overview

## 6.1 Project Type

Check all that apply.

- [x] Electronics-based

- [ ] Mechanical

- [x] Sensor-based

- [x] App-connected

- [x] Motorized

- [ ] Sound-based

- [x] Light-based

- [x] Screen/UI-based

- [x] Fabricated structure

- [x] Game logic based

- [x] Installation

- [ ] Other:

## 6.2 High-Level System Description

Explain how the system works in simple terms.

Include:

- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
The camera feed is processed on a laptop using computer vision to detect the car and map its position into a virtual coordinate system. This position is then used to update a projected game environment in real time, including obstacles and goal areas.

When the player attempts to move the car, the system checks whether movement in that direction is allowed (e.g., no obstacle nearby). Based on this logic, commands are sent to the ESP32, which controls the motors of the car.

The physical structure includes the car chassis with motors and a marker (along with structures to block light), while the digital system includes the projection, tracking, and game logic. The interaction between these creates a feedback loop between the real and virtual worlds.

## 6.3 Input / Output Map

| System Part                              | Type            | What It Does                                                               |
| ---------------------------------------- | --------------- | -------------------------------------------------------------------------- |
| `Controller (Laptop Interface: W/A/S/D)` | Input           | `Sends movement commands (forward, back, left, right)`                     |
| `Camera (Phone mounted on top)`          | Input           | `Captures real-world view and detects ArUco markers`                       |
| `Laptop (Python + OpenCV + Pygame)`      | Processing      | `Tracks car position, runs game logic, checks collisions, maps projection` |
| `ESP32`                                  | Processing      | `Receives commands and controls motor driver`                              |
| `Motors (via driver module)`             | Output          | `Moves the car physically`                                                 |
| `Projector`                              | Output          | `Displays the virtual game environment`                                    |
| `Car chassis + marker`                   | Physical Action | `Moves in real space and interacts with projected world`                   |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch

Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

Example:

```md

```

<img width="1559" height="1233" alt="image" src="https://github.com/user-attachments/assets/695c6d44-1e1b-4834-aabb-da8c1e412a38" />

## 7.2 Labeled Build Sketch

Add a sketch with labels showing:

- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`
<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/95637f31-b4e7-4427-a9e1-4b63fbeb0ac5" />

## 7.3 Approximate Dimensions

| Dimension        | Value   |
| ---------------- | ------- |
| Length           | `16 cm` |
| Width            | `16 cm` |
| Height           | `8 cm`  |
| Estimated weight | `400 g` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features

Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [ ] Linkages
- [ ] Hinges
- [x] Shafts
- [ ] Springs
- [ ] Bearings
- [x] Wheels
- [ ] Sliders
- [ ] Levers
- [ ] Not applicable

## 8.2 Mechanical Description

Describe the mechanism and what it is meant to do.

**Response:**  
`The system consists of a small two-wheel drive car powered by DC motors connected to wheels via motor shafts. The motors are mounted onto a fabricated chassis, designed to hold them firmly in place to prevent wobble or misalignment.

A third contact point (caster or low-friction base) is used to balance the car and maintain stability while moving. The chassis also holds the electronics, battery, and an ArUco marker on top for tracking.

The mechanism is designed for simple differential drive: both wheels rotate together for forward/backward movement, and in opposite directions for turning or rotating in place.`

## 8.3 Motion Planning

If something moves, explain:

- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`

**What moves:**  
The two main wheels rotate to drive the car, while the chassis moves across the surface.

**What causes the movement:**  
DC motors controlled by the ESP32 (via a motor driver) generate rotation in the wheels.

**How far it moves:**  
The car moves freely within the defined projection area, typically covering the full mapped surface (table/floor area).

**How fast it moves:**  
Speed is controlled using PWM, allowing slower, controlled movement for accuracy. The speed is intentionally limited to maintain tracking stability and precision.

**What could go wrong:**

- Uneven motor speeds causing the car to drift
- Friction or imbalance (especially from the rear support) affecting smooth movement
- Wheels slipping on the surface
- Loose motor mounting causing instability
- Sudden movements reducing tracking accuracy
- Power fluctuations affecting motor performance`

## 8.4 Simulation / CAD / Animation Before Making

If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used                      | File / Link                                                                                                                          | What Was Tested |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| `Blender models for structure` | <img width="1919" height="966" alt="image" src="https://github.com/user-attachments/assets/a8234488-b156-4dbd-a5b8-23a683820646" />
 |                 |
| `                              | `How the car can look, variations`                                                                                                   |                 |
| `Fusion 360`                   | `<img width="1600" height="851" alt="image" src="https://github.com/user-attachments/assets/12ef0a31-bbdf-4af5-913d-1f90316582fd" /> |                 |
| `                              | `Final physical form with accurate dimensions`                                                                                       |                 |

## 8.5 Changes After Digital Testing

What changed after the CAD, animation, or simulation stage?

**Response:**  
`Updated the size of structure for all components to fit inside the structure. Updated the "lid" design to properly fit. `

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component                 | Quantity | Purpose                               |
| ------------------------- | --------:| ------------------------------------- |
| `[ESP32]`                 | `1`      | `[Main controller]`                   |
| `[L298N Motor Driver]`    | `1`      | `[Control Motors]`                    |
| `[BO Motors]`             | `2`      | `[Rotate wheels]`                     |
| `[Buck Converter]`        | `1`      | `[Power ESP32]`                       |
| `[Li Ion Battery Pack]`   | `2`      | `[Power]`                             |
| `[Projector]`             | `1`      | `[Display obstacles]`                 |
| `Camera (Webcam / Phone)` | `1`      | `[Tracks car position using markers]` |

## 9.2 Wiring Plan

Describe the main electrical connections.

**Response:**  
`The ESP32 is connected to the motor driver (L298N) using four GPIO pins (18,19; 22,23) to control motor direction (IN1, IN2, IN3, IN4). Two PWM-capable pins (ENA and ENB; 25 and 26) are connected to control the speed of each motor.

The motors are connected to the output terminals of the motor driver. The motor driver is powered directly by the battery pack (higher voltage), while the ESP32 receives regulated 5V from the buck converter.

All components share a common ground to ensure stable operation. The projector and camera are connected to the laptop, which handles tracking and game logic separately.`

## 9.3 Circuit Diagram

Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`
<img width="867" height="1156" alt="WhatsApp Image 2026-04-24 at 9 35 27 AM" src="https://github.com/user-attachments/assets/2154c287-b58a-4205-98c3-1c93e1b00565" />


## 9.4 Power Plan

| Question         | Response                                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Power source     | `Battery (Li-ion pack)`                                                                                                                           |
| Voltage required | `~6–8.4V for motors (via driver), stepped down to 5V for ESP32 (buck converter)`                                                                  |
| Current concerns | `Motors can draw high current under load, which may cause voltage drops affecting ESP32 and WiFi stability`                                       |
| Safety concerns  | `Avoid over-discharging Li-ion batteries, ensure proper voltage regulation, prevent short circuits, and secure wiring to avoid loose connections` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform                | Purpose                                        |
| ------------------------------ | ---------------------------------------------- |
| `[MicroPython]`                | `Control ESP32`                                |
| `[Python/PyGame/OpenCV]`       | `Track markers, game logic, create projection` |
| `[Fusion/Blender/Illustrator]` | `[Prototyping structure]`                      |
|                                |                                                |

## 10.2 Software Logic

Describe what the code must do.

Include:

- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`

- **Startup behavior:**  
  The ESP32 initializes motor pins, PWM control, and starts a WiFi access point with a web server. The laptop initializes camera input, tracking system, and projection mapping.
- **Input handling:**  
  Movement commands are received from the laptop (pygame sends http requests)
- **Sensor reading:**  
  The camera continuously captures frames, and OpenCV detects ArUco markers to determine the car’s position and orientation.
- **Decision logic:**  
  The system maps the car’s position into a virtual coordinate system and checks for nearby obstacles or collisions. If movement is valid, the command is allowed; if not, it is blocked or replaced with a feedback action (like a slight shake).
- **Output behavior:**  
  The ESP32 drives the motors using PWM signals to control speed and direction. The projector displays the updated game environment, including obstacles, targets, and feedback visuals.
- **Communication logic:**  
  The laptop sends HTTP requests (e.g., `/forward`, `/left`) to the ESP32 over WiFi. The ESP32 parses these commands and executes motor actions.
- **Reset behavior:**  
  If no command is received within a short timeout, the ESP32 stops the motors. The game resets when a level is completed or restarted.`

## 10.3 Code Flowchart

Insert a flowchart showing your code logic.

Suggested sequence:

- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/42706d87-4e7e-4f83-b7e4-22ad84d44350" />
<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/66b36423-4d29-474a-9683-0b5e29e17555" />



## 10.4 Pseudocode

```text
START

INITIALIZE ESP32
INITIALIZE CAMERA + TRACKING
INITIALIZE PROJECTION SYSTEM

LOOP:

    CAPTURE camera frame
    DETECT ArUco markers

    IF corner markers detected:
        CALCULATE homography (camera → game space)

    IF car marker detected:
        MAP car position to game space
        SMOOTH position

    READ user input (button / control command)

    CHECK if movement direction is valid:
        IF obstacle nearby:
            BLOCK movement
            SEND "shake" or stop command
        ELSE:
            SEND movement command to ESP32

    ESP32 RECEIVES command:
        SET motor direction
        APPLY PWM speed

    UPDATE projected visuals:
        DRAW car, obstacles, feedback

    IF level goal reached:
        LOAD next level or reset

    IF no input for timeout:
        STOP motors

REPEAT
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?

- [ ] Yes
- [x] No

If yes, complete this section.

## 11.2 Why is the app needed?

Explain what the app adds to the experience.

Examples:

- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`[Write here]`

## 11.3 App Features

| Feature                             | Purpose     |
| ----------------------------------- | ----------- |
| `[Bluetooth connect button]`        | `[Purpose]` |
| `[Score display]`                   | `[Purpose]` |
| `[Control button / slider / label]` | `[Purpose]` |

## 11.4 UI Mockup

Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item                             | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec               | Why This Choice?          |
| -------------------------------- | --------:| ------- | ------------ | --------------:| ----------------------------- | ------------------------- |
| `[ESP32]`                        | `1`      | `Yes`   | `No`         | `0`            | `38 Pin ESP32`                | `[To control components]` |
| `[Motor Driver]`                 | `[1]`    | `[Yes]` | `[No]`       | `0`            | `[LN296]`                     | `[To drive both motors]`  |
| `[DC Motors and wheel]`          | `[2]`    | `[No]`  | `[Yes]`      | `[150]`        | `[BO Motors and 6 cm wheels]` | `[high torque motors]`    |
| `[Buck Converter]`               | `[1]`    | `[No]`  | `[Yes]`      | `[75]`         |                               |                           |
| `[Li-ion batteries with holder]` | `[1]`    | `[No]`  | `[Yes]`      | `[200]`        |                               |                           |

## 12.2 Material Justification

Explain why you selected your main materials and components.

Examples:

- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`MDF was used for laser cutting instead of 3D printing due to time constraints, as laser cutting allows rapid prototyping and quick iteration of designs. It also provides sufficient structural rigidity for the chassis while being easy to modify if needed.`

`DC motors (BO motors) were chosen instead of servos or steppers because the system requires continuous rotation for movement rather than precise angular control (Previously, we were considering using steppers as we were planning on tracking movement on the ESP using its relative position from an origin, but since we're using a camera now, this is not required). A motor driver (L298N) was used to allow bidirectional control and speed variation using PWM.`

`A simple low-friction support (instead of a complex caster wheel mechanism) was used to reduce fabrication complexity while still maintaining stability for short-term use during the exhibition.`

## 12.3 Items to Purchase Separately

| Item                 | Why Needed               | Purchase Link | Latest Safe Date to Procure | Status       |
| -------------------- | ------------------------ | ------------- | --------------------------- | ------------ |
| `BO Motors + Wheels` | `Drive system for car`   | `robu.in`     | `15th April`                | `[Received]` |
| `Buck Converter`     | `Stable power for ESP32` | `local store` | `before testing`            | `[Received]` |
| `Li-ion Batteries`   | `Portable power`         | `local store` | `before testing`            | `Recieved`   |

## 12.4 Budget Summary

| Budget Item           | Estimated Cost              |
| --------------------- | ---------------------------:|
| Electronics           | `[400]`                     |
| Mechanical parts      | `[200]`                     |
| Fabrication materials | `[0 (Available on campus)]` |
| Purchased extras      | `[0]`                       |
| Contingency           | `[300]`                     |
| **Total**             | `[900]`                     |

## 12.5 Budget Reflection

If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`The design already prioritizes low-cost, commonly available components, making it flexible to scale down if needed. Projector can be obtained in-house.`

---

# 13. Planning the Work

## 13.1 Team Working Agreement

Write how your team will work together.

Include:

- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
`Tasks are divided based on areas of focus: electronics (ESP32 + motor control), software (tracking + projection + game logic), and fabrication (chassis and assembly). Each member takes primary responsibility for one area while collaborating during integration.`

## 13.2 Task Breakdown

| Task ID | Task                    | Owner    | Estimated Hours | Deadline     | Dependency | Status |
| ------- | ----------------------- | -------- | ---------------:| ------------ | ---------- | ------ |
| T1      | `[Finalize concept]`    | `[Both]` | `2`             | `1st April`  | `None`     | `Done` |
| T2      | `[Complete BOM]`        | `[Mukund]` | `1`             | `8th April`  | `T1`       | `Done` |
| T3      | `[Test electronics]`    | `[Mukund]` | `2`             | `15th April` | `T1`       | `Done` |
| T4      | `[Build structure]`     | `[Manan]` | `4`             | `18th April` | `T1`       | `Done` |
| T5      | `[Write control code]`  | `[Mukund]` | `4`             | `18th April` | `T3`       | `Done` |
| T6      | `[Integrate system]`    | `[Manan]` | `4`             | `19th April` | `T4, T5`   | `Done` |
| T7      | `[Playtest]`            | `[Manan]` | `2`             | `21st April` | `T6`       | `Done` |
| T8      | `[Refine and document]` | `[Mukund]` | `3`             | `22nd April` | `T7`       | `Done` |

## 13.3 Responsibility Split

| Area                 | Main Owner | Support Owner |
| -------------------- | ---------- | ------------- |
| Concept and gameplay | `[Manan]`  | `[Mukund]`    |
| Electronics          | `[Mukund]` | `[Manan]`     |
| Coding               | `[Mukund]` | `[Manan]`     |
| App                  | `[NA]`     | `[NA]`        |
| Mechanical build     | `[Manan]`  | `[Mukund]`    |
| Testing              | `[Manan]`  | `[Mukund]`    |
| Documentation        | `[Mukund]` | `[Manan]`     |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk

Expected outcomes:

- [x] Idea finalized
- [x] Core interaction decided
- [x] Sketches made
- [x] BOM completed
- [x] Purchase needs identified
- [ ] Key uncertainty identified
- [x] Basic feasibility tested

### Week 2 — Build Subsystems

Expected outcomes:

- [x] Electronics tests completed
- [ ] CAD / structure planning completed
- [ ] App UI started if needed
- [x] Mechanical concept tested
- [x] Main subsystems partially working

### Week 3 — Integrate

Expected outcomes:

- [x] Physical body built
- [x] Electronics integrated
- [x] Code connected to hardware
- [ ] App connected if required
- [x] First playable version exists

### Week 4 — Refine and Finish

Expected outcomes:

- [x] Technical bugs reduced
- [x] Playtesting completed
- [x] Improvements made
- [x] Documentation completed
- [x] Final build ready

## 14.2 Weekly Update Log

| Week   | Planned Goal   | What Actually Happened | What Changed   | Next Steps     |
| ------ | -------------- | ---------------------- | -------------- | -------------- |
| Week 1 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |
| Week 2 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |
| Week 3 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |
| Week 4 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk                                                            | Type         | Likelihood | Impact   | Mitigation Plan                                                                       | Owner                |
| --------------------------------------------------------------- | ------------ | ---------- | -------- | ------------------------------------------------------------------------------------- | -------------------- |
| WiFi connection between laptop and ESP32 becomes unstable       | `Technical`  | `Medium`   | `High`   | Keep ESP32 close, ensure stable power supply, reduce network load, add fail-safe stop | `[Mukund]`           |
| Camera tracking becomes jittery or loses marker during movement | `Technical`  | `High`     | `Medium` | Improve lighting, tune camera settings, add smoothing and limit speed                 | `[Manan]`            |
| Car drifts due to uneven motor speeds or friction               | `Mechanical` | `High`     | `Medium` | Calibrate motor speeds, reduce friction (better caster), adjust PWM values            | `[Mukund and Manan]` |
| Projection misalignment with physical space`                    | `Technical`  | `Medium`   | `High`   | Manual calibration using draggable points before gameplay                             | `[Manan]`            |
| Power fluctuations from battery affecting motors/WiFi           | `Electrical` | `Medium`   | `High`   | Use stable voltage via buck converter, ensure batteries are charged                   | `[Mukund]`           |

## 15.2 Biggest Unknown Right Now

What is the single biggest uncertainty in your project at this stage?

**Response:**  
`The biggest uncertainty is maintaining reliable real-time tracking while the car is moving at higher speeds. While tracking works well when the car is stationary, motion introduces jitter and occasional loss of detection, which directly affects gameplay responsiveness and accuracy.`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing     | How You Will Test It                                                                 | Success Condition                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| `[Wifi connection]`    | `[Check if motor spins via app button]`                                              | `[Both motors accurately respond to wifi signals]`                                                   |
| `[Marker tracking]`    | `[Setup markers and check position and orientation]`                                 | `[OpenCV accurately displays a rectangle around the arUko marker along with an arrow for direction]` |
| `[Obstacle Detection]` | `[Move physcal markers and set vistual obstacles to cahnge color when intersecting]` | `[Multiple objects display color change in real time when moving the marker]`                        |

## 16.2 Playtesting Plan

| Question                             | How You Will Check                                                                           |
| ------------------------------------ | -------------------------------------------------------------------------------------------- |
| Do players understand what to do?    | `Show the setup without explanation and observe if they start controlling the car correctly` |
| Is the interaction satisfying?       | `Observe reactions (engagement, frustration) and ask for quick feedback after playing`       |
| Do players want another turn?        | `See if they voluntarily replay or ask to try again`                                         |
| Is the challenge balanced?           | `Watch if players complete levels too easily or struggle too much`                           |
| Is the response clear and immediate? | `Check if players notice the car stopping/shaking instantly when near obstacles`             |

## 16.3 Testing and Debugging Log

| Date          | Problem Found                         | Type         | What You Tried                                | Result               | Next Action                                    |
| ------------- | ------------------------------------- | ------------ | --------------------------------------------- | -------------------- | ---------------------------------------------- |
| `18th April`  | `Car not balancing properly`          | `Mechanical` | `Add low-friction caster support to one side` | `Worked`             | `improve caster structure`                     |
| `[20th April` | `Car drifting to one side`            | `Mechanical` | `Adjusted PWM values for each motor`          | `Worked fairly well` | `Fine-tune further`                            |
| `20th April`  | `Tracking jitter when car moves fast` | `Technical`  | `Added smoothing and limited movement steps`  | `Partly`             | `Improve Lighting and camera angle (top down)` |

## 16.4 Playtesting Notes

| Tester      | What They Did                        | What Confused Them                    | What They Enjoyed                         | What You Will Change                          |
| ----------- | ------------------------------------ | ------------------------------------- | ----------------------------------------- | --------------------------------------------- |
| `Classmate` | `Tried navigating through obstacles` | `Some obstacles ewren't clear enough` | `Liked projection + real car interaction` | `Add a slight red highlight around obstacles` |
| `Friend`    | `Tested movement controls`           | `Unsure about goal initially`         | `Liked level progression idea`            | `Add clear start/end indicators`              |

---

# 17. Build Documentation

## 17.1 Fabrication Process

Describe how the project was physically made.

Include:

- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`The fabrication process involved designing, manufacturing, assembling, and refining both the physical structure and electronic integration of the system.`

`Design (CAD Modeling):
The initial model was created using CAD software, where components were designed based on the actual dimensions of the electronic parts. This ensured accurate fitting and minimized errors during assembly.
Cutting (Laser Cutting):
The designed parts were fabricated using laser cutting techniques. Sheets were cut precisely according to the CAD model to create the structural base and mounts for components.`

`Components were fixed using adhesives and mechanical supports. Certain parts were intentionally kept modular (not permanently fixed) to allow easy replacement and modification of electronics.
Surface Finishing:
Some parts were sanded to smooth rough edges after cutting. Sawdust mixed with adhesive was used to fill gaps and uneven edges, improving structural finish. The final structure was then painted for better aesthetics and durability.`

`Environment Setup (Dark Room Fabrication):
To enhance projection visibility, a controlled dark environment was created using Z-boards, paper sheets, and bedsheets. This minimized external light interference and improved projection clarity.
Revisions and Iterations:
Multiple adjustments were made throughout the process, including refining alignment, improving structural stability, repositioning components, and optimizing the interaction between the physical car and projected environment.`

## 17.2 Build Photos

Add photos throughout the project.

Suggested images:

- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.
- <img width="960" height="1280" alt="WhatsApp Image 2026-04-24 at 9 46 02 AM (1)" src="https://github.com/user-attachments/assets/74baa570-5770-483e-be6d-d2f03386e37c" />

<img width="1280" height="960" alt="WhatsApp Image 2026-04-24 at 9 46 02 AM" src="https://github.com/user-attachments/assets/249d0757-08fc-4539-a53d-eebeecb1dfe9" />
<img width="1280" height="960" alt="WhatsApp Image 2026-04-24 at 9 46 03 AM" src="https://github.com/user-attachments/assets/832a13aa-64fb-4d61-8eb9-af2de39f7f0f" />
<img width="1280" height="960" alt="WhatsApp Image 2026-04-24 at 9 46 03 AM (3)" src="https://github.com/user-attachments/assets/53e1b241-035e-4f2d-9da8-8637af0d94ab" />
<img width="867" height="1156" alt="image" src="https://github.com/user-attachments/assets/9ff87177-1cd9-47f8-87e1-8ff1e99b06a0" />

<img width="1280" height="960" alt="WhatsApp Image 2026-04-24 at 9 46 04 AM" src="https://github.com/user-attachments/assets/66cf90f6-58d0-4da1-8a4e-5718cfd02c81" />


<img width="1280" height="960" alt="WhatsApp Image 2026-04-24 at 9 46 03 AM (2)" src="https://github.com/user-attachments/assets/3a62ce9c-10dd-47c8-aa2c-abdf86f1d55a" />

<img width="960" height="1280" alt="WhatsApp Image 2026-04-24 at 9 46 03 AM (1)" src="https://github.com/user-attachments/assets/3053a2b0-1c81-44df-a153-90555a41ce06" />

<img width="867" height="1156" alt="WhatsApp Image 2026-04-23 at 11 43 13 AM" src="https://github.com/user-attachments/assets/5c96dc82-32f7-4cbc-919c-0e5fc85683d9" />



## 17.3 Version History

| Version | Date     | What Changed | Why        |
| ------- | -------- | ------------ | ---------- |
| `v1`    | `17th April` | `Cardboard Prototype` | `Quick test of components and movement` |
| `v2`    | `18th April` | `Better, Firmer structure` | `making it less flimsy` |
| `v3`    | `20th April` | `Final lazer cut model` | `Structure, aesthetics` |

---

# 18. Final Outcome

## 18.1 Final Description

Describe the final version of your project.

**Response:**  
`The final version looked and felt like a proper game, especially with the drawn game maps. The game logic intself was fairly simple to understand since it takes from a lot of common game tropes. The caster on the car was situated only on one side, which ended up adding a bit more playfulness since when the car stopped suddenly(when "hitting" an obstacle), it veered forward almost like suspension. The entire projected structure, especially in the dark, looked visually imersive, though daytime visibility could be improved by adding a full covered fabrication/tent.`

## 18.2 What Works Well

- `Car tracks accurately`
- `Projection and car is able to react in real time`
- `Scaffolding around projector makes it fairly visible even during the day`
- `visual feedback clealy comunicated interaction`

## 18.3 What Still Needs Improvement

- `Power Supply to car died quickly, causing wifi to fluctuate`
- `Sound effects and a customizable game flow could be integrated.`
- `More interction between the projection and car, like trails behind it. `

## 18.4 What Changed From the Original Plan

How did the project change from the initial idea?

**Response:**  
`The first concept involved the esp32 tracking its own relative position by using stepper motors and a relative coordinate system, so the map and the car's system would be fully separate. We steered from this idea since we realized that motors can sometimes skip steps and the missed values can pile up due to friction, causing tracking to become highly inacurate over time. We switched to a camera-based tracking system, which fixed the alignment issue and woul also allow us to have to projection react to the car's movement i real-time (currently the obstacles turn yellow when car is close, and blue when car is touching. This could also be expanded to have to car leave a traiool behind it.).`
`Our very first idea was about a physical obstacle course, but using the current virtual one allowed the project to be more interesting both to play and design.   It opens up the possibilty for further digital/physical interaction, and is not just limited to games.`

---

# 19. Reflection

## 19.1 Team Reflection

What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`We mamnaged to use the time we had farily well, integrating the core MVP along with some of our stretch features like projection interaction. We worked efficiently when breaking the project into smaller parts (tracking, motor control, projection), and then integrating them.

What slowed us down was debugging across systems especially when issues could come from hardware, power supply, or code at the same time. Integration took longer than expected because small problems (like motor imbalance or WiFi instability) affected the whole system.

Overall, task division worked well, but we realized that testing integration earlier would have saved time.
The final outcome `

## 19.2 Technical Reflection

What did you learn about:

- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`The foremost learning was how to get virtual and physical systems to interact with each other. We used arUko markers, OpenCV and PyGame to create not only an immersive environment but a real-time tracking system for interaction as well. 
In mechanisms and fabrication, we saw how small physical details (like wheel balance or caster friction) significantly affect behavior. Rapid prototyping using laser cutting helped us iterate quickly.
In coding, we worked with real-time systems using Python, OpenCV, and MicroPython, and learned how to handle tracking noise using smoothing and constraints. We also learned how to efficiently and properly send and manage communication between devices over WiFi.`

## 19.3 Design Reflection

What did you learn about:

- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`We learned that designing for play is not just about functionality, but about responsiveness and feedback. Small details like the car shaking slightly when blocked or obstacles changing color made the interaction more engaging and understandable. Visual feedback helped communicate rules naturally.`
`We also realized the importance of iteration. Moving from a physical obstacle course to a projected one made the system more flexible and interesting, and allowed us to explore more possibilities.`
`Overall, the project showed how combining physical interaction with digital feedback can create a more immersive and playful experience.`

## 19.4 If You Had One More Week

What would you improve next?

**Response:**  
`The structure could be more secure allowing for a more permanent place for the camera. Adding a led backplate to the aruko marker on the car would allow it to be tracked better, since in dark environments the tracking stutters when it goes slightly outside of the projection area. We could also make the borders be an obstacles, not allowing the car to go outside of the boundry.`
`If we had another week we could have integrated most of our stretch features, including physical object detection so that players can place actual objects in the path of the car and the system could detect that as well (if the object was of a set color). This would allow for more of an immersive experience, and blur the line further between digital and physical interaction.`

` `

---

# 20. Final Submission Checklist

Before submission, confirm that:

- [x] Team details are complete
- [x] Project description is complete
- [x] Inspiration sources are included
- [x] Player journey is written
- [x] Sketches are added
- [x] BOM is complete
- [x] Purchase list is complete
- [x] Budget summary is complete
- [x] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [x] Code flowchart is added
- [x] Task breakdown is complete
- [x] Weekly logs are updated
- [x] Risk register is complete
- [x] Testing log is updated
- [x] Playtesting notes are included
- [x] Build photos are included
- [x] Final reflection is written
<img width="1131" height="1600" alt="image" src="https://github.com/user-attachments/assets/3ae2ba11-1365-435a-9e14-f691484a4012" />

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval

- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review

`[Instructor fills this section]`

## 22.3 Final Review Notes

`[Instructor fills this section]`
