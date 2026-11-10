import json, os, subprocess

def mouse_pos():
    out = subprocess.run(["cliclick", "p"], capture_output=True, text=True).stdout.strip()
    x, y = out.split(",")
    return int(float(x)), int(float(y))

print("Simulator 창을 띄워두고, 이후로는 창을 옮기지 마세요.\n")
input("1) 마우스를 휴대폰 화면의 '왼쪽 위' 모서리에 올리고, 클릭하지 말고 Enter... ")
x1, y1 = mouse_pos()
input("2) 마우스를 휴대폰 화면의 '오른쪽 아래' 모서리에 올리고, 클릭하지 말고 Enter... ")
x2, y2 = mouse_pos()

region = [x1, y1, x2 - x1, y2 - y1]
path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "hidagent", "sim_region.json")
with open(path, "w") as f:
    json.dump({"region": region}, f)
print(f"\n저장 완료: {region} -> {path}")
