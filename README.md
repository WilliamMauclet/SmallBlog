# SmallBlog
Project to create a small blog with Flask. A previous attempt can be found at https://github.com/WilliamMauclet/CV-Flask.

I would like my blog's looks to be inspired by the following two: 
* https://nicolas.perriault.net/
* https://pythonhosted.org/Flask-Mail/

## TECHNOLOGIES
* FLask
* SQLAlchemy (http://flask-sqlalchemy.pocoo.org/)
* SQLite
* Flask-Admin
* No CSS libraries 
* Responsive design: https://www.w3schools.com/Css/css_rwd_viewport.asp (Viewport trick)
* VSCode shortcuts: https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf
* Flask-WTF?
* Flask-Markdown?

## BTW
* Windows: set terminal to git bash terminal with setting: "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe"
* To make pipenv work best in VSCode, change the python.pythonPath in the user settings to the path returned by "which python" from the pipenv shell. Restart to select the Python environment.
* To debug: it's the open file that will be debugged. To get input to work, add the field <<"console": "integratedTerminal">> to the launch.json of python under <<"name":"python">>.
* JetBrains IDEs: set terminal to "C:\Program Files\Git\bin\sh.exe" --login -i 
* About hashing passwords: https://www.reddit.com/r/flask/comments/32iuyl/hashing_passwords_not_matching/cqc4ikp/

## TODO
* Responsive design
    * @media min-width max-width => redefine 960!
    * \<meta name="viewport" content="width=device-width, initial-scale=1.0">
* Admin pages
    * https://github.com/flask-admin/flask-admin/tree/master/examples/auth-flask-login
    * Some text in admin home
    * Login/authentication
    * Allow images: https://flask-admin.readthedocs.io/en/latest/advanced/
* Posts and About in markdown?
* "Contact" page consists of key-value pairs
* Posts can contain images
* https://www.quora.com/How-do-I-divide-a-flask-app-into-multiple-files