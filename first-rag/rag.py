import requests

def query_gemma(prompt):
    url = "http://192.168.1.149:11434/api/generate"
    payload = {
        "model": "gemma3:12b",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data.get('response', 'no response in JSON')
    except requests.exceptions.ConnectionError:
        return "❌ لم يتم الاتصال بالخادم، تحقق من عنوان IP أو تشغيل النموذج."
    except requests.exceptions.Timeout:
        return "⌛ انتهت مهلة الاتصال بالخادم."
    except requests.exceptions.HTTPError as e:
        return f"⚠️ خطأ في الطلب: {e}"
    except ValueError:
        return "⚠️ الاستجابة ليست بصيغة JSON صالحة."

while True:
    user_input = input ("أكتب سؤالك بالعربية أو أكتب خروج للإنها البرنامج: ")
    if user_input.lower() == "خروج":
        print("تم إنهاء البرنامج.")
        break
    response = query_gemma(user_input)
    print(f"الرد: {response}")
    print("--------------------------------------------------") 
    
    # this Code make log file gemmai_arabic_log .
    with open("logs/arabic_gemma_log.txt","a",encoding="utf-8") as log_file:
        log_file.write(f"سؤال: {user_input}\n")
        log_file.write(f"رد: {response}\n")
        log_file.write("--------------------------------------------------\n")