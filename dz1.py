def decimal_to_binary(ip_decimal):
    """Конвертирует десятичный IP в двоичный"""
    octets = list(map(int, ip_decimal.split('.')))
    binary_octets = [format(octet, '08b') for octet in octets]
    return '.'.join(binary_octets)

def binary_to_decimal(ip_binary):
    """Конвертирует двоичный IP в десятичный"""
    binary_octets = ip_binary.split('.')
    decimal_octets = [str(int(octet, 2)) for octet in binary_octets]
    return '.'.join(decimal_octets)

def validate_ip(ip_str, is_binary=False):
    """Валидирует IP-адрес"""
    octets = ip_str.split('.')
    
    if len(octets) != 4:
        return False, "IP-адрес должен содержать 4 октета, разделенных точками."
    
    for octet in octets:
        if is_binary:
            if len(octet) != 8 or not all(c in '01' for c in octet):
                return False, "Каждый двоичный октет должен состоять из 8 бит (0 или 1)."
        else:
            if not octet.isdigit():
                return False, "Октеты должны быть целыми числами."
            num = int(octet)
            if num < 0 or num > 255:
                return False, "Неверный формат IP-адреса. Каждый октет должен быть от 0 до 255."
    
    return True, ""

def main():
    print("Программа для конвертации IP-адресов между десятичным и двоичным представлением")
    
    while True:
        print("\nВыберите режим работы:")
        print("1 - Десятичный IP в двоичный")
        print("2 - Двоичный IP в десятичный")
        print("0 - Выход")
        
        choice = input("> ").strip()
        
        if choice == '0':
            print("Выход из программы.")
            break
        elif choice == '1':
            ip_decimal = input("\nВведите IP-адрес в десятичном формате (например 192.168.1.1): ").strip()
            valid, message = validate_ip(ip_decimal)
            
            if not valid:
                print(f"Ошибка: {message}")
                continue
                
            binary_ip = decimal_to_binary(ip_decimal)
            print(f"\nДвоичное представление: {binary_ip}")
            
        elif choice == '2':
            ip_binary = input("\nВведите IP-адрес в двоичном формате (например 11000000.10101000.00000001.00000001): ").strip()
            valid, message = validate_ip(ip_binary, is_binary=True)
            
            if not valid:
                print(f"Ошибка: {message}")
                continue
                
            decimal_ip = binary_to_decimal(ip_binary)
            print(f"\nДесятичное представление: {decimal_ip}")
            
        else:
            print("Неверный выбор. Пожалуйста, введите 1, 2 или 0.")

if __name__ == "__main__":
    main()