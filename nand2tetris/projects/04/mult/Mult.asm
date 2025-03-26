// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Code1 (unoptimized)
// pseudo-code:
//
// int i;
// R2 = 0;
//
// for(i=0; i<R0; i++)
//		R2 += R1;
//
//@R2		// init R2=0
//M = 0
//@i		// i=0
//M=0
//
//(LOOP)
//@i
//D=M
//@R0
//D=D-M
//@END
//D;JEQ	// i<R0 ?
//
//@i		// i++
//M=M+1
//
//@R1		// R2=R2+R1
//D=M
//@R2
//M=M+D
//
//@LOOP
//0;JMP
//
//(END)
//@END
//0;JMP

// Code2 (optimized)
// pseudo-code:
//int i;
//R2=0;
//
//if(R0<R1)
//	for(i=0; i<=R0; i++)
//		R2 += R1;
//else
//	for(i=0; i<=R1; i++)
//		R2 += R0;

@R2
M=0
@i
M=0

@R0
D=M
@R1
D=D-M
@IF_BRANCH
D;JLT
@ELSE_BRANCH
0;JMP

(IF_BRANCH)
@i
D=M
@R0
D=D-M
@END
D;JEQ	// i<R0 ?

@i		// i++
M=M+1

@R1		// R2=R2+R1
D=M
@R2
M=M+D

@IF_BRANCH
0;JMP

(ELSE_BRANCH)
@i
D=M
@R1
D=D-M
@END
D;JEQ	// i<R1 ?

@i		// i++
M=M+1

@R0		// R2=R2+R0
D=M
@R2
M=M+D

@ELSE_BRANCH
0;JMP

(END)
@END
0;JMP