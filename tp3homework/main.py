from models.teacher import teacher
from models.student import student
from models.subscription import subscription
from models.event import event
from models.meeting import meeting
from models.trip import trip
from models.competition import competition
from models.donation import donation
from models.monthly_subscription import monthly_subscription
from models.annual_subscription import annual_subscription
import webbrowser

# ---------- DATA CREATION ----------

teachers = [
    teacher(1, "Ahmed Ben Ali", "ahmed@example.com", "0550-123456", "Algiers", "2022-01-15", ["Tajwid"], ["Teaching Quran"]),
    teacher(2, "Fatima Bensalem", "fatima@example.com", "0551-987654", "Oran", "2021-03-22", ["Arabic"], ["Quranic Studies"]),
    teacher(3, "Youssef Amrani", "youssef@example.com", "0552-765432", "Constantine", "2023-05-10", ["Tafsir"], ["Islamic Education"]),
    teacher(4, "Sara Khaled", "sara@example.com", "0553-222333", "Blida", "2022-09-01", ["Recitation"], ["Community Work"])
]

groups = {
    "Group 1": {"teacher": teachers[0], "students": []},
    "Group 2": {"teacher": teachers[1], "students": []},
    "Group 3": {"teacher": teachers[2], "students": []},
    "Group 4": {"teacher": teachers[3], "students": []}
}

first_names = ["Amir", "Sara", "Youssef", "Leila", "Omar", "Meryem", "Ali", "Nadia", "Hassan", "Fatima"]
last_names = ["Ben Ali", "Bensalem", "Amrani", "Khaled", "Mansouri", "Bouaziz"]

all_subscriptions, monthly_subs, annual_subs, donations = [], [], [], []

for i in range(60):
    group_name = f"Group {(i)//15 + 1}"
    sub = subscription(i+1, 5000, "2025-01-10", "paid" if i % 2 == 0 else "unpaid")
    s = student(i+1, f"{first_names[i % len(first_names)]} {last_names[i % len(last_names)]}",
                f"student{i+1}@example.com", f"0550-{100000+i+1}", "Algeria",
                "2024-09-10", ["Quran Reading"], ["Tafsir"], group_name, sub.status)
    groups[group_name]["students"].append(s)
    all_subscriptions.append(sub)
    # alternons entre monthly et annual
    if i % 3 == 0:
        monthly_subs.append(monthly_subscription(s.student_id, 3000, "2025-02-01", "paid"))
    else:
        annual_subs.append(annual_subscription(s.student_id, 30000, "2025-01-01", "paid"))

# Donations
donations = [
    donation("Karim Abbas", 2000, "2025-01-20"),
    donation("Amina Soufi", 5000, "2025-02-10", "For orphan students")
]

# Events
events = [
    event("Quran Recitation Contest", "A competition for best recitation.", "2025-11-15", "Ahmed Ben Ali",
          [s.full_name for s in groups["Group 1"]["students"][:5]]),
    event("Ramadan Charity", "Community charity during Ramadan.", "2025-03-10", "Sara Khaled",
          [s.full_name for s in groups["Group 2"]["students"][:5]])
]
meetings = [
    meeting("Teachers Meeting", "Monthly teacher coordination.", "2025-04-01", "Fatima Bensalem",
            [t.full_name for t in teachers])
]
trips = [
    trip("Educational Trip", "Trip to Quranic Museum.", "2025-05-10", "Youssef Amrani",
         [s.full_name for s in groups["Group 3"]["students"][:5]])
]
competitions = [
    competition("Quran Memorization", "Competition for memorization.", "2025-06-15", "Ahmed Ben Ali",
                [s.full_name for s in groups["Group 4"]["students"][:5]])
]

# ---------- TABLE GENERATION ----------

