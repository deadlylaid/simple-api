import falcon

import msgpack


class Resource:
    def on_get(self, req, resp):
        doc = {
                'images':[
                    {
                        'herf':'images/lemon.png'
                        }
                    ]
                }

        resp.data = msgpack.packb(doc, use_bin_type=True)
        resp.content = falcon.MEDIA_MSGPACK
        resp.status = falcon.HTTP_200
