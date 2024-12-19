## Anonymous Leaderboard (lev-1)


Table `anonymous-leaderboard`


CRUD functions required (should have tests)

## stage-0
**table-prep**
  - table:
    - leaderboard
  - schema
    - id
    - score

## stage-1:
**basic-crud-ops**
- crud funcs
  - create_ldb_entity
  - get_leaderboard
  - clear_leaderboard

## stage-2
**ldb-with-user-names**
- schema-update
  - add column user_name (uniq)
- crud_ops
  - update-old-queries
    - create_ldb_entity
    - create_or_update_ldb_score
    - get_leaderboard
    - delete_entity

