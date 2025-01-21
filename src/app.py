# Extract data from images
import pytesseract as pyt
from PIL import Image

# If tesseract exe not on PATH :
pyt.pytesseract.tesseract_cmd = "src/tesseract/tesseract.exe"

def get_nums_from_img(path:str):
    img_str = pyt.image_to_string(Image.open(path))
    img_arr = img_str.replace("\n\n", " ").replace("\n", " ").split(" ")
    img_vals = []

    for i in img_arr:
        try: num_val = float(f"0{i}") if i.startswith(".") else float(i)
        except Exception: pass
        else: img_vals.append(num_val)

    return img_arr, img_vals

if __name__ == "__main__":
    extract, nums = get_nums_from_img("data/drawing.png")
    
    print(f"Text array : {extract}")
    print(f"Value array : {nums}")
    