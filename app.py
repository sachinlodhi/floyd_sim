from flask import Flask, jsonify, request, render_template
import extract
app = Flask(__name__)


'''For testing on the front-end part'''

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_address_play', methods=['POST'])
def process_text():
    print("Called")
    place = request.form['place']
    nodes = int(request.form['nodes'])

    # You can now use text1 and text2 in your processing logic



    print(place, nodes)
    json_data = extract.get_data(place_name=place, node_nums = nodes)

    return jsonify({'result': json_data})

    return f'Place : {place}, Nodes: {nodes}'



'''For API call'''
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


@app.route('/process_address', methods=['GET'])
def process_address():
    # Get the 'address' parameter from the query string
    address = request.args.get('address')
    print("indside the fucntion")

    # Process the address (you can replace this with your logic)
    result = f"Processing address: {address}"

    json_data = extract.get_data(place_name=address)

    return jsonify({'result': json_data})


if __name__ == '__main__':
    app.run()