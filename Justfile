default:
    just --list

install:
    pip install -r requirements.txt

alias c := create_kinesis_stream
alias d := delete_kinesis_stream
alias l := list_kinesis_streams

create_kinesis_stream:
	aws kinesis create-stream --stream-name APIData --shard-count 1

delete_kinesis_stream:
	aws kinesis delete-stream --stream-name APIData

list_kinesis_streams:
	aws kinesis list-streams

bulk_post:
    python bulk_post_to_api.py