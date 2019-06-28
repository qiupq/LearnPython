from FormEditor import FormEditor
from feedback import FeedbackData, FormData 
from Tkinter import mainloop
FormEditor("Feedback Editor", FeedbackData, feedback.DIRECTORY)
mainloop()
