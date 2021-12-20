# -*- coding: utf-8 -*-
"""
A python visualisation of ball collisions, using the turtle module.


buggy on some machines - every second iteration ends in the screen not responding 
fix by closing the unresponsive window, and running the code again.
"""

import turtle
import numpy as np
import random

sim = turtle.Screen()
sim.bgcolor("black")
sim.title("Collision Visualizer")
sim.tracer(0)
        
balls = []

for i in range(6):
    balls.append(turtle.Turtle())

for i, ball in enumerate(balls):
    #Setting up the objects
    ball.shape("circle")
    ball.color(['yellow', 'blue', 'white', 'purple', 'green', 'red'][i])
    ball.penup()
    
    #Generating random positions
    
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)    

    #Generating random velocities:
    
    ball.dx = random.uniform(-0.5, 0.5)
    ball.dy = random.uniform(-0.5, 0.5) 
    
    #Generating random radius (base is 20):
    
    ratio = random.uniform(1, 5)
    ball.shapesize(ratio, ratio, 1)
        
    ball.speed(5)
    ball.goto(x, y)

#run the simulation
while True:
    
    sim.update()             
    
    for ball in balls:
        #move balls according to their velocities
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)
        
        #check for wall collisions (perfectly elastic collisions)
        if ball.xcor() > 300:
            ball.dx *= -1
            
        if ball.xcor() < -300:
            ball.dx *= -1
            
        if ball.ycor() > 300:
            ball.dy *= -1
            
        if ball.ycor() < -300:
            ball.dy *= -1
            
            
        #check for collisions between each other (complexity n^2):
        
    for i, value in enumerate(balls):
        for j in range(i+1, len(balls)):
            #calculate radius of collision:
            ball_1 = balls[i]
            ball_2 = balls[j]
            
            dist = ball_1.shapesize()[0] * 10 + ball_2.shapesize()[0] * 10
            
            #collision occurs:
            if ball_1.distance(ball_2) <= dist:
                #Math for 2d elastic collisions, also taking in account masses.
                v1 = np.array((ball_1.dx, ball_1.dy))
                v2 = np.array((ball_2.dx, ball_2.dy))
                
                r1 = np.array((ball_1.xcor(), ball_1.ycor()))
                r2 = np.array((ball_2.xcor(), ball_2.ycor()))

                
                rad1 = ball_1.shapesize()[0]
                rad2 = ball_2.shapesize()[0]
                
                m1, m2 = rad1**2, rad2**2
                M = m1+m2
                
                d = np.linalg.norm(r1-r2)**2
                
                u1 = v1 - 2*m2 / M * np.dot(v1-v2, r1-r2) / d * (r1 - r2)
                u2 = v2 - 2*m1 / M * np.dot(v2-v1, r2-r1) / d * (r2 - r1)
                
                ball_1.dx, ball_1.dy = u1[0], u1[1]
                ball_2.dx, ball_2.dy = u2[0], u2[1]
                
    
                    
                    
            
turtle.done()
    

