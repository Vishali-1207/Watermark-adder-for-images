from PIL import Image, ImageDraw, ImageFont

def add_watermark(image_path, watermark_text, output_path='watermarked-image.png'):
    
    image = Image.open(image_path).convert('RGBA')
    
    watermark = Image.new('RGBA', image.size, (0, 0, 0, 0))
    
    draw = ImageDraw.Draw(watermark)

    font = ImageFont.truetype('arial.ttf', 36)

    text_bbox = font.getbbox(watermark_text)
    
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    
    width, height = image.size
    
    x = (width - text_width) / 2
    
    y = height - text_height - 10

    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

    watermarked_image = Image.alpha_composite(image, watermark)
    
    watermarked_image.save(output_path, 'PNG')
    
image_path = input("Enter the image path: ")

watermark_text = input("Enter the watermark text: ")

add_watermark(image_path, watermark_text)

