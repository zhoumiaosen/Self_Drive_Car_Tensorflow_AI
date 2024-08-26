## Overview

This project focuses on developing a fully functional end to end AI-driven autonomous robot car, based and build up on the repositorie: [Self_Drive_Car_Line_Tracking](https://github.com/zhoumiaosen/Self_Drive_Car_Line_Tracking). The project requires control boards with a Raspberry Pi 4 B and an Adeept Motor Hat V2, and it uses an Adeept 2-wheel robot car. The project involves using the Pi camera to collect data, which is then used to train the AI model. The trained model will enable the robot car to react appropriately to its real-world environment.

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
├── models/
│   └── car_drive.h5
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
- tensorflow
- keras
- numpy
- RPi.GPIO

You can install the necessary packages using the following command:

```bash
pip install opencv-python tensorflow keras numpy
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
End to end AI self driving:

https://github.com/user-attachments/assets/3a7739e7-db5b-4ca6-a7ff-d4323a111132

## Next Steps
- **Coding Change :**
Given the challenges of installing OpenCV and TensorFlow, the project will be re-coded using Picamera2, PIL, and PyTorch for more streamlined development.
- **Reinforcement Learning :**
Experiment with reinforcement learning to further advance the project into a more complex AI-driven system.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request to contribute to the project.

## License
This project is licensed under the MIT License.
