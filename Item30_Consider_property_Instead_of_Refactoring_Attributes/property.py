

from datetime import datetime, timedelta
class Bucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()

        self.max_quota = 0
        self.quota_consumed = 0

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        if amount == 0:
            self.quota_consumed = 0
            self.max_quota = 0

        elif delta < 0:
            assert self.quota_consumed == 0
            self.max_quota = amount

        else:
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta

    def __repr__(self):
        return 'Bucket(quota=%d)' % self.quota

def fill(bucket, amount):
    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now

    bucket.quota += amount


def deduct(bucket, amount):
    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        return False

    if bucket.quota - amount < 0:
        return False

    bucket.quota -= amount
    return True

a = Bucket(60)
fill(a, 100)

if deduct(a, 99):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')

if deduct(a, 3):
    print('Had 3 quota')
else:
    print('Not enough for 3 quota')
print(a)
