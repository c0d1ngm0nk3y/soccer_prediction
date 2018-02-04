from data.TestDataGenerator import TestDataGenerator
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from analysis.Util import show_plot

def generate_data():
    seasons = map(str, range(2006, 2017))

    generator = TestDataGenerator()

    train_data = []
    x_data = []
    y_data = []
    for season in seasons:
        season_data = generator.generate_from_season('bl1', season)
        train_data.extend(season_data)

    for data in train_data:
        (input_list, _, results, _) = data
        x_data.append(input_list)
        y_data.append(results[0])

    x_train, x_test, y_train, y_test = train_test_split(
        x_data, y_data)#, test_size=0.25)


    return ((x_train, y_train), (x_test, y_test))

def test_n_neighbors(n, train_data, test_data):
    neigh = KNeighborsClassifier(n_neighbors=n)
    (x_train, y_train) = train_data
    neigh.fit(x_train, y_train)

    #score = neigh.score(x_train, y_train)
    (x_test, y_test) = test_data
    score = neigh.score(x_test, y_test)
    return score

def main():
    x_axis = []
    y_axis = []

    (train_data, test_data) = generate_data()

    max_n = 25
    for n in range(1, max_n + 1):
        x_axis.append(n)

        score = test_n_neighbors(n, train_data, test_data)
        y_axis.append(score * 100)

    show_plot(x_axis, y_axis, x_axis[-1])


if __name__ == "__main__":
    main()
