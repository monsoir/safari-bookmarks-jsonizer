# Safari bookmarks jsonizer

Transform exported Safari bookmarks as JSON file

## How to use

1. Create and activate a virtual environment, using Python 3.6.2

    ```
    virtualenv --no-site-packages env
    source env/bin/activate
    ```

2. Install

    ```sh
    pip install safari-bookmarks-jsonizer
    ```

3. Run it

    ```sh
    jsonize -i ./Safari\ Bookmarks.html -o ./result.json
    ```

## Output file format

```JSON
{
    "title": "<category name>",
    "catelogs": [
        {
            "address": "<bookmark address>",
            "name": "<bookmark name>",
            "favicon": "<bookmark icon, optional>",
            "remark": "<remark of the bookmark, optional>"
        },
        {
            "//": "..."
        }
    ],
    "categories": [
        {
            "title": "subcategory name",
            "catelogs": [
                {
                    "//": "...",
                }
            ],
            "categories": []
        }
    ]
}
```

## Help

```sh
jsonize -h
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


