# Micro GSM Network

## Description

This project aims to use the *LimeNET Micro* Software Defined Radio to set up a public GSM network using Yate and YateBTS. The rationale for this project was to study and experiment mobile communications and the GSM protocol with a low-end device.
It creates simple and basic GSM network for SMS and voice calls running on a LimeNET Micro with a Raspberry Pi CM3 board flashed with Ubuntu 20.04 LTS.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Installation

### Hardware Requirements
- LimeNET Micro SDR
- Antennas for 900MHz (EMEA GSM-900 band)
- Raspberry Pi compute module 3

### Software Requirements
- Yate
- YateBTS
- LimeUtil

### Steps

1. **Clone the Repository**:  
    ```
    git clone https://github.com/OxMarco/Micro-GSM-Network.git
    ```
   
2. **Install Dependencies**:  
    ```
    sudo apt-get update
    sudo apt-get install yate yatebts
    ```
   
3. **Run Setup Script**:  
    ```
    ./setup.sh
    ```

## Usage

1. **Init the Lime toolkit software**:  
    ```
    LimeUtil --update
    ```

2. **Run scripts**:
	Run the *.sh* scripts one by one to initialise the GSM stack.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
