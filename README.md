# Minecraft Biome Classification

![Minecraft Biome Classification](https://github.com/Grandher/Minecraft-biome-classification_python/blob/main/images/1.jpg)

## О проекте

Minecraft Biome Classification - это проект по мультиклассификации биомов из игры Minecraft. Модель была обучена с использованием библиотеки PyTorch на датасете, содержащем 40 тысяч скриншотов игры. Программа способна определить тип биома на загруженном в неё скриншоте, будь то тайга, лес, пустыня и другие.

## Визуальный интерфейс

Для удобства пользователей был разработан визуальный интерфейс при помощи библиотеки Streamlit. Простота использования и интуитивный дизайн делают взаимодействие с программой легким и приятным.

Посмотрите [рабочий пример здесь](https://minecraft-biome-classification.streamlit.app/).

![Example](https://github.com/Grandher/Minecraft-biome-classification_python/blob/main/images/4.png)

## Результаты и метрики

Модель продемонстрировала высокую точность на тестовом наборе данных. На третьем изображении представлены следующие метрики точности:
- Общая точность: 58%
- Точность на популярных классах: 98%
- Время инференса на процессоре: 0.03 секунды
- Время инференса на видеокарте: 0.019 секунд

![Metrics](https://github.com/Grandher/Minecraft-biome-classification_python/blob/main/images/3.jpg)

## Запуск локально

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/your-username/minecraft-biome-classification.git
    ```

2. Установите необходимые зависимости:

    ```bash
    pip install -r requirements.txt
    ```

3. Запустите программу:

    ```bash
    streamlit run app.py
    ```

Теперь вы можете открыть браузер и перейти по адресу [http://localhost:8501](http://localhost:8501), чтобы воспользоваться программой локально.
