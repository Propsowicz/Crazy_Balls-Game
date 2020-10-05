import os

class HighScore:
    def __init__(self):
        home_dir = os.path.expanduser("~")
        game_dir = "AppData\\Local\\sqrball"

        self.dir = os.path.join(home_dir, game_dir)
        if not os.path.isdir(self.dir):
            os.makedirs(self.dir)


        score_file = open((self.dir + "\\scores.txt"), "a+")
        try:
            score_file.seek(0)
            x = score_file.readline()
            scores_list = x.split(";")
            scores_list.pop()

            new_list = []

            for i in scores_list:
                l = i.split(",")
                new_list.append(tuple([l[0], int(l[1])]))
            s = sorted(new_list, key=lambda x: x[1], reverse=True)

            score_1 = s[0][1]
            name_1 = s[0][0]
            self.table_of_scores_name_1 = "1. " + name_1
            self.table_of_scores_sc_1 = str(score_1)
            try:
                name_2 = s[1][0]
                score_2 = s[1][1]
                self.table_of_scores_name_2 = "2. " + name_2
                self.table_of_scores_sc_2 = str(score_2)
            except:
                self.table_of_scores_name_2 = "2. - "
                self.table_of_scores_sc_2 = " - "
                self.table_of_scores_name_3 = "3. - "
                self.table_of_scores_sc_3 = " - "

            try:
                name_3 = s[2][0]
                score_3 = s[2][1]
                self.table_of_scores_name_3 = "3. " + name_3
                self.table_of_scores_sc_3 = str(score_3)
            except:
                self.table_of_scores_name_3 = "3. - "
                self.table_of_scores_sc_3 = " - "

            score_file.close()
        except:
            self.table_of_scores_name_1 = "1. - "
            self.table_of_scores_sc_1 = " - "
            self.table_of_scores_name_2 = "2. - "
            self.table_of_scores_sc_2 = " - "
            self.table_of_scores_name_3 = "3. - "
            self.table_of_scores_sc_3 = " - "


    def get_score(self, points):
        score_file = open((self.dir + "\\scores.txt"), "a+")

        try:
            score_file.seek(0)
            x = score_file.readline()
            scores_list = x.split(";")
            scores_list.pop()

            new_list = []

            for i in scores_list:
                l = i.split(",")
                new_list.append(tuple([l[0], int(l[1])]))
            s = sorted(new_list, key=lambda x: x[1], reverse=True)

            score_1 = s[0][1]
            score_2 = s[1][1]
            score_3 = s[2][1]

            if points > score_1 or points > score_2 or points > score_3:
                score_file.close()
                return True
            else:
                score_file.close()
                return False
        except:
            score_file.close()
            return True

    def add_new_score(self, name, points):
        score_file = open((self.dir + "\\scores.txt"), "a+")
        score_file.write(name + "," + str(points) + ";")

