\"\"\"
Study Planner Module for CampusNotes.
Helps students schedule study sessions, calculate estimated revision hours,
and organize topic reviews based on target exam dates.
\"\"\"

from datetime import datetime, timedelta
from typing import List, Dict, Any


class StudyPlanner:
    def __init__(self, subject_name: str, exam_date: str):
        self.subject_name = subject_name
        self.exam_date = datetime.strptime(exam_date, "%Y-%m-%d")
        self.topics: List[Dict[str, Any]] = []

    def add_topic(self, topic_name: str, estimated_hours: float, difficulty: str = "Medium") -> None:
        \"\"\"Add a curriculum topic to the study plan.\"\"\"
        self.topics.append({
            \"topic\": topic_name,
            \"estimated_hours\": estimated_hours,
            \"difficulty\": difficulty,
            \"completed\": False
        })

    def generate_schedule(self) -> Dict[str, Any]:
        \"\"\"Calculates revision timeline and daily recommended effort.\"\"\"
        total_hours = sum(t[\"estimated_hours\"] for t in self.topics)
        days_remaining = max(1, (self.exam_date - datetime.now()).days)
        daily_hours = round(total_hours / days_remaining, 2)

        return {
            \"subject\": self.subject_name,
            \"exam_date\": self.exam_date.strftime(\"%Y-%m-%d\"),
            \"days_remaining\": days_remaining,
            \"total_estimated_hours\": total_hours,
            \"daily_target_hours\": daily_hours,
            \"total_topics\": len(self.topics),
            \"topics\": self.topics
        }


def format_study_summary(plan: Dict[str, Any]) -> str:
    \"\"\"Returns human-readable summary of the study schedule.\"\"\"
    header = f\"=== Study Schedule: {plan['subject']} (Exam: {plan['exam_date']}) ===\"
    metrics = f\"Days Left: {plan['days_remaining']} | Total Hours: {plan['total_estimated_hours']} | Daily Target: {plan['daily_target_hours']} hrs/day\"
    return f\"{header}\n{metrics}\n\"
