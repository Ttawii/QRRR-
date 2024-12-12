# QRRR! Code Decryption Tool - CTF Walkthrough for Flagyard

### The files I uploaded are a showcase of my attempts to solve the CTF.

This repository provides a **CTF walkthrough** for solving a challenge from the **Flagyard** platform. The challenge involves extracting QR codes hidden within frames of a video, decoding them, and decrypting the encrypted messages using ROT13. The tool is developed in Python and helps to automate the extraction, decoding, and decryption process.

## System Requirements

- Python 3.6 or higher
- `opencv-python` library for extracting images from video
- `pyzbar` library for decoding QR codes from images
- `codecs` library for decoding ROT13 encrypted text

## Challenge Overview

This walkthrough is based on the **QRRR!** challenge from the Flagyard CTF platform. In this challenge:
- A video contains multiple frames with QR codes embedded within them.
- These QR codes contain encoded messages that need to be decrypted.
- The encrypted text within the QR codes is encrypted using the **ROT13** cipher.

## How to Use

### 1. Extracting Frames from a Video

The first step is to extract individual frames from the provided video. This can be done using the `opencv-python` library. Use the following script to extract all the frames and save them as PNG images:

```python
import cv2
import os

# Path to the video
video_path = "path_to_video.mp4"
output_folder = "extracted_frames"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Load the video
cap = cv2.VideoCapture(video_path)
frame_number = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Save each frame as a PNG image
    cv2.imwrite(os.path.join(output_folder, f"frame_{frame_number}.png"), frame)
    frame_number += 1

cap.release()
print("Frames extracted successfully.")
```
### 2. Extracting QR Codes from Images
Once the frames are extracted, you can decode the QR codes present in the images using the **pyzbar** library. The following script will read the images, detect QR codes, and extract the data:

```python
from pyzbar.pyzbar import decode
from PIL import Image
import os

image_folder = "extracted_frames"
decoded_codes = {}

for image_file in os.listdir(image_folder):
    if image_file.endswith(".png"):
        image_path = os.path.join(image_folder, image_file)
        image = Image.open(image_path)
        
        # Decode QR codes from the image
        decoded_objects = decode(image)
        for obj in decoded_objects:
            decoded_codes[image_file] = obj.data.decode("utf-8")

# Print the decoded QR codes
for frame, code in decoded_codes.items():
    print(f"Code in {frame}: {code}")
```
### 3. Decrypting Encoded Texts
Some QR codes may contain messages encrypted with ROT13. To decrypt these messages, you can use the following script:
```python
import codecs

def decode_rot13(text):
    return codecs.decode(text, 'rot_13')

# Example encoded texts from QR codes
encoded_texts = [
    "SyntL{q6pnbcxfqcbnfxqEEE!}",
    "SyntL{qbnfxqcbnfxqnfxqcbnf_nbfqwfnvwqbnvfwqbv_nfffnff!}",
    "SyntL{nbfcxqcbfnxq_fvbqswfqsfbqs_fbbbbrrrrr___rvswbnvfw!}",
    "SyntL{qstqtsqtvewre_qvfqcs_qsqs!}",
    "SyntL{fxwqxwf_qfbq_qfswfqsf!}",
    "SyntL{vvfqsfq_xqfwxfq_qwfqf!}",
    "SyntL{ncfqx7c6jbxf_qbfws6_qbvfwqbvswf!}",
    "SyntL{wuxqysfqyn_fqcbfqcqf_5678765qqqq!}",
    "SyntL{Pbatengf_h_tbg_vggg}",
    "SyntL{ncfxbqcnxfq_vqfnwqs56!}",
    "SyntL{qfstugtstsqfr_ss!}",
    "SyntL{abg_gur_synt_jnyynu!}",
    "SyntL{fnyqnbfxqfncbxqnnbfcxq!}",
    "SyntL{kxqsxbfcxsfb_fqfqfqfqfqqfqf!}",
    "SyntL{abg_gur_synnnnnnnnnnnnttttt!}",
    "SyntL{qbnfcbxqfn7!}",
    "SyntL{bqfc2tq!}",
    "SyntL{bqfc2tqfqsfq!}"
]

# Decrypt all the encoded texts
decoded_texts = [decode_rot13(text) for text in encoded_texts]

# Print the decrypted texts
for text in decoded_texts:
    print(text)
```
### 4. Results
After running the scripts, you will get the decoded QR codes from the images, followed by the decrypted messages. These messages may eventually reveal the flag or key information needed to solve the challenge.

## Conclusion

This project serves as a walkthrough for solving the **QRRR!** CTF challenge on the **Flagyard** platform. By automating the process of extracting QR codes from video frames, decoding them, and decrypting the encrypted messages using ROT13, I was able to gain valuable insights into various tools and techniques commonly used in Capture the Flag (CTF) challenges. 

The project demonstrates the practical application of computer vision, QR code decoding, and cryptographic techniques, all essential skills for tackling cybersecurity challenges. The scripts and tools provided here can be adapted for similar CTF problems or real-world applications involving QR code extraction and encryption.

I hope this project serves as a useful resource for others tackling similar challenges, and I encourage you to explore and modify the code for further learning and experimentation. 

Feel free to reach out with any questions or suggestions!


### Contact me: 

<a href="https://www.instagram.com/t2tt/" style="color: white; text-decoration: none;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Instagram_logo_2022.svg" alt="Instagram" width="30" />
</a>





