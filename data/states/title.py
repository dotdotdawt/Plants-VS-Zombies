"""
Module: title.py
Overview:
    This is currently a placeholder for the Title State of the game.
Imports:
    pygame as pg
    from .. import setup,tools
Classes:
    Title(tools._State):
        Methods:
            __init__(self)
            render_font(self,font,size,msg,color=(255,255,255)
            update(self,Surf,keys,current_time)
            get_event(self,event)
"""
import pygame as pg
from .. import setup,tools

class Title(tools._State):
    """This State is updated while our game shows the title screen."""
    def __init__(self):
        tools._State.__init__(self)
        self.title = self.render_font("Fixedsys500c",40,"Title Screen Place Holder")
        self.title_rect = self.title.get_rect(center=(setup.SCREEN_RECT.centerx,75))
        self.ne_key = self.render_font("Fixedsys500c",20,"[Press Any Key]",(255,255,0))
        self.ne_key_rect = self.ne_key.get_rect(center=(setup.SCREEN_RECT.centerx,500))
        self.blink = False
        self.timer = 0.0

    def render_font(self,font,size,msg,color=(255,255,255)):
        """Takes the name of a loaded font, the size, and the color and returns
        a rendered surface of the msg given."""
        selected_font = pg.font.Font(setup.FONTS[font],size)
        return selected_font.render(msg,1,color)

    def update(self,surface,keys,current_time):
        """Updates the title screen."""
        self.current_time = current_time
        surface.fill((50,50,50))
        surface.blit(self.title,self.title_rect)
        if self.current_time-self.timer > 1000/5.0:
            self.blink = not self.blink
            self.timer = self.current_time
        if self.blink:
            surface.blit(self.ne_key,self.ne_key_rect)

    def get_event(self,event):
        """Get events from Control.  Currently changes to next state on any key
        press."""
        if event.type == pg.KEYDOWN:
            self.next = "MENU"
            self.done = True
