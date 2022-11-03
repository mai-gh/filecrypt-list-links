

## automate downloading from filecrypt / zippyshare

```
git clone https://github.com/mansuf/zippyshare-downloader
cd zippyshare-downloader
wget https://raw.githubusercontent.com/mai-gh/filecrypt-list-links/main/gen-links.py
python gen-links.py $FILECRYPTURL > link-list.txt
cat link-list.txt | while read line; do PYTHONPATH=$(pwd) python -m zippyshare_downloader $line; done
```
