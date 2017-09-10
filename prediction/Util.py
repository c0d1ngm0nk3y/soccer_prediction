THRESHOLD = 0.025
MID_POINT = 0.5
MAX_DIFF = 2
DIFF_PER_GOAL = (MID_POINT / MAX_DIFF)

def interprete(out):
    home = out[0]
    away = out[1]

    if home > (MID_POINT + THRESHOLD) and away < (MID_POINT - THRESHOLD):
        return 1
    if away > (MID_POINT + THRESHOLD) and home < (MID_POINT - THRESHOLD):
        return 2
    return 0

def calculate_confidence(out):
    outcome = interprete(out)

    if outcome == 1:
        delta = out[0] - out[1] - (2*THRESHOLD)
        confidence = delta / (1 - (2*THRESHOLD)) * 100
    elif outcome == 2:
        delta = out[1] - out[0] - (2 * THRESHOLD)
        confidence = delta / (1 - (2 * THRESHOLD)) * 100
    else:
        delta = abs(out[0] - out[1])
        confidence = 100 - ((delta / (MID_POINT + THRESHOLD)) * 100)

    return round(max(min(confidence, 99), 0.01))

def calculate_output_for_points(x, y):
    diff = x - y
    out = MID_POINT + (DIFF_PER_GOAL * diff)
    out = max(min(out, 0.99), 0.01)
    return out
