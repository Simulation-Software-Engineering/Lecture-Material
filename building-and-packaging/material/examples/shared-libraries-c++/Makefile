
all: shared static

shared:
	$(CXX) main.cpp -o main-shared

static:
	$(CXX) -static main.cpp -o main-static

clean:
	rm -rf main-shared main-static

