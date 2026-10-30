
from app.model import get_model

model = get_model()

response = model.invoke(
    "Explain RAG in simple English in three sentences."
)

print("Response type:", type(response))
print("Response content:", repr(response.content))
print("Full response:", response)
