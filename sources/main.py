import twitter2
import folium
import geopy_stuff
import os


def build_map(friends_coord):
    """
    (list(list(str, (float, float)))) -> folium.Map()
    Returns map object which contains markers with names in given
    coordinates
    """

    mp = folium.Map()
    fg = folium.FeatureGroup(name='friends_locations')

    friends_coord.sort(key=lambda x: x[1])
    to_add_next = [friends_coord[0][0]]
    for i in range(1, len(friends_coord)):
        if friends_coord[i][1] == friends_coord[i - 1][1]:
            to_add_next.append(friends_coord[i][0])
        else:
            friends_to_add = '|'.join(to_add_next)
            fg.add_child(folium.Marker(
                         location=list(friends_coord[i - 1][1]),
                         popup=friends_to_add,
                         icon=folium.Icon()))
            to_add_next = [friends_coord[i][0]]
    friends_to_add = '|'.join(to_add_next)
    fg.add_child(
        folium.Marker(
            location=list(friends_coord[-1][1]),
            popup=friends_to_add, icon=folium.Icon()))

    mp.add_child(fg)
    return mp


def main(nickname):
    data_list = []
    try:
        data_list = twitter2.get_info_by_nickname(nickname)['users']
        lst_friends = []
        for item in data_list:
            try:
                coordinates = geopy_stuff.get_latitude_longtitude(
                    item['location'])
                lst_friends.append([item['name'], coordinates])
            except:
                continue

        home = os.path.dirname(__file__)
        out_path = os.path.join(home,
                                os.path.join('templates', 'map.html'))
        build_map(lst_friends).save(out_path)
    except:
        with open("map.html", "w") as file:
            file.write('Something wrong. Check username carefully.')
