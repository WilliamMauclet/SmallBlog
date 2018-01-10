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
* To make pipenv work best in VSCode, change the python.pythonPath in the user settings to the path returned by "which python" from the pipenv shell.
* To debug: it's the open file that will be debugged. To get input to work, add the field <<"console": "integratedTerminal">> to the launch.json of python under <<"name":"python">>.

## TODO
* Responsive design
    * @media min-width max-width => redefine 960!
    * <meta name="viewport" content="width=device-width, initial-scale=1.0">
* Admin pages
    * Some text in admin home
    * Login/authentication
* About me
* Posts in markdown?
* "Contact" page consists of key-value pairs
* Posts can contain images