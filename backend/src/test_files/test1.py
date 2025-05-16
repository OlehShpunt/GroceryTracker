from PIL import Image
import pytesseract

# Load image
receipt1_1 = Image.open('/Users/olehshpunt/Documents/GitHub/GroceryTracker/backend/assets/receipt_images/receipt1_1.jpg')
receipt1 = Image.open('/Users/olehshpunt/Documents/GitHub/GroceryTracker/backend/assets/receipt_images/receipt1.png')
receipt2 = Image.open('/Users/olehshpunt/Documents/GitHub/GroceryTracker/backend/assets/receipt_images/receipt2.jpg')
receipt3 = Image.open('/Users/olehshpunt/Documents/GitHub/GroceryTracker/backend/assets/receipt_images/receipt3.jpg')
receipt4 = Image.open('/Users/olehshpunt/Documents/GitHub/GroceryTracker/backend/assets/receipt_images/receipt4.jpg')
receipt5 = Image.open('/Users/olehshpunt/Documents/GitHub/GroceryTracker/backend/assets/receipt_images/receipt5.jpg')


image = receipt5

if image is None:
    print("Error: Could not load image.")
    exit()

# OCR
custom_config = "--oem 1 --psm "
text = pytesseract.image_to_string(image, lang='eng', config=custom_config)

# Print output
print("OCR Output:\n")
print(text)