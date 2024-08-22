from flask import Flask, request, jsonify
from libgenapi import Libgenapi  # Replace 'your_module_name' with the actual module name where Libgenapi is defined

app = Flask(__name__)

# Initialize the Libgenapi instance with mirrors
libgenapi_instance = Libgenapi(mirrors=["http://libgen.rs"])

@app.route('/search', methods=['GET'])
def search_books():
    # Get the search term from the query parameters
    search_term = request.args.get('q')
    if not search_term:
        return jsonify({"error": "No search term provided"}), 400
    
    # Perform the search using the Libgenapi instance
    results = libgenapi_instance.libgen.search(search_term)
    
    # Return the results as JSON
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)