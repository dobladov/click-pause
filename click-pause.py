# -*- coding: utf-8 -*-

from gi.repository import GObject, Peas

class StarterPlugin (GObject.Object, Peas.Activatable):
    __gtype_name__ = 'ClickPause'

    object = GObject.property (type = GObject.Object)


    def do_deactivate (self):
        self._totem = None
        print("Click Pause disabled")


    def do_activate (self):
        self._totem = self.object
        
        video = self.object.get_video_widget()
        video.connect("button_press_event", self.toggle_pause)
        print("Click Pause enabled")


    def toggle_pause(self, widget, event):
        if (event.button == 3 ):
            self._totem.play_pause()
            print('Play' if self._totem.is_playing() else 'Pause')