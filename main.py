from manim import *

code_file = "hello_world.py"

code_text = ""

my_lang = "python"

time_to_write: int | float = 4
time_to_show: int | float = 1
time_to_unwrite: int | float = 4


class SlowHighlightedCode(Scene):
    def construct(self):
        if code_file:    
            code = Code(
                code_file = code_file,
                language=my_lang,
                background_config={"fill_opacity": 0},
                paragraph_config={"font": "Noto Sans Mono"},
            ).scale(0.7)
        elif code_text:
            code = Code(
                code_string = my_code,
                language=my_lang,
                background_config={"fill_opacity": 0},
                paragraph_config={"font": "Noto Sans Mono"},
            ).scale(0.7)
        else:
            raise ValueError("Please enter the code to code_text or code_file")

        self.play(Write(code, run_time=time_to_write))
        self.wait(time_to_show)
        self.play(Unwrite(code, run_time=time_to_unwrite, reverse=False))
        self.wait(2)
