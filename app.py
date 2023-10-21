from flask import Flask
from flask import render_template,request
import json
import time
import requests
import os

app = Flask(__name__)
print("Testing")
REPLICATE_API_KEY = os.getenv('REPLICATE_API_KEY')
print('REPLICATE_API_KEY:', REPLICATE_API_KEY)
headers = {
#    "Authorization": f"Token {REPLICATE_API_KEY}",
    "Authorization": "Token REPLICATE_API_KEY",
    "Content-Type" : "application/json"
}
print("Testing2")
print(REPLICATE_API_KEY)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("question")
        print(q)
        body = json.dumps(
            {
                "version" : "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
                "input"   :
                {
                    "prompt" : q
                }
            }
        )
        output = requests.post("https://api.replicate.com/v1/predictions",data=body,headers=headers)
        time.sleep(10)
        print(output.status_code)
        # Print the content of the response
        print("Testing Before output.content")
        print(output.content)
        print("Testing after output.content")
        get_url = output.json()["urls"]["get"]
        print(output.json())
        print(get_url)
        get_result = requests.post(get_url,headers=headers).json()['output']
        print(get_result)
        return(render_template("index.html",result=get_result[0]))
    else:
        return(render_template("index.html",result="waiting........"))

if __name__ == "__main__":
    app.run(debug=True)
