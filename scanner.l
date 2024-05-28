%{
#include <stdio.h>
%}

%option noyywrap

/* Regular expressions for tokens */
DIGIT   	[0-9]
LETTER  	[a-zA-Z]
ID      	{LETTER}({LETTER}|{DIGIT})*
INT_CONST   {DIGIT}+
FLOAT_CONST {DIGIT}+"."{DIGIT}+
WS      	[ \t\n\r]+
COMMENT 	("//"(.)*)
STRING      \"([^\"\n]|\\.)*\"

%%
"int"|"float"|"char"   	{ printf("Keyword          : %s\n",yytext); }
"if"|"else"|"for"|"while"|"return"   	{ printf("Keyword          : %s\n",yytext); }
{STRING} {printf("String          : %s\n",yytext); }
{ID}    	{ printf("Identifier        : %s\n", yytext); }
{INT_CONST} { printf("Integer Constant: %s\n", yytext); }
{FLOAT_CONST} { printf("Float Constant: %s\n", yytext); }
"+"|"-"|"*"|"/"|"="|"("|")"|"<"|">"    	{ printf("Operator: %s\n",yytext); }
{WS}    	; 
{COMMENT}   ; 
"#"([^\n])*\n { printf("Preprocessor Directive: %s\n", yytext); } 
.       	{ printf("Unrecognized token: %s\n", yytext); }
%%
int main(int argc, char *argv[]) {
	if (argc != 2) {
    	printf("Usage: %s input_file\n", argv[0]); //use sample.c
    	return 1;
	}
	FILE *file = fopen(argv[1], "r");
	if (!file) {
    	perror("Error opening file");
    	return 1;
	}
	yyin = file;
	yylex();
	fclose(file);
	return 0;
}
