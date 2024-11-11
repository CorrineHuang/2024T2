#pip install flask
from flask import Flask
from flask import render_template,request

app=Flask("_name_")#bring this application to headphone


#这一行代码表示，当访问根路径 '/' 时，Flask 会接受 GET 和 POST 两种请求方式。
@app.route('/',methods=['GET','POST'])

#当用户访问根路径时，Flask 会渲染 index.html 页面并返回给浏览器，展示该网页内容。
def index():
    return(render_template("index.html"))

# __name__ is reserved for system use. 
if __name__=='__main__':
    app.run()
