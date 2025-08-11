


class utils:

    def getting_vat (self,price):
        print(f"Getting VAT for {price}")
        new_price= price.replace("$","")
        new_price_as_int= int(new_price)
        new_price_final= new_price_as_int * 1.18
        print(f"the final price is {new_price_final}")
        return new_price_final


    def add_suffix(self , price,rate):
        price= price*rate
        price_as_str = str(price)
        new_price = price_as_str+"ILS"
        print(f"the price is {new_price}")


    def avarage(self,num_1,num_2):
        avg_new_price = (num_1 + num_2)/2
        return avg_new_price


    def print_between_numbers(self,num1,num2):
        if (num1 >num2):
            low = num2
            high = num1
        else:
            low = num1
            high = num2

        for num in range(low,high):
            print(f"{num}")


    def avg_of_list(self,numbers):
        sum_of_num = 0
        for num in numbers:
            len_of_list= len(numbers)
            sum_of_num= sum(numbers)
            avg_of_num= (sum_of_num/len_of_list)
            break

        print(f"the avg is: {avg_of_num}")
        return avg_of_num ,len_of_list


    def sum_of_list(self,numbers):
        total_sum = sum(numbers)
        print(f"the total sum is: {total_sum}")


    def list_of_string(self,names):
        longest_name=0
        list_of_longest = []
        for name in names:
            len_name = len(name)
            if (len_name > longest_name):
                longest_name = len_name
                the_bigger_name = name
        for name in names:
                len_name = len(name)
                if (longest_name == len_name ):
                    list_of_longest.append(name)
        print(f"the longest name is:{list_of_longest} ({longest_name})")


    def list_of_age(self,numbers):
        for age in numbers:
            if (0<= age <=18):
                print(f"{age} is child")
            elif (19<= age <=60):
                print(f"{age} is adult")
            elif (61<= age <=120):
                print(f"{age} is senior")
            else:
                print(f"{age} is error")