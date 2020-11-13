//Mohammad Asim Iqbal
#include <stdio.h>
#include <dirent.h>
#include <string.h>
#include <string.h>

#define BUFFER_SIZE 1980
#define BUFFER_SIZE2 1000 
int main(int argc, char * argv[])
{
	// file descriptor
	FILE * fptr;
	// temporary file descriptor
	FILE * ftemp;

	// searching the directory
	struct dirent *de;

	// hard coding the buffer size to be 1980
	char buffer[BUFFER_SIZE];
	char new_buffer[BUFFER_SIZE2];

	// arrays for storing find, replace, and prefix parameter
	char find[100], replace[100], prefix[100];
	
	// In case thrre are not enough arguments given
	if (argc != 4){
		printf("Usage Info: search <find> <replace> <prefix> \n");
		return -1;
		}
	
	// copying the argv arguments to respective find, replace, and prefix array
	strcpy(find, argv[1]);
	strcpy(replace, argv[2]);
	strcpy(prefix, argv[3]);
	// opening up the current directory
	DIR *dr = opendir(".");
	// if error occured
	if (dr == NULL){
		printf("Error while opening the directory");
		return 1;
		}
	
	while (( de = readdir(dr)) != NULL){
		//char s1[] = de->d_name;
		char s1[100];
		strcpy(s1, de->d_name);
		char s2[] = ".txt";

		// for all the .txt files
		if (strstr(de->d_name, s2)){
			// creating temporary file
			// then replacing the original file with the temporary file.
			// no changes made to original file, just creating a illusion 
			fptr = fopen(de->d_name, "r");
			ftemp = fopen("replace.temp", "w");
			// if any error occured
			if (ftemp == NULL || fptr == NULL){
				printf("Error in opening the file.\n");
				return 2;
				}
			// to keep the track of find parameter in the file
			int counter_find = 0;
			while ((fgets(buffer, BUFFER_SIZE, fptr)) != NULL){
				int index = 0;
				char *position;
				char temp[BUFFER_SIZE];

				int length_find = strlen(find);
				// looping throught the every line of the file 
				// if found the file parameter
				while((position = strstr(buffer, find)) != NULL){
					printf("Line-> %s, find and replace operation done where find: %s and replace: %s\n",buffer,find,replace);
					// making backup of the current line in temp
					strcpy(temp, buffer);
					// getting the inded of first occurence of find
					index = position - buffer;
					// terminating the line upto the first occurrence of the find parameter
					buffer[index] = '\0';
					// concateting the edited line with replace parameter
					strcat(buffer, replace);
					// concateting the edited line wiht the rest line by getting the part from  temp
					strcat(buffer, temp + index + length_find);
					// increasing thr counter
					counter_find = counter_find + 1;
					}
				// putting ther editied line to ftemp
				fputs(buffer, ftemp);
				}
			// closing files
			fclose(fptr);
			fclose(ftemp);
			
			remove(de->d_name);
			// renaming temp file to the original file
			rename("replace.temp", s1);
			// for the count of prefix parameter in the file
			int counter_prefix = 0;
			// if file doesnot have file paramter, search for the prefix parameter
			if (counter_find == 0){
				fptr = fopen(de->d_name,"r");
				ftemp = fopen("new_replace.temp","w");
				// looping through the each line
				while ((fgets(new_buffer, BUFFER_SIZE2, fptr)) != NULL){
					int new_index = 0;
					char *new_position;
					char new_temp[BUFFER_SIZE2];
					int find_x = strlen(find);
					int prefix_x = strlen(prefix);
					int counter = 0;
					// if prefix parameter found
					//int * pointer = new_buffer;
					while((new_position = strstr(new_buffer+counter, prefix))){
						printf("Line-> %s, Apppend operation done where find: %s and prepend: %s\n",new_buffer,find,prefix);
						// storing the line read to new_temp
						strcpy(new_temp, new_buffer);
						// getting the index of the first occurence of the prefix parameter in the file
						new_index = new_position - new_buffer;
						// terminating the line upto the first occurence of the prefix paramter
						new_buffer[new_index] = '\0';
						// concatenating the editied line with the file parameter
						strcat(new_buffer, find);
						// prepending just before the prefix parameter 
						strcat(new_buffer, new_temp + new_index);
						// increasing count of counter_prefix
						counter_prefix = counter_prefix + 1;
						counter = new_index + strlen(prefix) + strlen(find);
						//new_buffer += new_index;
						//pointer = pointer + new_index + find_x + prefix_x; 	
						//new_position++;
						}
				// putting the edited line into ftemp
				fputs(new_buffer, ftemp);
				}
			// closing files
			fclose(fptr);
			fclose(ftemp);
			
			remove(de->d_name);
			// renaming the temp file with the original file
			rename("new_replace.temp", s1);
				
			}
			// if file do not have any of the parameters
			// No changes in the file
			if(counter_find ==0 && counter_prefix == 0){
				printf("File is not changed as falied to find.\n");
				}


			}

			
		}
		
	
	closedir(dr);
	return 0;
}
