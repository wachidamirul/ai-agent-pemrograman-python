from core.planner import Planner
from core.memory import Memory
from core.state import State
from core.logger import Logger

from tools.calculator import calculator
from tools.search_csv import search_csv
from tools.summarize_text import summarize_text


class Agent:
    def __init__(self):
        self.planner = Planner()
        self.memory = Memory()
        self.state = State()
        self.logger = Logger()


    def decide_tool(self, task):
        task = task.lower()
        if "hitung" in task or "berapa" in task:
            return "calculator"
        if "cari" in task:
            return "search_csv"
        if "ringkas" in task:
            return "summarize_text"
        return None

    def run(self, user_input):
        plan = self.planner.create_plan(user_input)
        tool = self.decide_tool(user_input)

        last_result = None

        for step in plan:
            try:
                # STEP 1: memahami tujuan (NO TOOL)
                if step == "Memahami tujuan":
                    result = f"Tujuan dipahami: {user_input}"

                # STEP 2: eksekusi task utama (TOOL DIPANGGIL DI SINI)
                elif step == user_input:
                    if tool == "calculator":
                        expr = user_input.replace("hitung", "").strip()
                        result = calculator(expr)

                    elif tool == "search_csv":
                        keyword = user_input.replace("cari", "").strip()
                        result = search_csv(keyword)

                    elif tool == "summarize_text":
                        text = user_input.replace("ringkas", "").strip()
                        result = summarize_text(text)

                    else:
                        result = "Tidak ada tool yang sesuai"

                    last_result = result

                # STEP 3: simpulan (NO TOOL)
                elif step == "Menyimpulkan hasil":
                    result = f"Hasil akhir: {last_result}"

                else:
                    result = f"Menjalankan langkah: {step}"

                self.memory.add(result)
                self.state.update(step, result)
                self.logger.success(step, result)

            except Exception as e:
                self.logger.error(step, e)
                return f"Error pada langkah '{step}': {e}"

        return last_result


