#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from caesar import encrypt
import cgi

# html_head = """
#     <!DOCTYPE html>
#     <html>
#         <head>
#             <title>Caesar</title>
#         </head>
#         <body>
# """

form = """
    <form method="post">
        <label>
            <strong>Enter some text to ROT13:</strong>
            <br />
            <textarea autofocus required rows="10" cols="80" name="rot_textarea">%(rot_text)s</textarea>
        </label>
        <br />
        <input type="submit" />
    </form>
"""

# html_close = """
#         </body>
#     </html>
# """

def escape_html(s):
    return cgi.escape(s, quote = True)


class MainHandler(webapp2.RequestHandler):
    
    def write_form(self, rot_text=""):
        self.response.out.write(form % {"rot_text": escape_html(rot_text)})
    
    def get(self):
        self.write_form()

    def post(self):
        rot_text = self.request.get("rot_textarea")
        self.write_form(encrypt(rot_text, 13))
    

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
