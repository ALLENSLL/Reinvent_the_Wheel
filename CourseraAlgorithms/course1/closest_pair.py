import numpy as np


def closest_pair(points):
    n_points = points.shape[0]
    if n_points == 2:
        return np.linalg.norm(points[0] - points[1]), points
    elif n_points == 3:
        dis1 = np.linalg.norm(points[0] - points[1])
        dis2 = np.linalg.norm(points[1] - points[2])
        dis3 = np.linalg.norm(points[2] - points[0])
        min_dis = min(dis1, dis2, dis3)
        if min_dis == dis1:
            min_pair = points[[0, 1]]
        elif min_dis == dis2:
            min_pair = points[[1, 2]]
        else:
            min_pair = points[[0, 2]]
        return min_dis, min_pair
    else:
        points_x, points_y = sort_points(points)
        cut = n_points // 2
        x_average = points_x[-1, 0]

        left_points, right_points = points[:cut, :], points[cut:, :]

        dis1, min_pair1 = closest_pair(left_points)
        dis2, min_pair2 = closest_pair(right_points)
        min_dis = min(dis1, dis2)
        min_pair = (min_pair1 if min_dis == dis1 else min_pair2)
        mask = np.zeros(len(points_y), dtype=bool)
        for i in range(points_y.shape[0]):
            if (min_dis - x_average) < points_y[i, 0] and (points_y[i, 0] < min_dis) + x_average:
                mask[i] = True
        S_y = points_y[mask]

        for i in range(len(S_y) - 1):
            for j in range(1, min(7, len(S_y) - i)):
                dis = np.linalg.norm(points_y[i] - points_y[i + j])
                if dis < min_dis:
                    min_dis = dis
                    min_pair = points_y[[i, i + j]]
        return min_dis, min_pair


def sort_points(points):
    points_x = points[np.argsort(points[:, 0])]
    points_y = points[np.argsort(points[:, 1])]
    return points_x, points_y


def force_search(points):
    min_dis = np.inf
    for i in range(points.shape[0] - 1):
        for j in range(i + 1, points.shape[0]):
            dis = np.linalg.norm(points[i] - points[j])
            if dis < min_dis:
                min_dis = dis
                min_pair = points[[i, j]]
    return min_dis, min_pair


if __name__ == '__main__':
    points = np.random.rand(2000, 2)
    min_dis, min_pair = closest_pair(points)
    print(min_pair)