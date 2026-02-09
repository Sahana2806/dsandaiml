raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(raw_logs)
print("Unique Users:", unique_users)
print("Is ID05 a unique visitor?", "ID05" in unique_users)
print("Total log entries:", len(raw_logs))
print("Total unique visitors:", len(unique_users))


