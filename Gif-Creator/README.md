# Gif-Creator

Gif-Creator is a simple Python project that converts video files into GIFs using the `moviepy` library.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with Gif-Creator, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Gif-Creator.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Gif-Creator
    ```
3. Install the required dependencies:
    ```sh
    pip install moviepy
    ```

## Usage

To convert a video file to a GIF, follow these steps:

1. Replace the  variable in  with the path to your video file.
2. Replace the  variable in  with the desired path for the output GIF.
3. Run the script:
    ```sh
    python main.py
    ```

Example:
```py
from moviepy.editor import *

# Replace the path with the path of your video file
video_path = "Milky_Way.mp4"

# Load the video
video = VideoFileClip(video_path)

# Replace the output_path with the path where you want to save the GIF
output_path = "output.gif"

# Convert the video to GIF
video.write_gif(output_path)

# Close the video file
video.close()

```
## License
This project is licensed under the MIT License. See the LICENSE file for more information.

