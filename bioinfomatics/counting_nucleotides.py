class Bioinformatics:
    def color_dnaoutput(data): # display colors
        bcloors = {
            "A": "\033[92m",
            "C": "\033[94m",
            "G": "\033[93m",
            "T": "\033[91m",
            "U": "\033[91m",
            "reset": "\033[0;0m"
        }
    
        tmpstr = ""

        for nuc in data:
            if nuc in bcloors:
                tmpstr += bcloors [nuc] + nuc + bcloors["reset"]
            else:
                tmpstr += bcloors["reset"] + nuc

        return tmpstr + "\033[0;0m"

    def count_nucleotides(data, arr): 
        data = {"A": 0, "C": 0, "G": 0, "T": 0}

        for nuc in arr:
            data[nuc] += 1
        return data.values()
    
    def TranscribeDNAtoRNA(data):
        print(data.replace("T", "U"))

     
    def ComplementingDNA(data):
        return data[::-1].translate(str.maketrans("ACGT", "TGCA"))

if __name__ == "__main__":
    arr = "GTTACAAGAATGCGGCCTGGGGTCGTAGAGCAGTCTACTTCTAGCCTACTCATTATACTTAATGGGTACACCAAATTACTCACTCAAGACGTATAGGACTAGAGTATCCAGAGGTATACAATAGGCGTTCTTTACGAACATGTTGCATTCTACAGTTCTCGGTGAGCGATCGCTAAGAACGGCTACGAGTGGGACTCCACCTGTGAGTTCCGCCGTATATGCCTAACTGTGACTTCTCTGCTGGGTCAGCACCCTGGGTGGGACGCGAGAGTTAGTTACGTCTTTCACCGGATTACGATTTCTTAGTAAGCGGTATTGCGGGTTTATGCCGTTCATTGCTCCGTAAACGGATCTGTGTCCTCCCATGCCGAGCTTGGGCGTAGTAACTTGTACGTTCTAGTAAACGACCCCCTAGCACATGGGTCGTTCTCAGCTTTCATAGGCCGTAGGAATGTCGCGCAGGAGATAACAATAAGGGTAGACGCGTAAGGGGGATACCATAGCTTTGTCAGAAACAATTGTCACCTGTCTACACACAATAGTGGTGGCTCTGGCAATTCTATTCACTATCGGCGCCCGCGCTCTATTACCATGTGAAGGGGTGTTTGTGTTCAAAGGATAGGCCTCGCGTGTAATCTCCCCTCGTGGCGGGAAAATCTAACATTTCAGACGTGAAAGTACTCATGAGGGACAGGTTAGGTTAAGGATGGGAAGGCATGGGCGCTCCCTTGTTTAGGCTCCCAATCGGGCACGCCAGACTAAGGTTGGTAATTGGTTGAGGAAAAGTGGCCGCATATGAA"
    res = (Bioinformatics.ComplementingDNA(arr))
    print(Bioinformatics.color_dnaoutput(res))