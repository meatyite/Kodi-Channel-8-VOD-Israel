# -*- coding: utf-8 -*-

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

VIDEOS = {'Lod': [{'name': 'Season 1 Episode 1',
                       'thumb': 'https://images1.ynet.co.il/PicServer3/2012/12/31/4367428/72121.jpg_S.jpg',
                       'video': 'http://ynethd-i.akamaihd.net/i/1212/hot/3012121400NQT830974.mp4/master.m3u8',
                       'genre': 'Documentary Series'},
                      {'name': 'Season 1 Episode 2',
                       'thumb': 'https://images1.ynet.co.il/PicServer3/2013/01/01/4370588/72135.jpg_s.jpg',
                       'video': 'http://ynethd-i.akamaihd.net/i/1212/hot/3012121400NQT830975.mp4/master.m3u8',
                       'genre': 'Documentary Series'},
                      {'name': 'Season 1 Episode 3',
                       'thumb': 'https://images1.ynet.co.il/PicServer3/2013/01/03/4375595/72301.jpg_s.jpg',
                       'video': 'http://ynethd-i.akamaihd.net/i/1212/hot/0301131130NQT830976-lod-ep-3.mp4/master.m3u8',
                       'genre': 'Documentary Series'},
                      {'name': 'Season 1 Episode 4',
                       'thumb': 'https://images1.ynet.co.il/PicServer3/2013/01/07/4381637/72402.jpg_s.jpg',
                       'video': 'http://ynethd-i.akamaihd.net/i/1212/hot/0601131500LOD04.mp4/master.m3u8',
                       'genre': 'Documentary Series'},
                      {'name': 'Season 1 Episode 5',
                       'thumb': 'https://images1.ynet.co.il/PicServer3/2013/01/07/4381643/72403.jpg_s.jpg',
                       'video': 'http://ynethd-i.akamaihd.net/i/1212/hot/0601131500LOD05.mp4/master.m3u8',
                       'genre': 'Documentary Series'},
                      {'name': 'Season 1 Episode 6',
                       'thumb': 'https://images1.ynet.co.il/PicServer3/2013/01/10/4391253/72567.jpg_s.jpg',
                       'video': 'http://ynethd-i.akamaihd.net/i/1212/hot/0601131500LOD05.mp4/master.m3u8',
                       'genre': 'Documentary Series'},
                      {'name': 'Season 2 Episode 1',
                       'thumb': 'https://images1.ynet.co.il/PicServer4/2014/12/29/5784595/LOD1_S.jpg',
                       'video': 'http://ynethd-i.akamaihd.net/i/1214/HOT/29121230LOD_2_ep_01.mp4/master.m3u8',
                       'genre': 'Documentary Series'}
                     ],
            'Documentraries': [{'name': 'The Truth Behind Airbnb',
                      'thumb': 'https://images1.ynet.co.il/PicServer5/2017/07/15/7908548/Airbnb_01.jpg',
                      'video': 'https://ynethd-i.akamaihd.net/i/0717/HOT/2407171400AIRBNB_NIGHTMARES.mp4/master.m3u8',
                      'genre': 'Documentary'},
                     {'name': 'The Story Of Nadia Comaneci',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2016/07/24/7155023/NADIA_COMANECI_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0716/HOT/2407161200NADIA_COMANECI.mp4/master.m3u8',
                      'genre': 'Documentary'},
                     {'name': 'The Murder of Jonbenet',
                      'thumb': 'https://images1.ynet.co.il/PicServer5/2017/07/15/7908550/overkill_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0717/HOT/2707171830OVERKIL_%20THE_MURDER_OF_JONBENET.mp4/master.m3u8',
                      'genre': 'Documentary'},
                     {'name': 'Sacred Sperm ',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2015/01/01/5790806/ZERA_KODESH_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/1214/HOT/29121430Sacred_Sperm_new.mp4/master.m3u8',
                      'genre': 'Documentary'},
                     {'name': 'High-Functioning',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2014/06/09/5377275/tifkud_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0614/HOT/08061400HIGH_FUNCTION.mp4/master.m3u8',
                      'genre': 'Documentary'},
                     {'name': 'Shameless',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2014/04/30/5300104/shame_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0414/HOT/29041630SHAMELESS.mp4/master.m3u8',
                      'genre': 'Documentary'},
                     {'name': 'I am God',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2014/10/07/5628364/DIFFERENT_GOD_2_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/1014/HOT/06101200I_AM_GOD.mp4/master.m3u8',
                      'genre': 'Documentary'}
                     ]}


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: types.GeneratorType
    """
    return VIDEOS.iterkeys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or server.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, 'My Video Collection')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # https://codedocs.xyz/xbmc/xbmc/group__python__xbmcgui__listitem.html#ga0b71166869bda87ad744942888fb5f14
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': category,
                                    'genre': category,
                                    'mediatype': 'video'})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, category)
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': video['name'],
                                    'genre': video['genre'],
                                    'mediatype': 'video'})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
