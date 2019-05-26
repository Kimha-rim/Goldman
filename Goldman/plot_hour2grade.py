
import matplotlib.pyplot as plt  
%matplotlib inline

def plot_hour2grade(x_data, y_data, xline, yline):
    """ x_data, y_data의 값들을 그래프로 출력 """
    plt.figure()  
    plt.plot(x_data, y_data, 'ob')  
    plt.plot(xline, yline)
    plt.title('Silver to Gold')
    plt.xlabel('Silver price')
    plt.ylabel('Gold price')
    plt.show()
