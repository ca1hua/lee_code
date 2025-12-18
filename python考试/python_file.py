class Solution():
    def solve(self, file_1, file_2, file_3):
        '''
        :type file_1, file_2, file_3: str
        :rtype : None
        '''
        # Read the numbers from file_1 and file_2
        with open(file_1, 'r') as f1:
            numbers_1 = list(map(int, f1.read().split()))

        with open(file_2, 'r') as f2:
            numbers_2 = list(map(int, f2.read().split()))

        # Combine the numbers from both files
        all_numbers = numbers_1 + numbers_2

        # Sort the numbers in ascending order
        all_numbers.sort()

        # Write the sorted numbers into file_3
        with open(file_3, 'w') as f3:
            f3.write('\n'.join(map(str, all_numbers)))

