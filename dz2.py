def get_network_class(ip):
    """Определяет класс сети по IP-адресу"""
    first_octet = int(ip.split('.')[0])
    
    if 1 <= first_octet <= 126:
        return 'A'
    elif 128 <= first_octet <= 191:
        return 'B'
    elif 192 <= first_octet <= 223:
        return 'C'
    elif 224 <= first_octet <= 239:
        return 'D (мультикаст)'
    elif 240 <= first_octet <= 255:
        return 'E (зарезервирован)'
    else:
        return 'Неизвестный'

def get_default_mask(net_class):
    """Возвращает маску подсети по умолчанию для класса"""
    if net_class == 'A':
        return '255.0.0.0'
    elif net_class == 'B':
        return '255.255.0.0'
    elif net_class == 'C':
        return '255.255.255.0'
    else:
        return 'Не применяется'

def get_network_range(ip, net_class):
    """Вычисляет начальный и конечный адреса сети"""
    octets = list(map(int, ip.split('.')))
    
    if net_class == 'A':
        start = f"{octets[0]}.0.0.0"
        end = f"{octets[0]}.255.255.255"
    elif net_class == 'B':
        start = f"{octets[0]}.{octets[1]}.0.0"
        end = f"{octets[0]}.{octets[1]}.255.255"
    elif net_class == 'C':
        start = f"{octets[0]}.{octets[1]}.{octets[2]}.0"
        end = f"{octets[0]}.{octets[1]}.{octets[2]}.255"
    else:
        start = "Не применяется"
        end = "Не применяется"
    
    return start, end

def validate_ip(ip_str):
    """Проверяет корректность IP-адреса"""
    octets = ip_str.split('.')
    
    if len(octets) != 4:
        return False, "IP-адрес должен содержать 4 октета, разделенных точками."
    
    for octet in octets:
        if not octet.isdigit():
            return False, "Октеты должны быть целыми числами."
        num = int(octet)
        if num < 0 or num > 255:
            return False, "Неверный формат IP-адреса. Каждый октет должен быть от 0 до 255."
    
    return True, ""

def main():
    print("Программа для определения класса сети и параметров по IP-адресу")
    
    while True:
        ip = input("\nВведите IP-адрес (или 'exit' для выхода): ").strip()
        
        if ip.lower() == 'exit':
            print("Выход из программы.")
            break
        
        valid, message = validate_ip(ip)
        if not valid:
            print(f"Ошибка: {message}")
            continue
        
        net_class = get_network_class(ip)
        mask = get_default_mask(net_class)
        start, end = get_network_range(ip, net_class)
        
        print("\nРезультат анализа:")
        print(f"IP-адрес: {ip}")
        print(f"Класс сети: {net_class}")
        print(f"Маска подсети: {mask}")
        print(f"Начальный адрес сети: {start}")
        print(f"Конечный адрес сети: {end}")

if __name__ == "__main__":
    main()