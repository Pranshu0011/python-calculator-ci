from flask import Flask, render_template_string, request
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Python Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 400px; margin: 0 auto; padding: 20px; }
        .calculator { border: 1px solid #ccc; padding: 20px; border-radius: 5px; }
        input, select, button { padding: 8px; margin: 5px 0; width: 100%; }
        .result { margin-top: 15px; font-weight: bold; }
        .error { color: red; }
    </style>
</head>
<body>
    <div class="calculator">
        <h2>Python Calculator</h2>
        <form method="POST">
            <input type="number" name="num1" placeholder="First number" step="any" required>
            <select name="operation">
                <option value="add">+</option>
                <option value="subtract">-</option>
                <option value="multiply">×</option>
                <option value="divide">÷</option>
            </select>
            <input type="number" name="num2" placeholder="Second number" step="any" required>
            <button type="submit">Calculate</button>
        </form>
        
        {% if result is not none %}
        <div class="result">
            Result: {{ result }}
        </div>
        {% endif %}
        
        {% if error %}
        <div class="error">
            {{ error }}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    error = None
    
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']
            
            if operation == 'add':
                result = add(num1, num2)
            elif operation == 'subtract':
                result = subtract(num1, num2)
            elif operation == 'multiply':
                result = multiply(num1, num2)
            elif operation == 'divide':
                result = divide(num1, num2)
                
        except ValueError as e:
            error = str(e)
        except Exception as e:
            error = "An error occurred during calculation"
    
    return render_template_string(HTML_TEMPLATE, result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
