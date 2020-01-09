import hmac
import base64
import json
import hashlib

from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

ARTICLE_SECRET = b'l`IceCm?<$9R}<tiEdcB}DH~BX6YRFb[pVHro5GLCZTCtUFC4zCFIad2[1{rlc}&'
ARTICLE_DIGEST_TYPE = 'sha256'

# also available at `thorn.utils.hmac.verify`
def verify(hmac_header, digest_method, secret, message):
    digestmod = getattr(hashlib, digest_method)
    signed = base64.b64encode(
        hmac.new(secret, message, digestmod).digest(),
    )
    return hmac.compare_digest(signed, hmac_header.encode('utf-8'))

@require_POST
@csrf_exempt
def on_task_finished(request):
    digest = request.META.get('HTTP_HOOK_HMAC')
    if not digest:
        return HttpResponse(status=403)
    body = request.body
    if verify(digest, ARTICLE_DIGEST_TYPE, ARTICLE_SECRET, body):
        payload = json.loads(body)
        print('task finished: {}'.format(payload))
        return HttpResponse(status=200)
    return HttpResponse(status=403)