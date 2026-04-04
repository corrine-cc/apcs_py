while True:
    try:

        line = input()
        if not line:
            break
        n = int(line)
        
        result = ""
        

        for i in range(n):
  
            code = input().replace(" ", "")
       
            if "0101" in code:
                result += "A"
            elif "0111" in code:
                result += "B"
            elif "0010" in code:
                result += "C"
            elif "1101" in code:
                result += "D"
            elif "1000" in code:
                result += "E"
            elif "1100" in code:
                result += "F"
                

        print(result)
        
    except EOFError:
        break
