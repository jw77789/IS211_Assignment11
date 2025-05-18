from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

# Global list to hold To Do items
todo_items = []

@app.route('/')
def index():
    return render_template('index.html', items=todo_items)

@app.route('/submit', methods=['POST'])
def submit():
    task = request.form.get('task')
    email = request.form.get('email')
    priority = request.form.get('priority')

    # Basic validation
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return redirect('/')
    if priority not in ['Low', 'Medium', 'High']:
        return redirect('/')

    # Add valid item
    todo_items.append({'task': task, 'email': email, 'priority': priority})
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    todo_items.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
