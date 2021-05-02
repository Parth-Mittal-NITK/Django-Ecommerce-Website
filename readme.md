# Django_Ecommerce_Website
My first website using Django's Model View Template architecture

<h3>Installing and using a Virtual Environment</h3>

`pip install virtualenvwrapper-win`<br>
`mkvirtualenv test` &nbsp; _test = name of virtual env_

<h3>Install required packages:</h3>

`pip install Django`<br>

<h3>To run project:</h3>

`pip install -r requirements.txt`<br>
_After ensuring that we are in a virtual environment (If not, use `workon test`)_



`python manage.py makemigrations` <br>
`python manage.py migrate` <br>
`python manage.py runserver`<br>

<h3>Create Super user:</h3>

`python manage.py createsuperuser`

<h3>Admin Site:</h3>

http://127.0.0.1:8000/admin

<h3>Implemented Features</h3>
<ul>
    <li>User Registration, Login and Logout</li>
    <li>Extended default user model</li>
    <li>Cart functionality</li>
    <li>Viewing each product</li>
    <li>Searching Products</li>
    <li>Placing order</li>    
</ul>
<h3>Non-implemented Features</h3>
<ul>
    <li>Changing quantity of items in cart</li>
    <li>Buy Now</li>
    <li>Persistant Cart with each user</li>
</ul>
<h3>References:</h3>
<a href="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">CodeWithHarry Django Series </a><br>
<a href="https://www.youtube.com/playlist?list=PLsyeobzWxl7r2ukVgTqIQcl-1T0C2mzau">Telusko Django Series </a><br>
<p>Stackoverflow</p>