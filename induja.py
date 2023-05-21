import webbrowser
import geopy
import folium
import matplotlib.pyplot as plt
import matplotlib.pyplot as pyplot
from PyDictionary import PyDictionary
import requests

class line_plot:
    def __init__(self):
        self.x_axis = []
        self.y_axis = []
        n=int(input("enter no of coordinates"))
        for i in range(n):
            x=int(input("enter x value"))
            self.x_axis.append(x)
            y=int(input("enter y value"))
            self.y_axis.append(y)
        plt.plot(self.x_axis, self.y_axis)
        title=input("enter the title")
        plt.title(title)
        xn=input("enter x_axis name")
        plt.xlabel(xn)
        yn=input("enter y_axis name")
        plt.ylabel(yn)
        plt.show()
class line:
        def __init__(self):
            with open("coordinates.txt") as f:
                data = [tuple(map(int, line.strip().split(","))) for line in f]
            x_values = [x for x, y in data]
            y_values = [y for x, y in data]
            plt.plot(x_values, y_values)

            plt.title("Line Plot of Coordinates")
            plt.xlabel("X values")
            plt.ylabel("Y values")
            plt.show()

    
class bar_plot:
    def __init__(self):
        self.x_axis = []
        self.y_axis = []
        n=int(input("enter no of coordinates"))
        for i in range(n):
            x=int(input("enter x value"))
            self.x_axis.append(x)
            y=int(input("enter y value"))
            self.y_axis.append(y)
        plt.bar(self.x_axis, self.y_axis)
        title=input("enter the title")
        plt.title(title)
        xn=input("enter x_axis name")
        plt.xlabel(xn)
        yn=input("enter y_axis name")
        plt.ylabel(yn)
        plt.show()
class bar:
    def __init__(self):
            with open("coordinates.txt") as f:
                data = [tuple(map(int, line.strip().split(","))) for line in f]

            x_values = [x for x, y in data]
            y_values = [y for x, y in data]

            plt.bar(x_values, y_values)

            plt.title("Line Plot of Coordinates")
            plt.xlabel("X values")
            plt.ylabel("Y values")
            plt.show()

class scatter_plot:
    def __init__(self):
        self.x1=[]
        self.y1=[]
        self.x2=[]
        self.y2=[]
        title=input("enter the title")
        name1=input("enter the name of the first plot")
        n1=int(input("enter the number of coordinates in first plot"))
        name2=input("enter the name of the second plot")
        n2=int(input("enter the number of coordinates in second plot"))
        for i in range(n1):
            elt=int(input("enter the x1 coordinate"))
            self.x1.append(elt)
            val=int(input("enter the y1 coordinate"))
            self.y1.append(val)
        for i in range(n2):
            elt=int(input("enter the x2coordinate"))
            self.x2.append(elt)
            val=int(input("enter the y2coordinate"))
            self.y2.append(val)
        pyplot.scatter(self.x1, self.y1, label = name1, color='c')
        pyplot.scatter(self.x2,self.y2,label= name2,color='g')
        pyplot.title(title)
        pyplot.xlabel('x')
        pyplot.ylabel('y')
        pyplot.legend()
        # Print the chart
        pyplot.show()
class scatter:
    def __init__(self):
            with open("coordinates.txt") as f:
                data = [tuple(map(int, line.strip().split(","))) for line in f]

            x_values = [x for x, y in data]
            y_values = [y for x, y in data]
            plt.scatter(x_values, y_values)

            plt.title("Line Plot of Coordinates")
            plt.xlabel("X values")
            plt.ylabel("Y values")

            plt.show()
class pie_chart:
    def __init__(self):
        import matplotlib.pyplot as pyplot
        slice=[]
        activities=[]
        title=input("enter the title name")
        slices=int(input("enter the number of slices"))
        for i in range(slices):
            val=int(input("enter the value of slice:"))
            slice.append(val)
        for i in range(slices):
            act=input("enter the activity name:")
            activities.append(act)
        cols = ['r','b','c','g', 'orange']
        pyplot.pie(slice,
                   labels =activities,
                   colors = cols,
                   startangle = 90,
                   shadow = True,
                   autopct ='%1.1f%%')
        pyplot.title(title)

        # Print the chart
        pyplot.show()
class pie:
    def __init__(self):
        with open("data.txt") as f:
            data = [line.strip().split(",") for line in f]

        values = [float(value) for value, label in data]
        labels = [label for value, label in data]

        # Create pie chart
        plt.pie(values, labels=labels)
    
        # Set plot title
        plt.title("Pie Chart of Data")

        # Display plot
        plt.show()
