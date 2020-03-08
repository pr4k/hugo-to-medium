import os
import sys

from medium import Client

ENV = os.environ
def postToMedium(heading,body):
    client = Client(application_id = ENV["APP_ID"],application_secret = ENV["APP_SECRET"])

    client.access_token = ENV["ACCESS_TOKEN"]

    user = client.get_current_user()

    post = client.create_post(user_id = user["id"], title = heading, content = body, content_format = "markdown", publish_status = "draft")

    print("New!! post at ",post["url"])

commit_msg = " ".join(sys.argv[1:])
blog_path = os.path.join(ENV["GITHUB_WORKSPACE"],ENV["BLOG_DIR"])
blog_dir = os.listdir(blog_path)
if "PUBLISH" in commit_msg.upper():
    post_name = commit_msg.upper().split("PUBLISH")[1].strip()[:-1]
    for i in blog_dir:
        if post_name == i.upper().strip():
            post_path = os.path.join(blog_path,i)
            body = open(post_path,"r").read()
            postToMedium(i,body)
