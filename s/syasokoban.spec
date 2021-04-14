%undefine _debugsource_packages

Name:    syasokoban
Version: 2.0.1
Release: 10.1
Source0: %{name}-%{version}.tar.gz
Source1:    %{name}.desktop  
Source2:    %{name}.png
Patch1:     %{name}-gcc43.patch
Patch2:     %{name}-iconsdir.patch
Summary:    Still Yet Another Sokoban
License:    GPLv2+
URL:        http://grayskygames.com/sokoban.html
Group:      Games/Puzzles 
BuildRequires: SDL-devel

%description
An implementation of the popular Sokoban puzzle game. 
The goal is to push the crates onto the designated squares without
getting stuck.

%prep
%setup -q
%patch1 -p1 
%patch2 -p1
sed -i '13i #include <unistd.h>' src/Main.cpp

%build
make DATADIR=%{_datadir}/%{name}/data/

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p %{buildroot}/%_datadir/pixmaps
install -m 644 %SOURCE2 %{buildroot}/%_datadir/pixmaps
cp -rf $RPM_BUILD_DIR/%{name}-%{version}/data $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 %SOURCE1 $RPM_BUILD_ROOT%{_datadir}/applications/
make install BINDIR=$RPM_BUILD_ROOT%{_bindir}

%files
%attr(755, root, root) %{_bindir}/syasokoban
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon May 16 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.1
- Rebuilt for Fedora
* Sat May 01 2010 Andre Guerreiro <andre.guerreiro@caixamagica.pt>
+ First Caixa Magica Package, no localization


