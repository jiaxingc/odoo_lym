# -*- coding: utf-8 -*-

# from odoo import models, fields, api

# import logging
# _logger = logging.getLogger(__name__)

# class LymIndex(models.TransientModel):
#     _name = "theme_ciosp.index"
#     _description = "Index"

    # def get_event(self, website):
    #     event = self.env["event.event"]
    #     palestras_on = list()
        
    #         event = website.event_id
    #         palestras_on = self.env["lym_programacao.programacao"].get_palestras_on(website)
    #     return {
    #         "event": event,
    #         "palestras": palestras_on
    #     }
        # if website.event_id:
        #     event = website.event_id
        #     palestras_on = self.env["lym_programacao.programacao"].get_palestras_on(website)
        # return {
        #     "event": event,
        #     "palestras": palestras_on
        # }