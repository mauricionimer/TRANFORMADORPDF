import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox

from pdf_generator import gerar_pdf


class TransformadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MIT Revisão Programada — Gerador de PDF")
        self.root.geometry("560x300")
        self.root.resizable(False, False)

        self.caminho_excel = ""

        tk.Label(root, text="Gerador de PDF — MIT Revisão Programada", font=("Arial", 15, "bold")).pack(pady=(16, 4))
        tk.Label(root, text="Selecione a planilha da edição e clique em Gerar PDF.", font=("Arial", 10)).pack(pady=(0, 16))

        frame = tk.LabelFrame(root, text=" Planilha da edição ", padx=10, pady=10)
        frame.pack(fill="x", padx=20, pady=5)

        self.lbl_excel = tk.Label(frame, text="Nenhuma planilha selecionada", fg="red")
        self.lbl_excel.pack(side="left", padx=(0, 10))
        tk.Button(frame, text="Selecionar Excel...", command=self.selecionar_excel).pack(side="right")

        self.btn_gerar = tk.Button(
            root, text="GERAR PDF", command=self.gerar,
            bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), height=2,
            state="disabled",
        )
        self.btn_gerar.pack(fill="x", padx=20, pady=20)

        self.lbl_status = tk.Label(root, text="", font=("Arial", 9))
        self.lbl_status.pack(pady=(0, 10))

    def selecionar_excel(self):
        caminho = filedialog.askopenfilename(
            title="Selecione a planilha da edição",
            filetypes=[("Excel", "*.xlsx")],
        )
        if caminho:
            self.caminho_excel = caminho
            self.lbl_excel.config(text=os.path.basename(caminho), fg="green")
            self.btn_gerar.config(state="normal")

    def gerar(self):
        if not self.caminho_excel:
            messagebox.showwarning("Atenção", "Selecione a planilha primeiro!")
            return

        destino = filedialog.asksaveasfilename(
            title="Salvar PDF como",
            defaultextension=".pdf",
            initialfile="MIT Revisão Programada.pdf",
            filetypes=[("PDF", "*.pdf")],
        )
        if not destino:
            return

        self.btn_gerar.config(state="disabled", text="Gerando...")
        self.lbl_status.config(text="Lendo a planilha e montando o PDF, aguarde...")
        self.root.update()

        thread = threading.Thread(target=self._gerar_em_segundo_plano, args=(destino,), daemon=True)
        thread.start()

    def _gerar_em_segundo_plano(self, destino):
        try:
            gerar_pdf(self.caminho_excel, destino)
        except Exception as e:
            self.root.after(0, self._erro, str(e))
        else:
            self.root.after(0, self._sucesso, destino)

    def _sucesso(self, destino):
        self.btn_gerar.config(state="normal", text="GERAR PDF")
        self.lbl_status.config(text="")
        messagebox.showinfo("Pronto!", f"PDF gerado com sucesso em:\n{destino}")

    def _erro(self, mensagem):
        self.btn_gerar.config(state="normal", text="GERAR PDF")
        self.lbl_status.config(text="")
        messagebox.showerror("Erro ao gerar PDF", mensagem)


if __name__ == "__main__":
    root = tk.Tk()
    app = TransformadorApp(root)
    root.mainloop()
