Raspberry Pi 4 Hardware Diagnostic Shield
Overview
This is a custom-designed PCB shield for the Raspberry Pi 4, designed as part of my Robotics and Hardware engineering studies. It provides four independent LED channels for real-time hardware status monitoring and software debugging.

Technical Specifications
Interface: 40-pin GPIO Header

Channels: 4x Independent LED indicators

Protection: 330Ω current-limiting resistors (calculated for 3.3V logic)

Software: Designed in KiCad 8.0

Validation: 100% Pass on Electrical Rules Check (ERC)

Design Logic
Each LED is mapped to a specific GPIO pin (GPIO17, 27, 22, 23) allowing for multi-threaded status updates. The board uses a common Ground plane to ensure signal stability.

<img width="1840" height="880" alt="image" src="https://github.com/user-attachments/assets/4492a2a4-5c5d-436e-bc5c-38cf4a59d7e6" />

<img width="1337" height="754" alt="test" src="https://github.com/user-attachments/assets/60bd2113-ca40-4452-ad5e-f724d26bbbe6" />
