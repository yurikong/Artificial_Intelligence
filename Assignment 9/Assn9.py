from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn import tree, ensemble
import matplotlib.pyplot as plt
import numpy as np


class Evaluation:
    def __init__(self):
        # data set
        self.cancer = load_breast_cancer()
        # split data set into train set and test set at ratio 1:9
        # X: input, Y: output
        self.X_train, self.X_test, self.y_train, self.y_test \
            = train_test_split(self.cancer.data, self.cancer.target, test_size=0.9)
        self.tree_score = 0
        self.bagging_score = {}
        self.boost_score = {}
        self.forest_score = {}

    def decision_tree(self):
        t1 = tree.DecisionTreeClassifier(criterion='gini').fit(self.X_train, self.y_train)
        self.tree_score = t1.score(self.X_test, self.y_test)

    def bagging(self):
        for bag_count in range(2, 82, 4):
            bagging = ensemble.BaggingClassifier(tree.DecisionTreeClassifier(), n_estimators=bag_count).fit(
                self.X_train, self.y_train)
            self.bagging_score[bag_count] = bagging.score(self.X_test, self.y_test)
        plt.scatter(x=self.bagging_score.keys(), y=self.bagging_score.values())
        plt.xlabel('n_estimators')
        plt.ylabel('Scores')
        plt.title('Bagging')
        plt.show()

    def forest(self):
        for feature_count in range(3, 31, 3):
            for bag_count in range(5, 56, 5):
                forest = ensemble.RandomForestClassifier(tree.DecisionTreeClassifier())
                forest.set_params(max_features=feature_count, n_estimators=bag_count)
                forest.fit(self.X_train, self.y_train)
                self.forest_score[(feature_count, bag_count)] = forest.score(self.X_test, self.y_test)
        keys = list(zip(*self.forest_score.keys()))
        fig, ax = plt.subplots()
        scatter = ax.scatter(
            #x=keys[1],
            x=np.array(keys[1]),
            #y=self.forest_score.values(),
            y=[i for i in self.forest_score.values()],
            #s=keys[0]
            s=np.array(keys[0])
        )
        plt.title("Random Forest")
        plt.xlabel("n_estimators")
        plt.ylabel("Scores")
        handles, labels = scatter.legend_elements(prop="sizes", alpha=0.5)
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        ax.legend(handles, labels, loc="center left", bbox_to_anchor=(1, 0.5), title="Feature Counts")
        plt.show()

    def boost(self):
        for bag_count in range(2, 82, 4):
            boost = ensemble.AdaBoostClassifier(tree.DecisionTreeClassifier(), n_estimators=bag_count).fit(
                self.X_train, self.y_train)
            self.boost_score[bag_count] = boost.score(self.X_test, self.y_test)
        plt.scatter(x=self.boost_score.keys(), y=self.boost_score.values())
        plt.xlabel('n_estimators')
        plt.ylabel('Scores')
        plt.title('AdaBoost')
        plt.show()

    def summary(self):
        print('Tree score:', self.tree_score)
        print('Bagging score:', self.bagging_score)
        print('Boost score:', self.boost_score)
        print('Forest score:', self.forest_score)


if __name__ == '__main__':
    exp = Evaluation()
    exp.decision_tree()
    exp.bagging()
    exp.forest()
    exp.boost()
    exp.summary()

