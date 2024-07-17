# wallpaperhub-downloader
A simple python project to download a batch of wallpapers from [wallpaperhub.app](https://www.wallpaperhub.app/)

## Features
- Download wallpapers from wallpaperhub.app
- Specify the creator of the wallpaper
- Wallpaper title as filename

## Usage
1. Clone the repository
2. Install the required packages
```bash
pip install requests
```
3. Run the script
```bash
python main.py
```

After running the script, you will start downloading 20 random wallpapers by the creator Microsoft from wallpaperhub.app. The wallpapers will be saved in the `./downloads/microsoft/` folder in the root directory of the project.

## TODO
- [ ] Add a wallpaper_info.csv file to handle metadata for all downloaded wallpapers (e.g., file_path, creator, title, description, resolution, downloads, etc.).
- [ ] Add "Pick" feature. "Pick" feature will allow the user to pick wallpapers based on the metadata in the wallpaper_info.csv file. (pick only high-res, pick only specific creator, etc.)
- [ ] Utilize multi-modal models (like CLIP) to create a themed album from downloaded wallpapers based on sentence prompts.
- [ ] Automatically find the max_page for specific creator and limit.
- [ ] (?) Add a GUI for the script (using Tkinter or PyQt)