from celery_task import send_email


result = send_email.delay("yuan")
print(f"result.id: {result.id}")

result2 = send_email.delay("alex")
print(f"result2.id: {result2.id}")
