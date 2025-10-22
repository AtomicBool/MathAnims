from manim import *
class DotProduct(ThreeDScene):
    def construct(self):
        # 创建坐标系
        # 创建全屏网格背景
        grid = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.4
            },
            axis_config={
                "stroke_color": BLUE,
                "stroke_width": 2,
            },
            faded_line_ratio=1,
        )
        
        # 创建两个向量
        vec1 = Vector(grid.c2p(2, 0, 0), color=RED)
        vec2 = Vector(grid.c2p(1, 3, 5), color=GREEN)

        '''
            S1 SECTION 1
            绘制两个向量及其夹角
        ''' 
        
        # 添加向量标签
        vec1_label = MathTex("\\vec{a}(2, 0)").next_to(vec1.get_end(), UP)
        vec2_label = MathTex("\\vec{b}(1, 3)").next_to(vec2.get_end(), RIGHT)
        
        # 计算并绘制夹角
        angle = Angle(vec1, vec2, radius=0.6, other_angle=False)
        angle_label = MathTex("\\theta").next_to(angle, UR, buff=0.05)
        
        # 动画序列 1.1
        self.add(grid)
        self.play(GrowArrow(vec1), GrowArrow(vec2), run_time = 1.2)
        self.play(Write(vec1_label), Write(vec2_label), run_time = 1.2)
        self.play(Create(angle), Write(angle_label), run_time = 0.7)
        self.wait(6)

        '''
            S1 SECTION 2
            通过构造向量C并用余弦定理证明点乘
            来源 MIT OCW Multivariable Calculus, Lecture 1: Dot Product
        ''' 

        # 构造向量C链接AB
        vec_c = Arrow(vec1.get_end(), vec2.get_end(), buff=0, color=YELLOW).set_opacity(0.25)
        vec_c_label = MathTex("\\vec{c}").next_to(vec_c.get_center(), UP+RIGHT).set_opacity(0.75)

        # 方程组A 余弦定理及代入模长后的余弦定理
        formulaGroupA = [
            (r"c^2 = a^2 + b^2 - 2ab \cos \theta", {}),                                             # 1.1
            (r"|\vec{c}|^2 = |\vec{a}|^2 + |\vec{b}|^2 - 2|\vec{a}||\vec{b}|\cos\theta",            # 1.2
            {
                r"|\vec{c}|^2": YELLOW,
                r"|\vec{a}|^2": RED,
                r"|\vec{b}|^2": GREEN,
                r"2|\vec{a}||\vec{b}|\cos\theta" : BLUE
            })      
        ]

        ## 方程组A的mobject
        eq1_cosine_law_1 = MathTex(
            formulaGroupA[0][0],
            font_size = 48
        ).to_edge(UL)

        eq1_cosine_law_2 = MathTex(
            formulaGroupA[1][0],
            tex_to_color_map = formulaGroupA[1][1],
            font_size = 48
        ).to_edge(UL)

        # 方程组B 向量间关系的表达式

        formulaGroupB = [
            (r"\vec{b} = \vec{a} + \vec{c}", {}),                                                           # 2.1
            (r"\vec{c} = \vec{b} - \vec{a}", {}),                                                           # 2.2
            (r"(\vec{c})^2 = (\vec{b} - \vec{a})^2", {}),                                                   # 2.3
            (r"\vec{c}\cdot\vec{c} = \vec{a}\cdot\vec{a} + \vec{b}\cdot\vec{b} - 2\vec{a}\cdot\vec{b}",     # 2.4
            {
                r"\vec{c}\cdot\vec{c}": YELLOW,
                r"\vec{a}\cdot\vec{a}": RED,
                r"\vec{b}\cdot\vec{b}": GREEN,
                r"2\vec{a}\cdot\vec{b}": BLUE
            })
        ]

        ## 方程组B的mobject
        eq2_vec_c = []

        for i in range(len(formulaGroupB)):
            eq2_vec_c.append(MathTex(formulaGroupB[i][0], tex_to_color_map = formulaGroupB[i][1]))
            if(i <= 2) : eq2_vec_c[i].font_size = 55
            eq2_vec_c[i].next_to(eq1_cosine_law_1, DOWN, aligned_edge=LEFT)

        # eq.3 点乘定义, 两个相同向量点乘等于模长平方的式子
        eq3_dot_product_1 = MathTex(
            r"\because \vec{a} \cdot \vec{b} = a_x b_x + a_y b_y",
            font_size = 40
        ).next_to(eq2_vec_c[0], DOWN, aligned_edge=LEFT)

        eq3_dot_product_2 = MathTex(
            r"\therefore \vec{a} \cdot \vec{a} = a_x^2 + a_y^2 = |\vec{a}|^2",
            tex_to_color_map = {r"\vec{a}": RED, r"a_x": RED, r"a_y": RED},
            font_size = 40
        ).next_to(eq3_dot_product_1, DOWN, aligned_edge=LEFT)

        eq3_dot_product_3 = Tex(
            r"(also applies to B and C)",
            font_size = 40,
            tex_to_color_map = {r"B": GREEN, r"C": YELLOW}
        ).next_to(eq3_dot_product_2, DOWN, aligned_edge=LEFT)

        eq3_dot_product_4 = Tex(
            r"(obtain the EQUATION from DIFFERENTS)",
            font_size = 25,
            tex_to_color_map = {r"EQUATION": BLUE, r"DIFFERENTS": BLUE}
        ).next_to(eq3_dot_product_3, DOWN, aligned_edge=LEFT)

        # 动画序列 1.2

        self.play(Write(eq1_cosine_law_1), run_time = 0.5)
        self.play(GrowArrow(vec_c), Write(vec_c_label), run_time = 0.7)
        self.wait(5)

        self.play(Transform(eq1_cosine_law_1, eq1_cosine_law_2), run_time = 1.5)
        self.wait(5)

        self.play(Write(eq2_vec_c[0]), run_time = 1.5)
        self.wait()
        self.play(Transform(eq2_vec_c[0], eq2_vec_c[1]), run_time = 1.5)

        self.wait(2)
        self.play(Transform(eq2_vec_c[0], eq2_vec_c[2]), run_time = 1.5)

        self.wait(2)
        self.play(Transform(eq2_vec_c[0], eq2_vec_c[3]), run_time = 1.5)

        self.wait(6)

        self.play(
            Write(eq3_dot_product_1),
            Write(eq3_dot_product_2),
            Write(eq3_dot_product_3),
            Write(eq3_dot_product_4), run_time = 1.5
        )

        self.wait(5)

        # 20sec self.wait(20)

        '''
            S1 SECTION 3
            Application : Orthogonality & Solving Equations
        ''' 

        axes = ThreeDAxes(
            x_range=[-5, 5, 1],  # x轴范围
            y_range=[-5, 5, 1],  # y轴范围
            z_range=[-4, 4, 1],  # z轴范围
            axis_config={
                "stroke_color": BLUE,
                "stroke_width": 2,
            }
        )

        # Fade out all mobjects and create 3D axes
        self.play(
            *[FadeOut(*self.mobjects)],
            Create(axes), run_time = 1
        )

        # A 3D Vector and plane perpendicular to it
        vec3 = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(1, 1, 1),
            color=RED,
            thickness=0.01,
        )
        
        plane = Polygon(
            axes.c2p(2.115,0.701,0.184),
            axes.c2p(0.701,2.115,0.184),
            axes.c2p(-0.115,1.299,1.816),
            axes.c2p(1.299,-0.115,1.816),
            color=BLUE,
            fill_opacity=0.3,
            stroke_width=2,
        )

        plane_label = Tex("Orthogonality", font_size = 40).to_corner(UL)
        vec3_label = MathTex(r"\vec{v} = (1, 1, 1)", font_size = 40).next_to(plane_label, DOWN, aligned_edge=LEFT)
        eq4_linearEQ_1 = MathTex(r"x + y + z = 0", font_size = 40).next_to(vec3_label, DOWN, aligned_edge=LEFT)
        eq4_linearEQ_2 = MathTex(r"\begin{bmatrix} x\\ y\\ z\end{bmatrix}\begin{bmatrix}1\\ 1\\ 1\end{bmatrix}=0", font_size = 40).next_to(eq4_linearEQ_1, DOWN, aligned_edge=LEFT)

        # Move Camera to a better angle
        self.move_camera(
            phi=75 * DEGREES,
            theta=-45 * DEGREES,
            run_time = 2,
            rate_func = smooth
        )

        # 动画序列 1.3
        self.play(Create(vec3), Create(plane), run_time = 2)

        self.add_fixed_in_frame_mobjects(plane_label, vec3_label, eq4_linearEQ_1, eq4_linearEQ_2)
        self.play(Write(plane_label), Write(vec3_label), Write(eq4_linearEQ_1), Write(eq4_linearEQ_2))

        # Move camera around the scene
        self.begin_3dillusion_camera_rotation()
        self.wait(10) # 15sec
        self.stop_3dillusion_camera_rotation()



# 1080p60: manim -pqh main.py DotProduct
# 1080p60 OPENGL: manim -pqh --renderer opengl main.py DotProduct