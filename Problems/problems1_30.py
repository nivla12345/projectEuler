__author__ = 'Alvin'
import math
import Tools

## The problems that aren't in here were simple enough to do in the python command line.

# Find the sum of all multiples of 3 or 5 below 1000
def p1():
    # Less than 1000 hence 999
    upper_limit = 999
    # Using the sum exclusion principle
    sum_5_multiples = 5*Tools.summation(upper_limit/5)
    sum_3_multiples = 3*Tools.summation(upper_limit/3)
    # 3 * 5 gets double counted
    sum_15_multiples = 15*Tools.summation(upper_limit/15)
    return sum_5_multiples + sum_3_multiples - sum_15_multiples


# Sum all even fibonnacis below 4M
def p2():
    fib_sum = 0
    count = 3
    x = Tools.fibonacci(count)
    while x < 4000000:
        if x % 2 == 0:
            fib_sum += x
        count += 1
        x = Tools.fibonacci(count)
    return fib_sum


# Return the largest prime factor of: 600851475143
def p3():
    cons = 600851475143
    cons_sqrt = math.sqrt(cons)
    largest_prime_root = 1
    for i in xrange(3, int(cons_sqrt + 1), 2):
        if cons % i == 0:
            larger_root = cons / i
            if Tools.is_prime(larger_root):
                return larger_root
            if Tools.is_prime(i):
                largest_prime_root = i
    return largest_prime_root


# Return the largest palindrome that is the product of 2 3-digit numbers
def p4():
    largest_palindrome = 999
    for i in xrange(999, 1, -1):
        for j in xrange(999, i, -1):
            product = i * j
            if Tools.is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
    return largest_palindrome


# Find the smallest # that is a multiple of [1, 20]
def p5():
    # 2, 4, 8, -> 16
    # 3        -> 9
    # 5        -> 5
    # 7        -> 7
    # 11       -> 11
    # 13       -> 13
    # 17       -> 17
    # 19       -> 19
    return 16 * 9 * 5 * 7 * 11 * 13 * 17 * 19


# Subtract the 100 square of sums from the 100 sum of squares
def p6():
    sum_of_squares = 0
    for i in xrange(1, 101):
        sum_of_squares += i * i
    return 5050 * 5050 - sum_of_squares


# Find the 10001st prime number
def p7():
    count = 1
    work_var = 3
    while count < 10001:
        if Tools.is_prime(work_var):
            count += 1
        work_var += 2
    return work_var - 2


# Find the largest product of 13 adjacent numbers
def p8():
    NUMBER = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
