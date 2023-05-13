class Preprocessing:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    # drop columns
    def drop_column(self, column):
        self.data_frame.drop(columns=[column], inplace=True)