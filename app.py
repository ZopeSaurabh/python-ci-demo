from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

board = [""] * 9
player = "X"

def winner():
    w = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]
    for a,b,c in w:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    global player
    i = request.json["i"]

    if board[i] == "":
        board[i] = player
        win = winner()
        player = "O" if player == "X" else "X"
        return jsonify({"board": board, "win": win})
    return jsonify({"error": "invalid"})

@app.route("/reset")
def reset():
    global board, player
    board = [""] * 9
    player = "X"
    return jsonify({"msg": "reset"})

if __name__ == "__main__":
    app.run(debug=True)