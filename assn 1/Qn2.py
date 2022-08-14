# A program to draw the olympic rings
#
# @author 
# @assignment CSCI 333 Assignment 1
# @date 7/17/2022
#

from ezgraphics import GraphicsWindow

def drawRing(canv, color, diameter, x_pos, y_pos):
    canv.setOutline(color)
    canv.drawOval(x_pos, y_pos, diameter, diameter)


winsize_x = 640
ring_padding = 1
line_width = 15
winsize_y = ((1.5 * winsize_x) / 3) + (ring_padding * 2)

ring_diameter = (winsize_x / 3) - (ring_padding * 2) - line_width
total_space_ring_x = (ring_padding * 2) + line_width + ring_diameter
total_space_ring_y = total_space_ring_x / 2

win = GraphicsWindow(winsize_x, winsize_y)
canvas = win.canvas()
canvas.setLineWidth(line_width)

ring_pos_x = ring_padding + (line_width / 2)
ring_pos_y = ring_pos_x
drawRing(canvas, "blue", ring_diameter, ring_pos_x, ring_pos_y)

ring_pos_x += total_space_ring_x
drawRing(canvas, "black", ring_diameter, ring_pos_x, ring_pos_y)

ring_pos_x += total_space_ring_x
drawRing(canvas, "red", ring_diameter, ring_pos_x, ring_pos_y)

ring_pos_x = (total_space_ring_x / 2) + (line_width / 2) + ring_padding
ring_pos_y += total_space_ring_y
drawRing(canvas, "yellow", ring_diameter, ring_pos_x, ring_pos_y)

ring_pos_x += total_space_ring_x
drawRing(canvas, "green", ring_diameter, ring_pos_x, ring_pos_y)
win.wait()
