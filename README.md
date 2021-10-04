# Shake to find (XFCE Edition)

You don't need to buy an expensive MacBook to have this simple feature. No anymore. This simple python script increases and decreases the size of your cursor when you shake it.

## Installation

First, install the dependencies:

```
sudo apt-get update
sudo apt-get install python3 python3-pip
python3 -m pip install pyautogui
```

Just clone this repo and copy the script to /usr/bin

```bash
git clone https://github.com/Pasch0/Shake_To_Find.git
cd Shake_To_Find
sudo cp shaketofind.py /usr/bin
```

## Usage
You can just run or configure to start with your system

```bash
shaketofind
```

## Disclaimer
Some aplications read cursor state at start and don't apply changes after this. So, this function will work fine in most apps, but some apps like xterm, vscode or electron based will not apply increases or deacreses of cursor size. If you press Ctrl+Alt+T when your cursor increases, only in your terminal the cursor will be always big. It's not a script bug, it's a limitation of this aplication.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
