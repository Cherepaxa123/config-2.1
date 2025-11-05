import sys

package = None;
url = None;
test_mode = None;

i = 1;
while i < len(sys.argv):
    if sys.argv[i] == '--package' and i + 1 < len(sys.argv):
        package = sys.argv[i+1];
        i += 2;
    elif sys.argv[i] == '--url' and i + 1 < len(sys.argv):
        url = sys.argv[i+1];
        i += 2;
    elif sys.argv[i] == '--test_mode':
        test_mode = True
        i += 1;
    else:
        i += 1
errors = []

if not package:
    errors.append("Не указан --package")
elif not package.strip():
    errors.append("Имя пакета не может быть пустым")

if not url:
    errors.append("Не указан --url")
elif not url.strip():
    errors.append("URl/ путь не может быть пустым")

if errors:
    print("Ошибки: ")
    for error in errors:
        print(" -" + error)
    sys.exit(1)

print("Параметры конфигурации: ")
print(" package: " + package)
print(" url: " + url)
print(" test_mode: " + str(test_mode))

print("\n Запуск анализа пакета" + package + " " + "\n")