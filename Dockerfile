FROM python:3.7.2-alpine3.9
RUN apk add --no-cache \
    jq \
    curl \
    git \
    python
RUN apk add --no-cache python3-dev libstdc++ && \
    apk add --no-cache g++ && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    pip3 install medium 
ADD entrypoint.sh /
ADD post.py /
RUN chmod +x /post.py
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
