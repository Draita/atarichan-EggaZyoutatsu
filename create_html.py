import json

html_template = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Flash Games Archive</title>
    <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css'>
    <script src="https://unpkg.com/@ruffle-rs/ruffle"></script>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            height: 100vh;
            overflow: hidden;
        }}
        #menu {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.9);
            z-index: 10;
            overflow-y: auto;
            justify-content: center;
            align-items: center;
        }}
        #menu ul {{
            list-style: none;
            padding: 20px;
            margin: 0;
            max-height: 80vh;
            overflow-y: auto;
        }}
        #menu li {{
            margin: 10px 0;
        }}
        #menu button {{
            background: none;
            border: none;
            color: white;
            font-size: 18px;
            cursor: pointer;
            width: 100%;
            text-align: center;
            padding: 10px;
        }}
        #menu button:hover {{
            background: rgba(255, 255, 255, 0.1);
        }}
        #hamburger, #settings {{
            position: fixed;
            z-index: 20;
            font-size: 30px;
            cursor: pointer;
            background: rgba(0, 0, 0, 0.5);
            color: white;
            border: none;
            padding: 10px;
            border-radius: 5px;
        }}
        #hamburger {{
            top: 20px;
            left: 20px;
        }}
        #settings {{
            top: 20px;
            right: 20px;
        }}
        #gameContainer {{
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 800px;
            height: 600px;
            max-width: 100%;
            max-height: 100%;
        }}
        #sizeMenu {{
            display: none;
            position: fixed;
            top: 70px;
            right: 20px;
            background: rgba(0, 0, 0, 0.8);
            padding: 10px;
            border-radius: 5px;
            z-index: 15;
            max-height: 80vh;
            overflow-y: auto;
        }}
        #sizeMenu button, #sizeMenu label {{
            display: block;
            width: 100%;
            padding: 5px;
            margin: 5px 0;
            background: none;
            border: none;
            color: white;
            cursor: pointer;
        }}
        #sizeMenu button:hover, #sizeMenu label:hover {{
            background: rgba(255, 255, 255, 0.1);
        }}
    </style>
</head>
<body>
    <button id='hamburger'><i class='fas fa-bars'></i></button>
    <button id='settings'><i class='fas fa-cog'></i></button>
    <div id='menu'>
        <ul></ul>
    </div>
    <div id='sizeMenu'>
        <label><input type="checkbox" id="fullscreenCheck"> Fullscreen</label>
        <button onclick="setSize('100%', '100%')">Fill Browser</button>
        <button onclick="setSize('1920px', '1080px')">1920x1080</button>
        <button onclick="setSize('1600px', '900px')">1600x900</button>
        <button onclick="setSize('1366px', '768px')">1366x768</button>
        <button onclick="setSize('1280px', '720px')">1280x720</button>
        <button onclick="setSize('1024px', '768px')">1024x768</button>
        <button onclick="setSize('800px', '600px')">800x600</button>
        <button onclick="setSize('640px', '480px')">640x480</button>
    </div>
    <div id='gameContainer'></div>

    <script>
        const games = {json_data};

        document.getElementById('hamburger').onclick = function() {{
            const menu = document.getElementById('menu');
            menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';
        }};

        document.getElementById('settings').onclick = function() {{
            const sizeMenu = document.getElementById('sizeMenu');
            sizeMenu.style.display = sizeMenu.style.display === 'block' ? 'none' : 'block';
        }};

        document.getElementById('fullscreenCheck').onchange = function() {{
            if (this.checked) {{
                if (document.documentElement.requestFullscreen) {{
                    document.documentElement.requestFullscreen();
                }}
            }} else {{
                if (document.exitFullscreen) {{
                    document.exitFullscreen();
                }}
            }}
        }};

        function setSize(width, height) {{
            const container = document.getElementById('gameContainer');
            container.style.width = width;
            container.style.height = height;
            document.getElementById('sizeMenu').style.display = 'none';
        }}

        document.addEventListener('fullscreenchange', function() {{
            const fullscreenCheck = document.getElementById('fullscreenCheck');
            fullscreenCheck.checked = !!document.fullscreenElement;
        }});

        function loadGame(index) {{
            const game = games[index];
            const binaryString = atob(game.data);
            const bytes = new Uint8Array(binaryString.length);
            for (let i = 0; i < binaryString.length; i++) {{
                bytes[i] = binaryString.charCodeAt(i);
            }}
            const uncompressed = pako.inflate(bytes);
            const blob = new Blob([uncompressed], {{type: 'application/x-shockwave-flash'}});
            const url = URL.createObjectURL(blob);

            const container = document.getElementById('gameContainer');
            container.innerHTML = '';
            const ruffleObject = RufflePlayer.newest();
            const player = ruffleObject.createPlayer();
            player.style.width = '100%';
            player.style.height = '100%';
            container.appendChild(player);
            player.load({{url: url}});
            document.getElementById('menu').style.display = 'none';
            window.location.hash = game.name;
        }}

        function loadGameFromHash() {{
            const hash = window.location.hash.substring(1);
            const gameIndex = games.findIndex(game => game.name === hash);
            if (gameIndex !== -1) {{
                loadGame(gameIndex);
            }}
        }}

        window.addEventListener('load', loadGameFromHash);
        window.addEventListener('hashchange', loadGameFromHash);

        const menuList = document.getElementById('menu').getElementsByTagName('ul')[0];
        games.forEach((game, index) => {{
            const li = document.createElement('li');
            const button = document.createElement('button');
            button.textContent = game.name;
            button.onclick = () => {{
                window.location.hash = game.name;
            }};
            li.appendChild(button);
            menuList.appendChild(li);
        }});
    </script>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/pako/2.0.4/pako.min.js'></script>
</body>
</html>
"""

# Read the JSON data from the file
with open('flash_games.json', 'r') as f:
    json_data = f.read()

# Write the updated HTML to a file
with open('index.html', 'w') as f:
    f.write(html_template.format(json_data=json_data))

print("index.html file updated successfully with routing functionality, fullscreen checkbox, and resizable game window.")