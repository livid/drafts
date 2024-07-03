# Planet API Server

Planet includes an API server, which you can enable from the Settings.

Authentication is optional, as most usage is local or within your LAN. However, you can set a username and password if desired.

By default, the API server listens on port 8086.

Here are all the methods it supports:

## GET /v0/planets/my

http://127.0.0.1:8086/v0/planets/my

List all sites.

## GET /v0/planets/my/:planet_id

Get info of a specific site.

## POST /v0/planets/my/:planet_id

Modify a site. These fields can be modified via POST request:

- name
- about

cURL example:

Change a site name to `example`:

```
curl -v -F name=example http://127.0.0.1:8086/v0/planets/my/EB9579B2-6654-4EC2-A972-822DA871020B
```

## POST /v0/planets/my/:planet_id/publish

Manually triggers a publish action.

## GET /v0/planets/my/:planet_id/public

Preview a site. This URL can be opened in browser to see build result of a site.

## GET /v0/planets/my/:planet_id/articles

List all posts under a site.

## POST /v0/planets/my/:planet_id/articles

Create a new post.

cURL example to create a post with a picture attachment.

```
curl -X POST http://127.0.0.1:8086/v0/planets/my/999BB908-B79A-4C89-8DA6-1339BDFCE03E/articles \
  -F "attachment=@example.jpeg" \
  -F "title=title" \
  -F "content=content"
```

Known issue: You cannot set the post creation date and time in versions 0.17 and below. This feature will be available in version 0.18.2 and later.

## GET /v0/planets/my/:planet_id/articles/:article_id

Get info of a specific post.

## POST /v0/planets/my/:planet_id/articles/:article_id

Modify a post.

Known issue: As of version 0.17, modifying a post via API requires re-providing all fields, including the title, content, and attachment. If any field is omitted, it will be emptied. In future versions, only the fields provided will be modified.

cURL example:

```
curl -v -F title="New Title" -F content="New Content" -F "attachment=@example.jpeg" http://127.0.0.1:8086/v0/planets/my/999BB908-B79A-4C89-8DA6-1339BDFCE03E/articles/C57804D9-01DE-420E-8ACF-C35B9A4358CE
```

## DELETE /v0/planets/my/:planet_id/articles/:article_id

Delete a post.

---

This documentation will be updated as the API evolves. If you encounter any issues, please let us know by opening a new issue [here](https://github.com/Planetable/Planet). The source code of the API server can be found in this file:

https://github.com/Planetable/Planet/blob/main/Planet/PlanetAPI.swift