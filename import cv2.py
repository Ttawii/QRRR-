import cv2
import os


video_path = video_path = video_path = "C:/Users/Ttawi/Desktop/QRRR!/ezgif-2-2f7bb47747.mp4"  
video_capture = cv2.VideoCapture(video_path)


if not video_capture.isOpened():
    print("Error: Could not open video file.")
    exit()


output_folder = "extracted_frames"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


frame_count = 0
while True:
    ret, frame = video_capture.read()
    if not ret:
        break  

    
    frame_filename = os.path.join(output_folder, f"frame_{frame_count}.png")
    cv2.imwrite(frame_filename, frame)
    frame_count += 1


video_capture.release()
print(f"تم استخراج {frame_count} إطارًا وحفظها في المجلد '{output_folder}'")
