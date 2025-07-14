from datetime import datetime, timedelta
from glob import glob


def writeToReadme():
    readme_path = 'README.md'

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('# Bing Wallpaper\n\n')

        f.write('\n')
        f.write('Python 每日爬取必应壁纸\n')
        f.write('\n')

        filename = datetime.now().strftime("%Y/%m/%d")
        paths = glob(f'./DownloadedWallpapers/{filename}.jpg')
        if paths:
            f.write('\n\n## 今日图片\n')
            f.write('\n\n![]({}){} [Download]({})'.format(paths[0], filename, paths[0]))

        f.write('\n\n## 最近30天的图片链接\n')
        f.write('\n\n|      |      |      |\n')
        f.write('| :----: | :----: | :----: |\n')
        index = 1
        for i in range(30):
            date = datetime.now() - timedelta(days=i)
            filename = date.strftime("%Y/%m/%d")
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


if __name__ == '__main__':
    writeToReadme()
