# Example 2
from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/home', methods=['GET'])
def home_get():
    """
    This endpoint provides a name based on input
    ---
    parameters:
      - name: name
        in: query
        type: string
        required: false
        default: EugeneH
    responses:
      200:
        description: Returns message that says "Hello name"
    """
    name = request.args.get('name', 'Eugene')
    return jsonify({'message': f'Hello {name}!'})

if __name__ == '__main__':
    app.run(debug=True) 

# https://7071-cs-340668953872-default.cs-us-east1-vpcf.cloudshell.dev/api/home? 

# use app_flasgger for assigment
