<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Webpage</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
            padding: 50px;
        }

        h1 {
            color: #333;
        }

        p {
            color: #666;
        }

        button {
            background-color: blue;
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 5px;
        }

        button:hover {
            background-color: darkblue;
        }
    </style>
</head>
<body>

    <h1>Welcome to HTML</h1>
    <p>This is a simple HTML page with CSS and JavaScript.</p>

    <button onclick="showMessage()">Click Me</button>

    <script>
        function showMessage() {
            alert("Hello! You clicked the button.");
        }
    </script>

</body>
</html>
