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
      "Hello from thread: Thread-1\n",
      "Hello from thread: Thread-2\n",
      "Hello from thread: Thread-3\n",
      "Hello from thread: Thread-4\n",
      "Hello from thread: Thread-5\n",
      "All threads have finished.\n"
     ]
    }
   ],
   "source": [
    "import threading\n",
    "\n",
    "def print_thread_name():\n",
    "    print(f\"Hello from thread: {threading.current_thread().name}\")\n",
    "\n",
    "threads = []\n",
    "\n",
    "num_threads = 5\n",
    "for i in range(num_threads):\n",
    "    thread = threading.Thread(target=print_thread_name, name=f\"Thread-{i+1}\")\n",
    "    threads.append(thread)\n",
    "    thread.start()\n",
    "\n",
    "# Đợi tất cả các luồng kết thúc\n",
    "for thread in threads:\n",
    "    thread.join()\n",
    "\n",
    "print(\"All threads have finished.\")\n"
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