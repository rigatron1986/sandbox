import redis
import time

r = redis.Redis(host='192.168.1.171', port=6379, db=1)
# print(r.get('hello'))
print(r.keys())
# print(r.get('hello').decode())

# print(type(r))
# print(dir(r))
# r.delete('hello')

dir_r = ['RESPONSE_CALLBACKS', '__abstractmethods__', '__annotations__', '__class__', '__class_getitem__',
         '__contains__', '__del__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__enter__',
         '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__',
         '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__parameters__',
         '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__slots__', '__str__',
         '__subclasshook__', '__weakref__', '_abc_impl', '_disconnect_raise', '_eval', '_evalsha', '_fcall',
         '_georadiusgeneric', '_geosearchgeneric', '_is_protocol', '_is_runtime_protocol',
         '_send_command_parse_response', '_zaggregate', '_zrange', 'acl_cat', 'acl_deluser', 'acl_dryrun',
         'acl_genpass', 'acl_getuser', 'acl_help', 'acl_list', 'acl_load', 'acl_log', 'acl_log_reset', 'acl_save',
         'acl_setuser', 'acl_users', 'acl_whoami', 'append', 'auth', 'bf', 'bgrewriteaof', 'bgsave', 'bitcount',
         'bitfield', 'bitop', 'bitpos', 'blmove', 'blmpop', 'blpop', 'brpop', 'brpoplpush', 'bzmpop', 'bzpopmax',
         'bzpopmin', 'cf', 'client', 'client_getname', 'client_getredir', 'client_id', 'client_info', 'client_kill',
         'client_kill_filter', 'client_list', 'client_no_evict', 'client_pause', 'client_reply', 'client_setname',
         'client_tracking', 'client_tracking_off', 'client_tracking_on', 'client_trackinginfo', 'client_unblock',
         'client_unpause', 'close', 'cluster', 'cms', 'command', 'command_count', 'command_docs', 'command_getkeys',
         'command_getkeysandflags', 'command_info', 'command_list', 'config_get', 'config_resetstat', 'config_rewrite',
         'config_set', 'connection', 'connection_pool', 'copy', 'dbsize', 'debug_object', 'debug_segfault', 'decr',
         'decrby', 'delete', 'dump', 'echo', 'eval', 'eval_ro', 'evalsha', 'evalsha_ro', 'execute_command', 'exists',
         'expire', 'expireat', 'expiretime', 'failover', 'fcall', 'fcall_ro', 'flushall', 'flushdb', 'from_url', 'ft',
         'function_delete', 'function_dump', 'function_flush', 'function_kill', 'function_list', 'function_load',
         'function_restore', 'function_stats', 'geoadd', 'geodist', 'geohash', 'geopos', 'georadius',
         'georadiusbymember', 'geosearch', 'geosearchstore', 'get', 'get_connection_kwargs', 'get_encoder', 'getbit',
         'getdel', 'getex', 'getrange', 'getset', 'graph', 'hdel', 'hello', 'hexists', 'hget', 'hgetall', 'hincrby',
         'hincrbyfloat', 'hkeys', 'hlen', 'hmget', 'hmset', 'hrandfield', 'hscan', 'hscan_iter', 'hset', 'hsetnx',
         'hstrlen', 'hvals', 'incr', 'incrby', 'incrbyfloat', 'info', 'json', 'keys', 'lastsave', 'latency_histogram',
         'lcs', 'lindex', 'linsert', 'llen', 'lmove', 'lmpop', 'load_external_module', 'lock', 'lolwut', 'lpop', 'lpos',
         'lpush', 'lpushx', 'lrange', 'lrem', 'lset', 'ltrim', 'memory_doctor', 'memory_help', 'memory_malloc_stats',
         'memory_purge', 'memory_stats', 'memory_usage', 'mget', 'migrate', 'module_list', 'module_load',
         'module_loadex', 'module_unload', 'monitor', 'move', 'mset', 'msetnx', 'object', 'parse_response', 'persist',
         'pexpire', 'pexpireat', 'pexpiretime', 'pfadd', 'pfcount', 'pfmerge', 'ping', 'pipeline', 'psetex', 'psync',
         'pttl', 'publish', 'pubsub', 'pubsub_channels', 'pubsub_numpat', 'pubsub_numsub', 'quit', 'randomkey',
         'readonly', 'readwrite', 'register_script', 'rename', 'renamenx', 'replicaof', 'reset', 'response_callbacks',
         'restore', 'role', 'rpop', 'rpoplpush', 'rpush', 'rpushx', 'sadd', 'save', 'scan', 'scan_iter', 'scard',
         'script_debug', 'script_exists', 'script_flush', 'script_kill', 'script_load', 'sdiff', 'sdiffstore', 'select',
         'sentinel', 'sentinel_ckquorum', 'sentinel_failover', 'sentinel_flushconfig',
         'sentinel_get_master_addr_by_name', 'sentinel_master', 'sentinel_masters', 'sentinel_monitor',
         'sentinel_remove', 'sentinel_reset', 'sentinel_sentinels', 'sentinel_set', 'sentinel_slaves', 'set',
         'set_response_callback', 'setbit', 'setex', 'setnx', 'setrange', 'shutdown', 'sinter', 'sintercard',
         'sinterstore', 'sismember', 'slaveof', 'slowlog_get', 'slowlog_len', 'slowlog_reset', 'smembers', 'smismember',
         'smove', 'sort', 'sort_ro', 'spop', 'srandmember', 'srem', 'sscan', 'sscan_iter', 'stralgo', 'strlen',
         'substr', 'sunion', 'sunionstore', 'swapdb', 'sync', 'tdigest', 'time', 'topk', 'touch', 'transaction', 'ts',
         'ttl', 'type', 'unlink', 'unwatch', 'wait', 'watch', 'xack', 'xadd', 'xautoclaim', 'xclaim', 'xdel',
         'xgroup_create', 'xgroup_createconsumer', 'xgroup_delconsumer', 'xgroup_destroy', 'xgroup_setid',
         'xinfo_consumers', 'xinfo_groups', 'xinfo_stream', 'xlen', 'xpending', 'xpending_range', 'xrange', 'xread',
         'xreadgroup', 'xrevrange', 'xtrim', 'zadd', 'zcard', 'zcount', 'zdiff', 'zdiffstore', 'zincrby', 'zinter',
         'zintercard', 'zinterstore', 'zlexcount', 'zmpop', 'zmscore', 'zpopmax', 'zpopmin', 'zrandmember', 'zrange',
         'zrangebylex', 'zrangebyscore', 'zrangestore', 'zrank', 'zrem', 'zremrangebylex', 'zremrangebyrank',
         'zremrangebyscore', 'zrevrange', 'zrevrangebylex', 'zrevrangebyscore', 'zrevrank', 'zscan', 'zscan_iter',
         'zscore', 'zunion', 'zunionstore']
