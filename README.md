# Safari bookmarks jsonizer

将 Safari 导出的书签文件转换为 JSON 格式的文件

## 运行

1. 下载代码

    ```sh
    git clone https://github.com/Monsoir/safari-bookmarks-jsonizer.git
    cd safari-bookmarks-jsonizer/
    ```

2. 创建并激活虚拟环境，使用的是 Python 3.6.2 开发

    virtualenv --no-site-packages env
    source env/bin/activate
    ```

3. 安装依赖

    ```sh
    pip install -r requirements.txt 
    ```

4. 使用

    ```sh
    python jsonize.py -i ./Safari\ Bookmarks.html -o result.json
    ```

## 帮助

```sh
python jsonize.py -h
```

```
transform.py -i <input file> -o <output file>
transform.py -input <input file> -o <output file>

other options:
--ignore-folder: an array of folder names which and bookmarks in which will not appear in the result json file
--ignore-items: an array of bookmark names which will not appear in the result json file
--only-extract-folders: an array of folder names, bookmarks in which will be appear in the result json file, but not include the ones in subfolder name of which
--only-extract-items: an array of bookmark names which will appear in the result json file
```


