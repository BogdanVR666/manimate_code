## Manimation the code
This simple script allows you to animate your code to using that animation in video editor

- requirements:
  + manim
  + LaTeX (optional)

to use this script, put code file to same directory or write code into `code_text` var in `main.py` file, and use 
```bash
uv run manim -qh --format=mov --transparent main.py
```
and this way you will get a `media` folder, the file you needed is in the `media/videos/main/1080p60/` directory
