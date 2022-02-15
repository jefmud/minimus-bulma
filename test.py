from minimus import Minimus, redirect, render_template, parse_formvars


app = Minimus(__name__)

@app.route('/')
def index(env):
    return redirect('/example1')

@app.route('/example1')
def example1(env):
    fields = { 'title':'Resource Form', 'username': "user1", 'password': "pass1" }
    return render_template('utility/example1.html', fields=fields)

@app.route('/example2')
def example2(env):
    fields = {'title':'Rich Text Editor', 'content': '<h1>Hello World</h1><p>This is a test</p>'}
    return render_template('utility/example2.html', fields=fields)

@app.route('/example3')
def example3(env):
    fields = {'title':'Example, TinyMCE editor', 'content': '<h1>Hello World</h1><p>This is a test</p>'}
    return render_template('utility/example3.html', fields=fields)

@app.route('/example4')
def example4(env):
    fields = {'title':'Example, Select Field'}
    selections = [('Option 1', 'option1'), ('Option 2', 'option2'), ('Option 3', 'option3')]
    return render_template('utility/example4.html', fields=fields, selections=selections)

@app.route('/example5')
def example5(env):
    fields = {'title': 'Example, Radio Field'}
    radiobtns = [('Yes', 1), ('No', 0), ('Maybe', 0), ('Maybe not', 0)]
    return render_template('utility/example5.html', fields=fields, radiobtns=radiobtns)
    
@app.route('/example6')
def example6(env):
    fields = {'title':'Example, Modals'}
    return render_template('utility/example6.html', fields=fields)

@app.route('/example7', methods=['GET', 'POST'])
def example7(env):
    fields = parse_formvars(env)
    fields['title'] = 'Example, Summernote (Bootstrap only, sorry)'
    return render_template('utility/example7.html', fields=fields)

app.run(server='gevent')