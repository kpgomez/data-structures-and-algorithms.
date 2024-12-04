# from class pseudocode for last code challenge
def merge(left, right, arr):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
    k += 1

    # https://chat.openai.com/c/74481750-c964-46a4-ad33-dc86bc45769e
    if i == len(left):
        # set remaining entries in arr to remaining values in right
        pass
    else:
        pass
        # set remaining entries arr to remaining values in left

def merge_sort(arr: list) -> None:
    length = len(arr)

    if length > 1:
        mid = length // 2
        left = arr[0: mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)


def compare(a, b):
    if a > b:
        return 1
    if a < b:
        return -1
    if a == b:
        return 0

def sort_by_title(movies: list) -> list:
    # initialize empty list
    # check movies[index]["title"]
    # ignore "A", "An", and "The "
    # movies[index].lstrip("The ")

    # loop through the list checking each title

    #

def sort_by_year(movies: list) -> list:
    ...
    # compare movies[index]["year"]





if __name__ == "__main__":
    movies = [
        {
            "title": "Beetlejuice",
            "year": 1988,
            "genres": ["Comedy", "Fantasy"],
        },
        {
            "title": "The Cotton Club",
            "year": 1984,
            "genres": ["Crime", "Drama", "Music"],
        },
        {
            "title": "The Shawshank Redemption",
            "year": 1994,
            "genres": ["Crime", "Drama"],
        },
        {
            "title": "Crocodile Dundee",
            "year": 1986,

            "genres": ["Adventure", "Comedy"],
        },
        {
            "title": "Valkyrie",
            "year": 2008,
            "genres": ["Drama", "History", "Thriller"],
        },
        {
            "title": "Ratatouille",
            "year": 2007,
            "genres": ["Animation", "Comedy", "Family"],
        },
        {
            "title": "City of God",
            "year": 2002,

            "genres": ["Crime", "Drama"],
        },
        {
            "title": "Memento",
            "year": 2000,

            "genres": ["Mystery", "Thriller"],
        },
        {
            "title": "The Intouchables",
            "year": 2011,

            "genres": ["Biography", "Comedy", "Drama"],
        },
        {
            "title": "Stardust",
            "year": 2007,
            "genres": ["Adventure", "Family", "Fantasy"],
        },
    ]
    sorted_movies_by_name = sort_by_title(movies)
    newest = sort_by_year(movies)
