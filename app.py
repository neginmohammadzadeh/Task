from flask import Flask, render_template, Response, request, jsonify

app = Flask(__name__)
app.config['title'] = 'Fan App'

# These initial values are supposed to be set by admin 
fan_init = {
    'speed': 2,
    'direction': 'reverse'
}


@app.route('/')
def index(): 
    return render_template('index.html', title=app.config['title']) 

# Get initial values
@app.route('/api/fan/init')
def init():
    return jsonify(fan_init)

# Increase the speed of the fan
@app.route('/api/fan/speedup')
def speed_up():
    # get the current speed
    _speed = request.headers.get('speed')
    if _speed == None:
        return Response(status='400')
    if _speed not in ['0','1','2','3']:
        return jsonify({'speed' :'0'} )
    # to make sure the speed is between 0 and 3
    _speed = (int(_speed)+ 1) % 4    
    return jsonify({'speed' : str(_speed)})

# Change the direction of the fan
@app.route('/api/fan/reverse')
def reverse():
    _dir= request.headers.get('dir')
    if _dir == None:
        return Response(status='400')
    if _dir == 'normal':
        _dir ='reverse'
    else:
        _dir = 'normal'
    return jsonify({'direction' : _dir}) 

# Check Server Error- Just for test cases
@app.route('/api/fan/checkservererror')
def check_server_error():
   temp =  10/0

# Handle Not Found Error
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message ': 'Not Found'}), 404

# Handle Server Error
@app.errorhandler(Exception)
def server_error(e):
    return jsonify({'message ':'Server Error'}), 500
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000 )

