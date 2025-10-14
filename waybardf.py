#!/usr/bin/env python3
'''
Waybar module for displaying the storage space used/available on 1 mount point
'''
import os
import sys
import json
import argparse

def main():
    text = ''
    tooltip = ''
    cssclass = 'normal'

    parser = argparse.ArgumentParser(
        prog = 'waybardf.py',
        description = 'Waybar module for displaying the storage space used/available on 1 mount point',
    )
    parser.add_argument('-l', '--label', type=str, help='label to be displayed (defaults to the full mount point path)')
    parser.add_argument('-d', '--debug', default=False, action='store_true')
    parser.add_argument('mountpoint', const=None, type=str, help='mount point - ex: \'/mnt/backups\'')
    args = parser.parse_args()
    if args.label: label = args.label
    else: label = args.mountpoint
    mnt = args.mountpoint
    cmd = f'df -h --output=size,used,pcent,avail {mnt} | tail -n1'
    result = os.popen(cmd).read()
    if (args.debug): sys.stderr.write(f'result: {result}')

    fields = result.split()
    size = fields[0]
    used = fields[1]
    pcent = fields[2]
    avail = fields[3]
    text = f'{label}: {pcent}'
    pcent = int(pcent.strip('%'))
    if pcent > 90: cssclass = 'warning'
    if pcent > 98: cssclass = 'critical'
    tooltip = f'''total space:\t{size}
used:\t\t{used}
available:\t{avail}'''
    output_json = {
        'text': text,
        'tooltip': tooltip,
        'class': cssclass
    }
    out = json.dumps(output_json)
    if (args.debug): sys.stderr.write(out)
    print(out)

if __name__ == '__main__':
    main()
