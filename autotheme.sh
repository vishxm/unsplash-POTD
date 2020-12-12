#!/bin/bash
python base.py
rm ~/.config/wpg/schemes/*image*.json
wpg -a ~/us-scraper/image.png
wpg -s ~/us-scraper/image.png
feh --bg-fill /home/vishwas/us-scraper/image.png
