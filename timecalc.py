from datetime import timedelta
import sys
import re


def help():
    print("Calculate TIME!")
    print("Usage: python " + sys.argv[0] + " Time_1 [+|-] Time_2")


def main():
    t_fp = re.compile('\d\d\:\d\d\:\d\d')
    try:
        if(t_fp.match(sys.argv[1]) and t_fp.match(sys.argv[3]) and (sys.argv[2] == '+' or sys.argv[2] == '-')):
            time_1 = sys.argv[1]
            time_2 = sys.argv[3]
            operator = sys.argv[2]
            s1 = int(time_1[:2]) * 60 * 60 + \
                int(time_1[3:5]) * 60 + int(time_1[6:8])
            s2 = int(time_2[:2]) * 60 * 60 + \
                int(time_2[3:5]) * 60 + int(time_2[6:8])
            t1 = timedelta(seconds=s1)
            t2 = timedelta(seconds=s2)
            if(operator == '+'):
                t_sum = t1 + t2
                print(t_sum)
            else:
                t_sub = timedelta(hours=0, minutes=0, seconds=0)
                if(t2 > t1):
                    t_sub = t2 - t1
                elif(t2 < t1):
                    t_sub = t1 - t2
                else:
                    pass
                print(t_sub)
        else:
            help()
            exit()
    except IndexError:
        print("Error: No arguments")
        help()
        exit()


if __name__ == "__main__":
    main()
