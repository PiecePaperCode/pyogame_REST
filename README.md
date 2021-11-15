# pyogame_REST
![picture](Screenshot.png)
<pre>
This is the pyogame REST API for the library pyogame.
Every function or variable in pyogame is presentet in the url Path. 
Functions that expect parameters are POST JSON request.

You Login over the '/login' url. Same arguments as in pyogame. (see Client.py)
'/' gives you an overview of all functions and variables.
</pre>
# install
```shell
pip install -r requirements.txt 
```
# run
```shell
python3 API.py 
Running on http://127.0.0.1:5000/
```
# client
The client.py represents an reference implementation.
for more information go to https://github.com/alaingilbert/pyogame
