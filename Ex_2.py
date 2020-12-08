time = int(input('Введите количество секунд '))
hours = int(time / 3600)
if hours < 10:
    hours = '0' + str(hours)
ostatok = time % 3600
minutes = int(ostatok / 60)
if minutes < 10:
    minutes = '0' + str(minutes)
ostatok = ostatok % 60
seconds = ostatok
if seconds < 10:
    seconds = '0' + str(seconds)
print(f'{hours}:{minutes}:{seconds}')
