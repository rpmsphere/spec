%undefine _debugsource_packages
%define		oname MotoGT

Name:		motogt
Version:	20110505
Release:	15.1
Summary:	A free motorcycle racing game
License:	GPLv2+
Group:		Games/Arcade
URL:		http://motogt.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/motogt/%{oname}-%{version}.zip
Source2:	motogt.desktop
Source3:	MotoGT.png
Patch0:		motogt-makefile.patch
Patch1:		motogt-savedir.patch
Patch2:		motogt-init.patch
Patch3:		motogt-png15.patch
BuildRequires:	compat-SFML16-devel
BuildRequires:	libpng-devel
BuildRequires:	libpng10-devel
BuildRequires:	pkgconfig(glu)

%description
MotoGT is 2D top-viewed game where you drive a MotoGP bike, and you want
to win races. In career mode you start with a regular bike, but when you
win races you get experience, and experience let's you improve your bike.
If you win championships, you can also unlock hidden features.

%prep
%setup -q -n %{oname}
%patch0 -p1 -b .makefile~
%patch1 -p1 -b .savedir~
%patch2 -p1 -b .init~
%patch3 -p1 -b .png15~
sed -i 's|sfml-\([a-z]*\)|sfml-\1-1.6|g' src/Makefile.lnx
mv data data_hi ; sed -i 's|data|data_hi|g' src/* ; sed -i 's|data_hi_low|data_low|' src/global.cpp

sed -i 's|png.h|libpng10/png.h|' data_hi/src/bikes/hue.cpp
g++ data_hi/src/bikes/hue.cpp -lpng10 -o data_hi/src/bikes/hue.bin

%build
#setup_compile_flags
export CFLAGS="-I/usr/include/sfml1 -fPIE"
make

%install
mkdir -p %{buildroot}%{_libdir}/%{oname}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -Dm 755 %{oname}.bin -D %{buildroot}%{_libdir}/%{oname}
install -Dm 644 %{SOURCE2} -D %{buildroot}%{_datadir}/applications
install -Dm 644 %{SOURCE3} -D %{buildroot}%{_datadir}/pixmaps
cp -rf data_hi %{buildroot}%{_libdir}/%{oname}
cp -rf data_low %{buildroot}%{_libdir}/%{oname}
cp -rf doc %{buildroot}%{_libdir}/%{oname}

mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash
cd %{_libdir}/%{oname}
exec ./%{oname}.bin
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_libdir}/%{oname}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{oname}.png

%changelog
* Thu Jun 16 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20110505
- Rebuilt for Fedora
* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 20110505-5
+ Revision: 70fde03
- MassBuild#464: Increase release tag
