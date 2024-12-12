def remove_duplicate_lines(input_file, output_file):
    # فتح الملف للقراءة
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # إزالة الأسطر المكررة باستخدام مجموعة
    unique_lines = set(lines)

    # فتح الملف للإخراج وكتابة الأسطر الفريدة
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(sorted(unique_lines))

    print(f"تم إزالة الأسطر المتكررة وتم حفظ النتيجة في {output_file}")

# استخدام الوظيفة
input_file = "C:/Users/Ttawi/Desktop/QRRR!/QR-codes.txt"  # استبدل بالمسار الصحيح للملف النصي
output_file = "C:/Users/Ttawi/Desktop/QRRR!/result.txt"  # استبدل بالمسار الذي تريد حفظ الملف الناتج فيه
remove_duplicate_lines(input_file, output_file)