def generate_table_students():
    rows = ""
    for group_name, data in groups.items():
        for s in data["students"]:
            rows += f"<tr><td>{s.student_id}</td><td>{s.full_name}</td><td>{s.group}</td><td>{s.subscription_status}</td><td>{s.email}</td><td>{s.phone}</td><td>{', '.join(s.skills)}</td><td>{', '.join(s.interests)}</td></tr>"
    return f"""
    <h2>Students</h2>
    <table>
        <tr><th>ID</th><th>Name</th><th>Group</th><th>Status</th><th>Email</th><th>Phone</th><th>Skills</th><th>Interests</th></tr>
        {rows}
    </table>
    """

def generate_table_teachers():
    rows = ""
    for t in teachers:
        rows += f"<tr><td>{t.teacher_id}</td><td>{t.full_name}</td><td>{t.email}</td><td>{t.phone}</td><td>{t.address}</td><td>{t.join_date}</td><td>{', '.join(t.skills)}</td><td>{', '.join(t.interests)}</td></tr>"
    return f"""
    <h2>Teachers</h2>
    <table>
        <tr><th>ID</th><th>Name</th><th>Email</th><th>Phone</th><th>Address</th><th>Join Date</th><th>Skills</th><th>Interests</th></tr>
        {rows}
    </table>
    """

def generate_table_groups():
    rows = ""
    for name, data in groups.items():
        t = data["teacher"]
        rows += f"<tr><td>{name}</td><td>{t.full_name}</td><td>{', '.join(t.skills)}</td><td>{len(data['students'])}</td></tr>"
    return f"""
    <h2>Groups</h2>
    <table>
        <tr><th>Group</th><th>Teacher</th><th>Skills</th><th>Students</th></tr>
        {rows}
    </table>
    """

def generate_event_table(title, event_list):
    rows = ""
    for e in event_list:
        participants = ", ".join(e.participants)
        rows += f"<tr><td>{getattr(e, 'type', 'Event')}</td><td>{e.event_name}</td><td>{e.description}</td><td>{e.event_date}</td><td>{e.organizer}</td><td>{participants}</td></tr>"
    return f"""
    <h2>{title}</h2>
    <table>
        <tr><th>Type</th><th>Name</th><th>Description</th><th>Date</th><th>Organizer</th><th>Participants</th></tr>
        {rows}
    </table>
    """

def generate_subscription_table(title, subs):
    rows = ""
    for sub in subs:
        period = getattr(sub, 'period', 'Standard')
        rows += f"<tr><td>{getattr(sub, 'student_id', '-')}</td><td>{sub.amount}</td><td>{sub.date}</td><td>{sub.status}</td><td>{period}</td></tr>"
    return f"""
    <h2>{title}</h2>
    <table>
        <tr><th>Student ID</th><th>Amount</th><th>Date</th><th>Status</th><th>Type</th></tr>
        {rows}
    </table>
    """

def generate_donation_table():
    rows = ""
    for d in donations:
        rows += f"<tr><td>{d.donor_name}</td><td>{d.amount}</td><td>{d.date}</td><td>{d.message}</td></tr>"
    return f"""
    <h2>Donations</h2>
    <table>
        <tr><th>Donor</th><th>Amount</th><th>Date</th><th>Message</th></tr>
        {rows}
    </table>
    """

