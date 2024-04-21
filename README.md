## HOW IT WORKS
 * The code is not dynamic at all. Works for only only one vide file in the entire world. Its not hard i am just lazy. 
 * The main.py file reads the csv file containg trivia questions and the audio template.
 * Invokes the utils/make_video to make the video with that question . 
 * The make_video uses openCV and pillow to edit the video and stores it in the resulsts folder. The make_video file is no that crazy in itself the actual math is in utils/font_size (which i wrote myself mhmmm, did not steal. Couldn't be me!). 
 * This function dynamically calculates the font size according to text length and frazme size. so that the no text overflow can be seen.
 * Now the main files takes the edited video and adds audio to it.
