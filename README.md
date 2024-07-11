# Make It Simple

Welcome to the **Make It Simple** project! This repository contains various Python scripts to simplify and automate tasks such as image and music conversion.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Guide](#guide)
<!-- - [Contributing](#contributing)
- [License](#license)
- [Contact](#contact) -->

## Project Description

**Make It Simple** aims to provide easy-to-use Python scripts for everyday automation tasks. Currently, the project includes:
- Image conversion (JPG to PNG)
- Music conversion and management

## Features

- Convert JPG images to PNG format using `ffmpeg`.
- Manage and convert music files with custom scripts.
- Simple and interactive CLI interface.

## Installation

### Prerequisites

- Python 3.x
- `ffmpeg` installed and accessible from your PATH
- Virtual environment (optional but recommended)

### Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/make-it-simple.git
    cd make-it-simple
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Image Conversion

To convert JPG images to PNG, run the following script:

```sh
python image_conversion.py
```
To convert music formats, run the following script:

```sh
python music_conversion.py
```

## Guide
<p align="center">
 <img width="1000" src="assets/image_conversion.mp4" alt="image_conversion.mp4"/>
</p>
