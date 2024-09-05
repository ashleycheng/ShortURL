ShortURL-API document
==
### API 1: Create Short URL
#### `POST` **/api/short_url**
##### Required parameter
- original_url (type: string; URL format, its length should not exceed 2048)

#### Example 1:
If the original_url is valid, it would create a short url successfully and get the **status code 201**.
##### Payload
```json=
{
  "original_url": "https://ec.ltn.com.tw/article/breakingnews/4789741"
}
```
##### Return
```json=
{
  "short_url": "http://localhost:8000/HOVtlDrO",
  "expiration_date": "2024-10-05",
  "success": true,
  "reason": null
}
```
#### Example 2:
If the length of original_url exceed 2048, it would get the **status code 400** .
##### Payload
```json=
{
  "original_url": "https://www.microsoft.com/onerfstatics/marketingsites-eas-prod/chinese-traditional/shell/_scrf/css/themes=default.device=uplevel_web_pc_webkit_chrome/1b-9d8ed9/c9-be0100/a6-e969ef/43-9f2e7c/82-8b5456/a0-5d3913/43-5a5ab8/ca-ae3ce4?ver=2.0&_cf=02242021_3231/css/themes=default.device=uplevel_web_pc_webkit_chrome/1b-9d8ed9/c9-be0100/a6-e969ef/43-9f2e7c/82-8b5456/a0-5d3913/43-5a5ab8/ca-ae3ce4?ver=2.0&_cf=02242021_3231/css/themes=default.device=uplevel_web_pc_webkit_chrome/1b-9d8ed9/c9-be0100/a6-e969ef/43-9f2e7c/82-8b5456/a0-5d3913/43-5a5ab8/ca-ae3ce4?ver=2.0&_cf=02242021_3231/css/themes=default.device=uplevel_web_pc_webkit_chrome/1b-9d8ed9/c9-be0100/a6-e969ef/43-9f2e7c/82-8b5456/a0-5d3913/43-5a5ab8/ca-ae3ce4?ver=2.0&_cf=02242021_3231/css/themes=default.device=uplevel_web_pc_webkit_chrome/1b-9d8ed9/c9-be0100/a6-e969ef/43-9f2e7c/82-8b5456/a0-5d3913/43-5a5ab8/ca-ae3ce4?ver=2.0&_cf=02242021_3231/css/themes=default.device=uplevel_web_pc_webkit_chrome/1b-9d8ed9/c9-be0100/a6-e969ef/43-9f2e7c/82-8b5456/a0-5d3913/43-5a5ab8/ca-ae3ce4?ver=2.0&_cf=02242021_3231/css/themes=default.device=uplevel_web_pc_webkit_chrome/1b-9d8ed9/c9-be0100/a6-e969ef/43-9f2e7c/82-8b5456/a0-5d3913/43-5a5ab8/ca-ae3ce4?ver=2.0&_cf=02242021_3231/css/themes=default.device=uplevel_web_pc_webkit_chrome/1b-9d8ed9/c9-be0100/a6-e969ef/43-9f2e7c/82-8b5456/a0-5d3913/43-5a5ab8/ca-ae3ce4?ver=2.0&_cf=02242021_3231/css/themes=default.device=uplevel_web_pc_webkit_chrome/1b-9d8ed9/c9-be0100/a6-e969ef/43-9f2e7c/82-8b5456/a0-5d3913/43-5a5ab8/ca-ae3ce4?ver=2.0&_cf=02242021_3231/css/themes=default.device=uplevel_web_pc_webkit_chrome/1b-9d8ed9/c9-be0100/a6-e969ef/43-9f2e7c/82-8b5456/a0-5d3913/43-5a5ab8/ca-ae3ce4?ver=2.0&_cf=02242021_3231/css/themes=default.device=uplevel_web_pc_webkit_chrome/1b-9d8ed9/c9-be0100/a6-e969ef/43-9f2e7c/82-8b5456/a0-5d3913/43-5a5ab8/ca-ae3ce4?ver=2.0&_cf=02242021_3231/css/themes=default.device=uplevel_web_pc_webkit_chrome/1b-9d8ed9/c9-be0100/a6-e969ef/43-9f2e7c/82-8b5456/a0-5d3913/43-5a5ab8/ca-ae3ce4?ver=2.0&_cf=02242021_3231/css/themes=default.device=uplevel_web_pc_webkit_chrome/1b-9d8ed9/c9-be0100/a6-e969ef/43-9f2e7c/82-8b5456/a0-5d3913/43-5a5ab8/ca-ae3ce4?ver=2.0&_cf=02242021_323143-5a5ab8/ca-ae3ce4?ver=2.0&_cf=02242021_3231/css/themes=default.device=uplevel_web_pc_webkit_chrome/1b-9d8ed9/c9-be0100/a6-e969ef/43-9f2e7c/82-8b5456/a0-5d3913/43-5a5ab8/ca-ae3ce4?ver=2.0&_cf=02242021_3231/css/themes=default.device=uplevel_web_pc_webkit_chrome/1b-9d8ed9/c9-be0100/a6-e969ef/43-9f2e7c/82-8b5456/a0-5d3913/43-5a5ab8/ca-ae3ce4?ver=2.0&_cf=02242021_3231/css/themes=default.device=uplevel_web_pc_webkit_chrome/1b-9d8ed9/c9-be0100/a6-e969ef/43-9f2e7c/82-8b5456/a0-5d3913/43-5a5ab8/ca-ae3ce4?ver=2.0&_cf=02242021_3231"
}
```
##### Return
```json=
{
  "short_url": null,
  "expiration_date": null,
  "success": false,
  "reason": "The original_url is too long.Enter a valid URL."
}
```
#### Example 3:
If the original_url doesn't match URL pattern, it would get the **status code 400** .
##### Payload
```json=
{
  "original_url": "jshjhfjsdjhfjs"
}
```
##### Return
```json=
{
  "short_url": null,
  "expiration_date": null,
  "success": false,
  "reason": "Enter a valid URL."
}
```

### API 2: Redirect Using Short URL
#### `GET` **/{shortURLstr}**
> shortURLstr is a unique string used to make a short URL, which can map to the original URL.
#### Example 1:
If the shortURLstr is valid, it would redirect to the original url and get the **status code 302**.
##### Command
```bash=
curl http://localhost:8000/2KY5XM6f -I
```
##### Return
<img width="889" alt="image" src="https://github.com/user-attachments/assets/b402990d-e4ff-4a11-a32f-9e0014075bc2">

#### Example 2:
If the shortURLstr doesn't exist, it would get the **status code 404**.
##### Command
```bash=
curl http://0.0.0.0:8000/HOVtlD -I
```
##### Return
<img width="383" alt="image" src="https://github.com/user-attachments/assets/72b6c9b3-032b-4198-82b0-09b71859f8b6">

User guide - Docker
==
1. Pull the docker image from [docker hub](https://hub.docker.com/r/cscashley/shorturl-api-django):

```docker image pull cscashley/shorturl-api-django:v1.0.0```

2. Run the image in the local environment, using port 8000:

```docker run --name django-app -p 8000:8000 -d cscashley/shorturl-api-django:v1.0.0```

3. Then the Django service will run on localhost http://0.0.0.0:8000, and api could be tested on http://0.0.0.0:8000/docs/.
