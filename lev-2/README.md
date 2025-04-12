## Moviebook (lev-2)
Multiple migrations are there for you to be aware of connotations of a simple addition of single column.
# stage-1
CRUD on artist tables

- schema:
  - id
  - name
  - pic_link (nullable)
  - info

- api funcs:
  - create_artist
  - delete_artist_by_id
  - update_artist_info_by_id
  - get_artist_by_id
  - get_artist_by_name
  - get_artists_with_similar_names (names that contains these characters)

- db funcs required (add tests for all)
  - create_artist
  - delete_artist
  - delete_artist_by_id
  - update_artist_info_by_id
  - get_artist_by_id
  - get_artist_by_name
  - get_artists_with_similar_names (names that contains these characters)


----
# stage-2
add movies tables
