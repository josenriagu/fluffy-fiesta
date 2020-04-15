def queensAttack(n, k, r_q, c_q, obstacles):
    # possible = set()
    count = 0

    # given queen's spot, generate possible moves
    # def gen_moves(r_q, c_q):

    # generate horizontal left moves
    # assign new variables
    hl = c_q

    while hl > 1:
        if [r_q, hl - 1] in obstacles:
            print(
                f"found obstacle at {(r_q, hl - 1)}. terminating this side...")
            break
        else:
            count += 1
            # possible.add((r_q, hl - 1))
            hl -= 1

    # generate horizontal right moves
    # assign new variables
    hr = c_q

    while hr < n:
        if [r_q, hr + 1] in obstacles:
            print(
                f"found obstacle at {(r_q, hr + 1)}. terminating this side...")
            break
        else:
            count += 1
            # possible.add((r_q, hr + 1))
            hr += 1
    # generate vertical top moves
    # assign new variables
    vt = r_q

    while vt < n:
        if [vt + 1, c_q] in obstacles:
            print(
                f"found obstacle at {(vt + 1, c_q)}. terminating this side...")
            break
        else:
            count += 1
            # possible.add((vt + 1, c_q))
            vt += 1

    # generate vertical down moves
    # assign new variables
    vd = r_q

    while vd > 1:
        if [vd - 1, c_q] in obstacles:
            print(
                f"found obstacle at {(vd - 1, c_q)}. terminating this side...")
            break
        else:
            count += 1
            # possible.add((vd - 1, c_q))
            vd -= 1

    # generate low left diag moves
    # assign new variables
    lld_r_q, lld_c_q = r_q, c_q

    low_left = True

    while low_left:
        if lld_r_q == 1 or lld_c_q == 1:
            low_left = False
            break
        elif [lld_r_q - 1, lld_c_q - 1] in obstacles:
            print(
                f"found obstacle at {(lld_r_q - 1, lld_c_q - 1)}. terminating this side...")
            break
        else:
            count += 1
            # possible.add((lld_r_q - 1, lld_c_q - 1))
            lld_r_q -= 1
            lld_c_q -= 1

    # generate low right diag moves
    # assign new variables
    lrd_r_q, lrd_c_q = r_q, c_q

    low_right = True

    while low_right:
        if lrd_r_q == 1 or lrd_c_q == n:
            low_right = False
            break
        elif [lrd_r_q - 1, lrd_c_q + 1] in obstacles:
            print(
                f"found obstacle at {(lrd_r_q - 1, lrd_c_q + 1)}. terminating this side...")
            break
        else:
            count += 1
            # possible.add((lrd_r_q - 1, lrd_c_q + 1))
            lrd_r_q -= 1
            lrd_c_q += 1

    # generate high left diag moves
    # assign new variables
    hld_r_q, hld_c_q = r_q, c_q

    high_left = True

    while high_left:
        if hld_r_q == n or hld_c_q == 1:
            high_left = False
            break
        elif [hld_r_q + 1, hld_c_q - 1] in obstacles:
            print(
                f"found obstacle at {(hld_r_q + 1, hld_c_q - 1)}. terminating this side...")
            break
        else:
            count += 1
            # possible.add((hld_r_q + 1, hld_c_q - 1))
            hld_r_q += 1
            hld_c_q -= 1

    # generate high right diag moves
    # assign new variables
    hrd_r_q, hrd_c_q = r_q, c_q

    high_right = True

    while high_right:
        if hrd_r_q == n or hrd_c_q == n:
            high_right = False
            break
        elif [hrd_r_q + 1, hrd_c_q + 1] in obstacles:
            print(
                f"found obstacle at {(hrd_r_q + 1, hrd_c_q + 1)}. terminating this side...")
            break
        else:
            count += 1
            # possible.add((hrd_r_q + 1, hrd_c_q + 1))
            hrd_r_q += 1
            hrd_c_q += 1

    # gen_moves(r_q, c_q)
    return count


print(queensAttack(4, 0, 4, 4, []))
print(queensAttack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]]))
print(queensAttack(1, 0, 1, 1, []))
print(queensAttack(100000, 100000, 6453, 3654, [[72035, 57014], [24109, 50912]]))
