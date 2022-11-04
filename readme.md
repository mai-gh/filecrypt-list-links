

## automate downloading from filecrypt / zippyshare

```
git clone https://github.com/mansuf/zippyshare-downloader
wget https://raw.githubusercontent.com/mai-gh/filecrypt-list-links/main/gen-links.py
python gen-links.py https://filecrypt.co/Container/XXXXXXXXXX | tee link-list.txt
cat link-list.txt | while read line; do PYTHONPATH=$(pwd)/zippyshare-downloader python -m zippyshare_downloader $line; done
```
