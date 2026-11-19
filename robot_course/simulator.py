"""วาดหุ่นยนต์ 2D ง่ายๆ จากมุมข้อต่อ [shoulder, elbow, wrist] (0-180 องศา)"""
import math
import matplotlib.pyplot as plt

JOINTS = ("shoulder", "elbow", "wrist")


def _to_list(angles):
    if isinstance(angles, dict):
        return [angles[k] for k in JOINTS]
    return list(angles)


def show_robot(angles, title="Robot pose"):
    """angles: list [shoulder, elbow, wrist] หรือ dict ที่มีคีย์ shoulder/elbow/wrist"""
    s, e, w = _to_list(angles)
    ok = all(0 <= a <= 180 for a in (s, e, w))
    color = "#1f77b4" if ok else "#d62728"

    def step(x, y, phi, length):
        r = math.radians(phi)  # 0 = ชี้ลง, 90 = ชี้ออกข้าง, 180 = ชี้ขึ้น
        return x + length * math.sin(r), y - length * math.cos(r)

    sx, sy = 0.0, 3.0
    ex, ey = step(sx, sy, s, 1.4)
    wx, wy = step(ex, ey, s + e, 1.2)
    hx, hy = step(wx, wy, s + e + w, 0.6)

    fig, ax = plt.subplots(figsize=(4, 4))
    ax.plot([0, 0], [0.5, 3.0], color="gray", lw=8)             # ลำตัว
    ax.add_patch(plt.Circle((0, 3.5), 0.45, color="gray"))        # หัว
    ax.plot([sx, ex, wx, hx], [sy, ey, wy, hy], color=color, lw=5, marker="o", ms=10)
    ax.text(sx - 0.1, sy + 0.15, f"shoulder {s}°", ha="right", fontsize=8)
    ax.text(ex + 0.1, ey, f"elbow {e}°", fontsize=8)
    ax.text(wx + 0.1, wy - 0.15, f"wrist {w}°", fontsize=8)
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(0, 5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title if ok else title + "  (angle out of 0-180!)", color=color, fontsize=10)
    plt.show()
