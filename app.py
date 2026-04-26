from flask import Flask, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    task_html = ""

    for i, task in enumerate(tasks):
        status = "✔️" if task["done"] else ""
        style = "text-decoration: line-through; color: gray;" if task["done"] else ""

        task_html += f"""
        <div style="background:#f1f1f1;padding:10px;margin:10px 0;border-radius:8px;display:flex;justify-content:space-between;align-items:center;">
            <span style="{style}">{task["name"]} {status}</span>
            <div>
                <a href="/complete/{i}">
                    <button style="background:#4CAF50;color:white;border:none;padding:5px 10px;border-radius:5px;">Complete</button>
                </a>
                <a href="/delete/{i}">
                    <button style="background:#f44336;color:white;border:none;padding:5px 10px;border-radius:5px;">Delete</button>
                </a>
            </div>
        </div>
        """

    return f"""
    <html>
    <head>
        <title>Todo App</title>
    </head>
    <body style="font-family:Arial;background:#eee;display:flex;justify-content:center;align-items:center;height:100vh;">

        <div style="background:white;padding:30px;border-radius:10px;width:400px;box-shadow:0 0 10px rgba(0,0,0,0.1);">

            <h2 style="text-align:center;">📝 To-Do App</h2>

            <form method="POST" action="/add" style="display:flex;gap:10px;">
                <input name="task" placeholder="Enter task" required
                    style="flex:1;padding:8px;border:1px solid #ccc;border-radius:5px;">
                <button type="submit"
                    style="background:#28a745;color:white;border:none;padding:8px 15px;border-radius:5px;">
                    Add
                </button>
            </form>

            <div style="margin-top:20px;">
                {task_html}
            </div>

        </div>

    </body>
    </html>
    """

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    tasks.append({"name": task, "done": False})
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    tasks.pop(index)
    return redirect('/')

@app.route('/complete/<int:index>')
def complete(index):
    tasks[index]["done"] = True
    return redirect('/')


app.run(host='0.0.0.0', port=5000)