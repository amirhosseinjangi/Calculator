from flask import Flask, render_template, request
import math

app = Flask(__name__)


# توابع مثلثاتی بر اساس درجه
def deg_sin(x):
    return math.sin(math.radians(x))


def deg_tan(x):
    return math.tan(math.radians(x))


def safe_eval(expr: str):
    """
    ارزیابی عبارت با sin و tan درجه‌ای.
    اینجا از eval استفاده شده ولی محیطش محدود شده.
    """
    allowed_globals = {
        "__builtins__": None,
        "sin": deg_sin,
        "tan": deg_tan,
        "pi": math.pi,
        "e": math.e,
    }
    return eval(expr, allowed_globals, {})


@app.route("/", methods=["GET", "POST"])
def index():
    expression = ""
    result = ""
    error = ""

    if request.method == "POST":
        expression = request.form.get("expression", "").strip()

        if expression:
            try:
                value = safe_eval(expression)
                result = str(value)
            except Exception:
                error = "خطا در محاسبه"
        else:
            error = "عبارتی وارد نشده است"

    return render_template(
        "index.html",
        expression=expression,
        result=result,
        error=error,
    )


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
