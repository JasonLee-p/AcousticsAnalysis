from path_lib import *
import torchaudio
import matplotlib.pyplot as plt


def show_audio(audio_path):
    if not audio_path.exists():
        raise FileNotFoundError(f"音频文件不存在: {audio_path}")
    # 加载音频文件
    waveform, sample_rate = torchaudio.load(audio_path)

    # 打印音频信息
    print("Waveform shape:", waveform.shape)
    print("Sample rate:", sample_rate)

    # 生成频谱图
    spectrogram_transform = torchaudio.transforms.Spectrogram()
    spectrogram = spectrogram_transform(waveform)

    # 打印频谱图形状
    print("Spectrogram shape:", spectrogram.shape)

    # 转换频谱图为2D numpy数组（适用于单声道音频）
    spectrogram = spectrogram[0].numpy()

    # 绘制频谱图
    plt.figure(figsize=(10, 4))
    plt.imshow(spectrogram, cmap='viridis', aspect='auto', origin='lower')
    plt.title('频谱图')
    plt.ylabel('频率/Hz')
    plt.xlabel('时间/s')
    plt.colorbar(label='强度/dB')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    show_audio(PATH_RAW_AUDIO / "PanYunGuoCui.wav")
