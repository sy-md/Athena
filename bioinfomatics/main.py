import requests
from pysam import FastaFile
from Bio import SeqIO

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
        return(data.replace("T", "U"))

    def ReadingLines(arr=None, flname=None):
        """
        for linux the file format is: "dna_data/rosalind_rna.txt"
        for windows the file format is: its the full path
        """
        db = {
            "database": [],
            "test" : ""
        }

        idd = ""
        mystring = ""

        fasta = f"dna_data/{flname}"
        if flname:
            with open(fasta, 'r') as file:
                for line in file.readlines():
                    if line.startswith(">"):
                        db[line] = []
                        print(f"the idd is: {line}")
                        idd = line

                    else:
                        #mystring += line.strip()
                        db["database"].append(line.strip())
                        #db[idd] = mystring
        if arr:
            for i in range(len(arr)):
                if arr[i].startswith(">"):
                    db[arr[i]] = []
                    idd = arr[i]
                else:
                    mystring += arr[i].strip()
                    db["test"] = mystring
        return db

    def ComplementingDNA(data):
        #return data[::-1].translate(str.maketrans("ACGT", "TGCA"))
        if isinstance(data,list):
            return("data is a list")
        else:
            return("data is not a list")
        
    def MakingGCContnent(data):
        """
        FASTA format:
            >Rosalind_6404
            ID "Rosaling_xxxx" {0...9}

        """
        gc_content = {}

        for i in range(len(data)):
            if data[i].startswith(">"):
                label = i
                gc_content[data[label]] = [data[label+1]]
        return Bioinformatics.ComputingGCContent(gc_content)
        #print(gc_content)
        
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
        print(f"the highest GC content is:\n{name} {highest}%")

    def HammingDistance(data: list) -> int: 
        """
        The Hamming distance between two strings of equal length is the number of
        positions at which the corresponding symbols are different.
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
        return(protein)

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
        mstr = ""
        for id in data["database"]:

            url = f"http://www.uniprot.org/uniprot/{id}.fasta"
            response = requests.get(url)
            for line in response.text.splitlines():

                if line.startswith(">"):
                    db.append(line[4:line.rfind("|")])
                    #print(line[4:line.rfind("|")])
                else:
                    print(line)
                    mstr += line
            db.append(str(mstr))
        return db

    def FindingaSharedMotif(data: dict) -> str:
        """
        Finding a Shared Motif out of multiple DNA strings
        using the longest common substring method
        """
        freq = {}

        for key, value in data.items():
            for i in range(len(value)):
                if value[i:i+2] in data[key]:
                    freq[value[i:i+2]] = freq.get(value[i:i+2], 0) + 1

        # return the longest substring
        return max(freq, key=freq.get)

    def TranslatingDNAtoProtein(data: str) -> str:
        """
        Translating DNA to Protein
        """
        dna_codon = {
            "TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V",
            "TTC": "F", "CTC": "L", "ATC": "I", "GTC": "V",
            "TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
            "TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V",
            "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
            "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
            "TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
            "TCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
            "TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
            "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
            "TAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
            "TAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
            "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G",
            "TGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
            "TGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
            "TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
        }
        protein = ""
        for i in range(0, len(data), 3):
            if dna_codon[data[i:i+3]] == "Stop":
                break
            protein +=  dna_codon[data[i:i+3]]
        return(protein)

    def ReadingFramesTranslations(data: str, pos) -> list:
        """
        this function returns the reading frames of the dna
        by using a for loop to iterate through the dna string
        and then using the dna_codon dictionary to translate the dna
        into protein creating 3 reading frames that is really 6 reading frames
        because the dna can be read in the reverse direction

        """
        dna_codon = {
            "TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V",
            "TTC": "F", "CTC": "L", "ATC": "I", "GTC": "V",
            "TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
            "TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V",
            "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
            "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
            "TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
            "TCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
            "TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
            "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
            "TAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
            "TAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
            "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G",
            "TGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
            "TGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
            "TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
        }
        return [dna_codon[data[i:i+3]] for i in range(pos, len(data)-2, 3)]

    def CalculatingProtiensMass(data: str) -> float:
        """
        Calculating Protein Mass
        """
        mass = {
            "A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259,
            "F": 147.06841, "G": 57.02146, "H": 137.05891, "I": 113.08406,
            "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293,
            "P": 97.05276, "Q": 128.05858, "R": 156.10111, "S": 87.03203,
            "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333
        }
        massa = 0
        for i in range(len(data)):
            massa += mass[data[i]]
        return massa

    def ComputeAllProteinFromOrf(data: str) -> list:
        """
        Compute All Protein From Orf
        """
        dna_codon = {
            "TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V",
            "TTC": "F", "CTC": "L", "ATC": "I", "GTC": "V",
            "TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
            "TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V",
            "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
            "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
            "TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
            "TCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
            "TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
            "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
            "TAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
            "TAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
            "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G",
            "TGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
            "TGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
            "TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
        }
        protein = []
        for i in range(0, len(data), 3):
            if dna == "ATG":
                protein.append(dna_codon[data[i:i+3]])
            if dna_codon[data[i:i+3]] == "Stop":
                break
            protein.append(dna_codon[data[i:i+3]])


if __name__ == "__main__":
    #flname = "rosalind_prtm.txt"
    arr = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
    #arr = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    parsed = Bioinformatics.ReadingLines(arr=arr)
    #parsed = Bioinformatics.ReadingLines(flname=flname)
    #print(parsed)
    #print(Bioinformatics.FindingaMotifinDNA(parsed))
    #print(B:ioinformatics.FindingaProteinMotif(parsed[0]))
    #print(Bioinformatics.FindingaProteinMotifWithDatabase(parsed))
    frames = []
    for i in range(3):
        frames.append(Bioinformatics.ReadingFramesTranslations(parsed["test"], i))
        print(f"the reading frame {i+1} is: {frames[i]}")



 
