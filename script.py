import subprocess

from db_engine import s, Emotion

emotions = s.query(Emotion).all()
subprocess.run('', shell=True)
while True:
    emotion = input("\n#\n")
    item = s.query(Emotion).filter(Emotion.name == emotion).first()
    if item:
        print(item.name, end="\n")
    else:
        print(f"Not found \"{emotion}\"")