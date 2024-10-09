    def dp(value, weight_index):
        if value < 1 or weight_index < 0:
            return False
        if possible[value]:
            return True
        if new_arr[weight_index] == value:
            possible[value] = True
            return True
        if dp(value - new_arr[weight_index], weight_index - 1) or dp(value, weight_index - 1):
            possible[value] = True
        return possible[value]
    dp(k, len(new_arr) - 1)