# Summer2021-Homework-2-Site

2021 夏季学期 - 大作业（二）- 第二部分 - Web 编程

大作业[第一部分](https://github.com/tohlh/Summer2021-Homework-2-Scraper)

## 所使用的工具/技术
Django、PostgreSQL、Vue + Vuetify

## Django Models

使用了以下的 Models:

```python
class Channel(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
    profilePic = models.TextField()
    description = models.TextField()
    joinedDate = models.DateTimeField()
    totalViews = models.BigIntegerField()
    subscriberCount = models.TextField()
    videos =  ArrayField(models.TextField())

class Video(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    videoThumbnail = models.TextField()
    interactionCount = models.BigIntegerField()
    likeCount = models.BigIntegerField()
    dislikecount = models.BigIntegerField()
    uploadDate = models.DateTimeField()
    datePublished = models.DateTimeField()
    channelID = models.TextField()
    genre = models.TextField()
    comments = ArrayField(models.TextField())
```

`Channel` 和 `Video` 分别对应了爬取资料中的 `channels` 和 `videos`

## URLs

使用了以下的URL。所有的URL均可直接访问，除了 `search-videos` 和 `search-channels`。这两个URL负责显示搜索结果，必须通过 `POST` 访问。直接访问会重定向到视频或作者列表页。

```python
path('admin/', admin.site.urls),
path('', mySite_views.index),
path('page<int:page>/', mySite_views.index),
path('channels/', mySite_views.channels),
path('channel/page<int:page>', mySite_views.channels),
path('video/<str:id>', mySite_views.video_details),
path('channel/<str:id>', mySite_views.channel_details),
path('search-videos', mySite_views.search_videos_result),
path('search-videos/page<int:page>', mySite_views.search_videos_result),
path('search-channels', mySite_views.search_channels_result),
path('search-channels/page<int:page>', mySite_views.search_channels_result),search_channels_result),
```

## 前端

前端使用了 Vue 框架以及用 Vuetify 美化。每一个 template 都为一个 Vue app ，有着自己使用的一些部件（Components）。Statics 中的 `components.js` 则有着公用的部件，其中包括：

1. `toolbar`：网页最上端的栏，当中能选择跳转至视频或作者列表页，也能搜索视频或作者。
2. `page-footer`：网页页脚
3. `video-card`：视频列表页里每个视频的条目
4. `channel-card`：作者列表页里每个作者的条目

## Toolbar
`toolbar` 最重要的功能在于搜索视频/频道。当用户搜索时，前端的 `Form` 会 `POST` 到 `search-videos` 或 `search-channels` 的 URL，后端会获取名为 `searched` 的变量值，并从数据库中搜索。

由于此过程需要前端有 `csrf_token`, 然后 `toolbar` 处于 `statics` 内，因此在 `toolbar` 中使用了 `<slot>` 获取 `csrf_token`:

```html
<slot name="token"></slot>
```

## `video-card`

`video-card` 接受4个 `props`：
```JavaScript
props: ['id', 'thumbnail', 'title', 'views'],
```
在各页面使用 `video-card` 时只需要传入以上数据：

```html
<video-card
    id="{{ video.id|safe }}"
    thumbnail="{{ video.videoThumbnail|safe }}"
    title="{{ video.title }}"
    views="{{ video.interactionCount | intcomma }}"
></video-card>
```

## `channel-card`

`channel-card` 接受4个 `props`：
```JavaScript
props: ['id', 'profilepic', 'name', 'subscribercount'],
```
在各页面使用 `channel-card` 时只需要传入以上数据：
```html
<channel-card
    id="{{ channel.id }}"
    profilepic="{{ channel.profilePic }}"
    name="{{ channel.name }}"
    subscribercount="{{ channel.subscriberCount | intcomma }}"
></channel-card>
```
## 分页

分页使用了 Vuetify 内置的 `<v-pagination>` 实现，用户在点击页面时会调用 `paginate()` 函数跳转至指定的页面。旁边的输入页码栏则在用户按回车键的时候调用 `paginateFromField()` 函数跳转至指定的页面。

在视频和作者列表页中，以上的动作十分简单，只需要直接跳转至该页面的URL即可。在搜索页时，由于牵涉到 `POST` 以及 `csrf_token`，`paginate()` 和 `paginateFromField()` 会使用隐形的 `form` 并 `POST` 搜索字眼到指定页的 URL。
