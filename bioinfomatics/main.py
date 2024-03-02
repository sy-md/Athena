import requests

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

    def ReadingLines(arr=None, flname=None):
        """
        trying to solve the problem for when im given a file and it has
        new lines and i need to read the lines and return the data to 
        be ablie to ComplementingDNA 

        F:\Athena/bioinfomatics/dna_data/
        """
        db = []
        new_line = -1
        format = f"F:\Athena/bioinfomatics/dna_data/{flname}"
        if flname:
            with open(format, 'r') as file:
                for i in (file):
                    if i.startswith(">"):
                        db.append(i[:new_line])
                    genome_sequence = ''
                    for line in file:
                        if line.startswith('>'):
                            break
                        genome_sequence += line[:new_line]
                    db.append(genome_sequence)
                    if line.startswith(">") != '>':
                        break
                    else:
                        db.append(line)
        if arr:
            return arr.splitlines()

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
        
if __name__ == "__main__":
    flname = "rosalind_lcsm.txt"
    #arr = "GATTACA\nTAGACCA\nATACA"
    #parsed = Bioinformatics.ReadingLines(arr=arr)
    parsed = Bioinformatics.ReadingLines(flname=flname)
    print(parsed)
    #print(Bioinformatics.FindingaMotifinDNA(parsed))
    #print(Bioinformatics.FindingaProteinMotif(parsed[0]))
    #print(Bioinformatics.FindingaProteinMotifWithDatabase(parsed))

    print(Bioinformatics.FindingaSharedMotif(parsed))



 