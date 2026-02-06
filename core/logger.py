class Logger:
    def success(self, step, result):
        print(f"[OK] {step} -> {result}")

    def error(self, step, error):
        print(f"[ERROR] {step} -> {error}")
