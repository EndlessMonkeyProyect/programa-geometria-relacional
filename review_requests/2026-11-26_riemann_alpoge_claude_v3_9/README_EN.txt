RIEMANN–ALPÖGE–CLAUDE | ENGLISH REVIEW EDITION 3.9

Purpose: independent examination of identities, equivalences, and proposed mathematical correspondences.
The English note is an adapted review edition of the complete Spanish v3.9, not a page-for-page translation. The English presentation and Issue text are tailored to the request. The Spanish original and original verification archive are retained unchanged.

To build the English PDFs: from english/, run pdflatex twice on review_note_EN.tex and review_slides_EN.tex (TeX Live with the packages declared in the source).

For numerical reproduction: extract original_spanish/Equivalencias_v3_9_fuente_y_verificacion.zip. Open its verificacion_v3_9 directory and run the scripts in this order:
  1. checks.py
  2. wnum.py
  3. gram.py
  4. disc.py
  5. fig.py
  6. vasyunin.py
  7. economia.py
  8. minm.py
  9. cadena_lc.py
Requirements: Python 3, NumPy, mpmath, Matplotlib. Consult the original LEEME.txt and SHA256SUMS.txt. Numerical results are reproduced in the supplied review reports; this English edition verifies file integrity but does not repeat the nine numerical runs or independently audit Lean. The original reports and source files retain their original language.

SHA256SUMS.txt in this archive covers the files delivered. Verify with sha256sum -c SHA256SUMS.txt from the extracted archive root.
