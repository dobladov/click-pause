# -*- coding: utf-8 -*-

import logging
from gi.repository import GObject, Peas

class StarterPlugin (GObject.Object, Peas.Activatable):
    __gtype_name__ = 'ClickPause'

    object = GObject.property (type = GObject.Object)
    logger = logging.getLogger('clickPause')
    logger.setLevel(logging.DEBUG)

    def do_deactivate (self):
        self._totem = None
        logging.info("Click Pause disabled")


    def do_activate (self):
        self._totem = self.object
        
        video = self.object.get_video_widget()
        video.connect("button_press_event", self.toggle_pause)
        logging.info("Click Pause enabled")


    def toggle_pause(self, widget, event):
        if (event.button == 3 ):
            self._totem.play_pause()
            logging.info('Play' if self._totem.is_playing() else 'Pause')