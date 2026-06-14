from datetime import datetime


class DNASequence:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence.upper().strip()

    def is_valid(self):
        valid_bases = {"A", "T", "G", "C"}

        for base in self.sequence:
            if base not in valid_bases:
                return False

        return True


class MutationAnalyzer:
    def __init__(self, original_dna, variant_dna):
        self.original = original_dna
        self.variant = variant_dna

    def calculate_hamming_distance(self):
        distance = 0

        for i in range(len(self.original.sequence)):
            if self.original.sequence[i] != self.variant.sequence[i]:
                distance += 1

        return distance

    def generate_report(self):
        if not self.original.is_valid() or not self.variant.is_valid():
            return "Error: One or both DNA sequences contain invalid characters!"

        if len(self.original.sequence) != len(self.variant.sequence):
            return "Error: DNA sequences must have the same length!"

        total_length = len(self.original.sequence)
        mutations = self.calculate_hamming_distance()
        distance_percentage = (mutations / total_length) * 100

        if distance_percentage > 20:
            risk_level = "HIGH RISK - Significant genetic difference detected."
        elif distance_percentage > 5:
            risk_level = "MEDIUM RISK - Moderate mutation level detected."
        else:
            risk_level = "LOW RISK - Low mutation level detected."

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        report_text = "==================================================\n"
        report_text += "BIOLOGIX - DNA MUTATION REPORT\n"
        report_text += f"Timestamp: {current_time}\n"
        report_text += "==================================================\n"
        report_text += f"Original Sample: {self.original.name} ({self.original.sequence})\n"
        report_text += f"Variant Sample: {self.variant.name} ({self.variant.sequence})\n"
        report_text += f"Sequence Length: {total_length} bases\n"
        report_text += f"Total Mutations Found: {mutations}\n"
        report_text += f"Evolutionary Distance: {distance_percentage:.2f}%\n"
        report_text += f"Risk Level: {risk_level}\n"
        report_text += "Note: This program is an educational simulation and not a medical diagnosis tool.\n"
        report_text += "==================================================\n"

        return report_text

    def save_report_to_file(self, report_content, filename="mutation_report.txt"):
        with open(filename, "a", encoding="utf-8") as file:
            file.write(report_content + "\n")

        print(f"Report saved to '{filename}'")


print("Welcome to BioLogix Application!")

orig_name = input("Enter the name of the original DNA sample: ")
orig_seq = input("Enter the original DNA sequence: ")

original_dna = DNASequence(orig_name, orig_seq)

var_name = input("Enter the name of the variant DNA sample: ")
var_seq = input("Enter the variant DNA sequence: ")

variant_dna = DNASequence(var_name, var_seq)

analyzer = MutationAnalyzer(original_dna, variant_dna)

final_report = analyzer.generate_report()

print("\n" + final_report)

if "Error" not in final_report:
    save_choice = input("Do you want to save this report? (yes/no): ").lower().strip()

    if save_choice == "yes" or save_choice == "y":
        analyzer.save_report_to_file(final_report)