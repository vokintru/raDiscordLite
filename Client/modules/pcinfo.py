import http.client
import platform


def get_ip():
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    answer = conn.getresponse().read()
    return answer


def sysinfo():
    global_ip = str(get_ip())[2:-1]
    data = 'OS: ' + platform.uname()[0] + ' ' + platform.uname()[2] + ' - ' + platform.architecture()[0] + '\n'
    data += 'Узел: ' + platform.node() + '\n'
    data += 'Имя ПК: ' + platform.uname()[1] + '\n'
    data += 'Версия: ' + platform.uname()[3] + '\n'
    data += 'Тип системы: ' + platform.uname()[4] + '\n'
    data += 'Описание: ' + platform.uname()[5] + '\n'
    data += 'Публичный IP: ' + global_ip + '\n'
    return data
