from fpdf import FPDF

class ChordPDFGenerator:
    def __init__(self, title, artist, chords_and_lyrics, key=None):
        self.title = title
        self.artist = artist
        self.chords_and_lyrics = chords_and_lyrics
        self.key = key
    
    def generate_pdf(self, filename):
        try:
            pdf = FPDF()
            pdf.add_page()
            
            # Create a mapping for Romanian characters
            romanian_map = {
                'ș': 's',
                'ț': 't',
                'ă': 'a',
                'î': 'i',
                'â': 'a',
                'Ș': 'S',
                'Ț': 'T',
                'Ă': 'A',
                'Î': 'I',
                'Â': 'A'
            }
            
            # Function to replace Romanian characters
            def replace_romanian(text):
                for rom, eng in romanian_map.items():
                    text = text.replace(rom, eng)
                return text
            
            # Set margins
            pdf.set_left_margin(20)
            pdf.set_right_margin(20)
            
            # Title and Artist
            pdf.set_font("Helvetica", size=22)
            title = replace_romanian(self.title)
            artist = replace_romanian(self.artist)
            pdf.cell(0, 10, f"{title} - {artist}", new_x="LMARGIN", new_y="NEXT", align='C')
            
            # Add some space after title
            pdf.ln(5)
            
            # Key information
            pdf.set_font("Helvetica", size=12, style="I")
            pdf.cell(0, 10, f"Key: {self.key}", new_x="LMARGIN", new_y="NEXT", align='C')
            
            # Add space before lyrics
            pdf.ln(10)
            
            # Lyrics with proper spacing
            pdf.set_font("Helvetica", size=14)  # Slightly smaller font
            line_height = 8  # Adjust line height
            
            for line in self.chords_and_lyrics.split("\n"):
                line = replace_romanian(line)
                if line.strip():  # Only process non-empty lines
                    if line.startswith(('Chorus:', 'Bridge:')):
                        pdf.ln(5)  # Add extra space before sections
                        pdf.set_font("Helvetica", size=14, style="B")
                        pdf.cell(0, line_height, line, new_x="LMARGIN", new_y="NEXT", align='L')
                        pdf.set_font("Helvetica", size=14, style="")  # Reset font
                    else:
                        pdf.cell(0, line_height, line, new_x="LMARGIN", new_y="NEXT", align='L')
                else:
                    pdf.ln(5)  # Add space for empty lines
            
            pdf.output(filename)
            print(f"PDF generated successfully: {filename}")
        except Exception as e:
            print(f"Error generating PDF: {str(e)}")
            import os
            print(f"Attempted to save at: {os.path.abspath(filename)}")


# Example usage
if __name__ == "__main__":
    title = "Tu Ești Credincios"
    artist = "Sunny Tranca"
    chords_and_lyrics = """
    C             F             C
    Tu ești credincios, tot ce faci e desăvârșit
    F             G       F             C   F
    Ce începi duci la bun sfârșit, o, Tată, Tu ești credincios

    Chorus:
    F             G        C         G/B   Am
    Îmi ridic mâinile spre Tine, în Tine-i nădejdea mea
    F             G        C        Dm     C/E
    Tu lucrezi Tată pentru mine, Tu nu mă vei abandona

    Bridge:
    C                       F  
    Eu sunt lucrarea Lui, lucrarea Tatălui  
    C                       F  
    Eu sunt lucrarea Lui, lucrarea Tatălui  
    C/E                 F             C/E  F  
    Eu sunt lucrarea Lui, lucrarea Tatălui  

    """
    key = "C Major"

    generator = ChordPDFGenerator(title, artist, chords_and_lyrics, key)
    generator.generate_pdf("tu_esti_credincios.pdf")