import speedtest

s = speedtest.Speedtest()

down_speed = s.download()
up_speed = s.upload()
ping = s.results.ping

down_speed_mbps = down_speed / 1_000_000
up_speed_mbps = up_speed / 1_000_000

print(f"Vel. Download: {down_speed_mbps:.2f} Mbps")
print(f"Vel. Upload: {up_speed_mbps:.2f} Mbps")
print(f"Ping: {ping:.2f} ms")