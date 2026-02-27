# mini siem tool

a beginner-friendly python project that simulates how a security information and event management (siem) system works at a basic level.

## what it does
- reads through system log files
- detects failed login attempts
- flags accounts with multiple failed logins as potential brute force attacks
- counts successful vs failed login attempts
- outputs a clean summary report

## why i built this
siem tools are used by security analysts every day to monitor systems and detect threats. this project helped me understand the core logic behind log analysis and threat detection.

## usage
```bash
python bruteforce.py
```

## technologies used
- python 3
- file i/o and string parsing
- collections module (counter)

## disclaimer
this project is for educational purposes only.
