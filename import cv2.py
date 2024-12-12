import cv2
import os

# تحميل الفيديو
video_path = video_path = video_path = "C:/Users/Ttawi/Desktop/QRRR!/ezgif-2-2f7bb47747.mp4"  # استبدل بالمسار الصحيح للفيديو
video_capture = cv2.VideoCapture(video_path)

# التأكد من أن الفيديو تم تحميله بنجاح
if not video_capture.isOpened():
    print("Error: Could not open video file.")
    exit()

# إنشاء مجلد لحفظ الإطارات
output_folder = "extracted_frames"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# استخراج الإطارات
frame_count = 0
while True:
    ret, frame = video_capture.read()
    if not ret:
        break  # انتهى الفيديو

    # حفظ الإطار كصورة PNG
    frame_filename = os.path.join(output_folder, f"frame_{frame_count}.png")
    cv2.imwrite(frame_filename, frame)
    frame_count += 1

# إغلاق الفيديو
video_capture.release()
print(f"تم استخراج {frame_count} إطارًا وحفظها في المجلد '{output_folder}'")