class find_meaning:
    def __init__(self):
        # create dictionary object
        dictionary=PyDictionary()    
        # get user input
        word = input("Enter a word: ")
        # get meaning of the word
        meaning = dictionary.meaning(word)

        # check if meaning is available
        if meaning is not None:
            # print meanings
            for key, value in meaning.items():
                print(f"{key}:")
                for item in value:
                    print(f"- {item}")
        else:
            print("Meaning not found.")
class search_query:
    def __init__(self):
        # get user input
        sentence = input("Enter a sentence: ")
        # construct search query
        query = "https://www.youtube.com/results?search_query=" + sentence.replace(" ", "+")
        # open the first video in the search results
        webbrowser.open(query)
    
class find_location:
    def __init__(self):
        # get user input
        address = input("Enter a location: ")
        # geocode the address
        geolocator = geopy.Nominatim(user_agent="info-graphics")
        location = geolocator.geocode(address)
        # create map centered at the location
        map_center = [location.latitude, location.longitude]
        m = folium.Map(location=map_center, zoom_start=10)
        # add marker for the location
        folium.Marker(location=map_center, popup=address).add_to(m)
        # display the map
        m.save('map.html')
    
    

def main():
    print("1.LINE PLOT")
    print("2.BAR PLOT")
    print("3.SCATTER PLOT")
    print("4.PIE CHART")
    print("5.FIND MEANING")
    print("6.SEARCH QUERY")
    print("7.FIND LOCATION")
    print("8.line file")
    print("9.bar file")
    print("10.scatter file")
    print("11.pie file")
    while 1:
        ch=int(input("Enter the choice"))
        if ch==1:
            dis=int(input("Enter 1 to know about lineplot "))
            if dis==1:
                # get user input
                sentence = "lineplot"
                # construct search query
                query = "https://www.youtube.com/results?search_query=" + sentence.replace(" ", "+")
                # open the first video in the search results
                webbrowser.open(query)
            else:
                break
            l=line_plot()
        elif ch==2:
            dis=int(input("Enter 1 to know about bar plot"))
            if dis==1:
                # get user input
                sentence = "barplot"
                query = "https://www.youtube.com/results?search_query=" + sentence.replace(" ", "+")
                # open the first video in the search results
                webbrowser.open(query)
            else:
                break
            b=bar_plot()
        elif ch==3:
            dis=int(input("Enter 1 to know about scatter plot"))
            if dis==1:
                # get user input
                sentence = "scatter plot"
                # construct search query
                query = "https://www.youtube.com/results?search_query=" + sentence.replace(" ", "+")
                # open the first video in the search results
                webbrowser.open(query)
            else :
                break
            s=scatter_plot()
        elif ch==4:
            dis=int(input("Enter 1 to know about pie chart"))
            if dis==1:
                # get user input
                sentence = "pie chart"
                # construct search query
                query = "https://www.youtube.com/results?search_query=" + sentence.replace(" ", "+")
                # open the first video in the search results
                webbrowser.open(query)
            else:
                break
            p=pie_chart()
        elif ch==5:
            dis=int(input("Enter 1 to know about finding meaning for words using dictionary"))
            if dis==1:
                # get user input
                sentence = "finding meaning of the word using dictionary in python"
                # construct search query
                query = "https://www.youtube.com/results?search_query=" + sentence.replace(" ", "+")
                # open the first video in the search results
                webbrowser.open(query)
            else:
                break
            fm=find_meaning()
        elif ch==6:
            dis=int(input("Enter 1 to know about searching query in python"))
            if dis==1:
                # get user input
                sentence = "searching query in python"
                # construct search query
                query = "https://www.youtube.com/results?search_query=" + sentence.replace(" ", "+")
                # open the first video in the search results
                webbrowser.open(query)
            else:
                break
            sq=search_query()
        elif ch==7:
            dis=int(input("Enter 1 to know about finding locations in python"))
            if dis==1:
                # get user input
                sentence = "find location using geopy in python"
                # construct search query
                query = "https://www.youtube.com/results?search_query=" + sentence.replace(" ", "+")
                # open the first video in the search results
                webbrowser.open(query)
            else:
                break
            fyl=find_location()
        elif ch==8:
            li=line()
        elif ch==9:
            ba=bar()
        elif ch==10:
            sa=scatter()
        elif ch==11:
            pi=pie()
          
main()
