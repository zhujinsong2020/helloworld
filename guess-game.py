 # 猜数字小游戏
  import random

  print("=" * 30)
  print("  欢迎来到猜数字游戏！")
  print("=" * 30)

  number = random.randint(1, 100)
  count = 0

  while True:
      guess = int(input("请猜一个 1-100 的数字："))
      count += 1

      if guess < number:
          print("太小了！再试试～")
      elif guess > number:
          print("太大了！再试试～")
      else:
          print(f"恭喜你！猜对了！数字就是 {number}")
          print(f"你一共猜了 {count} 次")
          break