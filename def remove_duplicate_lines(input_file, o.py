def remove_duplicate_lines(input_file, output_file):
   
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    
    unique_lines = set(lines)

    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(sorted(unique_lines))

    print(f"تم إزالة الأسطر المتكررة وتم حفظ النتيجة في {output_file}")


input_file = "C:/Users/Ttawi/Desktop/QRRR!/QR-codes.txt"  
output_file = "C:/Users/Ttawi/Desktop/QRRR!/result.txt"  
remove_duplicate_lines(input_file, output_file)
