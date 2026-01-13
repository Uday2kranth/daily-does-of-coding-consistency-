import os
import math
import wave
import struct
import time

SAMPLE_RATE = 44100

def write_wav(filename, samples, sample_rate=SAMPLE_RATE):
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        frames = b''.join(struct.pack('<h', int(max(-32767, min(32767, int(s * 32767))))) for s in samples)
        wf.writeframes(frames)

def sine_wave(freq, duration, volume=0.5, sample_rate=SAMPLE_RATE):
    length = int(duration * sample_rate)
    return [volume * math.sin(2 * math.pi * freq * (i / sample_rate)) for i in range(length)]

def chord(freqs, duration, volume=0.5, sample_rate=SAMPLE_RATE):
    length = int(duration * sample_rate)
    samples = []
    for i in range(length):
        t = i / sample_rate
        s = sum(math.sin(2 * math.pi * f * t) for f in freqs)
        samples.append(volume * (s / len(freqs)))
    return samples

def sweep(f_start, f_end, duration, volume=0.5, sample_rate=SAMPLE_RATE):
    length = int(duration * sample_rate)
    samples = []
    for i in range(length):
        t = i / sample_rate
        frac = i / (length - 1)
        freq = f_start + (f_end - f_start) * frac
        samples.append(volume * math.sin(2 * math.pi * freq * t))
    return samples

def mix(samples_list):
    length = max(len(s) for s in samples_list)
    out = []
    for i in range(length):
        s = 0.0
        for arr in samples_list:
            if i < len(arr):
                s += arr[i]
        out.append(s / len(samples_list))
    return out

def main():
    out_dir = os.path.abspath('.')
    files = []

    # simple beeps
    f1 = os.path.join(out_dir, 'beep_440.wav')
    write_wav(f1, sine_wave(440, 0.7, volume=0.6))
    files.append(('A4 440Hz', f1))

    f2 = os.path.join(out_dir, 'beep_660.wav')
    write_wav(f2, sine_wave(660, 0.7, volume=0.6))
    files.append(('E5 660Hz', f2))

    # chord
    f3 = os.path.join(out_dir, 'chord_C_major.wav')
    write_wav(f3, chord([261.63, 329.63, 392.00], 1.0, volume=0.6))
    files.append(('C major chord', f3))

    # sweep
    f4 = os.path.join(out_dir, 'sweep.wav')
    write_wav(f4, sweep(300, 1200, 1.2, volume=0.6))
    files.append(('Frequency sweep', f4))

    print('Generated files:')
    for name, path in files:
        print(f' - {name}: {path}')

    # Try to play using playsound; if not available, try winsound (Windows only)
    try:
        from playsound import playsound
    except Exception as e:
        print('\nplaysound import failed:', e)
        try:
            import winsound
        except Exception as e2:
            print('winsound not available either. To hear the files, open them directly in a media player.')
            return
        else:
            print('\nUsing winsound fallback (Windows).')
            for name, path in files:
                print(f'Playing {name} -> {path}')
                winsound.PlaySound(path, winsound.SND_FILENAME)
            return

    print('\nUsing playsound to play samples.')
    for name, path in files:
        print(f'Playing {name} -> {path}')
        try:
            playsound(path)
        except Exception as e:
            print('playsound failed for', path, '->', e)


if __name__ == '__main__':
    main()
