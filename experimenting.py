import boto3

kinesis = boto3.client('kinesis')

kinesis.list_streams()

response = kinesis.describe_stream(
    StreamName='APIData',
)

kinesis.list_shards(
    StreamName='APIData',
)

shard_iterator = kinesis.get_shard_iterator(
    StreamName='APIData',
    ShardId='shardId-000000000000',
    ShardIteratorType='LATEST',
)

reccord = kinesis.get_records(
    ShardIterator=shard_iterator["ShardIterator"],
    Limit=123
)
print(reccord)
len(reccord["Records"])

reccord = kinesis.get_records(
    ShardIterator=reccord["NextShardIterator"],
    Limit=123
)
print(reccord)