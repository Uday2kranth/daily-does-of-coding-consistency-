# import asyncio
# from playsound import playsound

# async def play_after(delay, path):
#     await asyncio.sleep(delay)
#     loop = asyncio.get_running_loop()
#     await loop.run_in_executor(None, playsound, path)

# async def main():
#     tasks = [
#         asyncio.create_task(play_after(0, r"C:\...\sweep.wav")),
#         asyncio.create_task(play_after(20, r"C:\...\beep_440.wav")),
#     ]
#     await asyncio.gather(*tasks)

# if __name__ == "__main__":
#     asyncio.run(main())
import asyncio
from playsound import playsound

async def play_after(delay, path):
    await asyncio.sleep(delay)
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, playsound, path)

async def main():
    await play_after(0, r"C:\Users\uday2\Desktop\vs code\anu radha mam\sweep.wav")
    await play_after(20, r"C:\Users\uday2\Desktop\vs code\anu radha mam\beep_440.wav")

if __name__ == "__main__":
    asyncio.run(main())