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
        if flname:
            
            format = f"F:\Athena/bioinfomatics/dna_data/{flname}"
            #format = f"dna_data/{flname}"
            with open(format, "r") as fl:
                return fl.read().splitlines()
        if arr:
            return arr.splitlines()
             
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

            
            
        

if __name__ == "__main__":
    flname = "rosalind_gc.txt"
    parsed = Bioinformatics.ReadingLines(flname=flname)
    Bioinformatics.MakingGCContnent(parsed)