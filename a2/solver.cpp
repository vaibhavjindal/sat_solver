#include <bits/stdc++.h>
using namespace std;

//"solution" stores the propositions that we get after solving the encoding
vector<int> solution;

//uncomment the following line for counting the steps
//long long int counter=0;

//returns the index of the clause of smallest length in the encoding
int smallest_clause(vector<vector<int>> v){
	int min=v[0].size();
	int index=0,n=v.size();
	for(int i=0;i<v.size();i++){
		if(v[i].size()<min){
			min=v[i].size();
			index=i;
		}
	}
	return index;
}

//for a given index of clause, it returns the element 
//which is repeated most often in the complete encoding
int max_occur_prop(vector<vector<int>> v,int index){
	int s=v[index].size();
	int arr[s]={0};
	int n=v.size();
	for(int i=0;i<n;i++){
		int m=v[i].size();
		for(int j=0;j<m;j++){
			for(int k=0;k<s;k++){
				if(v[i][j]==v[index][k]||v[i][j]==-v[index][k]){
					arr[k]++;
					break;
				}
			}
		}
	}
	int max=arr[0];
	int ind=0;
	for(int i=0;i<s;i++){
		if(arr[i]>max){
			max=arr[i];
			ind=i;
		}
	}
	return v[index][ind];
}

//for a given literal, it removes all the clauses containing that literal
//and removes the negation of the literal from all the clauses, finally
//returning the modified vector
vector<vector<int>> trim(vector<vector<int>> v, int prop){
	int v_rows=v.size();
	vector<int> row_eliminate;
	for(int i=0;i<v_rows;i++){
		int row_size=v[i].size();
		for(int j=0;j<row_size;j++){
			if(v[i][j]==prop){
				row_eliminate.push_back(i);
				break;
			}
			else if(v[i][j]==-1*prop){
				v[i].erase(v[i].begin()+j);
				break;
			}
		}
	}
	int row_eliminate_size=row_eliminate.size();
	for(int i=0;i<row_eliminate_size;i++){
		v.erase(v.begin()+row_eliminate[i]-i);
	}
	return v;
}

//recursive function to break the encoding
//takes a vector of vectors as an input
//returns 1 and stores the satisfiable literals in the universal variable vector "solution" 
//if a satisfiable encoding exists, otherwise returns 0
int solve(vector<vector<int>> v) {
	//uncomment the following line for counter implementation
	//counter++;
	int size=v.size();
	if(size==0){//if all the clauses have been eliminated, we have got a satisfiable encoding
		return 1;
	}
	int index=smallest_clause(v);
	if(v[index].size()==0){//if the smallest clause is of length 0, we have got a contradiction
		return 0;
	}
	int prop=max_occur_prop(v,index);//prop is the literal that we will use to break the encoding

	solution.push_back(prop);//add prop to the solution
	if(solve(trim(v,prop))==1){//if the encoding is satisfiable after assuming the literal to be true
		return 1;
	}
	else{//otherwise
		solution.pop_back();//remove the last added literal
		solution.push_back(-1*prop);//add the negative of prop
		if(solve(trim(v,-1*prop))==1){//if the encoding is satisfiable
			return 1;
		}
		else{//otherwise
			solution.pop_back();//remove the negative of prop from solution
			return 0;
		}
	}
}

 

int main() {
	clock_t tStart = clock();//start time
	
	//reading the input file and storing the encoding in vector of vectors
	int props,clauses;//number of literals and clauses
	string data;
	ifstream f;
	f.open("input.txt");
	while(1){
		getline(f,data);
		if(data[0]=='p'){
			istringstream iss(data);
			vector<string> results((istream_iterator<string>(iss)),istream_iterator<string>());
			props=stoi(results[2]);
			clauses=stoi(results[3]);
			break;
		}
	}
	vector< vector<int> > encoding(clauses);//vector of vectors to store the encoding
	for(int i=0;i<clauses;i++){
		getline(f,data);
		istringstream iss(data);
		vector<string> results((istream_iterator<string>(iss)),istream_iterator<string>());
		int l=results.size();
		for(int j=0;j<l-1;j++){
			encoding[i].push_back(stoi(results[j]));
		}
	}
	f.close();

	int result=solve(encoding);//result==1 if encoding in SAT, otherwise 0

	//output procedure
	ofstream out_file;
	out_file.open("output.txt");
	if(result==1){
		out_file<<"SAT\n";
		//if some literal is not in solution, then it can take any value, we give it a true value 
		int arr[props];//arr contains the final satisfiable encoding
		for(int i=0;i<props;i++){
			arr[i]=i+1;
		}
		for(int i=0;i<solution.size();i++){
			if(solution[i]<0){//if negative of a ith proposition is true
				arr[(-1*solution[i])-1]=solution[i];
			}
		}
		for(int i=0;i<props;i++){
			out_file<<arr[i]<<" ";
		}
		out_file<<"0";
	}
	else{
	out_file<<"UNSAT";	
	}
	out_file.close();

	//uncomment the following line for counter implementation
	//cout<<"Number of recursive calls:"<<counter<<"\n";
	printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0;
}