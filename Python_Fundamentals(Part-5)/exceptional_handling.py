try:
    x = int(input("Enter the no:"))
    ans = 10/x

#*except ZeroDivisionError:
#*except:

except Exception as e:
    print(e) #*To print particular error

else:
    print(f"ans: {ans}")

finally:
    print("ankita")