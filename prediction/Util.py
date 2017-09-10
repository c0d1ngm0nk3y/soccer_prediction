def interprete(out):
    home = out[0]
    away = out[1]
    threshold = 0.5
    variable = 0.05

    if home > (threshold + variable) and away < (threshold - variable):
        return 1
    if away > (threshold + variable) and home < (threshold - variable):
        return 2
    return 0

def calculate_confidence(out):
    outcome = interprete(out)

    if outcome == 1:
        delta = out[0] - out[1]
        confidence = delta * 100
    elif outcome == 2:
        delta = out[1] - out[0]
        confidence = delta * 100
    else:
        delta = abs(out[0] - out[1])
        confidence = 100 - (delta * 100)

    return round(min(confidence, 99))

def calculate_output_for_points(x, y):
    diff = x - y
    out = 0.5 + (0.15 * diff)
    out = max(min(out, 0.99), 0.01)
    return out
