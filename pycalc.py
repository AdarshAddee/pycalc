

while True:
	
	print("\n\n\033[3;31;40m<================================================================ Welcome In PyCalc =================================================================>\n\n")
	
	print(" \033[1;36;40m[1] Add")
	print(" \033[1;32;40m[2] Subtract")
	print(" \033[1;33;40m[3] Multiply")
	print(" \033[1;34;40m[4] Divide")
	print(" \033[1;35;40m[5] Remainder")
	print(" \033[1;37;40m[6] Quotient")
	print(" \033[1;31;40m[99] Exit")
	
	print("\n\033[1;33;40mEnter Your Choice")
	user_ch = int(input("\033[1;33;40mAD4rSH_> "))
	
	if user_ch == 1:
		
		print("\n\033[1;36;40mEnter Your First Value:")
		num1 = float(input("\033[1;36;40mAD4rSH_> "))
		print("\033[1;36;40mEnter Your Second Value:")
		num2 = float(input("\033[1;36;40mAD4rSH_> "))
	
		result = num1 + num2
		print(f"\n\033[1;36;40mThe Addition Of {num1} and {num2} is {result}")
		
	elif user_ch == 2:
		
		print("\n\033[1;36;40mEnter Your First Value:")
		num1 = float(input("\033[1;36;40mAD4rSH_> "))
	
		print("\033[1;36;40mEnter Your Second Value:")
		num2 = float(input("\033[1;36;40mAD4rSH_> "))
		
		result = num1 - num2
		print(f"\n\033[0;32;40mThe Subtraction Of {num1} and {num2} is {result}")
		
	elif user_ch == 3:
		
		print("\n\033[1;36;40mEnter Your First Value:")
		num1 = float(input("\033[1;36;40mAD4rSH_> "))
		print("\033[1;36;40mEnter Your Second Value:")
		num2 = float(input("\033[1;36;40mAD4rSH_> "))
		
		result = num1 * num2
		print(f"\n\033[1;33;40mThe Multiplication Of {num1} and {num2} is {result}")
		
	elif user_ch == 4:
		
		print("\n\033[1;36;40mEnter Your First Value:")
		num1 = float(input("\033[1;36;40mAD4rSH_> "))
		print("\033[1;36;40mEnter Your Second Value:")
		num2 = float(input("\033[1;36;40mAD4rSH_> "))
		
		result = num1 / num2
		print(f"\n\033[1;34;40mThe Division Of {num1} and {num2} is {result}")	
		
	elif user_ch == 5:
		
		print("\n\033[1;36;40mEnter Your First Value:")
		num1 = float(input("\033[1;36;40mAD4rSH_> "))
		print("\033[1;36;40mEnter Your Second Value:")
		num2 = float(input("\033[1;36;40mAD4rSH_> "))
		
		result = num1 % num2
		print(f"\n\033[1;35;40mThe Remainder Of {num1} and {num2} is {result}")	
		
	elif user_ch == 6:
		
		print("\n\033[1;36;40mEnter Your First Value:")
		num1 = float(input("\033[1;36;40mAD4rSH_> "))
		print("\033[1;36;40mEnter Your Second Value:")
		num2 = float(input("\033[1;36;40mAD4rSH_> "))
		
		result = num1 // num2
		print(f"\n\033[1;37;40mThe Quotient Of {num1} and {num2} is {result}")	
	
	elif user_ch == 99:
		print("\n\033[1;31;40mBye - Bye, See You Again\n")
		break
	
	else:
		print("Please Enter A Valid Value ~~")
	
	
	
	
	
	
	