# ---------- HTML TEMPLATE ----------
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Quranic School</title>
<style>
body {{ margin:0; font-family:Poppins,sans-serif; display:flex; flex-direction:column; height:100vh; }}
.sidebar {{ width:100%; background:#c7f0c2; padding:10px; display:flex; flex-wrap:wrap; justify-content:center; }}
.sidebar button {{ padding:10px 15px; margin:5px; border:none; border-radius:8px; cursor:pointer; font-size:16px; background:#a4e1a1; transition:all .3s; }}
.sidebar button:hover {{ background:#7ed957; transform:scale(1.05); }}
.tabs button {{ border:none; background:#ecfce9; margin:3px; padding:8px 15px; border-radius:10px; cursor:pointer; transition:0.3s; }}
.tabs button:hover {{ background:#c2f7c0; }}
.tabs button.active {{ background:#a2e5a0; font-weight:bold; }}
.content {{ flex:1; padding:20px; overflow-y:auto; text-align:center; }}
table {{ width:100%; border-collapse: collapse; margin-top:10px; }}
th, td {{ border:1px solid #ccc; padding:8px; }}
th {{ background-color:#d9f8c4; }}
tr:nth-child(even){{ background:#f6fff6; }}
img {{ width:80%; border-radius:20px; margin-top:20px; }}
.bottombar {{ width:100%; background:#f5fff5; padding:20px; border-top:1px solid #d0e8d0; text-align:center; font-size:15px; }}
</style>
</head>
<body>

<div class="sidebar">
<button onclick="showSection('home')">🏠 Home</button>
<button onclick="showSection('students')">👨‍🎓 Students</button>
<button onclick="showSection('teachers')">👩‍🏫 Teachers</button>
<button onclick="showSection('groups')">📚 Groups</button>
<button onclick="showSection('events')">🕌 Events</button>
<button onclick="showSection('subscriptions')">💳 Subscriptions</button>
</div>

<div class="content" id="content">
<div id="home">
<h2>Welcome to Quranic School</h2>
<p>“And We have certainly made the Quran easy for remembrance, so is there any who will remember?” (Al-Qamar 54:17)</p>
<img src="img/pic.jpg" alt="Quranic Image">
<div class="bottombar">
<h3>📅 Opening Hours</h3>
<p>Sunday to Thursday | 8:00 AM - 4:00 PM</p>
<h3>📞 Contact</h3>
<p>Email: contact@quranicschool.com | Phone: 0550-000000</p>
</div>
</div>

<div id="students" style="display:none;">{generate_table_students()}</div>
<div id="teachers" style="display:none;">{generate_table_teachers()}</div>
<div id="groups" style="display:none;">{generate_table_groups()}</div>

<!-- EVENTS SECTION -->
<div id="events" style="display:none;">
<div class="tabs">
<button onclick="showSubSection('events_general', this)">General</button>
<button onclick="showSubSection('events_meeting', this)">Meetings</button>
<button onclick="showSubSection('events_trip', this)">Trips</button>
<button onclick="showSubSection('events_competition', this)">Competitions</button>
</div>
<div id="events_general">{generate_event_table("General Events", events)}</div>
<div id="events_meeting" style="display:none;">{generate_event_table("Meetings", meetings)}</div>
<div id="events_trip" style="display:none;">{generate_event_table("Trips", trips)}</div>
<div id="events_competition" style="display:none;">{generate_event_table("Competitions", competitions)}</div>
</div>

<!-- SUBSCRIPTIONS SECTION -->
<div id="subscriptions" style="display:none;">
<div class="tabs">
<button onclick="showSubSection('sub_monthly', this)">Monthly</button>
<button onclick="showSubSection('sub_annual', this)">Annual</button>
<button onclick="showSubSection('sub_donation', this)">Donations</button>
</div>
<div id="sub_monthly">{generate_subscription_table("Monthly Subscriptions", monthly_subs)}</div>
<div id="sub_annual" style="display:none;">{generate_subscription_table("Annual Subscriptions", annual_subs)}</div>
<div id="sub_donation" style="display:none;">{generate_donation_table()}</div>
</div>
</div>

<script>
function showSection(id){{
    const sections = ['home','students','teachers','groups','events','subscriptions'];
    sections.forEach(s => document.getElementById(s).style.display = 'none');
    document.getElementById(id).style.display = 'block';
}}
function showSubSection(id, btn){{
    const subsections = ['events_general','events_meeting','events_trip','events_competition','sub_monthly','sub_annual','sub_donation'];
    subsections.forEach(s => {{
        const el = document.getElementById(s);
        if (el) el.style.display = 'none';
    }});
    document.getElementById(id).style.display = 'block';
    document.querySelectorAll('.tabs button').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
}}
</script>

</body>
</html>"""

with open("quranic_school.html", "w", encoding="utf-8") as f:
    f.write(html_content)

webbrowser.open("quranic_school.html")
print("✅ Quranic School interactive page generated successfully with full SOLID features!")
