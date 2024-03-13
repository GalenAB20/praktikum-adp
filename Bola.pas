uses crt;
var
    r : integer;
    Luas, Volume : real;
begin
clrscr;
    WriteLn('Nama = Galen Alfakhriy Berno');
    WriteLn('NIM = 2210433048');
    Writeln;
    Write('Masukan nilai jari-jari = ');
    ReadLn(r);
    Writeln;
    Luas := 4 * Pi * r * r;
    WriteLn('Luas Permukaan Bola = ',Luas:10:2);
    Volume := 4 / 3 * Pi * r * r * r;
    WriteLn('Volume Bola = ',Volume:10:2);
readln;
end.
