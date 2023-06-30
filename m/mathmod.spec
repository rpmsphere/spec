Name:          mathmod
Version:       11.1
Release:       1
Summary:       A program which generate 3D and 4D surfaces
Group:         Sciences/Mathematics
URL:           https://sourceforge.net/projects/mathmod
Source0:       https://sourceforge.net/projects/mathmod/files/MathMod-%{version}/%{name}-%{version}-source.zip
Source1:       %{name}.1
License:       GPLv2
BuildRequires: qt5-qtbase-devel
Provides:      k3dsurf = %{version}

%description
MathMod is a mathematical modeling software that visualize and
animate implicit and parametric surfaces. MathMod supports:
* 3D and 4D plotting and animation
* OBJ output file format
* Scripting language compatible with JSON
* Large set of scripted examples

%prep
%setup -q

%build
%qmake_qt5
make

%install
install -D -m755 MathMod %{buildroot}%{_bindir}/%{name}
install -D -m644 images/win/ico.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -m644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1

# Create the system menu entry
%{__mkdir_p}  %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=MathMod
GenericName=3D and 4D surfaces generation
GenericName[it]=Grafici di funzioni 3D e 4D
GenericName[ru]=Генерация 3D и 4D поверхностей
Comment=Tool for mathematical surfaces
Comment[af]=Hulpmiddel vir wiskundige oppervlakke
Comment[sq]=Mjet për sipërfaqet matematike
Comment[ast]=Preséu pa superficies matemátiques
Comment[be]=Прылада для працы з матэматычнымі паверхнямі
Comment[bn]=গাণিতিক পৃষ্ঠতলের জন্য টুল
Comment[bs]=Alat za matematičke površine
Comment[pt_BR]=Ferramenta para superfícies matemáticas
Comment[bg]=Инструмент за математически повърхнини
Comment[ca]=Eina per a superfícies matemàtiques
Comment[ca@valencia]=Eina per a superfícies matemàtiques
Comment[crh]=Matematiksel yüzeyler için bir araç
Comment[zh_CN]=数学曲面工具
Comment[da]=Værktøj til matematiske overflader
Comment[cs]=Nástroj pro zobrazení matematického prostoru
Comment[nl]=Programma voor wiskundige oppervlaktes
Comment[fi]=Matemaattisten pintojen työkalu
Comment[fr]=Outil pour les surfaces mathématiques
Comment[gl]=Ferramenta para superficies matemáticas
Comment[de]=Werkzeug für mathematische Oberflächen
Comment[gd]=Inneal son uachdaran matamataig
Comment[el]=Εργαλείο για μαθηματικές επιφάνειες
Comment[hu]=Eszköz matematikai felületekhez
Comment[it]=Strumento per superfici matematiche
Comment[ja]=数学的な曲面ツール
Comment[ky]=Математикалык тегиздиктер менен иштөө үчүн шайман
Comment[lt]=Įrankis matematiniams paviršiams
Comment[ms]=Alat untuk permukaan matematik
Comment[oc]=Aisina per las susfàcias matematicas
Comment[nb]=Verktøy for matematiske overflater
Comment[pl]=Przekształcanie i wizualizacja wielowymiarowych powierzchni za pomocą matematycznych przekształceń
Comment[pt]=Ferramenta para superfícies matemáticas
Comment[ru]=Инструмент для работы с математическими поверхностями
Comment[ro]=Unealtă pentru suprafețe matematice
Comment[sk]=Nástroj na matematické povrchy
Comment[sl]=Orodje za matematične površine
Comment[sv]=Verktyg för matematiska ytor
Comment[es]=Herramienta para superficies matemáticas
Comment[tr]=Matematiksel yüzeyler için bir araç
Comment[uk]=Інструмент для роботи з математичними поверхнями
Comment[vi]=Công cụ bề mặt toán học
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Education;Science;Math;
EOF

%files
%doc *.txt documentation/*.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.*

%changelog
* Sun Oct 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 11.1
- Rebuilt for Fedora
* Tue Nov 10 2015 alexl <alexl> 3.1-1.mga6
+ Revision: 901433
- version 3.1
- add man page
- use icon from sources instead of separated source
- qt5 build
- del Encoding field from desktop file
* Wed Oct 15 2014 umeabot <umeabot> 1.0-0.svn20140414.5.mga5
+ Revision: 741678
- Second Mageia 5 Mass Rebuild
* Sun Sep 28 2014 alexl <alexl> 1.0-0.svn20140414.4.mga5
+ Revision: 731488
- added Provides: k3dsurf
* Tue Sep 16 2014 umeabot <umeabot> 1.0-0.svn20140414.3.mga5
+ Revision: 682209
- Mageia 5 Mass Rebuild
* Tue Aug 05 2014 alexl <alexl> 1.0-0.svn20140413.3.mga5
+ Revision: 660030
- added new Comment for desktop file and translated it
* Mon Jul 21 2014 alexl <alexl> 1.0-0.svn20140413.2.mga5
+ Revision: 654986
- fixed desktop file
* Mon May 19 2014 alexl <alexl> 1.0-0.svn20140413.1.mga5
+ Revision: 623711
- imported package mathmod
