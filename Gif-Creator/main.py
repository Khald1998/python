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
