import tkinter as tk
import numpy as np
import time


class Drawing:
    def __init__(self, dim, title='Drawing', canvas_color='white'):
        width, height = dim
        self.width = width
        self.height = height
        self.title = title
        self.canvas_color = canvas_color

        self.origin = (0, 0)
        self.push_origin = []
        self.theta = 0
        self.push_theta = []

        self.root = tk.Tk()
        self.root.resizable(0, 0)
        self.root.title(self.title)

        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg=self.canvas_color)
        self.canvas.pack()

    def draw(self, draw_function=None):
        run = True
        while run:
            try:
                self.clear_canvas()
                if draw_function is not None:
                    self.push()
                    draw_function()
                    self.pop()
                self.root.update()
            except tk.TclError:
                run = False
            time.sleep(0.1)

    def clear_canvas(self):
        self.canvas.destroy()
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg=self.canvas_color)
        self.canvas.pack()

    def draw_circle(self, pos, r, color='black', fill=None, line_width=1):
        origin_x, origin_y = self.origin
        pos_vector = np.array(pos).transpose()
        r_matrix = np.array([[np.cos(self.theta), -np.sin(self.theta)],
                             [np.sin(self.theta), np.cos(self.theta)]])
        new_pos_vector = r_matrix.dot(pos_vector)
        tr_x = new_pos_vector[0] + origin_x
        tr_y = new_pos_vector[1] + origin_y
        self.canvas.create_oval(tr_x-r, tr_y-r, tr_x+r, tr_y+r, outline=color, fill=fill, width=line_width)

    def draw_line(self, start_pos, end_pos, color='black', line_width=1):
        origin_x, origin_y = self.origin
        start_pos_vector = np.array(start_pos).transpose()
        end_pos_vector = np.array(end_pos).transpose()
        r_matrix = np.array([[np.cos(self.theta), -np.sin(self.theta)],
                             [np.sin(self.theta), np.cos(self.theta)]])
        new_start_pos_vector = r_matrix.dot(start_pos_vector)
        new_end_pos_vector = r_matrix.dot(end_pos_vector)
        tr_sx = new_start_pos_vector[0] + origin_x
        tr_sy = new_start_pos_vector[1] + origin_y
        tr_ex = new_end_pos_vector[0] + origin_x
        tr_ey = new_end_pos_vector[1] + origin_y
        self.canvas.create_line(tr_sx, tr_sy, tr_ex, tr_ey, fill=color, width=line_width)

    def draw_rect(self, pos, size, color='black', fill=None, line_width=1):
        origin_x, origin_y = self.origin
        x, y = pos
        width, height = size
        v1 = np.array([x, y]).transpose()
        v2 = np.array([x + width, y]).transpose()
        v3 = np.array([x + width, y + height]).transpose()
        v4 = np.array([x, y + height]).transpose()
        r_matrix = np.array([[np.cos(self.theta), -np.sin(self.theta)],
                             [np.sin(self.theta), np.cos(self.theta)]])
        new_v1 = r_matrix.dot(v1)
        new_v2 = r_matrix.dot(v2)
        new_v3 = r_matrix.dot(v3)
        new_v4 = r_matrix.dot(v4)
        tr_v1x = new_v1[0] + origin_x
        tr_v1y = new_v1[1] + origin_y
        tr_v2x = new_v2[0] + origin_x
        tr_v2y = new_v2[1] + origin_y
        tr_v3x = new_v3[0] + origin_x
        tr_v3y = new_v3[1] + origin_y
        tr_v4x = new_v4[0] + origin_x
        tr_v4y = new_v4[1] + origin_y
        self.canvas.create_polygon(tr_v1x, tr_v1y, tr_v2x, tr_v2y, tr_v3x, tr_v3y, tr_v4x, tr_v4y,
                                   outline=color, fill=fill, width=line_width)

    def translate(self, new_origin):
        origin_x, origin_y = self.origin
        pos_vector = np.array(new_origin)
        r_matrix = np.array([[np.cos(self.theta), -np.sin(self.theta)],
                             [np.sin(self.theta), np.cos(self.theta)]])
        new_pos_vector = np.dot(r_matrix, pos_vector)
        r_x = new_pos_vector[0]
        r_y = new_pos_vector[1]
        tr_x = r_x + origin_x
        tr_y = r_y + origin_y
        self.origin = (tr_x, tr_y)

    def rotate(self, theta):
        self.theta = self.theta + theta

    def push(self):
        self.push_origin.append(self.origin)
        self.push_theta.append(self.theta)

    def pop(self):
        if not self.push_origin == []:
            self.origin = self.push_origin.pop(-1)
        if not self.push_theta == []:
            self.theta = self.push_theta.pop(-1)
