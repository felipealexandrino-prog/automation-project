import requests

requisition = requests.get("https://jsonplaceholder.typicode.com/posts")
actual_data = requisition.json()

target_user = 2
count = 0

for line in actual_data:
    if line['userId'] == target_user:
        print(f"Título: XXXXXXXX\n")
        print(f"POST\n{line['body']}\n")
        count += 1

print(f"O usuário {target_user} fez {count} posts!")

with open("posts_user2", "w") as archive:
    for line in actual_data:
        if line['userId'] == target_user:
            archive.write(f"TItulo {line['title']}\n")
            archive.write(f"ID DO POST -> {line['id']}\n")