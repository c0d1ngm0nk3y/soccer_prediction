THRESHOLD = 0.025
MID_POINT = 0.5
MAX_DIFF = 2
DIFF_PER_GOAL = (MID_POINT / MAX_DIFF)
MIN_DIFFERENCE = 0.4

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
        delta = out[0] - out[1] - (2*THRESHOLD) + MIN_DIFFERENCE
        confidence = delta * 100.0
    elif outcome == 2:
        delta = out[1] - out[0] - (2 * THRESHOLD) + MIN_DIFFERENCE
        confidence = delta * 100.0
    else:
        delta = abs(out[0] - out[1])
        confidence = 100 - 100.0 * (delta / 0.2)

    return round(max(min(confidence, 99), 0.01))

def calculate_output_for_points(points_a, points_b):
    diff = points_a - points_b
    out = MID_POINT + (DIFF_PER_GOAL * diff)
    out = max(min(out, 0.99), 0.01)
    return out

def calculate_result_out_v_home_away(home_points, away_points):
    y_points_home = calculate_output_for_points(home_points, away_points)
    y_points_away = calculate_output_for_points(away_points, home_points)

    output = [y_points_home, y_points_away]
    return output

def calculate_result_out_v_home(home_points, away_points):
    if home_points > away_points:
        return [0.99]

    return [0.01]

class HomeAwayJudger(object):
    def interprete(self, out):
        return interprete(out)

    def calculate_out_v(self, home_points, away_points):
        return calculate_result_out_v_home_away(home_points, away_points)

    def calculate_confidence(self, out):
        return calculate_confidence(out)

class HomeJudger(object):
    def interprete(self, out):
        home = out[0]
        if home >= 0.4:
            return 1

        return 2

    def calculate_out_v(self, home_points, away_points):
        return calculate_result_out_v_home(home_points, away_points)

    def calculate_confidence(self, out):
        return out[0] * 100

class AwayJudger(object):
    def interprete(self, out):
        away = out[0]
        if away >= 0.4:
            return 2

        return 1

    def calculate_out_v(self, home_points, away_points):
        if home_points < away_points:
            return [0.99]

        return [0.01]

    def calculate_confidence(self, out):
        return out[0] * 100

def create_judger(judger_id):
    if judger_id == "home":
        return HomeJudger()
    elif judger_id == "away":
        return AwayJudger()

    return HomeAwayJudger()
