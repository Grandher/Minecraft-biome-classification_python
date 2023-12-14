import streamlit as st
from PIL import Image
import torch
from torchvision import transforms
from MinecraftModel import MinecraftModel

# Загрузка модели
model_save_path = "minecraft_model.pth" 
num_classes = 41  # Количество классов
model = MinecraftModel(num_classes)
model.load_state_dict(torch.load(model_save_path, map_location='cpu'))
model.eval()

# Функция классификации изображения
def classify_image(image):
    image = transforms.Resize((180, 360))(image)
    image = transforms.ToTensor()(image)
    image = image.unsqueeze(0)
    with torch.no_grad():
        output = model(image)
    _, predicted_class = torch.max(output, 1)
    return predicted_class.item()

st.set_page_config(
    page_title="Minecraft Biome Classifier",
    page_icon="icon.ico",
)

st.title("Minecraft Biome Classifier")

# Загрузка изображения
uploaded_image = st.file_uploader("Выберите изображение", type=["jpg", "jpeg", "png"])

# Названия классов
biome_names = ["beach","birch_forest","birch_forest_hills","birch_forest_hills_mutated","cold_beach","cold_taiga","cold_taiga_hills",
                   "cold_taiga_mutated","deep_cold_ocean","desert","desert_hills","desert_mutated","extreme_hills","extreme_hills_mutated",
                   "extreme_hills_plus_trees","extreme_hills_plus_trees_mutated","flower_forest","forest","forest_hills","frozen_river",
                   "ice_mountains","ice_plains","jungle","jungle_hills","legacy_frozen_ocean","mega_taiga","mega_taiga_hills","mesa","mesa_plateau",
                   "mesa_plateau_stone","plains","river","roofed_forest","roofed_forest_mutated","savanna","savanna_plateau","sunflower_plains",
                   "swampland","taiga","taiga_hills","taiga_mutated"]

if uploaded_image is not None:
    # Отображение изображения
    image = Image.open(uploaded_image)
    st.image(image, caption="Загруженное изображение", use_column_width=True)

    # Классификация изображения
    class_index = classify_image(image)
    st.write("Предполагаемый биом:", biome_names[class_index])
