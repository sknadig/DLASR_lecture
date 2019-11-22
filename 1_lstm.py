from manimlib.imports import *

class Gate(object):
    def __init__(self, pos=0):
        pass
    def __call__(self):
        pass

class LSTM(Scene):
    CONFIG = {
            "camera_config": {
            "background_color": WHITE,
           },
           
           "circle_config": {
            "color": RED,
        },
    }
    def construct(self):
        lstm_square = Rectangle(stroke_width=1,
                stroke_color=BLACK,
                fill_opacity=1,
                height=4,
                width=8)
        
        self.play(ShowCreation(lstm_square), run_time=0.5)

        ctm1 = TexMobject(r"C_{t-1}", tex_to_color_map={
            r"C_{t-1}": BLACK})
        ctm1.scale(0.5)
        ctm1.move_to(lstm_square.get_corner(UL)+[-1, -0.5, 0])
        self.play(ShowCreation(ctm1), run_time=0.5)

        htm1 = TexMobject(r"h_{t-1}", tex_to_color_map={
            r"h_{t-1}": BLACK})
        htm1.scale(0.5)
        htm1.move_to(lstm_square.get_corner(DL)+[-1, 0.5, 0])
        self.play(ShowCreation(htm1), run_time=0.5)


        xt = TexMobject(r"x_{t}", tex_to_color_map={
            r"x_{t}": BLACK})
        xt.scale(0.5)
        xt.move_to(lstm_square.get_corner(DL)+[0.5, -1, 0])
        self.play(ShowCreation(xt), run_time=0.5)

        ctm1_arrow = Arrow(
            ctm1.get_right(),
            lstm_square.get_corner(UL) + [0, -0.5, 0],
            color=BLACK,
            buff=0.0,
        )

        htm1_arrow = Arrow(
            htm1.get_right(),
            lstm_square.get_corner(DL) + [0, 0.5, 0],
            color=BLACK,
            buff=0.0,
        )

        xt_arrow = Arrow(
            xt.get_top(),
            lstm_square.get_corner(DL) + [0.5, 0, 0],
            color=BLACK,
            buff=0.0,
        )

        self.play(ShowCreation(ctm1_arrow), run_time=0.5)
        self.play(ShowCreation(htm1_arrow), run_time=0.5)
        self.play(ShowCreation(xt_arrow), run_time=0.5)


    
        wif = Rectangle(stroke_width=1,
                stroke_color=BLACK,
                fill_opacity=1,
                height=0.5,
                width=0.5)

        whf = Rectangle(stroke_width=1,
                stroke_color=BLACK,
                fill_opacity=1,
                height=0.5,
                width=0.5)

        wif_text = TexMobject(r"W_{if}", tex_to_color_map={
            r"W_{if}": BLACK})
        wif_text.scale(0.5)

        whf_text = TexMobject(r"W_{hf}", tex_to_color_map={
            r"W_{hf}": BLACK})
        whf_text.scale(0.5)
        
        wif.move_to([-2.75,-1,0])
        whf.next_to(wif, RIGHT, buff=0)
        wif_text.move_to(wif)
        whf_text.move_to(whf)

        

        self.play(ShowCreation(wif), run_time=0.5)
        self.play(ShowCreation(wif_text), run_time=0.5)
        
        self.play(ShowCreation(whf), run_time=0.5)
        self.play(ShowCreation(whf_text), run_time=0.5)

        sum1 = Circle(stroke_width=1, radius=0.1)
        sum1.move_to(wif.get_corner(UR)+[0,0.5,0])
        sum1_text = TexMobject("+", tex_to_color_map={
            "+": BLACK})
        sum1_text.move_to(sum1)
        sum1_text.scale(0.5)

        self.play(ShowCreation(sum1), run_time=0.5)
        self.play(ShowCreation(sum1_text), run_time=0.5)

        wif_to_sum = Arrow(
            wif.get_top(),
            sum1.get_left(),
            color=BLACK,
            buff=0.0,
            path_arc= -90 * DEGREES,
        )

        whf_to_sum = Arrow(
            whf.get_top(),
            sum1.get_right(),
            color=BLACK,
            buff=0.0,
            path_arc= 90 * DEGREES,
        )

        self.play(ShowCreation(wif_to_sum), run_time=0.5)
        self.play(ShowCreation(whf_to_sum), run_time=0.5)





        wii = Rectangle(stroke_width=1,
                stroke_color=BLACK,
                fill_opacity=1,
                height=0.5,
                width=0.5)

        whi = Rectangle(stroke_width=1,
                stroke_color=BLACK,
                fill_opacity=1,
                height=0.5,
                width=0.5)

        wii_text = TexMobject(r"W_{ii}", tex_to_color_map={
            r"W_{ii}": BLACK})
        wii_text.scale(0.5)

        whi_text = TexMobject(r"W_{hi}", tex_to_color_map={
            r"W_{hi}": BLACK})
        whi_text.scale(0.5)

        wii.next_to(whf, RIGHT, buff=0.25)
        whi.next_to(wii, RIGHT, buff=0)

        wii_text.move_to(wii)
        whi_text.move_to(whi)

        self.play(ShowCreation(wii), run_time=0.5)
        self.play(ShowCreation(wii_text), run_time=0.5)
        self.play(ShowCreation(whi), run_time=0.5)
        self.play(ShowCreation(whi_text), run_time=0.5)

        sum2 = Circle(stroke_width=1, radius=0.1)
        sum2.move_to(wii.get_corner(UR)+[0,0.5,0])

        sum2_text = TexMobject("+", tex_to_color_map={
            "+": BLACK})
        sum2_text.move_to(sum2)
        sum2_text.scale(0.5)

        self.play(ShowCreation(sum2), run_time=0.5)
        self.play(ShowCreation(sum2_text), run_time=0.5)

        wii_to_sum = Arrow(
            wii.get_top(),
            sum2.get_left(),
            color=BLACK,
            buff=0.0,
            path_arc= -90 * DEGREES,
        )

        whi_to_sum = Arrow(
            whi.get_top(),
            sum2.get_right(),
            color=BLACK,
            buff=0.0,
            path_arc= 90 * DEGREES,
        )

        self.play(ShowCreation(wii_to_sum), run_time=0.5)
        self.play(ShowCreation(whi_to_sum), run_time=0.5)





        wig = Rectangle(stroke_width=1,
                stroke_color=BLACK,
                fill_opacity=1,
                height=0.5,
                width=0.5)

        whg = Rectangle(stroke_width=1,
                stroke_color=BLACK,
                fill_opacity=1,
                height=0.5,
                width=0.5)

        wig_text = TexMobject(r"W_{ig}", tex_to_color_map={
            r"W_{ig}": BLACK})
        wig_text.scale(0.5)

        whg_text = TexMobject(r"W_{hg}", tex_to_color_map={
            r"W_{hg}": BLACK})
        whg_text.scale(0.5)

        wig.next_to(whi, RIGHT, buff=0.25)
        whg.next_to(wig, RIGHT, buff=0)

        wig_text.move_to(wig)
        whg_text.move_to(whg)

        self.play(ShowCreation(wig), run_time=0.5)
        self.play(ShowCreation(wig_text), run_time=0.5)
        self.play(ShowCreation(whg), run_time=0.5)
        self.play(ShowCreation(whg_text), run_time=0.5)

        sum3 = Circle(stroke_width=1, radius=0.1)
        sum3.move_to(wig.get_corner(UR)+[0,0.5,0])

        sum3_text = TexMobject("+", tex_to_color_map={
            "+": BLACK})
        sum3_text.move_to(sum3)
        sum3_text.scale(0.5)

        self.play(ShowCreation(sum3), run_time=0.5)
        self.play(ShowCreation(sum3_text), run_time=0.5)

        wig_to_sum = Arrow(
            wig.get_top(),
            sum3.get_left(),
            color=BLACK,
            buff=0.0,
            path_arc= -90 * DEGREES,
        )

        whg_to_sum = Arrow(
            whg.get_top(),
            sum3.get_right(),
            color=BLACK,
            buff=0.0,
            path_arc= 90 * DEGREES,
        )

        self.play(ShowCreation(wig_to_sum), run_time=0.5)
        self.play(ShowCreation(whg_to_sum), run_time=0.5)








        wio = Rectangle(stroke_width=1,
                stroke_color=BLACK,
                fill_opacity=1,
                height=0.5,
                width=0.5)

        who = Rectangle(stroke_width=1,
                stroke_color=BLACK,
                fill_opacity=1,
                height=0.5,
                width=0.5)

        wio_text = TexMobject(r"W_{io}", tex_to_color_map={
            r"W_{io}": BLACK})
        wio_text.scale(0.5)

        who_text = TexMobject(r"W_{ho}", tex_to_color_map={
            r"W_{ho}": BLACK})
        who_text.scale(0.5)

        wio.next_to(whg, RIGHT, buff=0.25)
        who.next_to(wio, RIGHT, buff=0)

        wio_text.move_to(wio)
        who_text.move_to(who)

        self.play(ShowCreation(wio), run_time=0.5)
        self.play(ShowCreation(wio_text), run_time=0.5)
        self.play(ShowCreation(who), run_time=0.5)
        self.play(ShowCreation(who_text), run_time=0.5)

        sum4 = Circle(stroke_width=1, radius=0.1)
        sum4.move_to(wio.get_corner(UR)+[0,0.5,0])

        sum4_text = TexMobject("+", tex_to_color_map={
            "+": BLACK})
        sum4_text.move_to(sum4)
        sum4_text.scale(0.5)

        self.play(ShowCreation(sum4), run_time=0.5)
        self.play(ShowCreation(sum4_text), run_time=0.5)

        wio_to_sum = Arrow(
            wio.get_top(),
            sum4.get_left(),
            color=BLACK,
            buff=0.0,
            path_arc= -90 * DEGREES,
        )

        who_to_sum = Arrow(
            who.get_top(),
            sum4.get_right(),
            color=BLACK,
            buff=0.0,
            path_arc= 90 * DEGREES,
        )

        self.play(ShowCreation(wio_to_sum), run_time=0.5)
        self.play(ShowCreation(who_to_sum), run_time=0.5)


        htm1_path = VMobject()
        htm1_path.set_stroke(BLACK, 2)
        htm1_path.start_new_path(lstm_square.get_corner(DL)+[0,0.5,0])
        htm1_path.add_line_to(who.get_bottom()+[0,-0.25,0])

        self.play(GrowArrow(htm1_path), run_time=0.5)

        htm1_to_whf = Arrow(
            whf.get_bottom()+[0,-0.25,0],
            whf.get_bottom(),
            color=BLACK,
            stroke_width=2,
            buff=0.0,
        )

        htm1_to_whi = Arrow(
            whi.get_bottom()+[0,-0.25,0],
            whi.get_bottom(),
            color=BLACK,
            stroke_width=2,
            buff=0.0,
        )

        htm1_to_whg = Arrow(
            whg.get_bottom()+[0,-0.25,0],
            whg.get_bottom(),
            color=BLACK,
            stroke_width=2,
            buff=0.0,
        )

        htm1_to_who = Arrow(
            who.get_bottom()+[0,-0.25,0],
            who.get_bottom(),
            color=BLACK,
            stroke_width=2,
            buff=0.0,
        )

        self.play(ShowCreation(htm1_to_whf), run_time=0.5)
        self.play(ShowCreation(htm1_to_whi), run_time=0.5)
        self.play(ShowCreation(htm1_to_whg), run_time=0.5)
        self.play(ShowCreation(htm1_to_who), run_time=0.5)