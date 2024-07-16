#%%
import requests
import random
import os

def get_wallpaper_url_batch(api_url: str, limit: int = 20, max_pages: int = 1) -> list:
    """
    Get a batch of wallpaper URLs from the WallpaperHub API.

    Parameters
    ----------
    creator_url : str
        The URL of API to the creator whose wallpapers are to be retrieved.
    limit : int, optional
        The number of wallpapers to retrieve per page, by default 20.
    max_pages : int, optional
        The maximum number of pages to retrieve, by default 1.

    Returns
    -------
    list
        A list of wallpaper URLs.

    """

    # Define the URL of the API
    url = "https://wallpaperhub.app/api/v1/creators/microsoft/wallpapers/"
    # Set the parameters for the request
    params = {
        'limit': limit,
        'page': random.randint(1, max_pages)
    }

    # Send a GET request
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the wallpaper URLs
        wallpaper_urls = [item['entity']['variations'][0]['resolutions'][0]['url'] for item in data['entities']]
        wallpaper_titles = [item['entity']['title'] for item in data['entities']]
        return wallpaper_urls, wallpaper_titles
        # print(f"URL: {data['entities'][0]['entity']['variations'][0]['resolutions'][0]['url']}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return [], []
    
def download_wallpaper(url: str, path: str):
    """
    Download a wallpaper from a given URL.

    Parameters
    ----------
    url : str
        The URL of the wallpaper to download.
    path : str
        The path where the wallpaper will be saved.

    Returns
    -------
    bool
        True if the wallpaper was downloaded successfully, False otherwise.

    """
    # Send a GET request
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Save the image to a file
        with open(path, 'wb') as file:
            file.write(response.content)
        return True
    else:
        print(f"Failed to download wallpaper. Status code: {response.status_code}")
        return False
    
# Get a batch of wallpaper URLs
print("Getting wallpaper URLs...")
creator = 'microsoft'
api_url = f'https://wallpaperhub.app/api/v1/creators/{creator}/wallpapers/'
wallpaper_urls, wallpaper_titles = get_wallpaper_url_batch(api_url=api_url,
                                         limit=20, 
                                         max_pages=215)
print(f"Retrieved {len(wallpaper_urls)} wallpaper URLs")

# Create the 'downloads' folder if it doesn't exist
if not os.path.exists('./downloads'):
    # Create the 'downloads' folder
    os.makedirs('./downloads')

# Download wallpapers
print("Downloading wallpapers...")
for i in range(len(wallpaper_urls)):
    wallpaper_title = wallpaper_titles[i].replace(' ', '_')
    wallpaper_title = ''.join(c for c in wallpaper_title if c.isalnum() or c in ['_', '-'])
    wallpaper_title = wallpaper_title[:255]  # Limit the title to 255 characters
    download_wallpaper(wallpaper_urls[i], f"./downloads/{wallpaper_title}.jpg")
    print(f"Downloaded wallpaper {i+1} of {len(wallpaper_urls)}")

# %%