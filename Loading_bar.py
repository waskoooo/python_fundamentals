def loading_bar(percent):
    filled_segments = percent // 10
    empty_segments = 10 - filled_segments

    bar = f"{percent}% [{'%' * filled_segments}{'.' * empty_segments}]"
    if percent == 100:
        return f"{bar}\n100% Complete!\n[{'%' * 10}]"
    else:
        return f"{bar}\nStill loading..."

percent = int(input())
print(loading_bar(percent))