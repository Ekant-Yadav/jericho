from PIL import ImageFont, ImageDraw, Image 
import cv2
import numpy as np
from string import ascii_letters
import textwrap
from utils.font_size import get_font_size



def generate_video(index, row):
    cap = cv2.VideoCapture('templates/template.mp4')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output = cv2.VideoWriter( "result/output" + str(index)+"na.mp4", fourcc, 30, (1080, 1920))

    f=0

    question = row["Question"]
    question_font_path = "templates/Roboto-Bold.ttf"
    ques_params = get_font_size((800,235),question,question_font_path )
    ques  = {
        "text" : ques_params[0],
        "text_size" : ques_params[1],
        "start_height" : 390,
        "padding" : 7,
        "font" : ImageFont.truetype(question_font_path, ques_params[1]),
        "duration": range(60,385),
        "line_width": [ImageDraw.Draw(Image.new(mode="RGB", size=(1080, 1920))).textlength(i, font = ImageFont.truetype(question_font_path, ques_params[1])) for i in ques_params[0]]
    }


    options = [row["Option 1"], row["Option 2"], row["Option 3"]]
    options_font_path = "templates/Roboto-Bold.ttf"
    option_params = [get_font_size((800,140), i, options_font_path) for i in options]
    opt_text_size = min(i[1] for i in option_params)
    opt = {
        "text" : [i[0] for i in option_params],
        "text_size" : opt_text_size,
        "start_height": 900,
        "padding": 7,
        "margin": 50,
        "font": ImageFont.truetype(options_font_path, opt_text_size),
        "duration" : range(130, 385),
        "line_width" : [[ImageDraw.Draw(Image.new(mode="RGB", size=(1080, 1920))).textlength(i, font = ImageFont.truetype(options_font_path, opt_text_size)) for i in j[0]] for j in option_params]
    }


    answer = row["Answer"]
    answer_font_path = "templates/Roboto-Bold.ttf"
    ans_params = get_font_size((900,200),answer,answer_font_path )
    ans  = {
        "text" : ans_params[0],
        "text_size" : ans_params[1],
        "start_height" : 1920/2,
        "padding" : 7,
        "font" : ImageFont.truetype(answer_font_path, ans_params[1]),
        "duration": 424,
        "line_width": [ImageDraw.Draw(Image.new(mode="RGB", size=(1080, 1920))).textlength(i, font = ImageFont.truetype(answer_font_path, ans_params[1])) for i in ans_params[0]]
    }

    font = cv2.FONT_HERSHEY_SIMPLEX
    ret, frame = cap.read()
    # get coords based on boundary

    while(True): 
        
        # Capture frames in the video 
        ret, frame = cap.read()

        if ret == True: 
            f+=1
            
            if f in ques["duration"]:
                cv2_im_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                pil_im = Image.fromarray(cv2_im_rgb)
                draw = ImageDraw.Draw(pil_im)  
                current_h = ques["start_height"]
                for i,line in enumerate(ques["text"]):
                    draw.text(((1080 - ques["line_width"][i]) / 2, current_h), line, (0,0,0), font=ques["font"])
                    current_h += ques["text_size"] + ques["padding"]
                
                if f in opt["duration"]:
                    current_opt_h = opt["start_height"]
                    for j, new_opt in enumerate(opt["text"]):
                        for i, line in enumerate(new_opt):
                            draw.text(((1080 - opt["line_width"][j][i]) / 2, current_opt_h), line, (254,254,254), font=opt["font"])
                            current_opt_h+= opt["text_size"] + opt["padding"]
                        current_opt_h += opt["margin"]
                frame = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR) 
            if f > 424:
                cv2_im_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                pil_im = Image.fromarray(cv2_im_rgb)
                draw = ImageDraw.Draw(pil_im)
                current_h = ans["start_height"]
                for i,line in enumerate(ans["text"]):
                    draw.text(((1080 - ans["line_width"][i]) / 2, current_h), line, (254,254,254), font=ans["font"])
                    current_h += ans["text_size"] + ans["padding"]
                
                # Get back the image to OpenCV  
                frame = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR) 

            #Adding to output
            output.write(frame)
        
            # creating 'q' as the quit  
            # button for the video 
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break
        
        else:
            break
    
    # release the cap object 
    cap.release() 
    output.release() 
    # close all windows 
    cv2.destroyAllWindows() 