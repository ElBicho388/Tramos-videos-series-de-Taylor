#!/usr/bin/env python
# coding: utf-8

# ### Programación Manim
# Por: Jose Raul Martinez Afanador y Marian Lamar 
# 
# Con la ayuda de: Juan Sebastián Alba Gamboa.
# 
# Con la ayuda de la librería se graficaron los ejemplos expuestos en el video.
# 
# Todo fue programado usando Google Colab.

# In[1]:


#Código para Instalar Manim
get_ipython().system('sudo apt ubdate')
get_ipython().system('sudo apt install libcairo2-dev ffmpeg texlive texlive-latex-extra texlive-fonts-extra texlive-latex-recommended texlive-science tipa libpango1.0-dev')
get_ipython().system('pip install manim ')
get_ipython().system('pip install Ipython --upgrade')


# In[ ]:


#Importamos la librería
from manim import*
import numpy as np


# In[ ]:


#Grafica del Seno

%%manim -qm -v WARNING grafica_func

class grafica_func(Scene):
   def construct(self):
      
      #escena presentación serie del seno
      tex3 = MathTex(r"sin(x)", font_size=160)
      tex3_0 = MathTex(r"sin(x) = \sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{(2n+1)!}", font_size=100)
      self.play(Write(tex3))
      self.wait(2)
      self.play(Transform(tex3,tex3_0))
      self.wait(2)

      #escena 1
      tex4 = MathTex(r"\sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{(2n+1)!}", font_size=60)
      tex4.to_edge(DOWN, buff=1)
      tex4.to_edge(RIGHT, buff=3.5)
      
      ax = Axes(
        x_range=[-4,6,1],
        y_range=[-2,2,1],
        axis_config={"color": GREEN}, x_length=9, y_length=7)

      ax_0 = Axes(
        x_range=[-4,6,1],
        y_range=[-2,2,1],
        axis_config={"color": GREEN}, x_length=15, y_length=15)

      self.play(Transform(tex3,tex4))
      self.play(Create(ax, run_time=1.5))
      self.wait(0.4)
      self.play(Transform(ax, ax_0))
      curva0 = ax.plot(lambda x: np.sin(x), color=RED)
      label_seno = MathTex(r'sin(x)', color=RED, font_size=60)
      label_seno.to_edge(UL, buff=2.7)
      self.play(Create(curva0))
      self.play(Write(label_seno))
      self.wait(2)

      tex6 = MathTex(r"x", font_size=80)
      tex6.to_edge(DOWN, buff=2.7)
      tex6.to_edge(RIGHT, buff=7.2)
      tex7 = MathTex(r"x - \frac{x^{3}}{3!}", font_size=70)
      tex7.to_edge(RIGHT, buff=5.6)
      tex7.to_edge(DOWN, buff=2.1)
      tex8 = MathTex(r"x - \frac{x^{3}}{3!} + \frac{x^{5}}{5!}", font_size=60)
      tex8.to_edge(DOWN, buff=2.1)
      tex8.to_edge(RIGHT, buff=5.0)
      tex9 = MathTex(r"x - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} - \frac{x^{7}}{7!}", font_size=55)
      tex9.to_edge(RIGHT, buff=3.9)
      tex9.to_edge(DOWN, buff=1.9)
      tex10 = MathTex(r"x - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} \\ - \frac{x^{7}}{7!} + \frac{x^{9}}{9!}", font_size=50)
      tex10.to_edge(DOWN, buff=1.3)
      tex10.to_edge(RIGHT, buff=5.1)
      tex11 = MathTex(r"x - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} - \frac{x^{7}}{7!} \\ + \frac{x^{9}}{9!} - \frac{x^{11}}{11!}", font_size=45)
      tex11.to_edge(DOWN, buff=1.4)
      tex11.to_edge(RIGHT, buff=4.6)
      tex12 = MathTex(r"x - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} - \frac{x^{7}}{7!} \\ + \frac{x^{9}}{9!} - \frac{x^{11}}{11!} + \frac{x^{13}}{13!}", font_size=45)
      tex12.to_edge(DOWN, buff=1.4)
      tex12.to_edge(RIGHT, buff=4.2)

      #escena 2 (los demás terminos de la sum)
      curva1 = ax.plot(lambda x: x)
      curva2 = ax.plot(lambda x: x - np.power(x,3)/6)
      curva3 = ax.plot(lambda x: x - np.power(x,3)/6 + np.power(x,5)/np.math.factorial(5))
      curva4 = ax.plot(lambda x: x - np.power(x,3)/6 + np.power(x,5)/np.math.factorial(5) - np.power(x,7)/np.math.factorial(7))
      curva5 = ax.plot(lambda x: x - np.power(x,3)/6 + np.power(x,5)/np.math.factorial(5) - np.power(x,7)/np.math.factorial(7) + np.power(x,9)/np.math.factorial(9))
      curva6 = ax.plot(lambda x: x - np.power(x,3)/6 + np.power(x,5)/np.math.factorial(5) - np.power(x,7)/np.math.factorial(7) + np.power(x,9)/np.math.factorial(9) - np.power(x,11)/np.math.factorial(11))
      curva7 = ax.plot(lambda x: x - np.power(x,3)/6 + np.power(x,5)/np.math.factorial(5) - np.power(x,7)/np.math.factorial(7) + np.power(x,9)/np.math.factorial(9) - np.power(x,11)/np.math.factorial(11) + np.power(x,13)/np.math.factorial(13))

      self.play(Create(curva1, run_time=2),Transform(tex3,tex6))
      self.wait()

      self.play(Transform(curva1,curva2), Transform(tex3,tex7))
      self.wait(0.5)
      self.play(Transform(curva1,curva3), Transform(tex3,tex8))
      self.wait(0.5)
      self.play(Transform(curva1,curva4), Transform(tex3,tex9))
      self.wait(0.5)
      self.play(Transform(curva1,curva5), Transform(tex3,tex10))
      self.wait(0.5)
      self.play(Transform(curva1,curva6), Transform(tex3,tex11))
      self.wait(0.5)
      self.play(Transform(curva1,curva7), Transform(tex3,tex12))
      self.wait()
      self.play(FadeOut(ax, scale=1),
                FadeOut(curva0,scale=1),
                FadeOut(label_seno,scale=1),
                FadeOut(tex3,scale=1),
                FadeOut(curva1,scale=1,run_time=2.4))
      self.wait()


