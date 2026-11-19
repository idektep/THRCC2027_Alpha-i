# Robot RL Course: Python & Reinforcement Learning for Humanoid Robot

หลักสูตรออนไลน์ 10 สัปดาห์ สำหรับผู้เรียนอายุ 13–17 ปี เรียนรู้ด้วยตนเองผ่าน VS Code และ Jupyter Notebook ตั้งแต่พื้นฐาน Python ไปจนถึงการใช้ Reinforcement Learning (Q-Learning) เพื่อฝึกให้หุ่นยนต์ Humanoid เรียนรู้และควบคุมท่าทางได้ พร้อมเตรียมความพร้อมสำหรับการแข่งขัน

## Course Outline

| Week | Topic | Learning Outcome |
|---|---|---|
| 0 | Environment Setup | ติดตั้งเครื่องมือและเตรียมสภาพแวดล้อมสำหรับการเรียน |
| 1 | Introduction to Python Programming | เขียน Python เพื่อกำหนดและปรับค่ามุมข้อต่อ |
| 2 | Python Functions & NumPy Fundamentals | ใช้ NumPy จัดการ State และสร้าง Q-table |
| 3 | Humanoid Robot Control & Simulation | เข้าใจ State และควบคุมหุ่นยนต์ผ่าน Action |
| 4 | Introduction to Reinforcement Learning | เข้าใจ RL Feedback Loop และ Reward |
| 5 | Q-Learning Algorithm & Q-table Training | ฝึก Q-table เพื่อทำ Single Target Pose |
| 6 | Exploration & Hyperparameter Optimization | ปรับ Hyperparameters และวิเคราะห์ผล Training |
| 7 | Goal-Conditioned Q-Learning & Sequential Pose Control | ควบคุมหุ่นยนต์ให้ทำท่าทางต่อเนื่อง |
| 8 | Advanced Reinforcement Learning Environment | เรียนรู้การรับมือกับความไม่แน่นอนของสภาพแวดล้อม |
| 9 | Q-Learning Performance Evaluation & Optimization | ประเมินและปรับปรุงประสิทธิภาพของ Policy |
| 10 | Competition Preparation & Mock Challenge | เตรียมความพร้อมสำหรับการแข่งขัน |

## Requirements

**Hardware**
- Windows 10/11, macOS หรือ Linux
- RAM อย่างน้อย 4 GB
- พื้นที่ว่างอย่างน้อย 2 GB
- อินเทอร์เน็ตสำหรับดาวน์โหลดโปรแกรมและรับชมบทเรียน

**Software**

| Software | Version |
|---|---|
| Python | 3.13.11 (แนะนำ) |
| Visual Studio Code | Latest |
| Python Extension | Latest |
| Jupyter Extension | Latest |

**Python Libraries**
- numpy
- matplotlib
- ipykernel
- ipywidgets

## Installation & Setup

### 1. Install Python

ดาวน์โหลด Python 3.13 จาก [Python Official Website](https://www.python.org/downloads/)

- Windows: ระหว่างติดตั้งให้เลือก Add python.exe to PATH
- macOS: ตรวจสอบเวอร์ชันด้วยคำสั่ง `python3 --version`
- Linux: ติดตั้ง Python 3.13.11 ผ่าน pyenv

### 2. Install VS Code

ดาวน์โหลดและติดตั้งจาก [Visual Studio Code](https://code.visualstudio.com/download)

จากนั้นติดตั้ง Extensions:
- Python (Microsoft)
- Jupyter (Microsoft)

### 3. Download Course

ดาวน์โหลด Source Code จาก GitHub โดยเลือก Code → Download ZIP หรือใช้คำสั่ง

```bash
git clone <repository-url>
```

แตกไฟล์และเปิดโฟลเดอร์ `robot-rl-course` ใน VS Code

### 4. Create Virtual Environment

เปิด Terminal ใน VS Code แล้วสร้าง Virtual Environment

**Windows**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Verify Installation

เปิดไฟล์ `week00/check_setup.ipynb`

1. เลือก Select Kernel
2. เลือก Python Environments
3. เลือก `.venv`
4. กด Run All

หากแสดงข้อความ **"ผ่านทั้งหมด พร้อมเริ่มสัปดาห์ 1"** แสดงว่าพร้อมเริ่มเรียน

## Course Structure

```text
robot-rl-course/
│
├── README.md
├── requirements.txt
├── .gitignore
├── robot_course/
│   ├── __init__.py
│   └── simulator.py
│
├── week00/
│   └── check_setup.ipynb
│
├── week01/
│   └── assignment/
│       ├── 1_mission.ipynb
│       ├── 2_learn.ipynb
│       ├── 3_try_it.ipynb
│       ├── 4_challenge.ipynb
│       └── 5_check.ipynb
│
└── week02/ ... week10/
```

## How to Learn

แต่ละสัปดาห์ประกอบด้วย Notebook 5 บท เรียนตามลำดับ ดังนี้

| Notebook | Description | Time |
|---|---|---|
| 1_mission | แนะนำภารกิจและเป้าหมายการเรียนรู้ | 5 นาที |
| 2_learn | เรียนรู้แนวคิดและทดลองรันโค้ด | 25 นาที |
| 3_try_it | ฝึกเขียนโค้ดด้วยตนเอง | 30 นาที |
| 4_challenge | ฝึกแก้โจทย์ 3 ระดับ | 30 นาที |
| 5_check | แบบทดสอบและตรวจสอบความเข้าใจ | 15 นาที |

**Learning Guidelines**
- เรียนตามลำดับ Notebook ที่กำหนด
- รันเซลล์แรกของแต่ละ Notebook ก่อนเริ่มเรียน
- ทดลองทำโจทย์ด้วยตนเองก่อนดูเฉลยจากวิดีโอ
- ตรวจสอบผลลัพธ์จาก Output ที่โจทย์กำหนด
- หากพบปัญหา สามารถตรวจสอบคำแนะนำใน Notebook แต่ละบท

**Estimated Learning Time:** ประมาณ 2 ชั่วโมงต่อสัปดาห์

## Notes

- ใช้ Virtual Environment (`.venv`) และ `requirements.txt` ชุดเดียวกันตลอดหลักสูตร ไม่ต้องสร้างใหม่เมื่อเริ่มสัปดาห์ถัดไป
- โฟลเดอร์ `robot_course/` เป็นไลบรารีของหลักสูตร ไม่จำเป็นต้องแก้ไข
- หากดาวน์โหลดผ่าน Git สามารถใช้ `git pull` เพื่ออัปเดตเนื้อหาใหม่ได้
- แนะนำให้เก็บไฟล์งานส่วนตัวแยกไว้ในโฟลเดอร์ `my_work/`

