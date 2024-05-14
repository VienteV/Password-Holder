main_if_not_login = """"<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Form</title>
    <style>
        body {
            background-color: #f3f3f3;
            font-family: Arial, sans-serif;
        }

        .login-container {
            width: 300px;
            margin: 100px auto;
            padding: 20px;
            background-color: #e0f7fa;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .login-container h2 {
            text-align: center;
            color: #00897b;
        }

        .login-container input[type="text"],
        .login-container input[type="password"],
        .login-container input[type="submit"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #b2dfdb;
            border-radius: 5px;
            box-sizing: border-box;
        }

        .login-container input[type="submit"] {
            background-color: #4db6ac;
            color: white;
            cursor: pointer;
        }

        .login-container input[type="submit"]:hover {
            background-color: #009688;
        }
    </style>
</head>

<body>
    <div class="login-container">
        <h2>Login Form</h2>
        <form action="/main" method="post">
            <input type="text" name="username" placeholder="Username">
            <input type="password" name="password" placeholder="Password">
            <input type="submit" value="Login">
        </form>
    </div>
</body>

</html> """


main_if_login = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Form Template</title>
<style>
    body {
        background-color: #f0f0f0;
        font-family: Arial, sans-serif;
    }
    .container {
        display: flex;
        justify-content: space-between;
        padding: 20px;
    }
    .form-input {
        width: 50%;
        background-color: #c8e6c9;
        padding: 20px;
        margin-right: 20px;
    }
    .form-list {
        width: 40%;
        background-color: #a5d6a7;
        padding: 20px;
    }
    input[type="text"], textarea {
        width: 100%;
        padding: 8px;
        margin-bottom: 10px;
        box-sizing: border-box;
    }
    button {
        padding: 10px 20px;
        background-color: #4caf50;
        color: white;
        border: none;
        cursor: pointer;
    }
</style>
</head>
<body>
<div class="container">
    <div class="form-input">
        <h2>Add Information</h2>
        <form id="input-form" method='post'>
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name"><br>
            <label for="password">Password:</label><br>
            <input type="text" id="password" name="password"><br>
            <button type="submit">Submit</button>
        </form>
    </div>
    <div class="form-list">
        <h2>Passwords List</h2>
        <ul id="info-list">
        %for i in login_password:
            <li><a href='/main/{{i}}'>{{i}}</a></li>
        %end
        </ul>
    </div>
</div>

<script>
    const form = document.getElementById('input-form');
    const infoList = document.getElementById('info-list');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;

        const listItem = document.createElement('li');
        listItem.textContent = ${name} - ${email} - ${message};
        infoList.appendChild(listItem);
        
        form.reset();
    });
</script>
</body>
</html>"""

one_site = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Form Template</title>
<style>
    body {
        background-color: #f0f0f0;
        font-family: Arial, sans-serif;
    }
    .container {
        display: flex;
        justify-content: space-between;
        padding: 20px;
    }
    .form-input {
        width: 50%;
        background-color: #c8e6c9;
        padding: 20px;
        margin-right: 20px;
    }
    .form-list {
        width: 40%;
        background-color: #a5d6a7;
        padding: 20px;
    }
    input[type="text"], textarea {
        width: 100%;
        padding: 8px;
        margin-bottom: 10px;
        box-sizing: border-box;
    }
    button {
        padding: 10px 20px;
        background-color: #4caf50;
        color: white;
        border: none;
        cursor: pointer;
    }
</style>
</head>
<body>
    <div class="form-list">
        <h2>{{name}}</h2>
        <ul id="info-list">
        <h3>Password: {{password}}</h3>
        <h1><form id="input-form" method='post'>
        <button type="submit" name="action" value="Delete">Delete</button>
        </form></h1>
        <form id="input-form" method='post'>
        <label for="password">New password:</label><br>
        <input type="text" id="password" name="password"><br>
        <button type="submit" name="action" value='Update'>Update password</button>
        </form>
    </div>
</div>
<script>
    const form = document.getElementById('input-form');
    const infoList = document.getElementById('info-list');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;

        const listItem = document.createElement('li');
        listItem.textContent = ${name} - ${email} - ${message};
        infoList.appendChild(listItem);
        
        form.reset();
    });
</script>
</body>
</html>
"""

