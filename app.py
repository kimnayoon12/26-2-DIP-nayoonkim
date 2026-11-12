import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import scipy.ndimage as nd
from PIL import Image

# 페이지 설정
st.set_page_config(
    page_title="Medical Image Object Counting",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Medical Image Object Counting App")
st.markdown("`hw05.ipynb`에서 구현한 알고리즘을 바탕으로 이미지를 업로드하여 Object를 카운트하고 분석하는 웹 앱입니다.")

st.divider()

# 사이드바 설정 (파라미터 조절)
st.sidebar.header("⚙️ 처리 설정 (Parameters)")
med_kernel = st.sidebar.slider("Median Filter Kernel Size", min_value=3, max_value=15, value=7, step=2)
th_val = st.sidebar.slider("Threshold Value", min_value=0, max_value=255, value=190, step=1)

# 파일 업로더
uploaded_file = st.file_uploader("이미지 파일을 업로드하세요 (JPG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 1. 이미지 불러오기 및 그레이스케일 변환
    image = Image.open(uploaded_file).convert('L')
    f = np.array(image)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Input Image (Grayscale)")
        fig, ax = plt.subplots()
        ax.imshow(f, cmap='gray')
        ax.axis('off')
        st.pyplot(fig)
        
    # 2. 전처리 (Median Filtering)
    f_denoised = signal.medfilt2d(f, med_kernel)
    
    with col2:
        st.subheader("2. Denoised Image")
        fig, ax = plt.subplots()
        ax.imshow(f_denoised, cmap='gray')
        ax.axis('off')
        st.pyplot(fig)
        
    st.divider()
    
    # 3. 픽셀 강도 히스토그램 및 Thresholding
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("3. Pixel Intensity Histogram")
        fig, ax = plt.subplots()
        ax.hist(f_denoised.ravel(), bins=256, range=(0, 256), color='gray')
        ax.axvline(th_val, color='red', linestyle='--', label=f'Threshold: {th_val}')
        ax.set_xlabel('Pixel Intensity')
        ax.set_ylabel('Frequency')
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.5)
        st.pyplot(fig)
        
    # Thresholding을 통한 binary mask 생성
    f_mask = f_denoised > th_val
    
    with col4:
        st.subheader("4. Binary Mask")
        fig, ax = plt.subplots()
        ax.imshow(f_mask, cmap='gray')
        ax.axis('off')
        st.pyplot(fig)
        
    st.divider()
    
    # 4. Connected Component 추출 및 분석
    st.subheader("5. Connected Component Analysis & Object Counting")
    labels, nums = nd.label(f_mask)
    
    col5, col6 = st.columns(2)
    with col5:
        fig, ax = plt.subplots()
        ax.imshow(labels, cmap='Spectral_r')
        ax.axis('off')
        ax.set_title(f"Total Objects Found: {nums - 1}")
        st.pyplot(fig)
        
    # 각 컴포넌트 픽셀 수 계산
    if nums > 1:
        cc = np.zeros((nums - 1, 2))
        for i in range(1, nums):
            cc[i - 1, 0] = i
            cc[i - 1, 1] = np.sum(labels == i)
            
        ind_max = np.argmax(cc[:, 1])
        ind_min = np.argmin(cc[:, 1])
        
        with col6:
            st.markdown(f"### 📊 분석 결과 요약")
            st.info(f"**총 감지된 Object 수:** {nums - 1}개")
            st.success(f"**가장 큰 Component (Index {int(cc[ind_max, 0])}):** 픽셀 수 {int(cc[ind_max, 1])}개")
            st.warning(f"**가장 작은 Component (Index {int(cc[ind_min, 0])}):** 픽셀 수 {int(cc[ind_min, 1])}개")
            
        # 5. 가장 큰 것과 가장 작은 것 시각화
        st.markdown("### 🏆 가장 큰 객체 vs 가장 작은 객체 비교")
        fig, ax = plt.subplots(1, 3, figsize=(15, 5))
        
        ax[0].imshow(f, cmap='gray')
        ax[0].set_title('Input Image')
        ax[0].axis('off')
        
        ax[1].imshow(labels == cc[ind_max, 0], cmap='Spectral_r')
        ax[1].set_title(f'Largest (Idx: {int(cc[ind_max, 0])})')
        ax[1].axis('off')
        
        ax[2].imshow(labels == cc[ind_min, 0], cmap='Spectral_r')
        ax[2].set_title(f'Smallest (Idx: {int(cc[ind_min, 0])})')
        ax[2].axis('off')
        
        st.pyplot(fig)
    else:
        st.warning("감지된 객체가 없습니다. 임계값(Threshold)을 조절해 보세요.")
else:
    st.info("👆 사이드바에서 설정을 확인하고, 분석할 이미지를 업로드해 주세요.")
