HIGHEST_SIDE_LENGTH = 2 ** 31

def main():
    t_case = int(input())
    
    for i in range(t_case):
        n_cube = int(input())
        sides = list(map(lambda x: int(x), input().split()))
        
        # print(n_cube)
        # print(sides)
        
        i_top = 0
        i_bottom = n_cube - 1
        s_top = HIGHEST_SIDE_LENGTH
        
        result = "Yes"
        
        while i_top <= i_bottom:
            # print(sides[i_top], sides[i_bottom])
            choice = 0
            if sides[i_top] >= sides[i_bottom]:
                choice = sides[i_top]
                i_top += 1
            else: # sides[i_top] < sides[i_bottom]
                choice = sides[i_bottom]
                i_bottom -= 1
            
            # print(choice)
            
            if choice > s_top:
                result = "No"
                break;
            
            s_top = choice
            

        print(result)
    

if __name__ == "__main__":
    main()
