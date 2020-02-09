# w2o
word2odio: a routine helper to english word learners, from a specific wordlist to a clip of audio. #mini_program #wechat

[TOC]

### v1.0
Note: Not a mini pg, it's a python program rather.
> main files:
> - api.py
> - wordlist.py
> - w2o.py(main)
> - json_formatter.py

#### Directory general structure:
```shell
.
├── LICENSE
├── README.md
├── __pycache__
│   ├── api.cpython-37.pyc
│   ├── json_formatter.cpython-37.pyc
│   └── wordlist.cpython-37.pyc
├── api.py
├── foo.py
├── json_formatter.py
├── w2o.py
└── wordlist.py

1 directory, 10 files

'generating EXAMPLE_DIR ...'
CWD = "~/Documents/daily-vocab/"
├── ELC (DIR_EXAMPLE)
│   ├── ELC.json
│   └── ELC.mp3
│   └── ELC.txt

```



#### dependencies
>In my case, env: Mac-MacOS Majave 10.14.6 (18G103), Homebrew
- pydub.AudioSegment
```shell
pip3 install pydub
```
- ffmpeg or libav
```shell
brew install ffmpeg libavcodec-extra
```

---
dev_log:

## to-do:
- bugs:
    - shared data problem of the same wordlist in loops
- features:
    - audio ouput based on files, without inputting words on console(supported format: .txt)

