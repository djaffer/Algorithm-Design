# Encoding DNA/RNA Sequence Challenge

#

An example DNA / RNA sequences is like the following:

&quot;-Gdo-Gdo-Ado-Ado-Tdo-Gro-Gro-Cro-Uro-Uro-Uro-Ur&quot;

Each element in the sequence is encoded with a four letter pattern such as ​ **-Gdo** ​or -​ **Ums** ​.

1. The first character represents any special modifications to the base, or &quot; **-**&quot; if there are no modifications.
2. The second character represents the base, which encodes the genetic information of the DNA / RNA. For **-Gdo** and **-Ums** , the bases are **G** and **U** , respectively.
3. The third character represents the sugar backbone, with **r** for RNA, **d** for DNA, or        another special character such as **m**         ​ for a modified RNA sugar. For **-Gdo** and **-Ums** , the sugars are **d** and **m** , respectively. ** **
4. The fourth character represents the phosphate linkage, which joins each combined base and sugar unit of the sequence together. For - **Gdo** and **-Ums** , the linkages are **o** and **s** , respectively.

Important things to note:

- The final base and sugar unit do not have a linkage because there is no next unit to link to. So, a sequence that has _N_ bases will be represented by a string of length 4 × _N_ − 1.
- A sequence is best considered as alternating 3 character and 1 character elements instead 4 character elements. The first three characters form a single sugar-base chemical unit, or nucleoside.

# Question 1:

Sometimes we synthesize a sequence where the measured molecular masses does not agree with the mass of the input sequence. Verifying the number of base-sugar units in the sequence and mass of the sequence can be helpful to troubleshoot.

1. A)Write a function that takes the sequence string as input and returns the number of each of the different parts in the sequence (base-sugar units and linkages). For example, the input &quot;-Uro-Uro-Gro-Ums-Um&quot; should return 2 **-Ur** , 1 **-Gr** , 2 **-Um** ,3 **o** , and 1 **s** in some format (the implementation is up to you).

1. B)Write a function that takes the number of the different parts of the sequence as input and returns the mass of the sequence. Assume you could ask a chemist for a lookup table for the molecular masses of each part.

# Question 2:

Most customers want sequence strings that only show the bases. For example,

&quot;-Gdo-Gdo-Ado-Ado-Tdo-Gro-Gro-Cro-Uro-Uro-Uro-Ur&quot; could be represented as &quot;GGAATGGCUUUU&quot;. However, this representation mostly obscures the DNA vs. RNA information, so our shipping labels wrap DNA bases in square brackets. For example, the above sequence would be written as &quot;[GGAAT]GGCUUUU&quot;.

A) Write a function that takes a sequence as input and returns that sequence in shipping label format.

# Question 3:

Synthego often needs to validate customer provided sequence data against the following list of acceptable modifiers, bases, sugars, and linkages:

- acceptable modifiers : **-** , **m** , **b** , **i**
- acceptable bases : **A** , **G** ​, **C** , ​ **T** , **U** , **I**
- acceptable sugars : **d** , **r** , **m**         ​, **f** , **a** , **i** ​, **p**
- acceptable linkages : **o** , ​ **s**

A) Write a function that takes an arbitrary input sequence. If the sequence conforms to the definition of a sequence string above and acceptable inputs, indicate success. If the sequence fails to conform to the definition and acceptable inputs, indicate failure, the failure condition, and the position in the sequence string where the failure occurred.

** **