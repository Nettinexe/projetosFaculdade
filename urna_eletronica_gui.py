#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Urna Eletrônica - GUI (Tkinter) – v3.1
--------------------------------------
Novidade:
- (Admin) Remoção de eleitores: selecione um ou mais na aba "Eleitores" do Painel Admin e clique em
  "Remover selecionado(s)". Se algum já tiver votado, é solicitado confirmação. A apuração não é alterada.

Mantido da v3.0:
- Tela principal em TELA INTEIRA, somente Votação.
- Painel Admin em pop-up com abas (Configuração, Candidatos, Eleitores, Resultados, Segurança), protegido por PIN.
- Persistência JSON, log de auditoria, imagens de candidatos, cadastro de eleitor com nome, limpeza após confirmar voto.
"""

import os
import json
import hashlib
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog

try:
    from PIL import Image, ImageTk
    PIL_OK = True
except Exception:
    PIL_OK = False

STATE_FILE = os.path.join(os.path.dirname(__file__), 'election_state.json')
AUDIT_FILE = os.path.join(os.path.dirname(__file__), 'audit_log.txt')
DEFAULT_ADMIN_PIN = '1234'

PHOTO_WIDTH = 200
PHOTO_HEIGHT = 220


def now_iso():
    return datetime.now().isoformat(timespec='seconds')


def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def load_image(path, width=PHOTO_WIDTH, height=PHOTO_HEIGHT):
    if not path or not os.path.exists(path):
        return None, "Imagem não encontrada."
    try:
        if PIL_OK:
            img = Image.open(path)
            img = img.convert("RGBA")
            img = img.resize((width, height), Image.LANCZOS)
            return ImageTk.PhotoImage(img), None
        else:
            img = tk.PhotoImage(file=path)  # PNG/GIF
            return img, None
    except Exception as e:
        return None, f"Falha ao carregar imagem: {e}"


class ElectionState:
    def __init__(self):
        self.data = {
            "meta": {
                "name": "Eleição",
                "created_at": now_iso(),
                "admin_pin_hash": sha256_hex(DEFAULT_ADMIN_PIN),
                "is_open": False,
                "auto_register_voter": False,
            },
            # number -> {"name":str, "party":str, "image":str}
            "candidates": {},
            # voter_id -> {"name":str, "has_voted":bool, "registered_at":iso}
            "voters": {},
            "tally": {
                "valid": {},
                "blank": 0,
                "null": 0,
                "total": 0
            }
        }

    # ---------- Persistence ----------
    def load(self):
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            # retrocompatibilidade
            for num, info in list(self.data.get("candidates", {}).items()):
                info.setdefault("image", "")
            for vid, info in list(self.data.get("voters", {}).items()):
                info.setdefault("name", "")

    def save(self):
        with open(STATE_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    # ---------- Audit ----------
    def audit(self, message: str):
        with open(AUDIT_FILE, 'a', encoding='utf-8') as f:
            f.write(f"[{now_iso()}] {message}\n")

    # ---------- Meta ----------
    @property
    def is_open(self) -> bool:
        return bool(self.data["meta"]["is_open"])

    def set_open(self, open_flag: bool):
        self.data["meta"]["is_open"] = bool(open_flag)
        self.save()
        self.audit(f"Eleição {'ABERTA' if open_flag else 'FECHADA'}.")

    def set_name(self, name: str):
        self.data["meta"]["name"] = name
        self.save()
        self.audit(f"Nome da eleição definido: {name}")

    def set_auto_register(self, flag: bool):
        self.data["meta"]["auto_register_voter"] = bool(flag)
        self.save()
        self.audit(f"Cadastro automático de eleitor: {'ATIVO' if flag else 'INATIVO'}")

    def set_admin_pin(self, pin: str):
        self.data["meta"]["admin_pin_hash"] = sha256_hex(pin)
        self.save()
        self.audit("PIN do administrador alterado.")

    def verify_admin_pin(self, pin: str) -> bool:
        return sha256_hex(pin) == self.data["meta"]["admin_pin_hash"]

    # ---------- Candidates ----------
    def add_candidate(self, number: str, name: str, party: str = "", image: str = "") -> bool:
        number = str(number).strip()
        if not number.isdigit() or number == "0":
            return False
        if number in self.data["candidates"]:
            return False
        self.data["candidates"][number] = {"name": name.strip(), "party": party.strip(), "image": image.strip()}
        self.data["tally"]["valid"][number] = 0
        self.save()
        self.audit(f"Candidato cadastrado: {number} - {name} ({party}) img={bool(image)}")
        return True

    def update_candidate_image(self, number: str, image_path: str) -> bool:
        number = str(number).strip()
        cand = self.data["candidates"].get(number)
        if not cand:
            return False
        cand["image"] = image_path.strip()
        self.save()
        self.audit(f"Imagem do candidato {number} atualizada.")
        return True

    def remove_candidate(self, number: str) -> bool:
        number = str(number).strip()
        if number in self.data["candidates"]:
            self.data["candidates"].pop(number)
            self.data["tally"]["valid"].pop(number, None)
            self.save()
            self.audit(f"Candidato removido: {number}")
            return True
        return False

    def list_candidates(self):
        return self.data["candidates"]

    # ---------- Voters ----------
    def add_voter(self, voter_id: str, voter_name: str = "") -> bool:
        voter_id = voter_id.strip()
        if not voter_id:
            return False
        if voter_id in self.data["voters"]:
            return False
        self.data["voters"][voter_id] = {"name": voter_name.strip(), "has_voted": False, "registered_at": now_iso()}
        self.save()
        self.audit(f"Eleitor cadastrado: {voter_id} ({voter_name.strip()})")
        return True

    def remove_voter(self, voter_id: str) -> bool:
        """Remove o eleitor do cadastro. Não altera apuração já realizada."""
        voter_id = voter_id.strip()
        if voter_id in self.data["voters"]:
            self.data["voters"].pop(voter_id)
            self.save()
            self.audit(f"Eleitor removido: {voter_id}")
            return True
        return False

    def has_voted(self, voter_id: str) -> bool:
        v = self.data["voters"].get(voter_id)
        return bool(v and v.get("has_voted"))

    def mark_voted(self, voter_id: str):
        if voter_id in self.data["voters"]:
            self.data["voters"][voter_id]["has_voted"] = True
        else:
            if self.data["meta"]["auto_register_voter"]:
                self.data["voters"][voter_id] = {"name": "", "has_voted": True, "registered_at": now_iso()}
                self.audit(f"Eleitor auto-cadastrado ao votar: {voter_id}")
            else:
                raise ValueError("Eleitor não cadastrado.")
        self.save()

    # ---------- Voting ----------
    def cast_vote(self, voter_id: str, number_str: str) -> str:
        voter_id = voter_id.strip()
        if not self.is_open:
            raise RuntimeError("A eleição não está aberta para votação.")
        if self.has_voted(voter_id):
            raise RuntimeError("Este eleitor já votou.")

        number_str = str(number_str).strip()
        if number_str == "0":
            self.data["tally"]["blank"] += 1
            result_type = "BRANCO"
        elif number_str in self.data["candidates"]:
            self.data["tally"]["valid"][number_str] += 1
            result_type = "VÁLIDO"
        else:
            self.data["tally"]["null"] += 1
            result_type = "NULO"

        self.data["tally"]["total"] += 1
        self.mark_voted(voter_id)
        self.save()
        self.audit(f"Voto registrado: tipo={result_type}")
        return result_type

    # ---------- Results ----------
    def results(self):
        tally = self.data["tally"]
        total = max(1, tally["total"])
        items = []
        for num, count in sorted(tally["valid"].items(), key=lambda kv: (-kv[1], kv[0])):
            cand = self.data["candidates"].get(num, {"name": "Candidato removido", "party": "", "image": ""})
            items.append({
                "number": num,
                "name": cand["name"],
                "party": cand.get("party", ""),
                "image": cand.get("image", ""),
                "votes": count,
                "percent": (count / total) * 100.0
            })
        blank = {"label": "BRANCO", "votes": tally["blank"], "percent": (tally["blank"] / total) * 100.0}
        null = {"label": "NULO", "votes": tally["null"], "percent": (tally["null"] / total) * 100.0}
        return items, blank, null, tally["total"]

    def reset_all(self, confirm_text: str) -> bool:
        if confirm_text != "APAGAR TUDO":
            return False
        name = self.data["meta"]["name"]
        self.__init__()
        self.data["meta"]["name"] = name
        self.save()
        self.audit("Todos os dados foram APAGADOS (reset).")
        return True


# ------------------------------ Admin Panel (Toplevel) ------------------------------
class AdminPanel(tk.Toplevel):
    def __init__(self, master, state: ElectionState, on_state_changed=None):
        super().__init__(master)
        self.title("Painel do Administrador")
        self.state_obj = state
        self.on_state_changed = on_state_changed or (lambda: None)

        # Modal-like behavior
        self.transient(master)
        self.grab_set()

        self.geometry("1100x720")
        try:
            if os.name == "nt":
                self.state("zoomed")
        except Exception:
            pass

        self._build_ui()
        self._refresh_all()

    def _build_ui(self):
        # Notebook with all admin tools
        self.nb = ttk.Notebook(self)
        self.nb.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Tabs
        self.tab_config = ttk.Frame(self.nb)
        self.tab_candidates = ttk.Frame(self.nb)
        self.tab_voters = ttk.Frame(self.nb)
        self.tab_results = ttk.Frame(self.nb)
        self.tab_security = ttk.Frame(self.nb)

        self.nb.add(self.tab_config, text="Configuração")
        self.nb.add(self.tab_candidates, text="Candidatos")
        self.nb.add(self.tab_voters, text="Eleitores")
        self.nb.add(self.tab_results, text="Resultados")
        self.nb.add(self.tab_security, text="Segurança")

        self._build_config_tab()
        self._build_candidates_tab()
        self._build_voters_tab()
        self._build_results_tab()
        self._build_security_tab()

    # ---------- CONFIG ----------
    def _build_config_tab(self):
        f = self.tab_config

        frm_name = ttk.LabelFrame(f, text="Nome da eleição")
        frm_name.pack(fill=tk.X, padx=10, pady=10)
        self.entry_name = ttk.Entry(frm_name)
        self.entry_name.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
        ttk.Button(frm_name, text="Salvar nome", command=self._save_name).pack(side=tk.LEFT, padx=5)

        frm_flags = ttk.LabelFrame(f, text="Status e opções")
        frm_flags.pack(fill=tk.X, padx=10, pady=10)
        ttk.Button(frm_flags, text="Abrir eleição", command=lambda: self._set_open(True)).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(frm_flags, text="Fechar eleição", command=lambda: self._set_open(False)).pack(side=tk.LEFT, padx=5, pady=5)

        self.auto_var = tk.BooleanVar(value=self.state_obj.data["meta"]["auto_register_voter"])
        self.chk_auto = ttk.Checkbutton(frm_flags, text="Cadastro automático ao votar", variable=self.auto_var,
                                        command=self._toggle_auto_register)
        self.chk_auto.pack(side=tk.LEFT, padx=10, pady=5)

    def _save_name(self):
        name = self.entry_name.get().strip()
        if not name:
            messagebox.showwarning("Atenção", "Nome inválido.")
            return
        self.state_obj.set_name(name)
        self.on_state_changed()
        messagebox.showinfo("OK", "Nome atualizado.")

    def _set_open(self, flag: bool):
        self.state_obj.set_open(flag)
        self.on_state_changed()
        messagebox.showinfo("OK", f"Eleição {'aberta' if flag else 'fechada'}.")

    def _toggle_auto_register(self):
        self.state_obj.set_auto_register(self.auto_var.get())
        messagebox.showinfo("OK", "Configuração de auto-cadastro atualizada.")

    # ---------- CANDIDATES ----------
    def _build_candidates_tab(self):
        f = self.tab_candidates

        frm_list = ttk.LabelFrame(f, text="Candidatos cadastrados")
        frm_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree_cands = ttk.Treeview(frm_list, columns=("num", "nome", "partido", "votos"), show="headings", height=10)
        for col, w in zip(("num", "nome", "partido", "votos"), (90, 260, 140, 80)):
            self.tree_cands.heading(col, text=col.upper())
            self.tree_cands.column(col, width=w, anchor=tk.CENTER if col in ("num","votos") else tk.W)
        self.tree_cands.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        frm_add = ttk.LabelFrame(f, text="Adicionar / Atualizar / Remover")
        frm_add.pack(fill=tk.X, padx=10, pady=10)

        ttk.Label(frm_add, text="Número:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        ttk.Label(frm_add, text="Nome:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        ttk.Label(frm_add, text="Partido:").grid(row=0, column=4, padx=5, pady=5, sticky="e")
        ttk.Label(frm_add, text="Imagem:").grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.ent_cnum = ttk.Entry(frm_add, width=10)
        self.ent_cname = ttk.Entry(frm_add, width=30)
        self.ent_cparty = ttk.Entry(frm_add, width=20)
        self.ent_cimg = ttk.Entry(frm_add, width=40)

        self.ent_cnum.grid(row=0, column=1, padx=5, pady=5)
        self.ent_cname.grid(row=0, column=3, padx=5, pady=5)
        self.ent_cparty.grid(row=0, column=5, padx=5, pady=5)
        self.ent_cimg.grid(row=1, column=1, columnspan=4, padx=5, pady=5, sticky="we")
        ttk.Button(frm_add, text="Selecionar imagem...", command=self._choose_image).grid(row=1, column=5, padx=5, pady=5)

        ttk.Button(frm_add, text="Adicionar", command=self._add_candidate).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        ttk.Button(frm_add, text="Atualizar imagem (pelo número)", command=self._update_candidate_image).grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="w")
        ttk.Button(frm_add, text="Remover selecionado", command=self._remove_candidate).grid(row=2, column=5, padx=5, pady=5, sticky="e")

    def _choose_image(self):
        path = filedialog.askopenfilename(title="Escolher imagem do candidato",
                                          filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.gif"), ("Todos", "*.*")])
        if path:
            self.ent_cimg.delete(0, tk.END)
            self.ent_cimg.insert(0, path)

    def _add_candidate(self):
        num = self.ent_cnum.get().strip()
        name = self.ent_cname.get().strip()
        party = self.ent_cparty.get().strip()
        image = self.ent_cimg.get().strip()
        if not num or not name:
            messagebox.showwarning("Atenção", "Informe número e nome.")
            return
        if self.state_obj.add_candidate(num, name, party, image):
            self._refresh_candidates()
            self.ent_cnum.delete(0, tk.END)
            self.ent_cname.delete(0, tk.END)
            self.ent_cparty.delete(0, tk.END)
            messagebox.showinfo("OK", "Candidato adicionado.")
        else:
            messagebox.showerror("Erro", "Falha ao adicionar. Número inválido/duplicado ou 0.")

    def _update_candidate_image(self):
        num = self.ent_cnum.get().strip()
        image = self.ent_cimg.get().strip()
        if not num or not image:
            messagebox.showwarning("Atenção", "Informe o número do candidato e selecione a imagem.")
            return
        if self.state_obj.update_candidate_image(num, image):
            self._refresh_candidates()
            messagebox.showinfo("OK", "Imagem atualizada.")
        else:
            messagebox.showerror("Erro", "Não foi possível atualizar a imagem (verifique o número).")

    def _remove_candidate(self):
        sel = self.tree_cands.selection()
        if not sel:
            messagebox.showwarning("Atenção", "Selecione um candidato na lista.")
            return
        num = self.tree_cands.item(sel[0], "values")[0]
        if self.state_obj.remove_candidate(num):
            self._refresh_candidates()
            messagebox.showinfo("OK", "Candidato removido.")
        else:
            messagebox.showerror("Erro", "Não foi possível remover.")

    # ---------- VOTERS ----------
    def _build_voters_tab(self):
        f = self.tab_voters

        frm_list = ttk.LabelFrame(f, text="Eleitores")
        frm_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree_voters = ttk.Treeview(frm_list, columns=("id", "nome", "votou", "cadastro"), show="headings", height=12, selectmode="extended")
        headers = ("ID", "NOME", "VOTOU", "CADASTRO")
        widths = (180, 220, 80, 220)
        for (col, head, w) in zip(("id","nome","votou","cadastro"), headers, widths):
            self.tree_voters.heading(col, text=head)
            self.tree_voters.column(col, width=w, anchor=tk.CENTER if col in ("votou",) else tk.W)
        self.tree_voters.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        frm_add = ttk.LabelFrame(f, text="Adicionar eleitor")
        frm_add.pack(fill=tk.X, padx=10, pady=10)
        ttk.Label(frm_add, text="ID do eleitor:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        ttk.Label(frm_add, text="Nome do eleitor:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.ent_vid = ttk.Entry(frm_add, width=24)
        self.ent_vname = ttk.Entry(frm_add, width=28)
        self.ent_vid.grid(row=0, column=1, padx=5, pady=5)
        self.ent_vname.grid(row=0, column=3, padx=5, pady=5)
        ttk.Button(frm_add, text="Adicionar", command=self._add_voter).grid(row=0, column=4, padx=8, pady=5)

        frm_actions = ttk.Frame(f)
        frm_actions.pack(fill=tk.X, padx=10, pady=5)
        ttk.Button(frm_actions, text="Remover selecionado(s)", command=self._remove_selected_voters).pack(side=tk.LEFT, padx=5)

    def _add_voter(self):
        vid = self.ent_vid.get().strip()
        vname = self.ent_vname.get().strip()
        if not vid:
            messagebox.showwarning("Atenção", "Informe um ID.")
            return
        if self.state_obj.add_voter(vid, vname):
            self.ent_vid.delete(0, tk.END)
            self.ent_vname.delete(0, tk.END)
            self._refresh_voters()
            messagebox.showinfo("OK", "Eleitor cadastrado.")
        else:
            messagebox.showerror("Erro", "Falha: ID inválido ou já existe.")

    def _remove_selected_voters(self):
        sel = self.tree_voters.selection()
        if not sel:
            messagebox.showwarning("Atenção", "Selecione um ou mais eleitores para remover.")
            return

        ids = []
        voted_count = 0
        for item in sel:
            vid, name, voted, _ = self.tree_voters.item(item, "values")
            ids.append(vid)
            if str(voted).lower().startswith("s"):  # "Sim"
                voted_count += 1

        if voted_count > 0:
            if not messagebox.askyesno(
                "Confirmação",
                f"{voted_count} selecionado(s) já votaram. Remover mesmo assim?\n"
                "Isso NÃO altera a apuração, apenas remove o cadastro."
            ):
                return

        removed = 0
        for vid in ids:
            if self.state_obj.remove_voter(vid):
                removed += 1

        self._refresh_voters()
        messagebox.showinfo("Remoção concluída", f"{removed} eleitor(es) removido(s).")

    # ---------- RESULTS ----------
    def _build_results_tab(self):
        f = self.tab_results

        frm_tot = ttk.LabelFrame(f, text="Resumo")
        frm_tot.pack(fill=tk.X, padx=10, pady=10)
        self.lbl_total = ttk.Label(frm_tot, text="Total de votos: 0")
        self.lbl_total.pack(side=tk.LEFT, padx=10, pady=5)

        frm_table = ttk.LabelFrame(f, text="Apuração")
        frm_table.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree_results = ttk.Treeview(frm_table, columns=("num","nome","partido","votos","percent"), show="headings", height=10)
        for col, w in zip(("num","nome","partido","votos","percent"), (90, 260, 140, 80, 100)):
            self.tree_results.heading(col, text=col.upper())
            self.tree_results.column(col, width=w, anchor=tk.CENTER if col in ("num","votos","percent") else tk.W)
        self.tree_results.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.lbl_blank = ttk.Label(f, text="BRANCO: 0 (0,00%)")
        self.lbl_null = ttk.Label(f, text="NULO: 0 (0,00%)")
        self.lbl_blank.pack(padx=10, pady=(0,5), anchor="w")
        self.lbl_null.pack(padx=10, pady=(0,10), anchor="w")

        frm_buttons = ttk.Frame(f)
        frm_buttons.pack(fill=tk.X, padx=10, pady=5)
        ttk.Button(frm_buttons, text="Atualizar", command=self._refresh_results).pack(side=tk.LEFT, padx=5)
        ttk.Button(frm_buttons, text="Encerrar e Apurar", command=self._close_and_show_final).pack(side=tk.RIGHT, padx=5)

    def _close_and_show_final(self):
        # Extra segurança: confirmar com PIN novamente
        pin = simpledialog.askstring("PIN", "PIN do administrador:", show="*")
        if pin is None:
            return
        if not self.state_obj.verify_admin_pin(pin):
            messagebox.showerror("Erro", "PIN inválido.")
            return
        self.state_obj.set_open(False)
        self._refresh_results()
        self.on_state_changed()
        messagebox.showinfo("Apuração", "Eleição encerrada. Resultados atualizados.")

    # ---------- SECURITY ----------
    def _build_security_tab(self):
        f = self.tab_security

        frm_pin = ttk.LabelFrame(f, text="Segurança")
        frm_pin.pack(fill=tk.X, padx=10, pady=10)
        ttk.Button(frm_pin, text="Alterar PIN do administrador", command=self._change_pin).pack(side=tk.LEFT, padx=5, pady=5)

        frm_reset = ttk.LabelFrame(f, text="Reset total")
        frm_reset.pack(fill=tk.X, padx=10, pady=10)
        ttk.Label(frm_reset, text="Para confirmar, digite exatamente: APAGAR TUDO").pack(side=tk.LEFT, padx=5, pady=5)
        self.ent_reset = ttk.Entry(frm_reset, width=24)
        self.ent_reset.pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(frm_reset, text="Apagar tudo", command=self._do_reset).pack(side=tk.LEFT, padx=5, pady=5)

    def _change_pin(self):
        old = simpledialog.askstring("PIN", "PIN atual:", show="*")
        if old is None:
            return
        if not self.state_obj.verify_admin_pin(old):
            messagebox.showerror("Erro", "PIN atual incorreto.")
            return
        new1 = simpledialog.askstring("PIN", "Novo PIN:", show="*")
        if new1 is None or not new1:
            messagebox.showwarning("Atenção", "PIN inválido.")
            return
        new2 = simpledialog.askstring("PIN", "Confirme o novo PIN:", show="*")
        if new1 != new2:
            messagebox.showerror("Erro", "Confirmação não confere.")
            return
        self.state_obj.set_admin_pin(new1)
        messagebox.showinfo("OK", "PIN alterado com sucesso.")

    def _do_reset(self):
        txt = self.ent_reset.get().strip()
        if self.state_obj.reset_all(txt):
            self.ent_reset.delete(0, tk.END)
            self._refresh_all()
            self.on_state_changed()
            messagebox.showinfo("OK", "Todos os dados foram apagados.")
        else:
            messagebox.showerror("Erro", "Texto de confirmação incorreto. Nada foi apagado.")

    # ---------- Refresh helpers ----------
    def _refresh_candidates(self):
        for i in self.tree_cands.get_children():
            self.tree_cands.delete(i)
        cands = self.state_obj.list_candidates()
        items, _, _, _ = self.state_obj.results()
        vote_map = {it["number"]: it["votes"] for it in items}
        for num in sorted(cands.keys(), key=lambda x: (len(x), x)):
            info = cands[num]
            votos = vote_map.get(num, 0)
            self.tree_cands.insert("", tk.END, values=(num, info["name"], info.get("party",""), votos))

    def _refresh_voters(self):
        for i in self.tree_voters.get_children():
            self.tree_voters.delete(i)
        voters = self.state_obj.data["voters"]
        items = list(voters.items())
        items.sort(key=lambda kv: kv[1]["registered_at"], reverse=True)
        for vid, info in items[:400]:
            name = info.get("name", "")
            self.tree_voters.insert("", tk.END, values=(vid, name, "Sim" if info["has_voted"] else "Não", info["registered_at"]))

    def _refresh_results(self):
        for i in self.tree_results.get_children():
            self.tree_results.delete(i)
        items, blank, null, total = self.state_obj.results()
        self.lbl_total.config(text=f"Total de votos: {total}")
        for it in items:
            self.tree_results.insert("", tk.END, values=(it["number"], it["name"], it["party"], it["votes"], f"{it['percent']:.2f}%"))
        self.lbl_blank.config(text=f"BRANCO: {blank['votes']} ({blank['percent']:.2f}%)")
        self.lbl_null.config(text=f"NULO: {null['votes']} ({null['percent']:.2f}%)")

    def _refresh_all(self):
        # config
        self.entry_name.delete(0, tk.END)
        self.entry_name.insert(0, self.state_obj.data["meta"]["name"])
        self.auto_var.set(self.state_obj.data["meta"]["auto_register_voter"])
        # tables
        self._refresh_candidates()
        self._refresh_voters()
        self._refresh_results()


# ------------------------------ Main Voting Window ------------------------------
class UrnaGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Urna Eletrônica")
        self.state_obj = ElectionState()
        self.state_obj.load()

        self.photo_cache = None
        self._build_header()
        self._build_voting_screen()
        self._go_fullscreen_best_effort()
        self._refresh_header()
        self._update_candidate_preview(clear_all=True)

    # Fullscreen & window management
    def _go_fullscreen_best_effort(self):
        try:
            if os.name == "nt":
                self.state("zoomed")  # Windows
            else:
                # Linux/Mac fallback: maximize geometry
                self.update_idletasks()
                self.attributes("-zoomed", True)
        except Exception:
            # Fallback: full screen
            try:
                self.attributes("-fullscreen", True)
                # ESC para sair do fullscreen (se necessário)
                self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))
            except Exception:
                # último recurso
                self.geometry("1280x800")

    # Header (title + status + admin button)
    def _build_header(self):
        frm = ttk.Frame(self)
        frm.pack(fill=tk.X, padx=12, pady=8)

        self.lbl_title = ttk.Label(frm, text=self.state_obj.data['meta']['name'], font=("Arial", 20, "bold"))
        self.lbl_title.pack(side=tk.LEFT)

        self.lbl_status = ttk.Label(frm, text="", foreground="blue", font=("Arial", 12, "bold"))
        self.lbl_status.pack(side=tk.LEFT, padx=16)

        ttk.Button(frm, text="Painel do Administrador", command=self._open_admin_panel).pack(side=tk.RIGHT, padx=8)

    # Voting screen only
    def _build_voting_screen(self):
        f = ttk.Frame(self)
        f.pack(fill=tk.BOTH, expand=True, padx=16, pady=12)

        top = ttk.Frame(f)
        top.pack(fill=tk.X)
        self.lbl_voting_status = ttk.Label(top, text="", font=("Arial", 14, "bold"))
        self.lbl_voting_status.pack(side=tk.LEFT, padx=4, pady=6)

        # layout: left (input + keypad), right (candidate card)
        container = ttk.Frame(f)
        container.pack(fill=tk.BOTH, expand=True, pady=10)

        # LEFT
        left = ttk.Frame(container)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        voter_box = ttk.LabelFrame(left, text="Identificação do Eleitor")
        voter_box.pack(fill=tk.X, pady=8)
        ttk.Label(voter_box, text="ID do eleitor:").pack(side=tk.LEFT, padx=5, pady=5)
        self.ent_vote_vid = ttk.Entry(voter_box, width=28, font=("Arial", 14))
        self.ent_vote_vid.pack(side=tk.LEFT, padx=5, pady=5)

        display = ttk.LabelFrame(left, text="Número do candidato")
        display.pack(fill=tk.X, pady=8)
        self.var_number = tk.StringVar(value="")
        self.lbl_number = ttk.Entry(display, textvariable=self.var_number, font=("Courier New", 28, "bold"), width=14, justify="center")
        self.lbl_number.pack(padx=10, pady=10)

        keypad = ttk.LabelFrame(left, text="Teclado")
        keypad.pack(fill=tk.BOTH, expand=True, pady=8)

        def mkbtn(txt, cmd, r, c):
            b = ttk.Button(keypad, text=txt, command=cmd)
            b.grid(row=r, column=c, padx=8, pady=8, sticky="nsew")
            keypad.grid_columnconfigure(c, weight=1)

        for i in range(1, 10):
            r = (i-1)//3
            c = (i-1)%3
            mkbtn(str(i), lambda d=i: self._k_digit(str(d)), r, c)
        mkbtn("0", lambda: self._k_digit("0"), 3, 1)

        mkbtn("BRANCO", self._k_branco, 4, 0)
        mkbtn("CORRIGE", self._k_corrige, 4, 1)
        mkbtn("CONFIRMA", self._k_confirma, 4, 2)

        # RIGHT
        right = ttk.LabelFrame(container, text="Candidato selecionado")
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.lbl_cand_photo = ttk.Label(right, text="Sem imagem", anchor="center")
        self.lbl_cand_photo.pack(pady=12)

        self.lbl_cand_name = ttk.Label(right, text="Nome: —", font=("Arial", 14, "bold"))
        self.lbl_cand_party = ttk.Label(right, text="Partido: —", font=("Arial", 13))
        self.lbl_cand_num = ttk.Label(right, text="Número: —", font=("Arial", 13))
        self.lbl_cand_name.pack(anchor="w", padx=10, pady=4)
        self.lbl_cand_party.pack(anchor="w", padx=10, pady=2)
        self.lbl_cand_num.pack(anchor="w", padx=10, pady=2)

        self.lbl_vote_result = ttk.Label(f, text="", foreground="green", font=("Arial", 12, "bold"))
        self.lbl_vote_result.pack(pady=6)

    # ---------------- Voting handlers ----------------
    def _k_digit(self, d):
        s = self.var_number.get() + d
        if len(s) > 5:
            return
        self.var_number.set(s)
        self._update_candidate_preview()

    def _k_corrige(self):
        self.var_number.set("")
        self._update_candidate_preview()

    def _k_branco(self):
        self.var_number.set("0")
        self._update_candidate_preview(called_by_branco=True)

    def _k_confirma(self):
        voter_id = self.ent_vote_vid.get().strip()
        num = self.var_number.get().strip()
        if not voter_id:
            messagebox.showwarning("Atenção", "Informe o ID do eleitor.")
            return

        if num == "0":
            msg = "Voto em BRANCO. Confirmar?"
        elif num in self.state_obj.list_candidates():
            ci = self.state_obj.list_candidates()[num]
            msg = f"Você escolheu: {num} - {ci['name']} ({ci.get('party','')}). Confirmar?"
        else:
            msg = "Número inexistente. Se prosseguir, será NULO. Confirmar?"

        if not messagebox.askyesno("Confirmar voto", msg):
            self.lbl_vote_result.config(text="Voto cancelado.", foreground="orange")
            return

        try:
            res = self.state_obj.cast_vote(voter_id, num if num else "X")
            self.lbl_vote_result.config(text=f"Voto COMPUTADO: {res}.", foreground="green")
            # Limpa tudo para o próximo eleitor
            self.ent_vote_vid.delete(0, tk.END)
            self.var_number.set("")
            self._update_candidate_preview(clear_all=True)
            # foco no ID
            self.ent_vote_vid.focus_set()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def _update_candidate_preview(self, called_by_branco=False, clear_all=False):
        if clear_all:
            self.lbl_cand_name.config(text="Nome: —")
            self.lbl_cand_party.config(text="Partido: —")
            self.lbl_cand_num.config(text="Número: —")
            self.lbl_cand_photo.config(image="", text="Sem imagem")
            self.photo_cache = None
            # atualizar status/header
            self._refresh_header()
            return

        num = self.var_number.get().strip()
        if called_by_branco or num == "0":
            self.lbl_cand_name.config(text="Nome: — (BRANCO)")
            self.lbl_cand_party.config(text="Partido: —")
            self.lbl_cand_num.config(text="Número: 0")
            self.lbl_cand_photo.config(image="", text="Sem imagem")
            self.photo_cache = None
            return

        cands = self.state_obj.list_candidates()
        if num in cands:
            info = cands[num]
            self.lbl_cand_name.config(text=f"Nome: {info['name']}")
            self.lbl_cand_party.config(text=f"Partido: {info.get('party','')}")
            self.lbl_cand_num.config(text=f"Número: {num}")
            img, err = load_image(info.get("image", ""))
            if img:
                self.photo_cache = img
                self.lbl_cand_photo.config(image=img, text="")
            else:
                self.photo_cache = None
                self.lbl_cand_photo.config(image="", text=err or "Sem imagem")
        else:
            self.lbl_cand_name.config(text="Nome: — (NÚMERO INVÁLIDO)")
            self.lbl_cand_party.config(text="Partido: —")
            self.lbl_cand_num.config(text=f"Número: {num if num else '—'}")
            self.lbl_cand_photo.config(image="", text="Sem imagem")
            self.photo_cache = None

    # Header refresh
    def _refresh_header(self):
        self.lbl_title.config(text=self.state_obj.data['meta']['name'])
        status = f"Status: {'ABERTA' if self.state_obj.is_open else 'FECHADA'} | Auto-cadastro: {'ON' if self.state_obj.data['meta']['auto_register_voter'] else 'OFF'}"
        self.lbl_status.config(text=status)
        self.lbl_voting_status.config(text=f"Eleição {'ABERTA' if self.state_obj.is_open else 'FECHADA'}")

    # Admin panel open (PIN-gated)
    def _open_admin_panel(self):
        pin = simpledialog.askstring("PIN", "PIN do administrador:", show="*")
        if pin is None:
            return
        if not self.state_obj.verify_admin_pin(pin):
            messagebox.showerror("Erro", "PIN inválido.")
            return

        def on_state_changed():
            # quando algo é alterado no painel, refletir na tela principal
            self._refresh_header()
            # manter preview consistente
            self._update_candidate_preview()

        AdminPanel(self, self.state_obj, on_state_changed=on_state_changed)

def main():
    app = UrnaGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
