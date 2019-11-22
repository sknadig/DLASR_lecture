from manimlib.imports import *

class Gate(object):
    def __init__(self, pos=0):
        pass
    def __call__(self):
        pass

class RNN(Scene):
    CONFIG = {
            "camera_config": {
            "background_color": WHITE,
           },
           "circle_config": {
            "color": RED,
        },
    }
    
    def get_h(self, idx=0):

        h_0 = Rectangle(stroke_width=1,
                stroke_color=BLACK,
                fill_opacity=1,
                height=0.25,
                width=2)

        h_0.next_to(self.rnn_square, UP, buff=2)

        h_text = "h_{%s}" % (str(idx))

        h_0_text = TexMobject(h_text, tex_to_color_map={
            h_text: BLACK})

        h_0_text.scale(0.5)
        
        h_0_text.move_to(h_0)

        rnn_to_h0 = Arrow(
            self.tanh.get_top(),
            h_0.get_bottom(),
            color=BLACK,
            buff=0.0,
        )

        return h_0, h_0_text, rnn_to_h0
        
    def get_x(self, idx=0):
        x_0 = Rectangle(stroke_width=1,
                stroke_color=BLACK,
                fill_opacity=1,
                height=0.25,
                width=2)

        x_0.next_to(self.rnn_square, DOWN, buff=2)

        x_text = "x_{%s}" % (str(idx))

        x_0_text = TexMobject(x_text, tex_to_color_map={
            x_text: BLACK})
        x_0_text.scale(0.5)
        
        x_0_text.move_to(x_0)

        x0_to_rnn = Arrow(
            x_0.get_top(),
            self.rnn_square.get_bottom(),
            color=BLACK,
            buff=0.0,
        )

        return x_0, x_0_text, x0_to_rnn

    def get_htm1(self, idx=0):
        htm1 = Rectangle(stroke_width=1,
                stroke_color=BLACK,
                fill_opacity=1,
                height=0.5,
                width=2)

        htm1.next_to(self.rnn_square, LEFT, buff=1)

        h_text = "h_{%s}" % (str(idx))

        htm1_text = TexMobject(h_text, tex_to_color_map={
            h_text: BLACK})

        htm1_text.move_to(htm1)

        rnn_to_htm1 = Arrow(
            self.rnn_square.get_top(),
            htm1.get_top(),
            color=BLACK,
            buff=0.0,
            path_arc= 145 * DEGREES,
        )

        htm1_to_rnn = Arrow(
            htm1.get_bottom(),
            self.rnn_square.get_corner(DL) + [0,0.25,0],
            color=BLACK,
            buff=0.0,
            path_arc= 45 * DEGREES,
        )

        return htm1, htm1_text, rnn_to_htm1, htm1_to_rnn

    def construct(self):
        self.rnn_square = Rectangle(stroke_width=1,
                stroke_color=BLACK,
                fill_opacity=1,
                height=2,
                width=2)    

        
        self.wih = Rectangle(stroke_width=1,
                stroke_color=BLACK,
                fill_opacity=1,
                height=0.5,
                width=0.5) 
        
        self.wih.move_to(self.rnn_square.get_bottom() + [0, 0.25, 0])
        wih_text = TexMobject(r"W_{ih}", tex_to_color_map={
            r"W_{ih}": BLACK})
        wih_text.scale(0.5)
        wih_text.move_to(self.wih)


        self.whh = Rectangle(stroke_width=1,
                stroke_color=BLACK,
                fill_opacity=1,
                height=0.5,
                width=0.5) 

        self.whh.move_to(self.rnn_square.get_corner(DL) + [0.25, 0.25, 0])

        whh_text = TexMobject(r"W_{hh}", tex_to_color_map={
            r"W_{hh}": BLACK})
        whh_text.scale(0.5)
        whh_text.move_to(self.whh)

        sum1 = Circle(stroke_width=3, radius=0.1)
        sum1.move_to(self.wih.get_top()+[0,0.5,0])
        sum1_text = TexMobject("+", tex_to_color_map={
            "+": RED})
        sum1_text.move_to(sum1)
        sum1_text.scale(0.5)


        self.tanh = Rectangle(stroke_width=1,
                stroke_color=BLACK,
                fill_opacity=1,
                height=0.5,
                width=0.75) 

        self.tanh.move_to(sum1.get_top() + [0, 0.5, 0])

        self.tanh_text = TexMobject(r"tanh", tex_to_color_map={
            r"tanh": BLACK})
        self.tanh_text.scale(0.5)
        self.tanh_text.move_to(self.tanh)

        x0, x1, x2 = self.get_x(idx=0)
        h0, h1, h2 = self.get_h(idx=0)
        z0, z1, z2, z3 = self.get_htm1(idx=-1)

        wih_sum = Arrow(
            self.wih.get_top(),
            sum1.get_bottom(),
            color=BLACK,
            stroke_width = 4,
            buff=0.0,
        )

        whh_sum = Arrow(
            self.whh.get_top(),
            sum1.get_left(),
            color=BLACK,
            buff=0.0,
            stroke_width = 1,
            path_arc= -45 * DEGREES,
        )

        sum_tanh = Arrow(
            sum1.get_top(),
            self.tanh.get_bottom(),
            color=BLACK,
            stroke_width = 4,
            buff=0.0,
        )


        self.play(ShowCreation(self.rnn_square), ShowCreation(self.wih), ShowCreation(wih_text),
        ShowCreation(self.whh), ShowCreation(whh_text), ShowCreation(z0), ShowCreation(sum1), ShowCreation(sum1_text),
        ShowCreation(self.tanh), ShowCreation(self.tanh_text),
        ShowCreation(wih_sum),
        ShowCreation(whh_sum),
        ShowCreation(sum_tanh),
        ShowCreation(z1), run_time=2)

        self.play(ShowCreation(x0), ShowCreation(x1),
        ShowCreation(x2),
        ShowCreation(z3), run_time=2)

        self.play(ShowCreation(h0), ShowCreation(h1), 
        ShowCreation(h2),
        ShowCreation(z2), run_time=2)