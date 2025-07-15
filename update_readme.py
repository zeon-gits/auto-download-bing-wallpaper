from datetime import datetime, timedelta
from glob import glob


def writeToReadme():
    readme_path = 'README.md'

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('# Bing Wallpaper\n\n')

        f.write('\n')
        f.write('Daily Automated Bing Wallpaper Scraping via Github Actions\n\n')
        f.write('picurl.py will create a DownloadedWallpapers folder in the current directory,\n')
        f.write('and save the downloaded wallpaper to that folder.\n\n')
        f.write('After cloning this repository to your local machine, you can run picurl.py to scrape wallpaper\n')
        f.write('\n')

        filename = datetime.now().strftime("%Y-%m-%d")
        paths = glob(f'./DownloadedWallpapers/{filename}.jpg')
        if paths:
            f.write('\n\n## Photo Today\n')
            f.write('\n\n![]({}){} [Download]({})'.format(paths[0], filename, paths[0]))

        f.write('\n\n## Photo Links from the Last 30 Days\n')
        f.write('\n\n|      |      |      |\n')
        f.write('| :----: | :----: | :----: |\n')
        index = 1
        for i in range(30):
            date = datetime.now() - timedelta(days=i)
            filename = date.strftime("%Y-%m-%d")
            paths = glob(f'./DownloadedWallpapers/{filename}.jpg')
            if paths:
                file = "![]({}){} [Download]({})".format(paths[0], filename, paths[0])
                f.write('|' + file)
                if index % 3 == 0:
                    f.write('|\n')
                index += 1

        if index % 3 != 1:
            f.write('|')

        f.write('\n\n')
        print(f'successfully updated {readme_path}')


if __name__ == '__main__':
    writeToReadme()
