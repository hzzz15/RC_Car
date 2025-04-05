import os
import cv2
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

IMG_SIZE = 64
input_dir = "./processed_images"  # 폴더 경로
label_map = {"left": 0, "right": 1, "straight": 2}

X, y = [], []

for fname in os.listdir(input_dir):
    if fname.endswith(".png"):
        for label in label_map:
            if fname.startswith(label):
                path = os.path.join(input_dir, fname)
                img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                if img is None:
                    continue
                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
                X.append(img)
                y.append(label_map[label])
                break

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1) / 255.0
y = to_categorical(np.array(y), num_classes=len(label_map))

# 데이터 분리
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# CNN 모델 정의
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 1)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(len(label_map), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 학습
model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

# 모델 저장
model.save("cnn_model.h5")
print("모델 저장 완료: cnn_model.h5")
