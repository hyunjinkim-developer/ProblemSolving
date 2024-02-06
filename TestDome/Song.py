"""
Problem:
https://www.testdome.com/questions/python/song/94852
"""

# Solution 1:
class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_in_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        song_list = set()

        current = self
        while current.next != None:
            if current.name in song_list:
                return True
            else:
                song_list.add(current.name)
                current = current.next

        return False


first = Song("Hello")
second = Song("Eye of the tiger")
third = Song("third")

first.next_song(second)
second.next_song(third)
third.next_song(second)

print(first.is_in_repeating_playlist())

"""
# Solution 2:

class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_in_repeating_playlist(self):
        # :returns: (bool) True if the playlist is repeating, False if not.
        
        song_list = set()

        current = self
        while current.next != None:
            if current.next.name not in song_list:
                song_list.add(current.name)
                current = current.next
            else:
                return True
        return False


first = Song("Hello")
second = Song("Eye of the tiger")
third = Song("third")

first.next_song(second)
second.next_song(third)
third.next_song(second)

print(first.is_in_repeating_playlist())
"""

