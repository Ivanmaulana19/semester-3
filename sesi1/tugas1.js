const prompt = require('prompt-sync')();
// Minta input nilai dari pengguna
let matematika = parseFloat(prompt("Masukan nilai Matematika: "));
let bahasainggris = parseFloat(prompt("masukan nilai Bahasa Inggris: "));
let ipa = parseFloat(prompt("Masukan nilai IPA: "));

// Hitung rata-rata
let nilaiRataRata = (matematika + bahasainggris + ipa) / 3;

console.log("Nilai Rata-Rata:", nilaiRataRata);

//tentukan status kelulusan
if (nilaiRatarata >= 80) {
    console.log("Status Kelulusan: Lulus");
} else {
    console.log("Status Kelulusan: Tidak Lulus");
}