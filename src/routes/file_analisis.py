from flask import Flask, jsonify, request, Blueprint, render_template
#from openai import OpenAI
import google.generativeai as gemini
import environs
#import os

blueprint_usuario = Blueprint('blueprintUsuario',__name__)
env = environs.Env()
env.read_env()

#client = OpenAI(api_key=env.list("OPENAI_API_KEY")[0])
gemini.configure(api_key=env.list("GOOGLE_API_KEY")[0])

client = gemini.GenerativeModel('gemini-pro')
#client = OpenAI()
@blueprint_usuario.route('/',methods=["GET"])
def home():
    return render_template('file_analisis/home.html')

@blueprint_usuario.route('/file',methods=["POST"])
def read():
    if request.method == 'POST':   
        file = request.files['file'] 
        fileContent=file.read().decode("utf-8")
        prompts = [
            fileContent + "   how many logs are there",
            fileContent + "   Give me a summary of the logs",
            fileContent + "   give me the security risks"
        ]

        # Remove "text: " from prompts before sending to client (server-side filtering)

        cantidad = client.generate_content(prompts[0])
        summary = client.generate_content(prompts[1])
        risks = client.generate_content(prompts[2])

        # Access and potentially process generated content (assuming parts[0] is relevant)
        cantidad_content = cantidad.candidates[0].content.parts[0].text
        summary_content = summary.candidates[0].content.parts[0].text
        risks_content = risks.candidates[0].content.parts[0].text
        return render_template("file_analisis/result.html", name = file.filename, 
                            amount = cantidad_content 
                            ,summary= summary_content
                            ,risks = risks_content
                            )   
    
