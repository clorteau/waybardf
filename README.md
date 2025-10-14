A module for waybar that monitors the storage space of mount points (using df)

![screenshot](https://raw.githubusercontent.com/clorteau/waybardf/refs/heads/main/screenshot.png)

# Dependencies
- Python
- df
# Download
Download [waybardf.py](https://raw.githubusercontent.com/clorteau/waybardf/refs/heads/main/waybardf.py) anywhere you have permission to read it.
# Usage
In your waybar's .jsonc, add one entry per mount point you want to monitor. Examples:
```json
"custom/df1": {
    "format": "🖴 {text}",
    "exec": "~/scripts/waybar/waybardf.py /",
    "return-type": "json",
    "interval": 30,
    "on-click": "pcmanfm-qt"
  },
  "custom/df2": {
    "format": "🖴 {text}",
    "exec": "~/scripts/waybar/waybardf.py -l backups /mnt/backups",
    "return-type": "json",
    "interval": 30,
    "on-click": "pcmanfm-qt /mnt/backups"
  },
```
This modules exposes 3 css classes for styling:
- 'normal'
- 'warning' when space usage is over 90%
- 'critical' when space usage is over 98%
Example of 'style.css':
```css
#custom-df1.normal, custom-df2.normal {
  background: @background-primary;
}
#custom-df1.warning, custom-df2.warning {
  background: darkorange;
}
#custom-df1.critical, custom-df2.critical {
  background: darkred;
}
```
The script takes 2 arguments:
- optional '--label': label to use instead of the mount point's path
- the mount point
```bash
./waybardf.py --help
usage: waybardf.py [-h] [-l LABEL] [-d] mountpoint

Waybar module for displaying the storage space used/available on 1 mount point

positional arguments:
  mountpoint         mount point - ex: '/mnt/backups'

options:
  -h, --help         show this help message and exit
  -l, --label LABEL  label to be displayed (defaults to the full mount point path)
  -d, --debug
````
