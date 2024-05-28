%{
#include <stdio.h>
%}

/* Definitions */
oct [0][0-7]+
hex 0[xX][0-9A-Fa-f]+

%%
{hex} { printf("Hexadecimal number: %s\n", yytext); }
{oct} { printf("Octal number: %s\n", yytext); }
.|\n  { /* Ignore other inputs */ }

%%

int main() {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
