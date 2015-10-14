__author__ = 'rfischer'

_num_choices_when_found = 0

def find_path_to_exit(cur_pos, num_choices):
    #print cur_pos
    #print num_choices
    global _num_choices_when_found

    (cury, curx) = cur_pos
    # found end
    if cur_pos == exit_pos:
        _num_choices_when_found = num_choices
        return num_choices
    # can never go back
    visited_places.add(cur_pos)
    check_right = 0
    check_left = 0
    check_up = 0
    check_down = 0
    # Check right
    if (curx < M-1) and forest[cury][curx+1] != 'X' and (cury, curx+1) not in visited_places:
        check_right = 1
    if (curx > 0) and forest[cury][curx-1] != 'X' and (cury, curx-1) not in visited_places:
        check_left = 1
    if (cury < N-1) and forest[cury+1][curx] != 'X' and (cury+1, curx) not in visited_places:
        check_down = 1
    if (cury > 0) and forest[cury-1][curx] != 'X' and (cury-1, curx) not in visited_places:
        check_up = 1

    if check_up + check_down + check_right + check_left > 1:
        num_choices += 1

    if check_right:
        find_path_to_exit((cury, curx+1), num_choices)
    if check_left:
        find_path_to_exit((cury, curx-1), num_choices)
    if check_up:
        find_path_to_exit((cury-1, curx), num_choices)
    if check_down:
        find_path_to_exit((cury+1, curx), num_choices)


    return -1

  # find path to exit
 #       Follow all paths until the only workable path found
 #       Count number of junctions as they are encountered
 #       Probably need a recursive search algorithm



T = input()

for i in range(0, T):

   num_choices = 0
   N, M = [int(n) for n in raw_input().split(' ')]
   forest = []
   for j in range (0, N):
       forest.append(raw_input())
       hp = forest[j].find("M")
       if (hp > -1):
           hermione_pos = (j, hp)
       ep = forest[j].find("*")
       if (ep > -1):
           exit_pos = (j, ep)
   K = input()
   visited_places = set(hermione_pos)

   path_junctions = find_path_to_exit(hermione_pos, 0)

   if _num_choices_when_found == K:
       print "Impressed"
   else:
       print "Oops!"



