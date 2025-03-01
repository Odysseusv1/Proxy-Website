from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

# Route to render the HTML page
@app.route('/')
def index():
    return render_template_string(open("index.html").read())

# Proxy route to fetch and serve the target page
@app.route('/proxy', methods=['GET'])
def proxy():
    url = request.args.get('url')  # Get the URL from the query parameter
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        # Fetch the content of the target URL
        response = requests.get(url)
        
        # Return the content from the target URL
        return response.text  # Return the HTML content as is
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
