%global _name yoda_soccer

Summary:        Yoda Soccer is a project which intends to create a new free game for Windows with the gameplay and the style of the well known Sensible World of Soccer (a.k.a. SWOS). 
Name:           yodasoccer
Version:        0.7.7
Release:        1.bin
License:        GPL
Group:          Amusements/Games
Source0:        http://nchc.dl.sourceforge.net/sourceforge/yodasoccer/%{_name}_077_lin.tar.gz
Source1:        %{name}.desktop
Source2:	%{name}.png
URL:            http://yodasoccer.sourceforge.net/
BuildRequires:	mesa-libGL-devel libX11-devel mesa-libGLU-devel

%description
Started on June 2002, Yoda Soccer is a project which intends to create a new
free game for Windows with the gameplay and the style of the well known
Sensible World of Soccer (a.k.a. SWOS). This doesn't mean that we'll redo swos
for this OS, it would be only a waste of time, but we'll try to add many
features missed in Swos. If you want to know more about this, please go in the
Info section. Yoda soccer is written in Blitzmax (www.blitzmax.com) language.

%prep
%setup -q -c %{_name}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cd %{_name}_077
cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}/

#desktop and icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

#exec
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} <<EOF
cd /usr/share/yodasoccer
./yodasoccer
EOF

chmod 755 %{buildroot}%{_bindir}/%{name}
%clean

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.7
- Rebuilt for Fedora
* Tue Nov 04 2008 Feather Mountain <john@ossii.com.tw> - 0.7.3-1.ossii
- Build for M6(OSSII)
