## Overview

This project focuses on developing a line-following robot car using OpenCV, powered by a Raspberry Pi 4 B and controlled via an Adeept Motor Hat V2. The robot, based on the Adeept 2-wheel robot car, will autonomously follow a line by processing visual input, employing motor control, and integrating line detection and tracking. This endeavor serves as a foundational step towards creating a fully functional AI-driven autonomous robot car.

## Project Structure
```plaintext
Car_Line_Tracking/
│
├── src/
│   ├── car_AI_load_model.py              
│   ├── Motor.py    
│   ├── car_AI_Run.py  
│   ├── car_AI_train.py
│   └── car_data_capture.py  
│ 
│                         
├── models/
│   ├── car_drive_Sep_26_2023_V5.h5 
│   ├── car_drive_v3.h5
│   └── car_drive.h5
│ 
│ 
├── DIR/
│   ├── a/
│   ├── d/
│   ├── w/
│   ├── s/
│   └── READEM.md	# Project data collection instructions
│ 
└── README.md		# Project overview and instructions
```

## Requirements

- Python 3.7+
- opencv
- RPi.GPIO

You can install the necessary packages using the following command:

```bash
pip install opencv-python 
```

## How to Run

### 1. Run Line Tracking 

Run car with one cmd:

```bash
python src/car_AI_Run.py
```
### 2. Hardware	
#### Control Board
Raspberry pi 4 B:<br>
<img src="assets/Raspberry_pi_4.png" alt="Diagram" width="250">

Adeept Motor Hat V2:<br>
<img src="assets/Adeept Motor Hat V2.png" alt="Diagram" width="250">

#### Robot Car
Robot car front:<br>
<img src="assets/car_front.png" alt="Diagram" width="250">

Robot car top:<br>
<img src="assets/car_top.png" alt="Diagram" width="250">

Robot car bottom:<br>
<img src="assets/car_bottom.png" alt="Diagram" width="250">

## Results
AI self driving:



## Next Steps
- **AI Model Deploy :**
 Experiment with neural network architectures to improve car self drive performance.
- **End-to-End AI System :**
Consider exploring end-to-end learning approaches where a neural network directly controls the robot based on raw camera input.
- **Reinforcement Learning :**
Experiment with reinforcement learning to further advance your project into a more complex AI-driven system.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request to contribute to the project.

## License
This project is licensed under the MIT License.
