
for n in range(20):
    tvs = [False for tv in range(n)]

    def format_tv_state(state, index):
        # Unicode characters for squares and subscript numbers
        white_square = "□"
        black_square = "■"
        subscripts = str(index + 1).translate(str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉"))
        return f"{black_square}{subscripts}" if state else f"{white_square}{subscripts}"



    for i in range(len(tvs)):
        for j in range(i, len(tvs)):
            if (j + 1) % (i + 1) == 0:
                tvs[j] = not tvs[j]


    num_on = 0
    for tv in tvs:
        if tv:
            num_on += 1
        # Print formatted version
        
    print([format_tv_state(tv, idx) for idx, tv in enumerate(tvs)], "\nWhen n = ", n, "|S| = ", {num_on})
    print(f"")