""".replace("\n", "")
    length = 1000
    product = 0
    for i in xrange(0, 987):
        number = NUMBER[i: i + 13]
        if not number.__contains__("0"):
            tmp_product = p8_sum13(number)
            if tmp_product > product:
                product = tmp_product
    return product


def p8_sum13(x):
    return int(x[0]) * \
           int(x[1]) * \
           int(x[2]) * \
           int(x[3]) * \
           int(x[4]) * \
           int(x[5]) * \
           int(x[6]) * \
           int(x[7]) * \
           int(x[8]) * \
           int(x[9]) * \
           int(x[10]) * \
           int(x[11]) * \
           int(x[12])


# Find a, b, and c s.t. a + b + c = 1000 where a^2 + b^2 = c^2
def p9():
    for c in xrange(998, 333, -1):
        a_plus_b = 1000 - c
        for b in xrange(1, a_plus_b, 1):
            a = a_plus_b - b
            if a * a + b * b == c * c:
                return a * b * c
    return 0


# Sum all the primes bellow 2000000
def p10():
    sum_of_primes = 2
    for i in xrange(3, 2000000, 2):
        if Tools.is_prime(i):
            sum_of_primes += i
    return sum_of_primes


# Given a 20x20 grid, find the largest product of 4 in a row
def p11():
    # Format grid
    GRID = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""
    arr = GRID.split()
    grid_arr = []
    for i in xrange(20):
        tmp_arr = []
        for j in xrange(20):
            tmp_arr.append(arr[i * 20 + j])
        grid_arr.append(tmp_arr)
    # Tools.print_grid(grid_arr)
    return iterate(grid_arr)


# Iterates 4 numbers: upper right, right, lower right, and down
# and returns the largest product
def iterate(grid):
    num_iter = 3
    grid_dim = 20
    product = 0
    for i in xrange(20):
        for j in xrange(20):
            right_past_edge = (j + num_iter) >= grid_dim
            top_past_edge = (i - num_iter) < 0
            bottom_past_edge = (i + num_iter) >= grid_dim
            # Upper right
            if not right_past_edge and not top_past_edge:
                right_top_product = string_grid_product(grid[i][j], grid[i - 1][j + 1], grid[i - 2][j + 2],
                                                        grid[i - 3][j + 3])
                if right_top_product > product:
                    product = right_top_product
            # Right
            if not right_past_edge:
                right_product = string_grid_product(grid[i][j], grid[i][j + 1], grid[i][j + 2], grid[i][j + 3])
                if right_product > product:
                    product = right_product
            # Lower right
            if not bottom_past_edge and not right_past_edge:
                bottom_right_prodcut = string_grid_product(grid[i][j], grid[i + 1][j + 1], grid[i + 2][j + 2],
                                                           grid[i + 3][j + 3])
                if bottom_right_prodcut > product:
                    product = bottom_right_prodcut
            # Down
            if not bottom_past_edge:
                bottom_product = string_grid_product(grid[i][j], grid[i - 1][j], grid[i - 2][j], grid[i - 3][j])
                if bottom_product > product:
                    product = bottom_product
    return product


# Takes the string product of 4 numbers
def string_grid_product(a, b, c, d):
    return int(a) * int(b) * int(c) * int(d)


# Find the first triangle number with > 500 divisors
def p12():
    nth_triangle_number = 1
    n = 1
    while Tools.num_divisors(nth_triangle_number) < 501:
        nth_triangle_number += (n + 1)
        n += 1
    return nth_triangle_number


def p13():
    large_number = """37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690"""
    sum_of_digits = 0
    for i in large_number.split('\n'):
        sum_of_digits += int(i)
    return str(sum_of_digits)


collatz_lengths = dict()


def p14():
    longest_length = 0
    largest_collatz_value = 0
    n = 1
    while (n < 1000000):
        n_collatz_length = collatz_length(n)
        if n_collatz_length > longest_length:
            longest_length = n_collatz_length
            largest_collatz_value = n
        n += 1
    return largest_collatz_value


def collatz_length(n):
    original_n = n
    length = 0
    # This dictionary tracks the temporary lengths of locals that were seen
    temp_collatz_lengths = dict()
    while n != 1:
        length += 1
        if n in collatz_lengths:
            # TODO: Iterate through temp_collatz_lengths and add to collatz_lengths
            for i in temp_collatz_lengths:
                collatz_lengths[i] = length - temp_collatz_lengths[i]
            collatz_lengths[original_n] = length
            return length + collatz_lengths[n]
        # TODO: Add to temp_collatz_lengths
        temp_collatz_lengths[n] = length
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    # TODO: Iterate through temp_collatz_lengths and add to collatz_lengths
    for i in temp_collatz_lengths:
        collatz_lengths[i] = length - temp_collatz_lengths[i]
    # Deposit into dictionary
    collatz_lengths[original_n] = length + 1
    return length


def p15():
    large_number = str(1 << 1000)
    sum_of_digits = 0
    for i in large_number:
        sum_of_digits += int(i)
    return sum_of_digits


def p16():
    number_to_string = {1: "one",
                        2: "two",
                        3: "three",
                        4: "four",
                        5: "five",
                        6: "six",
                        7: "seven",
                        8: "eight",
                        9: "nine",
                        10: "ten",
                        11: "eleven",
                        12: "twelve",
                        13: "thirteen",
                        14: "fourteen",
                        15: "fifteen",
                        16: "sixteen",
                        17: "seventeen",
                        18: "eighteen",
                        19: "nineteen",
                        20: "twenty",
                        30: "thirty",
                        40: "forty",
                        50: "fifty",
                        60: "sixty",
                        70: "seventy",
                        80: "eighty",
                        90: "ninety"}
    letter_length = 11  # includes 1000
    # 1-100
    one_to_hundred = 0
    # 1-9
    one_through_nine = 0
    for i in xrange(1, 10, 1):
        one_through_nine += len(number_to_string[i])
    for i in xrange(1, 20, 1):
        number_string = number_to_string[i]
        one_to_hundred += len(number_string)
    for i in xrange(20, 100, 10):
        one_to_hundred += 10*len(number_to_string[i])
    one_to_hundred += 8*one_through_nine
    print one_to_hundred
    # All the hundreds
    letter_length += 10*one_to_hundred
    letter_length += len("hundredand")*891
    letter_length += len("hundred")*9
    # All the hundred numbers
    for i in xrange(1, 10, 1):
        letter_length += 100*len(number_to_string[i])
    return letter_length


def p17():
    triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
    triangle_lines = triangle.split('\n')
    optimized_line = [int(triangle_lines[0])]
    for i in xrange(1, len(triangle_lines), 1):
        new_line = triangle_lines[i].split()
        # Construct leftmost element
        new_optimized_line = [int(new_line[0]) + optimized_line[0]]
        # Construct optimized_line
        for j in xrange(1, len(new_line)-1):
            left = optimized_line[j-1] + int(new_line[j])
            right = optimized_line[j] + int(new_line[j])
            new_optimized_line.append(max(left, right))
        new_optimized_line.append(int(new_line[-1]) + optimized_line[-1])
        optimized_line = new_optimized_line
    return max(optimized_line)


# How many sundays are there in January during the 20th century
# 1 Jan 1901 to 31 Dec 2000
def p18():
    # 1 Jan 1901 is Tuesday
    current_day = 0
    current_month = 0
    current_year = 1901
    num_sundays_in_january = 0
    current_day_of_week = 1
    while not (current_day == 30 and current_month == 11 and current_year == 2000):
        # Iterate over months
        for month in xrange(12):
            # Iterate over days in month
            days_in_month = Tools.days_in_month(month + 1, current_year)
            for day in xrange(days_in_month):
                if current_day_of_week == 0 and day == 0:
                    num_sundays_in_january += 1
                current_day_of_week = (current_day_of_week + 1) % 7
                current_day = day
            current_month = month
        current_year += 1
    return num_sundays_in_january


# Sum the digits of 100!
def p20():
    hundred_factorial = str(math.factorial(100))
    sum_digits = 0
    for i in hundred_factorial:
        sum_digits += int(i)
    return sum_digits


# Sum all amicable numbers < 10000
# Given function d(n) = m, where d is the sum of the divisors < n, d(m) == d(n) implies m and n are amicable numbers.
def p21():
    Tools.sum_amicable_numbers = 0
    seen_amicable_numbers = set()
    count = 1
    while count < 10000:
        if count in seen_amicable_numbers:
            count += 1
            continue
        sum_of_divisors = Tools.sum_divisors(count)
        d_of_sum_divisors = Tools.sum_divisors(sum_of_divisors)
        if count == d_of_sum_divisors:
            if count == sum_of_divisors:
                count += 1
                continue
            else:
                Tools.sum_amicable_numbers += (count + sum_of_divisors)
                seen_amicable_numbers.add(count)
                seen_amicable_numbers.add(sum_of_divisors)
        count += 1
    return Tools.sum_amicable_numbers


# Find the sum of all numbers < 28123 that are NOT the sum of 2 abundant numbers
def p23():
    """
    My algorithm goes as follows.

    1)
    The number of abundant numbers is probably less than the numbers that are not abundant. Given this, my first step
    was in finding all the abundant numbers (there were ~5k abundant numbers out of 28k numbers total verifying my
    hypothesis).
    2)
    Then, I took every pair of abundant numbers that were less than the upper limit (28123) and threw them in a set to
    maintain uniqueness. The numbers in this set then constituted all the numbers that could be constituted of abundant
    numbers.
    3)
    At this point, all I had to do was sum the values in the set and subtract this from the net summation of 28123.

    O(n,m,0) = n*root(n) + (m^2)/2 + o
    n = 28123
    m = ~5k, abundant numbers less than 28123
    o = not too sure but the upper limit is 28123, its just the len(sum of pairs in abundant set)
    """
    const_upper_limit = 28123
    # Gather all the abundant numbers
    abundant_numbers = []
    for i in xrange(1, const_upper_limit):
        if Tools.sum_divisors(i) > i:
            abundant_numbers.append(i)
    sums = set()
    # Gather the sum of all abundant pairs whose sum of pairs are less than 28123
    for i in xrange(len(abundant_numbers)):
        for j in xrange(i, len(abundant_numbers)):
            abundant_sums = abundant_numbers[i] + abundant_numbers[j]
            if abundant_sums > 28123:
                break
            sums.add(abundant_sums)
    net_sum_of_possible_numbers = Tools.summation(const_upper_limit)
    return net_sum_of_possible_numbers - sum(sums)


# Return the millionth permutation of 9-0
def p24():
    """
    My algorithm goes as follows:
    1) Find the MSD (most significant digit). To find the MSD, let us examine permutations and how they work.
       From taking a look at a few permutations, we can see a pattern beginning to emerge. That pattern takes this basic
       form. Given n digits (in this problem n == 10), we know that the largest numbers will have a MSD of n - 1, the
       next smallest group of numbers n - 2 and so on. What's key is that the size of each group is the same with that
       size being: (n - 1)!. This number is actually quite intuitive given it is basically a reordering of the
       definition of factorials.

    2) Given this observation, we can search for the MSD in chunks of (n-1)!, the 2nd MSD in chunks of (n-2)! etc...

    O(n) = c
    c = 10 division operations or so
    """
    # To make this a generic solution, toggle these values around
    permutation_length = 10
    target_index = 999999
    # The target index is out of range
    if math.factorial(10) < target_index:
        return -1
    millionth_permutation = ""
    digits = range(permutation_length)
    n = len(digits)
    while n > 0:
        group_size = math.factorial(n-1)
        index = target_index/group_size
        digit = digits[index]
        millionth_permutation += str(digit)
        target_index -= (index * group_size)
        digits.remove(digit)
        n = len(digits)
    return millionth_permutation


# REturns the first fibonacci number with > 1000 digits
def p25():
    smallest_thousand_number = int("1" + "0"*999)
    n = 2
    fib_n = 1
    fib_n_minus_1 = 1
    while smallest_thousand_number >= fib_n:
        tmp_fib_n_minus_1 = fib_n
        fib_n += fib_n_minus_1
        fib_n_minus_1 = tmp_fib_n_minus_1
        n += 1
    return n


# Find the value d such that 1/d with the longest recurring cycle
def p26():
    d = 999
    max_d = 999
    max_cycle_length = 1
    while d > 0:
        current_cycle_length = Tools.get_cycle_length(d)
        if current_cycle_length > max_cycle_length:
            max_cycle_length = current_cycle_length
            max_d = d
        if max_cycle_length > d:
            return max_d
        d -= 1
    return max_d


def p27_prime_polynomial_length(a, b):
    count = 0
    while Tools.is_prime(Tools.nth_polynomial(count, 1, a, b)):
        count += 1
    return count


# Find the product of a, b s.t. n^2 + a*n + b where consecutive values of n starting from 0 yield the most primes.
def p27():
    # Generate "a" values. Values for "a" must be odd (unless b is 2)
    a_values = range(1, 1001, 2)
    # Generate "b" values.
    # Values for "b" must be prime because if we plug 0 into "n", we are left with "b". Hence, in
    # order for the polynomial to be 0, b must be prime
    b_values = []
    for i in xrange(1000):
        if Tools.is_prime(i):
            b_values.append(i)
    # Initialize vars
    max_ab = 0
    max_consecutive_ns = 0
    # Iterate over a and b values
    for a in a_values:
        for b in b_values:
            papb = p27_prime_polynomial_length(a, b)
            if papb > max_consecutive_ns:
                max_ab = a*b
                max_consecutive_ns = papb
            napb = p27_prime_polynomial_length(-a, b)
            if napb > max_consecutive_ns:
                max_ab = -a*b
                max_consecutive_ns = napb
            panb = p27_prime_polynomial_length(a, -b)
            if panb > max_consecutive_ns:
                max_ab = a*-b
                max_consecutive_ns = panb
            nanb = p27_prime_polynomial_length(-a, -b)
            if nanb > max_consecutive_ns:
                max_ab = a*b
                max_consecutive_ns = nanb
    return max_ab


# Find the sum of the diagonal numbers of a 1001x1001 grid
def p28():
    current_val = 3
    sum_vals = 1
    add_by = 2
    for i in xrange(500):
        for j in xrange(4):
            sum_vals += current_val + j*add_by
        current_val += (add_by*3 + add_by + 2)
        add_by += 2
    return sum_vals


# Find the number of unique powers for the equation a**b where a and b = [2:100]
def p29():
    vals = set()
    for a in xrange(2,101):
        for b in xrange(2,101):
            vals.add(a**b)
    return len(vals)


# Checks whether the sum of the 5th power of the digits equal to n
def p30_fifth_power_sum_digits(n):
    n_copy = n
    sum_fifth_power_digits = 0
    while n > 0:
        sum_fifth_power_digits += (n % 10)**5
        n /= 10
    return sum_fifth_power_digits == n_copy


# Find all the numbers that can be written as the sum of 5th powers of their digits
def p30():
    qualifying_numbers_sum = 0
    max_possible_value = 5*(9**5)
    for i in xrange(10, max_possible_value):
        if p30_fifth_power_sum_digits(i):
            qualifying_numbers_sum += i
    return qualifying_numbers_sum