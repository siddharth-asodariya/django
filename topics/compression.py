#  In every web request we get the http request and later we respond with that http request with raw text response. - If
# response is little bigger then response should be gziped to compress the response size, which can lead to lesser bandwidth
# and response time for the client.
# Django has built in support for gziping the response.
# Compress the responses greather than couple of kb.

 django.middleware.gzip.GZipMiddleware

#  This middleware should be placed before any other middleware that need to read or write the response body so that
# compression happens afterward.

# It will NOT compress content if any of the following are true:

# The content body is less than 200 bytes long.
# The response has already set the Content-Encoding header.
# The request (the browser) hasn’t sent an Accept-Encoding header containing gzip.
# If the response has an ETag header, the ETag is made weak to comply with RFC 7232#section-2.1.

# You can apply GZip compression to individual views using the gzip_page() decorator
