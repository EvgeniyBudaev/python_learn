def make_divider_of(divider):

    def division_operation(divisible):
        return divisible / divider
    return division_operation


div2 = make_divider_of(2)
print(div2(10))

# div5 = make_divider_of(5)
# print(div5(20))

# print(div5(div2(20)))