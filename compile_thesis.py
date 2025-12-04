import subprocess
import os

def compile_thesis():
    # Path to your main .tex file
    main_tex = "thesis.tex"   # change to your main file name

    # Ensure script runs from the directory it's located in
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    try:
        print("Compiling thesis using latexmk...")

        # Run latexmk
        subprocess.run(
            ["latexmk", "-pdf", "-interaction=nonstopmode", main_tex],
            check=True
        )

        print("\n✔ Compilation complete!")
    except subprocess.CalledProcessError:
        print("\n❌ Error during compilation. Check LaTeX logs.")
    except FileNotFoundError:
        print("\n❌ latexmk not found. Install with: sudo apt install latexmk")

if __name__ == "__main__":
    compile_thesis()
