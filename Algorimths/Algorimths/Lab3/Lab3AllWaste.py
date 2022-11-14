# def Merge(A, p, r, q):
#     nl = q-p+1
#     nr = r-q
#
#     L = []
#     R = []
#     for i in range(0, nl):
#         L.append(A[p + i])
#     for i in range(0, nr):
#         R.append(A[q + 1 + i])
#     # print("p = ", p)
#     # print("r = ", r)
#     # print("q = ", q)
#     # print(" L = ", L)
#     # print(" R = ", R)
#     i = 0
#     j = 0
#     for k in range(p, nr+nl):
#         if i < len(L) and j < len(R):
#             if L[i] <= R[j]:
#                 A[k] = L[i]
#                 i += 1
#             else:
#                 A[k] = R[j]
#                 j += 1
#         else:
#             if j < len(R):
#                 A[k] = R[j]
#                 j += 1
#             else:
#                 A[k] = L[i]
#                 i += 1
#
#
# def MergeSort(A, p, r):
#     if p < r:
#         q = (p + r) // 2
#         MergeSort(A, p, q)
#         MergeSort(A, q + 1, r)
#         Merge(A, p, r, q)

#def MergeTwoMassive(A,B, p, r, q):
#     nl = q - p + 1
#     nr = r - q
#
#     LA = []
#     RA = []
#     LB = []
#     RB = []
#     for i in range(0, nl):
#         LA.append(A[p + i])
#         LB.append(B[p + i])
#     # print("L = ",L)
#     for i in range(0, nr):
#         RA.append(A[q + 1 + i])
#         RB.append(B[q + 1 + i])
#     # print("R = ", R)
#
#     i = 0
#     j = 0
#     k = p
#     while i < len(LA) and j < len(RA):
#         if LA[i] <= RA[j]:
#             A[k] = LA[i]
#             B[k] = LB[i]
#             i += 1
#         else:
#             A[k] = RA[j]
#             B[k] = RB[j]
#             j += 1
#
#         k += 1
#
#     while i < len(LA):
#         A[k] = LA[i]
#         B[k] = LB[i]
#         i += 1
#         k += 1
#
#     while j < len(RA):
#         A[k] = RA[j]
#         B[k] = RB[j]
#         j += 1
#         k += 1
#
#
#
# def MergeSortTwoMassive(A,B, p, r):
#     if p < r:
#         q = (p + r) // 2
#         MergeSortTwoMassive(A,B, p, q)
#         MergeSortTwoMassive(A,B, q + 1, r)
#         MergeTwoMassive(A,B, p, r, q)

# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================

# def main():
#     mas1 = TakeOneMas(237)
#     mas2 = TakeOneMas(989)
#     masM = BuildDifference(mas1, mas2)
#     res = MergeSortCountInversion(masM, 0, len(masM) - 1)
#     print("res = ", res)
#     sum = CalculateCollaborativeFiltering(res, len(masM))
#     print("sum = ", sum)
#
#     mas = [5, 4, 3, 2, 1]
#     res = MergeSortCountInversion(mas, 0, len(mas) - 1)
#     print("res = ", res)
#     masA = [3, 2, 4, 5, 1]
#     masB = [2, 5, 3, 1, 4]
#     masC = [5, 3, 4, 1, 2]
#     # print(masA)
#     # print(masB)
#     # # MergeSortTwoMassive(masA,masB, 0, len(masA) - 1)
#     masM = BuildDifference(masA, masB)
#     masM1 = BuildDifference(masA, masC)
#     #
#     #
#     print("count inversion check:")
#     res = MergeSortCountInversion(masM, 0, len(masM) - 1)
#     # print("M = ", masM)
#     print("res = ", res)
#     sum = CalculateCollaborativeFiltering(res, len(masM))
#     print("sum = ", sum)
#
#     print()
#     print("count inversion check:")
#     res = MergeSortCountInversion(masM1, 0, len(masM1) - 1)
#     # print("M = ", masM1)
#     print("res = ", res)
#     sum = CalculateCollaborativeFiltering(res, len(masM1))
#     print("sum = ", sum)

    # ==================================================================================================================
    # mas3 = [1, 5, 6,  2, 3,4]
    # print(mas3)
    # inv = 0
    # inv = MergeCountInversioun(mas3, 0,(0+len(mas3) - 1)//2, len(mas3) - 1, inv)
    # print(mas3)
    # print(inv)
    # ==================================================================================================================

    # masA = [5, 3, 1, 2, 4]
    # print(masA)
    # res = MergeSortCountInversion(masA, 0, len(masA) - 1)
    # print(masA)
    # print("inv = ", res)
    # masB = [3, ]
    # print(masB)
    # MergeSortCountInversion(masB, 0, len(masB) - 1)
    # print(masB)
    # mas = TakeOneMas(1)
    # print(mas)
    # MergeSortCountInversion(mas, 0, len(mas)- 1)
    # print(mas)



    # print("input number from 1 to 1000")
    # a = int(input())
    # mas1 = TakeOneMas(a)
    # print(mas1)
    # MergeSort(mas1, 0, len(mas1) - 1)
    # print(mas1)