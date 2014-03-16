#include <iostream>
#include <ctime>
/*still very much a work in progress */

int main()

{
	int target  = 200;
	int ways = 0;

	using namespace std;
	for (int twoeuro = target; twoeuro >= 0; twoeuro -= 200) {
		for (int oneeuro = twoeuro; oneeuro >= 0; oneeuro -= 100) {
			for (int fifty = oneeuro; fifty >= 0; fifty -= 50) {
				for (int twenty = fifty; twenty >= 0; twenty -= 20) {
					for (int ten = twenty; ten >= 0; ten -= 10) {
						for (int five = ten; five >= 0; five -= 5) {
							for (int two = five; two >= 0; two -= 2) {
								ways++;
							}
						}
					}
				}
			}
		}
	}

	cout<<ways<<endl;
	return 0;
}

