# Serve static and media from the CDN
# CDN(Content Distribution Network) is the service which copies the files across different part of the globe. Later, whenever file is accesses, it is
# getting served from the nearby CDN server location from the client.
# File serving needs good amount of bandwidth from servers and CDN network has petabyte scale bandwidth available with them.
# There are multiple CDN services available. Examples are Amazon Cloudfront, Google CDN, Cloudflare CDN, Azure CDN etc.


# Use S3 or Storage to store the media files and later use CDNs to serve them.
# Use the AWS S3, Google cloud storage, Azure file storage etc services to store the media files.
# Above services copies the data across multiple data centers, almost unlimited bandwidth to serve the files and have high uptime.
# If from the beginning of the project such decision has been taken then whenever django app is moved to distributed architecture setup, can be done without almost no efforts on storage side.
