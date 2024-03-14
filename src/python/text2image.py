from PIL import Image, ImageDraw, ImageFont
import textwrap

def split_text(text, min_chars=100, max_chars=300):
    words = text.split()
    chunks = []
    current_chunk = words[0]

    for word in words[1:]:
        if len(current_chunk) + len(word) + 1 <= max_chars:
            current_chunk += ' ' + word
        else:
            chunks.append(current_chunk)
            current_chunk = word
    chunks.append(current_chunk)
    return chunks

def create_images_from_text(chunks, font_path="/System/Library/Fonts/Helvetica.ttc", font_size=20, line_width=75):
    images = []
    for i, chunk in enumerate(chunks):
        # Wrap text
        wrapped_text = textwrap.fill(chunk, width=line_width)
        img = Image.new('RGB', (800, 600), color=(255, 255, 255))  # Adjust the image size if needed
        d = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            print(f"Could not open font file: {font_path}. Make sure the path is correct.")
            return
        d.text((10,10), wrapped_text, fill=(0,0,0), font=font)
        images.append(img)
        img.save(f"text_image_{i}.png")
    return images

# Read text from the file
with open('/Users/farshid/farshid/pirahansiah.github.io/site/pages/CC.md', 'r') as file:
    text = file.read()

chunks = split_text(text)
create_images_from_text(chunks)

# Output the paths of the created images
for i in range(len(chunks)):
    print(f"/mnt/data/text_image_{i}.png")


# from PIL import Image, ImageDraw, ImageFont
# import textwrap

# def split_text(text, min_chars=100, max_chars=300):
#     words = text.split()
#     chunks = []
#     current_chunk = words[0]

#     for word in words[1:]:
#         if len(current_chunk) + len(word) + 1 <= max_chars:
#             current_chunk += ' ' + word
#         else:
#             chunks.append(current_chunk)
#             current_chunk = word
#     chunks.append(current_chunk)
#     return chunks

# def create_images_from_text(chunks, font_path="/System/Library/Fonts/Helvetica.ttc", font_size=20):
#     images = []
#     for i, chunk in enumerate(chunks):
#         img = Image.new('RGB', (800, 100), color=(255, 255, 255))
#         d = ImageDraw.Draw(img)
#         try:
#             font = ImageFont.truetype(font_path, font_size)
#         except IOError:
#             print(f"Could not open font file: {font_path}. Make sure the path is correct.")
#             return
#         d.text((10,10), chunk, fill=(0,0,0), font=font)
#         images.append(img)
#         img.save(f"text_image_{i}.png")
#     return images

# # Read text from the file
# with open('/Users/farshid/farshid/pirahansiah.github.io/site/pages/CC.md', 'r') as file:
#     text = file.read()

# chunks = split_text(text)
# create_images_from_text(chunks)

# # Output the paths of the created images
# for i in range(len(chunks)):
#     print(f"/mnt/data/text_image_{i}.png")
