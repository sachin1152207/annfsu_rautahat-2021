from datetime import datetime, timedelta

def time_ago(timestamp):
    now = datetime.now()
    diff = now - timestamp

    # If less than a minute
    if diff.total_seconds() < 60:
        return "just now"

    # If less than an hour
    elif diff.total_seconds() < 3600:
        minutes = int(diff.total_seconds() // 60)
        return f"{minutes} minute{'s' if minutes > 1 else ''} ago"

    # If less than a day
    elif diff.total_seconds() < 86400:
        hours = int(diff.total_seconds() // 3600)
        return f"{hours} hour{'s' if hours > 1 else ''} ago"

    # If more than a day, show date
    else:
        return timestamp.strftime("%Y-%m-%d")