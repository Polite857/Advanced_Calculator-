import math #Polite出生以来的第二个Python脚本 正式发布日期2025-08-15 BJT 02:41:37
print("高级计算器 v1.00")
计算模式 = input("请输入计算模式：\n加法为+\n减法为-\n乘法为*\n除法为/\n取余为#\n平方根√\n")
if 计算模式 == "+":
    print("您选择的计算模式为加法")
else:
        if 计算模式 == "-":
            print("您选择的计算模式为减法")
        else:
            if 计算模式 == "*":
                 print("您选择的计算模式为乘法")
            else:
                        if 计算模式 == "/":
                            print("您选择的计算模式为除法")
                        else:
                            if 计算模式 == "#":
                                print("您选择的计算模式为取余")
                            else:
                                if 计算模式 == "√":
                                    print("您选择的计算模式为平方根")
                                else:
                                    print("输入计算模式非法")
                                    input("按回车重新启动程序")
                                    exit
if 计算模式 == "+":
    Num1= input("请输入第一个加数\n")
else:
        if 计算模式 == "-":
            Num1= input("请输入被减数\n")
        else:
            if 计算模式 == "*":
                 Num1= input("请输入第一个乘数\n")
            else:
                        if 计算模式 == "/":
                            Num1= input("请输入被除数\n")
                        else:
                            if 计算模式 == "#":
                                Num1= input("请输入被除数\n")
                            else:
                                if 计算模式 == "√":
                                   Num1= input("请输入开方数\n")
                                else:
                                    input("输入计算模式非法")
                                    input("按回车重新启动程序")
                                    exit
if 计算模式 == "+":
    Num2= input("请输入第二个加数\n")
else:
        if 计算模式 == "-":
            Num2= input("请输入减数\n")
        else:
            if 计算模式 == "*":
                 Num2= input("请输入第二个乘数\n")
            else:
                        if 计算模式 == "/":
                            Num2= input("请输入除数\n")
                        else:
                            if 计算模式 == "#":
                                Num2= input("请输入除数\n")
                            else:
                                if 计算模式 == "√":
                                    print("平方根已跳过第二个数字")
                                else:
                                    input("输入计算模式非法\n")
                                    input("按回车重新启动程序")
                                    exit
if 计算模式 == "+":
    结果 = int(Num1) + int(Num2)
    print("计算结果为" + str(结果))
    input("\n按回车重新启动程序")
    exit
else:
        if 计算模式 == "-":
            结果 = int(Num1) - int(Num2)
            print("计算结果为" + str(结果))
            input("\n按回车重新启动程序")
            exit
        else:
            if 计算模式 == "*":
                  结果 = int(Num1) * int(Num2)
                  print("计算结果为" + str(结果))
                  input("\n按回车重新启动程序")
                  exit
            else:
                if 计算模式 == "/":
                        结果 = int(Num1) / int(Num2)
                        print("计算结果为" + str(结果))
                        input("\n按回车重新启动程序")
                        exit
                else:
                        if 计算模式 == "#":
                                结果 = int(Num1) % int(Num2)
                                print("计算结果为" + str(结果))
                                input("\n按回车重新启动程序")
                                exit
                        else:
                            if 计算模式 == "√":
                                结果 = math.sqrt(int(Num1))
                                print("计算结果为" + str(结果))
                            else:
                                input("输入计算模式非法")
                                input("按回车重新启动程序")
                                exit