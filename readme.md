# EggaZyoutatsu Preservation
[click here to open the website](https://draita.github.io/eggazyoutatsu/)

This project aims to preserve and make accessible a collection of Flash games by embedding them directly into an HTML file. The main components of the project are:

1. A Python script (\`generate_json.py\`) that compresses and encodes Flash (.swf) files.
2. An HTML file that loads and runs the embedded Flash games.

## Key Features

- **Compression and Encoding**: The Python script uses gzip compression and base64 encoding to efficiently store Flash games in a JSON format.
- **Standalone HTML**: The resulting HTML file is self-contained, allowing users to save and run the games locally without an internet connection.
- **Preservation**: This method ensures that these Flash games remain playable even as browser support for Flash diminishes.

## Importance of Embedding

Embedding the Flash files directly in the HTML is crucial for several reasons:

1. **Portability**: The entire collection can be distributed as a single HTML file.
2. **Offline Access**: Users can save the HTML file and play the games without an internet connection.
3. **Long-term Preservation**: As Flash support declines, this method ensures the games remain accessible.
4. **Ease of Use**: No need for separate file management or external dependencies.

## Usage

1. Place your .swf files in the 'flash' folder.
2. Run the \`generate_json.py\` script to create the \`flash_games.json\` file.
3. Use the generated JSON data to create the final HTML file with embedded games.

## Project Structure

- \`flash/\`: Directory containing the original .swf files
- \`generate_json.py\`: Python script for compressing and encoding Flash files
- \`flash_games.json\`: Generated JSON file containing compressed and encoded Flash games
- \`index.html\`: Final HTML file with embedded games

By following this approach, we ensure that these classic Flash games remain accessible and playable for years to come, preserving an important part of internet gaming history.