# In[ ]:


#Gráfica euler a la potencia X

%%manim -qm -v WARNING grafica_raul

class grafica_raul(Scene):
   def construct(self):
      
      #escena presentación serie euler a la potencia
      tex3 = MathTex(r"e^{x}", font_size=160)
      tex3_0 = MathTex(r"e^{x} = \sum_{n=0}^\infty \frac{x^{n}}{n!}", font_size=100)
      self.play(Write(tex3))
      self.wait(2)
      self.play(Transform(tex3,tex3_0))
      self.wait(2)

      #escena 1
      tex4 = MathTex(r"\sum_{n=0}^\infty \frac{x^{n}}{n!}", font_size=60)
      tex4.to_edge(DOWN, buff=2)
      tex4.to_edge(RIGHT, buff=3.5)
      
      ax = Axes(
        x_range=[-5,4,1],
        y_range=[-0.5,4,1],
        axis_config={"color": GREEN}, x_length=9, y_length=7)

      self.play(Transform(tex3,tex4))
      self.play(Create(ax, run_time=1.5))
      self.wait(0.4)
      curva0 = ax.plot(lambda x: np.exp(x), color=RED)
      label_seno = MathTex(r'e^{x}', color=RED, font_size=60)
      label_seno.to_edge(UL, buff=4)
      self.play(Create(curva0))
      self.play(Write(label_seno))
      self.wait(2)

      tex6 = MathTex(r"1", font_size=80)
      tex6.to_edge(DOWN, buff=3.2)
      tex6.to_edge(RIGHT, buff=5)
      tex7 = MathTex(r"1 + x", font_size=70)
      tex7.to_edge(RIGHT, buff=4.5)
      tex7.to_edge(DOWN, buff=2.1)
      tex8 = MathTex(r"1 + x + \frac{x^{2}}{2!}", font_size=60)
      tex8.to_edge(DOWN, buff=2.1)
      tex8.to_edge(RIGHT, buff=3.5)
      tex9 = MathTex(r"1 + x + \frac{x^{2}}{2!} + \frac{x^{3}}{3!}", font_size=55)
      tex9.to_edge(RIGHT, buff=2.5)
      tex9.to_edge(DOWN, buff=1.9)
      tex10 = MathTex(r"1 + x + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} + \frac{x^{4}}{4!}", font_size=50)
      tex10.to_edge(DOWN, buff=1.6)
      tex10.to_edge(RIGHT, buff=1.5)
      tex11 = MathTex(r"1 + x + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} \\ + \frac{x^{4}}{4!} + \frac{x^{5}}{5!}", font_size=45)
      tex11.to_edge(DOWN, buff=1.5)
      tex11.to_edge(RIGHT, buff=2.5)
      tex12 = MathTex(r"1 + x + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} \\ + \frac{x^{4}}{4!} + \frac{x^{5}}{5!} + \frac{x^{6}}{6!}", font_size=45)
      tex12.to_edge(DOWN, buff=1.5)
      tex12.to_edge(RIGHT, buff=2.5)
      tex13 = MathTex(r"1 + x + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} \\ + \frac{x^{4}}{4!} + \frac{x^{5}}{5!} + \frac{x^{6}}{6!} + \frac{x^{7}}{7!}", font_size=45)
      tex13.to_edge(DOWN, buff=1.5)
      tex13.to_edge(RIGHT, buff=2.5)

      #escena 2 (los demás terminos de la sum)
      curva1 = ax.plot(lambda x: 1)
      curva2 = ax.plot(lambda x: 1+x)
      curva3 = ax.plot(lambda x: 1 + x + np.power(x,2)/2)
      curva4 = ax.plot(lambda x: 1 + x + np.power(x,2)/2 + np.power(x,3)/6)
      curva5 = ax.plot(lambda x: 1 + x + np.power(x,2)/2 + np.power(x,3)/6 + np.power(x,4)/24)
      curva6 = ax.plot(lambda x: 1 + x + np.power(x,2)/2 + np.power(x,3)/6 + np.power(x,4)/24 + np.power(x,5)/(5*4*3*2))
      curva7 = ax.plot(lambda x: 1 + x + np.power(x,2)/2 + np.power(x,3)/6 + np.power(x,4)/24 + np.power(x,5)/(5*4*3*2) + np.power(x,6)/(6*5*4*3*2))
      curva8 = ax.plot(lambda x: 1 + x + np.power(x,2)/2 + np.power(x,3)/6 + np.power(x,4)/24 + np.power(x,5)/(5*4*3*2) + np.power(x,6)/(6*5*4*3*2) +np.power(x,7)/(7*6*5*4*3*2))

      self.play(Create(curva1, run_time=2),Transform(tex3,tex6))
      self.wait()

      self.play(Transform(curva1,curva2), Transform(tex3,tex7))
      self.wait(0.5)
      self.play(Transform(curva1,curva3), Transform(tex3,tex8))
      self.wait(0.5)
      self.play(Transform(curva1,curva4), Transform(tex3,tex9))
      self.wait(0.5)
      self.play(Transform(curva1,curva5), Transform(tex3,tex10))
      self.wait(0.5)
      self.play(Transform(curva1,curva6), Transform(tex3,tex11))
      self.wait(0.5)
      self.play(Transform(curva1,curva7), Transform(tex3,tex12))
      self.wait(0.6)
      self.play(Transform(curva1,curva8), Transform(tex3,tex13))
      self.wait()
      self.play(FadeOut(ax, scale=1),
                FadeOut(curva0,scale=1),
                FadeOut(label_seno,scale=1),
                FadeOut(tex3,scale=1),
                FadeOut(curva1,scale=1,run_time=2.4))
      self.wait()


