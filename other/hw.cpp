#include <iostream>
#include <fstream>
#include <cctype>
#include <algorithm>
using namespace std;

int SimpleCost(int seating[24], int weights[24][24]);
int DistanceCost(int seating[24], int weights[24][24]);

int main(){

//reads in matrix
	ifstream File("weights.csv");
	string mom;
	char tempC;
	int matrix[24][24];
	for(int i = 0; i < 24; i++){
		for(int j = 0; j < 24; j++){
			File >> matrix[i][j];
			if(j != 23)
				File >> tempC;
		}
		getline(File, mom);
	}
	
//initializes seating arrangement

int seating[24];
for(int i = 0; i < 24; i++){
	seating[i] = i;
}
	

int change = 1, current = 0, best = SimpleCost(seating, matrix), swap = 0, tempI;
int s1, s2;
while(change > 0){
	for(int i = 0; i < 24; i++){
		for(int j = 0; j < 24; i++){
			if(i != j){
				tempI = seating[i];
				seating[i] = seating[j];
				seating[j] = tempI;
				
				if(SimpleCost(seating, matrix) < best){
					change = best - SimpleCost(seating, matrix);
					best = SimpleCost(seating, matrix);
					swap++;
					i = 24;
					j = 24;
				}
				else{
					tempI = seating[i];
					seating[i] = seating[j];
					seating[j] = tempI;
					change = 0;
				}		
			}
		
		}
	}
}
		
	
return 0;
}

int SimpleCost(int seating[24], int weights[24][24]){
	int total = 0;
	int n1, n2;
	
	//checks front
	int student = seating[0];
	n1 = seating[1];
	
	for(int i = 0; i < 24; i++){
		if(n1 != i && student != i){
			total += weights[student][i];
		}
	}
	
	//checks back
	student = seating[23];
	n1 = seating[22];
	
	for(int i = 0; i < 24; i++){
		if(n1 != i && student != i){
			total += weights[student][i];
		}
	}
	
	//checks rest
	for(int i = 1; i < 23; i++){
		student = seating[i];
		n1 = seating[i - 1];
		n2 = seating[i + 1];
		
		for(int j = 0; j < 24; j++){
			if(n1 != j && student != j && n2 != j){
				total += weights[student][j];
			}
		}
	}
	
	return total;
}


int DistanceCost(int seating[24], int weights[24][24]){
	int total = 0;
	int n1, n2;
	int index;
	//checks front
	int student = seating[0];
	n1 = seating[1];
	int *pointer;
	for(int i = 0; i < 24; i++){
		if(n1 != i && student != i){
			//calculate distance
			pointer = find(seating, seating + 24, i);
			index = *pointer;
			total += weights[student][i] * (index - 1);
		}
	}
	
	//checks back
	student = seating[23];
	n1 = seating[22];
	
	for(int i = 0; i < 24; i++){
		if(n1 != i && student != i){
			pointer = find(seating, seating + 24, i);
			index = *pointer;
			total += weights[student][i] * (22 - index);
		}
	}
	
	//checks rest
	for(int i = 1; i < 23; i++){
		student = seating[i];
		n1 = seating[i - 1];
		n2 = seating[i + 1];
		
		for(int j = 0; j < 24; j++){
			if(n1 != j && student != j && n2 != j){
				pointer = find(seating, seating + 24, j);
				index = *pointer;
				if(index > i){
					total += weights[student][j] * (index - i - 1);
				}
				else{
					total += weights[student][j] * (i - index - 1);
				}
			}
		}
	}
	
	return total;
}

	
