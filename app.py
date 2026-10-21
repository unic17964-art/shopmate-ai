
import streamlit as st

st.set_page_config(page_title="ShopMate AI", page_icon="🛍️")

st.title("🛍️ ShopMate AI")
st.write("Your small-business assistant")

st.info("Demo mode: sample shop data only.")

st.subheader("📦 Inventory")

inventory = {
    "Pen": {"price": 50, "stock": 20},
    "Notebook": {"price": 150, "stock": 12},
    "School Bag": {"price": 800, "stock": 5},
    "Water Bottle": {"price": 250, "stock": 3},
}

for name, item in inventory.items():
    st.write(
        f"**{name}** — Rs. {item['price']} | "
        f"Stock: {item['stock']} units"
    )

st.subheader("💬 Ask ShopMate")
question = st.text_input("Ask about your inventory")

if question:
    q = question.lower()
    if "low" in q or "restock" in q:
        low = [
            f"{name}: {item['stock']} left"
            for name, item in inventory.items()
            if item["stock"] <= 5
        ]
        st.write("Products needing restock: " + ", ".join(low))
    elif "stock" in q or "inventory" in q:
        st.write("Your current inventory is listed above.")
    else:
        st.write(
            "Try asking: Which products are low stock?"
        )
      
