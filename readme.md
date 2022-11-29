

<h1 align="center">
Tugas Besar 2 IF3110
  <br>
</h1>

<h4 align="center">Simulasi Protokol Serial Optimistic Concurrency Control</h4>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#installations">installations</a> •
  <a href="#executing">Executing</a> •
  <a href="#credits">Credits</a> •
  <a href="#footnote">Footnote</a> 
</p>

## Description
Program yang dibuat untuk penyelesaian tugas besar 2 IF3140. Program ini akan mensimulasikan protokol Optimistic Concurrency Control dan menentukan apakah sebuah schedule serializable atau terdapat konflik.

## Requirements
- Python (atleast  3.8)

## Installations
### Installing program
```bash
git clone https://github.com/Noxira/OCC.git
cd OCC
```

## Executing
### running the program
```bash
py occ.py <input.txt>
```
### example input
```txt
R1(X)
W1(X)
W2(Y)
W3(Y)
W1(Y)
C1
C2
C3
```

## Screenshots
![enter image description here](https://media.discordapp.net/attachments/893484082275708980/1047153698712854548/image.png)
![enter image description here](https://media.discordapp.net/attachments/893484082275708980/1047153682258600026/image.png)
![enter image description here](https://media.discordapp.net/attachments/893484082275708980/1047153672687190077/image.png)
![enter image description here](https://media.discordapp.net/attachments/893484082275708980/1047153661400326194/image.png)

## Credits
<table>
    <tr>
      <td><b>Nama</b></td>
      <td><b>NIM</b></td>
    </tr>
    <tr>
      <td><b>Farrel Farandieka Fibriyanto</b></td>
      <td><b>13520054</b></td>
    </tr>
        <tr>
      <td><b>Putri Nurhaliza</b></td>
      <td><b>13520066</b></td>
       </tr>
        <tr>
      <td><b>Grace Claudia</b></td>
      <td><b>13520078</b></td>
    </tr>
        <tr>
      <td><b>Aloysius Gilang Pramudya</b></td>
      <td><b>13520147</b></td>
    </tr>
</table>

## Footnote
Program dibuat dengan referensi Salindia Perkuliahan IF3140 Tahun Ajaran 2022/2023