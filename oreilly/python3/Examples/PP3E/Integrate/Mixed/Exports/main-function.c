/*******************************************************
 * main program - loads embedded Python code from files;
 * this is mostly for testing only--in practice, the 
 * code may be extracted from HTML or XML files, be
 * read from a socket over a network, be fetched from 
 * a dbm file or sql database by event-name key, etc.
 *******************************************************/
 
#include <stdio.h>
#include "runpy.h"
#include "cinterface.h"

/* Python programs to run */
#define MAXFILE 4096
static char *tests[] = {"script1.py", "script2.py", "script3.py", NULL};

/* names that this C program exports to Python programs */
static int   aa = 0; 
static int   bb = 42;
static char  cc[64] = "";
static char *dd = "Cspam";
static float ee = 3.14159;  

/* mapping table used here */
static cnameMap myCnameMapTable[] = {
    {"aa", INT,  &aa},
    {"bb", INT,  &bb},         /* names exported to Python code */
    {"cc", STR1,  cc},         /* in python code: "cvar.cc" */
    {"dd", STR2, &dd},         /* linked to cinterface.so on import */
    {"ee", FLT,  &ee},
    {NULL, INT,  NULL}
};

/* define cinterface names */
char CnameMessage[128];

cnameMap *CnameMapLookup(char *name)
{
    /* map python attr names to C addrs for cinterface type */
    /* on reference and assignment; use hash-table if many names */

    cnameMap *cname;
    for (cname = myCnameMapTable; cname->name != NULL; cname++) {
        if (strcmp(name, cname->name) == 0)
            return cname;
    }
    return NULL;   /* reached NULL = not found */
}

static void 
dumpall()
{ 
    printf("vars in C:\taa=%d bb=%d cc=%s dd=%s ee=%f\n", aa, bb, cc, dd, ee); 
}

static void
run_user_code()                   
{                                 /* load/run Python code from text files */
    int status, nbytes;           /* XXX should also check status everywhere */
    char script[MAXFILE];         /* XXX should malloc a big-enough block */
    FILE *file;

    char **test = tests;
    dumpall();
    while (*test != NULL) {
        printf("\nStarting %s\n", *test);

        file = fopen(*test, "r");                  /* load Python file text */
        nbytes = fread(script, 1, MAXFILE, file);  /* customizable actions */
        script[nbytes] = '\0';

        status = RunPyExecCodeString(script);   /* all the action occurs */
        if (status != 0) {                      /* in cinterface.c calls */
            printf("%s\n", RunPyError);
            RunPyPrintPythonErrorInfo();
        }
        dumpall();
        test++;
    }
}

main(int argc, char **argv)              /* C's on-top, Python's embedded */
{                                        /* but Python uses C extensions  */
    int status = RunPyInitialize();
    if (status != 0) {
        printf("%s\n", RunPyError);
        RunPyPrintPythonErrorInfo();
    }
    run_user_code(); 
    printf(CnameMessage);
}
