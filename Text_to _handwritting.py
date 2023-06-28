import pywhatkit as pw

txt="Python is an interpriter language that has very large applictions."

pw.text_to_handwriting(txt,"demo1.png",[0,0,138])
print("End")