def medians(nums1, nums2):
    union = nums1 + nums2
    union.sort()
    delenie = len(union) // 2
    if len(union) % 2 == 0:
        mediana_chet = (union[delenie] + union[delenie - 1]) / 2
        return print(mediana_chet)
    elif len(nums1) == 0 and len(nums2) == 0:
        mediana = nums1 + nums2
        return print(mediana)
    else:
        mediana_nechet = union[delenie]
        return print(mediana_nechet)

