
all: shared static

shared: main.cpp
	$(CXX) main.cpp -o main-shared

static: main.cpp
	$(CXX) -static main.cpp -o main-static

clean:
	rm -rf main-shared main-static

