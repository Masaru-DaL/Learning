class OyaA:
  def __init__(self):
    print("oya A")

class OyaB:
  def __init__(self):
    print("oya B")

class Ko(OyaB, OyaA):
  def __init__(self):
    print("ko")

ko = Ko()
