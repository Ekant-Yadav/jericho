from string import ascii_letters
import textwrap
from PIL import ImageFont, ImageDraw, Image 

def get_font_size(textarea, text, font_name, pixel_gap = 7):
    text_width = int(textarea[0])
    text_height = int(textarea[1])
    
    for point_size in range(5, 90):
        wrapped_text = []
        font = ImageFont.truetype("automata/MODERNE SANS.ttf", point_size)
                
        avg_char_width = sum(font.getbbox(char)[2] for char in ascii_letters) / len(ascii_letters)
        max_char_height = max(font.getbbox(char)[3] - font.getbbox(char)[1] for char in ascii_letters)
        
        # Translate this average length into a character count
        max_char_count = int( (text_width) / avg_char_width)
        text = textwrap.fill(text=text, width=max_char_count)
        num_line = len(text.splitlines())
        
        wrapped_text.append(text)
        
        if (max_char_height * num_line) + (pixel_gap * (num_line + 1)) >= text_height:
            
            point_size = point_size - 1
            text = wrapped_text[-1]
            
            # print("\n --> SIZE: ", point_size)
            break
        
    return text.split('\n'), point_size