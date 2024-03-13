uses crt;
var
    X, r, S : real;
    a, b, c, d, e : integer;
begin
clrscr;
    WriteLn('Nama = Galen Alfakhriy Berno');
    WriteLn('NIM  = 2210433048');
    Writeln;
    WriteLn('Input Nilai');
    ReadLn(a);
    ReadLn(b);
    ReadLn(c);
    ReadLn(d);
    ReadLn(e);
    Writeln;
    X := (a + b + c + d + e) / 5;
    WriteLn('Rata - Rata    = ',X:10:2);
    r := (sqr(a - X) + sqr(b - X) + sqr(c - X) + sqr(d - X) + sqr(e - X)) / 5;
    WriteLn('Ragam          = ',r:10:2);
    S := Sqrt(r);
    WriteLn('Simpangan Baku = ',S:10:2);
readln;
end.
