import pandas as pd


class Join():

    def __init__(self):
        self.df_left = pd.DataFrame({'key': ['A', 'B', 'C'],
                                     'left': [1, 2, 3]})
        self.df_right = pd.DataFrame({'key': ['A', 'B', 'D'],
                                      'right': [4, 5, 6]})

    def prn(self):
        print('df_left\n', self.df_left)
        print('df_right\n', self.df_right)

    def left_join(self):
        df_left_join = self.df_left.merge(self.df_right, how='left', on='key')
        print('left join\n', df_left_join)

    def right_join(self):
        df_right_join = self.df_left.merge(self.df_right, how='right', on='key')
        print('right join \n', df_right_join)

    def outer_join(self):
        df_outer_join = self.df_left.merge(self.df_right, how='outer', on='key')
        print('outer_join\n', df_outer_join)

    def inner_join(self):
        df_inner_join = self.df_left.merge(self.df_right, how='inner', on='key')
        print('inner_join\n', df_inner_join)


if __name__ == '__main__':
    join = Join()
    join.prn()
    join.left_join()
    join.right_join()
    join.outer_join()
    join.inner_join()