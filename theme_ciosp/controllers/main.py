# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)

from odoo.addons.website.controllers import main

class Website(http.Controller):

    @http.route('/', type='http', auth="public", website=True, sitemap=True)
    def index(self, **kw):
        return request.redirect('/index')

main.Website.index = Website.index