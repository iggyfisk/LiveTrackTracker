''' Parse complicated input data '''
from email import message_from_bytes
from re import compile as re_compile

urlsearch = re_compile('"(http.*livetrack\.garmin\.com[a-zA-Z0-9\/-]*)"')

def get_livetrack_urls(email_data):
    ''' Search for and return livetrack urls from a livetrack notification email '''
    message = message_from_bytes(email_data)
    body = ''
    if message.is_multipart():
        for part in message.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('Content-Disposition'))

            # skip any text/plain (txt) attachments
            if ctype == 'text/plain' and 'attachment' not in cdispo:
                body = part.get_payload(decode=True)  # decode
                break
    # not multipart - i.e. plain text, no attachments, keeping fingers crossed
    else:
        body = message.get_payload(decode=True)

    if isinstance(body, (bytes, bytearray)):
        body = body.decode('UTF8')

    urls = []
    url_matches = urlsearch.search(body)
    if url_matches:
        for url in url_matches.groups():
            urls.append(url)

    return urls
