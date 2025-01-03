# Import the required libraries
from PIL import Image

# Load image1
img1 = Image.open('./path/name1.png').convert("L")
# Load 2
img2 = Image.open('./path/name2.png').convert("L")

# Check that the images are the same size
if img1.size == img2.size:
    # Create a blank image to hold the pixel differences
    diff_img = Image.new('RGB', img1.size)

    # Compare the pixel differences
    for x in range(img1.size[0]): # Create a blank image to hold the pixel differences.
        for y in range(img1.size[1]): 
         if (img1.getpixel((x, y)) - img2.getpixel((x, y))) > 35: 
            # Mark different pixel points in diff_img
            diff_img.putpixel((x, y), (255, 0, 0)) # Red color indicates different pixel points
    
    output_path = './diff_imgs/error map - name.jpg'
    diff_img.save(output_path)
    print(f'Difference image saved at {output_path}')

else:
    print('Image sizes do not match')