# In[ ]:


#Gráfica Ln(x+1)

%%manim -qm -v WARNING grafica_raul2

class grafica_raul2(Scene):
   def construct(self):
      #escena presentación serie del seno
      tex3 = MathTex(r" \ln{(1+x)}", font_size=160)
      tex3_0 = MathTex(r" \ln{(1+x)} = \sum_{n=1}^\infty (-1)^{n+1} \frac{x^{n}}{n}", font_size=100)
      self.play(Write(tex3))
      self.wait(2)
      self.play(Transform(tex3,tex3_0))
      self.wait(2)

      #escena 1
      tex4 = MathTex(r"\sum_{n=0}^\infty \frac{x^{n}}{n!}", font_size=60)
      tex4.to_edge(DOWN, buff=1.8)
      tex4.to_edge(RIGHT, buff=3.5)
      
      ax = Axes(
        x_range=[0.01,5,1],
        y_range=[-0.5,4,1],
        axis_config={"color": GREEN}, x_length=9, y_length=7)

      self.play(Transform(tex3,tex4))
      self.play(Create(ax, run_time=1.5))
      self.wait(0.4)
      curva0 = ax.plot(lambda x: np.log(1+x), color=RED)
      label_seno = MathTex(r'\ln{(1+x)}', color=RED, font_size=60)
      label_seno.to_edge(UL, buff=2.7)
      self.play(Create(curva0))
      self.play(Write(label_seno))
      self.wait(2)
      t_label = ax.get_T_label(x_val=1, graph=curva0, label=Tex("Radio de convergencia"))

      tex6 = MathTex(r"x", font_size=70)
      tex6.to_edge(RIGHT, buff=4.5)
      tex6.to_edge(DOWN, buff=2.1)
      tex7 = MathTex(r"x - \frac{x^{2}}{2}", font_size=60)
      tex7.to_edge(DOWN, buff=2.1)
      tex7.to_edge(RIGHT, buff=3.5)
      tex8 = MathTex(r"x - \frac{x^{2}}{2} + \frac{x^{3}}{3}", font_size=55)
      tex8.to_edge(RIGHT, buff=2.5)
      tex8.to_edge(DOWN, buff=1.9)
      tex9 = MathTex(r"x - \frac{x^{2}}{2} + \frac{x^{3}}{3} - \frac{x^{4}}{4}", font_size=50)
      tex9.to_edge(DOWN, buff=1.6)
      tex9.to_edge(RIGHT, buff=1.5)
      tex10 = MathTex(r"x - \frac{x^{2}}{2} + \frac{x^{3}}{3} \\ - \frac{x^{4}}{4} + \frac{x^{5}}{5}", font_size=45)
      tex10.to_edge(DOWN, buff=1.5)
      tex10.to_edge(RIGHT, buff=2.5)
      tex11 = MathTex(r"x - \frac{x^{2}}{2} + \frac{x^{3}}{3!} \\ - \frac{x^{4}}{4} + \frac{x^{5}}{5} - \frac{x^{6}}{6}", font_size=45)
      tex11.to_edge(DOWN, buff=1.5)
      tex11.to_edge(RIGHT, buff=2.5)
      tex12 = MathTex(r"x - \frac{x^{2}}{2} + \frac{x^{3}}{3!} \\ - \frac{x^{4}}{4} + \frac{x^{5}}{5} - \frac{x^{6}}{6} + \frac{x^{7}}{7}", font_size=45)
      tex12.to_edge(DOWN, buff=1.5)
      tex12.to_edge(RIGHT, buff=2.5)

      #escena 2 (los demás terminos de la sum)
      curva1 = ax.plot(lambda x: x)
      curva2 = ax.plot(lambda x: x - np.power(x,2)/2)
      curva3 = ax.plot(lambda x: x - np.power(x,2)/2 + np.power(x,3)/3)
      curva4 = ax.plot(lambda x: x - np.power(x,2)/2 + np.power(x,3)/3 - np.power(x,4)/4)
      curva5 = ax.plot(lambda x: x - np.power(x,2)/2 + np.power(x,3)/3 - np.power(x,4)/4 + np.power(x,5)/(5))
      curva6 = ax.plot(lambda x: x - np.power(x,2)/2 + np.power(x,3)/3 - np.power(x,4)/4 + np.power(x,5)/(5) - np.power(x,6)/(6))
      curva7 = ax.plot(lambda x: x - np.power(x,2)/2 + np.power(x,3)/3 - np.power(x,4)/4 + np.power(x,5)/(5) - np.power(x,6)/(6) +np.power(x,7)/(7))

      self.play(Create(curva1, run_time=2),Transform(tex3,tex6))
      self.wait()

      self.play(Transform(curva1,curva2), Transform(tex3,tex7))
      self.wait(0.5)
      self.play(Transform(curva1,curva3), Transform(tex3,tex8),Create(t_label))
      self.wait(0.5)
      self.play(Transform(curva1,curva4), Transform(tex3,tex9))
      self.wait(0.5)
      self.play(Transform(curva1,curva5), Transform(tex3,tex10))
      self.wait(0.5)
      self.play(Transform(curva1,curva6), Transform(tex3,tex11))
      self.wait(0.5)
      self.play(Transform(curva1,curva7), Transform(tex3,tex12))
      self.wait(0.6)
      self.play(FadeOut(ax, scale=1),
                FadeOut(curva0,scale=1),
                FadeOut(label_seno,scale=1),
                FadeOut(tex3,scale=1),
                FadeOut(curva1,scale=1,run_time=2.4),
                FadeOut(t_label, shift=DOWN))
      self.wait()

