from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

answer_dict={
                "1": ["Gran", "Gorilla", "Negro", "Madagascar", "Agradable", "Tigres", "Blancos", "Moverme"],
                "2": ["Domingo", "Tía", "Perro", "Hamburguesas", "Refrescos", "Agradable", "Cartas"],
                "3": ["Gato", "Apestoso", "California", "Gato", "Azul", "3", "Peces", "Bailar", "Canciones", "Triste", "Infantil", "Feliz"]
            }




#¡Añade aquí los datos de las historias!
stories = [
    {
        "story_id": "1",
        "inputs": 8,
        "title": "¡Hoy fuimos al zoológico!",
        "story": '¡Hoy fuimos al zoológico! Lo primero que vimos fue un <span class="rep_input">_____</span> <span class="rep_input">_____</span> <span class="rep_input">_____</span>. El encargado nos dijo que eso era normal, excepto en <span class="rep_input">_____</span>. ¡Fue una <span class="rep_input">_____</span> aventura! A la próxima, recordaré que, si alguna vez veo <span class="rep_input">_____</span> <span class="rep_input">_____</span>, debo <span class="rep_input">_____</span> hacia el otro lado.',
        "words": ["Gran", "Gorilla", "Negro", "Madagascar", "Agradable", "Tigres", "Blancos", "Moverme"]
    },
    {
        "story_id": "2",
        "inputs": 7,
        "title": "Día de Picnic",
        "story": 'El <span class="rep_input">_____</span> nos vamos de picnic. Iré con mi <span class="rep_input">_____</span> y mi <span class="rep_input">_____</span> favorito. Para comer, comeremos <span class="rep_input">_____</span> y beberemos <span class="rep_input">_____</span>. Terminaremos el día con un <span class="rep_input">_____</span> juego de <span class="rep_input">_____</span>.',
        "words": ["Domingo", "Tía", "Perro", "Hamburguesas", "Refrescos", "Agradable", "Cartas"]
    },
    {
        "story_id": "3",
        "inputs": 12,
        "title": "Cuento de un animal simplón",
        "story": 'Había una vez un <span class="rep_input">_____</span> <span class="rep_input">_____</span> de <span class="rep_input">_____</span>. Nadie sabía que era un <span class="rep_input">_____</span> porque tenía el pelaje <span class="rep_input">_____</span> y comía <span class="rep_input">_____</span> <span class="rep_input">_____</span> cada día. Le gustaba <span class="rep_input">_____</span> y cantar <span class="rep_input">_____</span>. Cuando estaba <span class="rep_input">_____</span>, empezaba a hablar de forma <span class="rep_input">_____</span>. Entonces se sentía <span class="rep_input">_____</span>.',
        "words": ["Gato", "Apestoso", "California", "Gato", "Azul", "3", "Peces", "Bailar", "Canciones", "Triste", "Infantil", "Feliz"]
    }
]




@app.route("/")
def index():
    return render_template("index.html")
    

#Añade aquí la API "/get-story".
@app.route("/get-story")
def get_story():
    return jsonify({
        "status":"success",
        "story":random.choice(stories)
    })

    


@app.route("/post-answers", methods=["POST"])
def post_answers():
    story_id = request.json.get("story_id")
    values = request.json.get("values")
    answers = answer_dict.get(story_id)
    index, score = 0, 0
    while index < len(values):
        if values[index].lower() == answers[index].lower():
            score += 1
        index += 1
    return jsonify({
        "status": "success",
        "result": f"{score} / {len(values)}"
    })

if __name__ == "__main__":
    app.run(debug=True)
