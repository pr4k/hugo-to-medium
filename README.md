# hugo-to-medium

[![GitHub issues](https://img.shields.io/github/issues/pr4k/hugo-to-medium)](https://github.com/pr4k/hugo-to-medium/issues)
[![GitHub forks](https://img.shields.io/github/forks/pr4k/hugo-to-medium)](https://github.com/pr4k/hugo-to-medium/network)
[![GitHub stars](https://img.shields.io/github/stars/pr4k/hugo-to-medium)](https://github.com/pr4k/hugo-to-medium/stargazers)
[![GitHub license](https://img.shields.io/github/license/pr4k/hugo-to-medium)](https://github.com/pr4k/hugo-to-medium)


Github action to directly post from hugo to medium.
This is created for those who are always importing their own hugo blog to medium.It uses Medium's API to directly upload the post from hugo to medium

## Usage

It uses commit message to identify which post to publish on medium.
Simply while making a commit include at last `PUBLISH <Your-post-name>.md`

### Example:
`git commit -m "Added: post PUBLISH: my-arch-setup.md`

## Creating main.yml

A sample `main.yml` can be
```bash
on: [push]

jobs:
  hugo_to_medium_job:
    runs-on: ubuntu-latest
    name: hugo-to-medium
    steps:
      # To use this repository's private action, you must check out the repository
      - uses: actions/checkout@v2
        with:
          ref: master
      - name: Hugo To medium Action step 
        uses: pr4k/Hugo-to-Medium@master # Uses an action in the root directory
        id: hello
        env:
          APP_ID: ${{secrets.APP_ID}}
          ACCESS_TOKEN: ${{secrets.ACCESS_TOKEN}}
          APP_SECRET: ${{secrets.APP_SECRET}}
          BLOG_DIR: ${{secrets.BLOG_DIR}}
      #
```
paste this to `.github/workflow/main.yml` 

`APP_ID`: This is your medium Developer APP id , Go to [Medium Applications](https://medium.com/me/applications)
`ACCESS_TOKEN` : This can be generated from [Settings page](https://medium.com/me/settings)
`APP_SECRET`: This is your medium Developer APP Secret , Go to [Medium Applications](https://medium.com/me/applications)

Set these as your environment variable, and done

