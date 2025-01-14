{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Factorial of 10 is: 3628800\n"
     ]
    }
   ],
   "source": [
    "import threading\n",
    "\n",
    "# Hàm tính giai thừa cho một khoảng số\n",
    "def factorial_partial(start, end, result, index):\n",
    "    partial_result = 1\n",
    "    for num in range(start, end + 1):\n",
    "        partial_result *= num\n",
    "    result[index] = partial_result\n",
    "\n",
    "# Hàm chính để tính giai thừa\n",
    "def calculate_factorial(number, num_threads):\n",
    "    if number == 0 or number == 1:\n",
    "        return 1\n",
    "\n",
    "    # Chia công việc thành các phần\n",
    "    step = number // num_threads\n",
    "    threads = []\n",
    "    results = [1] * num_threads\n",
    "\n",
    "    # Tạo và bắt đầu các luồng\n",
    "    for i in range(num_threads):\n",
    "        start = i * step + 1\n",
    "        end = (i + 1) * step if i != num_threads - 1 else number\n",
    "        thread = threading.Thread(target=factorial_partial, args=(start, end, results, i))\n",
    "        threads.append(thread)\n",
    "        thread.start()\n",
    "\n",
    "    # Chờ tất cả luồng hoàn thành\n",
    "    for thread in threads:\n",
    "        thread.join()\n",
    "\n",
    "    # Nhân các kết quả từ các luồng\n",
    "    factorial = 1\n",
    "    for partial_result in results:\n",
    "        factorial *= partial_result\n",
    "\n",
    "    return factorial\n",
    "\n",
    "# Hàm chính để chạy chương trình\n",
    "def main():\n",
    "    number = 10  # Số cần tính giai thừa\n",
    "    num_threads = 3  # Số luồng\n",
    "\n",
    "    result = calculate_factorial(number, num_threads)\n",
    "    print(f\"Factorial of {number} is: {result}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}