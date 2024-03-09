import requests
from Bio import SeqIO
import numpy as np

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

    def count_nucleotides(data, arr) -> list: 
        data = {"A": 0, "C": 0, "G": 0, "T": 0}

        for nuc in arr:
            data[nuc] += 1
        return data.values()
    
    def TranscribeDNAtoRNA(data) -> str:
        return(data.replace("T", "U"))

    def ReadingLines(arr=None, flname=None) -> dict:
        """
        trying to solve the problem for when im given a file and it has
        new lines and i need to read the lines and return the data to 
        be ablie to ComplementingDNA 

        F:\Athena/bioinfomatics/dna_data/
        """
        db = {}
        format_file = f"F:\Athena/bioinfomatics/dna_data/{flname}"
        with open(format_file) as handle:
            for record in SeqIO.parse(handle, "fasta"):
                db[record.id] = [record.seq]
        return db 

    def ComplementingDNA(data) -> str:
        #return data[::-1].translate(str.maketrans("ACGT", "TGCA"))
        if isinstance(data,list):
            return("data is a list")
        else:
            return("data is not a list")
        
    def ComputingGCContent(gc_content: dict) -> float:
        """
        Computing GC content
        """
        highest = 0
        name = '' 

        for keys in gc_content.keys():
            CG_count = (
                (gc_content[keys][0].count("G") + gc_content[keys][0].count("C"))
                / len(gc_content[keys][0]) * 100
            )



            gc_content[keys].append(CG_count)

            if CG_count > highest:
                highest, name = CG_count, keys
        return(f"the highest GC content is:\n{name} {highest}%")

    def HammingDistance(data: list) -> int: 
        """
        The Hamming distance between two strings of equal length is the number of positions at which the corresponding symbols are different.
        """
        sum = 0
        if len(data[1]) and len(data[0]) == len(data[1]):
            for i in range(len(data[0])):
                if data[0][i] != data[1][i]:
                    sum += 1

        return sum            
    
    def TranslatingRNAtoProtein(data: str) -> str:
        """
        Translating RNA to Protein
        """
        rna_codon = {
            "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
            "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
            "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
            "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
            "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
            "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
            "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
            "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
            "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
            "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
            "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
            "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
            "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
            "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
            "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
            "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
        }
        protein = ""
        for i in range(0, len(data), 3):
            if rna_codon[data[i:i+3]] == "Stop":
                break
            protein = protein + rna_codon[data[i:i+3]]
        print(protein)

    def FindingaMotifinDNA(data: list) -> str:
        """
        Finding a Motif in DNA
        """
        motif = data[1]
        dna = data[0]
        pos = ""
        for i in range(len(dna)):
            if dna[i:i+len(motif)] == motif:
                pos += str(i+1) + " "
        
        return(pos)
    
    def FindingaProteinMotif(data: str) -> str:
        """
        Finding a Protein Motif
        """
        motif = ["N",["S","T"]]
        pos = ""
        for i in range(len(data)):
            if data[i] == motif[0] and data[i+1] != "P" and data[i+3] != "P":
                if data[i+2] in motif[1]:
                    pos += str(i+1) + " "
        return(pos)
    
    def FindingaProteinMotifWithDatabase(data: list) -> list:
        """
        Finding a Protein Motif with Database
        """
        err = """Error messages
                The 'accession' value has invalid format. It should be a valid UniProtKB accession
            """
        db = []
        str = ""
        for id in data:
            url = f"http://www.uniprot.org/uniprot/{id}.fasta"
            response = requests.get(url)
            for line in response.text.splitlines():

                if line.startswith(">"):
                    db.append(line[4:line.rfind("|")])
                    #print(line[4:line.rfind("|")])
                else:
                    print(line(len(line)))
                    str += line
            db.append(str)
        return db

    def FindingaSharedMotif(data: list) -> str:
        """
        Finding a Shared Motif out of multiple DNA strings
        """
        freq = {}

        for i in range(len(data)):
            if data[i].startswith(">"):
                continue
            for j in range(len(data[i])):
                if data[i][j] in freq:
                    freq[data[i][j]] += 1
                else:
                    freq[data[i][j]] = 1
        return freq
    
    def Mendels_first_law(k, m, n):
       t = k + m + n # total population
       gen = [k, m, n] 
       prob_leaves = [] # the tree of probabilities
       base_p1 = [] # the first parents

       def calculate_probability_of_each_leaf(k, m, n):
           """
           calculates the probability of each leaf in the genetic tree.
           
           Args:
               k (int): Number of homozygous dominant alleles (GG)
               m (int): Number of heterozygous alleles (Gg)
               n (int): Number of homozygous recessive alleles (gg)
           """
           for i in range(0, len(gen)):
               base_p1.append(gen[i] / t)
               for j in range(0, len(gen)):
                   if i != j:
                       # Probability of dominant
                       prob_leaves.append(base_p1[i] * gen[j] / (t - 1))
                   else:
                       # Probability of recessive
                       prob_leaves.append(base_p1[i] * (gen[j] - 1) / (t - 1))

           dom_all = sum(prob_leaves)
           print(f"{prob_leaves}\n{dom_all}")
       

       def calculate_fraction_of_dominant_allele():
           """
           Calculates the fraction of dominant alleles in a genetic population.

           Returns:
           - None

           Prints:
           - The fraction of dominant alleles for each combination of genotypes.
           - The sum of the probabilities of each combination of genotypes.
           """
           GG = np.array([[0,0]])
           Gg = np.array([[0,1]])
           gg = np.array([[1,1]])

           frac = []
           sum_prob = []

           for iT in [GG, Gg, gg]:
               for i in [GG, Gg, gg]:
                   matrix = iT.T * i
                   dom = np.sum(matrix == 0) / 4
                   frac.append(dom)
           print(frac)
           
           for i in range(0, len(frac)):
               sum_prob.append(frac[i] * prob_leaves[i])
           print(sum(sum_prob))

       calculate_probability_of_each_leaf(k, m, n)
       calculate_fraction_of_dominant_allele()
        
if __name__ == "__main__":
    #flname = "rosalind_gc.txt"
    Bioinformatics.Mendels_first_law(28,23,16)

    #arr = "GATTACA\nTAGACCA\nATACA"
    #parsed = Bioinformatics.ReadingLines(arr=arr)
    #parsed = Bioinformatics.ReadingLines(flname=flname)
    #print(parsed)
    #print(Bioinformatics.ComputingGCContent(parsed))
    #print(parsed)
    #print(parsed)
    #print(Bioinformatics.FindingaMotifinDNA(parsed))
    #print(Bioinformatics.FindingaProteinMotif(parsed[0]))
    #print(Bioinformatics.FindingaProteinMotifWithDatabase(parsed))

    #print(Bioinformatics.FindingaSharedMotif(parsed))



 
