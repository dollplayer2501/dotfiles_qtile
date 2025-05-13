import psutil
import datetime


# システムの起動時刻を取得
boot_time = psutil.boot_time()

# 現在の時刻を取得
current_time = datetime.datetime.now().timestamp()

# 稼働時間を計算（秒単位）
uptime_seconds = current_time - boot_time

# 稼働時間を日、時間、分、秒に変換
uptime_days = uptime_seconds // (24 * 3600)
uptime_hours = (uptime_seconds % (24 * 3600)) // 3600
uptime_minutes = (uptime_seconds % (3600)) // 60
uptime_seconds = uptime_seconds % 60

# 結果を表示
print(f"システムの稼働時間: {int(uptime_days)}日 {int(uptime_hours)}時間 {int(uptime_minutes)}分 {int(uptime_seconds)}秒")


