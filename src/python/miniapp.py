#  # Process the image
#     image = cv2.imdecode(np.frombuffer(photo_bytes, np.uint8), cv2.IMREAD_COLOR)
#     pencil_sketch_image = pencil_sketch(image)

#     # Send the processed image back to the user
#     sketch_bytes = cv2.imencode('.png', pencil_sketch_image)[1].tobytes()

import cv2
import numpy as np

def pencil_sketch(img):    #Pencil Sketch
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_gray_image = cv2. bitwise_not(gray_image)
    blurred_image = cv2. GaussianBlur (inverted_gray_image, (21, 21), 0)
    inverted_blurred_image = cv2. bitwise_not(blurred_image)
    pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
    return pencil_sketch_image
   
def circleimg(img):        
    h, w = img.shape[:2]
    size = min(h, w)
    img = cv2.resize(img, (size, size))
    mask = np.zeros((size, size), dtype="uint8")
    center = (size // 2, size // 2)
    radius = size // 2
    cv2.circle(mask, center, radius, 255, -1)
    masked_image = cv2.bitwise_and(img, img, mask=mask)
    return masked_image
  
def edge_detection(img):    
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, 100, 200)
    return edges
def squareimg(img):    
    h, w = img.shape[:2]
    size = min(h, w)
    img = cv2.resize(img, (size, size))
    mask = np.zeros((size, size), dtype="uint8")
    cv2.rectangle(mask, (0, 0), (size, size), 255, -1)
    masked_image = cv2.bitwise_and(img, img, mask=mask)
    return masked_image

