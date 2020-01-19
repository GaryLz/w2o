# w2o
word2odio: a routine helper to english word learners, from a specific wordlist to a clip of audio. #mini_program #wechat


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
├── ELC
│   ├── ELC.json
│   └── ELC.mp3
├── LICENSE
├── README.md
├── Speech_US
│   ├── amazing.mp3
│   ├── atheist.mp3
│   ├── awesome.mp3
│   ├── coastal.mp3
│   ├── cool.mp3
│   ├── coral.mp3
│   ├── cruel.mp3
│   ├── exam.mp3
│   ├── excellent.mp3
│   ├── extraordinary.mp3
│   ├── fabulous.mp3
│   ├── faculty.mp3
│   ├── fantastic.mp3
│   ├── good.mp3
│   ├── gorgeous.mp3
│   ├── great.mp3
│   ├── naval.mp3
│   ├── nonsense.mp3
│   ├── one.mp3
│   ├── pathetic.mp3
│   ├── quiz.mp3
│   ├── sad.mp3
│   ├── stunning.mp3
│   ├── submarine.mp3
│   ├── test.mp3
│   └── tutourial.mp3
├── pycache
│   ├── api.cpython-37.pyc
│   ├── json_formatter.cpython-37.pyc
│   └── wordlist.cpython-37.pyc
├── api.py
├── foo.py
├── json_formatter.py
├── w2o.py
└── wordlist.py

3 directories, 38 files

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



