#!/bin/sh -l

main(){
    message=$(jq  '.commits[0].message' "$GITHUB_EVENT_PATH")
    python /post.py $message
}
main
