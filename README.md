<div align="center">

[![build](https://github.com/slickml/afk-bot/actions/workflows/ci.yml/badge.svg)](https://github.com/slickml/afk-bot/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/slickml/afk-bot/graph/badge.svg?token=Z7XP51MB4K)](https://codecov.io/gh/slickml/afk-bot)
[![license](https://img.shields.io/github/license/slickml/afk-bot)](https://github.com/slickml/afk-bot/blob/master/LICENSE/)
[![downloads](https://pepy.tech/badge/afk-bot)](https://pepy.tech/project/afk-bot)
![pypi_version](https://img.shields.io/pypi/v/afk-bot)
![python_version](https://img.shields.io/pypi/pyversions/afk-bot)
[![slack_invite](https://badgen.net/badge/Join/SlickML%20Slack/purple?icon=slack)](https://www.slickml.com/slack-invite)
![twitter_url](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FSlickML)

</div>
<p align="center">
  <a href="https://github.com/slickml/afk-bot">
    <img src="https://raw.githubusercontent.com/slickml/afk-bot/master/assets/logo.png" width="250"></img>
  </a>
</p>

<div align="center">
<h1 align="center">AFK-Bot🤖: A bot for the away from keyboard times
</h1>
</div>

## 🧠 Philosophy
We strongly believe that all developers should have full access to their resources (i.e. `sudo` access or permission to deactivate screens saver, ...). `afk-bot` 🤖 is a simple bot that moves the mouse cursor (every 1 second by default and it can be customized); so, your status never goes `Idle` and your screen never gets locked 😂 ...


## 🛠 Installation
To begin with, you need to have a [Python version >=3.8](https://www.python.org) installed and to install the library
from [PyPI](https://pypi.org/project/afk-bot/) simply run 🏃‍♀️ :
```
$ pip install afk-bot
```

## 📌 Quick Start
`afk-bot` is a `command-line` based bot and you can simply run it in any `terminal` 🏃‍♀️ :
```
$ afk-bot                     <- runs the bot and the mouse cursor moves every 1 second by default

$ afk-bot -t <interval-range> <- you can customize the interval with -t or --time

$ afk-bot --help              <- shows the options 
```
To `exit`, simply press `CTRL+C` keys. 

## 📣 Common Issues
  - Mac users should note that the accessibility to `Apple Events Server (AEServer)` should be turned on. Simply follow the steps 🏃‍♀️ :
    ```
    System Preferences > Security & Privacy > Choose Privacy Tab > Select Accessibility from Left Pane > Enable AEServer
    ```
  - Some Linux users might need to export the environment variable `DISPLAY`. Simply run 🏃‍♀️ :
    ```
    $ export DISPLAY=:0
    ```
## 🧑‍💻🤝 Contributing
If you think more features should be added, please open up an issue an. PRs are more than welcome 🙏 . You can find the details of the development process in our SlickML🧞 [Contributing](CONTRIBUTING.md) guidelines. We strongly believe that reading and following these guidelines will help us make the contribution process easy and effective for everyone involved 🚀🌙 .



## ❓ 🆘 📲 Need Help?
Please join our [Slack Channel](https://www.slickml.com/slack-invite) to interact directly with the core team and our small community. This is a good place to discuss your questions and ideas or in general ask for help 👨‍👩‍👧 👫 👨‍👩‍👦 .

