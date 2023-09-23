import redis
red = redis.Redis(
    host ="redis-11694.c261.us-east-1-4.ec2.cloud.redislabs.com",
    port = 11694,
    password = "osOBAKaXI3yraaCjz9lVHWA5cgTd7VQ1"
)

red.set("var1", "value1")

print(red.get("var1"))