def triangleimg(img):    
    h, w = img.shape[:2]
    size = min(h, w)
    img = cv2.resize(img, (size, size))
    mask = np.zeros((size, size), dtype="uint8")
    pts = np.array([[size//2, 0], [size, size], [0, size]], np.int32).reshape((-1, 1, 2))
    cv2.fillPoly(mask, [pts], 255)
    masked_image = cv2.bitwise_and(img, img, mask=mask)
    return masked_image

def ellipseimg(img):    
    h, w = img.shape[:2]
    size = min(h, w)
    img = cv2.resize(img, (size, size))
    mask = np.zeros((size, size), dtype="uint8")
    center = (size // 2, size // 2)
    axes = (size // 2, size // 3)
    cv2.ellipse(mask, center, axes, 0, 0, 360, 255, -1)
    masked_image = cv2.bitwise_and(img, img, mask=mask)
    return masked_image

def starimg(img):    
    h, w = img.shape[:2]
    size = min(h, w)
    img = cv2.resize(img, (size, size))
    mask = np.zeros((size, size), dtype="uint8")
    pts = np.array([[size//2, 0], [size*3//4, size*3//4], [0, size//4], [size, size//4], [size//4, size*3//4]], np.int32).reshape((-1, 1, 2))
    cv2.fillPoly(mask, [pts], 255)
    masked_image = cv2.bitwise_and(img, img, mask=mask)
    return masked_image
def ellipseimg2(img):    
    h, w = img.shape[:2]
    size = min(h, w)
    img = cv2.resize(img, (size, size))
    mask = np.zeros((size, size), dtype="uint8")
    center = (size // 2, size // 2)
    axes = (size // 3, size // 2)
    cv2.ellipse(mask, center, axes, 0, 0, 360, 255, -1)
    masked_image = cv2.bitwise_and(img, img, mask=mask)
    return masked_image

def starimg2(img):    
    h, w = img.shape[:2]
    size = min(h, w)
    img = cv2.resize(img, (size, size))
    mask = np.ones((size, size), dtype="uint8") * 255
    pts = np.array([[size//2, 0], [size*3//4, size*3//4], [0, size//4], [size, size//4], [size//4, size*3//4]], np.int32).reshape((-1, 1, 2))
    cv2.fillPoly(mask, [pts], 0)
    masked_image = cv2.bitwise_and(img, img, mask=mask)
    return masked_image
def circle_emoji(img):    
    h, w = img.shape[:2]
    size = min(h, w)
    img = cv2.resize(img, (size, size))
    mask = np.zeros((size, size), dtype="uint8")
    center = (size // 2, size // 2)
    radius = size // 2
    cv2.circle(mask, center, radius, 255, -1)
    emoji = cv2.bitwise_and(img, img, mask=mask)
    return emoji

def transfer_image_style_opencv(img):
    img = cv2.resize(img, (224, 224))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (21, 21), 0)
    img_edges = cv2.Canny(img_blur, 100, 200)
    img_edges_colored = cv2.cvtColor(img_edges, cv2.COLOR_GRAY2BGR)
    img_result = cv2.addWeighted(img, 0.6, img_edges_colored, 0.4, 0)
    return img_result
def cartoonify_image(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(img_gray, 5)
    img_edges = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    img_color = cv2.bilateralFilter(img, 9, 300, 300)
    cartoon_img = cv2.bitwise_and(img_color, img_color, mask=img_edges)
    return cartoon_img

def anime_style_image(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)
    img_edges = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 7)
    img_color = cv2.bilateralFilter(img, 10, 150, 150)
    img_smooth = cv2.edgePreservingFilter(img_color, flags=1, sigma_s=60, sigma_r=0.4)
    anime_img = cv2.bitwise_and(img_smooth, img_smooth, mask=img_edges)
    return anime_img
def comic_book_style_image(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(img_gray, 5)
    img_edges = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    img_color = cv2.bilateralFilter(img, 9, 250, 250)
    comic_img = cv2.bitwise_and(img_color, img_color, mask=img_edges)
    comic_img = cv2.cvtColor(comic_img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(comic_img)
    s = cv2.equalizeHist(s)
    comic_img = cv2.merge([h, s, v])
    comic_img = cv2.cvtColor(comic_img, cv2.COLOR_HSV2BGR)
    return comic_img
def remove_background(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros_like(img)
    cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)
    result = cv2.bitwise_and(img, mask)
    return result

def apply_anime_comic_style(img, text):
    # Anime style
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)
    img_edges = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 7)
    img_color = cv2.bilateralFilter(img, 10, 150, 150)
    anime_img = cv2.bitwise_and(img_color, img_color, mask=img_edges)

    # Comic style
    img_blur = cv2.medianBlur(img_gray, 5)
    img_edges = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    img_color = cv2.bilateralFilter(img, 9, 250, 250)
    comic_img = cv2.bitwise_and(img_color, img_color, mask=img_edges)
    comic_img = cv2.cvtColor(comic_img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(comic_img)
    s = cv2.equalizeHist(s)
    comic_img = cv2.merge([h, s, v])
    comic_img = cv2.cvtColor(comic_img, cv2.COLOR_HSV2BGR)

    # Mirror and Flip transformations
    mirror_img = cv2.flip(comic_img, 1)
    flip_img = cv2.flip(comic_img, 0)

    # Combine images into a comic book page layout
    top_row = np.hstack((anime_img, comic_img))
    bottom_row = np.hstack((mirror_img, flip_img))
    comic_page = np.vstack((top_row, bottom_row))

    # Add text to the comic page
    cv2.putText(comic_page, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    return comic_page


def create_comic_page(image_path, texts):
    img = cv2.imread(image_path)
    page_height, page_width = 1000, 800
    page = np.ones((page_height, page_width, 3), dtype=np.uint8) * 255
    num_panels = 6
    panel_height, panel_width = page_height // 3, page_width // 2
    transformations = [
        lambda x: x,
        lambda x: cv2.flip(x, 1),
        lambda x: cv2.resize(x, (panel_width // 2, panel_height // 2)),
        lambda x: cv2.resize(x, (panel_width * 2, panel_height * 2))[panel_height//2:panel_height//2+panel_height, panel_width//2:panel_width//2+panel_width],
        lambda x: cv2.addWeighted(x, 1.5, np.zeros(x.shape, x.dtype), 0, 0),
        lambda x: cv2.cvtColor(pencil_sketch(x), cv2.COLOR_GRAY2BGR)
    ]
    for i in range(num_panels):
        panel = cv2.resize(img, (panel_width, panel_height))
        panel = transformations[i](panel)
        panel = cv2.resize(panel, (panel_width, panel_height))
        x, y = (i % 2) * panel_width, (i // 2) * panel_height
        page[y:y+panel_height, x:x+panel_width] = panel
        if i < len(texts):
            cv2.putText(page, texts[i], (x+10, y+30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    cv2.line(page, (page_width//2, 0), (page_width//2, page_height), (0, 0, 0), 2)
    cv2.line(page, (0, page_height//3), (page_width, page_height//3), (0, 0, 0), 2)
    cv2.line(page, (0, 2*page_height//3), (page_width, 2*page_height//3), (0, 0, 0), 2)
    return page

if __name__=='__main__':
    #dst=anime_style_image(img)
    #dst=pencil_sketch(img)
    #texts = ['Original', 'Flipped', 'Shrunk', 'Zoomed', 'Brightened', 'Sketch']
    #         texts = [
    #     "Just another day...",
    #     "Mirror, mirror on the wall!",
    #     "Honey, I shrunk the kids!",
    #     "Enhance... ENHANCE!",
    #     "My future's so bright!",
    #     "Sketchy situation here!" ]
    #dst = create_comic_page(input_image_path, texts)

    input_image_path = '/Users/farshid/Desktop/farshid.jpg'
    img = cv2.imread(input_image_path)
    #dst=pencil_sketch(img)
    #dst=circleimg(img)
    #dst=edge_detection(img)    
    #dst=squareimg(img)
    #dst=triangleimg(img)
    #dst=ellipseimg(img)
    #dst=starimg(img)
    #dst=ellipseimg2(img)
    #dst=starimg2(img)
    #dst=circle_emoji(img)
    #dst=transfer_image_style_opencv(img)
    #dst=cartoonify_image(img)
    #dst=anime_style_image(img)
    #dst=comic_book_style_image(img)
    #dst=remove_background(img)
    #dst=apply_anime_comic_style(img,"farshid")
    # texts = [
    # "Just another day...",
    # "Mirror, mirror on the wall!",
    # "Honey, I shrunk the kids!",
    # "Enhance... ENHANCE!",
    # "My future's so bright!",
    # "Sketchy situation here!"]
    # dst = create_comic_page(input_image_path, texts)
    dst=pencil_sketch(img)
    #dst=circleimg(img)
    #dst=circleimg(img)
    
    
    
    
    output_image_path = '/Users/farshid/Desktop/farshid-b.png'
    cv2.imwrite(output_image_path,dst)   
    
    #circleimg(input_image_path, output_image_path)
    
    
    outputimg=cv2.imread(output_image_path)
    cv2. imshow('result', outputimg)
    cv2. waitKey(0)
    cv2.destroyAllWindows()
    #source Code --> pirahansiah.com
